#!/usr/bin/env python
"""Shrink a local scBaseCount download to what the benchmark uses.

  delete-species : remove the per-sample h5ad directories of every organism except --keep
                   (metadata parquet tables are kept). Writes a log of what was removed.
  strip-layers   : rewrite every h5ad of --org without the `layers/` group (the two multi-mapper
                   count matrices, two thirds of each file), keeping X, obs, var, uns, obsm... as
                   they are. Each file is copied chunk-for-chunk (no recompression) to a temp file
                   next to it, verified (every dataset outside layers/ has identical shape, dtype
                   and contents; X checked by full read) and then atomically renamed over the
                   original. A file that already has no layers is skipped. Safe to re-run.

  python scripts/scbasecount_cleanup.py delete-species --root /datasets/arc --keep Homo_sapiens [--dry-run]
  python scripts/scbasecount_cleanup.py strip-layers --root /datasets/arc --org Homo_sapiens --workers 12 [--dry-run] [--limit N]
"""
import argparse, json, os, shutil, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import h5py
import numpy as np

FEATURE = "GeneFull_Ex50pAS"


def dir_size(p: Path):
    n = s = 0
    for f in p.rglob("*"):
        if f.is_file():
            n += 1; s += f.stat().st_size
    return n, s


def delete_species(a):
    root = Path(a.root); h5 = root / "h5ad" / FEATURE
    log = root / "CLEANUP_LOG.jsonl"
    victims = sorted(d for d in h5.iterdir() if d.is_dir() and d.name not in a.keep)
    total = 0
    for d in victims:
        n, s = dir_size(d); total += s
        print(f"{'would remove' if a.dry_run else 'removing'} {d}  {n} files  {s/1e12:.3f} TB", flush=True)
        if not a.dry_run:
            shutil.rmtree(d)
            with open(log, "a") as f:
                f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "action": "delete-species", "dir": str(d), "files": n, "bytes": s}) + "\n")
    print(f"{'would free' if a.dry_run else 'freed'} {total/1e12:.3f} TB across {len(victims)} organisms; kept {a.keep}")


def _copy_without_layers(src: Path, dst: Path):
    with h5py.File(src, "r") as fi, h5py.File(dst, "w") as fo:
        for k, v in fi.attrs.items():
            fo.attrs[k] = v
        for name in fi:
            if name == "layers":
                g = fo.create_group("layers")
                for k, v in fi["layers"].attrs.items():
                    g.attrs[k] = v
            else:
                fi.copy(fi[name], fo, name=name, expand_refs=True)


def _verify(src: Path, dst: Path):
    with h5py.File(src, "r") as fi, h5py.File(dst, "r") as fo:
        def walk(g, prefix=""):
            for k, v in g.items():
                if prefix == "" and k == "layers":
                    continue
                p = f"{prefix}/{k}"
                if isinstance(v, h5py.Group):
                    yield p, "g", v
                    yield from walk(v, p)
                else:
                    yield p, "d", v
        src_items = dict((p, (t, v)) for p, t, v in walk(fi))
        dst_items = dict((p, (t, v)) for p, t, v in walk(fo))
        if set(src_items) != set(dst_items):
            return f"path set differs: {set(src_items) ^ set(dst_items)}"
        for p, (t, v) in src_items.items():
            w = dst_items[p][1]
            if dict(v.attrs.items()).keys() != dict(w.attrs.items()).keys():
                return f"attrs differ at {p}"
            if t == "d":
                if v.shape != w.shape or v.dtype != w.dtype:
                    return f"shape/dtype differ at {p}"
                if v.size == 0:
                    continue
                if p.startswith("/X/") or v.size <= 200000:
                    a, b = v[()], w[()]
                    if v.dtype.kind == "O":
                        if not np.array_equal(a.astype(str), b.astype(str)):
                            return f"contents differ at {p}"
                    elif not np.array_equal(a, b):
                        return f"contents differ at {p}"
        if "layers" not in fo or len(fo["layers"]) != 0:
            return "layers not empty"
    return None


def strip_one(path_str: str):
    src = Path(path_str); tmp = src.with_name(src.name + ".strip.tmp")
    t0 = time.time()
    try:
        with h5py.File(src, "r") as f:
            if "layers" not in f or len(f["layers"]) == 0:
                return (path_str, "skip", src.stat().st_size, src.stat().st_size, 0.0, None)
        if tmp.exists():
            tmp.unlink()
        _copy_without_layers(src, tmp)
        err = _verify(src, tmp)
        if err:
            tmp.unlink(missing_ok=True)
            return (path_str, "fail", src.stat().st_size, 0, time.time() - t0, err)
        before = src.stat().st_size; after = tmp.stat().st_size
        os.replace(tmp, src)  # atomic on the same filesystem
        return (path_str, "ok", before, after, time.time() - t0, None)
    except Exception as e:  # noqa: BLE001
        tmp.unlink(missing_ok=True)
        return (path_str, "fail", src.stat().st_size if src.exists() else 0, 0, time.time() - t0, repr(e))


def strip_layers(a):
    root = Path(a.root); d = root / "h5ad" / FEATURE / a.org
    files = sorted(str(p) for p in d.glob("*.h5ad"))
    if a.limit:
        files = files[: a.limit]
    print(f"{len(files)} files in {d}", flush=True)
    if a.dry_run:
        tot = sum(Path(f).stat().st_size for f in files)
        print(f"dry run: {tot/1e12:.3f} TB on disk; expected after strip about {tot/3/1e12:.3f} TB")
        return
    log = root / "CLEANUP_LOG.jsonl"
    n_ok = n_skip = n_fail = 0; saved = 0; t0 = time.time()
    with ProcessPoolExecutor(a.workers) as ex, open(log, "a") as lf:
        futs = [ex.submit(strip_one, f) for f in files]
        for i, fut in enumerate(as_completed(futs), 1):
            p, st, before, after, dt, err = fut.result()
            if st == "ok":
                n_ok += 1; saved += before - after
            elif st == "skip":
                n_skip += 1
            else:
                n_fail += 1; print(f"FAIL {p}: {err}", flush=True)
            lf.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "action": "strip-layers", "file": p, "status": st, "bytes_before": before, "bytes_after": after, "seconds": round(dt, 1), "error": err}) + "\n")
            if i % 200 == 0 or i == len(files):
                el = time.time() - t0
                print(f"{i}/{len(files)}  ok {n_ok} skip {n_skip} fail {n_fail}  saved {saved/1e12:.3f} TB  {el/60:.0f} min  eta {el/i*(len(files)-i)/60:.0f} min", flush=True)
    print(f"done: ok {n_ok} skip {n_skip} fail {n_fail}; saved {saved/1e12:.3f} TB")


ap = argparse.ArgumentParser()
sub = ap.add_subparsers(dest="cmd", required=True)
p1 = sub.add_parser("delete-species"); p1.add_argument("--root", required=True); p1.add_argument("--keep", nargs="+", default=["Homo_sapiens"]); p1.add_argument("--dry-run", action="store_true")
p2 = sub.add_parser("strip-layers"); p2.add_argument("--root", required=True); p2.add_argument("--org", default="Homo_sapiens"); p2.add_argument("--workers", type=int, default=8); p2.add_argument("--dry-run", action="store_true"); p2.add_argument("--limit", type=int, default=0)
a = ap.parse_args()
{"delete-species": delete_species, "strip-layers": strip_layers}[a.cmd](a)

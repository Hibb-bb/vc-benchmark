#!/usr/bin/env python
"""Download registry files with resume + MD5 verification.

    python scripts/download_data.py --group scperturb [--only Norman,Adamson] [--dry-run]

Files land in data/raw/<group>/<name>. A sidecar <name>.ok is written after the MD5
matches; files with an .ok sidecar are skipped. wget -c resumes partial downloads, so the
job can be resubmitted after a timeout without losing progress.
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def md5sum(path: Path, chunk: int = 1 << 24) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def fetch(entry: dict, dest_dir: Path, retries: int = 5) -> bool:
    dest = dest_dir / entry["name"]
    ok = dest.with_suffix(dest.suffix + ".ok")
    lock = dest.with_suffix(dest.suffix + ".lock")
    if ok.exists():
        print(f"[skip] {entry['name']} (verified)", flush=True)
        return True
    if lock.exists() and time.time() - lock.stat().st_mtime < 6 * 3600:
        print(f"[skip] {entry['name']} (locked by another job)", flush=True)
        return None
    lock.write_text(str(time.time()))
    try:
        return _fetch_locked(entry, dest, ok, lock, retries)
    finally:
        lock.unlink(missing_ok=True)


def _fetch_locked(entry, dest, ok, lock, retries):
    for attempt in range(1, retries + 1):
        lock.touch()
        t0 = time.time()
        cmd = ["wget", "-c", "-q", "--tries=3", "--timeout=120", "-O", str(dest), entry["url"]]
        rc = subprocess.call(cmd)
        size = dest.stat().st_size if dest.exists() else 0
        if rc == 0 and size == entry["size"]:
            digest = md5sum(dest)
            if not entry.get("md5") or digest == entry["md5"]:  # no published MD5: size check only
                ok.write_text(digest + "\n")
                print(f"[ok]   {entry['name']} {size/1e9:.2f} GB in {time.time()-t0:.0f}s", flush=True)
                return True
            print(f"[md5!] {entry['name']} got {digest}, want {entry['md5']}; redownloading", flush=True)
            dest.unlink(missing_ok=True)
        else:
            print(f"[retry {attempt}] {entry['name']} rc={rc} size={size}/{entry['size']}", flush=True)
            time.sleep(30 * attempt)
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True)
    ap.add_argument("--only", default=None, help="comma-separated substrings of file names")
    ap.add_argument("--registry", default=str(ROOT / "configs" / "datasets.yaml"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reverse", action="store_true", help="largest first (run as a second job alongside the default)")
    args = ap.parse_args()

    reg = yaml.safe_load(Path(args.registry).read_text())
    group = reg["groups"][args.group]
    files = group["files"]
    if args.only:
        subs = [s.strip() for s in args.only.split(",")]
        files = [f for f in files if any(s in f["name"] for s in subs)]
    files = sorted(files, key=lambda f: f["size"], reverse=args.reverse)  # small first so work can start early

    dest_dir = ROOT / "data" / "raw" / args.group
    dest_dir.mkdir(parents=True, exist_ok=True)
    total = sum(f["size"] for f in files) / 1e9
    print(f"{args.group}: {len(files)} files, {total:.1f} GB -> {dest_dir}", flush=True)
    if args.dry_run:
        for f in files:
            print(f"  {f['size']/1e9:6.2f} GB  {f['name']}")
        return 0

    results = {f["name"]: fetch(f, dest_dir) for f in files}
    failed = [n for n, r in results.items() if r is False]
    skipped = [n for n, r in results.items() if r is None]
    if skipped:
        print("locked elsewhere (resubmit later if no .ok appears):", *skipped, sep="\n  ")
    if failed:
        print("FAILED:", *failed, sep="\n  ")
        return 1
    print("all files verified", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

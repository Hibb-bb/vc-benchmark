#!/usr/bin/env python
"""Parallel byte-range download for large single files (S3 and most CDNs support Range).

  python scripts/parallel_download.py URL DEST [--threads 16] [--part-mb 256]

Resumable: finished parts are recorded in DEST.parts; rerun to continue. The file is
preallocated and parts are written in place, so no concatenation step is needed.
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("dest")
ap.add_argument("--threads", type=int, default=16)
ap.add_argument("--part-mb", type=int, default=256)
a = ap.parse_args()
dest = Path(a.dest); state = Path(a.dest + ".parts")

req = urllib.request.Request(a.url, method="HEAD")
with urllib.request.urlopen(req) as r:
    total = int(r.headers["Content-Length"]); accept = r.headers.get("Accept-Ranges", "")
print(f"size {total/1e9:.2f} GB, accept-ranges={accept}", flush=True)
part = a.part_mb * 1024 * 1024
parts = [(i, s, min(s + part, total) - 1) for i, s in enumerate(range(0, total, part))]
done = set(json.load(open(state))) if state.exists() else set()
if not dest.exists() or dest.stat().st_size != total:
    with open(dest, "wb") as f:
        f.truncate(total)
    done = set()
print(f"{len(parts)} parts of {a.part_mb} MB; {len(done)} already done", flush=True)
t0 = time.time(); got = [0]


def fetch(p):
    i, s, e = p
    for attempt in range(6):
        try:
            rq = urllib.request.Request(a.url, headers={"Range": f"bytes={s}-{e}"})
            with urllib.request.urlopen(rq, timeout=120) as r, open(dest, "r+b") as f:
                f.seek(s)
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
            return i
        except Exception as ex:  # noqa
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"part {i} failed")


todo = [p for p in parts if p[0] not in done]
with ThreadPoolExecutor(a.threads) as ex:
    futs = {ex.submit(fetch, p): p for p in todo}
    for k, fut in enumerate(as_completed(futs)):
        i = fut.result(); done.add(i)
        if k % 10 == 0 or k == len(todo) - 1:
            json.dump(sorted(done), open(state, "w"))
            el = time.time() - t0
            print(f"  {len(done)}/{len(parts)} parts  {len(done)*part/1e9:.1f} GB  {len(done)*part/1e6/max(el,1):.0f} MB/s", flush=True)
json.dump(sorted(done), open(state, "w"))
print(f"done in {time.time()-t0:.0f}s", flush=True)

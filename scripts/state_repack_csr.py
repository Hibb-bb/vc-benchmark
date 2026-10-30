#!/usr/bin/env python
"""Rewrite the CSR X of an h5ad as contiguous (unchunked) datasets, in place.

  .venv/bin/python scripts/state_repack_csr.py cache/statetx_full/fold0/data/train.h5ad

STATE's data loader reads one cell (one CSR row, ~600 values) at a time, in random order. With chunked
datasets every row read pulls whole chunks (4 MB each at the builder's chunk size), so a training step of
32 x 512 cells moved ~128 GB and training never got past its first step. Contiguous datasets let h5py read
exactly the bytes of the row. The builder appends block by block, which needs chunked (resizable) datasets,
so it writes chunked first and this repacks at the end.
"""
import sys
import time

import h5py
import numpy as np

path = sys.argv[1]
t0 = time.time()
with h5py.File(path, "r+") as fh:
    g = fh["X"]
    for name in ("data", "indices", "indptr"):
        src = g[name]
        if src.chunks is None:
            print(f"{name}: already contiguous"); continue
        n, dt = src.shape[0], src.dtype
        tmp = g.create_dataset(name + "_contig", shape=(n,), dtype=dt, chunks=None)
        step = 1 << 27
        for i in range(0, n, step):
            tmp[i:i + step] = src[i:i + step]
        del g[name]
        g.move(name + "_contig", name)
        print(f"{name}: {n} values repacked contiguous ({time.time() - t0:.0f}s)", flush=True)
print(f"done in {time.time() - t0:.0f}s")

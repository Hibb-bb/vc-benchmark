#!/usr/bin/env python
"""Rewrite the CSR X of an h5ad as contiguous (unchunked) datasets.

  .venv/bin/python scripts/state_repack_csr.py cache/statetx_full/fold0/data/train.h5ad

STATE's data loader reads one cell (one CSR row, ~600 values) at a time, in random order. With chunked
datasets every row read pulls whole chunks (4 MB each at the builder's chunk size), so a training step of
32 x 512 cells moved ~128 GB and training never got past its first step. Contiguous datasets let h5py read
exactly the bytes of the row. The builder appends block by block, which needs chunked (resizable) datasets,
so it writes chunked first and this repacks at the end.

The repacked copy goes to a new file that then replaces the original: HDF5 does not give back the space of
deleted datasets, so repacking in place left a file twice the size of its contents (~74 GB for 37 GB).
"""
import os
import sys
import time

import h5py

path = sys.argv[1]
tmp_path = path + ".repack"
t0 = time.time()
with h5py.File(path, "r") as src, h5py.File(tmp_path, "w") as dst:
    for k, v in src.attrs.items():
        dst.attrs[k] = v
    for key in src:
        if key != "X":
            src.copy(src[key], dst, name=key)
    g, h = src["X"], dst.create_group("X")
    for k, v in g.attrs.items():
        h.attrs[k] = v
    for name in g:
        d = g[name]
        out = h.create_dataset(name, shape=d.shape, dtype=d.dtype, chunks=None)
        step = 1 << 27
        for i in range(0, d.shape[0], step):
            out[i:i + step] = d[i:i + step]
        print(f"{name}: {d.shape[0]} values written contiguous ({time.time() - t0:.0f}s)", flush=True)
os.replace(tmp_path, path)
print(f"done in {time.time() - t0:.0f}s: {os.path.getsize(path) / 1e9:.1f} GB")

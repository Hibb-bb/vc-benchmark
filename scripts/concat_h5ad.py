#!/usr/bin/env python
"""Concatenate many per-sample h5ad files (e.g. scBaseCount SRX files) into one h5ad that
`build_repr_panel_generic.py` can read.

  python scripts/concat_h5ad.py --glob 'data/raw/scbasecount/human/*.h5ad' --out data/raw/scbasecount/human_lung.h5ad \
      --sample-key srx_accession --meta sample_metadata.parquet --meta-key srx_accession \
      --meta-cols tissue,disease,perturbation,cell_line --per-file-cap 5000 --min-cells 200

* X must hold raw counts (integers); the script checks a sample and warns.
* --sample-key: obs column naming the sample; if the files lack it, the file stem is used.
* --meta joins sample-level columns (tissue, disease, ...) onto obs via --meta-key.
* --per-file-cap subsamples each file so a few hundred SRX files stay within memory; the panel
  builder caps per stratum anyway, so 2,000 to 5,000 cells per sample is plenty.
* Genes are intersected across files (inner join); files with fewer than --min-cells cells
  (after an optional --filter pandas query on obs) are skipped.
"""
import argparse
import glob
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

ap = argparse.ArgumentParser()
ap.add_argument("--glob", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--sample-key", default="srx_accession")
ap.add_argument("--meta", default=None, help="sample metadata parquet/csv")
ap.add_argument("--meta-key", default="srx_accession")
ap.add_argument("--meta-cols", default="tissue,disease,perturbation,cell_line,organism")
ap.add_argument("--per-file-cap", type=int, default=5000)
ap.add_argument("--min-cells", type=int, default=200)
ap.add_argument("--filter", default=None, help="pandas query on obs applied per file, e.g. \"cell_type.notna()\"")
ap.add_argument("--layer", default=None, help="use this layer as counts instead of X")
ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()

rng = np.random.default_rng(a.seed)
files = sorted(glob.glob(a.glob))
print(f"{len(files)} files", flush=True)
meta = None
if a.meta:
    meta = pd.read_parquet(a.meta) if a.meta.endswith(".parquet") else pd.read_csv(a.meta)
    cols = [c for c in a.meta_cols.split(",") if c in meta.columns]
    meta = meta.drop_duplicates(a.meta_key).set_index(a.meta_key)[cols]
    print(f"metadata: {len(meta)} samples, columns {cols}", flush=True)

parts, t0 = [], time.time()
for i, f in enumerate(files):
    x = ad.read_h5ad(f)
    if a.layer:
        x.X = x.layers[a.layer]
    x.layers.clear(); x.obsm.clear(); x.varm.clear(); x.uns.clear()
    if a.sample_key not in x.obs:
        x.obs[a.sample_key] = Path(f).stem
    if a.filter:
        x = x[x.obs.eval(a.filter).values].copy()
    if x.n_obs < a.min_cells:
        continue
    if x.n_obs > a.per_file_cap:
        x = x[np.sort(rng.choice(x.n_obs, a.per_file_cap, replace=False))].copy()
    x.X = sp.csr_matrix(x.X).astype(np.float32)
    x.obs_names = x.obs[a.sample_key].astype(str) + ":" + x.obs_names.astype(str)
    parts.append(x)
    if i % 20 == 0:
        print(f"  {i}/{len(files)}  {sum(p.n_obs for p in parts):,} cells  {time.time()-t0:.0f}s", flush=True)
assert parts, "no file passed the filters"
A = ad.concat(parts, join="inner", merge="first")
A.var_names_make_unique()
if meta is not None:
    A.obs = A.obs.join(meta, on=a.sample_key)
for c in A.obs.columns:
    if A.obs[c].dtype == object or str(A.obs[c].dtype) == "category":
        A.obs[c] = A.obs[c].astype(str)
s = A.X[: min(1000, A.n_obs)].data
if len(s) and not np.allclose(s, np.round(s)):
    print(f"WARNING: X does not look like raw integer counts (e.g. {s[:5]})", flush=True)
Path(a.out).parent.mkdir(parents=True, exist_ok=True)
A.write_h5ad(a.out)
print(f"wrote {a.out} {A.shape}; obs columns {list(A.obs.columns)}; {A.obs[a.sample_key].nunique()} samples; {time.time()-t0:.0f}s", flush=True)

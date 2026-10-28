#!/usr/bin/env python
"""Within-item split-half reliability of every Parse cytokine item, from the full 9.7M-cell file.

  .venv/bin/python scripts/parse_split_half.py [--seeds 3]       # run under Slurm (44 GB input)

For each item (cytokine x donor x cell type) the treated cells are split at random into two halves, and
so are the PBS control cells of the same donor and cell type. Each half gives its own shift
(mean log1p CP10k of treated half minus mean of control half, on the benchmark's 2,000 HVGs); the two
half-shifts are correlated (Pearson over genes), and the Spearman-Brown correction 2r / (1 + r) gives the
reliability of the full-size shift. Splitting the controls too keeps shared control noise from inflating
the agreement. Averaged over --seeds random splits.

Output: runs/pert_pool_v0/analysis_parse/split_half.parquet (item_id, r_half, reliability, n_treated, n_ctrl).
"""
import argparse
import time

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

from vcb import DATA, RUNS
from vcb.pert.folds import item_table
from vcb.pert.run import hvg_mask

ap = argparse.ArgumentParser()
ap.add_argument("--seeds", type=int, default=3)
ap.add_argument("--chunk", type=int, default=200_000)
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
DS = "parse_pbmc_cytokines"
RAW = DATA / "raw" / "parse_pbmc" / "20260203_Parse_10M_PBMC_cytokines.h5ad"

items = ad.read_h5ad(DATA / "items" / f"{DS}.items.h5ad")
meta, _, _ = item_table(items)
hv_genes = items.var_names[hvg_mask(items)].astype(str)
del items
raw = ad.read_h5ad(RAW, backed="r")
gpos = pd.Index(raw.var_names.astype(str)).get_indexer(hv_genes)
assert (gpos >= 0).all(), "HVGs missing from the raw file"
obs = raw.obs
ct = obs["cell_type"].astype(str).str.replace("/", "-", regex=False)
ctx = obs["donor"].astype(str) + "|" + ct
cyt = obs["cytokine"].astype(str)
log(f"raw {raw.shape}; {len(meta)} items")

ctx_codes = pd.Index(sorted(meta["context"].astype(str).unique()))
key_items = pd.Index(meta["perturbation"].astype(str) + "::" + meta["context"].astype(str))
cell_ctx = ctx_codes.get_indexer(ctx.values)
is_ctrl = (cyt.values == "PBS") & (cell_ctx >= 0)
cell_item = key_items.get_indexer((cyt + "::" + ctx).values)
use = is_ctrl | (cell_item >= 0)
log(f"cells used: {int(use.sum())} ({int(is_ctrl.sum())} controls)")

G = len(gpos)
S = {s: (np.zeros((len(key_items), 2, G)), np.zeros((len(key_items), 2)), np.zeros((len(ctx_codes), 2, G)), np.zeros((len(ctx_codes), 2))) for s in range(a.seeds)}
halves = {s: np.random.default_rng(s).integers(0, 2, raw.n_obs) for s in range(a.seeds)}
for i0 in range(0, raw.n_obs, a.chunk):
    i1 = min(i0 + a.chunk, raw.n_obs)
    sel = np.where(use[i0:i1])[0]
    if len(sel) == 0:
        continue
    X = sp.csr_matrix(raw.X[i0:i1])[sel]
    tot = np.asarray(X.sum(1)).ravel(); tot[tot == 0] = 1
    Xh = sp.diags(1e4 / tot) @ X[:, gpos]
    Xh.data = np.log1p(Xh.data)
    Xh = Xh.toarray()
    rows = i0 + sel
    it, cc, ctl = cell_item[rows], cell_ctx[rows], is_ctrl[rows]
    for s, (TS, TN, CS, CN) in S.items():
        h = halves[s][rows]
        m = ~ctl
        np.add.at(TS, (it[m], h[m]), Xh[m]); np.add.at(TN, (it[m], h[m]), 1)
        np.add.at(CS, (cc[ctl], h[ctl]), Xh[ctl]); np.add.at(CN, (cc[ctl], h[ctl]), 1)
    log(f"rows {i1}/{raw.n_obs}")

item_ctx = ctx_codes.get_indexer(meta["context"].astype(str).values)
rs = []
for s, (TS, TN, CS, CN) in S.items():
    T = TS / np.maximum(TN, 1)[..., None]
    C = (CS / np.maximum(CN, 1)[..., None])[item_ctx]
    d1, d2 = T[:, 0] - C[:, 0], T[:, 1] - C[:, 1]
    d1 = d1 - d1.mean(1, keepdims=True); d2 = d2 - d2.mean(1, keepdims=True)
    rs.append((d1 * d2).sum(1) / (np.linalg.norm(d1, axis=1) * np.linalg.norm(d2, axis=1) + 1e-12))
r = np.mean(rs, 0)
TN, CN = S[0][1].sum(1), S[0][3].sum(1)[item_ctx]
out = pd.DataFrame({"r_half": r, "reliability": np.clip(2 * r / (1 + r), -1, 1), "n_treated": TN, "n_ctrl": CN}, index=meta.index)
out.index.name = "item_id"
path = RUNS / "pert_pool_v0" / "analysis_parse" / "split_half.parquet"
out.to_parquet(path)
log(f"wrote {path}: median reliability {out['reliability'].median():.3f}; treated cells per item median {np.median(TN):.0f}")

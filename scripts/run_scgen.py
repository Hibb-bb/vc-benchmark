#!/usr/bin/env python
"""Train scGen on one fold of one dataset (unseen-context scheme) and write predicted deltas.

  .venv-scvi/bin/python scripts/run_scgen.py --dataset FrangiehIzar2021_RNA --fold 0 [--debug]

Uses the exact folds of the classical pool (vcb.pert.folds). Training cells: the stored
cell subsample of every *training* item plus all control cells. Output:
runs/pert_pool_v0/scgen/<dataset>.context.fold<k>.npz with item_ids and pred deltas over
all genes (HVG genes from scGen, other genes = mean_shift of the training fold).
"""
import argparse
import time
from pathlib import Path

import anndata as ad
import numpy as np

from vcb import DATA, RUNS
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask
from vcb.pert.scgen import SCGEN

ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--cells-per-item", type=int, default=100, help="training cells per item (subsample of the stored 500)")
ap.add_argument("--epochs", type=int, default=100)
ap.add_argument("--debug", action="store_true", help="tiny run on CPU to check the code path")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)

items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
cells_b = ad.read_h5ad(DATA / "items" / f"{a.dataset}.cells.h5ad", backed="r")
cobs = cells_b.obs
meta, D, ctrl_rows = item_table(items)
X_items = np.asarray(items.X)
splits = {f: (tr, te) for f, tr, te in fold_splits(meta, "context", a.folds)}
tr, te = splits[a.fold]
if a.debug:
    te = te[:6]
hv = hvg_mask(items)
hv_idx = np.where(hv)[0]
log(f"{a.dataset} fold {a.fold}: {len(tr)} train items, {len(te)} test items, {hv.sum()} HVGs")

# cells to load: a subsample per *training* item plus all controls (nothing from test items)
rng = np.random.default_rng(a.fold)
item_of_cell = cobs["item_id"].astype(str).values
is_ctrl_cell = cobs["is_control"].values.astype(bool)
train_items = set(meta.index[tr])
sel = []
for iid, idx in cobs.groupby("item_id", sort=False, observed=True).indices.items():
    if iid in train_items:
        sel.append(rng.choice(idx, min(a.cells_per_item, len(idx)), replace=False))
sel = np.concatenate(sel + [np.where(is_ctrl_cell)[0]])
if a.debug:
    sel = rng.choice(sel, min(3000, len(sel)), replace=False)
sel = np.sort(sel)
import scipy.sparse as sp
Xraw = sp.csr_matrix(cells_b[sel].to_memory().X, dtype=np.float32)
tot = np.asarray(Xraw.sum(1)).ravel()
tot[tot == 0] = 1
Xh = sp.diags((1e4 / tot).astype(np.float32)) @ Xraw[:, hv_idx]
Xh.data = np.log1p(Xh.data)
Xh = Xh.tocsr()
del Xraw
item_of_cell, is_ctrl_cell = item_of_cell[sel], is_ctrl_cell[sel]
ctx_of_cell = cobs["context"].astype(str).values[sel]
Xtr = Xh.toarray()
log(f"training cells {Xtr.shape}")

model = SCGEN(max_epochs=2 if a.debug else a.epochs, device=None).fit(Xtr, log=log)

# latents on demand (only the cells a prediction needs)
def Z_of(idx):
    return model.encode(Xh[idx].toarray())
Z_ctrl_by_ctx = {c: Z_of(np.where(is_ctrl_cell & (ctx_of_cell == c))[0]) for c in np.unique(ctx_of_cell[is_ctrl_cell])}
item_ctx = dict(zip(meta.index, meta["context"].astype(str)))
item_pert = dict(zip(meta.index, meta["perturbation"].astype(str)))

ms = D[tr].mean(0)  # mean_shift fallback for non-HVG genes (global; per-context handled by scoring reference anyway)
# index: perturbation -> {training context: cell rows}
cell_rows_by_item = cobs.iloc[sel].assign(_i=np.arange(len(sel))).groupby("item_id", sort=False, observed=True)["_i"].apply(np.asarray).to_dict()
src_by_pert = {}
for jj in tr:
    iid = meta.index[jj]
    if iid in cell_rows_by_item:
        src_by_pert.setdefault(item_pert[iid], {})[item_ctx[iid]] = cell_rows_by_item[iid]
preds, ids = [], []
for j in te:
    iid = meta.index[j]
    p, c = item_pert[iid], item_ctx[iid]
    src = {cc: Z_of(idx) for cc, idx in src_by_pert.get(p, {}).items() if cc in Z_ctrl_by_ctx}
    pred = ms.copy()
    if src and c in Z_ctrl_by_ctx:
        cells_pred = model.predict_delta(src, Z_ctrl_by_ctx, c, rng)
        ctrl_mean_hv = X_items[ctrl_rows[c]][hv]
        pred[hv] = cells_pred.mean(0) - ctrl_mean_hv
    preds.append(pred.astype(np.float32))
    ids.append(iid)
    if len(ids) % 100 == 0:
        log(f"  predicted {len(ids)}/{len(te)}")
log(f"items with a scGen prediction: {sum(1 for j in te if item_pert[meta.index[j]] in src_by_pert)}/{len(te)} (others fall back to mean_shift)")

out = RUNS / "pert_pool_v0" / "scgen"
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{a.dataset}.context.fold{a.fold}{'.debug' if a.debug else ''}.npz", item_ids=np.array(ids), pred=np.stack(preds), n_train_cells=Xtr.shape[0])
log(f"wrote {len(ids)} predictions")

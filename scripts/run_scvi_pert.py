#!/usr/bin/env python
"""scVI as a perturbation model (unseen perturbation-context combinations): train scVI on the
training cells with the perturbation as the batch variable, then decode the control cells of a
context under the held-out perturbation (batch transfer) and take the pseudobulk difference.

  .venv-scvi/bin/python scripts/run_scvi_pert.py --dataset FrangiehIzar2021_RNA --fold 0 [--debug]

Uses the exact folds of the classical pool (vcb.pert.folds, context scheme). Training cells: a
subsample of every *training* item plus all control cells; nothing from held-out items. Genes:
the benchmark's 2,000 HVGs (other genes fall back to the mean shift so all-gene metrics exist).
Output: runs/pert_pool_v0/scvi_cf/<dataset>.context.fold<k>.npz (item_ids, pred deltas).
"""
import argparse
import time
import warnings

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

from vcb import DATA, RUNS
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask

warnings.filterwarnings("ignore")


def pert_dose_key(df: pd.DataFrame) -> np.ndarray:
    """'perturbation|dose' as plain Python strings; missing doses become 'nan' under every pandas version."""
    pert = [str(x) for x in df["perturbation"].tolist()]
    dose = ["nan" if pd.isna(x) else str(x) for x in df["dose"].tolist()]
    return np.array([f"{p}|{d}" for p, d in zip(pert, dose)], dtype=object)


ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--scheme", default="context")
ap.add_argument("--cells-per-item", type=int, default=100)
ap.add_argument("--ctrl-cap", type=int, default=300, help="control cells per context used for prediction")
ap.add_argument("--latent", type=int, default=30)
ap.add_argument("--max-epochs", type=int, default=None)
ap.add_argument("--respondent", default="scvi_cf")
ap.add_argument("--debug", action="store_true")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
import scvi
scvi.settings.seed = a.fold

items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
cells_b = ad.read_h5ad(DATA / "items" / f"{a.dataset}.cells.h5ad", backed="r")
cobs = cells_b.obs
meta, D, ctrl_rows = item_table(items)
splits = {f: (tr, te) for f, tr, te in fold_splits(meta, a.scheme, a.folds)}
tr, te = splits[a.fold]
if a.debug:
    te = te[:8]
hv = hvg_mask(items); hv_idx = np.where(hv)[0]
log(f"{a.dataset} fold {a.fold} ({a.scheme}): {len(tr)} train items, {len(te)} test items, {hv.sum()} HVGs")

# cells: subsample per training item + all controls
rng = np.random.default_rng(a.fold)
is_ctrl = cobs["is_control"].values.astype(bool)
train_items = set(meta.index[tr])
sel = []
for iid, idx in cobs.groupby("item_id", sort=False, observed=True).indices.items():
    if iid in train_items:
        sel.append(rng.choice(idx, min(a.cells_per_item, len(idx)), replace=False))
sel = np.concatenate(sel + [np.where(is_ctrl)[0]])
if a.debug:
    sel = rng.choice(sel, min(4000, len(sel)), replace=False)
sel = np.sort(sel)
blocks = []
for i in range(0, len(sel), 200_000):  # chunked read, HVG columns only
    blocks.append(sp.csr_matrix(cells_b[sel[i:i + 200_000]].to_memory().X)[:, hv_idx])
X = sp.vstack(blocks).tocsr().astype(np.float32)
obs = cobs.iloc[sel].copy()
pert_key = pert_dose_key(obs)
pert_key[obs["is_control"].values.astype(bool)] = "control"
obs["pert_key"] = pert_key  # plain object strings; scvi makes the categorical itself
obs["ctx"] = np.array([str(x) for x in obs["context"].tolist()], dtype=object)
train = ad.AnnData(X=X, obs=obs[["pert_key", "ctx", "is_control"]].reset_index(drop=True))
log(f"training cells {train.shape}, {train.obs['pert_key'].nunique()} perturbation categories")

scvi.model.SCVI.setup_anndata(train, batch_key="pert_key")
model = scvi.model.SCVI(train, n_latent=a.latent, n_layers=2, gene_likelihood="nb")
n = train.n_obs
max_epochs = 2 if a.debug else (a.max_epochs or int(np.clip(400 * 20_000 / n, 25, 150)))
model.train(max_epochs=max_epochs, early_stopping=True, batch_size=512 if n > 200_000 else 128)
log(f"trained {len(model.history['elbo_train'])} epochs")

# prediction: control cells of the target context decoded under the target perturbation vs under control
item_key = dict(zip(meta.index, pert_dose_key(meta)))
item_ctx = dict(zip(meta.index, [str(x) for x in meta["context"].tolist()]))
X_items = np.asarray(items.X)
ms = D[tr].mean(0)
cats = set(train.obs["pert_key"].astype(str).unique())
ctrl_idx_by_ctx = {c: np.where((train.obs["ctx"].values == c) & train.obs["is_control"].values.astype(bool))[0] for c in np.unique(train.obs["ctx"].values)}
base_cache = {}
def decode_mean(idx, batch):
    sub = train[idx].copy()
    px = model.get_normalized_expression(sub, transform_batch=batch, library_size=1e4, return_numpy=True)
    return np.log1p(px).mean(0)
preds, ids, n_pred = [], [], 0
for j in te:
    iid = meta.index[j]; p, c = item_key[iid], item_ctx[iid]
    pred = ms.copy()
    idx = ctrl_idx_by_ctx.get(c, np.array([], dtype=int))
    if p in cats and len(idx) >= 5:
        if len(idx) > a.ctrl_cap:
            idx = np.sort(rng.choice(idx, a.ctrl_cap, replace=False))
        if c not in base_cache:
            base_cache[c] = decode_mean(idx, "control")
        pred[hv] = decode_mean(idx, p) - base_cache[c]
        n_pred += 1
    preds.append(pred.astype(np.float32)); ids.append(iid)
    if len(ids) % 200 == 0:
        log(f"  predicted {len(ids)}/{len(te)}")
log(f"items with an scVI prediction: {n_pred}/{len(te)} (others fall back to mean_shift)")
out = RUNS / "pert_pool_v0" / a.respondent
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{a.dataset}.{a.scheme}.fold{a.fold}{'.debug' if a.debug else ''}.npz", item_ids=np.array(ids), pred=np.stack(preds), n_train_cells=train.n_obs)
log(f"wrote {len(ids)} predictions")

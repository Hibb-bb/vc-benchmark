#!/usr/bin/env python
"""Re-derive STATE's predicted shifts as its own contrast: predicted cytokine state minus predicted control state.

  .venv/bin/python scripts/state_contrast_rescore.py [--respondent statetx_state]

STATE does not reproduce untreated cells: fed control cells labelled "control" its output drifts from its input
by more than a typical cytokine response (median norm 4.2 vs 3.0 on fold 0), so any shift measured against the
input carries that distortion. Reading STATE through its own contrast, mean prediction for (cytokine, context)
minus mean prediction for (control, same context), cancels the shared distortion and leaves the effect STATE
assigns to the cytokine. Uses the saved query.h5ad / pred.h5ad of each fold; rewrites only the HVG part of the
fold's prediction file (other genes keep the training fold's mean shift).
"""
import argparse

import anndata as ad
import numpy as np

from vcb import DATA, RUNS
from vcb.pert.run import hvg_mask

ap = argparse.ArgumentParser()
ap.add_argument("--respondent", default="statetx_state")
ap.add_argument("--folds", type=int, default=5)
a = ap.parse_args()
DS = "parse_pbmc_cytokines"
items = ad.read_h5ad(DATA / "items" / f"{DS}.items.h5ad")
hv = hvg_mask(items)
del items
for k in range(a.folds):
    w = RUNS.parent / "cache" / "statetx" / f"{a.respondent}_{DS}_fold{k}"
    q = ad.read_h5ad(w / "query.h5ad", backed="r").obs.reset_index(drop=True)
    pr = ad.read_h5ad(w / "pred.h5ad")
    P = np.asarray(pr.obsm["X_hvg"] if "X_hvg" in pr.obsm else pr.X, dtype=np.float32)
    key = q["pert"].astype(str) + "::ctx=" + q["cell_type"].astype(str)
    ctl = q["pert"].astype(str).eq("control").values
    ctl_mean = {c: P[np.where(ctl & (q["cell_type"].astype(str).values == c))[0]].mean(0) for c in q.loc[ctl, "cell_type"].astype(str).unique()}
    groups = {g: idx for g, idx in key[~ctl].groupby(key[~ctl]).groups.items()}
    path = RUNS / "pert_pool_v0" / a.respondent / f"{DS}.context.fold{k}.npz"
    z = dict(np.load(path, allow_pickle=True))
    preds, ids = z["pred"].copy(), z["item_ids"]
    done = 0
    for i, iid in enumerate(ids):
        g = str(iid).split(f"{DS}::", 1)[1]           # "<cytokine>::ctx=<context>"
        if g in groups:
            c = g.split("::ctx=", 1)[1]
            preds[i, hv] = P[np.asarray(groups[g])].mean(0) - ctl_mean[c]
            done += 1
    z["pred"] = preds
    np.savez_compressed(path, **z)
    print(f"fold {k}: {done}/{len(ids)} items re-derived as STATE's own contrast", flush=True)

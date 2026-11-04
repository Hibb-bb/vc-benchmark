#!/usr/bin/env python
"""Score an external respondent's fold predictions with the benchmark metrics and append
them to the dataset's scores table (replacing any previous rows of that respondent).

  python scripts/append_pert_scores.py --dataset FrangiehIzar2021_RNA --respondent scgen --scheme context

Expects runs/pert_pool_v0/<respondent>/<dataset>.<scheme>.fold<k>.npz for every fold.
The mean_shift reference prediction is recomputed per fold from the same splits.
"""
import argparse
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd

from vcb import DATA, RUNS
from vcb.pert.baselines import MeanShift
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.metrics import score_items
from vcb.pert.run import hvg_mask

ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--respondent", required=True)
ap.add_argument("--scheme", default="context")
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--run", default="pert_pool_v0", help="run whose scores table is merged into (and whose <respondent>/ holds the npz files unless --npz-root)")
ap.add_argument("--npz-root", default=None, help="directory holding <respondent>/<dataset>.<scheme>.fold<k>.npz")
ap.add_argument("--out", default=None, help="write the merged table here instead of in place (testing)")
a = ap.parse_args()

run = RUNS / a.run
items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
meta, D, _ = item_table(items)
pos = {iid: i for i, iid in enumerate(meta.index)}
pred = np.full_like(D, np.nan)
ms_pred = np.zeros_like(D)
for f, tr, te in fold_splits(meta, a.scheme, a.folds):
    npz = (Path(a.npz_root) if a.npz_root else run) / a.respondent / f"{a.dataset}.{a.scheme}.fold{f}.npz"
    assert npz.exists(), f"missing {npz}"
    z = np.load(npz, allow_pickle=True)
    for iid, p in zip(z["item_ids"], z["pred"]):
        pred[pos[iid]] = p
    ms = MeanShift().fit(None, D[tr], meta.iloc[tr])
    ms_pred[te] = ms.predict(None, meta.iloc[te])
ok = ~np.isnan(pred).any(1)
assert ok.all(), f"{(~ok).sum()} items without prediction"

mask = hvg_mask(items)
rows = []
for space, m in (("hvg", mask), ("all", None)):
    sc = score_items(pred, D, ms_pred, genes_mask=m)
    for metric, vals in sc.items():
        rows.append(pd.DataFrame({"item_id": meta.index, "respondent_id": a.respondent, "metric": f"{metric}@{space}", "value": vals}))
new = pd.concat(rows, ignore_index=True)
new["dataset_id"] = a.dataset
new["scheme"] = a.scheme

path = run / f"{a.dataset}.{a.scheme}.scores.parquet"
old = pd.read_parquet(path)
old = old[old["respondent_id"] != a.respondent]
pd.concat([old, new], ignore_index=True).to_parquet(Path(a.out) if a.out else path, index=False)
summ = pd.concat([old, new])[lambda d: d.metric == "pearson_delta@hvg"].groupby("respondent_id")["value"].mean().sort_values(ascending=False)
print(summ.round(3).to_string())

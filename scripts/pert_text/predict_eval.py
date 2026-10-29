#!/usr/bin/env python
"""Step 4b of the text perturbation encoder: do text embeddings help predict responses to unseen perturbations?

  .venv/bin/python scripts/pert_text/predict_eval.py --dataset NormanWeissman2019_filtered [--model Qwen3-Embedding-4B]

Uses the benchmark's own unseen-perturbation folds (scheme "perturbation": a test perturbation never appears in
training). Each perturbation is described by its text-card embedding (runs/pert_text/emb/<model>.full.npy),
reduced by PCA over the screen's perturbations to 32 dimensions and joined to a one-hot context. The standard
feature-driven models (ridge, KNN, MLP on a 50-PC response basis) are fitted on those features; the mean shift is
included as the reference of the pass rule. Results go to runs/pert_text/predict/ and never touch the published
scores tables, so they can be compared with the published models fitted on the screen's built-in features
(control-cell gene embeddings for genetic screens, one-hot labels otherwise).
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from vcb import DATA, RUNS
from vcb.pert.baselines import KNNShift, MeanShift, MLPPCA, RidgePCA
from vcb.pert.run import evaluate_dataset

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--model", default="Qwen3-Embedding-4B")
ap.add_argument("--field", default="full")
ap.add_argument("--dim", type=int, default=32)
a = ap.parse_args()

T = ROOT / "runs" / "pert_text"
keys = (T / "emb" / "keys.txt").read_text().splitlines()
E = np.load(T / "emb" / f"{a.model}.{a.field}.npy")
kpos = {k: i for i, k in enumerate(keys)}
tag = "txt" + a.model.split("-")[-1].lower().replace(".", "")


def features(meta):
    k = (meta["pert_type"].astype(str) + "::" + meta["perturbation"].astype(str)).values
    found = np.array([x in kpos for x in k])
    perts = sorted(set(k[found]))
    Z = E[[kpos[p] for p in perts]]
    d = min(a.dim, len(perts) - 1)
    Zp = PCA(n_components=d, random_state=0).fit_transform(Z)        # unsupervised, over the screen's perturbation names
    zmap = dict(zip(perts, Zp))
    Fp = np.stack([zmap.get(x, np.zeros(d)) for x in k]).astype(np.float32)
    ctx = pd.get_dummies(meta["context"].astype(str), prefix="c").values.astype(np.float32)
    return np.hstack([Fp, ctx]), found


def pool():
    ms = MeanShift()
    models = [RidgePCA(d=50, lam=100.0), KNNShift(k=20), MLPPCA(d=50, hidden=256)]
    for m in models:
        m.name = f"{m.name}_{tag}"
    return [ms] + models


out = T / "predict"
out.mkdir(parents=True, exist_ok=True)
evaluate_dataset(DATA / "items" / f"{a.dataset}.items.h5ad", DATA / "items" / f"{a.dataset}.cells.h5ad", out,
                 scheme="perturbation", pool=pool(), merge=True, features=features)
print(json.dumps({"dataset": a.dataset, "model": a.model, "tag": tag}))

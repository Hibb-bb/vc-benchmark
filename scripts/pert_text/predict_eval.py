#!/usr/bin/env python
"""Step 4b of the text perturbation encoder: do text embeddings help predict responses to unseen perturbations?

  .venv/bin/python scripts/pert_text/predict_eval.py --dataset NormanWeissman2019_filtered [--model Qwen3-Embedding-4B]
  .venv/bin/python scripts/pert_text/predict_eval.py --dataset parse_pbmc_cytokines --scheme context

Uses the benchmark's own folds (default scheme "perturbation": a test perturbation never appears in training;
"context" holds out perturbation x context combinations). Each perturbation is described by its text-card
embedding (runs/pert_text/emb/<model>.full.npy), reduced by PCA over the screen's perturbations to 32 dimensions
and joined to a one-hot context and, where doses vary, log10 dose (as the built-in chemical features are). Every
feature-driven model of the published pool (KNN, ridge, GP, PCA regression, subsampled variants, both MLPs) is fitted on those
features, so each has a twin fitted on the built-in features; the mean shift is included as the reference of the
pass rule. Results go to runs/pert_text/predict/ and never touch the published
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
from vcb.pert.baselines import MeanShift, MLPPCA, PCARegression, featured_pool
from vcb.pert.run import evaluate_dataset

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--model", default="Qwen3-Embedding-4B")
ap.add_argument("--field", default="full")
ap.add_argument("--dim", type=int, default=32)
ap.add_argument("--scheme", default="perturbation")
ap.add_argument("--emb-dir", default=None, help="embedding directory (default runs/pert_text/emb)")
ap.add_argument("--out", default=None, help="output directory (default runs/pert_text/predict)")
ap.add_argument("--min-cells", type=int, default=50)
ap.add_argument("--with-onehot", action="store_true", help="also append a one-hot perturbation (identity) block; tag suffix oh")
ap.add_argument("--builtin", action="store_true", help="fit the same pool on the screen's built-in features (no text, no suffix)")
ap.add_argument("--extra-metrics", action="store_true", help="also score the DE-gene metrics (vcb.pert.metrics.de_scores)")
a = ap.parse_args()

T = ROOT / "runs" / "pert_text"
EMB = Path(a.emb_dir) if a.emb_dir else T / "emb"
keys = (EMB / "keys.txt").read_text().splitlines()
E = np.load(EMB / f"{a.model}.{a.field}.npy")
kpos = {k: i for i, k in enumerate(keys)}
tag = "txt" + a.model.split("-")[-1].lower().replace(".", "") + ("oh" if a.with_onehot else "")


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
    parts = [Fp, ctx]
    if a.with_onehot:
        parts.append(pd.get_dummies(meta["perturbation"].astype(str), prefix="p").values.astype(np.float32))
    if meta["dose"].nunique() > 1:
        parts.append(np.log10(meta["dose"].fillna(0).values.astype(np.float32) + 1e-3)[:, None])
    return np.hstack(parts), found


def pool():
    ms = MeanShift()
    models = featured_pool() + [PCARegression(k) for k in (2, 5, 10, 20, 50, 100, 200)] + [MLPPCA(d=50, hidden=h) for h in (256, 1024)]
    if not a.builtin:
        for m in models:
            m.name = f"{m.name}_{tag}"
    return [ms] + models


out = Path(a.out) if a.out else T / "predict"
out.mkdir(parents=True, exist_ok=True)
evaluate_dataset(DATA / "items" / f"{a.dataset}.items.h5ad", DATA / "items" / f"{a.dataset}.cells.h5ad", out,
                 scheme=a.scheme, min_cells=a.min_cells, pool=pool(), merge=True,
                 features=None if a.builtin else features, extra_metrics=a.extra_metrics)
print(json.dumps({"dataset": a.dataset, "model": a.model, "tag": tag}))

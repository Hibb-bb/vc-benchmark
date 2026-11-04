#!/usr/bin/env python
"""Text-enhanced interaction models on the unseen-combination split (vcb.pert.text_models), with no-text twins.

  .venv/bin/python scripts/pert_text/interaction_eval.py --dataset immune_dictionary --emb-dir runs/pert_text/idict/emb \
      --out runs/pert_text/interact_idict --min-cells 30
  .venv/bin/python scripts/pert_text/interaction_eval.py --dataset parse_pbmc_cytokines --out runs/pert_text/interact

Scheme "context" only (benchmark folds). Features handed to the pool are one-hot perturbation + one-hot context (the
built-in features of these screens); the text enters only through the models' own text maps. Scores go to --out and
never touch the published tables.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import DATA
from vcb.pert.baselines import MeanShift, RidgePCA
from vcb.pert.run import evaluate_dataset
from vcb.pert.text_models import RidgeNeighbourCorrection, RidgeScaledInteraction

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--model", default="Qwen3-Embedding-4B")
ap.add_argument("--emb-dir", default=str(ROOT / "runs" / "pert_text" / "emb"))
ap.add_argument("--out", default=str(ROOT / "runs" / "pert_text" / "interact"))
ap.add_argument("--min-cells", type=int, default=50)
a = ap.parse_args()

E = Path(a.emb_dir)
keys = (E / "keys.txt").read_text().splitlines()
X = np.load(E / f"{a.model}.full.npy").astype(np.float32)
text = {k.split("::", 1)[1]: X[i] for i, k in enumerate(keys) if k.startswith("cytokine::")}


def features(meta):
    oh = pd.get_dummies(meta["perturbation"].astype(str), prefix="p").values.astype(np.float32)
    ctx = pd.get_dummies(meta["context"].astype(str), prefix="c").values.astype(np.float32)
    return np.hstack([oh, ctx]), meta["perturbation"].astype(str).isin(set(text)).values


pool = [MeanShift(), RidgePCA(50, 100.0)]                  # the published best on both screens' built-in features
for src in ("txt", "resp", "mix"):
    for alpha in (0.5, 1.0):
        pool.append(RidgeNeighbourCorrection(text, src=src, k=10, alpha=alpha))
for src in ("txt", "resp", "both"):
    for sc in (0.3, 1.0, 2.0):
        pool.append(RidgeScaledInteraction(text, src=src, s=sc))
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)
evaluate_dataset(DATA / "items" / f"{a.dataset}.items.h5ad", DATA / "items" / f"{a.dataset}.cells.h5ad", out,
                 scheme="context", min_cells=a.min_cells, pool=pool, merge=True, features=features)

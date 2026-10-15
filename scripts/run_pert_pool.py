#!/usr/bin/env python
"""python scripts/run_pert_pool.py --dataset NormanWeissman2019_filtered [--scheme perturbation|context]"""
import argparse

from vcb import DATA, RUNS
from vcb.pert.run import evaluate_dataset

ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--scheme", default="perturbation")
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--min-cells", type=int, default=50)
ap.add_argument("--pool", default="default", choices=["default", "pca_ladder"], help="pca_ladder: only the PCA-regression ladder, merged into the existing scores table")
a = ap.parse_args()

pool, merge = None, False
if a.pool == "pca_ladder":
    from vcb.pert.baselines import pca_ladder
    pool, merge = pca_ladder(), True
evaluate_dataset(DATA / "items" / f"{a.dataset}.items.h5ad", DATA / "items" / f"{a.dataset}.cells.h5ad", RUNS / "pert_pool_v0", scheme=a.scheme, n_folds=a.folds, min_cells=a.min_cells, pool=pool, merge=merge)

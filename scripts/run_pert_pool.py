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
ap.add_argument("--pool", default="default", choices=["default", "pca_ladder", "featured", "mlp", "latent"], help="pca_ladder / featured: only that subset, merged into the existing scores table")
ap.add_argument("--out-run", default="pert_pool_v0", help="run directory for the scores tables")
ap.add_argument("--cells-per-item", type=int, default=30, help="latent pool: cells per training item")
a = ap.parse_args()

pool, merge = None, False
if a.pool == "pca_ladder":
    from vcb.pert.baselines import pca_ladder
    pool, merge = pca_ladder(), True
elif a.pool == "mlp":
    from vcb.pert.baselines import mlp_pool
    pool, merge = mlp_pool(), True
elif a.pool == "featured":
    from vcb.pert.baselines import featured_pool
    pool, merge = featured_pool(), True
elif a.pool == "latent":
    from vcb.pert.latent import latent_pool
    pool, merge = latent_pool(DATA / "items" / f"{a.dataset}.cells.h5ad", a.scheme, cells_per_item=a.cells_per_item), True
evaluate_dataset(DATA / "items" / f"{a.dataset}.items.h5ad", DATA / "items" / f"{a.dataset}.cells.h5ad", RUNS / a.out_run, scheme=a.scheme, n_folds=a.folds, min_cells=a.min_cells, pool=pool, merge=merge)

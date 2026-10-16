"""Cross-fitted evaluation of the component-B pool on one dataset.

Split: K-fold over *perturbations* (unseen-perturbation scenario). Every perturbation is
held out exactly once, so every condition becomes an item with an out-of-fold prediction
from every respondent. For multi-context datasets a second scheme, `context`, holds out
(perturbation, context) pairs while the same perturbation stays visible in other contexts
(unseen-context scenario). Folds are deterministic in the seed.

Output: long table (item_id, respondent_id, metric, value) + items table with covariates.
"""
from __future__ import annotations

import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
from .baselines import MeanShift, default_pool
from .features import categorical_item_features, chemical_item_features, gene_embedding_from_controls, genetic_item_features
from .folds import fold_groups, fold_splits, item_table
from .metrics import score_items


def hvg_mask(items: ad.AnnData, n_top: int = 2000) -> np.ndarray:
    """Top genes by control variance / (mean + eps), pooled over contexts (unsupervised, no labels used)."""
    stats = items.uns["control_stats"]
    disp = np.zeros(items.n_vars)
    for ctx, s in stats.items():
        disp += np.asarray(s["var"]) / (np.asarray(s["mean"]) + 0.1)
    mask = np.zeros(items.n_vars, dtype=bool)
    mask[np.argsort(-disp)[:n_top]] = True
    return mask


def evaluate_dataset(items_path: Path, cells_path: Path, out_dir: Path, scheme: str = "perturbation", n_folds: int = 5, seed: int = 0, min_cells: int = 50, pool=None, merge: bool = False) -> pd.DataFrame:
    """pool: explicit list of respondents (default: default_pool). merge=True appends/replaces
    these respondents in an existing scores table instead of rewriting it."""
    t0 = time.time()
    items = ad.read_h5ad(items_path)
    dataset_id = items.obs["dataset_id"].iloc[0]
    obs = items.obs
    meta, D, ctrl_rows = item_table(items, min_cells)
    X = np.asarray(items.X)
    ctrl_mean_by_ctx = {c: X[r] for c, r in ctrl_rows.items()}
    genetic = meta["pert_type"].isin(["CRISPRi", "CRISPRa", "CRISPR_KO"]).mean() > 0.5
    multi_ctx = meta["context"].nunique() > 1
    print(f"[{dataset_id}] {len(meta)} items, genetic={genetic}, contexts={meta['context'].nunique()}, scheme={scheme}", flush=True)

    # Features
    featured = genetic
    if genetic:
        cells = ad.read_h5ad(cells_path)
        ctrl_cells = cells[cells.obs["is_control"].values.astype(bool)]
        gene_emb = gene_embedding_from_controls(ctrl_cells.X, items.var_names, seed=seed)
        F, found = genetic_item_features(meta, gene_emb)
        meta["target_in_var"] = found
        print(f"  target gene found in var for {found.mean():.1%} of items", flush=True)
    elif "smiles" in meta and meta["smiles"].astype(str).str.len().gt(3).any():
        F, found = chemical_item_features(meta)
        meta["target_in_var"] = found
        featured = True
        print(f"  Morgan fingerprint available for {found.mean():.1%} of items", flush=True)
    else:
        # one-hot perturbation + context + log dose: informative across contexts (a perturbation seen in
        # other contexts), uninformative for an unseen perturbation (its column is all zeros in training)
        F = categorical_item_features(meta)
        meta["target_in_var"] = False
        featured = multi_ctx
        print(f"  categorical features ({F.shape[1]} columns); featured={featured}", flush=True)

    # Folds (shared with external respondents via folds.py)
    gid = fold_groups(meta, scheme, seed)
    splits = list(fold_splits(meta, scheme, n_folds, seed))
    n_folds = len(splits)

    pool = pool if pool is not None else default_pool(items.var_names, ctrl_mean_by_ctx, genetic=genetic, multi_context=multi_ctx, featured=featured)
    names = [b.name for b in pool]
    mask = hvg_mask(items)
    # score fold by fold so only one prediction matrix lives in memory at a time
    scores = {(n, space, metric): np.full(len(meta), np.nan) for n in names for space in ("hvg", "all") for metric in ("pearson_delta", "pearson_delta_sys", "mse", "l2_ratio", "deg_overlap50")}
    for f, tr, te in splits:
        ms = MeanShift().fit(F[tr], D[tr], meta.iloc[tr])
        ms_pred = ms.predict(F[te], meta.iloc[te])
        for b in pool:
            tb = time.time()
            b.fit(F[tr], D[tr], meta.iloc[tr])
            pred = b.predict(F[te], meta.iloc[te])
            for space, m in (("hvg", mask), ("all", None)):
                sc = score_items(pred, D[te], ms_pred, genes_mask=m)
                for metric, vals in sc.items():
                    scores[(b.name, space, metric)][te] = vals
            print(f"  fold {f+1}/{n_folds} {b.name:22s} {time.time()-tb:5.1f}s", flush=True)
    rows = [pd.DataFrame({"item_id": meta.index, "respondent_id": n, "metric": f"{metric}@{space}", "value": v}) for (n, space, metric), v in scores.items()]
    long = pd.concat(rows, ignore_index=True)
    long["dataset_id"] = dataset_id
    long["scheme"] = scheme

    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{dataset_id}.{scheme}.scores.parquet"
    if merge and path.exists():
        old = pd.read_parquet(path)
        long = pd.concat([old[~old["respondent_id"].isin(names)], long], ignore_index=True)
    long.to_parquet(path, index=False)
    meta_out = meta[["dataset_id", "perturbation", "targets", "pert_type", "context", "dose", "time_h", "n_cells", "delta_l2", "target_in_var"]].copy()
    meta_out["fold_group"] = gid
    meta_out.to_parquet(out_dir / f"{dataset_id}.{scheme}.items.parquet")
    summ = long[long.metric == "pearson_delta@hvg"].groupby("respondent_id")["value"].agg(["mean", "median"]).sort_values("mean", ascending=False)
    print(summ.round(3).to_string(), flush=True)
    print(f"[{dataset_id}] done in {time.time()-t0:.0f}s", flush=True)
    return long

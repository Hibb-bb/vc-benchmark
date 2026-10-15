"""Deterministic folds shared by every component-B respondent (classical pool and ML models).

Moved verbatim from run.py so an external model (scGen, ...) reproduces the exact same
held-out sets: permute unique groups with the seed, map to integer ids, GroupKFold.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold


def fold_groups(meta: pd.DataFrame, scheme: str, seed: int = 0) -> np.ndarray:
    if scheme == "perturbation":
        groups = meta["perturbation"].astype(str).values
    elif scheme == "context":
        groups = (meta["perturbation"].astype(str) + "::" + meta["context"].astype(str)).values
    else:
        raise ValueError(scheme)
    rng = np.random.default_rng(seed)
    ug = np.unique(groups)
    perm = {g: i for i, g in enumerate(rng.permutation(ug))}
    return np.array([perm[g] for g in groups])


def fold_splits(meta: pd.DataFrame, scheme: str, n_folds: int = 5, seed: int = 0):
    """Yields (fold_index, train_idx, test_idx) over positional indices of meta."""
    gid = fold_groups(meta, scheme, seed)
    n_folds = min(n_folds, len(np.unique(gid)))
    gkf = GroupKFold(n_splits=n_folds)
    X = np.zeros((len(meta), 1))
    for f, (tr, te) in enumerate(gkf.split(X, None, gid)):
        yield f, tr, te


def item_table(items, min_cells: int = 50):
    """The same item selection run.py uses: non-control, matched control, enough cells.
    Returns (meta, D, ctrl_rows) where D is the delta matrix over all genes."""
    obs = items.obs
    is_ctrl = obs["is_control"].values.astype(bool)
    ctrl_rows = {obs["context"].iloc[i]: i for i in np.where(is_ctrl)[0]}
    keep = (~is_ctrl) & obs["has_matched_control"].values.astype(bool) & (obs["n_cells"].values >= min_cells)
    idx = np.where(keep)[0]
    meta = obs.iloc[idx].copy()
    dose = pd.to_numeric(meta["dose"], errors="coerce") if "dose" in meta else pd.Series(np.nan, index=meta.index)
    meta["pert_key"] = meta["perturbation"].astype(str) + np.where(dose.notna(), "@" + dose.astype(str), "")
    X = np.asarray(items.X)
    D = np.stack([X[i] - X[ctrl_rows[obs["context"].iloc[i]]] for i in idx]).astype(np.float32)
    return meta, D, ctrl_rows

"""Generic component-A panel builder: one annotated h5ad with raw counts -> a stratified,
donor- or context-disjoint panel that `vcb.repr.run.evaluate_panel` can score.

Strata are (context, label, donor). Whole donors (`split_by="donor"`) or whole contexts
(`split_by="context"`) are held out; nothing is shared between train and test. Test donors are
chosen greedily so that they cover as many contexts as possible, under the constraint that
every context keeps at least one train donor (a donor unique to its context stays in train).
Each stratum is capped (`test_cap`, `train_cap`) and dropped below `min_stratum` cells. Test
cells whose label has no train cells are kept but flagged `type_in_train = False`.

Panel obs columns consumed downstream: `cell_type`, `donor`, `tissue` (= context), `stratum`,
`split`, `type_in_train`, `dataset_id`, `total_counts`, `n_genes_by_counts`
(`vcb.repr.run.panel_items`, `scripts/fit_rasch.py`, `scripts/summarize.py`).
"""
from __future__ import annotations

import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp


def _counts(a: ad.AnnData, counts: str):
    if counts == "X":
        return a.X, a.var
    if counts == "raw":
        if a.raw is None:
            raise ValueError("--counts raw but the h5ad has no .raw; use --counts X or layers/<name>")
        return a.raw.X, a.raw.var
    if counts.startswith("layers/"):
        return a.layers[counts.split("/", 1)[1]], a.var
    raise ValueError(f"unknown counts spec {counts!r}")


def _choose_test_donors(obs: pd.DataFrame, test_frac: float, rng: np.random.Generator) -> list[str]:
    """Greedy: cover as many contexts as possible, keep >= 1 train donor per context, hit test_frac of cells."""
    n_total = len(obs)
    target = test_frac * n_total
    size = obs.groupby("donor", observed=True).size()
    ctx_of = obs.groupby("donor", observed=True)["tissue"].agg(lambda s: set(s.unique()))
    train_left = obs.groupby("tissue", observed=True)["donor"].nunique().to_dict()
    donors = sorted(size.index, key=lambda d: (-size[d], d))
    test, covered, n_test = [], set(), 0
    while n_test < target:
        best, best_key = None, None
        for d in donors:
            if d in test or any(train_left[c] <= 1 for c in ctx_of[d]):
                continue
            new = len(ctx_of[d] - covered)
            overshoot = max(0, n_test + size[d] - target)
            key = (new, -overshoot, size[d])
            if best_key is None or key > best_key:
                best, best_key = d, key
        if best is None:
            break
        test.append(best)
        covered |= ctx_of[best]
        n_test += size[best]
        for c in ctx_of[best]:
            train_left[c] -= 1
    return test


def _choose_test_contexts(obs: pd.DataFrame, test_frac: float) -> list[str]:
    """Hold out whole contexts whose labels are mostly present in the remaining contexts."""
    target = test_frac * len(obs)
    size = obs.groupby("tissue", observed=True).size()
    labels_in = obs.groupby("tissue", observed=True)["cell_type"].agg(lambda s: set(s.unique()))
    order = sorted(size.index, key=lambda c: (-size[c], c))
    test, n_test = [], 0
    for c in order[1:]:  # the largest context always stays in train
        others = set().union(*(labels_in[o] for o in order if o != c and o not in test))
        cov = obs.loc[obs["tissue"] == c, "cell_type"].isin(others).mean()
        if cov < 0.5 or n_test >= target:
            continue
        test.append(c)
        n_test += size[c]
    return test


def _cap(obs: pd.DataFrame, cap: int, rng: np.random.Generator) -> pd.Index:
    keep = []
    for _, idx in obs.groupby("stratum", observed=True).indices.items():
        if len(idx) > cap:
            idx = np.sort(rng.choice(idx, cap, replace=False))
        keep.append(obs.index[idx])
    return keep[0].append(keep[1:]) if keep else obs.index[:0]


def build_generic_panel(h5ad: Path, name: str, label_key: str, donor_key: str, context_key: str | None, out: Path, *,
                        counts: str = "raw", split_by: str = "donor", test_frac: float = 0.25, test_cap: int = 50,
                        train_cap: int = 200, min_stratum: int = 20, filter_query: str | None = None,
                        test_groups: list[str] | None = None, seed: int = 0) -> ad.AnnData:
    t0 = time.time()
    rng = np.random.default_rng(seed)
    # Select cells on obs first and read only the kept rows of X: a 2.6 M-cell concat file does not
    # fit through the old load-everything path. With counts == "X" the file is opened backed; other
    # counts specs (raw, layers/<name>) are loaded in memory as before.
    backed = counts == "X"
    a = ad.read_h5ad(h5ad, backed="r") if backed else ad.read_h5ad(h5ad)
    print(f"read {h5ad}: {a.shape}{' (backed)' if backed else ''} in {time.time()-t0:.0f}s", flush=True)
    if backed:
        X_full, var = a.X, a.var
    else:
        X_full, var = _counts(a, counts)
    obs = a.obs.copy()
    pos = np.arange(len(obs))  # positions into X_full of the rows still in obs
    for c in obs.columns:
        if obs[c].dtype == object or str(obs[c].dtype) == "category":
            obs[c] = obs[c].astype(str)
    if filter_query:
        m = obs.eval(filter_query).values.astype(bool)
        print(f"filter {filter_query!r}: {m.sum()} / {len(m)} cells", flush=True)
        obs, pos = obs[m], pos[m]
    for k in (label_key, donor_key) + ((context_key,) if context_key else ()):
        if k not in obs:
            raise KeyError(f"obs column {k!r} missing; available: {list(obs.columns)[:40]}")
    obs["cell_type"] = obs[label_key].astype(str)
    obs["donor"] = obs[donor_key].astype(str)
    obs["tissue"] = obs[context_key].astype(str) if context_key else "all"
    bad = obs["cell_type"].isin(["nan", "None", "", "NaN", "<NA>", "unknown", "Unknown"]) | obs["donor"].isin(["nan", "None", ""])
    if bad.any():
        print(f"dropping {bad.sum()} cells without label or donor", flush=True)
        obs, pos = obs[~bad.values], pos[~bad.values]
    obs["stratum"] = obs["tissue"] + "|" + obs["cell_type"] + "|" + obs["donor"]

    # drop strata below min_stratum before choosing the split, so small strata do not drive it
    n_str = obs["stratum"].map(obs["stratum"].value_counts())
    keep = (n_str >= min_stratum).values
    print(f"strata >= {min_stratum} cells: {keep.sum()} / {len(keep)} cells kept, {obs.loc[keep, 'stratum'].nunique()} strata", flush=True)
    obs, pos = obs[keep], pos[keep]

    unit = "donor" if split_by == "donor" else "tissue"
    if test_groups:
        test_units = [g for g in test_groups if g in set(obs[unit])]
        missing = sorted(set(test_groups) - set(test_units))
        if missing:
            print(f"warning: requested test {unit}s not found: {missing}", flush=True)
    elif split_by == "donor":
        test_units = _choose_test_donors(obs, test_frac, rng)
    else:
        test_units = _choose_test_contexts(obs, test_frac)
    obs["split"] = np.where(obs[unit].isin(test_units), "test", "train")
    print(f"held-out {unit}s ({len(test_units)}): {test_units[:20]}{' ...' if len(test_units) > 20 else ''}", flush=True)

    tr_idx = _cap(obs[obs["split"] == "train"], train_cap, rng)
    te_idx = _cap(obs[obs["split"] == "test"], test_cap, rng)
    kept = obs.index.isin(tr_idx.append(te_idx))
    obs, pos = obs[kept], pos[kept]
    order = np.argsort(pos, kind="stable")  # read rows in file order, then restore obs order
    X = X_full[pos[order]]
    if backed:
        X = X.to_memory() if hasattr(X, "to_memory") else X
    inv = np.empty_like(order); inv[order] = np.arange(len(order))
    X = sp.csr_matrix(X)[inv]
    print(f"loaded {X.shape[0]} kept rows ({X.nnz:,} nonzeros) in {time.time()-t0:.0f}s", flush=True)
    train_types = set(obs.loc[obs["split"] == "train", "cell_type"])
    obs["type_in_train"] = obs["cell_type"].isin(train_types)
    obs["dataset_id"] = name
    X = sp.csr_matrix(X, dtype=np.float32)
    obs["total_counts"] = np.asarray(X.sum(1)).ravel()
    obs["n_genes_by_counts"] = np.asarray((X > 0).sum(1)).ravel()
    if "cell_ontology_term_id" in obs and "cell_ontology_id" not in obs:
        obs["cell_ontology_id"] = obs["cell_ontology_term_id"]

    panel = ad.AnnData(X=X, obs=obs, var=var.copy())
    panel.var_names_make_unique()
    sample = X[: min(1000, X.shape[0])].data
    if len(sample) and not np.allclose(sample, np.round(sample)):
        print("WARNING: counts do not look like integers", flush=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    panel.write_h5ad(out)
    te = obs["split"] == "test"
    n_unseen = (~obs.loc[te, "type_in_train"]).sum()
    print(f"{name}: {(~te).sum()} train / {te.sum()} test; {obs['stratum'].nunique()} strata "
          f"({obs.loc[te, 'stratum'].nunique()} test); {obs['cell_type'].nunique()} types "
          f"({obs.loc[te, 'cell_type'].nunique()} in test); {n_unseen} test cells of unseen types; "
          f"{obs['donor'].nunique()} {donor_key}s, {obs['tissue'].nunique()} contexts; wrote {out} in {time.time()-t0:.0f}s", flush=True)
    return panel

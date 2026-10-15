"""Run the component-A pool on a panel: preprocess once, embed with every respondent, probe."""
from __future__ import annotations

import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd

from .embedders import Preprocessor, default_pool
from .probe import probe_responses


def panel_items(panel, te, y_tr):
    """Item covariate table for the test cells; works for any panel (TS2-specific columns optional)."""
    cols = [c for c in ["dataset_id", "tissue", "donor", "cell_type", "cell_ontology_id", "compartment", "stratum", "manually_annotated", "n_genes_by_counts", "total_counts"] if c in panel.obs.columns]
    items = panel.obs.loc[te, cols].copy()
    X = panel.X[te]
    if "total_counts" not in items:
        items["total_counts"] = np.asarray(X.sum(1)).ravel()
    if "n_genes_by_counts" not in items:
        items["n_genes_by_counts"] = np.asarray((X > 0).sum(1)).ravel()
    items["n_train_same_type"] = items["cell_type"].map(pd.Series(y_tr).value_counts()).fillna(0).astype(int)
    items.index.name = "item_id"
    return items


def evaluate_panel(panel_path: Path, out_dir: Path, n_hvg: int = 2000, probe_C: float = 1.0, seed: int = 0, pool=None) -> pd.DataFrame:
    t0 = time.time()
    panel = ad.read_h5ad(panel_path)
    tr = (panel.obs["split"] == "train").values
    te = (panel.obs["split"] == "test").values & panel.obs["type_in_train"].values.astype(bool)
    y_tr = panel.obs.loc[tr, "cell_type"].values
    y_te = panel.obs.loc[te, "cell_type"].values
    ids_te = panel.obs_names[te]
    print(f"panel {panel.shape}: {tr.sum()} train, {te.sum()} test items, {len(set(y_tr))} classes", flush=True)

    prep = Preprocessor(n_hvg=n_hvg, seed=seed).fit(panel.X[tr], panel.var_names)
    mats = {
        "scaled": (prep.transform(panel.X[tr]), prep.transform(panel.X[te])),
        "log": (prep.transform(panel.X[tr], scaled=False), prep.transform(panel.X[te], scaled=False)),
        "depth": (Preprocessor.depth_features(panel.X[tr]), Preprocessor.depth_features(panel.X[te])),
    }
    print(f"preprocessed in {time.time()-t0:.0f}s", flush=True)

    pool = pool or default_pool()
    out_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for e in pool:
        tb = time.time()
        Xtr, Xte = mats[e.needs]
        e.fit(Xtr)
        Ztr, Zte = e.transform(Xtr), e.transform(Xte)
        df = probe_responses(Ztr, y_tr, Zte, y_te, ids_te, e.name, C=probe_C, seed=seed)
        frames.append(df)
        print(f"  {e.name:22s} dim={Zte.shape[1]:4d} acc={df['k'].mean():.3f}  {time.time()-tb:5.0f}s", flush=True)
        pd.concat(frames).to_parquet(out_dir / "responses.parquet", index=False)  # checkpoint
    long = pd.concat(frames, ignore_index=True)
    long["dataset_id"] = panel.obs["dataset_id"].iloc[0]
    long.to_parquet(out_dir / "responses.parquet", index=False)
    items = panel_items(panel, te, y_tr)
    items.to_parquet(out_dir / "items.parquet")
    print(f"done in {time.time()-t0:.0f}s", flush=True)
    return long

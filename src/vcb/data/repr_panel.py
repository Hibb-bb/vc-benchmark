"""Build the component-A panel from Tabula Sapiens v2 per-tissue files.

Items are cells from a fixed, stratified panel. Stratum = (tissue, cell_ontology_class,
donor). Donors are split globally into train and test (donor-disjoint, so the probe can
never learn donor identity as a proxy for type). Within each stratum we cap the number of
cells: `test_cap` for test donors, `train_cap` for train donors.

Only 10X cells are used in v0 (smart-seq2 plates would add a protocol factor; they can be
added as their own items later). Labels: `cell_ontology_class` (+ CL id). Raw counts come
from layers['raw_counts'].
"""
from __future__ import annotations

import time
from pathlib import Path

import anndata as ad
import h5py
import numpy as np
import pandas as pd
import scipy.sparse as sp
from anndata.io import read_elem, sparse_dataset

OBS_KEEP = ["donor", "tissue", "method", "assay", "cell_ontology_class", "cell_ontology_id", "compartment", "broad_cell_class", "manually_annotated", "n_genes_by_counts", "total_counts", "pct_counts_mt", "sex", "age"]


def read_all_obs(files: list[Path]) -> pd.DataFrame:
    frames = []
    for p in files:
        with h5py.File(p, "r") as f:
            o = read_elem(f["obs"])
        o = o[[c for c in OBS_KEEP if c in o.columns]].copy()
        o["file"] = p.name
        o["row"] = np.arange(len(o))
        frames.append(o)
    obs = pd.concat(frames)
    obs.index = obs["file"].str.split("_").str[0] + "::" + obs.index.astype(str)
    return obs


def choose_test_donors(obs: pd.DataFrame, frac: float = 0.25, seed: int = 0) -> list[str]:
    """Greedy: pick donors so that test covers as many tissues as possible, ~frac of cells."""
    rng = np.random.default_rng(seed)
    donors = obs["donor"].astype(str)
    target = frac * len(obs)
    cover = obs.groupby(donors)["tissue"].agg(lambda s: set(s.astype(str)))
    sizes = donors.value_counts()
    chosen, covered, n = [], set(), 0
    cand = list(rng.permutation(cover.index))
    while n < target and cand:
        gain = {d: len(cover[d] - covered) for d in cand}
        d = max(cand, key=lambda x: (gain[x], -abs(sizes[x] - target / 6)))
        chosen.append(d)
        covered |= cover[d]
        n += sizes[d]
        cand.remove(d)
    return chosen


def build_panel(files: list[Path], out_path: Path, test_cap: int = 50, train_cap: int = 200, min_stratum: int = 20, test_donor_frac: float = 0.25, seed: int = 0, methods=("10X",)) -> ad.AnnData:
    t0 = time.time()
    rng = np.random.default_rng(seed)
    obs = read_all_obs(files)
    obs = obs[obs["method"].astype(str).isin(methods)].copy()
    obs = obs[obs["cell_ontology_class"].notna()]
    obs["donor"] = obs["donor"].astype(str)
    obs["cell_type"] = obs["cell_ontology_class"].astype(str)
    obs["stratum"] = obs["tissue"].astype(str) + "|" + obs["cell_type"] + "|" + obs["donor"]
    test_donors = choose_test_donors(obs, test_donor_frac, seed)
    obs["split"] = np.where(obs["donor"].isin(test_donors), "test", "train")
    print(f"{len(obs)} 10X cells, {obs['donor'].nunique()} donors, {obs['tissue'].nunique()} tissues, {obs['cell_type'].nunique()} types; test donors: {test_donors}", flush=True)

    keep = []
    for (stratum, split), g in obs.groupby(["stratum", "split"]):
        if len(g) < min_stratum:
            continue
        cap = test_cap if split == "test" else train_cap
        idx = g.index.values
        if len(idx) > cap:
            idx = rng.choice(idx, cap, replace=False)
        keep.append(idx)
    sel = obs.loc[np.concatenate(keep)].copy()
    # test items must be of a type the probe can learn: drop test types absent from train
    train_types = set(sel.loc[sel["split"] == "train", "cell_type"])
    sel["type_in_train"] = sel["cell_type"].isin(train_types)
    print(f"panel: {(sel['split']=='train').sum()} train / {(sel['split']=='test').sum()} test cells; {sel['stratum'].nunique()} strata; {(~sel['type_in_train'] & (sel['split']=='test')).sum()} test cells of unseen types (kept, flagged)", flush=True)

    blocks, var = [], None
    for p in files:
        rows = sel.loc[sel["file"] == p.name, "row"].sort_values()
        if len(rows) == 0:
            continue
        with h5py.File(p, "r") as f:
            if var is None:
                var = read_elem(f["var"])
            else:
                v = read_elem(f["var"])
                assert (v.index == var.index).all(), f"gene order differs in {p.name}"
            X = sparse_dataset(f["layers/raw_counts"])[rows.values]
        blk = ad.AnnData(X=sp.csr_matrix(X, dtype=np.float32), obs=sel.loc[sel["file"] == p.name].loc[rows.index], var=var)
        blocks.append(blk)
        print(f"  {p.name.split('_')[0]:16s} {blk.n_obs:6d} cells  {time.time()-t0:.0f}s", flush=True)
    panel = ad.concat(blocks, join="inner", merge="same")
    panel.obs_names = sel.loc[panel.obs_names].index if panel.obs_names.isin(sel.index).all() else panel.obs_names
    panel.var = var
    for c in panel.obs.columns:
        if panel.obs[c].dtype == object or str(panel.obs[c].dtype) == "category":
            panel.obs[c] = panel.obs[c].astype(str)
    panel.obs["dataset_id"] = "tabula_sapiens_v2"
    panel.uns["test_donors"] = test_donors
    out_path.parent.mkdir(parents=True, exist_ok=True)
    panel.write_h5ad(out_path)
    print(f"wrote {out_path} {panel.shape} in {time.time()-t0:.0f}s", flush=True)
    return panel

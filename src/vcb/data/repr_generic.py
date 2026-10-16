"""Generic component-A panel builder for a single annotated h5ad (CELLxGENE, Parse, ...).

Same output format as the Tabula Sapiens panel (`repr_panel.py`): raw counts in X (CSR),
obs with cell_type, donor, tissue (= the context column), stratum, split, type_in_train,
dataset_id; uns records the held-out groups.

Split schemes (``split_by``):
  donor    hold out whole donors (default): the probe cannot learn donor identity.
  context  hold out whole contexts (study, tissue, lab, assay ...): cross-context transfer.
Within each stratum (context, cell_type, donor) at most `train_cap` / `test_cap` cells.
The matrix is read in row chunks from the backed file, so a 10M-cell file is fine.
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

from .repr_panel import choose_test_donors


def _counts_source(f: h5py.File, counts: str):
    """Return (dataset-like, encoding) for 'X', 'raw', or 'layers/<name>'."""
    g = f["X"] if counts == "X" else f["raw/X"] if counts == "raw" else f[counts]
    if isinstance(g, h5py.Group):
        return sparse_dataset(g), g.attrs.get("encoding-type", "")
    return g, "dense"


def build_generic_panel(h5ad: Path, name: str, label_key: str, donor_key: str, context_key: str | None, out_path: Path,
                        counts: str = "raw", split_by: str = "donor", test_frac: float = 0.25, test_cap: int = 50, train_cap: int = 200,
                        min_stratum: int = 20, filter_query: str | None = None, seed: int = 0, chunk: int = 100_000, test_groups: list[str] | None = None) -> ad.AnnData:
    t0 = time.time()
    rng = np.random.default_rng(seed)
    with h5py.File(h5ad, "r") as f:
        obs = read_elem(f["obs"])
        var_key = "raw/var" if counts == "raw" and "raw" in f and "var" in f["raw"] else "var"
        var = read_elem(f[var_key])
        M, enc = _counts_source(f, counts)
        n_cells, n_genes = M.shape
        print(f"[{name}] {n_cells:,} cells x {n_genes:,} genes from {counts} ({enc}); obs cols: {list(obs.columns)[:12]}...", flush=True)
        obs = obs.copy()
        obs["row"] = np.arange(n_cells)
        if filter_query:
            obs = obs.query(filter_query)
            print(f"[{name}] filter '{filter_query}' keeps {len(obs):,} cells", flush=True)
        obs = obs[obs[label_key].notna()]
        obs["cell_type"] = obs[label_key].astype(str)
        obs["donor"] = obs[donor_key].astype(str)
        obs["tissue"] = obs[context_key].astype(str) if context_key else name
        obs["stratum"] = obs["tissue"] + "|" + obs["cell_type"] + "|" + obs["donor"]

        if test_groups:
            held = set(test_groups)
        elif split_by == "donor":
            held = set(choose_test_donors(obs.rename(columns={"tissue": "tissue"}), test_frac, seed))
        elif split_by == "context":
            groups = obs["tissue"].value_counts()
            order = list(rng.permutation(groups.index))
            held, n = set(), 0
            for g in order:
                if n >= test_frac * len(obs):
                    break
                held.add(g); n += groups[g]
        else:
            raise ValueError(split_by)
        key = "donor" if split_by == "donor" else "tissue"
        obs["split"] = np.where(obs[key].isin(held), "test", "train")
        print(f"[{name}] split by {key}: held out {sorted(held)[:10]}{' ...' if len(held) > 10 else ''}; {int((obs['split']=='test').sum()):,} test cells before capping", flush=True)

        keep = []
        for (stratum, split), g in obs.groupby(["stratum", "split"], observed=True):
            if len(g) < min_stratum:
                continue
            cap = test_cap if split == "test" else train_cap
            idx = g.index.values
            keep.append(idx if len(idx) <= cap else rng.choice(idx, cap, replace=False))
        sel = obs.loc[np.concatenate(keep)].sort_values("row")
        train_types = set(sel.loc[sel["split"] == "train", "cell_type"])
        sel["type_in_train"] = sel["cell_type"].isin(train_types)
        print(f"[{name}] panel: {int((sel['split']=='train').sum()):,} train / {int((sel['split']=='test').sum()):,} test; {sel['stratum'].nunique()} strata; {sel['cell_type'].nunique()} types; {int((~sel['type_in_train'] & (sel['split']=='test')).sum())} test cells of unseen types", flush=True)

        rows = sel["row"].values
        blocks = []
        if enc == "csc_matrix":
            X = sp.csr_matrix(M[:, :])  # CSC: load whole matrix once (only viable for modest files)
            blocks.append(X[rows])
        else:
            for r0 in range(0, n_cells, chunk):
                r1 = min(r0 + chunk, n_cells)
                m = (rows >= r0) & (rows < r1)
                if m.any():
                    blocks.append(sp.csr_matrix(M[r0:r1])[rows[m] - r0])
                if (r0 // chunk) % 10 == 0:
                    print(f"  rows {r1:,}/{n_cells:,}  {time.time()-t0:.0f}s", flush=True)
        X = sp.vstack(blocks).tocsr().astype(np.float32)
    panel = ad.AnnData(X=X, obs=sel.drop(columns=["row"]), var=var)
    if "feature_name" in panel.var.columns:
        ens = panel.var.index.astype(str).values
        names = panel.var["feature_name"].astype(str).values.copy()
        dup = pd.Series(names).duplicated(keep="first").values
        names[dup] = ens[dup]  # keep symbols unique: duplicates fall back to the Ensembl id
        panel.var["ensembl_id"] = ens
        panel.var.index = pd.Index(names)
    for c in panel.obs.columns:
        if panel.obs[c].dtype == object or str(panel.obs[c].dtype) == "category":
            panel.obs[c] = panel.obs[c].astype(str)
    panel.obs["dataset_id"] = name
    panel.uns["held_out"] = sorted(held)
    panel.uns["split_by"] = split_by
    # a quick integer check on the counts
    sample = X[: min(1000, X.shape[0])].data
    if len(sample) and not np.allclose(sample, np.round(sample)):
        print(f"[{name}] WARNING: counts source does not look like raw integers (e.g. {sample[:5]})", flush=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    panel.write_h5ad(out_path)
    print(f"[{name}] wrote {out_path} {panel.shape} in {time.time()-t0:.0f}s", flush=True)
    return panel

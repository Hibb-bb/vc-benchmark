"""Build component-B items (conditions) from a raw perturbation h5ad.

Streaming over the stored matrix (CSR, CSC or dense are all handled; scPerturb files are
CSC, so the default path chunks over *genes*) produces:

  items h5ad  obs = one row per condition (controls included, flagged), X = mean
              log1p(CP10k) expression (dense float32); obs carries n_cells, context,
              perturbation, dose, time, targets, pert_type, delta_l2; uns['control_stats']
              holds per-context control mean / variance per gene.
  cells h5ad  a subsample of <= cells_per_condition raw-count cells per condition
              (controls get 4x), for cell-level metrics and gene embeddings.

QC: cells with ncounts < min_counts or ngenes < min_genes are dropped first (scPerturb
ships a few near-empty barcodes).
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

from .schema import CONTROL, condition_key, harmonize_scperturb

TARGET_SUM = 1e4


def _open_matrix(f: h5py.File, key: str = "X"):
    g = f[key]
    if isinstance(g, h5py.Group):
        enc = g.attrs.get("encoding-type", "")
        return sparse_dataset(g), enc
    return g, "dense"


def build_items(
    raw_path: Path,
    dataset_id: str,
    out_dir: Path,
    min_cells: int = 50,
    cells_per_condition: int = 500,
    gene_chunk: int = 2000,
    row_chunk: int = 50_000,
    min_counts: float = 500,
    min_genes: int = 200,
    seed: int = 0,
    harmonizer=harmonize_scperturb,
) -> tuple[ad.AnnData, ad.AnnData]:
    t0 = time.time()
    rng = np.random.default_rng(seed)
    out_dir.mkdir(parents=True, exist_ok=True)

    with h5py.File(raw_path, "r") as f:
        obs_raw = read_elem(f["obs"])
        var = read_elem(f["var"])
        M, enc = _open_matrix(f)
        n_cells, n_genes = M.shape
        print(f"[{dataset_id}] {n_cells} cells x {n_genes} genes, matrix={enc}", flush=True)

        obs = harmonizer(obs_raw, dataset_id)
        qc = np.ones(n_cells, dtype=bool)
        if "ncounts" in obs:
            qc &= obs["ncounts"].values >= min_counts
        if "ngenes" in obs:
            qc &= obs["ngenes"].values >= min_genes
        qc &= ~obs["perturbation"].isin(["unassigned", "nan", "None", "*", ""]).values
        obs["condition"] = condition_key(obs)
        obs.loc[obs["is_control"], "condition"] = CONTROL + "::ctx=" + obs.loc[obs["is_control"], "context"].astype(str)
        counts = obs.loc[qc, "condition"].value_counts()
        keep_cond = counts[(counts >= min_cells) | counts.index.str.startswith(CONTROL)].index
        obs["keep"] = qc & obs["condition"].isin(keep_cond)
        cond_codes, cond_names = pd.factorize(obs.loc[obs["keep"], "condition"])
        n_cond = len(cond_names)
        code_full = np.full(n_cells, -1, dtype=np.int64)
        code_full[np.where(obs["keep"].values)[0]] = cond_codes
        print(f"[{dataset_id}] QC keeps {qc.sum()}/{n_cells} cells; {n_cond} conditions with >= {min_cells} cells", flush=True)

        sub_idx = []
        for c, name in enumerate(cond_names):
            idx = np.where(code_full == c)[0]
            cap = cells_per_condition * (4 if name.startswith(CONTROL) else 1)
            if len(idx) > cap:
                idx = rng.choice(idx, cap, replace=False)
            sub_idx.append(idx)
        sub_idx = np.sort(np.concatenate(sub_idx))

        ok = code_full >= 0
        ind = sp.csr_matrix((np.ones(ok.sum(), dtype=np.float32), (code_full[ok], np.where(ok)[0])), shape=(n_cond, n_cells))
        N = np.bincount(code_full[ok], minlength=n_cond)
        ctrl_code_by_ctx = {}
        for c, name in enumerate(cond_names):
            if name.startswith(CONTROL):
                ctrl_code_by_ctx[obs.loc[obs["condition"] == name, "context"].iloc[0]] = c
        ctrl_ind = {ctx: sp.csr_matrix((np.ones((code_full == cc).sum(), dtype=np.float32), (np.zeros((code_full == cc).sum(), dtype=int), np.where(code_full == cc)[0])), shape=(1, n_cells)) for ctx, cc in ctrl_code_by_ctx.items()}

        S = np.zeros((n_cond, n_genes), dtype=np.float64)
        S2_ctrl = {ctx: np.zeros(n_genes, dtype=np.float64) for ctx in ctrl_code_by_ctx}
        sub_blocks = []

        if enc == "csc_matrix":
            # pass 1: per-cell totals; pass 2: group sums of log1p(CP10k), gene chunk by gene chunk
            tot = np.zeros(n_cells, dtype=np.float64)
            for g0 in range(0, n_genes, gene_chunk):
                g1 = min(g0 + gene_chunk, n_genes)
                tot += np.asarray(M[:, g0:g1].sum(axis=1)).ravel()
            tot[tot == 0] = 1.0
            scale = sp.diags((TARGET_SUM / tot).astype(np.float32))
            for g0 in range(0, n_genes, gene_chunk):
                g1 = min(g0 + gene_chunk, n_genes)
                Xc = sp.csr_matrix(M[:, g0:g1])
                sub_blocks.append(Xc[sub_idx])
                Xn = scale @ Xc
                Xn.data = np.log1p(Xn.data)
                S[:, g0:g1] = (ind @ Xn).toarray()
                for ctx, ci in ctrl_ind.items():
                    S2_ctrl[ctx][g0:g1] = (ci @ Xn.multiply(Xn)).toarray().ravel()
                print(f"  genes {g1}/{n_genes}  {time.time()-t0:.0f}s", flush=True)
            Xsub = sp.hstack(sub_blocks).tocsr()
        else:
            sub_mask = np.zeros(n_cells, dtype=bool)
            sub_mask[sub_idx] = True
            for r0 in range(0, n_cells, row_chunk):
                r1 = min(r0 + row_chunk, n_cells)
                Xr = sp.csr_matrix(M[r0:r1])
                if sub_mask[r0:r1].any():
                    sub_blocks.append(Xr[sub_mask[r0:r1]])
                tot = np.asarray(Xr.sum(axis=1)).ravel()
                tot[tot == 0] = 1.0
                Xn = sp.diags((TARGET_SUM / tot).astype(np.float32)) @ Xr
                Xn.data = np.log1p(Xn.data)
                S += (ind[:, r0:r1] @ Xn).toarray()
                for ctx, ci in ctrl_ind.items():
                    S2_ctrl[ctx] += (ci[:, r0:r1] @ Xn.multiply(Xn)).toarray().ravel()
                print(f"  rows {r1}/{n_cells}  {time.time()-t0:.0f}s", flush=True)
            Xsub = sp.vstack(sub_blocks).tocsr()

    mean = (S / np.maximum(N, 1)[:, None]).astype(np.float32)
    item_obs = (
        obs.loc[obs["keep"]].drop_duplicates("condition").set_index("condition")
        .loc[cond_names, ["dataset_id", "perturbation", "targets", "pert_type", "context", "dose", "dose_unit", "time_h", "is_control"]]
    )
    item_obs["n_cells"] = N
    item_obs.index = pd.Index([f"{dataset_id}::{c}" for c in cond_names], name="item_id")
    delta_l2 = np.full(n_cond, np.nan, dtype=np.float32)
    matched = np.zeros(n_cond, dtype=bool)
    for c in range(n_cond):
        cc = ctrl_code_by_ctx.get(item_obs["context"].iloc[c])
        if cc is not None:
            matched[c] = True
            delta_l2[c] = np.linalg.norm(mean[c] - mean[cc])
    item_obs["delta_l2"] = delta_l2
    item_obs["has_matched_control"] = matched
    for col in ["perturbation", "targets", "pert_type", "context", "dose_unit", "dataset_id"]:
        item_obs[col] = item_obs[col].astype(str)

    items = ad.AnnData(X=mean, obs=item_obs, var=var)
    items.uns["control_stats"] = {
        ctx: {"mean": mean[cc].copy(), "var": np.maximum(S2_ctrl[ctx] / max(N[cc], 1) - mean[cc].astype(np.float64) ** 2, 0).astype(np.float32), "n": int(N[cc])}
        for ctx, cc in ctrl_code_by_ctx.items()
    }
    cells_obs = obs.iloc[sub_idx].copy()
    cells_obs["item_id"] = [f"{dataset_id}::{c}" for c in cells_obs["condition"]]
    for col in cells_obs.columns:
        if cells_obs[col].dtype == object:
            cells_obs[col] = cells_obs[col].astype(str)
    cells = ad.AnnData(X=Xsub.astype(np.float32), obs=cells_obs, var=var)

    items.write_h5ad(out_dir / f"{dataset_id}.items.h5ad")
    cells.write_h5ad(out_dir / f"{dataset_id}.cells.h5ad")
    n_items = int((~item_obs["is_control"]).sum())
    print(f"[{dataset_id}] wrote {n_items} items (+{len(ctrl_code_by_ctx)} control rows), {cells.n_obs} subsampled cells, {time.time()-t0:.0f}s", flush=True)
    return items, cells

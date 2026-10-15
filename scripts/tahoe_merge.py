#!/usr/bin/env python
"""Merge Tahoe shard-task outputs into the benchmark item format.

  python scripts/tahoe_merge.py [--min-ctrl-mean 0.01] [--cells-per-condition 30] [--parts-glob 'task_*']

Produces data/items/tahoe100m.items.h5ad and tahoe100m.cells.h5ad with the same obs schema
as the scPerturb items (perturbation = drug, dose from sample metadata, context = cell line
name, pert_type = drug, plus `smiles` for chemical features). Gene space is restricted to
genes with pooled control mean log-expression above `--min-ctrl-mean` (keeps the matrices
tractable; ~20k genes instead of 62.7k).
"""
import argparse
import ast
import glob
from pathlib import Path

import anndata as ad
import h5py
import numpy as np
from anndata.io import read_elem, sparse_dataset
import pandas as pd
import scipy.sparse as sp

from vcb import DATA

ap = argparse.ArgumentParser()
ap.add_argument("--parts-glob", default="task_*")
ap.add_argument("--min-ctrl-mean", type=float, default=0.01)
ap.add_argument("--cells-per-condition", type=int, default=30)
ap.add_argument("--cells-per-control", type=int, default=1000)
ap.add_argument("--out-name", default="tahoe100m")
ap.add_argument("--cells-only", action="store_true", help="items file exists; only (re)build the cells file")
a = ap.parse_args()

parts = DATA / "raw" / "tahoe" / "parts"
meta_dir = DATA / "raw" / "tahoe" / "meta"
genes = pd.read_parquet(meta_dir / "gene_metadata.parquet")
samples = pd.read_parquet(meta_dir / "sample_metadata.parquet").set_index("sample")
lines = pd.read_parquet(meta_dir / "cell_line_metadata.parquet").drop_duplicates("Cell_ID_Cellosaur").set_index("Cell_ID_Cellosaur")
lines["cell_name"] = lines["cell_name"].astype(str).str.replace("/", "_", regex=False)  # 'HepG2/C3A' would nest in h5py
drugs = pd.read_parquet(meta_dir / "drug_metadata.parquet").drop_duplicates("drug").set_index("drug")

npzs = sorted(glob.glob(str(parts / f"{a.parts_glob}.npz")))
print(f"{len(npzs)} parts")
if a.cells_only:
    items = ad.read_h5ad(DATA / "items" / f"{a.out_name}.items.h5ad", backed="r")
    item_obs = items.obs.copy()
    var = items.var.copy()
    col = var["token_id"].values.astype(int)
    # rebuild the condition-key -> item_id map from the parts' meta
    metas = pd.concat([pd.read_parquet(f.replace(".npz", ".meta.parquet")) for f in npzs]); metas = metas[~metas.index.duplicated()]
    samples_ = samples
    def parse_conc(s):
        try:
            lst = ast.literal_eval(s); return float(lst[0][1])
        except Exception:
            return np.nan
    line_name = metas["cell_line_id"].map(lambda c: lines.loc[c, "cell_name"] if c in lines.index else c)
    conc = metas["sample"].map(lambda smp: parse_conc(samples_.loc[smp, "drugname_drugconc"]) if smp in samples_.index else np.nan)
    is_ctrl = metas["drug"] == "DMSO_TF"
    item_key = np.where(is_ctrl, "control::ctx=" + line_name.astype(str), metas["drug"].astype(str) + "::ctx=" + line_name.astype(str) + "::dose=" + conc.astype(str))
    key2item = dict(zip(metas.index, [f"{a.out_name}::{k}" for k in item_key]))
else:
    npzs = sorted(glob.glob(str(parts / f"{a.parts_glob}.npz")))
    print(f"{len(npzs)} parts")
    S, N, metas, ctrl_sq = {}, {}, [], {}
    total_cells = 0
    for f in npzs:
        z = np.load(f, allow_pickle=True)
        total_cells += int(z["n_cells"])
        for k, s, n in zip(z["keys"], z["S"], z["N"]):
            if k in S:
                S[k] += s; N[k] += n
            else:
                S[k] = s.astype(np.float32); N[k] = int(n)
        for l, sq in zip(z["ctrl_lines"], z["ctrl_sq"]):
            ctrl_sq[l] = ctrl_sq.get(l, 0) + sq
        metas.append(pd.read_parquet(f.replace(".npz", ".meta.parquet")))
    meta = pd.concat(metas); meta = meta[~meta.index.duplicated()]
    keys = list(S)
    print(f"{total_cells} cells, {len(keys)} conditions")

    # gene space: tokens present in gene_metadata, with pooled control mean above threshold
    tok = genes["token_id"].values.astype(int)
    ctrl_keys = [k for k in keys if meta.loc[k, "drug"] == "DMSO_TF"]
    ctrl_sum = np.sum([S[k] for k in ctrl_keys], axis=0); ctrl_n = sum(N[k] for k in ctrl_keys)
    ctrl_mean = ctrl_sum / max(ctrl_n, 1)
    keep_tok = tok[ctrl_mean[tok] > a.min_ctrl_mean]
    var = genes.set_index("gene_symbol").loc[genes["token_id"].isin(keep_tok).values, ["ensembl_id", "token_id"]]
    var = var[~var.index.duplicated()]
    col = var["token_id"].values.astype(int)
    print(f"genes kept: {len(col)} of {len(tok)} (control mean > {a.min_ctrl_mean})")

    # item table
    def parse_conc(s):
        try:
            lst = ast.literal_eval(s)
            return float(lst[0][1]), str(lst[0][2])
        except Exception:
            return np.nan, ""
    rows = []
    for k in keys:
        m = meta.loc[k]
        conc, unit = parse_conc(samples.loc[m["sample"], "drugname_drugconc"]) if m["sample"] in samples.index else (np.nan, "")
        line_name = lines.loc[m["cell_line_id"], "cell_name"] if m["cell_line_id"] in lines.index else m["cell_line_id"]
        is_ctrl = m["drug"] == "DMSO_TF"
        rows.append(dict(key=k, dataset_id=a.out_name, perturbation="control" if is_ctrl else m["drug"], targets="", pert_type="control" if is_ctrl else "drug",
                         context=line_name, dose=np.nan if is_ctrl else conc, dose_unit=unit, time_h=24.0, is_control=is_ctrl, n_cells=N[k],
                         sample=m["sample"], plate=m["plate"], cell_line_id=m["cell_line_id"],
                         smiles=("" if is_ctrl else str(drugs.loc[m["drug"], "canonical_smiles"]) if m["drug"] in drugs.index else "")))
    obs = pd.DataFrame(rows).set_index("key")
    # controls: one row per cell line (pool DMSO samples across plates); treated: one row per (drug, dose, line)
    X_full = np.stack([S[k] / max(N[k], 1) for k in keys]).astype(np.float32)[:, col]
    obs["item_key"] = np.where(obs["is_control"], "control::ctx=" + obs["context"], obs["perturbation"] + "::ctx=" + obs["context"] + "::dose=" + obs["dose"].astype(str))
    agg_idx = {}
    for i, ik in enumerate(obs["item_key"]):
        agg_idx.setdefault(ik, []).append(i)
    item_keys = list(agg_idx)
    Xi = np.zeros((len(item_keys), X_full.shape[1]), dtype=np.float32)
    n_i = np.zeros(len(item_keys), dtype=np.int64)
    for j, ik in enumerate(item_keys):
        idx = agg_idx[ik]
        w = obs["n_cells"].values[idx].astype(np.float64)
        Xi[j] = (X_full[idx] * (w / w.sum())[:, None]).sum(0)
        n_i[j] = w.sum()
    item_obs = obs.iloc[[agg_idx[ik][0] for ik in item_keys]].copy()
    item_obs["n_cells"] = n_i
    item_obs["n_samples_pooled"] = [len(agg_idx[ik]) for ik in item_keys]
    item_obs.index = pd.Index([f"{a.out_name}::{ik}" for ik in item_keys], name="item_id")
    item_obs = item_obs.drop(columns=["item_key", "sample"])
    ctrl_row = {c: j for j, c in enumerate(item_obs["context"]) if item_obs["is_control"].iloc[j]}
    item_obs["has_matched_control"] = item_obs["context"].map(lambda c: c in ctrl_row)
    item_obs["delta_l2"] = [np.linalg.norm(Xi[j] - Xi[ctrl_row[c]]) if c in ctrl_row else np.nan for j, c in enumerate(item_obs["context"])]
    for c in ["perturbation", "targets", "pert_type", "context", "dose_unit", "dataset_id", "plate", "cell_line_id", "smiles"]:
        item_obs[c] = item_obs[c].astype(str)

    items = ad.AnnData(X=Xi, obs=item_obs, var=var)
    cs = {}
    for c, j in ctrl_row.items():
        cid = item_obs["cell_line_id"].iloc[j]
        mu = Xi[j].astype(np.float64)
        sq = ctrl_sq.get(cid, np.zeros(len(ctrl_mean)))[col] / max(n_i[j], 1)
        cs[c] = {"mean": Xi[j].copy(), "var": np.maximum(sq - mu**2, 0).astype(np.float32), "n": int(n_i[j])}
    items.uns["control_stats"] = cs
    DATA.joinpath("items").mkdir(exist_ok=True)
    items.write_h5ad(DATA / "items" / f"{a.out_name}.items.h5ad")
    n_items = int((~item_obs["is_control"]).sum())
    print(f"items: {n_items} treated + {len(ctrl_row)} control rows; median cells/item {np.median(n_i[~item_obs['is_control'].values]):.0f}")

    key2item = dict(zip(obs.index, item_obs.index[[item_keys.index(ik) for ik in obs["item_key"]]]))

# cells: choose <= cap cells per item from the parts' obs, then load only those rows
rng = np.random.default_rng(0)
obs_parts = []
for f in npzs:
    with h5py.File(f.replace(".npz", ".cells.h5ad")) as h:
        o = read_elem(h["obs"])
    o["part"] = f; o["row"] = np.arange(len(o)); obs_parts.append(o)
cobs = pd.concat(obs_parts, ignore_index=True)
cobs["item_id"] = cobs["cond_key"].map(key2item).astype(str)
keep = []
for iid, idx in cobs.groupby("item_id", sort=False).indices.items():
    cap = a.cells_per_control if "::control::" in iid else a.cells_per_condition
    keep.append(idx if len(idx) <= cap else rng.choice(idx, cap, replace=False))
cobs = cobs.iloc[np.sort(np.concatenate(keep))]
print(f"cells selected: {len(cobs)} of {sum(len(o) for o in obs_parts)}")
blocks = []
for f, g in cobs.groupby("part", sort=False):
    with h5py.File(f.replace(".npz", ".cells.h5ad")) as h:
        X = sparse_dataset(h["X"])[np.sort(g["row"].values)]
    blocks.append(sp.csr_matrix(X)[:, col])
Xc = sp.vstack(blocks).tocsr().astype(np.float32)
cobs = cobs.sort_values(["part", "row"])
cells = ad.AnnData(X=Xc, obs=cobs.drop(columns=["part", "row"]).set_index(pd.Index([f"{p.split('/')[-1].split('.')[0]}:{r}" for p, r in zip(cobs["part"], cobs["row"])])), var=var)
cells.obs["is_control"] = (cells.obs["drug"].astype(str) == "DMSO_TF")
cells.obs["context"] = cells.obs["item_id"].map(item_obs["context"]).astype(str)
cells.obs["perturbation"] = cells.obs["item_id"].map(item_obs["perturbation"]).astype(str)
for c in cells.obs.columns:
    if cells.obs[c].dtype == object or str(cells.obs[c].dtype) == "category":
        cells.obs[c] = cells.obs[c].astype(str)
cells.write_h5ad(DATA / "items" / f"{a.out_name}.cells.h5ad")
print(f"cells: {cells.n_obs} x {cells.n_vars}")

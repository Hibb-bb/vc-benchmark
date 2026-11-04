#!/usr/bin/env python
"""Why do text cards help so little on Parse cytokines? Separate the data, the text and the embedding.

  .venv/bin/python scripts/pert_text/cytokine_diagnosis.py        # Slurm: loads the Parse items file

Per cell type (donor-averaged response of each cytokine, 2,000 HVGs, cytokines with a clear response only):
1. Data: how many cytokines respond clearly; how much of the response variance one shared programme carries;
   how reproducible a cytokine's response is between donor halves (the ceiling for any description).
2. Text vs biology: whether cytokines of the same family, or sharing a receptor subunit, respond alike. Family and
   receptors are exactly what the cards state, so if family-mates do not respond alike, no card can help.
3. Embedding: how well each similarity predicts response correlation (Spearman over cytokine pairs, and the mean
   response correlation with each cytokine's 3 nearest neighbours): full-card embedding, name-only embedding,
   family labels, shared receptor genes, and receptor expression in that cell type (not in the card).
Writes runs/pert_text/cytokine_diagnosis.{md,csv}.
"""
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import DATA
from vcb.pert.folds import item_table
from vcb.pert.run import hvg_mask

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "runs" / "pert_text"
rng = np.random.default_rng(0)
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", default="parse_pbmc_cytokines")
ap.add_argument("--cards", default="runs/pert_text/emb", help="embedding dir with keys.txt")
ap.add_argument("--table", default="src/vcb/data/parse_cytokines.tsv")
ap.add_argument("--min-snr", type=float, default=1.5)
A_ = ap.parse_args()

items = ad.read_h5ad(DATA / "items" / f"{A_.dataset}.items.h5ad")
meta, D, _ = item_table(items)
D = D[:, hvg_mask(items)].astype(np.float32)
del items
PARSE = A_.dataset == "parse_pbmc_cytokines"
meta = meta.reset_index(drop=True)
meta["cytokine"] = meta["perturbation"].astype(str)
if PARSE:
    fac = pd.read_parquet(ROOT / "runs" / "pert_pool_v0" / "analysis_parse" / "item_factors.parquet").set_index(["perturbation", "context"])
    meta["donor"], meta["cell_type"] = zip(*meta["context"].astype(str).str.split("|", n=1))
    idx = pd.MultiIndex.from_arrays([meta["perturbation"].astype(str), meta["context"].astype(str)])
    meta["snr"] = fac["snr"].reindex(idx).values
    meta["receptor_expr"] = fac["receptor_expr"].reindex(idx).values
    ref = pd.read_csv(ROOT / A_.table, sep="\t", keep_default_na=False).set_index("cytokine")
else:
    # Immune Dictionary: one item per (cytokine, cell type), mice pooled; no per-item SNR or receptor table, so
    # "clear" = the stronger half of responses in that cell type and the receptor-expression similarity is skipped
    meta["donor"], meta["cell_type"] = "pooled", meta["context"].astype(str)
    meta["norm"] = np.linalg.norm(D, axis=1)
    meta["snr"] = meta["norm"] / meta.groupby("cell_type")["norm"].transform("median") * 1.5
    meta["receptor_expr"] = np.nan
    ref = pd.read_csv(ROOT / A_.table, sep="\t", keep_default_na=False).set_index("label")
EMB = ROOT / A_.cards
keys = (EMB / "keys.txt").read_text().splitlines()
kpos = {k: i for i, k in enumerate(keys)}
EF = np.load(EMB / "Qwen3-Embedding-4B.full.npy").astype(np.float32)
EN = np.load(EMB / "Qwen3-Embedding-4B.name.npy").astype(np.float32)


def cos(X):
    X = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
    return X @ X.T


def corr(X):
    X = X - X.mean(1, keepdims=True)
    return cos(X)


CELL_TYPES = meta.groupby("cell_type")["n_cells"].sum().sort_values(ascending=False).index[:8] if "n_cells" in meta else meta["cell_type"].value_counts().index[:8]
rows, sim_rows = [], []
for ct in CELL_TYPES:
    m = meta[meta["cell_type"] == ct]
    # clear in at least half the donors (median SNR >= 1.5)
    med = m.groupby("cytokine")["snr"].median()
    clear = sorted(c for c in med[med >= 1.5].index if c in ref.index and f"cytokine::{c}" in kpos)
    n_all = m["cytokine"].nunique()
    if len(clear) < 8:
        rows.append({"cell_type": ct, "cytokines": n_all, "clear": len(clear)})
        continue
    P = np.stack([D[m.index[m["cytokine"] == c]].mean(0) for c in clear])
    # split-half reproducibility across donors
    rep = []
    for c in clear:
        idx = m.index[m["cytokine"] == c].values
        if len(idx) < 4:
            continue
        perm = rng.permutation(idx)
        h1, h2 = D[perm[: len(idx) // 2]].mean(0), D[perm[len(idx) // 2:]].mean(0)
        rep.append(np.corrcoef(h1, h2)[0, 1])
    # one shared programme?
    Pc = P - P.mean(0)
    sv = np.linalg.svd(P, compute_uv=False) ** 2
    pc1 = sv[0] / sv.sum()
    C = corr(P)
    iu = np.triu_indices(len(clear), 1)
    fam = ref.loc[clear, "family"].values
    same_fam = (fam[:, None] == fam[None, :])[iu]
    rec = [set(ref.at[c, "receptor_genes"].split(",")) - {""} for c in clear]
    share_rec = np.array([[len(a & b) > 0 for b in rec] for a in rec])[iu]
    r_expr = m.groupby("cytokine")["receptor_expr"].mean().reindex(clear).fillna(0).values
    sims = {
        "text card (full)": cos(EF[[kpos[f"cytokine::{c}"] for c in clear]]),
        "text name only": cos(EN[[kpos[f"cytokine::{c}"] for c in clear]]),
        "same family (label)": (fam[:, None] == fam[None, :]).astype(float),
        "shared receptor gene": np.array([[len(a & b) / max(1, len(a | b)) for b in rec] for a in rec]),
    }
    if PARSE:
        sims["receptor expressed here"] = -np.abs(np.log1p(r_expr)[:, None] - np.log1p(r_expr)[None, :])
    off = ~np.eye(len(clear), dtype=bool)
    rand_nn = C[off].mean()
    row = {"cell_type": ct, "cytokines": n_all, "clear": len(clear), "PC1 share": pc1,
           "donor split-half r (median)": float(np.median(rep)) if rep else np.nan,
           "resp corr same family": C[iu][same_fam].mean() if same_fam.any() else np.nan,
           "resp corr different family": C[iu][~same_fam].mean(),
           "resp corr shared receptor": C[iu][share_rec].mean() if share_rec.any() else np.nan,
           "resp corr no shared receptor": C[iu][~share_rec].mean(),
           "mean resp corr (any pair)": rand_nn}
    rows.append(row)
    for name, S in sims.items():
        S = S.copy(); np.fill_diagonal(S, -np.inf)
        nn = np.argsort(-S, axis=1)[:, :3]
        nn_corr = np.mean([C[i, nn[i]].mean() for i in range(len(clear))])
        rho = spearmanr(S[iu], C[iu]).statistic
        sim_rows.append({"cell_type": ct, "similarity": name, "spearman vs response corr": rho,
                         "response corr of 3 nearest": nn_corr, "any pair": rand_nn})
    print(f"[diag] {ct}: {len(clear)} clear of {n_all}", flush=True)

A = pd.DataFrame(rows)
S = pd.DataFrame(sim_rows)
sfx = "" if PARSE else "_" + A_.dataset
A.to_csv(T / f"cytokine_diagnosis{sfx}.csv", index=False)
S.to_csv(T / f"cytokine_diagnosis_similarity{sfx}.csv", index=False)
agg = S.groupby("similarity")[["spearman vs response corr", "response corr of 3 nearest", "any pair"]].mean().sort_values("spearman vs response corr", ascending=False)
md = [f"# Why text cards help little on cytokines ({A_.dataset})", "", "## Data, per cell type", "", A.round(3).to_markdown(index=False), "",
      "## Which similarity predicts response similarity (mean over cell types)", "", agg.round(3).to_markdown(), "",
      "## Per cell type", "", S.round(3).to_markdown(index=False), ""]
(T / f"cytokine_diagnosis{sfx}.md").write_text("\n".join(md))
print("\n".join(md))

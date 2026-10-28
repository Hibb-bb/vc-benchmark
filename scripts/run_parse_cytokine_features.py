#!/usr/bin/env python
"""Parse cytokine respondents whose perturbation features describe each cytokine by its genes.

  .venv/bin/python scripts/run_parse_cytokine_features.py --source scgpt [--scheme perturbation]

A cytokine is described by the representation of its ligand gene(s) and its receptor gene(s)
(src/vcb/data/parse_cytokines.tsv), taken from a pretrained model (runs/pert_pool_v0/cytokine_features/
<source>.parquet, built by build_cytokine_gene_features.py) or, as the no-pretraining control
(--source ctrlpca), from a gene embedding fitted on Parse's own control cells. The two halves are
averaged over subunits, concatenated, standardised and reduced by PCA over the 90 cytokines to 32
dimensions, then joined to a one-hot context. Because the description is built from genes, it exists
for a cytokine the model never saw, which is what the unseen-cytokine split needs.

The standard feature-driven models (ridge, KNN, Gaussian process, MLP on a 50-PC response basis) are
fitted on these features in the benchmark's own folds and appended to the scores table under
respondent ids with the suffix `_g<source>`; nothing else in the table changes.
"""
import argparse
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from vcb import DATA, RUNS
from vcb.pert.baselines import GPPCA, KNNShift, MLPPCA, RidgePCA
from vcb.pert.features import gene_embedding_from_controls
from vcb.pert.run import evaluate_dataset

DS = "parse_pbmc_cytokines"
ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--source", required=True, choices=["scgpt", "geneformer", "scfoundation", "esm2", "ctrlpca"])
ap.add_argument("--scheme", default=None, help="context or perturbation (default: both)")
ap.add_argument("--dim", type=int, default=32)
a = ap.parse_args()

ref = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False).set_index("cytokine")
if a.source == "ctrlpca":
    cells = ad.read_h5ad(DATA / "items" / f"{DS}.cells.h5ad", backed="r")
    ctrl = np.where(cells.obs["is_control"].values.astype(bool))[0]
    rng = np.random.default_rng(0)
    pick = np.sort(rng.choice(ctrl, min(5000, len(ctrl)), replace=False))
    emb = gene_embedding_from_controls(cells[pick].to_memory().X, cells.var_names.astype(str), dim=64)
else:
    emb = pd.read_parquet(RUNS / "pert_pool_v0" / "cytokine_features" / f"{a.source}.parquet")


def part(genes):
    gs = [g for g in genes.split(",") if g and g in emb.index]
    return (emb.loc[gs].values.mean(0), True) if gs else (np.zeros(emb.shape[1], np.float32), False)


rows, ok = {}, {}
for c, r in ref.iterrows():
    lig, f1 = part(r["ligand_genes"])
    rec, f2 = part(r["receptor_genes"])
    rows[c] = np.concatenate([lig, rec])
    ok[c] = f1 or f2
M = pd.DataFrame(rows).T
Z = (M - M.mean()) / (M.std() + 1e-6)
k = min(a.dim, Z.shape[0] - 1)
cyt = pd.DataFrame(PCA(n_components=k, random_state=0).fit_transform(Z.fillna(0).values), index=M.index)
print(f"{a.source}: {M.shape[1]}-dim cytokine descriptions -> {k} PCs; described {sum(ok.values())}/{len(ok)} cytokines")


def features(meta):
    p = meta["perturbation"].astype(str)
    Fc = np.stack([cyt.loc[x].values if x in cyt.index else np.zeros(k) for x in p]).astype(np.float32)
    ctx = pd.get_dummies(meta["context"].astype(str), prefix="c").values.astype(np.float32)
    return np.hstack([Fc, ctx]), np.array([ok.get(x, False) for x in p])


def pool():
    models = [RidgePCA(d=50, lam=100.0), KNNShift(k=20), GPPCA(d=50, ls_mult=1.0), MLPPCA(d=50, hidden=256)]
    for m in models:
        m.name = f"{m.name}_g{a.source}"
    return models


for scheme in ([a.scheme] if a.scheme else ["perturbation", "context"]):
    evaluate_dataset(DATA / "items" / f"{DS}.items.h5ad", DATA / "items" / f"{DS}.cells.h5ad", RUNS / "pert_pool_v0",
                     scheme=scheme, pool=pool(), merge=True, features=features)

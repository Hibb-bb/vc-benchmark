"""Perturbation features for unseen-perturbation prediction.

Genetic items: a target-gene embedding learned from *control cells only* (no leakage):
genes are rows, cells are columns of the log-normalized control matrix; standardize each
gene, run PCA across cells -> `dim` coordinates per gene. Multi-gene perturbations average
their targets. Also appended: control mean expression and detection fraction of the target.

Chemical / other items: one-hot of perturbation identity (seen-perturbation, unseen-context
scenario) plus one-hot context and log-dose. These cannot support unseen-perturbation
prediction without chemical descriptors, which v0 does not include.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.decomposition import PCA


def gene_embedding_from_controls(cells_ctrl, var_names: pd.Index, dim: int = 64, max_cells: int = 5000, seed: int = 0) -> pd.DataFrame:
    """cells_ctrl: raw-count sparse matrix of control cells (n_cells x n_genes)."""
    rng = np.random.default_rng(seed)
    X = sp.csr_matrix(cells_ctrl, dtype=np.float32)
    if X.shape[0] > max_cells:
        X = X[np.sort(rng.choice(X.shape[0], max_cells, replace=False))]
    tot = np.asarray(X.sum(axis=1)).ravel()
    tot[tot == 0] = 1
    X = sp.diags((1e4 / tot).astype(np.float32)) @ X
    X.data = np.log1p(X.data)
    G = X.T.toarray().astype(np.float32)             # genes x cells
    mu = G.mean(1, keepdims=True)
    sd = G.std(1, keepdims=True) + 1e-6
    Gz = (G - mu) / sd
    k = min(dim, Gz.shape[1] - 1, Gz.shape[0] - 1)
    Z = PCA(n_components=k, random_state=seed).fit_transform(Gz)
    emb = pd.DataFrame(Z, index=var_names, columns=[f"ge{i}" for i in range(k)])
    emb["ctrl_mean"] = mu.ravel()
    emb["ctrl_detect"] = np.asarray((X > 0).mean(axis=0)).ravel()
    return emb


def genetic_item_features(items_obs: pd.DataFrame, gene_emb: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Average target embeddings per item. Returns (F, found_mask)."""
    F = np.zeros((len(items_obs), gene_emb.shape[1]), dtype=np.float32)
    found = np.zeros(len(items_obs), dtype=bool)
    for i, t in enumerate(items_obs["targets"].astype(str)):
        genes = [g for g in t.split("|") if g and g in gene_emb.index]
        if genes:
            F[i] = gene_emb.loc[genes].values.mean(0)
            found[i] = True
    return F, found


def categorical_item_features(items_obs: pd.DataFrame) -> np.ndarray:
    pert = pd.get_dummies(items_obs["perturbation"].astype(str), prefix="p").values.astype(np.float32)
    ctx = pd.get_dummies(items_obs["context"].astype(str), prefix="c").values.astype(np.float32)
    dose = np.log10(items_obs["dose"].fillna(0).values.astype(np.float32) + 1e-3)[:, None]
    return np.hstack([pert, ctx, dose])


def chemical_item_features(items_obs: pd.DataFrame, n_bits: int = 1024, radius: int = 2) -> tuple[np.ndarray, np.ndarray]:
    """Morgan fingerprint of the compound + log10 dose + one-hot context. Requires an obs
    column `smiles`. Returns (F, found_mask); items without a parsable SMILES get zeros."""
    from rdkit import Chem, RDLogger
    from rdkit.Chem import rdFingerprintGenerator
    RDLogger.DisableLog("rdApp.*")
    gen = rdFingerprintGenerator.GetMorganGenerator(radius=radius, fpSize=n_bits)
    cache = {}
    fp = np.zeros((len(items_obs), n_bits), dtype=np.float32)
    found = np.zeros(len(items_obs), dtype=bool)
    for i, smi in enumerate(items_obs["smiles"].astype(str)):
        if smi in cache:
            v = cache[smi]
        else:
            mol = Chem.MolFromSmiles(smi) if smi and smi not in ("nan", "None") else None
            v = np.array(gen.GetFingerprintAsNumPy(mol), dtype=np.float32) if mol is not None else None
            cache[smi] = v
        if v is not None:
            fp[i] = v
            found[i] = True
    ctx = pd.get_dummies(items_obs["context"].astype(str), prefix="c").values.astype(np.float32)
    dose = np.log10(items_obs["dose"].fillna(0).values.astype(np.float32) + 1e-3)[:, None]
    return np.hstack([fp, ctx, dose]), found

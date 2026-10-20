"""Shared-encoder respondents for component B: a component-A embedding as the latent space of
a perturbation model whose other parts are held fixed.

Question: does a representation that is good at the annotation task (component A) also carry
perturbation responses? For every unsupervised embedder of the component-A pool (PCA, random
projection, Nyström, NMF, ICA, GMM, depth, random) we build one perturbation respondent,
`latent_<embedder>`, with the same recipe:

  1. cells of the training items (<= `cells_per_item` each) plus the control cells of every
     context are preprocessed exactly as in component A (log1p CP10k, 2,000 HVGs chosen on
     these cells, z-scored, clipped) and the embedder is fitted on them;
  2. every training item gets a latent pseudobulk z = mean latent of its cells, every context a
     latent control mean z_c; the item's latent response is d = z - z_c;
  3. a linear decoder W (ridge from the latent to log1p CP10k expression of the same cells, both
     centred) maps a latent response back to genes: delta_hat = W d_hat;
  4. the latent response of a test item is predicted by the same rule for every encoder:
       context scheme     mean latent response of the same perturbation (and dose) in its
                          training contexts; a perturbation never seen falls back to the mean
                          latent response of the test item's context (the latent mean shift);
       perturbation scheme  ridge from the item features (gene embedding, fingerprint or
                          one-hot) to the latent response, as RidgePCA does onto a delta basis.

So the only thing that varies across the family is the encoder. For a linear encoder the
prediction is the gene-space response projected onto the encoder's subspace; for the others the
decoder is the best linear read-out of the latent. Nothing about the test item's cells is used:
in the context scheme its cells are excluded from steps 1 to 3, in the perturbation scheme every
cell of the held-out perturbation is.
"""
from __future__ import annotations

import time

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.linear_model import Ridge

from ..repr.embedders import Embedder, Preprocessor, default_pool as repr_default_pool
from .baselines import Baseline

TARGET_SUM = 1e4


class LatentCellCache:
    """The cell subsample (<= cells_per_item per item, <= ctrl_per_context control cells per context),
    read once from the cells file by row selection, then preprocessed per fold on the training items."""

    def __init__(self, cells_path, cells_per_item: int = 30, ctrl_per_context: int = 2000, decoder_cells: int = 40000, seed: int = 0):
        import h5py
        from anndata.io import read_elem
        t0 = time.time()
        rng = np.random.default_rng(seed)
        with h5py.File(cells_path, "r") as f:
            obs = read_elem(f["obs"])
            var_names = pd.Index(read_elem(f["var"]).index)
        item = obs["item_id"].astype(str).values
        ctrl = obs["is_control"].values.astype(bool)
        order = np.argsort(item, kind="stable")
        item_sorted = item[order]
        starts = np.r_[0, np.where(item_sorted[1:] != item_sorted[:-1])[0] + 1, len(order)]
        idx = []
        for s, e in zip(starts[:-1], starts[1:]):
            block = order[s:e]
            cap = ctrl_per_context if ctrl[block[0]] else cells_per_item
            idx.append(block if len(block) <= cap else rng.choice(block, cap, replace=False))
        sel = np.sort(np.concatenate(idx))
        backed = ad.read_h5ad(cells_path, backed="r")
        self.X = sp.csr_matrix(backed[sel].to_memory().X, dtype=np.float32)
        backed.file.close()
        self.var_names = var_names
        self.item_of_cell = item[sel]
        self.ctx_of_cell = obs["context"].astype(str).values[sel]
        self.is_ctrl = ctrl[sel]
        self.decoder_cells, self.seed = decoder_cells, seed
        self.key = None
        print(f"  latent cache: {len(sel)} of {len(obs)} cells read ({self.is_ctrl.sum()} control) in {time.time()-t0:.0f}s", flush=True)

    def prepare(self, train_items: pd.Index):
        key = hash(tuple(sorted(train_items.astype(str))))
        if key == self.key:
            return
        t0 = time.time()
        allowed = set(train_items.astype(str))
        keep = self.is_ctrl | np.array([i in allowed for i in self.item_of_cell])
        X = self.X[keep]
        self.sel_item = self.item_of_cell[keep]
        self.sel_ctx = self.ctx_of_cell[keep]
        self.sel_ctrl = self.is_ctrl[keep]
        prep = Preprocessor(n_hvg=2000, seed=self.seed).fit(X, self.var_names)
        self.mats = {"scaled": prep.transform(X), "log": prep.transform(X, scaled=False), "depth": Preprocessor.depth_features(X)}
        # log1p CP10k over all genes for the decoder, on a subsample of the same cells
        rng = np.random.default_rng(self.seed)
        n = X.shape[0]
        dec = np.arange(n) if n <= self.decoder_cells else np.sort(rng.choice(n, self.decoder_cells, replace=False))
        Xd = X[dec]
        tot = np.asarray(Xd.sum(1)).ravel()
        tot[tot == 0] = 1.0
        Xd = sp.diags((TARGET_SUM / tot).astype(np.float32)) @ Xd
        Xd.data = np.log1p(Xd.data)
        self.dec_rows = dec
        self.dec_X = sp.csr_matrix(Xd)
        self.dec_mu = np.asarray(self.dec_X.mean(0)).ravel().astype(np.float32)
        self.key = key
        print(f"  latent cache: {n} cells ({self.sel_ctrl.sum()} control) preprocessed in {time.time()-t0:.0f}s", flush=True)


class LatentShift(Baseline):
    def __init__(self, embedder: Embedder, cache: LatentCellCache, scheme: str, lam_dec: float = 10.0, lam_feat: float = 10.0):
        self.emb, self.cache, self.scheme, self.lam_dec, self.lam_feat = embedder, cache, scheme, lam_dec, lam_feat
        self.name = f"latent_{embedder.name}"

    def fit(self, F, D, meta):
        c = self.cache
        c.prepare(meta.index)
        X = c.mats[self.emb.needs]
        self.emb.fit(X)
        Z = np.asarray(self.emb.transform(X), dtype=np.float64)
        # latent pseudobulk per training item and per context's controls
        df = pd.DataFrame(Z)
        df["key"] = np.where(c.sel_ctrl, "ctrl::" + pd.Series(c.sel_ctx).values, pd.Series(c.sel_item).values)
        means = df.groupby("key").mean()
        z_ctrl = {k[len("ctrl::"):]: means.loc[k].values for k in means.index if k.startswith("ctrl::")}
        ids = meta.index.astype(str)
        have = np.array([i in means.index and ctx in z_ctrl for i, ctx in zip(ids, meta["context"].astype(str))])
        d = np.zeros((len(meta), Z.shape[1]))
        for r, (i, ctx) in enumerate(zip(ids, meta["context"].astype(str))):
            if have[r]:
                d[r] = means.loc[i].values - z_ctrl[ctx]
        self.d_train_, self.have_ = d, have
        # linear decoder latent -> genes (centred ridge, closed form)
        Zd = Z[c.dec_rows] - Z[c.dec_rows].mean(0)
        k = Zd.shape[1]
        G = Zd.T @ Zd + self.lam_dec * np.eye(k)
        ZtX = np.asarray((c.dec_X.T @ Zd).T) - np.outer(Zd.sum(0), c.dec_mu)   # k x genes, centred X
        self.W_ = np.linalg.solve(G, ZtX).astype(np.float32)                      # k x genes
        # predictor of the latent response
        tr = meta[have].copy()
        tr_d = d[have]
        self.ctx_mean_ = {ctx: tr_d[(tr["context"].astype(str) == ctx).values].mean(0) for ctx in tr["context"].astype(str).unique()}
        self.global_mean_ = tr_d.mean(0) if len(tr_d) else np.zeros(Z.shape[1])
        if self.scheme == "context":
            pk = tr["pert_key"].astype(str) if "pert_key" in tr else tr["perturbation"].astype(str)
            self.by_pert_ = pd.DataFrame(tr_d, index=pk.values).groupby(level=0).mean()
        else:
            from sklearn.preprocessing import StandardScaler
            self.scaler_ = StandardScaler().fit(F[have])
            self.reg_ = Ridge(alpha=self.lam_feat).fit(self.scaler_.transform(F[have]), tr_d)
        return self

    def predict(self, F, meta):
        if self.scheme == "context":
            pk = meta["pert_key"].astype(str) if "pert_key" in meta else meta["perturbation"].astype(str)
            out = np.stack([self.by_pert_.loc[p].values if p in self.by_pert_.index else self.ctx_mean_.get(c, self.global_mean_)
                            for p, c in zip(pk, meta["context"].astype(str))])
        else:
            out = self.reg_.predict(self.scaler_.transform(F))
        return (out.astype(np.float32) @ self.W_).astype(np.float32)


def latent_pool(cells_path, scheme: str, cells_per_item: int = 30, embedders: list[Embedder] | None = None) -> list[Baseline]:
    """MeanShift is included so a scores table written on its own still carries the pass/fail reference."""
    from .baselines import MeanShift
    cache = LatentCellCache(cells_path, cells_per_item=cells_per_item)
    return [MeanShift()] + [LatentShift(e, cache, scheme) for e in (embedders or repr_default_pool())]

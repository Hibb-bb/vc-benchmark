"""The simple-model pool for component B.

Every respondent predicts the pseudobulk *delta* (perturbed mean minus matched control
mean, in log1p CP10k space) for held-out items from (a) features of the item and (b) the
training items' deltas. Interface: fit(F_train, D_train, meta_train) then predict(F_test,
meta_test) -> (n_test, n_genes).

Families, each with a capacity knob so abilities spread (plan, Phase 2):

  control_mean            delta = 0                                    floor
  random_shift            delta of a random training item              floor
  mean_shift              mean training delta (per context)            Systema baseline
  target_kd               mean_shift + on-target knockdown             cheap biology
  knn_k                   mean delta of k nearest items in feature space
  ridge_d_lam             ridge regression features -> PCA-d of deltas (Ahlmann-Eltze style)
  gp_ls                   GP regression (RBF) features -> PCA-d of deltas
  lowrank_r               soft-impute of the (perturbation x context) delta tensor;
                          only meaningful for multi-context datasets
"""
from __future__ import annotations

import numpy as np
from sklearn.decomposition import PCA
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel
from sklearn.linear_model import Ridge
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


class Baseline:
    name = "base"
    stochastic = False

    def fit(self, F, D, meta):  # meta: DataFrame with context, targets, perturbation, ...
        return self

    def predict(self, F, meta):
        raise NotImplementedError


class ControlMean(Baseline):
    name = "control_mean"

    def fit(self, F, D, meta):
        self.n_genes = D.shape[1]
        return self

    def predict(self, F, meta):
        return np.zeros((len(meta), self.n_genes), dtype=np.float32)


class MeanShift(Baseline):
    name = "mean_shift"

    def fit(self, F, D, meta):
        self.global_ = D.mean(0)
        self.by_ctx_ = {c: D[(meta["context"] == c).values].mean(0) for c in meta["context"].unique()}
        return self

    def predict(self, F, meta):
        return np.stack([self.by_ctx_.get(c, self.global_) for c in meta["context"]]).astype(np.float32)


class RandomShift(Baseline):
    stochastic = True

    def __init__(self, seed=0):
        self.seed = seed
        self.name = f"random_shift_s{seed}"

    def fit(self, F, D, meta):
        self.D_ = D
        return self

    def predict(self, F, meta):
        rng = np.random.default_rng(self.seed)
        return self.D_[rng.integers(0, len(self.D_), len(meta))]


class TargetKnockdown(MeanShift):
    """Mean shift, then force each target gene to a fixed fractional change of its control level.
    CRISPRi/KO: -80 % of control log-expression. CRISPRa: +50 %. Others: identical to mean_shift."""
    name = "target_kd"

    def __init__(self, var_names, ctrl_mean_by_ctx, kd_frac=0.8, act_frac=0.5):
        self.gene_index = {g: i for i, g in enumerate(var_names)}
        self.ctrl = ctrl_mean_by_ctx
        self.kd_frac, self.act_frac = kd_frac, act_frac

    def predict(self, F, meta):
        P = super().predict(F, meta).copy()
        for r, (ctx, targets, pt) in enumerate(zip(meta["context"], meta["targets"].astype(str), meta["pert_type"])):
            mu = self.ctrl.get(ctx)
            if mu is None or not targets:
                continue
            frac = -self.kd_frac if pt in ("CRISPRi", "CRISPR_KO") else (self.act_frac if pt == "CRISPRa" else 0.0)
            for g in targets.split("|"):
                j = self.gene_index.get(g)
                if j is not None:
                    P[r, j] = frac * mu[j]
        return P


class KNNShift(Baseline):
    def __init__(self, k=5):
        self.k = k
        self.name = f"knn_k{k}"

    def fit(self, F, D, meta):
        self.scaler_ = StandardScaler().fit(F)
        self.nn_ = NearestNeighbors(n_neighbors=min(self.k, len(F)), metric="cosine").fit(self.scaler_.transform(F))
        self.D_ = D
        return self

    def predict(self, F, meta):
        _, idx = self.nn_.kneighbors(self.scaler_.transform(F))
        return self.D_[idx].mean(1).astype(np.float32)


class _PCAOutput(Baseline):
    """Shared machinery: regress features onto a PCA-d basis of training deltas."""

    def __init__(self, d=50):
        self.d = d

    def _fit_output(self, D):
        self.mu_ = D.mean(0)
        k = min(self.d, D.shape[0] - 1, D.shape[1])
        self.pca_ = PCA(n_components=k, random_state=0).fit(D - self.mu_)
        return self.pca_.transform(D - self.mu_)

    def _inverse(self, Z):
        return (self.pca_.inverse_transform(Z) + self.mu_).astype(np.float32)


class RidgePCA(_PCAOutput):
    def __init__(self, d=50, lam=10.0):
        super().__init__(d)
        self.lam = lam
        self.name = f"ridge_d{d}_lam{lam:g}"

    def fit(self, F, D, meta):
        self.scaler_ = StandardScaler().fit(F)
        Z = self._fit_output(D)
        self.reg_ = Ridge(alpha=self.lam).fit(self.scaler_.transform(F), Z)
        return self

    def predict(self, F, meta):
        return self._inverse(self.reg_.predict(self.scaler_.transform(F)))


class MLPPCA(_PCAOutput):
    """Two-layer MLP from item features to the top-d components of the responses: the same inputs and
    outputs as RidgePCA, with a nonlinear map. Early stopping on 10 % of the training items."""

    def __init__(self, d=50, hidden=256, seed=0):
        super().__init__(d)
        self.hidden, self.seed = hidden, seed
        self.name = f"mlp_h{hidden}_d{d}"

    def fit(self, F, D, meta):
        from sklearn.neural_network import MLPRegressor
        self.scaler_ = StandardScaler().fit(F)
        Z = self._fit_output(D)
        self.reg_ = MLPRegressor(hidden_layer_sizes=(self.hidden,), alpha=1e-3, early_stopping=True, validation_fraction=0.1, max_iter=300, random_state=self.seed).fit(self.scaler_.transform(F), Z)
        return self

    def predict(self, F, meta):
        return self._inverse(self.reg_.predict(self.scaler_.transform(F)))


class PCARegression(RidgePCA):
    """PCA-regression ladder: ridge from item features onto the top-k principal components
    of the training responses, decoded back to genes. Same model as RidgePCA with a fixed
    penalty; the knob is k, mirroring the PCA ladder of component A."""

    def __init__(self, k, lam=10.0):
        super().__init__(d=k, lam=lam)
        self.name = f"pcareg_k{k}"


class GPPCA(_PCAOutput):
    def __init__(self, d=50, ls_mult=1.0, max_train=3000, seed=0):
        super().__init__(d)
        self.ls_mult, self.max_train, self.seed = ls_mult, max_train, seed
        self.name = f"gp_d{d}_ls{ls_mult:g}"

    def fit(self, F, D, meta):
        rng = np.random.default_rng(self.seed)
        if len(F) > self.max_train:
            sel = np.sort(rng.choice(len(F), self.max_train, replace=False))
            F, D = F[sel], D[sel]
        self.scaler_ = StandardScaler().fit(F)
        Fs = self.scaler_.transform(F)
        Z = self._fit_output(D)
        # median heuristic lengthscale, scaled by the capacity knob; no hyperparameter search
        sub = Fs[rng.choice(len(Fs), min(500, len(Fs)), replace=False)]
        d2 = ((sub[:, None, :] - sub[None, :, :]) ** 2).sum(-1)
        ls = np.sqrt(np.median(d2[d2 > 0])) * self.ls_mult
        kernel = ConstantKernel(1.0, "fixed") * RBF(length_scale=ls, length_scale_bounds="fixed") + WhiteKernel(0.1, (1e-3, 10))
        self.gp_ = GaussianProcessRegressor(kernel=kernel, normalize_y=True, random_state=self.seed).fit(Fs, Z)
        return self

    def predict(self, F, meta):
        return self._inverse(self.gp_.predict(self.scaler_.transform(F)))


class LowRank(Baseline):
    """Soft-impute the (perturbation x context) matrix of PCA-d delta coordinates.
    Falls back to mean_shift for perturbations never seen in any context."""

    def __init__(self, rank=5, d=50, n_iter=100):
        self.rank, self.d, self.n_iter = rank, d, n_iter
        self.name = f"lowrank_r{rank}"

    def fit(self, F, D, meta):
        self.mu_ = D.mean(0)
        k = min(self.d, D.shape[0] - 1, D.shape[1])
        self.pca_ = PCA(n_components=k, random_state=0).fit(D - self.mu_)
        Z = self.pca_.transform(D - self.mu_)
        pk = meta["pert_key"] if "pert_key" in meta else meta["perturbation"]
        self.perts_ = {p: i for i, p in enumerate(sorted(pk.unique()))}
        self.ctxs_ = {c: j for j, c in enumerate(sorted(meta["context"].unique()))}
        T = np.full((len(self.perts_), len(self.ctxs_), k), np.nan, dtype=np.float32)
        for z, p, c in zip(Z, pk, meta["context"]):
            T[self.perts_[p], self.ctxs_[c]] = z
        M = T.reshape(len(self.perts_), -1)
        mask = ~np.isnan(M)
        X = np.where(mask, M, 0.0)
        for _ in range(self.n_iter):
            U, s, Vt = np.linalg.svd(X, full_matrices=False)
            L = (U[:, : self.rank] * s[: self.rank]) @ Vt[: self.rank]
            X = np.where(mask, M, L)
        self.T_hat_ = X.reshape(T.shape)
        self.ctx_mean_ = {c: Z[(meta["context"] == c).values].mean(0) for c in self.ctxs_}
        return self

    def predict(self, F, meta):
        out = []
        pk = meta["pert_key"] if "pert_key" in meta else meta["perturbation"]
        for p, c in zip(pk, meta["context"]):
            if p in self.perts_ and c in self.ctxs_:
                out.append(self.T_hat_[self.perts_[p], self.ctxs_[c]])
            else:
                out.append(self.ctx_mean_.get(c, np.zeros(self.pca_.n_components_)))
        Z = np.stack(out)
        return (self.pca_.inverse_transform(Z) + self.mu_).astype(np.float32)


class SubsampledTrain(Baseline):
    """Training-fraction ladder: fit `base` on a random fraction of the training items.
    A monotone ability axis that mimics 'fewer perturbations seen'."""

    def __init__(self, base: Baseline, frac: float, seed: int = 0):
        self.base, self.frac, self.seed = base, frac, seed
        self.name = f"{base.name}_tf{frac:g}"

    def fit(self, F, D, meta):
        rng = np.random.default_rng(self.seed)
        n = max(5, int(round(self.frac * len(F))))
        sel = np.sort(rng.choice(len(F), min(n, len(F)), replace=False))
        self.base.fit(F[sel], D[sel], meta.iloc[sel])
        return self

    def predict(self, F, meta):
        return self.base.predict(F, meta)


def mlp_pool() -> list[Baseline]:
    return [MLPPCA(50, 256), MLPPCA(50, 1024)]


def pca_ladder(ks=(2, 5, 10, 20, 50, 100, 200)) -> list[Baseline]:
    return [PCARegression(k) for k in ks]


def featured_pool() -> list[Baseline]:
    """Respondents that need item features (gene embedding, fingerprint, or one-hot perturbation/context)."""
    pool: list[Baseline] = [KNNShift(k) for k in (1, 5, 20)]
    pool += [RidgePCA(d, lam) for d in (10, 50) for lam in (1.0, 100.0)]
    pool += [GPPCA(50, m) for m in (0.5, 2.0)]
    pool += [SubsampledTrain(RidgePCA(50, 100.0), f) for f in (0.3, 0.1)]
    pool += [SubsampledTrain(KNNShift(20), f) for f in (0.3, 0.1)]
    return pool


def default_pool(var_names, ctrl_mean_by_ctx, genetic: bool, multi_context: bool, seeds=(0, 1), featured: bool | None = None) -> list[Baseline]:
    """featured: items carry informative features (gene embedding or fingerprint); defaults to `genetic`."""
    featured = genetic if featured is None else featured
    pool: list[Baseline] = [ControlMean(), MeanShift(), TargetKnockdown(var_names, ctrl_mean_by_ctx)]
    pool += [RandomShift(seed=s) for s in seeds]
    if featured:
        pool += featured_pool()
    if multi_context:
        pool += [LowRank(r) for r in (2, 5, 10)]
    return pool

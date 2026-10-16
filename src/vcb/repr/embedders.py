"""The simple-model pool for component A: unsupervised embeddings with a capacity knob.

All embedders see the same preprocessed matrix: log1p(CP10k) on `n_hvg` highly variable
genes selected on the *train* panel, then z-scored per gene (train statistics), clipped at
10. fit() uses train cells only; transform() maps any cells (so test cells never influence
the embedding, which is why UMAP/t-SNE are excluded).

  pca_k        truncated PCA, k components                       the baseline ladder
  rproj_k      Gaussian random projection, k dims                same geometry, no variance ordering
  nystroem_k   RBF Nystroem features (k landmarks) on PCA-50     nonlinear, unsupervised
  nmf_k        NMF on the non-negative log matrix                different basis, same rank
  ica_k        FastICA on PCA-k                                  rotation of PCA; tests basis invariance
  gmm_k        GMM responsibilities (k components) on PCA-50     cluster-level respondent
  depth2       [log total counts, log n_genes]                   technical floor
  random_k     i.i.d. Gaussian features                          absolute floor
"""
from __future__ import annotations

import numpy as np
import scanpy as sc
import scipy.sparse as sp
from sklearn.decomposition import PCA, NMF, FastICA
from sklearn.kernel_approximation import Nystroem
from sklearn.mixture import GaussianMixture
from sklearn.random_projection import GaussianRandomProjection


class Preprocessor:
    def __init__(self, n_hvg=2000, clip=10.0, seed=0):
        self.n_hvg, self.clip, self.seed = n_hvg, clip, seed

    def fit(self, X_train_counts: sp.csr_matrix, var_names):
        a = sc.AnnData(X=sp.csr_matrix(X_train_counts, dtype=np.float32))
        a.var_names = var_names
        sc.pp.normalize_total(a, target_sum=1e4)
        sc.pp.log1p(a)
        sc.pp.highly_variable_genes(a, n_top_genes=self.n_hvg, flavor="seurat")
        self.hvg_ = np.where(a.var["highly_variable"].values)[0]
        Xh = a.X[:, self.hvg_].toarray()
        self.mu_ = Xh.mean(0)
        self.sd_ = Xh.std(0) + 1e-6
        return self

    def transform(self, X_counts: sp.csr_matrix, scaled=True):
        a = sc.AnnData(X=sp.csr_matrix(X_counts, dtype=np.float32))
        sc.pp.normalize_total(a, target_sum=1e4)
        sc.pp.log1p(a)
        Xh = a.X[:, self.hvg_].toarray()
        if not scaled:
            return Xh
        return np.clip((Xh - self.mu_) / self.sd_, -self.clip, self.clip).astype(np.float32)

    @staticmethod
    def depth_features(X_counts):
        tot = np.asarray(X_counts.sum(1)).ravel()
        ng = np.asarray((X_counts > 0).sum(1)).ravel()
        return np.stack([np.log1p(tot), np.log1p(ng)], 1).astype(np.float32)


class Embedder:
    name = "base"
    needs = "scaled"  # "scaled" | "log" | "counts"

    def fit(self, X):
        return self

    def transform(self, X):
        raise NotImplementedError


class PCAEmb(Embedder):
    def __init__(self, k, seed=0):
        self.k, self.seed, self.name = k, seed, f"pca_k{k}"

    def fit(self, X):
        self.m_ = PCA(n_components=self.k, svd_solver="randomized", random_state=self.seed).fit(X)
        return self

    def transform(self, X):
        return self.m_.transform(X)


class RandProjEmb(Embedder):
    def __init__(self, k, seed=0):
        self.k, self.seed, self.name = k, seed, f"rproj_k{k}_s{seed}"

    def fit(self, X):
        self.m_ = GaussianRandomProjection(n_components=self.k, random_state=self.seed).fit(X)
        return self

    def transform(self, X):
        return self.m_.transform(X)


class NystroemEmb(Embedder):
    def __init__(self, k, gamma_mult=1.0, seed=0, pca=50):
        self.k, self.gamma_mult, self.seed, self.pca = k, gamma_mult, seed, pca
        self.name = f"nystroem_k{k}_g{gamma_mult:g}"

    def fit(self, X):
        self.pca_ = PCA(n_components=self.pca, random_state=self.seed).fit(X)
        Z = self.pca_.transform(X)
        gamma = self.gamma_mult / (Z.shape[1] * Z.var())
        self.m_ = Nystroem(kernel="rbf", gamma=gamma, n_components=self.k, random_state=self.seed).fit(Z)
        return self

    def transform(self, X):
        return self.m_.transform(self.pca_.transform(X))


class NMFEmb(Embedder):
    needs = "log"

    def __init__(self, k, seed=0, max_fit=30000):
        self.k, self.seed, self.max_fit, self.name = k, seed, max_fit, f"nmf_k{k}"

    def fit(self, X):
        rng = np.random.default_rng(self.seed)
        if X.shape[0] > self.max_fit:
            X = X[rng.choice(X.shape[0], self.max_fit, replace=False)]
        self.m_ = NMF(n_components=self.k, init="nndsvda", max_iter=300, random_state=self.seed).fit(X)
        return self

    def transform(self, X):
        return self.m_.transform(X)


class ICAEmb(Embedder):
    def __init__(self, k, seed=0):
        self.k, self.seed, self.name = k, seed, f"ica_k{k}"

    def fit(self, X):
        self.pca_ = PCA(n_components=self.k, random_state=self.seed).fit(X)
        self.m_ = FastICA(n_components=self.k, random_state=self.seed, max_iter=500, whiten="unit-variance").fit(self.pca_.transform(X))
        return self

    def transform(self, X):
        return self.m_.transform(self.pca_.transform(X))


class GMMEmb(Embedder):
    def __init__(self, k, seed=0, pca=50, max_fit=30000):
        self.k, self.seed, self.pca, self.max_fit, self.name = k, seed, pca, max_fit, f"gmm_k{k}"

    def fit(self, X):
        rng = np.random.default_rng(self.seed)
        self.pca_ = PCA(n_components=self.pca, random_state=self.seed).fit(X)
        Z = self.pca_.transform(X)
        if Z.shape[0] > self.max_fit:
            Z = Z[rng.choice(Z.shape[0], self.max_fit, replace=False)]
        try:
            self.m_ = GaussianMixture(n_components=self.k, covariance_type="diag", random_state=self.seed, max_iter=200).fit(Z)
        except ValueError as e:  # collapsed component on a panel with many near-duplicate cells: regularise and retry
            print(f"  {self.name}: {str(e)[:60]}...; refitting with reg_covar=1e-3", flush=True)
            self.m_ = GaussianMixture(n_components=self.k, covariance_type="diag", random_state=self.seed, max_iter=200, reg_covar=1e-3).fit(Z)
        return self

    def transform(self, X):
        return self.m_.predict_proba(self.pca_.transform(X))


class DepthEmb(Embedder):
    needs = "depth"
    name = "depth2"

    def transform(self, X):
        return X


class RandomEmb(Embedder):
    def __init__(self, k=32, seed=0):
        self.k, self.seed, self.name = k, seed, f"random_k{k}_s{seed}"

    def transform(self, X):
        rng = np.random.default_rng(self.seed + X.shape[0])
        return rng.standard_normal((X.shape[0], self.k)).astype(np.float32)


def default_pool(seeds=(0, 1)) -> list[Embedder]:
    pool: list[Embedder] = [PCAEmb(k) for k in (4, 8, 16, 32, 64, 128, 256)]
    pool += [RandProjEmb(k, s) for k in (8, 32, 128) for s in seeds]
    pool += [NystroemEmb(k, g) for k in (64, 256) for g in (0.5, 2.0)]
    pool += [NMFEmb(k) for k in (16, 64)]
    pool += [ICAEmb(k) for k in (16, 64)]
    pool += [GMMEmb(k) for k in (10, 30, 100)]
    pool += [DepthEmb()] + [RandomEmb(32, s) for s in seeds]
    return pool

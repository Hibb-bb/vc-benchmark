"""Text-enhanced respondents for the unseen-combination split (a perturbation seen in other contexts).

With one-hot perturbation and context features, the additive part of a response (the perturbation's average effect
plus the context's average effect) is already learnable, and a text card adds nothing to it: the card is a fixed
function of the perturbation's identity. What one-hot features cannot carry is the interaction, how this
perturbation acts in this context beyond the two averages. These models use the text card for exactly that part,
by borrowing the interaction of perturbations with similar cards measured in the same context. Each has a no-text
twin that borrows from neighbours chosen another way, so any gain can be credited to the text.

  additive                 per gene: perturbation mean + context mean - grand mean (the two-way additive model)
  nbr_{src}_k{k}           additive + similarity-weighted mean interaction residual of the k nearest
                           perturbations measured in the same context; src = txt (text-card cosine),
                           resp (cosine of the perturbations' mean responses over training contexts, no text),
                           mix (average of the two similarities)
  ridge_x{src}_d{d}_lam    ridge on [one-hot perturbation, one-hot context, z_p (x) one-hot cell type] onto a
                           PCA-d response basis, z_p = text PCA (src = txt) or response PCA (src = resp)

meta must carry perturbation and context; the cell type is the last '|' field of the context.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge

from .baselines import Baseline, _PCAOutput


def _unit(X):
    return X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)


class _TwoWay(Baseline):
    """Per-gene additive fit: grand mean + perturbation effect + context effect (two passes of backfitting)."""

    def _fit_additive(self, D, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        self.mu_ = D.mean(0)
        R = D - self.mu_
        self.a_, self.b_ = {}, {}
        for _ in range(3):
            pa = pd.DataFrame(R - np.stack([self.b_.get(x, 0 * self.mu_) for x in c])).groupby(p).mean()
            self.a_ = {k: v.values for k, v in pa.iterrows()}
            cb = pd.DataFrame(R - np.stack([self.a_[x] for x in p])).groupby(c).mean()
            self.b_ = {k: v.values for k, v in cb.iterrows()}
        return p, c

    def _additive(self, p, c):
        z = 0 * self.mu_
        return np.stack([self.mu_ + self.a_.get(x, z) + self.b_.get(y, z) for x, y in zip(p, c)])


class Additive(_TwoWay):
    name = "additive"

    def fit(self, F, D, meta):
        self._fit_additive(D, meta)
        return self

    def predict(self, F, meta):
        return self._additive(meta["perturbation"].astype(str).values, meta["context"].astype(str).values).astype(np.float32)


class NeighbourInteraction(_TwoWay):
    def __init__(self, text: dict, src="txt", k=5, temp=0.05):
        self.text, self.src, self.k, self.temp = text, src, k, temp
        self.name = f"nbr_{src}_k{k}"

    def fit(self, F, D, meta):
        p, c = self._fit_additive(D, meta)
        R = D - self._additive(p, c)                                    # interaction residuals of training items
        self.res_ = {(x, y): r for x, y, r in zip(p, c, R)}
        self.in_ctx_ = pd.Series(p).groupby(c).apply(lambda s: sorted(set(s))).to_dict()
        perts = sorted(set(p) | set(self.text))
        self.pidx_ = {x: i for i, x in enumerate(perts)}
        T = _unit(np.stack([self.text.get(x, np.zeros(len(next(iter(self.text.values()))))) for x in perts]))
        A = _unit(np.stack([self.a_.get(x, 0 * self.mu_) for x in perts]))  # mean response of each perturbation
        St, Sr = T @ T.T, A @ A.T
        self.S_ = {"txt": St, "resp": Sr, "mix": (St + Sr) / 2}[self.src]
        return self

    def predict(self, F, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        out = self._additive(p, c)
        for i, (x, y) in enumerate(zip(p, c)):
            cand = [q for q in self.in_ctx_.get(y, []) if q != x]
            if not cand or x not in self.pidx_:
                continue
            s = np.array([self.S_[self.pidx_[x], self.pidx_[q]] for q in cand])
            top = np.argsort(-s)[: self.k]
            w = np.exp((s[top] - s[top].max()) / self.temp)
            w /= w.sum()
            out[i] += np.tensordot(w, np.stack([self.res_[(cand[j], y)] for j in top]), axes=1)
        return out.astype(np.float32)


class RidgeInteraction(_PCAOutput):
    def __init__(self, text: dict, src="txt", d=50, lam=10.0, zdim=16):
        super().__init__(d)
        self.text, self.src, self.lam, self.zdim = text, src, lam, zdim
        self.name = f"ridge_x{src}_d{d}_lam{lam:g}"

    def _design(self, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        ct = np.array([x.split("|")[-1] for x in c])
        Pp = sp.csr_matrix((np.ones(len(p)), (np.arange(len(p)), [self.pi_.get(x, 0) for x in p])), shape=(len(p), len(self.pi_)))
        Pp = Pp.multiply(np.array([x in self.pi_ for x in p])[:, None]).tocsr()
        Cc = sp.csr_matrix((np.ones(len(c)), (np.arange(len(c)), [self.ci_.get(x, 0) for x in c])), shape=(len(c), len(self.ci_)))
        Cc = Cc.multiply(np.array([x in self.ci_ for x in c])[:, None]).tocsr()
        Z = np.stack([self.z_.get(x, np.zeros(self.zdim)) for x in p])
        cols = [self.ti_.get(x, -1) for x in ct]
        X = np.zeros((len(p), len(self.ti_) * self.zdim), dtype=np.float32)
        for i, j in enumerate(cols):
            if j >= 0:
                X[i, j * self.zdim:(j + 1) * self.zdim] = Z[i]
        return sp.hstack([Pp, Cc, sp.csr_matrix(X)]).tocsr()

    def fit(self, F, D, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        self.pi_ = {x: i for i, x in enumerate(sorted(set(p)))}
        self.ci_ = {x: i for i, x in enumerate(sorted(set(c)))}
        self.ti_ = {x: i for i, x in enumerate(sorted({y.split("|")[-1] for y in c}))}
        if self.src == "txt":
            perts = sorted(set(self.text))
            Zt = PCA(n_components=min(self.zdim, len(perts) - 1), random_state=0).fit_transform(_unit(np.stack([self.text[x] for x in perts])))
        else:                                                           # no-text twin: PCA of mean training responses
            perts = sorted(set(p))
            M = np.stack([D[p == x].mean(0) for x in perts])
            Zt = PCA(n_components=min(self.zdim, len(perts) - 1), random_state=0).fit_transform(M - M.mean(0))
        Zt = Zt / (Zt.std(0, keepdims=True) + 1e-9)
        self.zdim = Zt.shape[1]
        self.z_ = dict(zip(perts, Zt))
        Zy = self._fit_output(D)
        self.reg_ = Ridge(alpha=self.lam).fit(self._design(meta), Zy)
        return self

    def predict(self, F, meta):
        return self._inverse(self.reg_.predict(self._design(meta)))


class RidgeNeighbourCorrection(Baseline):
    """The published ridge (one-hot perturbation + context -> PCA-d responses) plus a borrowed interaction:
    alpha x the similarity-weighted mean residual of the k nearest perturbations measured in the same context.
    Training residuals are out-of-fold (5-fold over training items), so they are not shrunk by in-sample fitting.
    src: txt (text cards), resp (mean training responses, no text), mix (average of both similarities).
    Name: rnbr_{src}_k{k}_a{alpha}."""

    def __init__(self, text: dict, src="mix", k=10, alpha=1.0, temp=0.05, d=50, lam=100.0):
        self.text, self.src, self.k, self.alpha, self.temp, self.d, self.lam = text, src, k, alpha, temp, d, lam
        self.name = f"rnbr_{src}_k{k}_a{alpha:g}"

    def _base(self):
        from .baselines import RidgePCA
        return RidgePCA(self.d, self.lam)

    def fit(self, F, D, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        self.base_ = self._base().fit(F, D, meta)
        oof = np.zeros_like(D)
        fold = np.random.default_rng(0).integers(0, 5, len(D))
        for f in range(5):
            tr, te = fold != f, fold == f
            oof[te] = self._base().fit(F[tr], D[tr], meta.iloc[np.where(tr)[0]]).predict(F[te], meta.iloc[np.where(te)[0]])
        R = D - oof
        self.res_ = {(x, y): r for x, y, r in zip(p, c, R)}
        self.in_ctx_ = pd.Series(p).groupby(c).apply(lambda s: sorted(set(s))).to_dict()
        perts = sorted(set(p) | set(self.text))
        self.pidx_ = {x: i for i, x in enumerate(perts)}
        dim = len(next(iter(self.text.values())))
        T = _unit(np.stack([self.text.get(x, np.zeros(dim)) for x in perts]))
        mu = D.mean(0)
        A = _unit(np.stack([D[p == x].mean(0) - mu if (p == x).any() else np.zeros(D.shape[1]) for x in perts]))
        St, Sr = T @ T.T, A @ A.T
        # put both similarities on a common scale (z-scored off-diagonal) before mixing
        z = lambda S: (S - S[~np.eye(len(S), dtype=bool)].mean()) / (S[~np.eye(len(S), dtype=bool)].std() + 1e-9)
        self.S_ = {"txt": z(St), "resp": z(Sr), "mix": (z(St) + z(Sr)) / 2}[self.src]
        return self

    def predict(self, F, meta):
        p, c = meta["perturbation"].astype(str).values, meta["context"].astype(str).values
        out = self.base_.predict(F, meta).copy()
        for i, (x, y) in enumerate(zip(p, c)):
            cand = [q for q in self.in_ctx_.get(y, []) if q != x]
            if not cand or x not in self.pidx_:
                continue
            s = np.array([self.S_[self.pidx_[x], self.pidx_[q]] for q in cand])
            top = np.argsort(-s)[: self.k]
            w = np.exp(s[top] - s[top].max())
            w /= w.sum()
            out[i] += self.alpha * np.tensordot(w, np.stack([self.res_[(cand[j], y)] for j in top]), axes=1)
        return out.astype(np.float32)


class RidgeScaledInteraction(Baseline):
    """The published ridge with an extra block z_p (x) one-hot cell type, scaled by s before the ridge so that the
    interaction is penalised more (effective penalty lam / s^2) than the additive one-hot part.
    z_p: text PCA (src=txt) or PCA of mean training responses (src=resp). Name: ridge_s{src}_s{s}."""

    def __init__(self, text: dict, src="txt", s=0.3, zdim=16, d=50, lam=100.0):
        self.text, self.src, self.s, self.zdim, self.d, self.lam = text, src, s, zdim, d, lam
        self.name = f"ridge_s{src}_s{s:g}"

    def _block(self, meta):
        p = meta["perturbation"].astype(str).values
        ct = np.array([x.split("|")[-1] for x in meta["context"].astype(str).values])
        Z = np.stack([self.z_.get(x, np.zeros(self.zk_)) for x in p])
        X = np.zeros((len(p), len(self.ti_) * self.zk_), dtype=np.float32)
        for i, t in enumerate(ct):
            j = self.ti_.get(t)
            if j is not None:
                X[i, j * self.zk_:(j + 1) * self.zk_] = Z[i]
        return X * self.s

    def fit(self, F, D, meta):
        from .baselines import RidgePCA
        p = meta["perturbation"].astype(str).values
        self.ti_ = {x: i for i, x in enumerate(sorted({y.split("|")[-1] for y in meta["context"].astype(str)}))}
        def zmap(kind):
            if kind == "txt":
                perts = sorted(self.text)
                M = _unit(np.stack([self.text[x] for x in perts]))
            else:
                perts = sorted(set(p))
                M = np.stack([D[p == x].mean(0) for x in perts])
            Z = PCA(n_components=min(self.zdim, len(perts) - 1), random_state=0).fit_transform(M - M.mean(0))
            return dict(zip(perts, Z / (Z.std(0, keepdims=True) + 1e-9)))
        if self.src == "both":                                         # response and text PCA side by side
            zr, zt = zmap("resp"), zmap("txt")
            kr, kt = len(next(iter(zr.values()))), len(next(iter(zt.values())))
            self.z_ = {x: np.concatenate([zr.get(x, np.zeros(kr)), zt.get(x, np.zeros(kt))]) for x in set(zr) | set(zt)}
        else:
            self.z_ = zmap(self.src)
        self.zk_ = len(next(iter(self.z_.values())))
        self.base_ = RidgePCA(self.d, self.lam)
        self.base_.scaler_ = __import__("sklearn.preprocessing", fromlist=["StandardScaler"]).StandardScaler().fit(F)
        Fs = np.hstack([self.base_.scaler_.transform(F), self._block(meta)])
        Zy = self.base_._fit_output(D)
        self.base_.reg_ = Ridge(alpha=self.lam).fit(Fs, Zy)
        return self

    def predict(self, F, meta):
        Fs = np.hstack([self.base_.scaler_.transform(F), self._block(meta)])
        return self.base_._inverse(self.base_.reg_.predict(Fs))

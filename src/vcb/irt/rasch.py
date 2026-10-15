"""Rasch (1PL) fits, dichotomous and binomial, by alternating Newton steps.

    P(correct) = sigmoid(theta_j - b_i)

Inputs are two (n_respondents x n_items) arrays: successes K and trials N (N=1 for
dichotomous items; N=0 marks a missing pair). Abilities carry a N(0, tau^2) ridge so a
respondent with all-correct or all-wrong answers stays finite (the paper's Fit operator);
difficulties are free with a sum-to-zero constraint that fixes the scale. Standard errors
come from the observed Fisher information. This is joint maximum likelihood, which is
adequate when each item has many respondents (our pool regime); it is what Phase 2 needs.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def fit_rasch(K: np.ndarray, N: np.ndarray, tau: float = 3.0, tau_b: float = 4.0, n_iter: int = 500, tol: float = 1e-6, anchors: dict[int, float] | None = None):
    """Returns (theta, theta_se, b, b_se, info_dict). anchors: {item_index: fixed_difficulty}.

    tau_b is a weak N(0, tau_b^2) ridge on free difficulties: it keeps items that every
    respondent passes (or fails) finite instead of diverging. Such items are also flagged in
    info['degenerate_item'] because they carry no information about this pool."""
    K = np.asarray(K, dtype=np.float64)
    N = np.asarray(N, dtype=np.float64)
    P, I = K.shape
    obs = N > 0
    # initial values from logits of marginal rates
    pj = (K.sum(1) + 0.5) / (N.sum(1) + 1.0)
    pi = (K.sum(0) + 0.5) / (N.sum(0) + 1.0)
    theta = np.log(pj / (1 - pj))
    b = -np.log(pi / (1 - pi))
    b -= b.mean()
    anchor_idx = np.array(sorted(anchors), dtype=int) if anchors else np.array([], dtype=int)
    if anchors:
        b[anchor_idx] = [anchors[i] for i in anchor_idx]
    free = np.ones(I, dtype=bool)
    free[anchor_idx] = False

    for it in range(n_iter):
        Z = theta[:, None] - b[None, :]
        Pm = _sigmoid(Z)
        W = N * Pm * (1 - Pm)
        # theta step (ridge)
        g_t = (K - N * Pm).sum(1) - theta / tau**2
        h_t = W.sum(1) + 1.0 / tau**2
        d_t = g_t / h_t
        theta = theta + d_t
        Z = theta[:, None] - b[None, :]
        Pm = _sigmoid(Z)
        W = N * Pm * (1 - Pm)
        # b step
        g_b = -(K - N * Pm).sum(0) - b / tau_b**2
        h_b = W.sum(0) + 1.0 / tau_b**2
        d_b = np.where(free, g_b / h_b, 0.0)
        b = b + d_b
        if not anchors and not np.isfinite(tau_b):
            shift = b.mean()  # only needed when no item prior fixes the location
            b -= shift
            theta -= shift
        if max(np.abs(d_t).max(), np.abs(d_b).max()) < tol:
            break

    Z = theta[:, None] - b[None, :]
    Pm = _sigmoid(Z)
    W = N * Pm * (1 - Pm)
    theta_se = 1.0 / np.sqrt(W.sum(1) + 1.0 / tau**2)
    b_se = 1.0 / np.sqrt(W.sum(0) + 1.0 / tau_b**2)
    rate = K.sum(0) / np.maximum(N.sum(0), 1)
    degenerate_item = (rate == 0) | (rate == 1)
    # fit statistics: standardized residual outfit per item and per respondent
    R2 = (K - N * Pm) ** 2 / (W + 1e-12)
    outfit_item = np.where(obs.sum(0) > 0, (R2 * obs).sum(0) / np.maximum(obs.sum(0), 1), np.nan)
    outfit_resp = np.where(obs.sum(1) > 0, (R2 * obs).sum(1) / np.maximum(obs.sum(1), 1), np.nan)
    ll = (K * np.log(Pm + 1e-12) + (N - K) * np.log(1 - Pm + 1e-12))[obs].sum()
    info = {"n_iter": it + 1, "loglik": float(ll), "outfit_item": outfit_item, "outfit_resp": outfit_resp, "degenerate_item": degenerate_item, "converged": bool(it + 1 < n_iter)}
    return theta, theta_se, b, b_se, info


def fit_from_long(df: pd.DataFrame, item_col="item_id", resp_col="respondent_id", k_col="k", n_col="n", **kw):
    """df has one row per (item, respondent) with successes k and trials n."""
    items = pd.Index(sorted(df[item_col].unique()))
    resps = pd.Index(sorted(df[resp_col].unique()))
    K = np.zeros((len(resps), len(items)))
    N = np.zeros_like(K)
    ri = resps.get_indexer(df[resp_col])
    ii = items.get_indexer(df[item_col])
    np.add.at(K, (ri, ii), df[k_col].values)
    np.add.at(N, (ri, ii), df[n_col].values)
    theta, theta_se, b, b_se, info = fit_rasch(K, N, **kw)
    abil = pd.DataFrame({"respondent_id": resps, "ability": theta, "se": theta_se, "outfit": info["outfit_resp"], "n_items": (N > 0).sum(1), "p_correct": K.sum(1) / np.maximum(N.sum(1), 1)}).sort_values("ability", ascending=False)
    diff = pd.DataFrame({"item_id": items, "difficulty": b, "se": b_se, "outfit": info["outfit_item"], "n_resp": (N > 0).sum(0), "p_correct": K.sum(0) / np.maximum(N.sum(0), 1), "degenerate": info["degenerate_item"]})
    return abil, diff, info


def item_information(theta_grid: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Fisher information of each item (columns) at each ability (rows)."""
    p = _sigmoid(theta_grid[:, None] - b[None, :])
    return p * (1 - p)

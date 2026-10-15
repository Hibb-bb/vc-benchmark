"""Per-item scores for component B. All operate on pseudobulk deltas (pred vs true).

  pearson_delta      Pearson(pred_delta, true_delta) over the evaluation genes (VCC/State style)
  pearson_delta_sys  same after subtracting the training mean shift from both; this is the
                     Systema correction: credit only for the perturbation-specific part
  mse                mean squared error of the delta
  deg_overlap50      |top50(|true|) & top50(|pred|)| / 50
  l2_ratio           ||pred - true|| / ||true||  (1.0 = as bad as predicting no change)
"""
from __future__ import annotations

import numpy as np


def _pearson_rows(A, B):
    A = A - A.mean(1, keepdims=True)
    B = B - B.mean(1, keepdims=True)
    num = (A * B).sum(1)
    den = np.sqrt((A * A).sum(1) * (B * B).sum(1)) + 1e-12
    return num / den


def score_items(pred, true, mean_shift, genes_mask=None, k=50) -> dict[str, np.ndarray]:
    if genes_mask is not None:
        pred, true, mean_shift = pred[:, genes_mask], true[:, genes_mask], mean_shift[:, genes_mask]
    out = {}
    out["pearson_delta"] = _pearson_rows(pred, true)
    out["pearson_delta_sys"] = _pearson_rows(pred - mean_shift, true - mean_shift)
    out["mse"] = ((pred - true) ** 2).mean(1)
    out["l2_ratio"] = np.linalg.norm(pred - true, axis=1) / (np.linalg.norm(true, axis=1) + 1e-12)
    kk = min(k, true.shape[1])
    top_t = np.argpartition(-np.abs(true), kk - 1, axis=1)[:, :kk]
    top_p = np.argpartition(-np.abs(pred), kk - 1, axis=1)[:, :kk]
    ov = np.array([len(np.intersect1d(a, b)) for a, b in zip(top_t, top_p)]) / kk
    out["deg_overlap50"] = ov
    return out

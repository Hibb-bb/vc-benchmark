"""Turn continuous component-B scores into Rasch responses.

Binary rule (default): respondent passes item i if its metric beats the reference
respondent's metric on the same item by at least `margin`. Reference defaults to the
mean-shift baseline, so difficulty reads as "how far past the shared shift do you need to
be on this item". Higher-is-better metrics only (pearson_delta*, deg_overlap50);
lower-is-better metrics (mse, l2_ratio) are negated first.

Graded rule: ordinal bin from a baseline ladder [control_mean, mean_shift, ridge_d50_lam1]:
0 = below control_mean, 1 = between control_mean and mean_shift, 2 = between mean_shift and
the linear model, 3 = above the linear model. Kept for the graded-response fit later.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

LOWER_IS_BETTER = ("mse", "l2_ratio")


def _oriented(long: pd.DataFrame, metric: str) -> pd.DataFrame:
    d = long[long["metric"] == metric].copy()
    if metric.split("@")[0] in LOWER_IS_BETTER:
        d["value"] = -d["value"]
    return d


def binarize(long: pd.DataFrame, metric: str = "pearson_delta@hvg", reference: str = "mean_shift", margin: float = 0.0, exclude_reference: bool = True) -> pd.DataFrame:
    d = _oriented(long, metric)
    ref = d[d["respondent_id"] == reference].set_index("item_id")["value"]
    d["ref"] = d["item_id"].map(ref)
    d = d.dropna(subset=["ref"])
    d["k"] = (d["value"] > d["ref"] + margin).astype(int)
    d["n"] = 1
    if exclude_reference:
        d = d[d["respondent_id"] != reference]
    return d[["dataset_id", "item_id", "respondent_id", "k", "n", "value", "ref"]]


def grade(long: pd.DataFrame, metric: str = "pearson_delta@hvg", ladder=("control_mean", "mean_shift", "ridge_d50_lam1")) -> pd.DataFrame:
    d = _oriented(long, metric)
    piv = d.pivot(index="item_id", columns="respondent_id", values="value")
    cuts = np.stack([piv[l].values for l in ladder if l in piv.columns], axis=1)
    cuts.sort(axis=1)
    out = []
    for r in piv.columns:
        g = (piv[r].values[:, None] > cuts).sum(1)
        out.append(pd.DataFrame({"item_id": piv.index, "respondent_id": r, "grade": g}))
    return pd.concat(out, ignore_index=True)

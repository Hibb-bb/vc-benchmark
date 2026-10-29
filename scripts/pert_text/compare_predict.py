#!/usr/bin/env python
"""Compare text-feature models with the published feature models on the unseen-perturbation split.

  .venv/bin/python scripts/pert_text/compare_predict.py      # writes runs/pert_text/predict/summary.md

For each screen with a runs/pert_text/predict/<dataset>.perturbation.scores.parquet: pass rate against the mean
shift (the benchmark's rule) and mean Pearson of the predicted shift on HVGs, for the text-feature models and
for the same model types in the published table (runs/pert_pool_v0), which use the screen's built-in features
(a control-cell gene embedding for genetic screens, one-hot labels otherwise, which carry no information about an
unseen perturbation).
"""
from pathlib import Path

import pandas as pd

from vcb.scoring import binarize

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "runs" / "pert_text" / "predict"
PUB = ROOT / "runs" / "pert_pool_v0"
BASE = ["ridge_d50_lam100", "knn_k20", "mlp_h256_d50"]


def summarise(sc, models):
    sc = sc[sc["respondent_id"].isin(models + ["mean_shift"])]
    b = binarize(sc)
    pr = b.groupby("respondent_id")["k"].mean()
    r = sc[sc["metric"] == "pearson_delta@hvg"].groupby("respondent_id")["value"].mean()
    return pd.DataFrame({"pass": pr, "pearson": r})


lines = ["# Text embeddings as features for unseen perturbations", "",
         "Pass = predicted shift correlates with the truth better than the mean shift does (the benchmark rule). "
         "Published = same model type with the screen's built-in features.", ""]
for f in sorted(P.glob("*.perturbation.scores.parquet")):
    ds = f.name.split(".perturbation")[0]
    txt = pd.read_parquet(f)
    tag = sorted({r.rsplit("_", 1)[1] for r in txt["respondent_id"].unique() if r != "mean_shift"})[0]
    t = summarise(txt, [f"{m}_{tag}" for m in BASE])
    pub = PUB / f"{ds}.perturbation.scores.parquet"
    p = summarise(pd.read_parquet(pub), BASE) if pub.exists() else pd.DataFrame()
    ms = t.loc["mean_shift", "pearson"] if "mean_shift" in t.index else float("nan")
    lines += [f"## {ds}", "", f"mean shift Pearson {ms:.3f}", "", "| model | text: pass | text: Pearson | published: pass | published: Pearson |", "|---|---|---|---|---|"]
    for m in BASE:
        tr = t.loc[f"{m}_{tag}"] if f"{m}_{tag}" in t.index else None
        pr = p.loc[m] if m in p.index else None
        fmt = lambda r, c, pc=False: "–" if r is None else (f"{r[c]:.0%}" if pc else f"{r[c]:.3f}")
        lines.append(f"| {m} | {fmt(tr, 'pass', True)} | {fmt(tr, 'pearson')} | {fmt(pr, 'pass', True)} | {fmt(pr, 'pearson')} |")
    lines.append("")
(P / "summary.md").write_text("\n".join(lines))
print("\n".join(lines))

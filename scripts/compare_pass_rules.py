#!/usr/bin/env python
"""Compare candidate pass rules on the Parse unseen-combination items.

  .venv/bin/python scripts/compare_pass_rules.py      # needs analysis_parse/split_half.parquet

Rules (r = Pearson of predicted vs measured shift on HVGs; r_res = the same after subtracting the average
response from both; rho = within-item split-half reliability):
  current       r > r of the average response
  raw>0.5       r > 0.5
  ratio>t       r / sqrt(rho) > t          (share of the achievable correlation)
  resratio>t    r_res / sqrt(rho) > t
Items with rho < 0.1 are unscorable under the ratio rules (nothing reliable to predict).
"""
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import RUNS

A = RUNS / "pert_pool_v0" / "analysis_parse"
sc = pd.read_parquet(RUNS / "pert_pool_v0" / "parse_pbmc_cytokines.context.scores.parquet")
r = sc[sc.metric == "pearson_delta@hvg"].pivot(index="item_id", columns="respondent_id", values="value")
rr = sc[sc.metric == "pearson_delta_sys@hvg"].pivot(index="item_id", columns="respondent_id", values="value")
rho = pd.read_parquet(A / "split_half.parquet")["reliability"].reindex(r.index)
ok = rho >= 0.1
ms = r["mean_shift"]
models = [c for c in r.columns if c != "mean_shift"]
den = np.sqrt(rho.clip(lower=0.1))
rules = {
    "current (beat average response)": r[models].gt(ms, axis=0),
    "raw r > 0.5": r[models] > 0.5,
    "r / sqrt(rho) > 0.5": r[models].div(den, axis=0).gt(0.5) & ok.values[:, None],
    "r / sqrt(rho) > 0.7": r[models].div(den, axis=0).gt(0.7) & ok.values[:, None],
    "r_res / sqrt(rho) > 0.2": rr[models].div(den, axis=0).gt(0.2) & ok.values[:, None],
    "r_res / sqrt(rho) > 0.3": rr[models].div(den, axis=0).gt(0.3) & ok.values[:, None],
}
ms_pass = {"current (beat average response)": np.nan, "raw r > 0.5": (ms > 0.5).mean(),
           "r / sqrt(rho) > 0.5": ((ms / den > 0.5) & ok).mean(), "r / sqrt(rho) > 0.7": ((ms / den > 0.7) & ok).mean(),
           "r_res / sqrt(rho) > 0.2": ((rr["mean_shift"] / den > 0.2) & ok).mean(), "r_res / sqrt(rho) > 0.3": ((rr["mean_shift"] / den > 0.3) & ok).mean()}
base = rules["current (beat average response)"].mean()
rows = []
for name, P in rules.items():
    pr = P.mean()
    rows.append({"rule": name, "best model (PCA reg 200D)": pr["pcareg_k200"], "MLP 256": pr["mlp_h256_d50"], "scGen": pr["scgen"],
                 "average response": ms_pass[name], "items nobody passes": (~P.any(axis=1)).mean(),
                 "unscorable (rho < 0.1)": 0.0 if name.startswith(("current", "raw")) else float((~ok).mean()),
                 "ranking vs current (Spearman)": spearmanr(pr, base)[0]})
out = pd.DataFrame(rows)
out.to_csv(A / "pass_rules.csv", index=False)
print(f"items {len(r)}; within-item reliability median {rho.median():.2f}; share below 0.1: {(~ok).mean():.0%}")
print(out.round(2).to_string(index=False))

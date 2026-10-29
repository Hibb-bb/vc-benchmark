#!/usr/bin/env python
"""Parse analysis scale with an absolute pass rule, and the error analysis redone on it.

  .venv/bin/python scripts/parse_error_rule.py [--k 1.5]

Pass rule: a model passes an item when its predicted shift lies within k times the item's measurement
noise of the measured shift, on the 2,000 HVGs:  ||pred - Δ|| <= k * noise, with
noise = sqrt( Σ_genes σ²_control (1/n_treated + 1/n_control) ), the same quantity as in signal-to-noise.
A model that knew the true response would land near 1.0 (the measurement itself is noisy), so k = 1.5
asks for a prediction about as close as a repeat measurement would be. Unlike the published rule (beat the
context's average response), it is fixed, does not depend on any other prediction, and lets weak and null
responses be passed by predicting a small change.

The scale is fitted on the same respondents that define the published Parse scale; respondents placed
there with difficulties held fixed are placed the same way here. Outputs go to
runs/pert_pool_v0/rasch_error/ (abilities, difficulties) and runs/pert_pool_v0/analysis_parse/error_rule/
(item table, summary.md, hardest items). The published scale is untouched.
"""
import argparse

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import RUNS
from vcb.irt.rasch import fit_from_long, fit_rasch

ap = argparse.ArgumentParser()
ap.add_argument("--k", type=float, default=1.5)
a = ap.parse_args()
G = 2000
R = RUNS / "pert_pool_v0"
OUTS = R / "rasch_error"; OUTS.mkdir(exist_ok=True)
OUTA = R / "analysis_parse" / "error_rule"; OUTA.mkdir(parents=True, exist_ok=True)
TAG = "parse_pbmc_cytokines.context"

sc = pd.read_parquet(R / f"{TAG}.scores.parquet")
f = pd.read_parquet(R / "analysis_parse" / "item_factors.parquet").join(pd.read_parquet(R / "analysis_parse" / "split_half.parquet")[["reliability"]])
mse = sc[sc.metric == "mse@hvg"].pivot(index="item_id", columns="respondent_id", values="value")
ratio = np.sqrt(mse * G).div(f["noise"].reindex(mse.index), axis=0)
ratio.to_parquet(OUTA / "error_ratio.parquet")

pub = pd.read_csv(R / "rasch" / f"{TAG}.abilities.csv")
pool = [r for r in pub.loc[pub["placement"].fillna("refit") != "anchored", "respondent_id"] if r in ratio.columns]
late = [r for r in ratio.columns if r not in pool and r != "mean_shift"]

def long_of(cols):
    P = (ratio[cols] <= a.k)
    d = P.stack().rename("k").reset_index()
    d["k"] = d["k"].astype(int); d["n"] = 1
    return d

abil, diff, info = fit_from_long(long_of(pool))
abil["placement"] = "refit"
# respondents added after the published scale was built: place with difficulties held fixed
if late:
    dd = diff.set_index("item_id"); dd = dd.loc[~dd["degenerate"], "difficulty"]
    L = long_of(late); L = L[L["item_id"].isin(dd.index)]
    items = pd.Index(sorted(L["item_id"].unique())); rs = pd.Index(sorted(L["respondent_id"].unique()))
    K = np.zeros((len(rs), len(items))); N = np.zeros_like(K)
    np.add.at(K, (rs.get_indexer(L["respondent_id"]), items.get_indexer(L["item_id"])), L["k"].values)
    np.add.at(N, (rs.get_indexer(L["respondent_id"]), items.get_indexer(L["item_id"])), L["n"].values)
    th, se, _, _, inf = fit_rasch(K, N, anchors={i: float(dd[it]) for i, it in enumerate(items)}, n_iter=300)
    pc = (ratio[late] <= a.k).mean()
    abil = pd.concat([abil, pd.DataFrame({"respondent_id": rs, "ability": th, "se": se, "outfit": inf["outfit_resp"], "n_items": len(ratio),
                                          "p_correct": pc.reindex(rs).values, "placement": "anchored"})], ignore_index=True)
abil = abil.sort_values("ability", ascending=False)
abil.to_csv(OUTS / f"{TAG}.abilities.csv", index=False)
diff.to_csv(OUTS / f"{TAG}.difficulties.csv", index=False)

d = diff.set_index("item_id")
f["difficulty_err"] = d["difficulty"].reindex(f.index)
f["p_correct_err"] = d["p_correct"].reindex(f.index)
f["nobody_err"] = f["p_correct_err"] == 0
f["everyone_err"] = f["p_correct_err"] == 1
f["ratio_best"] = ratio[pool].min(1).reindex(f.index)
f["ratio_nochange"] = ratio["control_mean"].reindex(f.index)
f.to_parquet(OUTA / "item_factors_err.parquet")

# ---- error analysis on the new scale ----
pc = f["p_correct_err"]
NUM = {"reliability": "within-item reliability", "snr": "signal-to-noise", "strength": "response size", "reproducibility": "donor agreement",
       "n_cells": "cells per item", "receptor_expr": "receptor expression", "ifn_share": "interferon-gene share", "ratio_nochange": "error of 'no change' (× noise)"}
lines = [f"# Parse error analysis under the absolute rule (pass if error <= {a.k} x noise)", "",
         f"Scale fitted on {len(pool)} respondents ({len(late)} more placed with difficulties held fixed). {len(f)} items; "
         f"passed by nobody {f['nobody_err'].mean():.0%}, by everyone {f['everyone_err'].mean():.0%}.", "",
         "## What predicts passing", "", "| descriptor | Spearman r with share of models passing | (published rule) |", "|---|---|---|"]
for c, n in NUM.items():
    ok = f[[c]].join(pc).dropna()
    old = f[[c, "p_correct_context"]].dropna()
    lines.append(f"| {n} | {spearmanr(ok[c], ok['p_correct_err'])[0]:+.2f} | {spearmanr(old[c], old['p_correct_context'])[0]:+.2f} |")
for grp in ("family", "lineage", "donor"):
    t = f.groupby(grp).agg(n=("p_correct_err", "size"), new=("p_correct_err", "mean"), old=("p_correct_context", "mean"), nobody=("nobody_err", "mean")).sort_values("new")
    lines += ["", f"## By {grp}", "", f"| {grp} | items | share passing (new) | (published) | passed by nobody |", "|---|---|---|---|---|"]
    lines += [f"| {k} | {int(r.n)} | {r.new:.0%} | {r.old:.0%} | {r.nobody:.0%} |" for k, r in t.iterrows()]
rb = pd.cut(f["reliability"], [-1, 0.1, 0.3, 0.5, 0.7, 1.01], labels=["below 0.1", "0.1-0.3", "0.3-0.5", "0.5-0.7", "0.7 and up"])
t = f.groupby(rb, observed=True).agg(n=("p_correct_err", "size"), new=("p_correct_err", "mean"), old=("p_correct_context", "mean"), nobody=("nobody_err", "mean"),
                                    nochange=("ratio_nochange", lambda x: (x <= a.k).mean()), cells=("n_cells", "median"))
lines += ["", "## By within-item reliability", "", "| reliability | items | share passing (new) | (published) | passed by nobody | 'no change' passes | median cells |", "|---|---|---|---|---|---|---|"]
lines += [f"| {k} | {int(r.n)} | {r.new:.0%} | {r.old:.0%} | {r.nobody:.0%} | {r.nochange:.0%} | {r.cells:.0f} |" for k, r in t.iterrows()]
abl = abil.merge(pub[["respondent_id", "ability"]].rename(columns={"ability": "published"}), on="respondent_id", how="left")
lines += ["", "## Model abilities", "", "| model | ability (new rule) | pass rate | ability (published rule) |", "|---|---|---|---|"]
lines += [f"| {r.respondent_id} | {r.ability:+.2f} | {r.p_correct:.0%} | {r.published:+.2f} |" for r in abl.itertuples()]
(OUTA / "summary.md").write_text("\n".join(lines) + "\n")
cols = ["cytokine", "family", "donor", "cell_type", "difficulty_err", "p_correct_err", "reliability", "snr", "strength", "n_cells", "reproducibility",
        "receptor_expr", "ifn_share", "ratio_best", "ratio_nochange", "difficulty_context"]
f.sort_values("p_correct_err").head(80)[cols].to_csv(OUTA / "hardest.csv")
print("\n".join(lines))

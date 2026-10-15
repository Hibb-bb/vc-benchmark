#!/usr/bin/env python
"""Fit Rasch models on pool outputs.

  # component B: binarize scores vs. mean_shift, fit per dataset and pooled
  python scripts/fit_rasch.py pert --run pert_pool_v0 [--metric pearson_delta@hvg --margin 0]
  # component A: cell-level dichotomous and stratum-level binomial fits
  python scripts/fit_rasch.py repr --run repr_pool_v0
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_from_long
from vcb.scoring import binarize

ap = argparse.ArgumentParser()
ap.add_argument("component", choices=["pert", "repr"])
ap.add_argument("--run", required=True)
ap.add_argument("--metric", default="pearson_delta@hvg")
ap.add_argument("--margin", type=float, default=0.0)
ap.add_argument("--reference", default="mean_shift")
ap.add_argument("--pool-runs", default=None, help="repr: comma-separated run names to pool on one scale (writes into --run)")
a = ap.parse_args()

run = RUNS / a.run
out = run / "rasch"
out.mkdir(parents=True, exist_ok=True)


def report(tag, abil, diff, info, extra=None):
    abil.to_csv(out / f"{tag}.abilities.csv", index=False)
    diff.to_csv(out / f"{tag}.difficulties.csv", index=False)
    lines = [f"# {tag}", "", f"- items: {len(diff)}, respondents: {len(abil)}, loglik: {info['loglik']:.1f}, iters: {info['n_iter']}, converged: {info['converged']}"]
    if extra:
        lines += extra
    q = np.percentile(diff.loc[~diff["degenerate"], "difficulty"], [5, 25, 50, 75, 95]) if (~diff["degenerate"]).any() else np.full(5, np.nan)
    lines += ["", f"- difficulty percentiles (5/25/50/75/95): {np.round(q, 2).tolist()}",
              f"- non-degenerate items: {(~diff['degenerate']).sum()}; nothing passes: {(diff['p_correct']==0).sum()}; everything passes: {(diff['p_correct']==1).sum()}",
              "", "| respondent | ability | se | p_correct | outfit |", "|---|---|---|---|---|"]
    lines += [f"| {r.respondent_id} | {r.ability:.2f} | {r.se:.2f} | {r.p_correct:.3f} | {r.outfit:.2f} |" for r in abil.itertuples()]
    (out / f"{tag}.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:6]), flush=True)
    print(abil[["respondent_id", "ability", "se", "p_correct"]].round(3).to_string(index=False), flush=True)


if a.component == "pert":
    files = sorted(run.glob("*.scores.parquet"))
    allb = []
    for f in files:
        long = pd.read_parquet(f)
        b = binarize(long, metric=a.metric, reference=a.reference, margin=a.margin)
        tag = f.name.replace(".scores.parquet", "")
        abil, diff, info = fit_from_long(b)
        report(tag, abil, diff, info, [f"- rule: pass if {a.metric} > {a.reference} + {a.margin}"])
        allb.append(b)
    # pooled scale: one response per item, so only the unseen-perturbation scheme enters
    allb = [b for b, f in zip(allb, files) if f.name.endswith(".perturbation.scores.parquet")]
    if len(allb) > 1:
        b = pd.concat(allb)
        abil, diff, info = fit_from_long(b)
        report("pooled", abil, diff, info, [f"- {b['dataset_id'].nunique()} datasets pooled on one scale (respondent names shared across datasets)"])
else:
    if a.pool_runs:
        runs = [RUNS / r for r in a.pool_runs.split(",")]
        # the same cell can be a test item in two panels built from one atlas (donor- vs context-held-out),
        # and strata share names across those panels: namespace both by run so they stay distinct items
        L, I = [], []
        for r in runs:
            lr = pd.read_parquet(r / "responses.parquet"); lr["item_id"] = r.name + "::" + lr["item_id"].astype(str); L.append(lr)
            ir = pd.read_parquet(r / "items.parquet"); ir.index = r.name + "::" + ir.index.astype(str); ir.index.name = "item_id"
            ir["stratum"] = r.name + "::" + ir["stratum"].astype(str); ir["source_run"] = r.name; I.append(ir)
        long = pd.concat(L, ignore_index=True)
        items = pd.concat(I)
        run.mkdir(parents=True, exist_ok=True); out.mkdir(exist_ok=True)
        long.to_parquet(run / "responses.parquet", index=False); items.to_parquet(run / "items.parquet")
        print(f"pooled {len(runs)} runs: {long.respondent_id.nunique()} respondents, {long.item_id.nunique()} items", flush=True)
    else:
        long = pd.read_parquet(run / "responses.parquet")
        items = pd.read_parquet(run / "items.parquet")
    abil, diff, info = fit_from_long(long)
    report("cell_level", abil, diff, info)
    # binomial Rasch at stratum level: k correct out of n cells per (stratum, respondent)
    s = long.merge(items[["stratum"]].astype(str), left_on="item_id", right_index=True)
    s["respondent_id"] = s["respondent_id"].astype(str)
    agg = s.groupby(["stratum", "respondent_id"])[["k", "n"]].sum().reset_index()
    agg = agg.rename(columns={"stratum": "item_id"})
    abil2, diff2, info2 = fit_from_long(agg, n_iter=3000)
    report("stratum_binomial", abil2, diff2, info2)

#!/usr/bin/env python
"""Place new perturbation respondents on the existing per-screen scales without refitting them.

  python scripts/place_anchored_pert.py --dataset parse_pbmc_cytokines --respondents a,b [--schemes context,perturbation] [--dry-run]

The pert counterpart of place_anchored.py. For each scheme, the respondents' scores in
runs/pert_pool_v0/<dataset>.<scheme>.scores.parquet are turned into pass/fail with the benchmark rule
(pearson_delta@hvg above the mean shift), and only their abilities are estimated, every item's
difficulty held at runs/pert_pool_v0/rasch/<dataset>.<scheme>.difficulties.csv. Rows are added to (or
replaced in) <dataset>.<scheme>.abilities.csv with placement = anchored; existing rows are marked refit.
The pooled scales are left alone: a respondent run on one screen has no answers on the other fourteen.
"""
import argparse

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_rasch
from vcb.scoring import binarize

ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--respondents", required=True)
ap.add_argument("--schemes", default="context,perturbation")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
run = RUNS / "pert_pool_v0"
resps = a.respondents.split(",")

for scheme in a.schemes.split(","):
    tag = f"{a.dataset}.{scheme}"
    sc = pd.read_parquet(run / f"{tag}.scores.parquet")
    have = sorted(set(resps) & set(sc["respondent_id"]))
    if not have:
        print(f"[place-pert] {tag}: none of the respondents scored; skipped")
        continue
    b = binarize(sc[sc["respondent_id"].isin(have + ["mean_shift"])])
    diff = pd.read_csv(run / "rasch" / f"{tag}.difficulties.csv").set_index("item_id")
    tot = b.groupby("respondent_id")["k"].agg(["sum", "size"])
    d = diff.loc[~diff["degenerate"], "difficulty"]
    b = b[b["item_id"].isin(d.index)]
    items = pd.Index(sorted(b["item_id"].unique()))
    rs = pd.Index(sorted(b["respondent_id"].unique()))
    K = np.zeros((len(rs), len(items))); N = np.zeros_like(K)
    np.add.at(K, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["k"].values)
    np.add.at(N, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["n"].values)
    theta, se, _, _, info = fit_rasch(K, N, anchors={i: float(d[it]) for i, it in enumerate(items)}, n_iter=300)
    new = pd.DataFrame({"respondent_id": rs, "ability": theta, "se": se, "outfit": info["outfit_resp"],
                        "n_items": tot["size"].reindex(rs).values, "p_correct": (tot["sum"] / tot["size"]).reindex(rs).values,
                        "placement": "anchored"})
    old = pd.read_csv(run / "rasch" / f"{tag}.abilities.csv")
    if "placement" not in old.columns:
        old["placement"] = "refit"
    for r in new.itertuples():
        print(f"[place-pert] {tag:40s} {r.respondent_id:28s} ability {r.ability:+.3f} ± {r.se:.3f}  pass {r.p_correct:.3f}  outfit {r.outfit:.2f}")
    merged = pd.concat([old[~old["respondent_id"].isin(new["respondent_id"])], new], ignore_index=True).sort_values("ability", ascending=False)
    if not a.dry_run:
        merged.to_csv(run / "rasch" / f"{tag}.abilities.csv", index=False)
print("[place-pert] dry run, nothing written" if a.dry_run else "[place-pert] abilities updated; difficulties unchanged")

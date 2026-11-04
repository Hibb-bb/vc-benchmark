#!/usr/bin/env python
"""Rank text-feature models with the published models on each screen's IRT scale.

  .venv/bin/python scripts/pert_text/rank.py      # writes runs/pert_text/rank/{<dataset>.<scheme>.abilities.csv, summary.md}

For every runs/pert_text/predict/<dataset>.<scheme>.scores.parquet, the text-feature respondents (suffix _txt*)
are turned into pass/fail with the benchmark rule and placed on the published scale with every item difficulty
held at runs/pert_pool_v0/rasch/<dataset>.<scheme>.difficulties.csv (the same anchored placement as
place_anchored_pert.py), so their abilities are directly comparable with the published respondents'. Nothing in
runs/pert_pool_v0 is written. As a check that anchoring does not decide the order, the scale is also refitted
with the text respondents included and the two rankings are compared.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import RUNS
from vcb.irt.rasch import fit_rasch
from vcb.names import plain_name
from vcb.scoring import binarize

ROOT = Path(__file__).resolve().parents[2]
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--pred", default=str(ROOT / "runs" / "pert_text" / "predict"))
ap.add_argument("--pub-run", default="pert_pool_v0")
ap.add_argument("--out", default=str(ROOT / "runs" / "pert_text" / "rank"))
args = ap.parse_args()
P = Path(args.pred)
OUT = Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)
PUB = RUNS / args.pub_run


def matrix(b, items):
    rs = pd.Index(sorted(b["respondent_id"].unique()))
    K = np.zeros((len(rs), len(items))); N = np.zeros_like(K)
    ri, ii = rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])
    np.add.at(K, (ri, ii), b["k"].values); np.add.at(N, (ri, ii), b["n"].values)
    return rs, K, N


NO_FEATURES = ("control_mean", "mean_shift", "random_shift", "target_kd", "lowrank_")
GENERATIVE = ("scgen", "scvi_cf", "cpa", "statetx")


def features_of(r):
    if r.startswith(NO_FEATURES):
        return "none"
    if r.startswith(GENERATIVE):
        return "own cell model"
    if "_txt" in r:
        return "text card + one-hot" if r.endswith("oh") else "text card"
    if "_g" in r and r.rsplit("_g", 1)[1] in ("scgpt", "geneformer", "scfoundation", "esm2", "ctrlpca"):
        return "cytokine genes: " + r.rsplit("_g", 1)[1]
    return "built-in"


def base_of(r):
    if "_txt" in r:
        return r.rsplit("_txt", 1)[0]
    if features_of(r).startswith("cytokine genes"):
        return r.rsplit("_g", 1)[0]
    return r


lines = ["# Text-feature models ranked with the published models", "",
         "Abilities on each screen's published Rasch scale (item difficulties fixed; text models placed by anchoring). "
         "'built-in' = the screen's own features: a gene embedding from control cells (genetic screens), Morgan "
         "fingerprint + dose (Tahoe), one-hot perturbation + context (sciPlex3, Parse). 'none' = reference "
         "respondents without item features; 'own cell model' = deep generative models with their own perturbation encoding.", ""]
for f in sorted(P.glob("*.scores.parquet")):
    tag = f.name.replace(".scores.parquet", "")
    ds, scheme = tag.rsplit(".", 1)
    txt = pd.read_parquet(f)
    txt_ids = sorted(r for r in txt["respondent_id"].unique() if "_txt" in r)
    pub_sc = pd.read_parquet(PUB / f"{tag}.scores.parquet")
    diff = pd.read_csv(PUB / "rasch" / f"{tag}.difficulties.csv").set_index("item_id")
    old = pd.read_csv(PUB / "rasch" / f"{tag}.abilities.csv")
    if "placement" not in old.columns:
        old["placement"] = "refit"
    d = diff.loc[~diff["degenerate"], "difficulty"]
    items = pd.Index(sorted(d.index))

    bt = binarize(txt[txt["respondent_id"].isin(txt_ids + ["mean_shift"])])
    bt = bt[bt["respondent_id"].isin(txt_ids)]
    tot = bt.groupby("respondent_id")["k"].agg(["sum", "size"])
    bt = bt[bt["item_id"].isin(items)]
    rs, K, N = matrix(bt, items)
    theta, se, _, _, info = fit_rasch(K, N, anchors={i: float(d[it]) for i, it in enumerate(items)}, n_iter=300)
    new = pd.DataFrame({"respondent_id": rs, "ability": theta, "se": se, "outfit": info["outfit_resp"],
                        "n_items": tot["size"].reindex(rs).values, "p_correct": (tot["sum"] / tot["size"]).reindex(rs).values,
                        "placement": "anchored (text)"})
    tab = pd.concat([old, new], ignore_index=True).sort_values("ability", ascending=False).reset_index(drop=True)
    tab["features"] = tab["respondent_id"].map(features_of)
    tab["model"] = tab["respondent_id"].map(base_of)
    tab["display"] = tab["model"].map(plain_name)
    tab["rank"] = np.arange(1, len(tab) + 1)
    tab.to_csv(OUT / f"{tag}.abilities.csv", index=False)

    # check: refit the published respondents of the original fit plus the text ones, nothing anchored
    refit_ids = list(old.loc[old["placement"] == "refit", "respondent_id"])
    ball = binarize(pd.concat([pub_sc[pub_sc["respondent_id"].isin(refit_ids + ["mean_shift"])], txt[txt["respondent_id"].isin(txt_ids)]]))
    ball = ball[ball["item_id"].isin(items) & ball["respondent_id"].isin(refit_ids + txt_ids)]
    rs2, K2, N2 = matrix(ball, items)
    th2 = fit_rasch(K2, N2, n_iter=300)[0]
    joint = pd.Series(th2, index=rs2)
    anch = tab.set_index("respondent_id")["ability"].reindex(rs2)
    rho = spearmanr(anch.values, joint.values).statistic

    pairs = tab[tab["features"].isin(["built-in", "text card"])].pivot_table(index="model", columns="features", values="ability")
    pairs = pairs.dropna(subset=["text card"])
    lines += [f"## {ds} ({scheme} split)", "",
              f"{len(items)} scored items; ranking with text models anchored vs refitted jointly: Spearman {rho:.3f}.", "",
              "| rank | model | features | ability ± se | pass |", "|---|---|---|---|---|"]
    for r in tab.itertuples():
        lines.append(f"| {r.rank} | {r.display} | {r.features} | {r.ability:+.2f} ± {r.se:.2f} | {r.p_correct:.0%} |")
    lines += ["", "Same model, two feature sets:", "", "| model | built-in | text | text − built-in |", "|---|---|---|---|"]
    for m, r in pairs.iterrows():
        b = r.get("built-in", np.nan)
        lines.append(f"| {plain_name(m)} | {b:+.2f} | {r['text card']:+.2f} | {r['text card'] - b:+.2f} |" if np.isfinite(b)
                     else f"| {plain_name(m)} | – | {r['text card']:+.2f} | – |")
    lines.append("")
    print(f"[rank] {tag}: {len(new)} text models placed; anchored vs joint Spearman {rho:.3f}")
(OUT / "summary.md").write_text("\n".join(lines))
print(f"[rank] wrote {OUT / 'summary.md'}")

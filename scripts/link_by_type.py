#!/usr/bin/env python
"""Does being good at annotating cell type X make an encoder good at predicting perturbations in X?

On Parse PBMC both components share the cell types and the 27 classical encoders (component A: the
embedding + frozen probe; component B: the same embedding as the basis of the latent-shift perturbation
model, `latent_<encoder>`). For every type X we estimate each encoder's A ability on the cells of X and
its B ability on the conditions whose context is X, with item difficulties anchored to the panel-level
(A) and screen-level (B) fits so that abilities are comparable across types. Then:

  within type     Spearman across encoders between the A and the B ability           (one per type)
  within encoder  Spearman across types between the encoder's A and B profiles       (one per encoder)
  residual        the same after subtracting each encoder's overall ability on each side, i.e. does the
                  type-specific part of representation quality transfer, beyond overall capacity

  python scripts/link_by_type.py      # writes runs/link_parse_v0/by_type.{md,json,png}
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from vcb import RUNS
from vcb.irt.rasch import fit_rasch
from vcb.names import family, plain_name
from vcb.scoring import binarize

OUT = RUNS / "link_parse_v0"
A_RUN, A_DIFF = RUNS / "repr_parse_pbmc_celltype", RUNS / "repr_parse_pbmc_celltype" / "rasch" / "cell_level.difficulties.csv"
B_SCORES, B_DIFF = RUNS / "pert_latent_v0" / "parse_pbmc_cytokines.context.scores.parquet", RUNS / "pert_joint_v0" / "rasch" / "parse_pbmc_cytokines.context.difficulties.csv"
MIN_ITEMS = 30


def anchored_abilities(long: pd.DataFrame, diff: pd.Series) -> pd.Series:
    """Respondent abilities with every item difficulty fixed (JML with all items anchored)."""
    long = long[long["item_id"].isin(diff.index)]
    items = pd.Index(sorted(long["item_id"].unique()))
    resps = pd.Index(sorted(long["respondent_id"].unique()))
    K = np.zeros((len(resps), len(items)))
    N = np.zeros_like(K)
    np.add.at(K, (resps.get_indexer(long["respondent_id"]), items.get_indexer(long["item_id"])), long["k"].values)
    np.add.at(N, (resps.get_indexer(long["respondent_id"]), items.get_indexer(long["item_id"])), long["n"].values)
    theta, _, _, _, _ = fit_rasch(K, N, anchors={i: float(diff[it]) for i, it in enumerate(items)}, n_iter=200)
    return pd.Series(theta, index=resps)


# ---------------- component A: cells of each type ----------------
ra = pd.read_parquet(A_RUN / "responses.parquet", columns=["item_id", "respondent_id", "k", "n"])
ia = pd.read_parquet(A_RUN / "items.parquet")
da = pd.read_csv(A_DIFF).set_index("item_id")
da = da.loc[~da["degenerate"], "difficulty"]
ra = ra[ra["respondent_id"].isin([r for r in ra["respondent_id"].unique() if not r.startswith("scvi")])]
ra["type_n"] = ra["item_id"].map(ia["cell_type"].astype(str).str.replace("/", "-", regex=False))

# ---------------- component B: conditions whose context is the type ----------------
sb = pd.read_parquet(B_SCORES)
bb = binarize(sb)
bb = bb[bb["respondent_id"].str.startswith("latent_")]
bb["encoder"] = bb["respondent_id"].str[len("latent_"):]
bb["type_n"] = bb["item_id"].str.split("ctx=").str[1].str.split("|").str[1]
db = pd.read_csv(B_DIFF).set_index("item_id")
db = db.loc[~db["degenerate"], "difficulty"]

encoders = sorted(set(ra["respondent_id"]) & set(bb["encoder"]))
types = sorted(set(ra["type_n"]) & set(bb["type_n"]))
print(f"{len(encoders)} shared encoders, {len(types)} shared types", flush=True)

A, B, nA, nB = {}, {}, {}, {}
for t in types:
    la = ra[ra["type_n"] == t]
    lb = bb[bb["type_n"] == t].drop(columns="respondent_id").rename(columns={"encoder": "respondent_id"})[["item_id", "respondent_id", "k", "n"]]
    nA[t], nB[t] = la["item_id"].nunique(), lb["item_id"].nunique()
    if nA[t] < MIN_ITEMS or nB[t] < MIN_ITEMS:
        continue
    A[t] = anchored_abilities(la, da).reindex(encoders)
    B[t] = anchored_abilities(lb, db).reindex(encoders)
    print(f"  {t:24s} A items {nA[t]:5d}  B items {nB[t]:5d}", flush=True)
A = pd.DataFrame(A)   # encoders x types
B = pd.DataFrame(B)
A_all = anchored_abilities(ra[["item_id", "respondent_id", "k", "n"]], da).reindex(encoders)
B_all = anchored_abilities(bb.drop(columns="respondent_id").rename(columns={"encoder": "respondent_id"})[["item_id", "respondent_id", "k", "n"]], db).reindex(encoders)
A_res, B_res = A.sub(A_all, axis=0), B.sub(B_all, axis=0)
null = [e for e in encoders if e.startswith(("rproj", "random", "depth"))]
real = [e for e in encoders if e not in null]


def sp(x, y):
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 5:
        return (np.nan, np.nan, int(m.sum()))
    r, p = stats.spearmanr(x[m], y[m])
    return (float(r), float(p), int(m.sum()))


res = {"encoders": encoders, "types": list(A.columns), "n_items": {t: {"A": int(nA[t]), "B": int(nB[t])} for t in A.columns},
       "overall": {"spearman_across_encoders": sp(A_all.values, B_all.values)}}
# 1. within type: ranking of encoders agrees across the two tasks?
wt = {t: {"raw": sp(A[t].values, B[t].values), "raw_no_null": sp(A.loc[real, t].values, B.loc[real, t].values), "residual": sp(A_res[t].values, B_res[t].values)} for t in A.columns}
res["within_type"] = wt
# 2. within encoder: is it strong on the same types in both tasks?
we = {e: {"raw": sp(A.loc[e].values, B.loc[e].values), "residual": sp(A_res.loc[e].values, B_res.loc[e].values)} for e in encoders}
res["within_encoder"] = we
# 3. pooled residual over every (encoder, type) cell
res["pooled_residual"] = sp(A_res.values.ravel(), B_res.values.ravel())
res["pooled_residual_no_null"] = sp(A_res.loc[real].values.ravel(), B_res.loc[real].values.ravel())
# how much of the per-type ability is the overall ability (variance explained)
res["share_overall"] = {"A": float(1 - A_res.values.var() / A.values.var()), "B": float(1 - B_res.values.var() / B.values.var())}
A.round(3).to_csv(OUT / "by_type_A.csv"); B.round(3).to_csv(OUT / "by_type_B.csv")
(OUT / "by_type.json").write_text(json.dumps(res, indent=1))

# ---------------- report ----------------
wt_raw = np.array([v["raw"][0] for v in wt.values()]); wt_res = np.array([v["residual"][0] for v in wt.values()])
we_raw = np.array([v["raw"][0] for v in we.values()]); we_res = np.array([v["residual"][0] for v in we.values()])
L = ["# Type-level link on Parse PBMC: does annotation quality for a type transfer to perturbation prediction in that type?", "",
     f"{len(encoders)} shared encoders x {len(A.columns)} cell types with >= {MIN_ITEMS} items on both sides. Abilities are anchored to the "
     "panel-level (A) and screen-level (B, unseen-combination scheme) item difficulties. `residual` subtracts each encoder's overall ability "
     "on each side, leaving the type-specific part.", "",
     f"- overall (one ability per encoder per side) Spearman across encoders: {res['overall']['spearman_across_encoders'][0]:+.2f}",
     f"- share of the per-type ability variance that is the encoder's overall ability: A {res['share_overall']['A']:.2f}, B {res['share_overall']['B']:.2f}",
     f"- within type, Spearman across encoders (raw): median {np.nanmedian(wt_raw):+.2f}, range {np.nanmin(wt_raw):+.2f} to {np.nanmax(wt_raw):+.2f}",
     f"- within type, residual (type-specific part): median {np.nanmedian(wt_res):+.2f}, range {np.nanmin(wt_res):+.2f} to {np.nanmax(wt_res):+.2f}, "
     f"{int((np.array([v['residual'][1] for v in wt.values()]) < 0.05).sum())} of {len(wt)} types with p < 0.05",
     f"- within encoder, Spearman across types (raw): median {np.nanmedian(we_raw):+.2f}; residual: median {np.nanmedian(we_res):+.2f}",
     f"- pooled residual over all (encoder, type) cells: {res['pooled_residual'][0]:+.2f} (p = {res['pooled_residual'][1]:.2g}, n = {res['pooled_residual'][2]}); "
     f"without the null encoders {res['pooled_residual_no_null'][0]:+.2f}", "",
     "| cell type | A items | B items | raw rho | raw rho (no null) | residual rho | p |", "|---|---|---|---|---|---|---|"]
for t, v in sorted(wt.items(), key=lambda kv: -kv[1]["residual"][0] if np.isfinite(kv[1]["residual"][0]) else 0):
    L.append(f"| {t} | {nA[t]} | {nB[t]} | {v['raw'][0]:+.2f} | {v['raw_no_null'][0]:+.2f} | {v['residual'][0]:+.2f} | {v['residual'][1]:.2g} |")
L += ["", "| encoder | family | A overall | B overall | raw rho across types | residual rho |", "|---|---|---|---|---|---|"]
for e in sorted(encoders, key=lambda e: -A_all[e]):
    L.append(f"| {plain_name(e)} | {family(e)} | {A_all[e]:+.2f} | {B_all[e]:+.2f} | {we[e]['raw'][0]:+.2f} | {we[e]['residual'][0]:+.2f} |")
(OUT / "by_type.md").write_text("\n".join(L) + "\n")
print("\n".join(L), flush=True)

# ---------------- figure ----------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 4.8))
ax = axes[0]
ax.scatter(A.values.ravel(), B.values.ravel(), s=10, alpha=0.6, color="#2f6fde")
ax.set_xlabel("A ability of encoder on cells of type X"); ax.set_ylabel("B ability of the same encoder on conditions in X")
ax.set_title(f"raw, all (encoder, type) cells: rho {sp(A.values.ravel(), B.values.ravel())[0]:+.2f}", fontsize=10); ax.grid(alpha=0.3)
ax = axes[1]
ax.scatter(A_res.values.ravel(), B_res.values.ravel(), s=10, alpha=0.6, color="#d9541e")
ax.axhline(0, color="#999", lw=0.6); ax.axvline(0, color="#999", lw=0.6)
ax.set_xlabel("A ability on type X minus overall A ability"); ax.set_ylabel("B ability on X minus overall B ability")
ax.set_title(f"type-specific part: rho {res['pooled_residual'][0]:+.2f}", fontsize=10); ax.grid(alpha=0.3)
ax = axes[2]
order = np.argsort(-wt_res)
tt = np.array(list(wt.keys()))[order]
ax.barh(range(len(tt)), wt_raw[order], color="#b8c4d6", label="raw")
ax.barh(range(len(tt)), wt_res[order], height=0.5, color="#d9541e", label="residual")
ax.set_yticks(range(len(tt))); ax.set_yticklabels(tt, fontsize=8); ax.invert_yaxis()
ax.set_xlabel("Spearman across encoders, within the type"); ax.legend(fontsize=8, frameon=False); ax.grid(alpha=0.3, axis="x")
fig.tight_layout(); fig.savefig(OUT / "by_type.png", dpi=150)

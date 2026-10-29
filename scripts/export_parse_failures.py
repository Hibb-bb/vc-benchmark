#!/usr/bin/env python
"""Data for the website page analysis/failures/ under the combined pass rule (Parse, unseen combinations).

  .venv/bin/python scripts/export_parse_failures.py        # writes site/data/parse_failures.json

Combined rule (scripts/parse_error_rule.py --rule combo): items whose response stands clearly above noise
(signal-to-noise >= 1.5) are passed when the prediction explains at least half of the R² a perfect model
would reach; weaker items are passed when the predicted change lies within 1.5 x the item's noise (a small
predicted change is a correct answer there). Reads the scores, the item descriptors and the combined-rule
scale in runs/pert_pool_v0/rasch_combo/.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.names import family, plain_name

ROOT = Path(__file__).resolve().parents[1]
R = RUNS / "pert_pool_v0"
TAG = "parse_pbmc_cytokines.context"
K, R2, SPLIT, G = 1.5, 0.5, 1.5, 2000
HIGH_ISG = {"Donor1", "Donor3", "Donor4", "Donor10"}

sc = pd.read_parquet(R / f"{TAG}.scores.parquet")
f = pd.read_parquet(R / "analysis_parse" / "item_factors.parquet")
mse = sc[sc.metric == "mse@hvg"].pivot(index="item_id", columns="respondent_id", values="value")
f = f.reindex(mse.index)
ratio = np.sqrt(mse * G).div(f["noise"], axis=0)
r2 = 1 - mse.div(f["strength"] ** 2 / G, axis=0)
ceil = (1 - (f["noise"] / f["strength"]) ** 2).clip(lower=0.05)
nr2 = r2.div(ceil, axis=0)
clear = f["snr"] >= SPLIT
P = pd.DataFrame(np.where(clear.values[:, None], nr2.values >= R2, ratio.values <= K), index=mse.index, columns=mse.columns)

ab = pd.read_csv(R / "rasch_combo" / f"{TAG}.abilities.csv")
pub = pd.read_csv(R / "rasch" / f"{TAG}.abilities.csv").set_index("respondent_id")["ability"]
dif = pd.read_csv(R / "rasch_combo" / f"{TAG}.difficulties.csv").set_index("item_id")
pool = [r for r in ab.loc[ab["placement"] == "refit", "respondent_id"] if r in P.columns]
pi = P[pool].mean(1)                                   # share of the scale-defining models passing each item
f["pass"] = pi
f["difficulty"] = dif["difficulty"].reindex(f.index)
f["nobody"] = pi == 0
f["achievable_r2"] = ceil
f["best_share"] = nr2[pool].max(1).clip(upper=1.5)

# ---- kinds of item ----
donor_specific = clear & (f["reproducibility"] < 0.3)
f["kind"] = np.select(
    [~clear & (pi >= 0.9), ~clear, donor_specific, clear & (pi >= 0.5), clear & (pi > 0)],
    ["nulleasy", "nullinvent", "donor", "captured", "partial"], default="missed")
KINDS = [
    ("captured", "Clear response, captured", "Most models explain at least half of what is achievable."),
    ("partial", "Clear response, partly captured", "Some models get there; most get the direction but not the size."),
    ("missed", "Clear response, missed by all", "A clear, reproducible response no model predicts well enough."),
    ("donor", "Clear but donor-specific", "Clear in this donor, different in the others: not inferable from the other donors."),
    ("nullinvent", "Weak or null, some models invent a response", "The right answer is a small change; some models predict a response that is not there."),
    ("nulleasy", "Weak or null, predicted correctly", "Almost every model predicts a small change, as it should."),
]
COLORS = {"captured": "var(--s3)", "partial": "var(--s4)", "missed": "var(--s8)", "donor": "var(--s7)", "nullinvent": "var(--s2)", "nulleasy": "var(--s0)"}
n_models = len(pool)


def example(sel, order, asc=False):
    g = f[sel].sort_values(order, ascending=asc)
    if g.empty:
        return None
    r = g.iloc[0]
    is_clear = r.snr >= SPLIT
    return {"cytokine": r.cytokine, "cell_type": r.cell_type, "donor": r.donor, "n_cells": int(r.n_cells), "snr": float(r.snr),
            "achievable_r2": float(r.achievable_r2) if is_clear else None, "best_share": float(r.best_share) if is_clear else None,
            "repro": None if pd.isna(r.reproducibility) else float(r.reproducibility), "receptor": None if pd.isna(r.receptor_expr) else float(r.receptor_expr),
            "passed": int(round(r["pass"] * n_models)), "of": n_models}


examples = {"captured": example(f.kind.eq("captured"), "snr"),
            "partial": example(f.kind.eq("partial") & f.family.str.contains("interferon"), "snr") or example(f.kind.eq("partial"), "snr"),
            "missed": example(f.kind.eq("missed"), "snr"), "donor": example(f.kind.eq("donor"), "snr"),
            "nullinvent": example(f.kind.eq("nullinvent"), "n_cells"),
            "nulleasy": example(f.kind.eq("nulleasy") & (f.receptor_expr < 0.01), "n_cells")}
kinds_out = [{"key": k, "name": n, "desc": d, "color": COLORS[k], "n": int((f.kind == k).sum()), "share": float((f.kind == k).mean()),
              "pass": float(pi[f.kind == k].mean()) if (f.kind == k).any() else None, "example": examples.get(k)} for k, n, d in KINDS]


# ---- what decides passing ----
def curve(x, nbins=10):
    q = pd.qcut(x, nbins, duplicates="drop")
    g = pd.DataFrame({"x": x, "p": pi}).groupby(q, observed=True)
    return [{"x": float(gg.x.median()), "y": float(gg.p.mean())} for _, gg in g]


curves = {"snr": curve(f.snr), "cells": curve(np.log10(f.n_cells)), "strength": curve(f.strength)}
snr_edges = [0, 1.2, 1.5, 2, 3, 1e9]
snr_lab = ["below 1.2", "1.2–1.5", "1.5–2", "2–3", "3 and up"]
lin_order = ["monocyte", "CD4 T", "CD8 T", "B", "dendritic", "NK", "innate-like T"]
sb = pd.cut(f.snr, snr_edges, labels=snr_lab, right=False)
heat = {"rows": snr_lab, "cols": lin_order, "p": [], "n": []}
for lab in snr_lab:
    row_p, row_n = [], []
    for ln in lin_order:
        m = (sb == lab) & (f.lineage == ln)
        row_p.append(float(pi[m].mean()) if m.sum() >= 20 else None); row_n.append(int(m.sum()))
    heat["p"].append(row_p); heat["n"].append(row_n)


# ---- biology ----
def by(col):
    g = f.groupby(col)
    out = pd.DataFrame({"n": g.size(), "pass": g["pass"].mean(), "nobody": g["nobody"].mean(), "snr": g["snr"].median(), "repro": g["reproducibility"].median()})
    return [{"name": str(k), **{c: (None if pd.isna(v) else float(v)) for c, v in r.items()}} for k, r in out.sort_values("pass", ascending=False).iterrows()]


lineage, donors, cyt = by("lineage"), by("donor"), by("cytokine")
for r in donors:
    r["high_isg"] = r["name"] in HIGH_ISG
for r in cyt:
    r["family"] = f.loc[f.cytokine == r["name"], "family"].iloc[0]
    r["is_cytokine"] = bool(f.loc[f.cytokine == r["name"], "is_cytokine"].iloc[0]) if "is_cytokine" in f else True
rb = pd.cut(f.receptor_expr, [-1, 0.01, 0.05, 0.2, 100], labels=["below 0.01", "0.01 to 0.05", "0.05 to 0.2", "above 0.2"])
receptor = [{"name": str(k), "n": int(len(g)), "pass": float(g["pass"].mean()), "snr": float(g.snr.median())} for k, g in f.groupby(rb, observed=True)]

# ---- weak and null items: who invents a response ----
weak = ~clear
nulls = [{"rid": m, "name": plain_name(m), "pass": float(P.loc[weak, m].mean()), "ratio": float(ratio.loc[weak, m].median())}
         for m in P.columns if m != "mean_shift"]
nulls.sort(key=lambda r: r["pass"])

# ---- noisy items still rank models ----
abil = ab.set_index("respondent_id")["ability"]
bands = [("signal-to-noise below 1.5", weak), ("signal-to-noise 1.5 to 3", clear & (f.snr < 3)), ("signal-to-noise 3 and above", f.snr >= 3)]
rank = []
for name, m in bands:
    pr = P.loc[m, pool].mean()
    pts = sorted([{"x": float(abil[r]), "y": float(v), "name": plain_name(r)} for r, v in pr.items()], key=lambda t: t["x"])
    rank.append({"band": name, "n_items": int(m.sum()), "rho": float(pd.Series([t["x"] for t in pts]).corr(pd.Series([t["y"] for t in pts]), method="spearman")), "pts": pts})

# ---- models ----
models = []
for row in ab.itertuples():
    rid = row.respondent_id
    models.append({"rid": rid, "name": plain_name(rid), "family": family(rid), "ability": float(row.ability),
                   "pass": float(P[rid].mean()) if rid in P else None, "pass_clear": float(P.loc[clear, rid].mean()) if rid in P else None,
                   "pass_weak": float(P.loc[weak, rid].mean()) if rid in P else None,
                   "published": None if rid not in pub.index else float(pub[rid]), "placement": row.placement})
models.sort(key=lambda m: -m["ability"])

hard = f["pass"] <= f["pass"].quantile(0.1)
sh = R / "analysis_parse" / "split_half.parquet"
out = {
    "meta": {"n_items": int(len(f)), "n_cytokines": int(f.cytokine.nunique()), "n_contexts": int(f.context.nunique()), "n_models": n_models,
             "k": K, "r2": R2, "split": SPLIT, "n_clear": int(clear.sum()), "n_weak": int(weak.sum()),
             "snr_vs_split_half": float(f.snr.corr(pd.read_parquet(sh)["reliability"].reindex(f.index), method="spearman")) if sh.exists() else None},
    "headline": {"nobody": float(f["nobody"].mean()), "clear_pass": float(pi[clear].mean()), "weak_pass": float(pi[weak].mean()),
                 "hard_clear_share": float(clear[hard].mean()), "rho_snr": float(f.snr.corr(pi, method="spearman")),
                 "best_model": models[0]["name"], "best_ability": models[0]["ability"]},
    "kinds": kinds_out, "curves": curves, "heat": heat, "lineage": lineage, "donors": donors, "cytokines": cyt, "receptor": receptor,
    "nulls": nulls, "rank": rank, "models": models,
}


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if not np.isfinite(o) else round(float(o), 4)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


path = ROOT / "site" / "data" / "parse_failures.json"
path.write_text(json.dumps(clean(out), separators=(",", ":"), allow_nan=False))
print(f"wrote {path} ({path.stat().st_size / 1e3:.0f} kB)")
print({k["key"]: (k["n"], round(k["share"], 3), None if k["pass"] is None else round(k["pass"], 2)) for k in kinds_out})
print(out["headline"])

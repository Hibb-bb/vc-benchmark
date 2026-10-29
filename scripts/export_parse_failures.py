#!/usr/bin/env python
"""Data for the website page analysis/failures/: why perturbation models fail on Parse cytokine items.

  .venv/bin/python scripts/export_parse_failures.py        # writes site/data/parse_failures.json

Unseen-combination split only. Reads the per-item descriptors (analyze_parse_hard_items.py), the
within-item split-half reliability (parse_split_half.py, optional), the scores table and the abilities.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.names import family, plain_name
from vcb.scoring import binarize

ROOT = Path(__file__).resolve().parents[1]
A = RUNS / "pert_pool_v0" / "analysis_parse"
DS, SCH = "parse_pbmc_cytokines", "context"
HIGH_ISG = {"Donor1", "Donor3", "Donor4", "Donor10"}   # high baseline ISG donors named by the source preprint

f = pd.read_parquet(A / "item_factors.parquet")
sh = A / "split_half.parquet"
has_rel = sh.exists()
if has_rel:
    f = f.join(pd.read_parquet(sh)[["reliability"]])
f["rel"] = f["snr"]            # one measure of measurement quality: signal-to-noise
rel_check = float(f["snr"].corr(f["reliability"], method="spearman")) if has_rel else None
d, p, nb, ref = f["difficulty_context"], f["p_correct_context"], f["nobody_context"], f["reference_r_context"]

# ---- classes ----
donor_specific = (f["rel"] >= 2) & (f["reproducibility"] < 0.3)
cls = np.select(
    [donor_specific, (f["rel"] >= 2) & (ref < 0.5), (f["rel"] >= 2) & (ref >= 0.5),
     (f["rel"] < 1.5) & (f["n_cells"] < 300), (f["rel"] < 1.5)],
    ["donor", "clear", "refright", "fewcells", "noresp"], default="between")
f["cls"] = cls
CLASSES = [
    ("clear", "Clear response", "Signal-to-noise 2 or more; the average response is not already right. A fair test of the model."),
    ("refright", "Reference already right", "Clear response, but the context's average response is nearly the answer, so it is hard to beat."),
    ("donor", "Donor-specific response", "Clear in this donor, different in the others. Seen only in other donors, it cannot be inferred."),
    ("between", "In between", "Signal-to-noise 1.5 to 2: a weak response. Mixed reasons."),
    ("noresp", "No detectable response", "Signal-to-noise below 1.5 despite enough cells: little or nothing to predict."),
    ("fewcells", "Too few cells", "Under 300 cells: the shift is mostly sampling noise."),
]
q90 = d[~nb].quantile(0.9)
hard = nb | (d >= q90)
n_models = int(round(1 / p[p > 0].min()))


def ex(sel, order, asc=False):
    g = f[sel].sort_values(order, ascending=asc)
    if g.empty:
        return None
    r = g.iloc[0]
    return {"cytokine": r.cytokine, "cell_type": r.cell_type, "donor": r.donor, "family": r.family, "n_cells": int(r.n_cells),
            "snr": round(float(r.snr), 2), "rel": None if pd.isna(r.rel) else round(float(r.rel), 2),
            "repro": None if pd.isna(r.reproducibility) else round(float(r.reproducibility), 2), "ref_r": round(float(r.reference_r_context), 2),
            "passed": int(round(r.p_correct_context * n_models)), "of": n_models, "difficulty": round(float(r.difficulty_context), 2),
            "receptor": None if pd.isna(r.receptor_expr) else round(float(r.receptor_expr), 3)}


f["_mid"] = -(f["difficulty_context"] - f.groupby("cls")["difficulty_context"].transform("median")).abs()
examples = {
    "clear": ex(f.cls.eq("clear"), "rel"),
    "refright": ex(f.cls.eq("refright"), "reference_r_context"),
    "donor": ex(f.cls.eq("donor") & f.family.str.contains("interferon"), "rel") or ex(f.cls.eq("donor"), "rel"),
    "between": ex(f.cls.eq("between"), "_mid"),
    "noresp": ex(f.cls.eq("noresp") & (f.receptor_expr < 0.01) & (f.reference_r_context < 0.5), "n_cells"),
    "fewcells": ex(f.cls.eq("fewcells") & (f.receptor_expr < 0.01), "difficulty_context"),
}
classes = []
for k, name, desc in CLASSES:
    m = f.cls.eq(k)
    classes.append({"key": k, "name": name, "desc": desc, "n": int(m.sum()), "share": float(m.mean()), "n_hard": int((m & hard).sum()),
                    "pass": float(p[m].mean()) if m.any() else None, "difficulty": float(d[m].mean()) if m.any() else None,
                    "cells": float(f.n_cells[m].median()) if m.any() else None, "rel": float(f.rel[m].median()) if m.any() else None,
                    "ref_r": float(ref[m].median()) if m.any() else None, "example": examples.get(k)})

# ---- two dials: pass rate by reliability x reference r ----
rel_edges = [0, 1.2, 1.5, 2, 3, 1000]
ref_edges = [-1, 0.2, 0.35, 0.5, 0.7, 1.01]
rb = pd.cut(f.rel, rel_edges, right=False, labels=False)
fb = pd.cut(ref, ref_edges, right=False, labels=False)
heat_p = [[None] * 5 for _ in range(5)]
heat_n = [[0] * 5 for _ in range(5)]
for (i, j), g in p.groupby([rb, fb]):
    heat_p[int(i)][int(j)] = float(g.mean()); heat_n[int(i)][int(j)] = int(len(g))

# ---- binned curves ----
def curve(x, nbins=10):
    q = pd.qcut(x, nbins, duplicates="drop")
    g = pd.DataFrame({"x": x, "p": p}).groupby(q, observed=True)
    return [{"x": float(gg.x.median()), "y": float(gg.p.mean()), "n": int(len(gg))} for _, gg in g]


curves = {"snr": curve(f.snr), "rel": curve(f.rel.dropna()), "cells": curve(np.log10(f.n_cells)), "strength": curve(f.strength)}

# ---- noisy items still rank models ----
sc = pd.read_parquet(RUNS / "pert_pool_v0" / f"{DS}.{SCH}.scores.parquet")
ab = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / f"{DS}.{SCH}.abilities.csv")
pool = ab[ab.get("placement", pd.Series("refit", index=ab.index)).fillna("refit") != "anchored"]
b = binarize(sc)
abil = pool.set_index("respondent_id")["ability"]
bands = [("signal-to-noise below 1.5", f.rel < 1.5), ("signal-to-noise 1.5 to 2", (f.rel >= 1.5) & (f.rel < 2)), ("signal-to-noise 2 and above", f.rel >= 2)]
rank = []
for name, m in bands:
    pr = b[b.item_id.isin(f.index[m]) & b.respondent_id.isin(abil.index)].groupby("respondent_id").k.mean()
    pts = sorted([{"x": float(abil[r]), "y": float(v), "name": plain_name(r)} for r, v in pr.items()], key=lambda t: t["x"])
    rho = float(pd.Series([t["x"] for t in pts]).corr(pd.Series([t["y"] for t in pts]), method="spearman"))
    rank.append({"band": name, "n_items": int(m.sum()), "rho": rho, "pts": pts})

# ---- biology ----
def by(col, extra=None):
    g = f.groupby(col)
    out = pd.DataFrame({"n": g.size(), "difficulty": g.difficulty_context.mean(), "pass": g.p_correct_context.mean(),
                        "nobody": g.nobody_context.mean(), "rel": g.rel.median(), "repro": g.reproducibility.median()})
    return [{"name": str(k), **{c: (None if pd.isna(v) else float(v)) for c, v in r.items()}} for k, r in out.sort_values("pass", ascending=False).iterrows()]


fam = by("family")
lineage = by("lineage")
donors = by("donor")
for r in donors:
    r["high_isg"] = r["name"] in HIGH_ISG
cyt = by("cytokine")
for r in cyt:
    r["family"] = f.loc[f.cytokine == r["name"], "family"].iloc[0]
    r["is_cytokine"] = bool(f.loc[f.cytokine == r["name"], "is_cytokine"].iloc[0]) if "is_cytokine" in f else True
rec_bins = pd.cut(f.receptor_expr, [-1, 0.01, 0.05, 0.2, 100], labels=["below 0.01", "0.01 to 0.05", "0.05 to 0.2", "above 0.2"])
receptor = [{"name": str(k), "n": int(len(g)), "pass": float(g.p_correct_context.mean()), "rel": float(g.rel.median())}
            for k, g in f.groupby(rec_bins, observed=True)]
receptor.append({"name": "no known receptor", "n": int(f.receptor_expr.isna().sum()), "pass": float(p[f.receptor_expr.isna()].mean()),
                 "rel": float(f.rel[f.receptor_expr.isna()].median())})

# ---- models: pass rate, ability and the two correlations ----
r_all = sc[sc.metric == "pearson_delta@hvg"].groupby("respondent_id").value.mean()
r_sys = sc[sc.metric == "pearson_delta_sys@hvg"].groupby("respondent_id").value.mean()
pr_all = b.groupby("respondent_id").k.mean()
models = []
for row in ab.itertuples():
    rid = row.respondent_id
    models.append({"rid": rid, "name": plain_name(rid), "family": family(rid), "ability": float(row.ability), "pass": float(pr_all.get(rid, np.nan)),
                   "r": float(r_all.get(rid, np.nan)), "r_sys": float(r_sys.get(rid, np.nan)), "placement": getattr(row, "placement", "refit") if isinstance(getattr(row, "placement", "refit"), str) else "refit"})
models.sort(key=lambda m: -m["ability"])
ms_r = float(r_all.get("mean_shift", np.nan))

out = {
    "meta": {"n_items": int(len(f)), "n_cytokines": int(f.cytokine.nunique()), "n_contexts": int(f.context.nunique()), "n_donors": int(f.donor.nunique()),
             "n_cell_types": int(f.cell_type.nunique()), "n_models": n_models, "has_reliability": bool(has_rel), "mean_shift_r": ms_r,
             "reliability_source": "signal-to-noise", "snr_vs_split_half": rel_check},
    "headline": {"share_clear": float((f.cls == "clear").mean()), "n_hard": int(hard.sum()), "n_nobody": int(nb.sum()),
                 "hard_unmeasurable": float((hard & f.cls.isin(["fewcells", "noresp"])).sum() / hard.sum()),
                 "hard_clear": int((hard & f.cls.eq("clear")).sum()),
                 "rho_rel": float(f.rel.corr(p, method="spearman")), "rho_snr": float(f.snr.corr(p, method="spearman")),
                 "rho_strength": float(f.strength.corr(p, method="spearman")), "rho_ref": float(ref.corr(p, method="spearman"))},
    "classes": classes, "heat": {"rel_edges": rel_edges, "ref_edges": ref_edges, "p": heat_p, "n": heat_n},
    "curves": curves, "rank": rank, "family": fam, "lineage": lineage, "donors": donors, "cytokines": cyt, "receptor": receptor, "models": models,
}
path = ROOT / "site" / "data" / "parse_failures.json"
def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if not np.isfinite(o) else round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


path.write_text(json.dumps(clean(out), separators=(",", ":"), allow_nan=False))
print(f"wrote {path} ({path.stat().st_size/1e3:.0f} kB); reliability from {out['meta']['reliability_source']}")
print({c["key"]: (c["n"], round(c["share"], 3), c["n_hard"]) for c in classes})
print(out["headline"])

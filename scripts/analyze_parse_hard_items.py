#!/usr/bin/env python
"""Error analysis of the Parse cytokine items: what makes an item hard?

  .venv/bin/python scripts/analyze_parse_hard_items.py            # writes runs/pert_pool_v0/analysis_parse/

Every item is one (cytokine, donor, cell type) pseudobulk shift. For each item this computes biological
and statistical descriptors, relates them to the item's Rasch difficulty in both splits (unseen
combination = "context", unseen cytokine = "perturbation"), and lists the hardest items with their
annotations. All expression quantities are on the benchmark's 2,000 HVGs in log1p CP10k space.

Descriptors
- strength: L2 norm of the shift; signal-to-noise = norm / expected sampling-noise norm, where the
  noise uses the context's control variance and the item's and controls' cell counts.
- reference score: Pearson r between the item's shift and the mean-shift prediction of its fold. The
  pass rule is "beat the mean shift", so an item whose response looks like the cell type's average
  response leaves little room to beat it.
- reproducibility: Pearson r between the item's shift and the mean shift of the same cytokine in the
  same cell type in the other donors (a ceiling set by biology and noise, not by any model).
- receptor expression: for each alternative receptor complex of the cytokine (receptor_complexes in
  src/vcb/data/parse_cytokines.tsv), the lowest control mean expression across its required subunits;
  the item takes the best complex (a cell needs only one working receptor).
- interferon share: share of the squared shift carried by a fixed set of interferon-stimulated genes.
- cytokine family, cell lineage, donor, cells per item.
"""
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import DATA, RUNS
from vcb.pert.baselines import MeanShift
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask

DS = "parse_pbmc_cytokines"
OUT = RUNS / "pert_pool_v0" / "analysis_parse"
OUT.mkdir(parents=True, exist_ok=True)
REF = Path(__file__).resolve().parents[1] / "src" / "vcb" / "data" / "parse_cytokines.tsv"
ISG = ["ISG15", "IFI6", "IFI44L", "IFI44", "IFIT1", "IFIT2", "IFIT3", "IFIT5", "MX1", "MX2", "OAS1", "OAS2", "OAS3",
       "OASL", "RSAD2", "IFI27", "IFITM1", "IFITM3", "STAT1", "IRF7", "XAF1", "HERC5", "EPSTI1", "CMPK2", "LY6E",
       "SAMD9L", "PLSCR1", "BST2", "EIF2AK2", "SP110", "GBP1", "IFI35", "USP18", "PARP9", "DDX58", "IFIH1"]
LINEAGE = {"CD4 Naive": "CD4 T", "CD4 Memory": "CD4 T", "Treg": "CD4 T", "CD8 Naive": "CD8 T", "CD8 Memory": "CD8 T",
           "MAIT": "innate-like T", "NKT": "innate-like T", "NK": "NK", "NK CD56bright": "NK", "B Naive": "B",
           "B Intermediate-Memory": "B", "CD14 Mono": "monocyte", "CD16 Mono": "monocyte", "cDC": "dendritic",
           "pDC": "dendritic", "HSPC": "progenitor"}

items = ad.read_h5ad(DATA / "items" / f"{DS}.items.h5ad")
meta, D, ctrl_rows = item_table(items)
hv = hvg_mask(items)
genes = np.asarray(items.var_names.astype(str))
gh = genes[hv]
Dh = D[:, hv]
stats = items.uns["control_stats"]
ref = pd.read_csv(REF, sep="\t", keep_default_na=False).set_index("cytokine")
gpos = {g: i for i, g in enumerate(genes)}

f = meta[["perturbation", "context", "n_cells"]].copy()
f["cytokine"] = f["perturbation"].astype(str)
f["donor"] = f["context"].astype(str).str.split("|").str[0]
f["cell_type"] = f["context"].astype(str).str.split("|").str[1]
f["lineage"] = f["cell_type"].map(LINEAGE).fillna("other")
f["family"] = f["cytokine"].map(ref["family"]).fillna("unknown")

# strength and signal-to-noise
f["strength"] = np.linalg.norm(Dh, axis=1)
noise = []
for i, c in enumerate(f["context"].astype(str)):
    s = stats[c]
    var = np.asarray(s["var"])[hv]
    n_ctrl = float(np.asarray(s["n"]).ravel()[0])
    noise.append(np.sqrt(var.sum() * (1.0 / max(f["n_cells"].iloc[i], 1) + 1.0 / max(n_ctrl, 1))))
f["noise"] = noise
f["snr"] = f["strength"] / f["noise"]

# interferon share of the response
isg = np.isin(gh, ISG)
f["ifn_share"] = (Dh[:, isg] ** 2).sum(1) / ((Dh ** 2).sum(1) + 1e-12)

# receptor expression in the responding cells' controls
def receptor_level(cyt, ctx):
    """Best receptor complex: max over alternative complexes of the min over its required subunits."""
    alts = [[g for g in c.split("+") if g] for c in str(ref["receptor_complexes"].get(cyt, "")).split("|")]
    alts = [c for c in alts if c and all(g in gpos for g in c)]
    if not alts:
        return np.nan
    m = np.asarray(stats[ctx]["mean"])
    return float(max(min(m[gpos[g]] for g in c) for c in alts))
f["receptor_expr"] = [receptor_level(c, x) for c, x in zip(f["cytokine"], f["context"].astype(str))]
f["receptor_known"] = f["receptor_expr"].notna()
f["is_cytokine"] = f["cytokine"].map(ref["is_cytokine"].astype(str).str.lower().eq("true")).fillna(True)

# reproducibility across donors (same cytokine, same cell type)
key = f["cytokine"] + "|" + f["cell_type"]
sums = pd.DataFrame(Dh).groupby(key.values).sum()
cnt = key.value_counts()
rep = np.full(len(f), np.nan)
for i, k in enumerate(key.values):
    n = cnt[k]
    if n < 2:
        continue
    other = (sums.loc[k].values - Dh[i]) / (n - 1)
    rep[i] = np.corrcoef(Dh[i], other)[0, 1]
f["reproducibility"] = rep

def zrow(x):
    x = x - x.mean(1, keepdims=True)
    return x / (np.linalg.norm(x, axis=1, keepdims=True) + 1e-12)

for scheme in ("context", "perturbation"):
    ms = np.zeros_like(Dh)
    for _, tr, te in fold_splits(meta, scheme, 5):
        ms[te] = MeanShift().fit(None, D[tr], meta.iloc[tr]).predict(None, meta.iloc[te])[:, hv]
    f[f"reference_r_{scheme}"] = (zrow(ms) * zrow(Dh)).sum(1)
    d = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / f"{DS}.{scheme}.difficulties.csv").set_index("item_id")
    f[f"difficulty_{scheme}"] = d["difficulty"].reindex(f.index)
    f[f"p_correct_{scheme}"] = d["p_correct"].reindex(f.index)
    f[f"nobody_{scheme}"] = d["p_correct"].reindex(f.index) == 0

f.to_parquet(OUT / "item_factors.parquet")

NUM = {"strength": "response strength (L2)", "snr": "signal-to-noise", "reproducibility": "agreement with other donors",
       "receptor_expr": "receptor expression", "ifn_share": "interferon-gene share", "n_cells": "cells per item"}
lines = ["# What makes a Parse cytokine item hard", "",
         f"{len(f)} items: {f['cytokine'].nunique()} cytokines x {f['context'].nunique()} donor-cell-type contexts. "
         "Difficulty from the per-screen Rasch fits. Spearman correlations over items that at least one model passed; "
         "items passed by nobody are summarised separately.", ""]
for scheme, label in (("context", "Unseen combination"), ("perturbation", "Unseen cytokine")):
    dcol, ncol = f"difficulty_{scheme}", f"nobody_{scheme}"
    inf = f[~f[ncol]]
    lines += [f"## {label}", "", f"- items passed by nobody: {int(f[ncol].sum())} of {len(f)}", "",
              "| descriptor | Spearman r with difficulty | median, hardest 10% | median, rest | median, passed by nobody |",
              "|---|---|---|---|---|"]
    q90 = inf[dcol].quantile(0.9)
    hard, rest = inf[inf[dcol] >= q90], inf[inf[dcol] < q90]
    for c, name in list(NUM.items()) + [(f"reference_r_{scheme}", "mean-shift reference r")]:
        ok = inf[[c, dcol]].dropna()
        r = spearmanr(ok[c], ok[dcol])[0] if len(ok) > 10 else np.nan
        lines.append(f"| {name if c in NUM else 'mean-shift reference r'} | {r:+.2f} | {hard[c].median():.3g} | {rest[c].median():.3g} | {f.loc[f[ncol], c].median():.3g} |")
    for grp in ("family", "lineage"):
        t = f.groupby(grp).agg(n_items=(dcol, "size"), mean_difficulty=(dcol, "mean"), nobody=(ncol, "mean")).sort_values("mean_difficulty", ascending=False)
        lines += ["", f"### By {grp}", "", f"| {grp} | items | mean difficulty | share passed by nobody |", "|---|---|---|---|"]
        lines += [f"| {k} | {int(r.n_items)} | {r.mean_difficulty:+.2f} | {r.nobody:.0%} |" for k, r in t.iterrows()]
    lines.append("")
    cols = ["cytokine", "family", "donor", "cell_type", dcol, f"p_correct_{scheme}", "strength", "snr", "reproducibility",
            "receptor_expr", "ifn_share", f"reference_r_{scheme}", "n_cells"]
    top = inf.sort_values(dcol, ascending=False).head(60)[cols]
    top.to_csv(OUT / f"hardest_{scheme}.csv")
    f.loc[f[ncol], cols].to_csv(OUT / f"nobody_{scheme}.csv")
    t = f.groupby("cytokine").agg(family=("family", "first"), mean_difficulty=(dcol, "mean"), nobody=(ncol, "mean"),
                                  snr=("snr", "median"), reproducibility=("reproducibility", "median")).sort_values("mean_difficulty", ascending=False)
    t.to_csv(OUT / f"by_cytokine_{scheme}.csv")
    ct = f.groupby("cell_type").agg(mean_difficulty=(dcol, "mean"), nobody=(ncol, "mean"), snr=("snr", "median")).sort_values("mean_difficulty", ascending=False)
    ct.to_csv(OUT / f"by_cell_type_{scheme}.csv")

(OUT / "summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print("wrote", OUT)

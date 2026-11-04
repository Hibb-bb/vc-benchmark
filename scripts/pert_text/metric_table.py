#!/usr/bin/env python
"""Raw metrics for each feature-driven model with built-in features and with the text card (unseen-perturbation split).

  .venv/bin/python scripts/pert_text/metric_table.py      # under Slurm: Tahoe's score tables are large

For every model fitted both ways, averages each metric over the items both versions scored, then reports per screen the
number of pairs where the text card is better and the median of (text - built-in). Metrics, all over the 2,000 HVGs:
  pearson_delta      Pearson r between predicted and measured expression change
  pearson_delta_sys  the same after subtracting the mean shift from both (signal beyond the average response)
  mse                mean squared error of the change (lower is better)
  deg_overlap50      overlap of the 50 genes with the largest predicted and measured change
  pass               share of items where pearson_delta beats the mean shift (the benchmark's pass rule)
Writes runs/pert_text/metrics.{csv,md}.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "runs"
SETS = [("Norman 2019", "NormanWeissman2019_filtered", "pert_pool_v0", "predict"),
        ("Replogle 2022", "ReplogleWeissman2022_K562_essential", "pert_pool_v0", "predict"),
        ("sciPlex3", "SrivatsanTrapnell2020_sciplex3", "pert_pool_v0", "predict"),
        ("Tahoe-100M", "tahoe100m", "pert_pool_v0", "predict"),
        ("Parse PBMC", "parse_pbmc_cytokines", "pert_pool_v0", "predict"),
        ("Immune Dictionary", "immune_dictionary", "pert_idict_v0", "predict_idict")]
METRICS = ["pearson_delta@hvg", "pearson_delta_sys@hvg", "mse@hvg", "deg_overlap50@hvg"]
LOWER = {"mse@hvg"}
SUF = "_txt4b"

rows = []
for name, ds, pub, pred in SETS:
    cols = ["item_id", "respondent_id", "metric", "value"]
    filt = [("metric", "in", METRICS)]
    t = pd.read_parquet(R / "pert_text" / pred / f"{ds}.perturbation.scores.parquet", columns=cols, filters=filt)
    t = t[t["respondent_id"].str.endswith(SUF) | (t["respondent_id"] == "mean_shift")]
    base_ids = {r[: -len(SUF)] for r in t["respondent_id"].unique() if r.endswith(SUF)}
    b = pd.read_parquet(R / pub / f"{ds}.perturbation.scores.parquet", columns=cols, filters=filt)
    b = b[b["respondent_id"].isin(base_ids | {"mean_shift"})]
    ms = b[(b["respondent_id"] == "mean_shift") & (b["metric"] == "pearson_delta@hvg")].set_index("item_id")["value"]
    for m in sorted(base_ids):
        if m not in set(b["respondent_id"]):
            continue
        for arm, tab, rid in (("builtin", b, m), ("text", t, m + SUF)):
            x = tab[tab["respondent_id"] == rid]
            p = x.pivot_table(index="item_id", columns="metric", values="value")
            p["pass"] = (p["pearson_delta@hvg"] > ms.reindex(p.index)).astype(float)
            for k, v in p.mean().items():
                rows.append({"screen": name, "model": m, "arm": arm, "metric": k, "value": v, "items": len(p)})
L = pd.DataFrame(rows)
L.to_csv(R / "pert_text" / "metrics.csv", index=False)

W = L.pivot_table(index=["screen", "model", "metric"], columns="arm", values="value").reset_index()
W["diff"] = W["text"] - W["builtin"]
W["better"] = np.where(W["metric"].isin(LOWER), W["diff"] < 0, W["diff"] > 0)
order = [s[0] for s in SETS]
lines = ["# Raw metrics, text card vs built-in features (unseen perturbations)", "",
         "Per screen: pairs where the text card is better / all pairs, and the median of text minus built-in "
         "(for MSE lower is better). Metrics over the 2,000 HVGs; values are item means per model.", "",
         "| screen | Pearson Δ | Pearson Δ beyond mean shift | MSE | top-50 gene overlap | pass rate |",
         "|---|---|---|---|---|---|"]
for s in order:
    cells = []
    for k in METRICS + ["pass"]:
        g = W[(W["screen"] == s) & (W["metric"] == k)]
        fmt = "{:+.4f}" if k == "mse@hvg" else "{:+.3f}"
        cells.append(f"{int(g['better'].sum())}/{len(g)}, {fmt.format(g['diff'].median())}")
    lines.append(f"| {s} | " + " | ".join(cells) + " |")
lines += ["", "## Best value per screen (any model)", "",
          "| screen | metric | best built-in | best text |", "|---|---|---|---|"]
for s in order:
    for k in METRICS + ["pass"]:
        g = W[(W["screen"] == s) & (W["metric"] == k)]
        f = (lambda c: g[c].min()) if k in LOWER else (lambda c: g[c].max())
        lines.append(f"| {s} | {k} | {f('builtin'):.4f} | {f('text'):.4f} |")
(R / "pert_text" / "metrics.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:4 + 2 + len(order)]))

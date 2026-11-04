#!/usr/bin/env python
"""One figure per metric: every feature-driven model with built-in features (grey) and with the Qwen3 text card (blue).

  .venv-text/bin/python scripts/pert_text/metric_figs.py  (adds src/ to the path)      # after slurm/text_de.slurm (under Slurm: Tahoe is large)

Reads runs/pert_text/de/{builtin,text}/<dataset>.perturbation.scores.parquet (unseen-perturbation split, same folds and
models in both). For each screen and model: the item mean of the metric with a +/-1 standard error bar, rows sorted by
the better of the two versions, the mean shift as a dashed reference line. Writes runs/pert_text/figures/metrics/
<metric>.{png,pdf} and runs/pert_text/de/summary.{csv,md} (wins and median text - built-in per screen and metric).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from vcb.names import plain_name  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DE = ROOT / "runs" / "pert_text" / "de"
FIG = ROOT / "runs" / "pert_text" / "figures" / "metrics"
FIG.mkdir(parents=True, exist_ok=True)
SCREENS = [("Norman 2019", "NormanWeissman2019_filtered"), ("Replogle 2022", "ReplogleWeissman2022_K562_essential"),
           ("sciPlex3", "SrivatsanTrapnell2020_sciplex3"), ("Tahoe-100M", "tahoe100m"),
           ("Parse PBMC", "parse_pbmc_cytokines"), ("Immune Dictionary", "immune_dictionary")]
# metric id -> (title, x label, lower is better)
METRICS = {
    "pearson_delta@hvg": ("Pearson Δ", "Pearson r of predicted vs measured change (2,000 HVGs)", False),
    "pearson_delta_sys@hvg": ("Pearson Δ beyond the mean shift", "Pearson r after removing the mean shift", False),
    "mse@hvg": ("Mean squared error", "MSE of the change (lower is better)", True),
    "pass": ("Pass rate", "share of items beating the mean shift", False),
    "de_precision20@hvg": ("Top-20 DE precision", "share of the 20 most-changed genes recovered", False),
    "de_dir_acc20@hvg": ("Top-20 DE direction accuracy", "share of the 20 DE genes with the right sign", False),
    "pearson_de20@hvg": ("Pearson on top-20 DE genes", "Pearson r over the 20 DE genes", False),
    "spearman_de20@hvg": ("Spearman on top-20 DE genes", "Spearman ρ over the 20 DE genes", False),
    "de_precision50@hvg": ("Top-50 DE precision", "share of the 50 most-changed genes recovered", False),
    "de_dir_acc50@hvg": ("Top-50 DE direction accuracy", "share of the 50 DE genes with the right sign", False),
    "pearson_de50@hvg": ("Pearson on top-50 DE genes", "Pearson r over the 50 DE genes", False),
    "spearman_de50@hvg": ("Spearman on top-50 DE genes", "Spearman ρ over the 50 DE genes", False),
}
SUF = "_txt4b"
GREY, BLUE = "#8a93a2", "#0f5fb5"


def load(arm, ds):
    p = DE / arm / f"{ds}.perturbation.scores.parquet"
    if not p.exists():
        return None
    s = pd.read_parquet(p, columns=["item_id", "respondent_id", "metric", "value"],
                        filters=[("metric", "in", [m for m in METRICS if m != "pass"])])
    s["respondent_id"] = s["respondent_id"].str.removesuffix(SUF)
    w = s.pivot_table(index=["respondent_id", "item_id"], columns="metric", values="value")
    ms = w.loc["mean_shift", "pearson_delta@hvg"]
    w["pass"] = (w["pearson_delta@hvg"].values > ms.reindex(w.index.get_level_values("item_id")).values).astype(float)
    return w


stats, have = [], []
for name, ds in SCREENS:
    b, t = load("builtin", ds), load("text", ds)
    if b is None or t is None:
        print(f"skip {name}: scores missing")
        continue
    have.append(name)
    models = sorted((set(b.index.get_level_values(0)) & set(t.index.get_level_values(0))) - {"mean_shift"})
    for arm, w in (("builtin", b), ("text", t)):
        for m in models + ["mean_shift"]:
            x = w.loc[m]
            for k in METRICS:
                if k in x:
                    v = x[k].dropna()
                    stats.append({"screen": name, "model": m, "arm": arm, "metric": k, "mean": v.mean(),
                                  "se": v.std(ddof=1) / np.sqrt(len(v)), "n": len(v)})
S = pd.DataFrame(stats)
S.to_csv(DE / "summary.csv", index=False)

plt.rcParams.update({"font.size": 7.5, "font.family": "sans-serif", "axes.spines.top": False,
                     "axes.spines.right": False, "axes.spines.left": False})
for k, (title, xlabel, lower) in METRICS.items():
    if k not in set(S["metric"]):
        continue
    n = len(have)
    fig, axs = plt.subplots(1, n, figsize=(2.15 * n + 1.4, 4.6), squeeze=False)
    for ax, name in zip(axs[0], have):
        g = S[(S["screen"] == name) & (S["metric"] == k)]
        ref = g[(g["model"] == "mean_shift") & (g["arm"] == "builtin")]["mean"]
        g = g[g["model"] != "mean_shift"].pivot_table(index="model", columns="arm", values=["mean", "se"])
        key = g[("mean", "builtin")].combine(g[("mean", "text")], min if lower else max)
        g = g.loc[key.sort_values(ascending=lower).index]
        y = np.arange(len(g))[::-1]
        for yi, (_, r) in zip(y, g.iterrows()):
            ax.plot([r[("mean", "builtin")], r[("mean", "text")]], [yi, yi], color="#c9ced6", lw=1, zorder=1)
        ax.errorbar(g[("mean", "builtin")], y, xerr=g[("se", "builtin")], fmt="o", ms=3.5, color=GREY, lw=0.8, zorder=2)
        ax.errorbar(g[("mean", "text")], y, xerr=g[("se", "text")], fmt="o", ms=3.5, color=BLUE, lw=0.8, zorder=3)
        if len(ref):
            ax.axvline(ref.iloc[0], color="#b0413e", lw=0.8, ls="--", zorder=0)
        ax.set_yticks(y)
        ax.set_yticklabels([plain_name(m) for m in g.index], fontsize=6.3)
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", color="#eceff3", lw=0.6)
        better = (g[("mean", "text")] < g[("mean", "builtin")]) if lower else (g[("mean", "text")] > g[("mean", "builtin")])
        ax.set_title(f"{name}\ntext better in {int(better.sum())}/{len(g)}", fontsize=8)
        ax.locator_params(axis="x", nbins=4)
    handles = [plt.Line2D([], [], marker="o", ls="", color=GREY, label="built-in features"),
               plt.Line2D([], [], marker="o", ls="", color=BLUE, label="Qwen3 text card"),
               plt.Line2D([], [], ls="--", color="#b0413e", label="mean shift")]
    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.02))
    fig.suptitle(title, y=1.07, fontsize=10, fontweight="bold")
    fig.supxlabel(xlabel, fontsize=8)
    fig.tight_layout(w_pad=0.8)
    stem = k.replace("@hvg", "")
    fig.savefig(FIG / f"{stem}.png", dpi=180, bbox_inches="tight")
    fig.savefig(FIG / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)

# per screen and metric: wins and median text - built-in
P = S[S["model"] != "mean_shift"].pivot_table(index=["screen", "model", "metric"], columns="arm", values="mean").reset_index()
P["diff"] = P["text"] - P["builtin"]
P["lower"] = P["metric"].map(lambda m: METRICS[m][2])
P["better"] = np.where(P["lower"], P["diff"] < 0, P["diff"] > 0)
lines = ["# Text card vs built-in features, every metric (unseen perturbations)", "",
         "Cell: models where the text card is better / models, median of text − built-in. DE genes = the k genes with the "
         "largest measured change among the 2,000 HVGs.", "",
         "| metric | " + " | ".join(have) + " |", "|---" * (len(have) + 1) + "|"]
for k, (title, _, _) in METRICS.items():
    row = [title]
    for name in have:
        g = P[(P["screen"] == name) & (P["metric"] == k)]
        row.append(f"{int(g['better'].sum())}/{len(g)}, {g['diff'].median():+.3g}" if len(g) else "")
    lines.append("| " + " | ".join(row) + " |")
(DE / "summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))

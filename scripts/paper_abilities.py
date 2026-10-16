#!/usr/bin/env python
"""Ability figures for the main text and ability/accuracy tables for the appendix.

Writes paper/bench/fig_abilities.{png,pdf}, paper/bench/tab_abilA.tex, paper/bench/tab_abilB.tex.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from vcb import RUNS, ROOT
from vcb.names import display_name, family, plain_name

out = ROOT / "paper" / "bench"
INK, MUTED = "#0b0b0b", "#52514e"
FAM_COLORS = {"PCA": "#2a78d6", "Random projection": "#eb6834", "Kernel features": "#1baf7a", "NMF": "#eda100", "ICA": "#e87ba4", "GMM": "#008300", "scVI": "#4a3aa7", "Floor": "#9a9995",
              "Ridge": "#2a78d6", "PCA regression": "#1baf7a", "Gaussian process": "#eb6834", "KNN": "#eda100", "Mean shift": "#e87ba4", "Low-rank": "#4a3aa7", "scGen": "#e34948"}
plt.rcParams.update({"font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": INK, "axes.grid": True, "grid.color": "#e6e5e1", "grid.linewidth": 0.6, "axes.axisbelow": True})

aA = pd.read_csv(RUNS / "repr_pooled_v2" / "rasch" / "cell_level.abilities.csv").sort_values("ability")
aB = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / "pooled.abilities.csv").sort_values("ability")
# collapse seeds: average the two seeds of a stochastic respondent for the figure
def collapse(a):
    a = a.copy()
    a["base"] = a["respondent_id"].str.replace(r"_s\d$", "", regex=True)
    g = a.groupby("base", as_index=False).agg(ability=("ability", "mean"), p_correct=("p_correct", "mean"), n=("ability", "size"))
    g["label"] = g["base"].map(lambda r: plain_name(r + "_s0").replace(" (seed 0)", " (2 seeds)") if r in ("random_k32", "random_shift") or r.startswith("rproj") else plain_name(r))
    g["family"] = g["base"].map(family)
    return g.sort_values("ability")

gA, gB = collapse(aA), collapse(aB)
fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.6), gridspec_kw={"width_ratios": [1, 1]})
for ax, g, title in [(axes[0], gA, "a  Representation"), (axes[1], gB, "b  Perturbation")]:
    y = np.arange(len(g))
    ax.hlines(y, 0, g["ability"], color="#d9d8d3", lw=1)
    for fam in g["family"].unique():
        m = g["family"] == fam
        ax.scatter(g.loc[m, "ability"], y[m], s=36, color=FAM_COLORS.get(fam, "#333"), label=fam, zorder=3, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(g["label"], fontsize=7.5)
    ax.axvline(0, color=MUTED, lw=0.8)
    ax.set_xlabel("ability")
    ax.set_title(title, loc="left", fontsize=9.5, color=INK)
    ax.legend(frameon=False, fontsize=7, loc="lower right")
fig.tight_layout(w_pad=3)
fig.savefig(out / "fig_abilities.png", dpi=220)
fig.savefig(out / "fig_abilities.pdf")
print("wrote fig_abilities")

# appendix tables
rowsA = "\n".join(f"{display_name(r.respondent_id)} & {r.ability:.2f} & {r.p_correct:.3f} \\\\" for r in aA.sort_values('ability', ascending=False).itertuples())
(out / "tab_abilA.tex").write_text("\\begin{tabular}{@{}lrr@{}}\n\\toprule\nModel & Ability & Accuracy \\\\\n\\midrule\n" + rowsA + "\n\\bottomrule\n\\end{tabular}\n")
rowsB = "\n".join(f"{display_name(r.respondent_id)} & {r.ability:.2f} \\\\" for r in aB.sort_values('ability', ascending=False).itertuples())
(out / "tab_abilB.tex").write_text("\\begin{tabular}{@{}lr@{}}\n\\toprule\nModel & Ability \\\\\n\\midrule\n" + rowsB + "\n\\bottomrule\n\\end{tabular}\n")
print("wrote tables:", len(aA), "A rows,", len(aB), "B rows")

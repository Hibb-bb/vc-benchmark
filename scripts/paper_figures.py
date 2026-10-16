#!/usr/bin/env python
"""Figures for the benchmark paper draft -> paper/bench/*.png and *.pdf."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from vcb import RUNS, ROOT

out = ROOT / "paper" / "bench"
stats = json.load(open(out / "stats.json"))
BLUE, ORANGE, GRAY, INK, MUTED = "#2a78d6", "#eb6834", "#b8b7b1", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED, "axes.grid": True, "grid.color": "#e6e5e1", "grid.linewidth": 0.6, "axes.axisbelow": True})

A_RUN = RUNS / "repr_pooled_v2"
dA = pd.read_csv(A_RUN / "rasch" / "cell_level.difficulties.csv")
itemsA = pd.read_parquet(A_RUN / "items.parquet")
PANEL_NAMES = {r["run"]: (r["name"] + (", " + r["held_out"] + " held out" if r["held_out"] in ("studies", "tissues") else "")) for r in stats["compA_panels"]}
dB = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / "pooled.difficulties.csv")
aA = pd.read_csv(A_RUN / "rasch" / "cell_level.abilities.csv")
aB = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / "pooled.abilities.csv")
cov = pd.concat([pd.read_parquet(p) for p in (RUNS / "pert_pool_v0").glob("*.perturbation.items.parquet")])
cov = cov[~cov.index.duplicated()]

fig, axes = plt.subplots(2, 2, figsize=(10, 7.8))
axes = axes.ravel()
bins = np.arange(-6, 6.01, 0.5)


def hist_panel(ax, diff, abil, color, title, ylabel):
    d = diff[~diff["degenerate"]]
    ax.hist(d["difficulty"], bins=bins, color=color, edgecolor="white", linewidth=0.5)
    lo, hi = abil["ability"].min(), abil["ability"].max()
    ax.axvspan(lo, hi, color=GRAY, alpha=0.25, lw=0, zorder=0)
    ax.axvline(abil["ability"].max(), color=INK, lw=1, ls="--")
    n_deg = int(diff["degenerate"].sum())
    ax.set_title(f"{title}\n{len(d):,} informative items\n({n_deg:,} passed by none or all, excluded)", loc="left", fontsize=8, color=INK)
    ax.set_xlabel("item difficulty (logits)")
    ax.set_ylabel(ylabel)
    ax.set_xlim(-6, 6)


hist_panel(axes[0], dA, aA, BLUE, "a  Representation: cells (pooled)", "items")
# b: per-panel distributions on the pooled representation scale
mA = dA.merge(itemsA[["source_run"]], left_on="item_id", right_index=True)
mA = mA[~mA["degenerate"]]
orderA = mA.groupby("source_run")["difficulty"].median().sort_values().index
ax = axes[1]
dataA = [mA.loc[mA["source_run"] == r, "difficulty"].values for r in orderA]
ax.boxplot(dataA, vert=False, widths=0.6, showfliers=False, patch_artist=True, medianprops=dict(color=INK, lw=1.2), boxprops=dict(facecolor=BLUE, alpha=0.55, edgecolor=BLUE, lw=0.8), whiskerprops=dict(color=MUTED, lw=0.8), capprops=dict(color=MUTED, lw=0.8))
ax.set_yticks(range(1, len(orderA) + 1))
ax.set_yticklabels([f"{PANEL_NAMES.get(r, r)}  (n={len(d):,})" for r, d in zip(orderA, dataA)], fontsize=7)
ax.axvspan(aA["ability"].min(), aA["ability"].max(), color=GRAY, alpha=0.25, lw=0, zorder=0)
ax.axvline(aA["ability"].max(), color=INK, lw=1, ls="--")
ax.set_xlim(-6, 6)
ax.set_xlabel("item difficulty (logits), pooled scale", fontsize=8.5)
ax.set_title("b  Representation: by panel\n(informative items, pooled scale)\n", loc="left", fontsize=8, color=INK)
hist_panel(axes[2], dB, aB, ORANGE, "c  Perturbation: conditions (pooled)", "items")

# d: per-dataset distributions on the pooled perturbation scale
m = dB.merge(cov, left_on="item_id", right_index=True)
m = m[~m["degenerate"]]
short = {"ReplogleWeissman2022_K562_gwps": "Replogle K562 genome-wide", "ReplogleWeissman2022_K562_essential": "Replogle K562 essential", "ReplogleWeissman2022_rpe1": "Replogle RPE1", "NadigOConner2024_jurkat": "Nadig Jurkat", "NadigOConner2024_hepg2": "Nadig HepG2", "SrivatsanTrapnell2020_sciplex3": "sciPlex3 (drug)", "McFarlandTsherniak2020": "McFarland (drug)", "FrangiehIzar2021_RNA": "Frangieh (KO)", "NormanWeissman2019_filtered": "Norman (CRISPRa)", "AdamsonWeissman2016_GSM2406681_10X010": "Adamson", "TianKampmann2021_CRISPRi": "Tian 2021 neurons", "TianKampmann2019_iPSC": "Tian 2019 iPSC", "TianKampmann2019_day7neuron": "Tian 2019 neurons", "tahoe100m": "Tahoe-100M (drug)", "parse_pbmc_cytokines": "Parse PBMC (cytokine)"}
order = m.groupby("dataset_id")["difficulty"].median().sort_values().index
ax = axes[3]
data = [m.loc[m["dataset_id"] == ds, "difficulty"].values for ds in order]
bp = ax.boxplot(data, vert=False, widths=0.6, showfliers=False, patch_artist=True, medianprops=dict(color=INK, lw=1.2), boxprops=dict(facecolor=ORANGE, alpha=0.55, edgecolor=ORANGE, lw=0.8), whiskerprops=dict(color=MUTED, lw=0.8), capprops=dict(color=MUTED, lw=0.8))
ax.set_yticks(range(1, len(order) + 1))
ax.set_yticklabels([f"{short.get(ds, ds)}  (n={len(d):,})" for ds, d in zip(order, data)], fontsize=8)
ax.axvspan(aB["ability"].min(), aB["ability"].max(), color=GRAY, alpha=0.25, lw=0, zorder=0)
ax.axvline(aB["ability"].max(), color=INK, lw=1, ls="--")
ax.set_xlim(-6, 4)
ax.set_xlabel("item difficulty (logits), pooled scale", fontsize=8.5)
ax.set_title("d  Perturbation: by dataset\n(informative items, pooled scale)\n", loc="left", fontsize=8, color=INK)
fig.text(0.005, 0.005, "shaded band: ability range of the classical pool;  dashed: best respondent", fontsize=8, color=MUTED)
fig.tight_layout(rect=(0, 0.02, 1, 1), w_pad=2, h_pad=2)
fig.savefig(out / "fig_difficulty.png", dpi=220)
fig.savefig(out / "fig_difficulty.pdf")
print("wrote", out / "fig_difficulty.png")

# ---- retirement figure: fraction retired vs pass-probability threshold, for three model strengths ----
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
thresholds = [0.75, 0.80, 0.85, 0.90, 0.95, 0.99]
deltas = [(0, "as able as the best current model", "#9a9995"), (1, "one unit above", "#2a78d6"), (2, "two units above", "#eb6834")]
fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.2), sharey=True)
for ax, (diff, abil, title) in zip(axes, [(dA, aA, "a  Representation items"), (dB, aB, "b  Perturbation items")]):
    d = diff[~diff["degenerate"]]["difficulty"].values
    best = abil["ability"].max()
    for delta, label, color in deltas:
        p = sigmoid(best + delta - d)
        frac = [(p >= t).mean() for t in thresholds]
        ax.plot(thresholds, frac, color=color, lw=2, marker="o", ms=4.5, label=label)
    ax.set_xticks(thresholds)
    ax.set_xticklabels([f"{t:.2f}" for t in thresholds])
    ax.set_xlabel("pass-probability threshold for retiring an item")
    ax.set_ylim(0, 1)
    ax.set_title(title, loc="left", fontsize=9.5, color=INK)
axes[0].set_ylabel("fraction of items retired")
axes[0].legend(frameon=False, fontsize=7.5, loc="upper right", title="hypothetical model", title_fontsize=7.5)
fig.tight_layout(w_pad=2)
fig.savefig(out / "fig_retire.png", dpi=220)
fig.savefig(out / "fig_retire.pdf")
print("wrote", out / "fig_retire.png")

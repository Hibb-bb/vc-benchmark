#!/usr/bin/env python
"""Pipeline diagram for the Methods section -> paper/bench/fig_pipeline.{png,pdf}.
One general pipeline, applies to both components."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from vcb import ROOT

out = ROOT / "paper" / "bench"
ACCENT, INK, MUTED = "#4440C6", "#0b0b0b", "#52514e"
fig, ax = plt.subplots(figsize=(11, 2.4))
ax.set_xlim(0, 11); ax.set_ylim(0, 2.4); ax.axis("off")
steps = [
    ("Data", "public atlases\nand screens"),
    ("Items", "one test case\neach"),
    ("Models", "simple and\nlearned"),
    ("Pass / fail\nmatrix", "models x items"),
    ("Rasch fit", r"$P(\mathrm{pass})=\sigma(\theta-b)$"),
    ("Ability $\\theta$\nDifficulty $b$", "per model\nper item"),
]
w, h, gap, x0, y0 = 1.5, 1.7, 0.3, 0.2, 0.35
for i, (title, sub) in enumerate(steps):
    x = x0 + i * (w + gap)
    fc = ACCENT if i in (3, 4) else "white"
    ax.add_patch(FancyBboxPatch((x, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15", fc=fc, ec=ACCENT, lw=1.6))
    tc = "white" if i in (3, 4) else INK
    ax.text(x + w / 2, y0 + h * 0.66, title, ha="center", va="center", fontsize=13, color=tc, fontweight="bold")
    ax.text(x + w / 2, y0 + h * 0.27, sub, ha="center", va="center", fontsize=10.5, color=("white" if i in (3, 4) else MUTED))
    if i < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((x + w + 0.03, y0 + h / 2), (x + w + gap - 0.03, y0 + h / 2), arrowstyle="-|>", mutation_scale=16, color=MUTED, lw=1.6))
fig.tight_layout(pad=0.2)
fig.savefig(out / "fig_pipeline.png", dpi=220)
fig.savefig(out / "fig_pipeline.pdf")
print("wrote fig_pipeline")

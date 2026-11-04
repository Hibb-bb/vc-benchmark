#!/usr/bin/env python
"""Figure and table numbers for the text-card technical report (paper/text_cards.tex).

  .venv-text/bin/python scripts/pert_text/paper_fig.py

Reads cache/text_artifact/data.json (the abilities shown in the text-card artifact; built by cache/text_artifact/build.py
from runs/pert_text/rank*/) and writes paper/textcards/fig_pairs.pdf plus paper/textcards/pairs.csv.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "paper" / "textcards"
OUT.mkdir(parents=True, exist_ok=True)
d = json.loads((ROOT / "cache" / "text_artifact" / "data.json").read_text())

rows = []
for s in d["screens"]:
    for r in s["rows"]:
        if r["b"] is not None and r["t"] is not None:
            rows.append({"screen": s["name"], "model": r["model"], "builtin": r["b"], "text": r["t"]})
P = pd.DataFrame(rows)
P.to_csv(OUT / "pairs.csv", index=False)

plt.rcParams.update({"font.size": 8, "font.family": "sans-serif", "axes.spines.top": False, "axes.spines.right": False})
fig, axs = plt.subplots(1, 6, figsize=(7.2, 1.55))
for ax, s in zip(axs, d["screens"]):
    g = P[P["screen"] == s["name"]]
    lo = min(g["builtin"].min(), g["text"].min()) - 0.3
    hi = max(g["builtin"].max(), g["text"].max()) + 0.3
    ax.plot([lo, hi], [lo, hi], color="0.6", lw=0.7, ls="--", zorder=0)
    win = g["text"] > g["builtin"]
    ax.scatter(g.loc[win, "builtin"], g.loc[win, "text"], s=9, color="#2f6db5", lw=0)
    ax.scatter(g.loc[~win, "builtin"], g.loc[~win, "text"], s=9, color="#b0413e", lw=0)
    ax.set_xlim(lo, hi); ax.set_ylim(lo, hi); ax.set_aspect("equal")
    name = s["name"].replace("Replogle 2022, K562 essential", "Replogle 2022").replace("Parse PBMC cytokines", "Parse PBMC")
    ax.set_title(f"{name}\n{int(win.sum())}/{len(g)} above line", fontsize=7.5)
    ax.tick_params(labelsize=6.5, length=2)
    ax.locator_params(nbins=4)
axs[0].set_ylabel("ability, text card")
fig.supxlabel("ability, built-in features", fontsize=8, y=0.02)
fig.tight_layout(pad=0.3, w_pad=0.6)
fig.savefig(OUT / "fig_pairs.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig_pairs.png", dpi=200, bbox_inches="tight")
print(P.groupby("screen").apply(lambda g: pd.Series({"pairs": len(g), "wins": int((g.text > g.builtin).sum()),
                                                     "median_gain": float(np.median(g.text - g.builtin))})))

# ---- example cards (paper/textcards/fig_cards.tex): one gene, one drug, one cytokine, cut to about 60 words ----
import re
CARDS = json.loads((ROOT / "cache" / "text_artifact" / "cards.json").read_text())
PICK = [("Gene", "CRISPRi::CDK9", "Gene (CRISPRi)"), ("Drug", "drug::Trametinib", "Drug"),
        ("Cytokine", "cytokine::IFN-gamma", "Cytokine")]
LABELS = ["Perturbation", "Type", "Target gene", "Targets", "Mechanism of action", "Approved for human use", "ChEMBL ID",
          "Cytokine family", "Encoded by", "Receptor genes"]


def tex(s):
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
                 ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s


boxes = []
for group, key, head in PICK:
    c = next(x for x in CARDS[group] if x["key"] == key)
    words = c["text"].split()
    body = tex(" ".join(words[:60])) + (" [\\dots]" if len(words) > 60 else "")
    body = re.sub(r"(^|\. )(" + "|".join(LABELS) + "):", lambda m: m.group(1) + r"\textbf{" + m.group(2) + ":}", body)
    boxes.append(f"\\cardbox{{{head}: {tex(c['key'].split('::')[1])}}}{{{len(words)} words}}{{{body}}}")
(OUT / "fig_cards.tex").write_text("\n\\hfill\n".join(boxes) + "\n")
print((OUT / "fig_cards.tex").read_text()[:600])

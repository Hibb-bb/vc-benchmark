#!/usr/bin/env python
"""Does representation difficulty predict perturbation difficulty? Item-level link on Parse PBMC.

The Parse 10M PBMC atlas is in both components: cell type is the label of the annotation panel
(component A, donors held out) and half of the context (donor | cell type) of the cytokine screen
(component B). Every B item therefore has a context whose representation difficulty is already
estimated. This script aggregates A difficulty per cell type and per (donor, cell type) and
correlates it with the mean B difficulty of the items in that context.

  python scripts/link_repr_pert.py            # writes runs/link_parse_v0/{link.md,*.csv,*.png,link.json}

Also, when latent_* respondents exist in the B scores (the shared-encoder family), the script
correlates A ability and B ability per encoder (`encoders` section).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from vcb import RUNS
from vcb.names import family, plain_name

OUT = RUNS / "link_parse_v0"
OUT.mkdir(parents=True, exist_ok=True)
A_RUN, A_POOLED = RUNS / "repr_parse_pbmc_celltype", RUNS / "repr_pooled_v3"
B_RUN = RUNS / "pert_pool_v0"
B_JOINT = RUNS / "pert_joint_v0"   # main pool + latent_* family on one scale (slurm/pert_latent_fit.slurm)


def norm_type(s: pd.Series) -> pd.Series:
    """The harmonizer replaced '/' by '-' in B contexts (h5py group separator)."""
    return s.astype(str).str.replace("/", "-", regex=False)


# ---------------- component A: cell items -> cell type / donor x type ----------------
items_a = pd.read_parquet(A_RUN / "items.parquet")
items_a["type_n"] = norm_type(items_a["cell_type"])
dA = {}
dA["panel"] = pd.read_csv(A_RUN / "rasch" / "cell_level.difficulties.csv").set_index("item_id")
pooled = pd.read_csv(A_POOLED / "rasch" / "cell_level.difficulties.csv")
pooled = pooled[pooled["item_id"].str.startswith("repr_parse_pbmc_celltype::")].copy()
pooled["item_id"] = pooled["item_id"].str.split("::", n=1).str[1]
dA["pooled"] = pooled.set_index("item_id")


def agg_a(diff: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    d = diff.join(items_a[["type_n", "donor", "n_train_same_type", "total_counts"]], how="inner")
    inf = d[~d["degenerate"]]
    g = inf.groupby(keys, observed=True)
    out = pd.DataFrame({"a_items": d.groupby(keys, observed=True).size(), "a_diff": g["difficulty"].mean(), "a_diff_se": g["difficulty"].std() / np.sqrt(g.size()),
                        "a_nobody": d.groupby(keys, observed=True)["p_correct"].apply(lambda s: (s == 0).mean()), "a_pass": d.groupby(keys, observed=True)["p_correct"].mean(),
                        "a_train_support": d.groupby(keys, observed=True)["n_train_same_type"].median()})
    return out


# ---------------- component B: condition items -> context ----------------
def load_b(scheme: str, pooled: bool) -> pd.DataFrame:
    name = {"context": "pooled_context", "perturbation": "pooled"}[scheme] if pooled else f"parse_pbmc_cytokines.{scheme}"
    d = pd.read_csv(B_RUN / "rasch" / f"{name}.difficulties.csv")
    d = d[d["item_id"].str.startswith("parse_pbmc_cytokines::")].set_index("item_id")
    it = pd.read_parquet(B_RUN / f"parse_pbmc_cytokines.{scheme}.items.parquet")
    d = d.join(it[["perturbation", "context", "n_cells", "delta_l2"]], how="inner")
    ctx = d["context"].astype(str).str.split("|", n=1, expand=True)
    d["donor"], d["type_n"] = ctx[0], ctx[1]
    return d


def agg_b(d: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    inf = d[~d["degenerate"]]
    g = inf.groupby(keys, observed=True)
    return pd.DataFrame({"b_items": d.groupby(keys, observed=True).size(), "b_diff": g["difficulty"].mean(), "b_diff_se": g["difficulty"].std() / np.sqrt(g.size()),
                         "b_nobody": d.groupby(keys, observed=True)["p_correct"].apply(lambda s: (s == 0).mean()), "b_pass": d.groupby(keys, observed=True)["p_correct"].mean(),
                         "b_n_cells": d.groupby(keys, observed=True)["n_cells"].median(), "b_effect": d.groupby(keys, observed=True)["delta_l2"].median()})


def corr_block(df: pd.DataFrame, x="a_diff", y="b_diff") -> dict:
    d = df.dropna(subset=[x, y])
    if len(d) < 4:
        return {"n": len(d)}
    rho, p = stats.spearmanr(d[x], d[y])
    r, pp = stats.pearsonr(d[x], d[y])
    out = {"n": int(len(d)), "spearman": float(rho), "spearman_p": float(p), "pearson": float(r), "pearson_p": float(pp)}
    # partial Spearman controlling for log cells per B item (deeper pseudobulks are easier to hit)
    if "b_n_cells" in d and d["b_n_cells"].nunique() > 2:
        z = np.log(d["b_n_cells"])
        rx = d[x] - np.polyval(np.polyfit(z, d[x], 1), z)
        ry = d[y] - np.polyval(np.polyfit(z, d[y], 1), z)
        out["spearman_partial_ncells"] = float(stats.spearmanr(rx, ry)[0])
    return out


res = {"levels": {}}
tables = {}
for a_scale in ("panel", "pooled"):
    for scheme in ("context", "perturbation"):
        for b_scale in ("screen", "pooled"):
            db = load_b(scheme, pooled=(b_scale == "pooled"))
            for level, keys in (("cell_type", ["type_n"]), ("donor_type", ["donor", "type_n"])):
                t = agg_a(dA[a_scale], keys).join(agg_b(db, keys), how="inner")
                tag = f"A_{a_scale}__B_{scheme}_{b_scale}__{level}"
                tables[tag] = t
                res["levels"][tag] = corr_block(t)
                res["levels"][tag]["nobody_spearman"] = float(stats.spearmanr(t["a_nobody"], t["b_nobody"])[0]) if len(t) > 3 else None

# headline: per-panel A scale, context-scheme B screen scale (the primary setting), both levels
main = {k: tables[k] for k in ("A_panel__B_context_screen__cell_type", "A_panel__B_context_screen__donor_type")}
for k, t in main.items():
    t.round(4).to_csv(OUT / f"{k}.csv")
res["headline"] = {k: res["levels"][k] for k in main}
res["cell_type_table"] = main["A_panel__B_context_screen__cell_type"].reset_index().round(3).to_dict(orient="records")
res["donor_type_table"] = main["A_panel__B_context_screen__donor_type"].reset_index().round(3).to_dict(orient="records")

# ---------------- model level: shared-encoder respondents, if present ----------------
abA = pd.read_csv(A_POOLED / "rasch" / "cell_level.abilities.csv").set_index("respondent_id")
enc = []
for tag in ("pooled_context", "pooled"):
    f = B_JOINT / "rasch" / f"{tag}.abilities.csv"
    if not f.exists():
        continue
    abB = pd.read_csv(f).set_index("respondent_id")
    for rid in abB.index:
        if not rid.startswith("latent_"):
            continue
        base = rid[len("latent_"):]
        if base in abA.index:
            enc.append({"scale": tag, "encoder": base, "name": plain_name(base), "family": family(base), "a_ability": float(abA.loc[base, "ability"]), "a_se": float(abA.loc[base, "se"]),
                        "b_ability": float(abB.loc[rid, "ability"]), "b_se": float(abB.loc[rid, "se"]), "b_pass": float(abB.loc[rid, "p_correct"]), "b_outfit": float(abB.loc[rid, "outfit"])})
if enc:
    e = pd.DataFrame(enc)
    res["encoders"] = {"rows": enc, "corr": {}}
    for tag, g in e.groupby("scale"):
        res["encoders"]["corr"][tag] = corr_block(g, "a_ability", "b_ability")
        real = g[g["family"] != "Random projection"]
        res["encoders"]["corr"][tag + "_without_rproj"] = corr_block(real, "a_ability", "b_ability")
    e.round(3).to_csv(OUT / "encoders.csv", index=False)

def _clean(o):
    """JSON has no NaN: write nulls instead."""
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


(OUT / "link.json").write_text(json.dumps(_clean(res), indent=1))

# ---------------- figure ----------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

n_ax = 2 + (1 if enc else 0)
fig, axes = plt.subplots(1, n_ax, figsize=(5.2 * n_ax, 4.6))
for ax, (k, t) in zip(axes, main.items()):
    c = res["levels"][k]
    ax.errorbar(t["a_diff"], t["b_diff"], xerr=t["a_diff_se"], yerr=t["b_diff_se"], fmt="o", ms=4, color="#2f6fde", ecolor="#b8c4d6", lw=0.8, capsize=0)
    if k.endswith("cell_type"):
        for ty, r in t.iterrows():
            ax.annotate(ty, (r["a_diff"], r["b_diff"]), fontsize=7, xytext=(3, 3), textcoords="offset points")
    ax.set_xlabel("representation difficulty (A), mean over cells, logits")
    ax.set_ylabel("perturbation difficulty (B), mean over cytokines, logits")
    ax.set_title(f"{'cell type' if k.endswith('cell_type') else 'donor x cell type'} (n={c['n']}): Spearman {c['spearman']:+.2f}, p={c['spearman_p']:.2g}", fontsize=10)
    ax.grid(alpha=0.3)
if enc:
    ax = axes[-1]
    g = e[e["scale"] == "pooled_context"] if (e["scale"] == "pooled_context").any() else e
    for fam, gg in g.groupby("family"):
        ax.errorbar(gg["a_ability"], gg["b_ability"], xerr=gg["a_se"], yerr=gg["b_se"], fmt="o", ms=5, label=fam, lw=0.8)
    for _, r in g.iterrows():
        ax.annotate(r["name"], (r["a_ability"], r["b_ability"]), fontsize=6, xytext=(3, 2), textcoords="offset points")
    c = res["encoders"]["corr"].get("pooled_context", res["encoders"]["corr"].get("pooled", {}))
    ax.set_xlabel("representation ability (A), logits")
    ax.set_ylabel("perturbation ability of the same encoder (B), logits")
    ax.set_title(f"shared encoders (n={c.get('n')}): Spearman {c.get('spearman', float('nan')):+.2f}", fontsize=10)
    ax.legend(fontsize=7, frameon=False)
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(OUT / "link_parse.png", dpi=160)

# ---------------- report ----------------
lines = ["# Representation -> perturbation link on Parse PBMC", "",
         "A: `repr_parse_pbmc_celltype` cell-level difficulties (donors held out). B: `parse_pbmc_cytokines` difficulties. "
         "Contexts are joined on (donor, cell type); only the five A test donors overlap. Mean difficulty over informative items; "
         "`nobody` is the share of items no respondent passes.", "", "| A scale | B scheme | B scale | level | n | Spearman | p | partial (log cells) | Pearson | nobody-share Spearman |", "|---|---|---|---|---|---|---|---|---|---|"]
for tag, c in res["levels"].items():
    a, b, lvl = tag.split("__")
    bs = b.split("_")
    lines.append(f"| {a[2:]} | {bs[1]} | {bs[2]} | {lvl} | {c.get('n')} | {c.get('spearman', float('nan')):+.3f} | {c.get('spearman_p', float('nan')):.2g} | {c.get('spearman_partial_ncells', float('nan')):+.3f} | {c.get('pearson', float('nan')):+.3f} | {c.get('nobody_spearman') if c.get('nobody_spearman') is None else round(c['nobody_spearman'], 3)} |")
lines += ["", "## Cell types (A panel scale, B context-scheme screen scale)", "", "| cell type | A items | A diff | A nobody | B items | B diff | B nobody | B cells/item |", "|---|---|---|---|---|---|---|---|"]
for ty, r in main["A_panel__B_context_screen__cell_type"].sort_values("a_diff").iterrows():
    lines.append(f"| {ty} | {int(r.a_items)} | {r.a_diff:+.2f} | {r.a_nobody:.2f} | {int(r.b_items)} | {r.b_diff:+.2f} | {r.b_nobody:.2f} | {int(r.b_n_cells)} |")
if enc:
    lines += ["", "## Shared encoders", "", "| scale | n | Spearman | p | without random projections |", "|---|---|---|---|---|"]
    for tag in ("pooled_context", "pooled"):
        c = res["encoders"]["corr"].get(tag)
        if c:
            c2 = res["encoders"]["corr"][tag + "_without_rproj"]
            lines.append(f"| {tag} | {c['n']} | {c['spearman']:+.3f} | {c['spearman_p']:.2g} | {c2.get('spearman', float('nan')):+.3f} (n={c2['n']}) |")
    lines += ["", "| encoder | family | A ability | B ability | B pass | B outfit | scale |", "|---|---|---|---|---|---|---|"]
    for r in sorted(enc, key=lambda r: -r["a_ability"]):
        lines.append(f"| {r['name']} | {r['family']} | {r['a_ability']:+.2f} | {r['b_ability']:+.2f} | {r['b_pass']:.2f} | {r['b_outfit']:.2f} | {r['scale']} |")
(OUT / "link.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))

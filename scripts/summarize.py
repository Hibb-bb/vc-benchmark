#!/usr/bin/env python
"""Join Rasch difficulties with item covariates and test the plan's predictions.

  python scripts/summarize.py pert --run pert_pool_v0
  python scripts/summarize.py repr --run repr_pool_v0

Writes runs/<run>/summary.md: ability table, difficulty distribution, Spearman correlations
of difficulty with covariates (B: effect size delta_l2, n_cells; A: train support of the
type, depth, compartment), and the saturated / unreachable item lists.
"""
import argparse

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import RUNS

ap = argparse.ArgumentParser()
ap.add_argument("component", choices=["pert", "repr"])
ap.add_argument("--run", required=True)
a = ap.parse_args()
run = RUNS / a.run
L = []


def corr_block(diff, cov, cols, title):
    L.append(f"\n### {title}\n")
    L.append("| covariate | Spearman rho | p | n |\n|---|---|---|---|")
    d = diff.merge(cov, left_on="item_id", right_index=True, how="inner")
    d = d[~d["degenerate"]]
    for c in cols:
        if c not in d or d[c].nunique() < 3:
            continue
        x = pd.to_numeric(d[c], errors="coerce")
        m = x.notna()
        if m.sum() < 10:
            continue
        r, p = spearmanr(d.loc[m, "difficulty"], x[m])
        L.append(f"| {c} | {r:.3f} | {p:.1e} | {m.sum()} |")
    return d


def abil_block(abil, title):
    L.append(f"\n### {title}\n")
    L.append("| respondent | ability | se | p_correct | outfit |\n|---|---|---|---|---|")
    for r in abil.itertuples():
        L.append(f"| {r.respondent_id} | {r.ability:.2f} | {r.se:.2f} | {r.p_correct:.3f} | {r.outfit:.2f} |")


def dist_block(diff):
    d = diff[~diff["degenerate"]]
    q = np.percentile(d["difficulty"], [5, 25, 50, 75, 95])
    L.append(f"\n- items: {len(diff)}; informative (non-degenerate): {len(d)}; nobody passes: {(diff['p_correct']==0).sum()}; everybody passes: {(diff['p_correct']==1).sum()}")
    L.append(f"- difficulty percentiles 5/25/50/75/95: {np.round(q, 2).tolist()}; median SE {d['se'].median():.2f}")
    hist, edges = np.histogram(d["difficulty"], bins=np.arange(-6, 6.5, 1.0))
    L.append("- histogram (bin lower edge: count): " + ", ".join(f"{e:+.0f}: {h}" for e, h in zip(edges[:-1], hist)))


if a.component == "pert":
    L.append(f"# Component B summary: {a.run}\n")
    rasch = run / "rasch"
    for f in sorted(rasch.glob("*.difficulties.csv")):
        tag = f.name.replace(".difficulties.csv", "")
        diff = pd.read_csv(f)
        abil = pd.read_csv(rasch / f"{tag}.abilities.csv")
        L.append(f"\n## {tag}")
        dist_block(diff)
        abil_block(abil, "Abilities")
        if tag.startswith("pooled"):
            scheme = "context" if tag == "pooled_context" else "perturbation"
            cov = pd.concat([pd.read_parquet(p) for p in run.glob(f"*.{scheme}.items.parquet")])
            cov = cov[~cov.index.duplicated()]
            # per-dataset difficulty means show the dataset factor
            d = diff.merge(cov, left_on="item_id", right_index=True)
            L.append("\n### Mean difficulty by dataset (dataset factor check)\n")
            L.append("| dataset | n items | mean difficulty | sd |\n|---|---|---|---|")
            for ds, g in d[~d["degenerate"]].groupby("dataset_id"):
                L.append(f"| {ds} | {len(g)} | {g['difficulty'].mean():.2f} | {g['difficulty'].std():.2f} |")
        else:
            ds, scheme = tag.rsplit(".", 1)
            p = run / f"{ds}.{scheme}.items.parquet"
            if p.exists():
                cov = pd.read_parquet(p)
                cov["log_n_cells"] = np.log10(cov["n_cells"])
                corr_block(diff, cov, ["delta_l2", "log_n_cells", "target_in_var", "dose"], "Difficulty vs covariates (prediction: difficulty falls with effect size)")
else:
    L.append(f"# Component A summary: {a.run}\n")
    rasch = run / "rasch"
    items = pd.read_parquet(run / "items.parquet")
    items["log_total_counts"] = np.log10(items["total_counts"].astype(float))
    items["log_n_train_same_type"] = np.log10(items["n_train_same_type"].astype(float))
    for tag in ["cell_level", "stratum_binomial"]:
        f = rasch / f"{tag}.difficulties.csv"
        if not f.exists():
            continue
        diff = pd.read_csv(f)
        abil = pd.read_csv(rasch / f"{tag}.abilities.csv")
        L.append(f"\n## {tag}")
        dist_block(diff)
        abil_block(abil, "Abilities")
        if tag == "cell_level":
            d = corr_block(diff, items, ["log_n_train_same_type", "log_total_counts", "n_genes_by_counts"], "Difficulty vs covariates (prediction: rare types and shallow cells are hard)")
            if "compartment" in d.columns:
                L.append("\n### Mean difficulty by compartment\n\n| compartment | n | mean | sd |\n|---|---|---|---|")
                for c, g in d.groupby("compartment", observed=True):
                    L.append(f"| {c} | {len(g)} | {g['difficulty'].mean():.2f} | {g['difficulty'].std():.2f} |")
            L.append("\n### Hardest 15 cell types (mean cell difficulty, >= 20 items)\n\n| cell type | n | mean difficulty | train cells |\n|---|---|---|---|")
            g = d.groupby("cell_type", observed=True).agg(n=("difficulty", "size"), mean=("difficulty", "mean"), tr=("n_train_same_type", "first"))
            for ct, r in g[g["n"] >= 20].sort_values("mean", ascending=False).head(15).iterrows():
                L.append(f"| {ct} | {r.n} | {r['mean']:.2f} | {int(r.tr)} |")
        else:
            strata = items.groupby("stratum", observed=True).agg(tissue=("tissue", "first"), cell_type=("cell_type", "first"), n_train_same_type=("n_train_same_type", "first"))
            strata["log_n_train_same_type"] = np.log10(strata["n_train_same_type"].astype(float))
            corr_block(diff, strata, ["log_n_train_same_type"], "Stratum difficulty vs train support")
            d = diff.merge(strata, left_on="item_id", right_index=True)
            L.append("\n### Hardest 15 strata\n\n| stratum | difficulty | se | p_correct |\n|---|---|---|---|")
            for r in d[~d["degenerate"]].sort_values("difficulty", ascending=False).head(15).itertuples():
                L.append(f"| {r.item_id} | {r.difficulty:.2f} | {r.se:.2f} | {r.p_correct:.2f} |")

(run / "summary.md").write_text("\n".join(L) + "\n")
print("\n".join(L))

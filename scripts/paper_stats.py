#!/usr/bin/env python
"""Numbers for the paper draft: composition tables, difficulty distributions, retirement
scenarios. Writes paper/bench/stats.json and prints markdown tables.

  python scripts/paper_stats.py
"""
import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd
import anndata as ad

from vcb import DATA, RUNS, ROOT

A_RUN = RUNS / "repr_pooled_v3"
# (run, display name, held-out unit, train cells override for runs whose panel is not on this machine)
PANELS = [
    ("repr_pool_v0", "Tabula Sapiens v2", "donors", None),
    ("repr_hao_pbmc_l2", "Hao 2021 PBMC", "donors", None),
    ("repr_heart_states", "Adult heart", "donors", None),
    ("repr_hlca_core_donor", "HLCA core", "donors", None),
    ("repr_hlca_core_study", "HLCA core", "studies", None),
    ("repr_immune_atlas_donor", "Cross-tissue immune atlas", "donors", None),
    ("repr_immune_atlas_tissue", "Cross-tissue immune atlas", "tissues", None),
    ("repr_parse_pbmc_celltype", "Parse 10M PBMC", "donors", None),
    ("repr_scbasecount_human200_lung", "scBaseCount, lung", "samples", 145543),
    ("repr_scbasecount_human200_skin", "scBaseCount, skin", "samples", 68112),
    ("repr_scbasecount_human200_bone_marrow", "scBaseCount, bone marrow", "samples", 104777),
    ("repr_scbasecount_human200_liver", "scBaseCount, liver", "samples", 51432),
    ("repr_scbasecount_human200_blood", "scBaseCount, blood", "samples", 129019),
    ("repr_scbasecount_human200_multitissue", "scBaseCount, 12 tissues", "tissues", 180127),
]
PANEL_FILE = {"repr_pool_v0": "ts2_panel_v0"}

out_dir = ROOT / "paper" / "bench"
out_dir.mkdir(parents=True, exist_ok=True)
res = {}

# ---------- component B composition ----------
rows = []
for f in sorted(glob.glob(str(DATA / "items" / "*.items.h5ad"))):
    ds = Path(f).name.replace(".items.h5ad", "")
    a = ad.read_h5ad(f, backed="r")
    o = a.obs
    tr = o[~o["is_control"].astype(bool)]
    ok = tr[(tr["n_cells"] >= 50) & tr["has_matched_control"].astype(bool)]
    rows.append(dict(dataset=ds, pert_type=tr["pert_type"].mode().iloc[0], contexts=int(o["context"].nunique()),
                     perturbations=int(tr["perturbation"].nunique()), conditions=len(tr), items=len(ok),
                     cells=int(o["n_cells"].sum()), genes=a.n_vars, median_cells_per_item=float(ok["n_cells"].median()),
                     doses=int(tr["dose"].nunique(dropna=True)) if tr["dose"].notna().any() else 0))
compB = pd.DataFrame(rows).sort_values("items", ascending=False)
res["compB"] = compB.to_dict(orient="records")
print("## Component B composition\n", compB.to_string(index=False))

# ---------- component A composition: one row per panel ----------
import h5py
from anndata.io import read_elem

def pool_only(df):
    """Respondents that define the scale. Models placed afterwards with difficulties held fixed
    (placement == 'anchored', the foundation models) are reported in their own tables, not in the
    scale's summaries or the retirement analysis."""
    return df[df["placement"] != "anchored"] if "placement" in df.columns else df

dA_pooled = pd.read_csv(A_RUN / "rasch" / "cell_level.difficulties.csv")
itemsA = pd.read_parquet(A_RUN / "items.parquet")
dA_pooled = dA_pooled.merge(itemsA[["source_run"]], left_on="item_id", right_index=True)
rowsA = []
for run, name, unit, tr_override in PANELS:
    it = pd.read_parquet(RUNS / run / "items.parquet")
    pf = DATA / "panels" / f"{PANEL_FILE.get(run, run.replace('repr_', ''))}.h5ad"
    tr = tr_override
    if pf.exists():
        with h5py.File(pf) as f:
            obs = read_elem(f["obs"])
        tr = int((obs["split"] == "train").sum())
    dd = dA_pooled[dA_pooled["source_run"] == run]
    ab = pool_only(pd.read_csv(RUNS / run / "rasch" / "cell_level.abilities.csv")).set_index("respondent_id")["ability"]
    rowsA.append(dict(run=run, name=name, held_out=unit, train_cells=tr, items=len(it), strata=int(it["stratum"].nunique()), types=int(it["cell_type"].nunique()),
                      test_units=int(it["donor"].nunique() if unit in ("donors", "samples") else it["tissue"].nunique()), contexts=int(it["tissue"].nunique()),
                      nobody=float((dd["p_correct"] == 0).mean()), mean_b=float(dd.loc[~dd["degenerate"], "difficulty"].mean()), top=ab.idxmax(), top_ability=float(ab.max()),
                      pca128=float(ab.get("pca_k128", np.nan)), scvi30=float(ab.get("scvi_k30_bnone", np.nan))))
compA = pd.DataFrame(rowsA)
res["compA_panels"] = compA.to_dict(orient="records")
res["compA"] = dict(panels=len(compA), train_cells=int(compA["train_cells"].sum()), test_items=int(compA["items"].sum()), strata=int(compA["strata"].sum()),
                    types=int(pd.concat([pd.read_parquet(RUNS / r / "items.parquet")["cell_type"] for r, *_ in PANELS]).nunique()), donor_panels=int((compA["held_out"].isin(["donors", "samples"])).sum()))
print("\n## Component A panels\n", compA.round(2).to_string(index=False), "\n", res["compA"])
def tex_int(x):
    return f"{int(x):,}"
def panel_table(fname, header, rowfn, totfn):
    lines = [rowfn(r) for r in compA.itertuples()] + ["\\midrule", totfn()]
    (out_dir / fname).write_text("\\begin{tabular}{@{}l" + "r" * (header.count("&")) + "@{}}\n\\toprule\n" + header + " \\\\\n\\midrule\n" + "\n".join(lines) + "\n\\bottomrule\n\\end{tabular}\n")
nobody_all = 100 * (dA_pooled["p_correct"] == 0).mean()
panel_table("tab_compA.tex", "Panel & Cell types & Train cells & Items & None pass & Mean diff.",
            lambda r: f"{r.name}{' (' + r.held_out + ' held out)' if r.held_out in ('studies', 'tissues') else ''} & {r.types} & {tex_int(r.train_cells)} & {tex_int(r.items)} & {100*r.nobody:.0f}\\% & {r.mean_b:+.2f} \\\\",
            lambda: f"Total & {res['compA']['types']} & {tex_int(res['compA']['train_cells'])} & {tex_int(res['compA']['test_items'])} & {nobody_all:.0f}\\% & \\\\")
panel_table("tab_compA_full.tex", "Panel & Held out & N held out & Contexts & Cell types & Train cells & Items & Strata",
            lambda r: f"{r.name} & {r.held_out} & {r.test_units} & {r.contexts} & {r.types} & {tex_int(r.train_cells)} & {tex_int(r.items)} & {r.strata} \\\\",
            lambda: f"Total & & & & {res['compA']['types']} & {tex_int(res['compA']['train_cells'])} & {tex_int(res['compA']['test_items'])} & {tex_int(res['compA']['strata'])} \\\\")
items = pd.read_parquet(RUNS / "repr_pool_v0" / "items.parquet")  # TS2 covariates (compartment) for the appendix

# ---------- difficulty distributions ----------
def dist(diff):
    d = diff[~diff["degenerate"]]
    q = np.percentile(d["difficulty"], [5, 25, 50, 75, 95])
    hist, edges = np.histogram(d["difficulty"], bins=np.arange(-6, 6.01, 0.5))
    return dict(n=len(diff), informative=len(d), nobody=int((diff["p_correct"] == 0).sum()), everybody=int((diff["p_correct"] == 1).sum()),
                q05=q[0], q25=q[1], q50=q[2], q75=q[3], q95=q[4], sd=float(d["difficulty"].std()), median_se=float(d["se"].median()),
                hist=hist.tolist(), edges=edges.tolist())

diffs = {}
diffs["A_cell"] = pd.read_csv(A_RUN / "rasch" / "cell_level.difficulties.csv")
diffs["A_stratum"] = pd.read_csv(A_RUN / "rasch" / "stratum_binomial.difficulties.csv")
diffs["A_ts2"] = pd.read_csv(RUNS / "repr_pool_v0" / "rasch" / "cell_level.difficulties.csv")
diffs["B_pooled"] = pd.read_csv(RUNS / "pert_pool_v0" / "rasch_paper" / "pooled.difficulties.csv")
res["dist"] = {k: dist(v) for k, v in diffs.items()}
for k, v in res["dist"].items():
    print(f"\n## {k}: n={v['n']} informative={v['informative']} nobody={v['nobody']} everybody={v['everybody']} q5/50/95={v['q05']:.2f}/{v['q50']:.2f}/{v['q95']:.2f} sd={v['sd']:.2f} medSE={v['median_se']:.2f}")

# per-dataset difficulty on the pooled B scale
cov = pd.concat([pd.read_parquet(p) for p in (RUNS / "pert_pool_v0").glob("*.perturbation.items.parquet")])
cov = cov[~cov.index.duplicated()]
dB = diffs["B_pooled"].merge(cov, left_on="item_id", right_index=True)
per_ds = dB.groupby("dataset_id").apply(lambda g: pd.Series(dict(items=len(g), informative=int((~g["degenerate"]).sum()), nobody=int((g["p_correct"] == 0).sum()),
                                                                   mean_b=g.loc[~g["degenerate"], "difficulty"].mean(), sd_b=g.loc[~g["degenerate"], "difficulty"].std())), include_groups=False)
res["per_dataset_B"] = per_ds.reset_index().to_dict(orient="records")
print("\n## per-dataset difficulty (pooled B scale)\n", per_ds.round(2).to_string())

# ---------- abilities ----------
abil = {}
abil["A_cell"] = pool_only(pd.read_csv(A_RUN / "rasch" / "cell_level.abilities.csv"))
abil["A_ts2"] = pool_only(pd.read_csv(RUNS / "repr_pool_v0" / "rasch" / "cell_level.abilities.csv"))
for run, *_ in PANELS:
    res[f"abil_panel_{run}"] = pd.read_csv(RUNS / run / "rasch" / "cell_level.abilities.csv").round(3).to_dict(orient="records")
abil["B_pooled"] = pd.read_csv(RUNS / "pert_pool_v0" / "rasch_paper" / "pooled.abilities.csv")
for k, v in abil.items():
    res[f"abil_{k}"] = v.round(3).to_dict(orient="records")
    print(f"\n## abilities {k}\n", v[["respondent_id", "ability", "se", "p_correct", "outfit"]].round(2).to_string(index=False))
sg = {}
for ds in ["FrangiehIzar2021_RNA", "McFarlandTsherniak2020", "SrivatsanTrapnell2020_sciplex3", "tahoe100m", "parse_pbmc_cytokines"]:
    f = RUNS / "pert_pool_v0" / "rasch_paper" / f"{ds}.context.abilities.csv"
    if f.exists():
        a_ = pd.read_csv(f); a_["rank"] = np.arange(1, len(a_) + 1)
        sg[ds] = a_[["respondent_id", "ability", "se", "p_correct", "outfit", "rank"]].round(2).to_dict(orient="records")
res["abil_context"] = sg

# ---------- covariates ----------
from scipy.stats import spearmanr
itA = itemsA.copy(); itA["log_n_train"] = np.log10(itA["n_train_same_type"].astype(float)); itA["log_counts"] = np.log10(itA["total_counts"].astype(float))
dA = diffs["A_cell"].merge(itA, left_on="item_id", right_index=True); dA = dA[~dA["degenerate"]]
dA["log_n_train"] = np.log10(dA["n_train_same_type"].astype(float).clip(lower=1))
res["corrA"] = {c: spearmanr(dA["difficulty"], dA[c])[0] for c in ["log_n_train", "log_counts"]}
res["corrA_by_panel"] = {r: {c: spearmanr(g["difficulty"], g[c])[0] for c in ["log_n_train", "log_counts"]} for r, g in dA.groupby("source_run")}
print("## corrA by panel", {k: {c: round(v, 2) for c, v in d.items()} for k, d in res["corrA_by_panel"].items()})
dBi = dB[~dB["degenerate"]].copy(); dBi["log_n_cells"] = np.log10(dBi["n_cells"])
res["corrB"] = {c: spearmanr(dBi["difficulty"], dBi[c])[0] for c in ["delta_l2", "log_n_cells"]}
res["corrB_by_dataset"] = {ds: spearmanr(g["difficulty"], g["delta_l2"])[0] for ds, g in dBi.groupby("dataset_id") if len(g) > 30}
print("\n## correlations A", res["corrA"], "\n## correlations B", res["corrB"], "\n", {k: round(v, 2) for k, v in res["corrB_by_dataset"].items()})

# ---------- retirement scenarios ----------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
scen = {}
for key, diff, ab in [("A_cell", diffs["A_cell"], abil["A_cell"]), ("A_stratum", diffs["A_stratum"], abil["A_cell"]), ("A_ts2", diffs["A_ts2"], abil["A_ts2"]), ("B_pooled", diffs["B_pooled"], abil["B_pooled"])]:
    d = diff[~diff["degenerate"]]
    theta_best = ab["ability"].max(); theta_mean = ab["ability"].mean()
    out = {"theta_best": theta_best, "theta_pool_mean": theta_mean, "n_informative": len(d), "n_all": len(diff), "everybody_now": int((diff["p_correct"] == 1).sum())}
    for delta in [0, 0.5, 1, 2, 3, 4]:
        th = theta_best + delta
        p = sigmoid(th - d["difficulty"].values)
        out[f"retire_p95_delta{delta}"] = int((p >= 0.95).sum())
        out[f"retire_p99_delta{delta}"] = int((p >= 0.99).sum())
        for t in (0.75, 0.80, 0.85, 0.90):
            out[f"retire_p{int(t*100)}_delta{delta}"] = int((p >= t).sum())
        info = p * (1 - p)
        out[f"info_frac_delta{delta}"] = float(info.sum() / (0.25 * len(d)))
        out[f"remaining_window_delta{delta}"] = int(((d["difficulty"].values > th - 2) & (d["difficulty"].values < th + 2)).sum())
    scen[key] = out
res["retire"] = scen
print("\n## retirement scenarios")
for k, v in scen.items():
    print(k, {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()})

# ---------- items already uninformative for the evaluated models (no hypothetical model) ----------
from vcb.names import family
now = {}
for key, diff, ab in [("A_cell", diffs["A_cell"], abil["A_cell"]), ("B_pooled", diffs["B_pooled"], abil["B_pooled"])]:
    th = ab.loc[ab["respondent_id"].map(family) != "Floor", "ability"].values
    b = diff["difficulty"].values
    P = sigmoid(th[None, :] - b[:, None])            # items x models
    pmin, pmax = P.min(1), P.max(1)
    deg_none, deg_all = (diff["p_correct"] == 0).values, (diff["p_correct"] == 1).values
    o = {"n_all": len(diff), "n_models": int(len(th)), "nobody": int(deg_none.sum()), "everybody": int(deg_all.sum())}
    for t in (0.75, 0.80, 0.85, 0.90, 0.95, 0.99):
        easy = (pmin >= t) | deg_all
        hard = (pmax <= 1 - t) | deg_none
        o[f"easy_{t}"] = float(easy.mean()); o[f"hard_{t}"] = float(hard.mean()); o[f"retired_{t}"] = float((easy | hard).mean())
    now[key] = o
res["retire_now"] = now
print("\n## uninformative now", {k: {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in now.items()})
json.dump(res, open(out_dir / "stats.json", "w"), indent=1, default=float)
print(f"\nwrote {out_dir / 'stats.json'}")

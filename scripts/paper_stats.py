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

# ---------- component A composition ----------
items = pd.read_parquet(RUNS / "repr_pool_v0" / "items.parquet")
pa = ad.read_h5ad(DATA / "panels" / "ts2_panel_v0.h5ad", backed="r")
po = pa.obs
compA = dict(train_cells=int((po["split"] == "train").sum()), test_cells=int((po["split"] == "test").sum()), test_items=len(items),
             types=int(po["cell_type"].nunique()), types_in_test=int(items["cell_type"].nunique()), tissues=int(po["tissue"].nunique()),
             donors=int(po["donor"].nunique()), test_donors=int(items["donor"].nunique()), strata=int(items["stratum"].nunique()),
             compartments=items["compartment"].value_counts().to_dict(), genes=pa.n_vars)
res["compA"] = compA
print("\n## Component A composition\n", json.dumps(compA, indent=1))

# ---------- difficulty distributions ----------
def dist(diff):
    d = diff[~diff["degenerate"]]
    q = np.percentile(d["difficulty"], [5, 25, 50, 75, 95])
    hist, edges = np.histogram(d["difficulty"], bins=np.arange(-6, 6.01, 0.5))
    return dict(n=len(diff), informative=len(d), nobody=int((diff["p_correct"] == 0).sum()), everybody=int((diff["p_correct"] == 1).sum()),
                q05=q[0], q25=q[1], q50=q[2], q75=q[3], q95=q[4], sd=float(d["difficulty"].std()), median_se=float(d["se"].median()),
                hist=hist.tolist(), edges=edges.tolist())

diffs = {}
diffs["A_cell"] = pd.read_csv(RUNS / "repr_pool_v0" / "rasch" / "cell_level.difficulties.csv")
diffs["A_stratum"] = pd.read_csv(RUNS / "repr_pool_v0" / "rasch" / "stratum_binomial.difficulties.csv")
diffs["B_pooled"] = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / "pooled.difficulties.csv")
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
abil["A_cell"] = pd.read_csv(RUNS / "repr_pool_v0" / "rasch" / "cell_level.abilities.csv")
abil["B_pooled"] = pd.read_csv(RUNS / "pert_pool_v0" / "rasch" / "pooled.abilities.csv")
for k, v in abil.items():
    res[f"abil_{k}"] = v.round(3).to_dict(orient="records")
    print(f"\n## abilities {k}\n", v[["respondent_id", "ability", "se", "p_correct", "outfit"]].round(2).to_string(index=False))
sg = {}
for ds in ["FrangiehIzar2021_RNA", "McFarlandTsherniak2020", "SrivatsanTrapnell2020_sciplex3", "tahoe100m"]:
    f = RUNS / "pert_pool_v0" / "rasch" / f"{ds}.context.abilities.csv"
    if f.exists():
        a_ = pd.read_csv(f); a_["rank"] = np.arange(1, len(a_) + 1)
        sg[ds] = a_[["respondent_id", "ability", "se", "p_correct", "outfit", "rank"]].round(2).to_dict(orient="records")
res["abil_context"] = sg

# ---------- covariates ----------
from scipy.stats import spearmanr
itA = items.copy(); itA["log_n_train"] = np.log10(itA["n_train_same_type"].astype(float)); itA["log_counts"] = np.log10(itA["total_counts"].astype(float))
dA = diffs["A_cell"].merge(itA, left_on="item_id", right_index=True); dA = dA[~dA["degenerate"]]
res["corrA"] = {c: spearmanr(dA["difficulty"], dA[c])[0] for c in ["log_n_train", "log_counts"]}
dBi = dB[~dB["degenerate"]].copy(); dBi["log_n_cells"] = np.log10(dBi["n_cells"])
res["corrB"] = {c: spearmanr(dBi["difficulty"], dBi[c])[0] for c in ["delta_l2", "log_n_cells"]}
res["corrB_by_dataset"] = {ds: spearmanr(g["difficulty"], g["delta_l2"])[0] for ds, g in dBi.groupby("dataset_id") if len(g) > 30}
print("\n## correlations A", res["corrA"], "\n## correlations B", res["corrB"], "\n", {k: round(v, 2) for k, v in res["corrB_by_dataset"].items()})

# ---------- retirement scenarios ----------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
scen = {}
for key, diff, ab in [("A_cell", diffs["A_cell"], abil["A_cell"]), ("A_stratum", diffs["A_stratum"], abil["A_cell"]), ("B_pooled", diffs["B_pooled"], abil["B_pooled"])]:
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

json.dump(res, open(out_dir / "stats.json", "w"), indent=1, default=float)
print(f"\nwrote {out_dir / 'stats.json'}")

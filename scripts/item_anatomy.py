#!/usr/bin/env python
"""Anatomy of difficulty: what the current pool cannot do, and why.

Component A (cells). For every test cell the frozen probe wrote its predicted label, so each hard
cell has a known confusion. Labels are mapped to Cell Ontology terms (by id where the panel has
one, else by exact name or synonym) and the ontology distance between the true and the predicted
label is measured. Per (panel, cell type): mean difficulty, share passed by nobody, the dominant
confusion and its distance, the distance to the nearest other label in the panel, and the depth of
the term. Also the share of difficulty variance explained by the cell type and by the stratum.

Component B (conditions). From the pseudobulk means and the control statistics stored with every
item bank: the number of genes outside the control noise band (did the cells react), the share of
the response that is the context's generic shift (cosine to the leave-one-out mean shift), the
on-target change for genetic screens (did the perturbation take), the target's control expression,
transcription-factor status (Lambert 2018), and dose. Items are binned into no reaction / generic
reaction / specific reaction and difficulty is summarised per bin.

  python scripts/item_anatomy.py          # writes runs/anatomy_v0/{anatomy.json, anatomy.md, ...}
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

import h5py
import networkx as nx
import numpy as np
import pandas as pd
from anndata.io import read_elem
from scipy import stats

from vcb import DATA, RUNS

OUT = RUNS / "anatomy_v0"
OUT.mkdir(parents=True, exist_ok=True)
A_RUN = RUNS / "repr_pooled_v3"
B_RUN = RUNS / "pert_pool_v0"
res: dict = {}


def spearman(x, y):
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 10 or len(np.unique(x[m])) < 3:
        return {"rho": None, "p": None, "n": int(m.sum())}
    r, p = stats.spearmanr(x[m], y[m])
    return {"rho": float(r), "p": float(p), "n": int(m.sum())}


# =====================================================================================
# Cell Ontology
# =====================================================================================
def parse_obo(path: Path):
    terms, cur = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line == "[Term]":
            cur = {"is_a": [], "syn": set(), "alt": [], "obsolete": False}
        elif line.startswith("[") or not line:
            if cur and "id" in cur:
                terms[cur["id"]] = cur
            cur = None if line.startswith("[") and line != "[Term]" else cur
            if not line:
                cur = None
        elif cur is not None:
            if line.startswith("id: "):
                cur["id"] = line[4:]
            elif line.startswith("name: "):
                cur["name"] = line[6:]
            elif line.startswith("is_a: "):
                cur["is_a"].append(line[6:].split(" ")[0])
            elif line.startswith("synonym: "):
                m = re.match(r'synonym: "(.*)" (EXACT|RELATED|BROAD|NARROW)', line)
                if m and m.group(2) in ("EXACT", "NARROW"):
                    cur["syn"].add(m.group(1))
            elif line.startswith("alt_id: "):
                cur["alt"].append(line[8:])
            elif line.startswith("is_obsolete: true"):
                cur["obsolete"] = True
    if cur and "id" in cur:
        terms[cur["id"]] = cur
    return {k: v for k, v in terms.items() if k.startswith("CL:") and not v["obsolete"]}


def norm_label(s: str) -> str:
    s = str(s).lower().strip()
    s = s.replace("-positive", "+").replace("positive", "+").replace("-negative", "-").replace("negative", "-")
    s = re.sub(r"[\s_]+", " ", s)
    return s


terms = parse_obo(DATA / "raw" / "ontology" / "cl-basic.obo")
G = nx.Graph()
for t, v in terms.items():
    for p in v["is_a"]:
        if p in terms:
            G.add_edge(t, p)
alt = {a: t for t, v in terms.items() for a in v["alt"]}
name_to_id = {}
for t, v in terms.items():
    for n in [v.get("name", "")] + sorted(v["syn"]):
        name_to_id.setdefault(norm_label(n), t)
ROOT = "CL:0000000"
depth = nx.single_source_shortest_path_length(G, ROOT) if ROOT in G else {}


def to_cl(label, cl_id=None):
    if isinstance(cl_id, str) and cl_id.startswith("CL:"):
        return alt.get(cl_id, cl_id) if (cl_id in terms or cl_id in alt) else None
    return name_to_id.get(norm_label(label))


_dist_cache = {}


def cl_dist(a, b):
    if a is None or b is None or a not in G or b not in G:
        return np.nan
    if a == b:
        return 0
    key = (a, b) if a < b else (b, a)
    if key not in _dist_cache:
        try:
            _dist_cache[key] = nx.shortest_path_length(G, a, b)
        except nx.NetworkXNoPath:
            _dist_cache[key] = np.nan
    return _dist_cache[key]


# =====================================================================================
# Component A: confusions
# =====================================================================================
items = pd.read_parquet(A_RUN / "items.parquet")
diff = pd.read_csv(A_RUN / "rasch" / "cell_level.difficulties.csv").set_index("item_id")
items = items.join(diff[["difficulty", "se", "p_correct", "degenerate"]], how="inner")
items["cl"] = [to_cl(l, c) for l, c in zip(items["cell_type"].astype(str), items["cell_ontology_id"].astype(object) if "cell_ontology_id" in items else [None] * len(items))]
items["depth"] = items["cl"].map(depth)
coverage = items.groupby("source_run", observed=True)["cl"].apply(lambda s: s.notna().mean())
res["A_ontology_coverage"] = coverage.round(3).to_dict()
print("ontology coverage by panel:\n", coverage.round(3).to_string(), flush=True)

# dominant wrong prediction per item, over all respondents
resp = pd.read_parquet(A_RUN / "responses.parquet", columns=["item_id", "k", "pred"])
wrong = resp[resp["k"] == 0]
conf = wrong.groupby("item_id", observed=True)["pred"].agg(lambda s: s.value_counts().index[0])
n_wrong = wrong.groupby("item_id", observed=True).size()
items["confusion"] = items.index.map(conf)
items["n_wrong"] = items.index.map(n_wrong).fillna(0)
items["confusion_cl"] = [to_cl(l) if isinstance(l, str) else None for l in items["confusion"]]
# confusion label -> ontology id within each panel: reuse the panel's own label->id map where available
lab2cl = items.dropna(subset=["cl"]).groupby(["source_run", "cell_type"], observed=True)["cl"].first().to_dict()
items["confusion_cl"] = [lab2cl.get((r, c), cc) for r, c, cc in zip(items["source_run"], items["confusion"], items["confusion_cl"])]
items["conf_dist"] = [cl_dist(a, b) for a, b in zip(items["cl"], items["confusion_cl"])]
del resp, wrong

# nearest other label in the same panel (ontology distance)
near = {}
for run, g in items.groupby("source_run", observed=True):
    labs = g.dropna(subset=["cl"]).groupby("cell_type", observed=True)["cl"].first()
    for lab, c in labs.items():
        d = [cl_dist(c, c2) for lab2, c2 in labs.items() if lab2 != lab]
        d = [x for x in d if np.isfinite(x)]
        near[(run, lab)] = min(d) if d else np.nan
items["nearest_label_dist"] = [near.get((r, l), np.nan) for r, l in zip(items["source_run"], items["cell_type"])]

inf = items[~items["degenerate"]]
res["A_corr"] = {
    "difficulty_vs_nearest_label_dist": spearman(inf["difficulty"].values, inf["nearest_label_dist"].values.astype(float)),
    "difficulty_vs_depth": spearman(inf["difficulty"].values, inf["depth"].values.astype(float)),
    "difficulty_vs_log_train_support": spearman(inf["difficulty"].values, np.log1p(inf["n_train_same_type"].values.astype(float))),
}
cd = items["conf_dist"].dropna()
res["A_confusion_distance_hist"] = cd.astype(int).value_counts().sort_index().to_dict()
res["A_confusion_within2"] = float((cd <= 2).mean()) if len(cd) else None
# by nobody-passes vs rest
nb = items[items["p_correct"] == 0]
res["A_nobody"] = {"n": int(len(nb)), "conf_dist_median": float(nb["conf_dist"].median()), "depth_median": float(nb["depth"].median()),
                   "rest_conf_dist_median": float(items[items["p_correct"] > 0]["conf_dist"].median()), "rest_depth_median": float(items[items["p_correct"] > 0]["depth"].median())}

# per (panel, cell type)
rows = []
for (run, lab), g in items.groupby(["source_run", "cell_type"], observed=True):
    gi = g[~g["degenerate"]]
    top = g["confusion"].value_counts()
    rows.append(dict(panel=run, cell_type=lab, cl=g["cl"].iloc[0], depth=g["depth"].iloc[0], n_items=len(g), mean_difficulty=float(gi["difficulty"].mean()) if len(gi) else np.nan,
                     nobody=float((g["p_correct"] == 0).mean()), pass_rate=float(g["p_correct"].mean()), train_support=int(g["n_train_same_type"].iloc[0]),
                     top_confusion=top.index[0] if len(top) else None, top_confusion_share=float(top.iloc[0] / top.sum()) if len(top) else np.nan,
                     top_confusion_dist=float(np.nanmedian(g.loc[g["confusion"] == (top.index[0] if len(top) else None), "conf_dist"])) if len(top) else np.nan,
                     nearest_label_dist=g["nearest_label_dist"].iloc[0]))
by_type = pd.DataFrame(rows).sort_values("mean_difficulty", ascending=False)
by_type.to_csv(OUT / "A_by_type.csv", index=False)
res["A_by_type"] = by_type.round(3).replace({np.nan: None}).to_dict(orient="records")

# decomposition: how much of cell difficulty is the type, how much the stratum
dec = {}
for run, g in inf.groupby("source_run", observed=True):
    v = g["difficulty"].var()
    r2_type = 1 - g["difficulty"].sub(g.groupby("cell_type", observed=True)["difficulty"].transform("mean")).var() / v
    r2_str = 1 - g["difficulty"].sub(g.groupby("stratum", observed=True)["difficulty"].transform("mean")).var() / v
    dec[run] = {"r2_type": float(r2_type), "r2_stratum": float(r2_str), "n": int(len(g))}
res["A_decomposition"] = dec

# =====================================================================================
# Component B: reaction decomposition
# =====================================================================================
tfs = set(l.strip() for l in open(DATA / "raw" / "knowledge" / "human_tfs_lambert2018.txt") if l.strip())
essential_targets = None
ess_items = DATA / "items" / "ReplogleWeissman2022_K562_essential.items.h5ad"
if ess_items.exists():
    with h5py.File(ess_items) as f:
        essential_targets = set(read_elem(f["obs"])["targets"].astype(str))

covB = []
for f in sorted(glob.glob(str(DATA / "items" / "*.items.h5ad"))):
    ds = Path(f).name.replace(".items.h5ad", "")
    with h5py.File(f) as h:
        obs = read_elem(h["obs"])
        var_names = pd.Index(read_elem(h["var"]).index.astype(str))
        X = h["X"]
        cs = {k: {"mean": h["uns"]["control_stats"][k]["mean"][()], "var": h["uns"]["control_stats"][k]["var"][()], "n": int(h["uns"]["control_stats"][k]["n"][()])} for k in h["uns"]["control_stats"].keys()}
        is_ctrl = obs["is_control"].values.astype(bool)
        keep = (~is_ctrl) & obs["has_matched_control"].values.astype(bool) & (obs["n_cells"].values >= 50)
        gidx = {g: i for i, g in enumerate(var_names)}
        for ctx in obs.loc[keep, "context"].astype(str).unique():
            if ctx not in cs:
                continue
            rows_idx = np.where(keep & (obs["context"].astype(str).values == ctx))[0]
            Xc = np.asarray(X[rows_idx]) if isinstance(X, h5py.Dataset) else np.asarray(read_elem(X)[rows_idx])
            mu, v, n_c = cs[ctx]["mean"], cs[ctx]["var"], cs[ctx]["n"]
            D = Xc - mu
            nc = obs["n_cells"].values[rows_idx].astype(float)
            se = np.sqrt(v[None, :] / nc[:, None] + v[None, :] / n_c + 1e-8)
            Z = D / se
            expressed = mu > 0.01
            n_resp = (np.abs(Z[:, expressed]) > 3).sum(1)
            S = D.sum(0)
            if len(rows_idx) > 1:
                ms_loo = (S[None, :] - D) / (len(rows_idx) - 1)
            else:
                ms_loo = np.zeros_like(D)
            cos = (D * ms_loo).sum(1) / (np.linalg.norm(D, axis=1) * np.linalg.norm(ms_loo, axis=1) + 1e-12)
            for r, i in enumerate(rows_idx):
                o = obs.iloc[i]
                tg = [g for g in str(o["targets"]).split("|") if g and g in gidx]
                on_lfc = float(np.mean([D[r, gidx[g]] for g in tg])) if tg else np.nan
                on_z = float(np.mean([Z[r, gidx[g]] for g in tg])) if tg else np.nan
                t_mu = float(np.mean([mu[gidx[g]] for g in tg])) if tg else np.nan
                covB.append(dict(item_id=obs.index[i], dataset_id=ds, pert_type=str(o["pert_type"]), context=ctx, dose=float(o["dose"]) if pd.notna(o["dose"]) else np.nan,
                                 n_cells=int(o["n_cells"]), delta_l2=float(o["delta_l2"]), n_resp_genes=int(n_resp[r]), frac_resp=float(n_resp[r] / max(expressed.sum(), 1)),
                                 cos_generic=float(cos[r]), on_target_lfc=on_lfc, on_target_z=on_z, target_ctrl_mean=t_mu, target_measured=bool(tg),
                                 is_tf=bool(set(str(o["targets"]).split("|")) & tfs), in_essential_screen=(bool(set(str(o["targets"]).split("|")) & essential_targets) if essential_targets else None)))
    print(f"[{ds}] {int(keep.sum())} items", flush=True)

cb = pd.DataFrame(covB).set_index("item_id")
genetic = cb["pert_type"].isin(["CRISPRi", "CRISPR_KO", "CRISPRa"])
no_kd = genetic & cb["target_measured"] & (cb["on_target_lfc"] > -0.1) & (cb["pert_type"] != "CRISPRa")
cb["bin"] = np.where((cb["n_resp_genes"] < 10) | no_kd, "no_reaction", np.where(cb["cos_generic"] >= 0.8, "generic", "specific"))
cb.to_parquet(OUT / "B_covariates.parquet")

bres = {}
for tag in ("pooled", "pooled_context"):
    fdf = B_RUN / "rasch" / f"{tag}.difficulties.csv"
    if not fdf.exists():
        continue
    d = pd.read_csv(fdf).set_index("item_id").join(cb, how="inner")
    di = d[~d["degenerate"]]
    out = {"n": int(len(d)), "corr": {c: spearman(di["difficulty"].values, di[c].values.astype(float)) for c in ["n_resp_genes", "cos_generic", "delta_l2", "on_target_lfc", "target_ctrl_mean", "n_cells", "dose"]}}
    out["corr_within_dataset"] = {}
    for ds, g in di.groupby("dataset_id"):
        out["corr_within_dataset"][ds] = {c: spearman(g["difficulty"].values, g[c].values.astype(float)) for c in ["n_resp_genes", "cos_generic", "delta_l2", "on_target_lfc"]}
    bins = d.groupby("bin").agg(n=("difficulty", "size"), mean_difficulty=("difficulty", lambda s: float(s[~d.loc[s.index, "degenerate"]].mean())), nobody=("p_correct", lambda s: float((s == 0).mean())), pass_rate=("p_correct", "mean"))
    out["bins"] = bins.round(3).to_dict(orient="index")
    out["bins_by_dataset"] = {ds: g.groupby("bin").agg(n=("difficulty", "size"), nobody=("p_correct", lambda s: float((s == 0).mean())), mean_difficulty=("difficulty", "mean")).round(3).to_dict(orient="index") for ds, g in d.groupby("dataset_id")}
    gi = di[genetic.reindex(di.index).fillna(False).values]
    if len(gi):
        out["tf"] = gi.groupby("is_tf")["difficulty"].agg(["size", "mean"]).round(3).to_dict(orient="index")
        mw = stats.mannwhitneyu(gi.loc[gi["is_tf"], "difficulty"], gi.loc[~gi["is_tf"], "difficulty"]) if gi["is_tf"].nunique() == 2 else None
        out["tf_p"] = float(mw.pvalue) if mw else None
        ge = gi[gi["in_essential_screen"].notna()]
        if len(ge):
            out["essential"] = ge.groupby("in_essential_screen")["difficulty"].agg(["size", "mean"]).round(3).to_dict(orient="index")
    bres[tag] = out
res["B"] = bres
res["B_bin_thresholds"] = {"no_reaction": "fewer than 10 genes with |z|>3, or a genetic target measured but not reduced (on-target log1p change > -0.1)", "generic": "cosine to the leave-one-out context mean shift >= 0.8", "specific": "otherwise"}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


(OUT / "anatomy.json").write_text(json.dumps(_clean(res), indent=1))

# ---------------- report ----------------
L = ["# Anatomy of difficulty (v0)", "", "## Component A: what the probe confuses", "",
     f"Ontology coverage of labels by panel: " + ", ".join(f"{k} {v:.2f}" for k, v in res["A_ontology_coverage"].items()), "",
     f"Share of wrong predictions within ontology distance 2 of the true label (sibling, parent or child): {res['A_confusion_within2']:.2f}" if res["A_confusion_within2"] is not None else "",
     "", "| covariate | Spearman rho | p | n |", "|---|---|---|---|"]
for k, v in res["A_corr"].items():
    L.append(f"| {k} | {v['rho'] if v['rho'] is None else round(v['rho'], 3)} | {v['p'] if v['p'] is None else f'{v['p']:.1e}'} | {v['n']} |")
L += ["", f"Items passed by nobody: n={res['A_nobody']['n']}, median confusion distance {res['A_nobody']['conf_dist_median']} (others {res['A_nobody']['rest_conf_dist_median']}), median depth {res['A_nobody']['depth_median']} (others {res['A_nobody']['rest_depth_median']})",
      "", "Variance of cell difficulty explained by cell type / stratum, per panel:", "", "| panel | R2 type | R2 stratum | n |", "|---|---|---|---|"]
for k, v in res["A_decomposition"].items():
    L.append(f"| {k} | {v['r2_type']:.2f} | {v['r2_stratum']:.2f} | {v['n']} |")
L += ["", "Hardest cell types (mean difficulty, pooled scale), with the dominant confusion:", "", "| panel | cell type | n | mean diff | nobody | top confusion | share | CL dist | nearest label dist |", "|---|---|---|---|---|---|---|---|---|"]
for r in by_type.head(30).itertuples():
    L.append(f"| {r.panel.replace('repr_', '')} | {r.cell_type} | {r.n_items} | {r.mean_difficulty:+.2f} | {r.nobody:.2f} | {r.top_confusion} | {r.top_confusion_share:.2f} | {r.top_confusion_dist} | {r.nearest_label_dist} |")
L += ["", "## Component B: weak perturbation, weak reaction, or generic reaction", "", f"Bins: {res['B_bin_thresholds']}", ""]
for tag, o in bres.items():
    L += [f"### {tag} scale (n={o['n']})", "", "| bin | n | mean difficulty | nobody | pass rate |", "|---|---|---|---|---|"]
    for b, v in o["bins"].items():
        L.append(f"| {b} | {v['n']} | {v['mean_difficulty']:+.2f} | {v['nobody']:.2f} | {v['pass_rate']:.3f} |")
    L += ["", "| covariate | Spearman rho | p | n |", "|---|---|---|---|"]
    for c, v in o["corr"].items():
        L.append(f"| {c} | {v['rho'] if v['rho'] is None else round(v['rho'], 3)} | {v['p'] if v['p'] is None else f'{v['p']:.1e}'} | {v['n']} |")
    if "tf" in o:
        L += ["", f"Transcription-factor targets vs others (genetic screens): {o['tf']}, Mann-Whitney p={o['tf_p']}"]
    if "essential" in o:
        L += [f"Target in the K562 essential screen vs not: {o['essential']}"]
    L.append("")
(OUT / "anatomy.md").write_text("\n".join(L) + "\n")
print("\n".join(L), flush=True)

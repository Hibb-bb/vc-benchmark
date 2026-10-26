#!/usr/bin/env python
"""Export the benchmark's Rasch results to the JSON files the website renders from.

  .venv/bin/python scripts/export_site_data.py            # writes site/data/*.json

Inputs: runs/repr_pooled_v3 (pooled representation scale), the 14 per-panel runs listed in
PANELS, runs/pert_pool_v0 (every screen's scores, items and Rasch fits), paper/bench/stats.json
and runs/link_parse_v0/link.json. Nothing under site/data/ is edited by hand.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from vcb import ROOT, RUNS
from vcb.names import family, plain_name
from vcb.scoring import binarize

SITE = ROOT / "site" / "data"
(SITE / "items").mkdir(parents=True, exist_ok=True)
A_RUN = RUNS / "repr_pooled_v3"
B_RUN = RUNS / "pert_pool_v0"
VERSION = "0.1"
EDGES = np.round(np.arange(-6, 6.001, 0.25), 2)

# (run, display name, held-out unit, source, licence)
PANELS = [
    ("repr_pool_v0", "Tabula Sapiens v2", "donors", "Tabula Sapiens v2 (28 tissues)", "CC BY 4.0"),
    ("repr_hao_pbmc_l2", "Hao 2021 PBMC", "donors", "CELLxGENE, Hao et al. 2021 PBMC reference", "CC BY 4.0"),
    ("repr_heart_states", "Adult heart", "donors", "CELLxGENE, Litviňuková et al. 2020", "CC BY 4.0"),
    ("repr_hlca_core_donor", "HLCA core", "donors", "CELLxGENE, Human Lung Cell Atlas core", "CC BY 4.0"),
    ("repr_hlca_core_study", "HLCA core", "studies", "CELLxGENE, Human Lung Cell Atlas core", "CC BY 4.0"),
    ("repr_immune_atlas_donor", "Cross-tissue immune atlas", "donors", "CELLxGENE, Domínguez Conde et al. 2022", "CC BY 4.0"),
    ("repr_immune_atlas_tissue", "Cross-tissue immune atlas", "tissues", "CELLxGENE, Domínguez Conde et al. 2022", "CC BY 4.0"),
    ("repr_parse_pbmc_celltype", "Parse 10M PBMC", "donors", "Parse Biosciences 10M PBMC cytokine atlas", "CC BY 4.0"),
    ("repr_scbasecount_human200_lung", "scBaseCount, lung", "samples", "scBaseCount (Arc Institute), human lung, 195 samples", "CC BY 4.0"),
    ("repr_scbasecount_human200_skin", "scBaseCount, skin", "samples", "scBaseCount (Arc Institute), human skin, 97 samples", "CC BY 4.0"),
    ("repr_scbasecount_human200_bone_marrow", "scBaseCount, bone marrow", "samples", "scBaseCount (Arc Institute), human bone marrow, 171 samples", "CC BY 4.0"),
    ("repr_scbasecount_human200_liver", "scBaseCount, liver", "samples", "scBaseCount (Arc Institute), human liver, 78 samples", "CC BY 4.0"),
    ("repr_scbasecount_human200_blood", "scBaseCount, blood", "samples", "scBaseCount (Arc Institute), human blood, 200 samples", "CC BY 4.0"),
    ("repr_scbasecount_human200_multitissue", "scBaseCount, 12 tissues", "tissues", "scBaseCount (Arc Institute), 12 human tissues, 355 samples", "CC BY 4.0"),
]
SCREENS = {  # dataset_id -> (display name, source, licence)
    "tahoe100m": ("Tahoe-100M", "Tahoe-100M drug atlas (Vevo), 50 cell lines x 379 drugs x 3 doses", "CC BY 4.0"),
    "parse_pbmc_cytokines": ("Parse PBMC cytokines", "Parse Biosciences 10M PBMC, 90 cytokines x donor x cell type", "CC BY 4.0"),
    "ReplogleWeissman2022_K562_gwps": ("Replogle K562 genome-wide", "scPerturb, Replogle et al. 2022 (CRISPRi, K562)", "CC BY 4.0"),
    "ReplogleWeissman2022_K562_essential": ("Replogle K562 essential", "scPerturb, Replogle et al. 2022 (CRISPRi, K562)", "CC BY 4.0"),
    "ReplogleWeissman2022_rpe1": ("Replogle RPE1", "scPerturb, Replogle et al. 2022 (CRISPRi, RPE1)", "CC BY 4.0"),
    "NadigOConner2024_jurkat": ("Nadig Jurkat", "scPerturb, Nadig et al. 2024 (CRISPRi, Jurkat)", "CC BY 4.0"),
    "NadigOConner2024_hepg2": ("Nadig HepG2", "scPerturb, Nadig et al. 2024 (CRISPRi, HepG2)", "CC BY 4.0"),
    "SrivatsanTrapnell2020_sciplex3": ("sciPlex3", "scPerturb, Srivatsan et al. 2020 (188 drugs, 3 lines, 4 doses)", "CC BY 4.0"),
    "McFarlandTsherniak2020": ("McFarland", "scPerturb, McFarland et al. 2020 (drugs, 196 lines)", "CC BY 4.0"),
    "FrangiehIzar2021_RNA": ("Frangieh", "scPerturb, Frangieh et al. 2021 (CRISPR KO, 3 culture conditions)", "CC BY 4.0"),
    "NormanWeissman2019_filtered": ("Norman", "scPerturb, Norman et al. 2019 (CRISPRa singles and doubles)", "CC BY 4.0"),
    "TianKampmann2021_CRISPRi": ("Tian 2021 neurons", "scPerturb, Tian et al. 2021 (CRISPRi, iPSC-derived neurons)", "CC BY 4.0"),
    "AdamsonWeissman2016_GSM2406681_10X010": ("Adamson", "scPerturb, Adamson et al. 2016 (CRISPRi, K562)", "CC BY 4.0"),
    "TianKampmann2019_iPSC": ("Tian 2019 iPSC", "scPerturb, Tian et al. 2019 (CRISPRi, iPSC)", "CC BY 4.0"),
    "TianKampmann2019_day7neuron": ("Tian 2019 neurons", "scPerturb, Tian et al. 2019 (CRISPRi, day-7 neurons)", "CC BY 4.0"),
}
SCHEME_LABEL = {"perturbation": "unseen perturbation", "context": "unseen combination"}


def r3(x):
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), 3)


def hist(diff: pd.DataFrame) -> list[int]:
    d = diff.loc[~diff["degenerate"], "difficulty"].values
    return np.histogram(np.clip(d, -5.999, 5.999), bins=EDGES)[0].tolist()


def quantiles(diff: pd.DataFrame) -> list[float] | None:
    d = diff.loc[~diff["degenerate"], "difficulty"].values
    return [r3(q) for q in np.percentile(d, [5, 25, 50, 75, 95])] if len(d) else None


def scale_block(abil: pd.DataFrame, diff: pd.DataFrame, **extra) -> dict:
    inf = diff[~diff["degenerate"]]
    return dict(items=int(len(diff)), informative=int(len(inf)), nobody=int((diff["p_correct"] == 0).sum()), everybody=int((diff["p_correct"] == 1).sum()),
                median_se=r3(inf["se"].median()) if len(inf) else None, quantiles=quantiles(diff), hist=hist(diff),
                abilities=[dict(rid=r.respondent_id, ability=r3(r.ability), se=r3(r.se), p=r3(r.p_correct), outfit=r3(r.outfit), n_items=int(r.n_items), placement=getattr(r, "placement", "refit")) for r in abil.itertuples()], **extra)


def read_fit(folder: Path, tag: str):
    return pd.read_csv(folder / f"{tag}.abilities.csv"), pd.read_csv(folder / f"{tag}.difficulties.csv")


stats = json.load(open(ROOT / "paper" / "bench" / "stats.json"))
out = {"meta": {"name": "Virtual Cell Bench", "version": VERSION, "generated": pd.Timestamp.today().strftime("%Y-%m-%d"), "repr_scale": A_RUN.name, "pert_run": B_RUN.name}}
# Shown by default on the site boards: one or two settings per simple family plus every learned model, so that
# readers focus on the foundation models. Every respondent still defines the scale; "show all" reveals the rest.
FEATURED = {"pca_k32", "pca_k128", "nystroem_k256_g0.5", "ica_k64", "nmf_k64", "gmm_k100", "rproj_k128_s0", "depth2", "random_k32_s0",
            "scvi_k30_bnone", "scvi_k30_btissue",
            "knn_k5", "knn_k20", "pcareg_k50", "pcareg_k200", "ridge_d50_lam1", "gp_d50_ls0.5", "lowrank_r10", "mlp_h256_d50", "mlp_h1024_d50",
            "scvi_cf", "scgen", "target_kd", "random_shift_s0", "control_mean"}


def is_featured(rid: str) -> bool:
    return rid in FEATURED or rid.startswith("fm_")


respondents: dict[str, dict] = {}


def reg(rid: str, comp: str):
    r = respondents.setdefault(rid, {"name": plain_name(rid), "family": family(rid), "components": [], "featured": is_featured(rid)})
    if comp not in r["components"]:
        r["components"].append(comp)


# ---------------- component A ----------------
abA, dA = read_fit(A_RUN / "rasch", "cell_level")
itemsA = pd.read_parquet(A_RUN / "items.parquet")
dA = dA.merge(itemsA[["source_run", "cell_type", "compartment", "n_train_same_type", "total_counts", "n_genes_by_counts", "tissue", "donor"]], left_on="item_id", right_index=True, how="left")
for rid in abA["respondent_id"]:
    reg(rid, "repr")
panel_meta = {run: dict(name=name, held_out=unit, source=src, licence=lic) for run, name, unit, src, lic in PANELS}
panel_stats = {p["run"]: p for p in stats["compA_panels"]}
repr_scales = {"pooled": scale_block(abA, dA, label="Pooled scale, 14 panels", run=A_RUN.name)}
panels = []
for run, name, unit, src, lic in PANELS:
    ab_p, d_p = read_fit(RUNS / run / "rasch", "cell_level")
    for rid in ab_p["respondent_id"]:
        reg(rid, "repr")
    dd = dA[dA["source_run"] == run]
    ps = panel_stats[run]
    label = name + (f" ({unit} held out)" if unit in ("studies", "tissues") else "")
    repr_scales[run] = scale_block(ab_p, d_p, label=label, run=run)
    top = ab_p.iloc[0]
    panels.append(dict(run=run, name=name, label=label, held_out=unit, source=src, licence=lic, train_cells=int(ps["train_cells"]), items=int(ps["items"]), strata=int(ps["strata"]),
                       types=int(ps["types"]), test_units=int(ps["test_units"]), contexts=int(ps["contexts"]), nobody=r3(ps["nobody"]), mean_difficulty=r3(ps["mean_b"]),
                       quantiles=quantiles(dd), hist=hist(dd), top=dict(rid=top.respondent_id, ability=r3(top.ability)),
                       pca128=r3(ab_p.set_index("respondent_id")["ability"].get("pca_k128")), scvi30=r3(ab_p.set_index("respondent_id")["ability"].get("scvi_k30_bnone"))))

# cell-type aggregates for the item browser
inf = dA[~dA["degenerate"]].copy()
g = dA.groupby(["source_run", "cell_type"], observed=True)
gi = inf.groupby(["source_run", "cell_type"], observed=True)
agg = pd.DataFrame({"n": g.size(), "nobody": g["p_correct"].apply(lambda s: float((s == 0).mean())), "pass": g["p_correct"].mean(),
                    "difficulty": gi["difficulty"].mean(), "se": gi["difficulty"].std() / np.sqrt(gi.size()), "support": g["n_train_same_type"].median(),
                    "compartment": g["compartment"].agg(lambda s: s.mode().iloc[0] if s.notna().any() else None)}).reset_index()
agg = agg[agg["n"] >= 5]
items_repr = [dict(panel=r.source_run, type=r.cell_type, n=int(r.n), difficulty=r3(r.difficulty), se=r3(r.se), nobody=r3(r.nobody), pass_rate=r3(r["pass"]), support=int(r.support) if pd.notna(r.support) else None, compartment=None if pd.isna(r.compartment) else str(r.compartment)) for _, r in agg.iterrows()]

# covariates
inf["log_support"] = np.log10(inf["n_train_same_type"].astype(float).clip(lower=1))
inf["log_counts"] = np.log10(inf["total_counts"].astype(float))
inf["log_genes"] = np.log10(inf["n_genes_by_counts"].astype(float))
covA = {"pooled": {c: r3(spearmanr(inf["difficulty"], inf[c])[0]) for c in ["log_support", "log_counts", "log_genes"]}, "by_panel": {}}
for run, gg in inf.groupby("source_run"):
    covA["by_panel"][run] = {c: r3(spearmanr(gg["difficulty"], gg[c])[0]) for c in ["log_support", "log_counts", "log_genes"]}
comp = inf.dropna(subset=["compartment"]).groupby("compartment", observed=True)["difficulty"].agg(["size", "mean", "std"])
covA["by_compartment"] = [dict(compartment=str(k), n=int(v["size"]), mean=r3(v["mean"]), sd=r3(v["std"])) for k, v in comp.iterrows() if v["size"] >= 20]
# binned relation (median difficulty per decile of the covariate) for the plots
def binned(df, col, q=10):
    d = df.dropna(subset=[col])
    d = d[np.isfinite(d[col])]
    bins = pd.qcut(d[col], q, duplicates="drop")
    gb = d.groupby(bins, observed=True)["difficulty"]
    return [dict(x=r3(iv.mid), q25=r3(v.quantile(0.25)), q50=r3(v.median()), q75=r3(v.quantile(0.75)), n=int(len(v))) for iv, v in gb]
covA["curves"] = {c: binned(inf, c) for c in ["log_support", "log_counts"]}
hard = agg[agg["n"] >= 20].sort_values("difficulty", ascending=False).head(25)
covA["hardest_types"] = [dict(panel=r.source_run, type=r.cell_type, n=int(r.n), difficulty=r3(r.difficulty), support=int(r.support)) for _, r in hard.iterrows()]

# ---------------- component B ----------------
def load_items_b(ds, scheme):
    it = pd.read_parquet(B_RUN / f"{ds}.{scheme}.items.parquet")
    return it


pert_scales = {}
screens_rows = {s["dataset"]: s for s in stats["compB"]}
ANAT = RUNS / "anatomy_v0"
anat_cov = pd.read_parquet(ANAT / "B_covariates.parquet")[["n_resp_genes", "cos_generic", "bin"]] if (ANAT / "B_covariates.parquet").exists() else None
abB, dB = read_fit(B_RUN / "rasch", "pooled")
abBc, dBc = read_fit(B_RUN / "rasch", "pooled_context")
for rid in list(abB["respondent_id"]) + list(abBc["respondent_id"]):
    reg(rid, "pert")
pert_scales["pooled"] = scale_block(abB, dB, label="Pooled scale, unseen perturbation, 15 screens", scheme="perturbation")
pert_scales["pooled_context"] = scale_block(abBc, dBc, label="Pooled scale, unseen combination, 5 multi-context screens", scheme="context")
covB_items = []
screens = []
screen_fits = {}
for f in sorted(B_RUN.glob("*.scores.parquet")):
    ds, scheme = f.name.replace(".scores.parquet", "").rsplit(".", 1)
    tag = f"{ds}.{scheme}"
    ab_s, d_s = read_fit(B_RUN / "rasch", tag)
    for rid in ab_s["respondent_id"]:
        reg(rid, "pert")
    name = SCREENS.get(ds, (ds,))[0]
    pert_scales[tag] = scale_block(ab_s, d_s, label=f"{name}, {SCHEME_LABEL[scheme]}", dataset=ds, scheme=scheme)
    screen_fits[tag] = (ab_s, d_s)
for ds, (name, src, lic) in SCREENS.items():
    row = screens_rows.get(ds)
    if row is None:
        continue
    it = load_items_b(ds, "perturbation")
    dd = dB[dB["item_id"].isin(it.index)]
    ab_s, _ = screen_fits[f"{ds}.perturbation"]
    sc = dict(dataset=ds, name=name, source=src, licence=lic, pert_type=row["pert_type"], contexts=int(row["contexts"]), perturbations=int(row["perturbations"]), conditions=int(row["conditions"]),
              items=int(row["items"]), cells=int(row["cells"]), genes=int(row["genes"]), median_cells=r3(row["median_cells_per_item"]), doses=int(row["doses"]),
              schemes=["perturbation"] + (["context"] if (B_RUN / f"{ds}.context.items.parquet").exists() else []),
              nobody=r3((dd["p_correct"] == 0).mean()), mean_difficulty=r3(dd.loc[~dd["degenerate"], "difficulty"].mean()), quantiles=quantiles(dd), hist=hist(dd),
              top=dict(rid=ab_s.iloc[0].respondent_id, ability=r3(ab_s.iloc[0].ability)))
    if "context" in sc["schemes"]:
        itc = load_items_b(ds, "context")
        ddc = dBc[dBc["item_id"].isin(itc.index)]
        ab_c, _ = screen_fits[f"{ds}.context"]
        sc["context"] = dict(nobody=r3((ddc["p_correct"] == 0).mean()), mean_difficulty=r3(ddc.loc[~ddc["degenerate"], "difficulty"].mean()), quantiles=quantiles(ddc), hist=hist(ddc), top=dict(rid=ab_c.iloc[0].respondent_id, ability=r3(ab_c.iloc[0].ability)))
    screens.append(sc)
    # per-condition items file: pooled-scale difficulties (pooled for the perturbation scheme, pooled_context for the context scheme)
    files = {}
    for scheme, dpool in (("perturbation", dB), ("context", dBc)):
        if scheme not in sc["schemes"]:
            continue
        it = load_items_b(ds, scheme)
        d = dpool.set_index("item_id").join(it[["perturbation", "context", "dose", "n_cells", "delta_l2"]], how="inner")
        if anat_cov is not None:
            d = d.join(anat_cov, how="left")
        else:
            d["n_resp_genes"], d["cos_generic"], d["bin"] = None, None, None
        files[scheme] = [[str(r.perturbation), str(r.context), None if pd.isna(r.dose) else r3(r.dose), int(r.n_cells), r3(r.delta_l2), r3(r.difficulty), r3(r.se), r3(r.p_correct),
                          None if pd.isna(r.n_resp_genes) else int(r.n_resp_genes), r3(r.cos_generic), None if pd.isna(r.bin) else str(r.bin)] for r in d.itertuples()]
        if scheme == "perturbation":
            covB_items.append(d.assign(dataset_id=ds))
    json.dump({"dataset": ds, "name": name, "columns": ["perturbation", "context", "dose", "n_cells", "delta_l2", "difficulty", "se", "p_correct", "n_resp_genes", "cos_generic", "bin"], "schemes": files}, open(SITE / "items" / f"{ds}.json", "w"), separators=(",", ":"))

cb = pd.concat(covB_items)
cb = cb[~cb["degenerate"]].copy()
cb["log_n_cells"] = np.log10(cb["n_cells"].astype(float))
cb["log_effect"] = np.log10(cb["delta_l2"].astype(float).clip(lower=1e-3))
covB = {"pooled": {c: r3(spearmanr(cb["difficulty"], cb[c])[0]) for c in ["log_effect", "log_n_cells"]}, "by_screen": {}}
for ds, gg in cb.groupby("dataset_id"):
    if len(gg) > 30:
        covB["by_screen"][ds] = {c: r3(spearmanr(gg["difficulty"], gg[c])[0]) for c in ["log_effect", "log_n_cells"]}
covB["curves"] = {c: binned(cb, c) for c in ["log_effect", "log_n_cells"]}

# ---------------- retire / coverage curves ----------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def coverage(diff, abil):
    th = abil.loc[abil["respondent_id"].map(family) != "Floor", "ability"].values
    b = diff["difficulty"].values
    P = sigmoid(th[None, :] - b[:, None])
    pmin, pmax = P.min(1), P.max(1)
    none, all_ = (diff["p_correct"] == 0).values, (diff["p_correct"] == 1).values
    ts = [0.75, 0.8, 0.85, 0.9, 0.95, 0.99]
    rows = []
    for t in ts:
        easy = (pmin >= t) | all_
        hard = (pmax <= 1 - t) | none
        rows.append(dict(t=t, easy=r3(easy.mean()), hard=r3(hard.mean()), uninformative=r3((easy | hard).mean())))
    # test information along the ability axis (sum of p(1-p) over informative items)
    grid = np.arange(-6, 6.01, 0.25)
    inf_items = diff.loc[~diff["degenerate"], "difficulty"].values
    pg = sigmoid(grid[:, None] - inf_items[None, :])
    info = (pg * (1 - pg)).sum(1)
    return dict(n_models=int(len(th)), theta_best=r3(th.max()), theta_mean=r3(th.mean()), curve=rows, information=dict(grid=[r3(x) for x in grid], info=[r3(x) for x in info]))


retire = {"repr": coverage(dA, abA), "pert": coverage(dB, abB), "pert_context": coverage(dBc, abBc)}

# ---------------- pairwise agreement and adaptive samples ----------------
rng = np.random.default_rng(0)


def pass_matrix_repr():
    r = pd.read_parquet(A_RUN / "responses.parquet", columns=["item_id", "respondent_id", "k"])
    r["item_id"] = r["item_id"].astype("category")
    r["respondent_id"] = r["respondent_id"].astype("category")
    rids = list(r["respondent_id"].cat.categories)
    items = r["item_id"].cat.categories
    M = np.zeros((len(items), len(rids)), dtype=np.int8)
    M[r["item_id"].cat.codes.values, r["respondent_id"].cat.codes.values] = r["k"].values.astype(np.int8)
    return pd.Index(items), rids, M


def pairwise(M, O=None):
    """[both, only i, only j, neither] over items observed for both."""
    M = M.astype(np.int32)
    O = np.ones_like(M) if O is None else O.astype(np.int32)
    both = M.T @ M
    oi = M.T @ ((1 - M) * O)
    oj = ((1 - M) * O).T @ M
    nei = ((1 - M) * O).T @ ((1 - M) * O)
    return np.stack([both, oi, oj, nei], -1).tolist()


def sample_items(diff_df: pd.DataFrame, idx_of: pd.Index, M: np.ndarray, n=2000, O=None):
    d = diff_df[~diff_df["degenerate"]]
    d = d[d["item_id"].isin(idx_of)]
    # stratified by difficulty bins so the sample covers the scale
    bins = pd.cut(d["difficulty"], np.arange(-6, 6.01, 0.5))
    per = max(1, n // bins.nunique())
    take = d.groupby(bins, observed=True, group_keys=False).apply(lambda g: g.sample(min(len(g), per), random_state=0))
    if len(take) < n:
        rest = d.drop(take.index)
        take = pd.concat([take, rest.sample(min(len(rest), n - len(take)), random_state=1)])
    pos = idx_of.get_indexer(take["item_id"])
    rows = []
    for p, b in zip(pos, take["difficulty"].values):
        mask = int("".join("1" if v else "0" for v in M[p][::-1]), 2)
        obs = int("".join("1" if v else "0" for v in (O[p] if O is not None else np.ones(M.shape[1]))[::-1]), 2)
        rows.append([r3(b), mask, obs])
    return rows


itemsA_idx, ridsA, MA = pass_matrix_repr()
pair_repr = {"rids": ridsA, "groups": []}
src = itemsA.loc[itemsA_idx, "source_run"].values
for run, *_ in PANELS:
    sel = src == run
    pair_repr["groups"].append(dict(id=run, label=panel_meta[run]["name"] + (f" ({panel_meta[run]['held_out']} held out)" if panel_meta[run]["held_out"] in ("studies", "tissues") else ""), n=int(sel.sum()), counts=pairwise(MA[sel])))
adaptive = {"repr": dict(rids=ridsA, items=sample_items(dA, itemsA_idx, MA)), "pert": {}}

# perturbation: binarized responses per screen (perturbation scheme) and per multi-context screen (context scheme)
def pass_matrix_pert(scheme, rid_order):
    frames = []
    for f in sorted(B_RUN.glob(f"*.{scheme}.scores.parquet")):
        long = pd.read_parquet(f)
        b = binarize(long)
        frames.append(b[["dataset_id", "item_id", "respondent_id", "k"]])
    b = pd.concat(frames, ignore_index=True)
    b = b[b["respondent_id"].isin(rid_order)]
    piv = b.pivot_table(index="item_id", columns="respondent_id", values="k", aggfunc="first")
    piv = piv.reindex(columns=rid_order)
    O = piv.notna().values.astype(np.int8)
    M = piv.fillna(0).values.astype(np.int8)
    ds_of = b.drop_duplicates("item_id").set_index("item_id")["dataset_id"].reindex(piv.index).values
    return piv.index, M, O, ds_of


pair_pert = {}
for scheme, ab_, d_, key in (("perturbation", abB, dB, "pooled"), ("context", abBc, dBc, "pooled_context")):
    rid_order = list(ab_["respondent_id"])
    idx, M, O, ds_of = pass_matrix_pert(scheme, rid_order)
    groups = []
    for ds in SCREENS:
        sel = ds_of == ds
        if sel.sum() == 0:
            continue
        groups.append(dict(id=ds, label=SCREENS[ds][0], n=int(sel.sum()), counts=pairwise(M[sel], O[sel])))
    pair_pert[key] = {"rids": rid_order, "groups": groups}
    adaptive["pert"][key] = dict(rids=rid_order, items=sample_items(d_, idx, M, O=O))

# ---------------- totals ----------------
totals = dict(repr_items=int(len(dA)), repr_panels=len(PANELS), repr_train_cells=int(stats["compA"]["train_cells"]), repr_types=int(stats["compA"]["types"]), repr_strata=int(stats["compA"]["strata"]),
              pert_items=int(sum(s["items"] for s in screens)), pert_screens=len(screens), pert_cells=int(sum(s["cells"] for s in screens)), pert_perturbations=int(sum(s["perturbations"] for s in screens)),
              pert_context_items=int(len(dBc)), respondents_repr=int(len(abA)), respondents_pert=int(len(set(abB["respondent_id"]) | set(abBc["respondent_id"]))),
              sources=7 + 3, informative_repr=int((~dA["degenerate"]).sum()), informative_pert=int((~dB["degenerate"]).sum()))

out.update(totals=totals, respondents=respondents, panels=panels, screens=screens, scales={"repr": repr_scales, "pert": pert_scales}, edges=[float(e) for e in EDGES],
           covariates={"repr": covA, "pert": covB}, retire=retire, pairwise={"repr": pair_repr, "pert": pair_pert}, scheme_label=SCHEME_LABEL)
json.dump(out, open(SITE / "bench.json", "w"), separators=(",", ":"), default=float)
json.dump(items_repr, open(SITE / "items_repr.json", "w"), separators=(",", ":"))
json.dump(adaptive, open(SITE / "adaptive.json", "w"), separators=(",", ":"))
link = RUNS / "link_parse_v0" / "link.json"
if link.exists():  # the link script writes NaN for undefined SEs; that is not JSON, so null them here
    json.dump(json.loads(link.read_text(), parse_constant=lambda c: None), open(SITE / "link.json", "w"), separators=(",", ":"))
bt = RUNS / "link_parse_v0" / "by_type.json"
if bt.exists():
    json.dump(json.loads(bt.read_text(), parse_constant=lambda c: None), open(SITE / "link_by_type.json", "w"), separators=(",", ":"))
if (ANAT / "anatomy.json").exists():
    json.dump(json.loads((ANAT / "anatomy.json").read_text(), parse_constant=lambda c: None), open(SITE / "anatomy.json", "w"), separators=(",", ":"))
    t = pd.read_csv(ANAT / "A_by_type.csv")
    cols = ["panel", "cell_type", "n_items", "mean_difficulty", "nobody", "top_confusion", "top_confusion_share", "top_confusion_dist", "nearest_label_dist", "depth"]
    t = t[cols].round(3)
    json.dump({"columns": cols, "rows": [[None if pd.isna(v) else (v.item() if hasattr(v, "item") else v) for v in row] for row in t.itertuples(index=False)]}, open(SITE / "anatomy_types.json", "w"), separators=(",", ":"))
for p in sorted(SITE.rglob("*.json")):
    print(f"{p.relative_to(ROOT)}  {p.stat().st_size/1e6:.2f} MB")

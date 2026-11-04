#!/usr/bin/env python
"""Pictures of the text-card perturbation embeddings and of how they line up with measured responses.

  .venv-text/bin/python scripts/pert_text/plot_embeddings.py [--model Qwen3-Embedding-4B]

Writes runs/pert_text/figures/:
- umap_global.png: one UMAP of every card (10,715 perturbations), coloured by perturbation type, then the same
  map with genes coloured by a coarse GO process, Tahoe drugs by mechanism of action and cytokines by family.
- umap_by_type.png: separate UMAPs of the gene cards (one per target gene), the drug cards and the cytokine cards.
- alignment.png: per screen, the perturbations' text UMAP and response UMAP side by side, both coloured by
  clusters of the measured response (k-means on the response profiles); then pairwise text similarity against
  response correlation. Only the stronger half of responses (by norm) is used: a weak response's profile is
  mostly noise and has no cluster to belong to.
- alignment.csv: per screen, the share of each perturbation's 10 nearest text neighbours that fall in its response
  cluster (against the chance rate), and the Spearman correlation of text similarity with response correlation.
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "runs" / "pert_text"
FIG = T / "figures"
FIG.mkdir(parents=True, exist_ok=True)
ap = argparse.ArgumentParser()
ap.add_argument("--model", default="Qwen3-Embedding-4B")
a = ap.parse_args()

keys = (T / "emb" / "keys.txt").read_text().splitlines()
E = np.load(T / "emb" / f"{a.model}.full.npy").astype(np.float32)
E /= np.linalg.norm(E, axis=1, keepdims=True)
kpos = {k: i for i, k in enumerate(keys)}
meta = pd.read_parquet(T / "perturbations.parquet").set_index("key").loc[keys]
ptype = meta["pert_type"].values

TYPE_COL = {"CRISPRi": "#4C78A8", "CRISPRa": "#72B7B2", "CRISPR_KO": "#54A24B", "drug": "#E45756", "cytokine": "#B279A2"}
GREY = "#d9d9d9"

# coarse GO process for target genes (first matching rule wins)
GO_RULES = [
    ("translation / ribosome", ("translation", "ribosom", "rrna")),
    ("RNA processing / splicing", ("splicing", "mrna processing", "rna processing", "trna")),
    ("DNA replication / repair / cell cycle", ("dna replication", "dna repair", "cell cycle", "mitotic", "cell division", "chromosome segregation")),
    ("proteasome / ubiquitin / folding", ("proteasom", "ubiquitin", "protein folding")),
    ("mitochondria / metabolism", ("mitochondri", "respiratory", "metabolic process", "biosynthetic process")),
    ("transcription / chromatin", ("transcription", "chromatin", "histone")),
    ("signalling / immune", ("signaling", "immune", "receptor")),
]
GO_COL = dict(zip([r[0] for r in GO_RULES], ["#4C78A8", "#F58518", "#E45756", "#72B7B2", "#54A24B", "#B279A2", "#9D755D"]))
genes = pd.read_parquet(T / "gene_info.parquet")


def go_class(sym):
    if sym not in genes.index:
        return None
    txt = (str(genes.at[sym, "go_bp"]) + " " + str(genes.at[sym, "name"])).lower()
    for name, kws in GO_RULES:
        if any(k in txt for k in kws):
            return name
    return None


MOA_RULES = [
    ("kinase inhibitor", ("tk inhibitor", "egfr", "mapk", "mek ", "raf ", "pi3k", "mtor", "cdk", "jak", "gsk3", "kinase", "aurora", "alk", "btk", "flt3", "bcr-abl")),
    ("DNA synthesis / damage", ("dna synthesis", "topoisomerase", "dna methyltransferase", "dna ", "parp")),
    ("microtubule / cytoskeleton", ("microtubule", "tubulin", "actin")),
    ("chromatin / epigenetic", ("hdac", "bromodomain", "bet ", "histone", "ezh", "methyltransferase")),
    ("nuclear / GPCR receptor ligand", ("receptor agonist", "receptor antagonist", "adrenoceptor", "glucocorticoid", "retinoic", "androgen", "estrogen", "dopamine", "serotonin", "histamine")),
    ("proteostasis / translation", ("proteasome", "protein synthesis", "hsp", "ubiquitin")),
    ("metabolism / transport", ("cyclooxygenase", "glucose transporter", "reductase", "metabol", "channel", "pump")),
]
MOA_COL = dict(zip([r[0] for r in MOA_RULES], ["#4C78A8", "#E45756", "#F58518", "#B279A2", "#54A24B", "#72B7B2", "#9D755D"]))
tahoe = pd.read_parquet(ROOT / "data" / "raw" / "tahoe" / "meta" / "drug_metadata.parquet").set_index("drug")


def moa_class(drug):
    if drug not in tahoe.index:
        return None
    m = str(tahoe.at[drug, "moa-fine"]).lower() + " "
    for name, kws in MOA_RULES:
        if any(k in m for k in kws):
            return name
    return None


cyt = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False).set_index("cytokine")["family"]
CYT_FAM = cyt.value_counts().index[:7].tolist()
CYT_COL = dict(zip(CYT_FAM, ["#4C78A8", "#F58518", "#E45756", "#72B7B2", "#54A24B", "#B279A2", "#9D755D"]))


def embed2d(X, n_neighbors=15, seed=0):
    Xp = PCA(n_components=min(50, len(X) - 1), random_state=seed).fit_transform(X)
    return umap.UMAP(n_neighbors=n_neighbors, min_dist=0.3, metric="cosine", random_state=seed).fit_transform(Xp)


def scatter(ax, Y, labels, colours, title, order=None, s=3, legend=True, other="other / unannotated"):
    labels = np.array([l if l in colours else None for l in labels], dtype=object)
    bg = np.array([l is None for l in labels])
    ax.scatter(Y[bg, 0], Y[bg, 1], s=s, c=GREY, lw=0, rasterized=True, label=other if bg.any() else None)
    for name in (order or colours):
        m = labels == name
        if m.any():
            ax.scatter(Y[m, 0], Y[m, 1], s=s * 2, c=colours[name], lw=0, rasterized=True, label=f"{name} ({m.sum()})")
    ax.set_title(title, fontsize=10, loc="left")
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    if legend:
        ax.legend(fontsize=7, markerscale=3, frameon=False, loc="upper left", bbox_to_anchor=(1.0, 1.0))


# ---------- 1. global map ----------
print("[plot] global UMAP", flush=True)
Yg = embed2d(E, n_neighbors=30)
sym = meta["perturbation"].astype(str).values
go = [go_class(s) if t in ("CRISPRi", "CRISPRa", "CRISPR_KO") else None for s, t in zip(sym, ptype)]
moa = [moa_class(s) if t == "drug" else None for s, t in zip(sym, ptype)]
fam = [cyt.get(s) if t == "cytokine" else None for s, t in zip(sym, ptype)]
fig, axs = plt.subplots(2, 2, figsize=(15, 11))
scatter(axs[0, 0], Yg, ptype, TYPE_COL, f"a  All {len(E):,} perturbation cards, by type")
scatter(axs[0, 1], Yg, go, GO_COL, "b  Genetic perturbations, by GO process of the target")
scatter(axs[1, 0], Yg, moa, MOA_COL, "c  Tahoe drugs, by mechanism of action", s=6)
scatter(axs[1, 1], Yg, fam, CYT_COL, "d  Parse cytokines, by family", s=10)
fig.suptitle(f"Text-card embeddings ({a.model}), one UMAP", x=0.01, ha="left", fontsize=12)
fig.tight_layout()
fig.savefig(FIG / "umap_global.png", dpi=150)
plt.close(fig)

# ---------- 2. per-type maps ----------
print("[plot] per-type UMAPs", flush=True)
fig, axs = plt.subplots(1, 3, figsize=(20, 6))
gsel = np.where(ptype == "CRISPRi")[0]            # one card per gene: CRISPRi covers the genome-wide screen
Y = embed2d(E[gsel], n_neighbors=30)
scatter(axs[0], Y, [go[i] for i in gsel], GO_COL, f"Gene cards (CRISPRi, {len(gsel):,}), by GO process")
dsel = np.where(ptype == "drug")[0]
Y = embed2d(E[dsel])
dl = [moa[i] if moa[i] else ("sciPlex3 only" if sym[i] not in tahoe.index else None) for i in dsel]
scatter(axs[1], Y, dl, {**MOA_COL, "sciPlex3 only": "#BAB0AC"}, f"Drug cards ({len(dsel)}), by mechanism", s=8)
csel = np.where(ptype == "cytokine")[0]
Y = embed2d(E[csel], n_neighbors=10)
scatter(axs[2], Y, [fam[i] for i in csel], CYT_COL, f"Cytokine cards ({len(csel)}), by family", s=30)
for i, j in enumerate(csel):
    axs[2].annotate(sym[j], Y[i], fontsize=5, alpha=0.7, xytext=(2, 2), textcoords="offset points")
fig.tight_layout()
fig.savefig(FIG / "umap_by_type.png", dpi=150)
plt.close(fig)

# ---------- 3. alignment with measured responses ----------
SCREENS = [("NormanWeissman2019_filtered", "Norman (CRISPRa)"), ("ReplogleWeissman2022_K562_essential", "Replogle K562 essential (CRISPRi)"),
           ("SrivatsanTrapnell2020_sciplex3", "sciPlex3 (drugs)"), ("tahoe100m", "Tahoe-100M (drugs)"), ("parse_pbmc_cytokines", "Parse (cytokines)")]
CL_COL = ["#4C78A8", "#F58518", "#E45756", "#72B7B2", "#54A24B", "#B279A2"]
rows = []
fig, axs = plt.subplots(len(SCREENS), 3, figsize=(15, 4.3 * len(SCREENS)))
rng = np.random.default_rng(0)
for r, (ds, label) in enumerate(SCREENS):
    print(f"[plot] alignment {ds}", flush=True)
    z = np.load(T / "profiles" / f"{ds}.npz", allow_pickle=True)
    names, P, pt = z["names"].astype(str), z["P"].astype(np.float32), str(z["pert_type"])
    k = np.array([f"{pt}::{n}" for n in names])
    ok = np.array([x in kpos for x in k])
    names, P, k = names[ok], P[ok], k[ok]
    norm = np.linalg.norm(P, axis=1)
    strong = norm >= np.median(norm)
    names, P, k = names[strong], P[strong], k[strong]
    X = E[[kpos[x] for x in k]]
    Pz = PCA(n_components=min(20, len(P) - 1), random_state=0).fit_transform(P - P.mean(0))
    ncl = 6 if len(P) >= 60 else 4
    cl = KMeans(ncl, n_init=20, random_state=0).fit_predict(Pz / np.linalg.norm(Pz, axis=1, keepdims=True))
    cols = {f"response cluster {c + 1}": CL_COL[c] for c in range(ncl)}
    labs = [f"response cluster {c + 1}" for c in cl]
    nn = min(15, len(X) - 2)
    s = 30 if len(X) < 300 else 8
    Yt = umap.UMAP(n_neighbors=nn, min_dist=0.3, metric="cosine", random_state=0).fit_transform(X)
    Yr = umap.UMAP(n_neighbors=nn, min_dist=0.3, metric="correlation", random_state=0).fit_transform(P)
    # text neighbours that share the response cluster, against the chance rate
    kk = min(10, len(X) - 1)
    idx = NearestNeighbors(n_neighbors=kk + 1, metric="cosine").fit(X).kneighbors(X, return_distance=False)[:, 1:]
    same = (cl[idx] == cl[:, None]).mean()
    chance = ((np.bincount(cl) / len(cl)) ** 2).sum()
    # pairwise text cosine vs response correlation
    iu = np.triu_indices(len(X), 1)
    if len(iu[0]) > 200_000:
        pick = rng.choice(len(iu[0]), 200_000, replace=False)
        iu = (iu[0][pick], iu[1][pick])
    S = (X @ X.T)[iu]
    Pc = P - P.mean(1, keepdims=True)
    Pc /= np.linalg.norm(Pc, axis=1, keepdims=True) + 1e-9
    C = (Pc @ Pc.T)[iu]
    rho = spearmanr(S, C).statistic
    rows.append({"screen": label, "perturbations (stronger half)": len(X), "clusters": ncl, "text kNN in same response cluster": same,
                 "chance": chance, "enrichment": same / chance, "spearman text sim vs response corr": rho})
    scatter(axs[r, 0], Yt, labs, cols, f"{label}: text UMAP", s=s, legend=False)
    scatter(axs[r, 1], Yr, labs, cols, f"response UMAP ({len(X)} perturbations)", s=s)
    if len(X) <= 100:
        for i, n in enumerate(names):
            axs[r, 0].annotate(n, Yt[i], fontsize=5, alpha=0.6, xytext=(2, 2), textcoords="offset points")
    ax = axs[r, 2]
    ax.hexbin(S, C, gridsize=40, cmap="Greys", bins="log", mincnt=1)
    q = pd.qcut(S, 10, duplicates="drop")
    m = pd.DataFrame({"S": S, "C": C}).groupby(q, observed=True).mean()
    ax.plot(m["S"], m["C"], "o-", c="#E45756", ms=4, lw=1.5)
    ax.set_xlabel("text-card cosine similarity", fontsize=8); ax.set_ylabel("response correlation", fontsize=8)
    ax.set_title(f"Spearman {rho:.2f}\ntext neighbours in same response cluster: {same:.0%} (chance {chance:.0%})", fontsize=9, loc="left")
    ax.tick_params(labelsize=7)
fig.suptitle("Do perturbations with similar text cards have similar responses?  Colour = cluster of the measured response",
             x=0.01, ha="left", fontsize=12)
fig.tight_layout(rect=(0, 0, 1, 0.985))
fig.savefig(FIG / "alignment.png", dpi=130)
plt.close(fig)
pd.DataFrame(rows).to_csv(FIG / "alignment.csv", index=False)
print(pd.DataFrame(rows).to_string(index=False))
print(f"[plot] wrote {FIG}")

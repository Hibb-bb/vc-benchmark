#!/usr/bin/env python
"""Immune Dictionary (Cui et al., Nature 2024; GEO GSE202186) -> one annotated h5ad of raw counts.

  .venv/bin/python scripts/ingest_immune_dictionary.py --stage demux [--channels 1]   # Slurm, ~1 h for all 44
  .venv/bin/python scripts/ingest_immune_dictionary.py --stage annotate               # Slurm, ~1 h

Mouse lymph nodes, 4 h after one injected cytokine (86 cytokines x 3 mice, PBS mice in every processing batch).
Each of the 44 10x channels pools up to 7 mice tagged with hashtag antibodies; the gene-expression libraries
(cytokine-samplesNN) and hashtag libraries (cytokine-hashtagsNN) are separate GEO samples, and
GSE202186_map.xlsx maps (channel, hashtag) to cytokine, batch and replicate.

demux: per channel, call cells (>= 500 UMIs and >= 250 genes, < 10% mitochondrial), read the hashtag counts of
the tags used in that channel, normalise each tag by its median over the called cells, and assign the top tag
when it is at least 3x the runner-up on that scale and has >= 5 raw counts (otherwise negative or doublet, dropped).
Writes data/raw/immune_dictionary/channels/chNN.h5ad.
annotate: concatenate, cluster (log CP10k, 3,000 HVGs, 50 PCs, Leiden) and name clusters by mouse lymph node
markers; clusters whose best marker set averages below 0.5 (log CP10k) are dropped as unassigned. Writes data/raw/immune_dictionary/immune_dictionary.h5ad with obs cytokine, mouse, batch, cell_type.
"""
import argparse
import re
import zipfile
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.io
import scipy.sparse as sp

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "immune_dictionary"
GEO = RAW / "geo"
OUT = RAW / "channels"
ap = argparse.ArgumentParser()
ap.add_argument("--stage", choices=["demux", "annotate"], required=True)
ap.add_argument("--channels", default=None, help="comma-separated channel numbers (default all)")
a = ap.parse_args()


def read_map():
    """GSE202186_map.xlsx without openpyxl: shared strings + sheet XML."""
    z = zipfile.ZipFile(RAW / "GSE202186_map.xlsx")
    ss = [re.sub(r"<[^>]+>", "", s) for s in re.findall(r"<si>.*?</si>", z.read("xl/sharedStrings.xml").decode(), flags=re.S)]
    rows = []
    for r in re.findall(r"<row[^>]*>(.*?)</row>", z.read("xl/worksheets/sheet1.xml").decode(), flags=re.S):
        row = {}
        for col, attr, v in re.findall(r'<c r="([A-Z]+)\d+"([^>]*)>(?:<v>([^<]*)</v>)?', r):
            if v:
                row[col] = ss[int(v)] if 't="s"' in attr else v
        rows.append(row)
    df = pd.DataFrame(rows[1:]).rename(columns={"A": "channel", "B": "hashtag", "C": "batch", "D": "cytokine", "E": "rep"})
    df["hashtag"] = df["hashtag"].astype(int)
    return df[df["cytokine"].notna() & (df["cytokine"] != "NA")]


def read_mtx(prefix):
    f = sorted(GEO.glob(f"GSM*_{prefix}-matrix.mtx.gz"))[0]
    stem = str(f).replace("-matrix.mtx.gz", "")
    M = scipy.io.mmread(f).tocsc()                    # features x barcodes
    bc = pd.read_csv(stem + "-barcodes.tsv.gz", header=None)[0].astype(str).str.replace("-1$", "", regex=True).values
    feat = pd.read_csv(stem + "-features.tsv.gz", header=None, sep="\t")
    return M, bc, feat


if a.stage == "demux":
    OUT.mkdir(parents=True, exist_ok=True)
    mp = read_map()
    chans = sorted(mp["channel"].unique())
    if a.channels:
        want = {f"cytokine-samples{int(c):02d}" for c in a.channels.split(",")}
        chans = [c for c in chans if c in want]
    for ch in chans:
        n = ch.replace("cytokine-samples", "")
        G, bc, feat = read_mtx(ch)
        umi = np.asarray(G.sum(0)).ravel()
        ngen = np.diff(G.indptr)
        mito = feat[1].astype(str).str.startswith("mt-").values
        pmt = np.asarray(G[mito].sum(0)).ravel() / np.maximum(umi, 1)
        cells = np.where((umi >= 500) & (ngen >= 250) & (pmt < 0.10))[0]
        H, hbc, hfeat = read_mtx(f"cytokine-hashtags{n}")
        hpos = pd.Index(hbc).get_indexer(bc[cells])
        found = hpos >= 0
        tags = mp[mp["channel"] == ch].set_index("hashtag")
        tag_rows = [i for i, t in enumerate(hfeat[0].astype(str)) if t.startswith("tag") and int(t[3:5]) in tags.index]
        tag_ids = [int(hfeat[0].astype(str)[i][3:5]) for i in tag_rows]
        Hc = np.zeros((len(cells), len(tag_rows)), dtype=np.float32)
        Hc[found] = H.tocsr()[tag_rows][:, hpos[found]].toarray().T
        med = np.maximum(np.median(Hc[found], axis=0), 1.0)
        R = Hc / med
        order = np.argsort(-R, axis=1)
        top, second = R[np.arange(len(R)), order[:, 0]], R[np.arange(len(R)), order[:, 1]] if R.shape[1] > 1 else np.zeros(len(R))
        top_raw = Hc[np.arange(len(R)), order[:, 0]]
        ok = found & (top_raw >= 5) & (top >= 3 * np.maximum(second, 1e-3))
        assigned = np.array(tag_ids)[order[:, 0]]
        keep = cells[ok]
        obs = pd.DataFrame({"channel": ch, "hashtag": assigned[ok], "n_counts": umi[keep], "n_genes": ngen[keep], "pct_mt": pmt[keep]},
                           index=[f"{n}_{b}" for b in bc[keep]])
        obs = obs.join(tags[["batch", "cytokine", "rep"]], on="hashtag")
        obs["mouse"] = obs["cytokine"].astype(str) + "_" + obs["rep"].astype(str) + "_b" + obs["batch"].astype(str)
        X = G[:, keep].T.tocsr().astype(np.float32)
        var = pd.DataFrame({"gene_ids": feat[0].astype(str).values}, index=pd.Index(feat[1].astype(str).values, name=None))
        cd = ad.AnnData(X=X, obs=obs, var=var)
        cd.var_names_make_unique()
        cd.write_h5ad(OUT / f"ch{n}.h5ad")
        print(f"[demux] {ch}: {len(cells)} called cells, {found.mean():.1%} with hashtag reads, "
              f"{ok.sum()} assigned ({ok.sum() / len(cells):.1%}); per tag {np.bincount(assigned[ok]).tolist()}", flush=True)

else:
    import scanpy as sc
    parts = [ad.read_h5ad(f) for f in sorted(OUT.glob("ch*.h5ad"))]
    A = ad.concat(parts, join="inner", merge="same")
    A.obs_names_make_unique()
    print(f"[annotate] {A.n_obs} cells, {A.obs['mouse'].nunique()} mice, {A.obs['cytokine'].nunique()} conditions", flush=True)
    B = A.copy()
    sc.pp.normalize_total(B, target_sum=1e4)
    sc.pp.log1p(B)
    sc.pp.highly_variable_genes(B, n_top_genes=3000, batch_key="batch")
    B = B[:, B.var["highly_variable"]].copy()
    sc.pp.scale(B, max_value=10)
    sc.tl.pca(B, n_comps=50)
    sc.pp.neighbors(B, n_neighbors=15)
    sc.tl.leiden(B, resolution=1.5, flavor="igraph", n_iterations=2)
    # mouse lymph node markers (first matching set by mean expression wins at the cluster level)
    MARK = {
        "B cell": ["Cd79a", "Cd19", "Ms4a1", "Cd79b"],
        "Plasma cell": ["Jchain", "Xbp1", "Sdc1", "Mzb1"],
        "T cell CD4": ["Cd3e", "Cd4", "Cd40lg", "Il7r"],
        "T cell CD8": ["Cd3e", "Cd8a", "Cd8b1"],
        "Treg": ["Foxp3", "Il2ra", "Ctla4"],
        "T cell gd": ["Trdc", "Tcrg-C1", "Cd163l1"],
        "NK cell": ["Nkg7", "Ncr1", "Klrb1c", "Gzma"],
        "ILC": ["Il7r", "Gata3", "Rora", "Kit"],
        "cDC1": ["Xcr1", "Clec9a", "Cd8a", "Itgae"],
        "cDC2": ["Sirpa", "Cd209a", "Clec4a4", "Itgam"],
        "Migratory DC": ["Ccr7", "Fscn1", "Ccl22", "Cd200"],
        "pDC": ["Siglech", "Bst2", "Ccr9", "Klk1"],
        "Macrophage": ["C1qa", "C1qb", "Adgre1", "Mertk"],
        "Monocyte": ["Ly6c2", "Ccr2", "Lyz2", "Fn1"],
        "Neutrophil": ["S100a8", "S100a9", "Retnlg", "Csf3r"],
        "Mast/basophil": ["Cpa3", "Mcpt8", "Fcer1a"],
    }
    lognorm = B.raw if B.raw is not None else None
    C = A.copy()
    sc.pp.normalize_total(C, target_sum=1e4)
    sc.pp.log1p(C)
    cl = B.obs["leiden"].values
    names = {}
    rows = []
    for k in sorted(set(cl), key=int):
        m = cl == k
        sub = C[m]
        score = {}
        for ct, genes in MARK.items():
            g = [x for x in genes if x in C.var_names]
            score[ct] = float(np.asarray(sub[:, g].X.mean(0)).mean()) if g else 0.0
        # T-cell subsets need Cd3e; drop CD8 for DCs etc. via the top score, then specialise T cells
        best = max(score, key=score.get)
        if score[best] < 0.5:                    # no marker set clearly expressed: low-quality or ambiguous cluster
            best = "Unassigned"
        cd3 = float(np.asarray(sub[:, "Cd3e"].X.mean())) if "Cd3e" in C.var_names else 0
        if best in ("T cell CD4", "T cell CD8", "Treg", "T cell gd", "ILC", "NK cell") and cd3 > 0.5:
            sub_s = {t: score[t] for t in ("T cell CD4", "T cell CD8", "Treg", "T cell gd")}
            best = max(sub_s, key=sub_s.get)
        names[k] = best
        rows.append({"cluster": k, "n": int(m.sum()), "label": best, **{t: round(v, 2) for t, v in score.items()}})
    tab = pd.DataFrame(rows)
    print(tab[["cluster", "n", "label"]].to_string(index=False), flush=True)
    tab.to_csv(RAW / "cluster_labels.csv", index=False)
    A.obs["leiden"] = cl
    A.obs["cell_type"] = pd.Categorical([names[k] for k in cl])
    A.obsm["X_pca"] = B.obsm["X_pca"]
    print(f"[annotate] dropping {int((A.obs['cell_type'] == 'Unassigned').sum())} unassigned cells", flush=True)
    A = A[A.obs["cell_type"] != "Unassigned"].copy()
    A.obs["cell_type"] = A.obs["cell_type"].cat.remove_unused_categories()
    A.write_h5ad(RAW / "immune_dictionary.h5ad")
    ct = pd.crosstab(A.obs["cytokine"], A.obs["cell_type"])
    ct.to_csv(RAW / "cytokine_celltype_counts.csv")
    print(A.obs["cell_type"].value_counts().to_string(), flush=True)
    print(f"[annotate] wrote {RAW / 'immune_dictionary.h5ad'}", flush=True)

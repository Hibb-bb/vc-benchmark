#!/usr/bin/env python
"""Step 4a: is a text embedding a good representation of a perturbation? Split-free checks.

  .venv/bin/python scripts/pert_text/evaluate.py      # after embed.py and response_profiles.py

For every screen and every representation (each text model x {full card, name only}, the non-text
baselines, and a random embedding):
- similarity match: Spearman correlation, over all pairs of perturbations in the screen, between the
  cosine similarity of their representations and the Pearson correlation of their measured response
  profiles (mean shift on the screen's HVGs);
- neighbours: mean response correlation between a perturbation and its 5 nearest neighbours in the
  representation, against the mean over all pairs;
- classes: leave-one-out 5-nearest-neighbour accuracy at recovering a known label (Tahoe mechanism of
  action, sciPlex3 pathway, cytokine family), against always guessing the commonest label.
Screens with more than 2,000 perturbations are subsampled to 2,000 (fixed seed).
Writes runs/pert_text/eval.csv and runs/pert_text/eval.md.
"""
import glob
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "runs" / "pert_text"
keys = (T / "emb" / "keys.txt").read_text().splitlines()
kpos = {k: i for i, k in enumerate(keys)}
EMB = {}
for f in sorted((T / "emb").glob("*.npy")):
    tag, field = f.stem.rsplit(".", 1)
    EMB[f"{tag} · {'card' if field == 'full' else 'name only'}"] = np.load(f)

cyt = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False).set_index("cytokine")
tahoe = pd.read_parquet(ROOT / "data" / "raw" / "tahoe" / "meta" / "drug_metadata.parquet").set_index("drug")
sci = pd.read_parquet(T / "perturbations.parquet").set_index("key")


def labels_for(ds, names):
    if ds == "parse_pbmc_cytokines":
        return pd.Series([cyt["family"].get(n) for n in names], index=names)
    if ds == "tahoe100m":
        return pd.Series([tahoe["moa-fine"].get(n) for n in names], index=names)
    if ds == "SrivatsanTrapnell2020_sciplex3":
        lab = {}
        txt = sci.loc[sci.pert_type == "drug", "text_full"]
        for k, t in txt.items():
            if "Pathway:" in t:
                lab[k.split("::", 1)[1]] = t.split("Pathway:")[1].split("(")[0].strip().rstrip(".")
        return pd.Series([lab.get(n) for n in names], index=names)
    return None


def cos(E):
    E = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-12)
    return E @ E.T


def corr(P):
    P = P - P.mean(1, keepdims=True)
    P = P / (np.linalg.norm(P, axis=1, keepdims=True) + 1e-12)
    return P @ P.T


def cytokine_fm(names, src):
    emb = pd.read_parquet(ROOT / "runs" / "pert_pool_v0" / "cytokine_features" / f"{src}.parquet")
    def part(gs):
        gs = [g for g in gs.split(",") if g in emb.index]
        return emb.loc[gs].values.mean(0) if gs else np.zeros(emb.shape[1])
    return np.stack([np.concatenate([part(cyt.loc[n, "ligand_genes"]), part(cyt.loc[n, "receptor_genes"])]) for n in names]), np.ones(len(names), bool)


rows = []
for f in sorted(glob.glob(str(T / "profiles" / "*.npz"))):
    z = np.load(f, allow_pickle=False)
    ds, names, P, ptype = Path(f).stem, z["names"], z["P"], str(z["pert_type"])
    sel = np.arange(len(names))
    if len(sel) > 2000:
        sel = np.sort(np.random.default_rng(0).choice(sel, 2000, replace=False))
    names, P = names[sel], P[sel]
    have = np.array([f"{ptype}::{n}" in kpos for n in names])
    reps = {k: (E[[kpos.get(f"{ptype}::{n}", 0) for n in names]], have) for k, E in EMB.items()}
    for b in ("base_ctrlpca", "base_morgan"):
        if b in z.files:
            reps[{"base_ctrlpca": "baseline · gene from control cells", "base_morgan": "baseline · chemical fingerprint"}[b]] = (z[b][sel], z[f"{b}_ok"][sel])
    if ds == "parse_pbmc_cytokines":
        for src in ("scgpt", "geneformer", "scfoundation", "esm2"):
            reps[f"baseline · {src} genes"] = cytokine_fm(names, src)
    reps["random"] = (np.random.default_rng(1).standard_normal((len(names), 256)).astype(np.float32), np.ones(len(names), bool))
    R = corr(P)
    iu = np.triu_indices(len(names), 1)
    lab = labels_for(ds, names)
    for rep, (E, ok) in reps.items():
        m = ok & np.isfinite(E).all(1) & (np.abs(E).sum(1) > 0)
        if m.sum() < 10:
            continue
        idx = np.where(m)[0]
        S = cos(E[idx]); Rm = R[np.ix_(idx, idx)]
        iu_m = np.triu_indices(len(idx), 1)
        rsa = spearmanr(S[iu_m], Rm[iu_m])[0]
        np.fill_diagonal(S, -np.inf)
        nn = np.argsort(-S, axis=1)[:, :5]
        nn_r = float(np.mean([Rm[i, nn[i]].mean() for i in range(len(idx))]))
        base_r = float(Rm[iu_m].mean())
        acc = chance = np.nan
        if lab is not None:
            L = lab.iloc[idx].values
            okl = pd.notna(L)
            if okl.sum() > 20:
                Li = L[okl]; Sl = S[np.ix_(okl, okl)]
                nnl = np.argsort(-Sl, axis=1)[:, :5]
                pred = [pd.Series(Li[r]).mode().iloc[0] for r in nnl]
                acc = float(np.mean(np.asarray(pred) == Li)); chance = float(pd.Series(Li).value_counts(normalize=True).iloc[0])
        rows.append({"dataset": ds, "type": ptype, "representation": rep, "n": int(len(idx)), "similarity_match": rsa,
                     "neighbour_r": nn_r, "all_pairs_r": base_r, "class_acc": acc, "class_chance": chance})
    print(f"{ds}: {len(names)} perturbations evaluated", flush=True)

ev = pd.DataFrame(rows)
ev.to_csv(T / "eval.csv", index=False)
lines = ["# Text embeddings as perturbation representations", "",
         "similarity match = Spearman r between representation similarity and response similarity over all pairs; "
         "neighbour r = mean response correlation with the 5 nearest neighbours (all-pairs mean in brackets); "
         "class = 5-NN accuracy at a known label (chance in brackets).", ""]
for ds, g in ev.groupby("dataset"):
    lines += [f"## {ds} ({g['type'].iloc[0]}, {int(g['n'].max())} perturbations)", "", "| representation | similarity match | neighbour r | class accuracy |", "|---|---|---|---|"]
    for r in g.sort_values("similarity_match", ascending=False).itertuples():
        cls = "" if np.isnan(r.class_acc) else f"{r.class_acc:.2f} ({r.class_chance:.2f})"
        lines.append(f"| {r.representation} | {r.similarity_match:+.3f} | {r.neighbour_r:.3f} ({r.all_pairs_r:.3f}) | {cls} |")
    lines.append("")
(T / "eval.md").write_text("\n".join(lines))
print("\n".join(lines))

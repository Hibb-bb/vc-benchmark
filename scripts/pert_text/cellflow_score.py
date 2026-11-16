#!/usr/bin/env python
"""Score CellFlow with a one-hot perturbation representation and with text cards, and place both on the published
scales (same procedure as cpa_score.py).

  .venv/bin/python scripts/pert_text/cellflow_score.py [small|combosciplex]   # scores every set whose cellflow_{onehot,text}/*.npz are complete

For each (dataset, scheme) with five folds of both arms: append_pert_scores.py merges cellflow_onehot and cellflow_text into a
copy of the published scores table (runs/pert_text/cellflow/<dataset>.<scheme>.scores.parquet; the published table is not
touched), then both are placed on the published Rasch scale with item difficulties held fixed. Writes
runs/pert_text/cellflow/summary_<preset>.md.
"""
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_rasch
from vcb.scoring import binarize

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "runs" / "pert_text" / "cellflow"
SETS = [("NormanWeissman2019_filtered", "perturbation", "pert_pool_v0"),
        ("SrivatsanTrapnell2020_sciplex3", "perturbation", "pert_pool_v0"), ("SrivatsanTrapnell2020_sciplex3", "context", "pert_pool_v0"),
        ("immune_dictionary", "perturbation", "pert_idict_v0"), ("immune_dictionary", "context", "pert_idict_v0"),
        ("tahoe100m", "perturbation", "pert_pool_v0"), ("tahoe100m", "context", "pert_pool_v0")]
import sys
PRESET = sys.argv[1] if len(sys.argv) > 1 else "small"      # "small" or "combosciplex" (run_cellflow.py --preset)
TAG = "cellflow_cs" if PRESET == "combosciplex" else "cellflow"
ARMS = [f"{TAG}_onehot", f"{TAG}_text"]
lines = [f"# CellFlow ({PRESET} settings) with a one-hot perturbation vs the text card", "",
         "Abilities on each dataset's published Rasch scale (item difficulties fixed). Pass = predicted shift correlates "
         "with the truth better than the mean shift does.", "",
         "| dataset | split | CellFlow one-hot | CellFlow text card | text − one-hot | best published model | ridge (d=50, λ=100) |",
         "|---|---|---|---|---|---|---|"]
for ds, scheme, run in SETS:
    if not all((C / arm / f"{ds}.{scheme}.fold{k}.npz").exists() for arm in ARMS for k in range(5)):
        lines.append(f"| {ds} | {scheme} | pending | pending | | | |")
        continue
    out = C / f"{ds}.{scheme}.{TAG}.scores.parquet"
    src = RUNS / run / f"{ds}.{scheme}.scores.parquet"
    pd.read_parquet(src).to_parquet(out, index=False)
    for arm in ARMS:
        subprocess.run([str(ROOT / ".venv" / "bin" / "python"), str(ROOT / "scripts" / "append_pert_scores.py"), "--dataset", ds,
                        "--scheme", scheme, "--respondent", arm, "--run", run, "--npz-root", str(C), "--out", str(out),
                        "--min-cells", "30" if ds == "immune_dictionary" else "50"],
                       check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
        # append_pert_scores merges into the published table read from --run; fold the earlier arm back in
        if arm != ARMS[0]:
            prev = pd.read_parquet(C / f"{ds}.{scheme}.{TAG}.prev.parquet")
            cur = pd.read_parquet(out)
            pd.concat([cur, prev[prev["respondent_id"] == ARMS[0]]], ignore_index=True).to_parquet(out, index=False)
        else:
            pd.read_parquet(out).to_parquet(C / f"{ds}.{scheme}.{TAG}.prev.parquet", index=False)
    sc = pd.read_parquet(out)
    b = binarize(sc[sc["respondent_id"].isin(ARMS + ["mean_shift"])])
    b = b[b["respondent_id"].isin(ARMS)]
    diff = pd.read_csv(RUNS / run / "rasch" / f"{ds}.{scheme}.difficulties.csv").set_index("item_id")
    d = diff.loc[~diff["degenerate"], "difficulty"]
    b = b[b["item_id"].isin(d.index)]
    items = pd.Index(sorted(d.index)); rs = pd.Index(ARMS)
    K = np.zeros((2, len(items))); N = np.zeros_like(K)
    np.add.at(K, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["k"].values)
    np.add.at(N, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["n"].values)
    th, se, *_ = fit_rasch(K, N, anchors={i: float(d[it]) for i, it in enumerate(items)}, n_iter=300)
    pub = pd.read_csv(RUNS / run / "rasch" / f"{ds}.{scheme}.abilities.csv")
    pub = pub[~pub["respondent_id"].astype(str).str.contains("_txt|_g(?:scgpt|geneformer|scfoundation|esm2|ctrlpca)$", regex=True)]
    best = pub.sort_values("ability", ascending=False).iloc[0]
    ridge = pub.set_index("respondent_id")["ability"].get("ridge_d50_lam100", np.nan)
    lines.append(f"| {ds} | {scheme} | {th[0]:+.2f} ± {se[0]:.2f} | {th[1]:+.2f} ± {se[1]:.2f} | {th[1] - th[0]:+.2f} | "
                 f"{best.respondent_id} {best.ability:+.2f} | {ridge:+.2f} |")
    r = sc[sc["metric"] == "pearson_delta@hvg"].groupby("respondent_id")["value"].mean()
    print(f"{ds} {scheme}: Pearson one-hot {r.get(ARMS[0], np.nan):.3f} text {r.get(ARMS[1], np.nan):.3f} mean_shift {r.get('mean_shift', np.nan):.3f}", flush=True)
(C / f"summary_{PRESET}.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))

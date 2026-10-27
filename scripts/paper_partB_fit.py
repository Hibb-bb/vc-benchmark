#!/usr/bin/env python
"""Part B pooled fit for the paper: the unseen-perturbation scale without the respondents added after
the paper's Part B section was written.

The live pooled fit (`runs/pert_pool_v0/rasch/pooled.*`) now includes the two item-feature MLPs added on
2026-10-20. Those belong to the perturbation work that is kept out of the paper for now, and adding them
moves every difficulty and ability a little. This refits the same 15 screens with the same rule
(pearson_delta@hvg against the mean shift) and the paper's respondent set, and writes
`runs/pert_pool_v0/rasch_paper/pooled.{abilities,difficulties}.csv` plus the per-screen fits of the
unseen-combination split, which the paper scripts read. The 2026-10-20 additions also include scVI
counterfactual and scGen on the unseen-combination screens; they are left out the same way.

    .venv/bin/python scripts/paper_partB_fit.py
"""
from pathlib import Path

import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_from_long
from vcb.scoring import binarize

RUN = RUNS / "pert_pool_v0"
EXCLUDE = {"mlp_h1024_d50", "mlp_h256_d50", "scvi_cf", "scgen"}  # added 2026-10-20, outside the paper's scope

parts = []
for f in sorted(RUN.glob("*.perturbation.scores.parquet")):
    long = pd.read_parquet(f).drop_duplicates(["item_id", "respondent_id", "metric"], keep="first")
    long = long[~long.respondent_id.isin(EXCLUDE)]
    parts.append(binarize(long, metric="pearson_delta@hvg", reference="mean_shift", margin=0.0))
b = pd.concat(parts)
abil, diff, info = fit_from_long(b)
out = RUN / "rasch_paper"
out.mkdir(exist_ok=True)
abil.to_csv(out / "pooled.abilities.csv", index=False)
diff.to_csv(out / "pooled.difficulties.csv", index=False)
# per-screen fits of the unseen-combination split, quoted in the text for Tahoe-100M and Parse
for f in sorted(RUN.glob("*.context.scores.parquet")):
    long = pd.read_parquet(f).drop_duplicates(["item_id", "respondent_id", "metric"], keep="first")
    long = long[~long.respondent_id.isin(EXCLUDE)]
    a_, d_, _ = fit_from_long(binarize(long, metric="pearson_delta@hvg", reference="mean_shift", margin=0.0))
    tag = f.name.replace(".scores.parquet", "")
    a_.to_csv(out / f"{tag}.abilities.csv", index=False)
    d_.to_csv(out / f"{tag}.difficulties.csv", index=False)
print(f"{b['dataset_id'].nunique()} screens, {len(diff)} items, {len(abil)} respondents, converged={info['converged']}")

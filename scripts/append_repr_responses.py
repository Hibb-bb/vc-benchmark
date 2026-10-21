#!/usr/bin/env python
"""Run the frozen probe on a cached external embedding and append its responses to a run.

  python scripts/append_repr_responses.py --panel data/panels/ts2_panel_v0.h5ad --run repr_pool_v0 --embedding scvi_k30_btissue

Same probe, same train/test panel, same item filter as the classical pool. Rows of the
same respondent are replaced.
"""
import argparse
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd

from vcb import ROOT, RUNS
from vcb.repr.probe import probe_responses

ap = argparse.ArgumentParser()
ap.add_argument("--panel", required=True)
ap.add_argument("--run", required=True)
ap.add_argument("--embedding", required=True, help="name of cache/embeddings/<name>.npz (may include a panel subdirectory, e.g. hao_pbmc_l2/fm_scgpt)")
ap.add_argument("--respondent", default=None, help="respondent_id to record (default: the embedding name)")
a = ap.parse_args()

panel = ad.read_h5ad(a.panel, backed="r")
obs = panel.obs
tr = (obs["split"] == "train").values
te = (obs["split"] == "test").values & obs["type_in_train"].values.astype(bool)
z = np.load(ROOT / "cache" / "embeddings" / f"{a.embedding}.npz", allow_pickle=True)
Ztr_df = pd.DataFrame(z["Z_train"], index=z["train_ids"])
tr_ids = obs.index[tr].intersection(Ztr_df.index)  # a debug embedding may cover a train subsample
if len(tr_ids) < tr.sum():
    print(f"warning: embedding covers {len(tr_ids)}/{tr.sum()} train cells; probe fit on those")
Zte_df = pd.DataFrame(z["Z_test"], index=z["test_ids"])
te_ids = obs.index[te]
missing = te_ids.difference(Zte_df.index)
if len(missing) and "debug" in (a.respondent or a.embedding):
    te_ids = te_ids.intersection(Zte_df.index)
assert te_ids.isin(Zte_df.index).all(), f"{len(missing)} test items lack an embedding"
Ztr, Zte = Ztr_df.loc[tr_ids].values, Zte_df.loc[te_ids].values
rid = a.respondent or a.embedding
df = probe_responses(Ztr, obs.loc[tr_ids, "cell_type"].values, Zte, obs.loc[te_ids, "cell_type"].values, te_ids, rid)
df["dataset_id"] = obs["dataset_id"].iloc[0]
path = RUNS / a.run / "responses.parquet"
old = pd.read_parquet(path)
old = old[old["respondent_id"] != rid]
pd.concat([old, df], ignore_index=True).to_parquet(path, index=False)
print(f"{rid}: dim={Zte.shape[1]} acc={df['k'].mean():.3f} on {len(df)} items; appended to {path}")

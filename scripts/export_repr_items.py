#!/usr/bin/env python
"""Regenerate runs/<run>/items.parquet from a panel (no pool rerun)."""
import argparse
from pathlib import Path
import anndata as ad
from vcb import RUNS
from vcb.repr.run import panel_items
ap = argparse.ArgumentParser(); ap.add_argument("--panel", required=True); ap.add_argument("--run", required=True); a = ap.parse_args()
panel = ad.read_h5ad(a.panel)
tr = (panel.obs["split"] == "train").values
te = (panel.obs["split"] == "test").values & panel.obs["type_in_train"].values.astype(bool)
items = panel_items(panel, te, panel.obs.loc[tr, "cell_type"].values)
items.to_parquet(RUNS / a.run / "items.parquet"); print(a.run, len(items), "items")

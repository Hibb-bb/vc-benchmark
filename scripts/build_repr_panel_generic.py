#!/usr/bin/env python
"""Build a component-A panel from any annotated h5ad.

  python scripts/build_repr_panel_generic.py --h5ad data/raw/cellxgene_repr/hlca_core.h5ad --name hlca_core \
      --label-key ann_finest_level --donor-key donor_id --context-key study --split-by context --counts raw
"""
import argparse
from pathlib import Path

from vcb import DATA
from vcb.data.repr_generic import build_generic_panel

ap = argparse.ArgumentParser()
ap.add_argument("--h5ad", required=True)
ap.add_argument("--name", required=True)
ap.add_argument("--label-key", required=True)
ap.add_argument("--donor-key", required=True)
ap.add_argument("--context-key", default=None)
ap.add_argument("--counts", default="raw", help="'X', 'raw', or 'layers/<name>'")
ap.add_argument("--split-by", default="donor", choices=["donor", "context"])
ap.add_argument("--test-groups", default=None, help="comma-separated held-out donors/contexts (overrides automatic choice)")
ap.add_argument("--test-frac", type=float, default=0.25)
ap.add_argument("--test-cap", type=int, default=50)
ap.add_argument("--train-cap", type=int, default=200)
ap.add_argument("--min-stratum", type=int, default=20)
ap.add_argument("--filter", default=None, help="pandas query on obs, e.g. \"assay == '10x 3\\' v3'\"")
ap.add_argument("--out", default=None)
a = ap.parse_args()
out = Path(a.out) if a.out else DATA / "panels" / f"{a.name}.h5ad"
build_generic_panel(Path(a.h5ad), a.name, a.label_key, a.donor_key, a.context_key, out, counts=a.counts, split_by=a.split_by,
                    test_frac=a.test_frac, test_cap=a.test_cap, train_cap=a.train_cap, min_stratum=a.min_stratum, filter_query=a.filter,
                    test_groups=a.test_groups.split(",") if a.test_groups else None)

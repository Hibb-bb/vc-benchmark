#!/usr/bin/env python
"""python scripts/build_pert_items.py --dataset NormanWeissman2019_filtered [--min-cells 50]"""
import argparse
from pathlib import Path

from vcb import DATA
from vcb.data.pert_items import build_items

ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True, help="scPerturb file stem")
ap.add_argument("--group", default="scperturb")
ap.add_argument("--min-cells", type=int, default=50)
ap.add_argument("--cells-per-condition", type=int, default=500)
ap.add_argument("--gene-chunk", type=int, default=2000)
ap.add_argument("--h5ad", default=None, help="explicit path (skips the registry .ok check)")
ap.add_argument("--pert-col", default=None, help="generic mode: obs column with the perturbation label")
ap.add_argument("--control-label", default=None)
ap.add_argument("--context-col", default=None, help="generic mode: context column(s), '|'-joined for combinations")
ap.add_argument("--pert-type", default="cytokine")
ap.add_argument("--dose-col", default=None)
a = ap.parse_args()

if a.h5ad:
    raw = Path(a.h5ad)
else:
    raw = DATA / "raw" / a.group / f"{a.dataset}.h5ad"
    assert (raw.with_suffix(".h5ad.ok")).exists(), f"{raw} not verified yet"
kw = {}
if a.pert_col:
    from vcb.data.schema import make_generic_harmonizer
    kw["harmonizer"] = make_generic_harmonizer(a.pert_col, a.control_label, a.context_col, a.pert_type, a.dose_col)
build_items(raw, a.dataset, DATA / "items", min_cells=a.min_cells, cells_per_condition=a.cells_per_condition, gene_chunk=a.gene_chunk, **kw)

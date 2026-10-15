#!/usr/bin/env python
"""python scripts/run_repr_pool.py --panel data/panels/ts2_panel_v0.h5ad --run repr_pool_v0"""
import argparse
from pathlib import Path

from vcb import RUNS
from vcb.repr.run import evaluate_panel

ap = argparse.ArgumentParser()
ap.add_argument("--panel", required=True)
ap.add_argument("--run", default="repr_pool_v0")
ap.add_argument("--n-hvg", type=int, default=2000)
a = ap.parse_args()
evaluate_panel(Path(a.panel), RUNS / a.run, n_hvg=a.n_hvg)

#!/usr/bin/env python
"""python scripts/build_repr_panel.py [--test-cap 50 --train-cap 200]  (uses all verified TS2 files)"""
import argparse
from pathlib import Path

from vcb import DATA
from vcb.data.repr_panel import build_panel

ap = argparse.ArgumentParser()
ap.add_argument("--test-cap", type=int, default=50)
ap.add_argument("--train-cap", type=int, default=200)
ap.add_argument("--min-stratum", type=int, default=20)
ap.add_argument("--out", default=str(DATA / "panels" / "ts2_panel_v0.h5ad"))
ap.add_argument("--only", default=None, help="comma-separated tissue prefixes (debug)")
a = ap.parse_args()

raw = DATA / "raw" / "tabula_sapiens_v2"
files = sorted(p for p in raw.glob("*.h5ad") if p.with_suffix(".h5ad.ok").exists())
if a.only:
    files = [p for p in files if p.name.split("_")[0] in a.only.split(",")]
print(f"{len(files)} verified tissue files")
build_panel(files, Path(a.out), test_cap=a.test_cap, train_cap=a.train_cap, min_stratum=a.min_stratum)

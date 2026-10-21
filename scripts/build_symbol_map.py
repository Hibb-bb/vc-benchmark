#!/usr/bin/env python
"""Symbol -> Ensembl gene id map, built from the var tables of the local panels that carry both.

Used by scripts/extract_fm_embedding.py as a fallback for panels whose var has symbols only (Parse 10M PBMC),
so that Ensembl-tokenised foundation models (CellPLM, TranscriptFormer, Geneformer, scPRINT) can map genes
offline. Output: src/vcb/data/symbol_to_ensembl.tsv.gz (committed; ~60k symbols).

  python scripts/build_symbol_map.py
"""
import gzip
from pathlib import Path

import h5py

from vcb import DATA

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "vcb" / "data" / "symbol_to_ensembl.tsv.gz"


def read_col(v, key):
    e = v[key]
    if isinstance(e, h5py.Dataset):
        return [x.decode() if isinstance(x, bytes) else str(x) for x in e[:]]
    cats = [c.decode() if isinstance(c, bytes) else str(c) for c in e["categories"][:]]
    return [cats[i] for i in e["codes"][:]]


m: dict[str, str] = {}
for path in sorted((DATA / "panels").glob("*.h5ad")):
    with h5py.File(path) as f:
        v = f["var"]
        if "ensembl_id" not in v:
            continue
        names = read_col(v, v.attrs["_index"])
        ens = read_col(v, "ensembl_id")
    n0 = len(m)
    for s, e in zip(names, ens):
        if e.startswith("ENSG") and s and not s.startswith("ENSG"):
            m.setdefault(s, e.split(".")[0])
    print(f"{path.name:40s} +{len(m) - n0:6d} -> {len(m)}", flush=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
with gzip.open(OUT, "wt") as fh:
    fh.write("symbol\tensembl_id\n")
    for s, e in sorted(m.items()):
        fh.write(f"{s}\t{e}\n")
print(f"wrote {OUT} ({len(m)} symbols)")

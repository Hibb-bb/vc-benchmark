#!/usr/bin/env python
"""Full-cell training and query files for one fold of the faithful STATE (ST) rerun on Parse.

  .venv/bin/python scripts/state_full_fold_data.py --fold 0 [--debug]     # Slurm, ~2-3 h, ~40 GB out

Reads the full 9.7M-cell Parse file once and writes, under cache/statetx_full/fold<k>/:
- data/train.h5ad: every treated cell of every *training* item of the fold (unseen-combination folds of
  vcb.pert.folds), plus every untreated (PBS) cell of the 169 donor x cell type contexts; no cell of a test
  item. X = log1p counts-per-10k (normalised over all genes) restricted to the benchmark's 2,000 HVGs, stored
  CSR (31% non-zero, ~40 GB); obs: cytokine, cell_type (18 types), donor.
- query.h5ad: for every test item, up to --pred-cells untreated cells of its donor and cell type, once labelled
  with the item's cytokine and once as PBS (STATE is read through its own contrast). obs: cytokine, cell_type,
  donor, item_id.
Files are written incrementally (CSR with 64-bit row pointers, appended block by block), so memory stays bounded.
"""
import argparse
import time
from pathlib import Path

import anndata as ad
import h5py
import numpy as np
import pandas as pd
import scipy.sparse as sp
from anndata.experimental import sparse_dataset, write_elem

from vcb import DATA
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--pred-cells", type=int, default=512)
ap.add_argument("--chunk", type=int, default=200_000)
ap.add_argument("--debug", action="store_true", help="first 3 donors only")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
DS = "parse_pbmc_cytokines"
OUT = ROOT / "cache" / "statetx_full" / f"fold{a.fold}{'_debug' if a.debug else ''}"
(OUT / "data").mkdir(parents=True, exist_ok=True)

items = ad.read_h5ad(DATA / "items" / f"{DS}.items.h5ad")
meta, _, _ = item_table(items)
hv_genes = items.var_names[hvg_mask(items)].astype(str)
del items
tr, te = {f: (t, e) for f, t, e in fold_splits(meta, "context", 5)}[a.fold]
key = meta["perturbation"].astype(str) + "::" + meta["context"].astype(str)
train_keys, test_keys = set(key.iloc[tr]), set(key.iloc[te])
test_items = pd.Series(meta.index[te], index=key.iloc[te].values)          # key -> item_id
contexts = set(meta["context"].astype(str))
log(f"fold {a.fold}: {len(train_keys)} training items, {len(test_keys)} test items")

raw = ad.read_h5ad(DATA / "raw" / "parse_pbmc" / "20260203_Parse_10M_PBMC_cytokines.h5ad", backed="r")
gpos = pd.Index(raw.var_names.astype(str)).get_indexer(hv_genes)
assert (gpos >= 0).all()
obs = raw.obs
ct = obs["cell_type"].astype(str).str.replace("/", "-", regex=False).values
donor = obs["donor"].astype(str).values
cyt = obs["cytokine"].astype(str).values
ctx = np.char.add(np.char.add(donor.astype("U"), "|"), ct.astype("U"))
k_all = np.char.add(np.char.add(cyt.astype("U"), "::"), ctx)
in_ctx = np.isin(ctx, list(contexts))
is_ctrl = (cyt == "PBS") & in_ctx
is_train = np.isin(k_all, list(train_keys))
keep = is_ctrl | is_train
if a.debug:
    keep &= np.isin(donor, ["Donor1", "Donor2", "Donor3"])
log(f"training file: {int(keep.sum())} cells ({int((keep & is_ctrl).sum())} controls)")

# controls kept for the query: up to pred-cells per context, chosen now so the query can be written in the same pass
rng = np.random.default_rng(a.fold)
ctrl_idx = np.where(is_ctrl)[0]
ctrl_by_ctx = pd.Series(ctrl_idx).groupby(ctx[ctrl_idx]).apply(lambda s: np.sort(rng.choice(s.values, min(a.pred_cells, len(s)), replace=False)))
need_ctx = {k.split("::", 1)[1] for k in test_keys}
q_cells = np.sort(np.concatenate([ctrl_by_ctx[c] for c in need_ctx if c in ctrl_by_ctx.index]))
q_pos = {c: i for i, c in enumerate(q_cells)}
Q = np.zeros((len(q_cells), len(gpos)), dtype=np.float32)

train_path = OUT / "data" / "train.h5ad"


def append_csr(fh, block):
    """Append rows to an on-disk CSR X with 64-bit row pointers (a full fold holds ~6e9 non-zeros, past
    int32; anndata's writer would downcast them). Encoding attributes follow the h5ad CSR spec."""
    if "X" not in fh:
        g = fh.create_group("X")
        g.attrs["encoding-type"] = "csr_matrix"; g.attrs["encoding-version"] = "0.1.0"
        g.attrs["shape"] = np.array([0, block.shape[1]], dtype=np.int64)
        g.create_dataset("data", shape=(0,), maxshape=(None,), dtype=np.float32, chunks=(1 << 20,))
        g.create_dataset("indices", shape=(0,), maxshape=(None,), dtype=np.int32, chunks=(1 << 20,))
        g.create_dataset("indptr", data=np.zeros(1, dtype=np.int64), maxshape=(None,), chunks=(1 << 16,))
    g = fh["X"]
    n0, nnz0 = int(g.attrs["shape"][0]), int(g["indptr"][-1])
    d, ind, ptr = g["data"], g["indices"], g["indptr"]
    d.resize((nnz0 + block.nnz,)); d[nnz0:] = block.data.astype(np.float32)
    ind.resize((nnz0 + block.nnz,)); ind[nnz0:] = block.indices.astype(np.int32)
    ptr.resize((n0 + block.shape[0] + 1,)); ptr[n0 + 1:] = block.indptr[1:].astype(np.int64) + nnz0
    g.attrs["shape"] = np.array([n0 + block.shape[0], block.shape[1]], dtype=np.int64)
rows_out = []
with h5py.File(train_path, "w") as fh:
    n_rows = 1_600_000 if a.debug else raw.n_obs          # debug: the first 1.6M cells only
    for i0 in range(0, n_rows, a.chunk):
        i1 = min(i0 + a.chunk, n_rows)
        sel = np.where(keep[i0:i1])[0]
        qs = q_cells[(q_cells >= i0) & (q_cells < i1)]
        if len(sel) == 0 and len(qs) == 0:
            continue
        need = np.union1d(sel, qs - i0)
        X = sp.csr_matrix(raw.X[i0:i1])[need]
        tot = np.asarray(X.sum(1)).ravel(); tot[tot == 0] = 1
        Xh = sp.diags((1e4 / tot).astype(np.float32)) @ X[:, gpos]
        Xh.data = np.log1p(Xh.data)
        Xh = sp.csr_matrix(Xh, dtype=np.float32)
        loc = pd.Index(need)
        if len(sel):
            block = Xh[loc.get_indexer(sel)]
            append_csr(fh, block)
            rows_out.append(i0 + sel)
        if len(qs):
            Q[[q_pos[c] for c in qs]] = Xh[loc.get_indexer(qs - i0)].toarray()
        log(f"rows {i1}/{raw.n_obs}")
    rows = np.concatenate(rows_out)
    tobs = pd.DataFrame({"cytokine": cyt[rows], "cell_type": ct[rows], "donor": donor[rows]}, index=obs.index[rows].astype(str))
    for c in tobs.columns:
        tobs[c] = tobs[c].astype("category")
    write_elem(fh, "obs", tobs)
    write_elem(fh, "var", pd.DataFrame(index=pd.Index(hv_genes, name=None)))
    for k in ("obsm", "varm", "obsp", "varp", "layers", "uns"):
        write_elem(fh, k, {})
    fh.attrs["encoding-type"] = "anndata"; fh.attrs["encoding-version"] = "0.1.0"
import subprocess, sys  # noqa: E401
subprocess.run([sys.executable, str(ROOT / "scripts" / "state_repack_csr.py"), str(train_path)], check=True)
log(f"wrote {train_path} ({train_path.stat().st_size / 1e9:.1f} GB, {len(rows)} cells), repacked contiguous")

# query: each test item's context controls, labelled with the item's cytokine and as PBS
qrows, qobs = [], []
for k, iid in test_items.items():
    c = k.split("::", 1)[1]
    if c not in ctrl_by_ctx.index:
        continue
    idx = [q_pos[x] for x in ctrl_by_ctx[c]]
    d, t = c.split("|", 1)
    qrows.append(idx); qobs.append(pd.DataFrame({"cytokine": k.split("::", 1)[0], "cell_type": t, "donor": d, "item_id": iid}, index=range(len(idx))))
for c in sorted(need_ctx):
    if c in ctrl_by_ctx.index:
        idx = [q_pos[x] for x in ctrl_by_ctx[c]]
        d, t = c.split("|", 1)
        qrows.append(idx); qobs.append(pd.DataFrame({"cytokine": "PBS", "cell_type": t, "donor": d, "item_id": "control::" + c}, index=range(len(idx))))
qo = pd.concat(qobs, ignore_index=True)
qo.index = [f"q{i}" for i in range(len(qo))]
qa = ad.AnnData(X=sp.csr_matrix(Q[np.concatenate(qrows)]), obs=qo, var=pd.DataFrame(index=pd.Index(hv_genes, name=None)))
qa.write_h5ad(OUT / "query.h5ad")
log(f"wrote query.h5ad {qa.shape}")

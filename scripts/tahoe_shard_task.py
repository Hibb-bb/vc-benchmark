#!/usr/bin/env python
"""Stream a contiguous range of Tahoe-100M expression shards from HuggingFace and reduce them.

  python scripts/tahoe_shard_task.py --task 0 --n-tasks 48 [--shards 3388] [--debug-local shard.parquet]

Per task, for every cell: condition key = sample|cell_line_id, log1p(CP10k) over the full
token space; accumulate per-condition sums and counts, per-cell-line control sums of
squares, and a reservoir of raw-count cells (30 per condition, 1000 per control line).
Shards are downloaded to a scratch dir and deleted after use. Output:
data/raw/tahoe/parts/task_<i>.npz and task_<i>.cells.h5ad.
"""
from __future__ import annotations

import argparse
import os
import shutil
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import scipy.sparse as sp

from vcb import DATA

REPO = "tahoebio/Tahoe-100M"
N_TOKENS = 62720  # token ids observed <= 62624; gene_metadata has 62710 genes (ids start at 3)
CONTROL_DRUG = "DMSO_TF"

ap = argparse.ArgumentParser()
ap.add_argument("--task", type=int, required=True)
ap.add_argument("--n-tasks", type=int, default=48)
ap.add_argument("--shards", type=int, default=3388)
ap.add_argument("--cells-per-condition", type=int, default=30)
ap.add_argument("--cells-per-control", type=int, default=1000)
ap.add_argument("--debug-local", default=None, help="process one local parquet instead of downloading")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)

out_dir = DATA / "raw" / "tahoe" / "parts"
out_dir.mkdir(parents=True, exist_ok=True)
tag = f"task_{a.task}" if not a.debug_local else "debug"
scratch = Path(os.environ.get("TMPDIR", f"/tmp/{os.environ.get('USER','u')}")) / f"tahoe_{tag}"
scratch.mkdir(parents=True, exist_ok=True)

# accumulators (dense per condition, grown in blocks)
cond_index: dict[str, int] = {}
BLOCK = 2048
S = np.zeros((BLOCK, N_TOKENS), dtype=np.float32)
N = np.zeros(BLOCK, dtype=np.int64)
cond_meta: list[tuple] = []  # (sample, cell_line_id, drug, plate)
ctrl_sq: dict[str, np.ndarray] = {}
reservoir: dict[int, list] = {}      # cond idx -> list of (indices, data) raw cells
seen: dict[int, int] = {}            # cond idx -> cells seen (for reservoir sampling)
res_meta: dict[int, list] = {}       # cond idx -> list of barcodes
rng = np.random.default_rng(a.task)


def cond_id(key, meta):
    global S, N
    i = cond_index.get(key)
    if i is None:
        i = len(cond_index)
        cond_index[key] = i
        cond_meta.append(meta)
        if i >= S.shape[0]:
            S = np.vstack([S, np.zeros((BLOCK, N_TOKENS), dtype=np.float32)])
            N = np.concatenate([N, np.zeros(BLOCK, dtype=np.int64)])
    return i


def process_table(tbl):
    df = tbl.to_pandas()
    genes = df["genes"].values
    exprs = df["expressions"].values
    n = len(df)
    # build CSR (drop the leading marker token)
    lens = np.array([len(g) - 1 for g in genes])
    indptr = np.concatenate([[0], np.cumsum(lens)])
    indices = np.concatenate([np.asarray(g[1:], dtype=np.int32) for g in genes])
    data = np.concatenate([np.asarray(e[1:], dtype=np.float32) for e in exprs])
    X = sp.csr_matrix((data, indices, indptr), shape=(n, N_TOKENS))
    tot = np.asarray(X.sum(1)).ravel()
    tot[tot == 0] = 1
    Xn = sp.diags((1e4 / tot).astype(np.float32)) @ X
    Xn.data = np.log1p(Xn.data)
    Xn = Xn.tocsr()
    keys = (df["sample"].astype(str) + "|" + df["cell_line_id"].astype(str)).values
    drugs = df["drug"].astype(str).values
    lines = df["cell_line_id"].astype(str).values
    plates = df["plate"].astype(str).values
    codes = np.array([cond_id(k, (df["sample"].iat[r], lines[r], drugs[r], plates[r])) for r, k in enumerate(keys)])
    uniq = np.unique(codes)
    ind = sp.csr_matrix((np.ones(n, dtype=np.float32), (codes, np.arange(n))), shape=(S.shape[0], n))
    S[uniq] += (ind[uniq] @ Xn).toarray()
    N[:] += np.bincount(codes, minlength=S.shape[0])[: len(N)]
    is_ctrl = drugs == CONTROL_DRUG
    for line in np.unique(lines[is_ctrl]):
        m = is_ctrl & (lines == line)
        Xc = Xn[m]
        ctrl_sq[line] = ctrl_sq.get(line, np.zeros(N_TOKENS, dtype=np.float64)) + np.asarray(Xc.multiply(Xc).sum(0)).ravel()
    # reservoir sampling of raw cells
    bc = df["BARCODE_SUB_LIB_ID"].astype(str).values
    for r in range(n):
        c = codes[r]
        cap = a.cells_per_control if is_ctrl[r] else a.cells_per_condition
        k = seen.get(c, 0)
        lst = reservoir.setdefault(c, [])
        if k < cap:
            lst.append((X.indices[X.indptr[r]:X.indptr[r + 1]].copy(), X.data[X.indptr[r]:X.indptr[r + 1]].copy()))
            res_meta.setdefault(c, []).append(bc[r])
        else:
            j = rng.integers(0, k + 1)
            if j < cap:
                lst[j] = (X.indices[X.indptr[r]:X.indptr[r + 1]].copy(), X.data[X.indptr[r]:X.indptr[r + 1]].copy())
                res_meta[c][j] = bc[r]
        seen[c] = k + 1
    return n


if a.debug_local:
    files = [Path(a.debug_local)]
else:
    from huggingface_hub import hf_hub_download
    per = int(np.ceil(a.shards / a.n_tasks))
    my = list(range(a.task * per, min((a.task + 1) * per, a.shards)))
    log(f"task {a.task}: shards {my[0]}..{my[-1]} ({len(my)})")
    files = my

n_cells = 0
for k, f in enumerate(files):
    if isinstance(f, int):
        name = f"data/train-{f:05d}-of-03388.parquet"
        for attempt in range(6):
            try:
                path = Path(hf_hub_download(REPO, name, repo_type="dataset", cache_dir=str(scratch), local_dir=str(scratch)))
                break
            except Exception as e:  # noqa
                log(f"  download retry {attempt+1} for {name}: {type(e).__name__}")
                time.sleep(20 * (attempt + 1))
        else:
            raise SystemExit(f"could not download {name}")
    else:
        path = f
    pf = pq.ParquetFile(path)
    for rg in range(pf.metadata.num_row_groups):
        n_cells += process_table(pf.read_row_group(rg))
    if isinstance(f, int):
        path.unlink(missing_ok=True)
    if k % 5 == 0 or k == len(files) - 1:
        log(f"  shard {k+1}/{len(files)}  cells {n_cells}  conditions {len(cond_index)}")

n_cond = len(cond_index)
keys = list(cond_index)
meta = pd.DataFrame(cond_meta, columns=["sample", "cell_line_id", "drug", "plate"], index=keys)
np.savez_compressed(out_dir / f"{tag}.npz", keys=np.array(keys), S=S[:n_cond], N=N[:n_cond], ctrl_lines=np.array(list(ctrl_sq)), ctrl_sq=np.stack([ctrl_sq[l] for l in ctrl_sq]) if ctrl_sq else np.zeros((0, N_TOKENS)), n_cells=n_cells)
meta.to_parquet(out_dir / f"{tag}.meta.parquet")
# reservoir cells -> sparse h5ad
rows, cols, vals, obs_key, obs_bc = [], [], [], [], []
r = 0
for c, lst in reservoir.items():
    for (ix, dt), bc in zip(lst, res_meta[c]):
        rows.append(np.full(len(ix), r)); cols.append(ix); vals.append(dt); obs_key.append(keys[c]); obs_bc.append(bc); r += 1
Xc = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(r, N_TOKENS)) if r else sp.csr_matrix((0, N_TOKENS))
cells = ad.AnnData(X=Xc, obs=pd.DataFrame({"cond_key": obs_key, "barcode": obs_bc}, index=[f"{tag}:{i}" for i in range(r)]))
cells.obs = cells.obs.join(meta, on="cond_key")
cells.write_h5ad(out_dir / f"{tag}.cells.h5ad")
shutil.rmtree(scratch, ignore_errors=True)
log(f"done: {n_cells} cells, {n_cond} conditions, {r} reservoir cells -> {out_dir}/{tag}.*")

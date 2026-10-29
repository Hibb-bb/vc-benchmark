#!/usr/bin/env python
"""Train a STATE transition model (arc-state `state tx`) on one fold of a perturbation dataset and write
predicted deltas for the fold's test items, in the format `append_pert_scores.py` reads.

  python scripts/run_state_tx.py --dataset parse_pbmc_cytokines --fold 0 [--model state] [--max-steps 20000] [--debug]

Runs in this repo's .venv (numpy, anndata) and shells out to `state` in the scfm-irt STATE venv
(STATE_BIN, default ../scfm-irt/.venv-state/bin/state). Protocol, matching scGen's:

- the exact folds of the classical pool (vcb.pert.folds, unseen-combination scheme "context"): a test
  item's cytokine was seen in other contexts and its context with other cytokines, never the pair;
- training cells: every stored cell of every *training* item plus all control cells; no cell of a
  test item is written to the training file;
- expression: log1p CP10k over all genes, restricted to the benchmark's 2,000 HVGs (vcb.pert.run.hvg_mask),
  stored as obsm["X_hvg"]; STATE models the HVG space directly (embed_key=X_hvg);
- prediction: for each test item, control cells of its context relabelled with the item's cytokine go
  through `state tx infer`; the item's predicted delta on HVGs is the mean predicted expression minus
  the context's control mean, and genes outside the HVGs get the training fold's mean shift (as scGen).

`--model` picks any model config shipped with arc-state (state, state_sm, cpa, scvi, perturb_mean,
context_mean, ...); the respondent id is `statetx_<model>` unless --respondent is given.
Only the unseen-combination scheme is supported: one-hot perturbations cannot represent a cytokine
that never appears in training.
"""
import argparse
import os
import shutil
import subprocess
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

from vcb import DATA, RUNS
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", default="parse_pbmc_cytokines")
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--model", default="state")
ap.add_argument("--respondent", default=None)
ap.add_argument("--max-steps", type=int, default=20000)
ap.add_argument("--batch-size", type=int, default=16)
ap.add_argument("--cell-set-len", type=int, default=None, help="override model.kwargs.cell_set_len")
ap.add_argument("--pred-cells", type=int, default=64, help="control cells relabelled per test item")
ap.add_argument("--debug", action="store_true", help="few contexts, 200 steps: checks the code path")
ap.add_argument("--work", default=None)
ap.add_argument("--infer-only", action="store_true", help="skip training; predict from the run's best.ckpt (e.g. after a time-limit kill)")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
resp = a.respondent or f"statetx_{a.model}"
STATE = os.environ.get("STATE_BIN", str(ROOT.parent / "scfm-irt" / ".venv-state" / "bin" / "state"))
work = Path(a.work or ROOT / "cache" / "statetx" / f"{resp}_{a.dataset}_fold{a.fold}{'_debug' if a.debug else ''}")
if a.infer_only:
    assert (work / "run" / "checkpoints").exists(), f"no checkpoints under {work}"
else:
    if work.exists():
        shutil.rmtree(work)
    (work / "data").mkdir(parents=True)

items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
meta, D, ctrl_rows = item_table(items)
X_items = np.asarray(items.X)
hv = hvg_mask(items)
hv_idx = np.where(hv)[0]
genes = items.var_names[hv_idx].astype(str)
tr, te = {f: (t, e) for f, t, e in fold_splits(meta, "context", a.folds)}[a.fold]
if a.debug:
    keep_ctx = set(meta["context"].astype(str).unique()[:6])
    tr = np.array([j for j in tr if meta["context"].iloc[j] in keep_ctx])
    te = np.array([j for j in te if meta["context"].iloc[j] in keep_ctx])[:40]
log(f"{a.dataset} fold {a.fold}: {len(tr)} train items, {len(te)} test items, {len(hv_idx)} HVGs, model {a.model}")

cells_b = ad.read_h5ad(DATA / "items" / f"{a.dataset}.cells.h5ad", backed="r")
cobs = cells_b.obs
is_ctrl = cobs["is_control"].values.astype(bool)
cell_ctx = cobs["context"].astype(str).values
train_ids = set(meta.index[tr])
sel = np.where(is_ctrl | cobs["item_id"].astype(str).isin(train_ids).values)[0]
if a.debug:
    sel = sel[np.isin(cell_ctx[sel], list(keep_ctx))]
log(f"loading {len(sel)} training cells ({int(is_ctrl[sel].sum())} controls)")
Xraw = sp.csr_matrix(cells_b[np.sort(sel)].to_memory().X, dtype=np.float32)
sel = np.sort(sel)
tot = np.asarray(Xraw.sum(1)).ravel()
tot[tot == 0] = 1
Xh = sp.diags((1e4 / tot).astype(np.float32)) @ Xraw[:, hv_idx]
Xh.data = np.log1p(Xh.data)
Xh = np.asarray(Xh.todense(), dtype=np.float32)
del Xraw

def obs_frame(pert, ctx):
    ctx = pd.Series(ctx).astype(str)
    return pd.DataFrame({"pert": pd.Series(pert).astype(str).values, "cell_type": ctx.values,
                         "gem_group": ctx.str.split("|").str[0].values})

o = obs_frame(np.where(is_ctrl[sel], "control", cobs["perturbation"].astype(str).values[sel]), cell_ctx[sel])
o.index = cobs.index[sel].astype(str)
if not a.infer_only:
    train = ad.AnnData(X=sp.csr_matrix(Xh), obs=o, var=pd.DataFrame(index=genes))
    train.obsm["X_hvg"] = Xh
    train.write_h5ad(work / "data" / "train.h5ad")
    log(f"wrote training file {train.shape}")

# STATE needs a validation set: a few training (context, cytokine) pairs held back from its own fit
rng = np.random.default_rng(a.fold)
tr_meta = meta.iloc[tr]
val_ctx = rng.choice(tr_meta["context"].astype(str).unique(), size=min(8, tr_meta["context"].nunique()), replace=False)
toml = ['[datasets]', f'parse = "{work / "data"}"', "", "[training]", 'parse = "train"', ""]
for c in val_ctx:
    perts = tr_meta.loc[tr_meta["context"].astype(str) == c, "perturbation"].astype(str).unique()
    pick = rng.choice(perts, size=min(3, len(perts)), replace=False)
    toml += [f'[fewshot."parse.{c}"]', "val = [" + ", ".join(f'"{p}"' for p in pick) + "]", "test = []", ""]
(work / "split.toml").write_text("\n".join(toml))

steps = 200 if a.debug else a.max_steps
cmd = [STATE, "tx", "train",
       f"data.kwargs.toml_config_path={work / 'split.toml'}", "data.kwargs.embed_key=X_hvg",
       "data.kwargs.output_space=gene", "data.kwargs.pert_col=pert", "data.kwargs.cell_type_key=cell_type",
       "data.kwargs.batch_col=gem_group", "data.kwargs.control_pert=control", "data.kwargs.num_workers=4",
       f"training.max_steps={steps}", f"training.batch_size={a.batch_size}",
       f"training.val_freq={min(2000, max(steps // 4, 50))}", f"training.ckpt_every_n_steps={min(2000, max(steps // 4, 50))}",
       f"model={a.model}", "use_wandb=false", f"output_dir={work}", "name=run"]
if a.cell_set_len:
    cmd.append(f"model.kwargs.cell_set_len={a.cell_set_len}")
if a.infer_only:
    log("inference only: training skipped")
else:
    log("train: " + " ".join(cmd[2:]))
    subprocess.run(cmd, check=True, cwd=work)

# prediction input: controls of each test item's context, relabelled with the item's cytokine
ctrl_by_ctx = {c: np.where((o["pert"].values == "control") & (o["cell_type"].values == c))[0] for c in np.unique(o["cell_type"].values)}
rows, perts, ctxs, owner = [], [], [], []
for j in te:
    iid, c, p = meta.index[j], str(meta["context"].iloc[j]), str(meta["perturbation"].iloc[j])
    pool = ctrl_by_ctx.get(c, np.array([], int))
    if len(pool) == 0:
        continue
    pick = rng.choice(pool, size=min(a.pred_cells, len(pool)), replace=False)
    rows += list(pick); perts += [p] * len(pick); ctxs += [c] * len(pick); owner += [iid] * len(pick)
ctl_rows = np.concatenate([ctrl_by_ctx[c] for c in sorted(set(ctxs))])
Xin = np.vstack([Xh[rows], Xh[ctl_rows]])
oin = obs_frame(perts + ["control"] * len(ctl_rows), ctxs + list(o["cell_type"].values[ctl_rows]))
oin.index = [f"q{i}" for i in range(len(oin))]
query = ad.AnnData(X=sp.csr_matrix(Xin), obs=oin, var=pd.DataFrame(index=genes))
query.obsm["X_hvg"] = Xin
query.write_h5ad(work / "query.h5ad")
cmd = [STATE, "tx", "infer", "--model-dir", str(work / "run"), "--adata", str(work / "query.h5ad"),
       "--embed-key", "X_hvg", "--pert-col", "pert", "--celltype-col", "cell_type", "--batch-col", "gem_group",
       "--control-pert", "control", "--output", str(work / "pred.h5ad")]
ck = work / "run" / "checkpoints" / "best.ckpt"
if ck.exists():
    cmd += ["--checkpoint", str(ck)]
log("infer: " + " ".join(cmd[2:]))
subprocess.run(cmd, check=True, cwd=work)
pred_ad = ad.read_h5ad(work / "pred.h5ad")
P = np.asarray(pred_ad.obsm["X_hvg"] if "X_hvg" in pred_ad.obsm else pred_ad.X, dtype=np.float32)[: len(rows)]
log(f"predicted matrix {P.shape}; input mean {Xin[:len(rows)].mean():.3f}, predicted mean {P.mean():.3f}")

ms = D[tr].mean(0)
owner = np.asarray(owner)
preds, ids = [], []
for j in te:
    iid = meta.index[j]
    c = str(meta["context"].iloc[j])
    pred = ms.copy()
    m = owner == iid
    if m.any():
        pred[hv] = P[m].mean(0) - X_items[ctrl_rows[c]][hv]
    preds.append(pred.astype(np.float32)); ids.append(iid)
out = RUNS / "pert_pool_v0" / resp
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{a.dataset}.context.fold{a.fold}{'.debug' if a.debug else ''}.npz",
                    item_ids=np.array(ids), pred=np.stack(preds), n_train_cells=len(sel))
log(f"wrote {len(ids)} predictions to {out}")

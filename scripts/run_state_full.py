#!/usr/bin/env python
"""Faithful STATE (ST) rerun on Parse, one fold: train with Arc's ST-HVG-Parse settings, then predict.

  python scripts/run_state_full.py --fold 0 --stage train      # resumable: rerun to continue from last.ckpt
  python scripts/run_state_full.py --fold 0 --stage predict    # needs a finished run; writes the fold's npz

Data come from scripts/state_full_fold_data.py (every cell of every training item plus all PBS controls; no
cell of a test item). Settings follow Arc's released config for ST-HVG-Parse (huggingface.co/arcinstitute/
ST-HVG-Parse, fewshot/split_0/config.yaml): state model with hidden size 384, 8 llama layers, energy loss,
cell sets of 512, batch 32, lr 3e-4, weight decay 5e-4; context = cell type (18 types) with donor as the batch
column, perturbation = cytokine, control = PBS. Steps default to 80,000 (Arc used 300,000).

Prediction reads STATE through its own contrast: for each test item, mean predicted expression of its
context's control cells labelled with the cytokine, minus the mean prediction for the same cells labelled
PBS (STATE does not reproduce untreated cells exactly, so measuring against the input would add that drift).
Genes outside the HVGs get the training fold's mean shift, as for every other respondent.
"""
import argparse
import os
import shutil
import subprocess
import time
from pathlib import Path

import anndata as ad
import numpy as np

from vcb import DATA, RUNS
from vcb.pert.folds import fold_splits, item_table
from vcb.pert.run import hvg_mask

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--stage", choices=["train", "predict"], required=True)
ap.add_argument("--max-steps", type=int, default=80000)
ap.add_argument("--respondent", default="statetx_state_full")
ap.add_argument("--debug", action="store_true")
ap.add_argument("--keep-data", action="store_true", help="do not delete the training file after prediction")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
STATE = os.environ.get("STATE_BIN", str(ROOT.parent / "scfm-irt" / ".venv-state" / "bin" / "state"))
W = ROOT / "cache" / "statetx_full" / f"fold{a.fold}{'_debug' if a.debug else ''}"
steps = 300 if a.debug else a.max_steps

if a.stage == "train" and (W / "TRAINED").exists():
    log("training already finished for this fold; nothing to do")
elif a.stage == "train":
    assert (W / "data" / "train.h5ad").exists(), f"build the data first: scripts/state_full_fold_data.py --fold {a.fold}"
    # STATE needs a validation set: a few (cell type, cytokine) pairs held back from its own fit
    (W / "split.toml").write_text("\n".join([
        "[datasets]", f'parse = "{W / "data"}"', "", "[training]", 'parse = "train"', "",
        '[fewshot."parse.CD4 Memory"]', 'val = ["IL-2", "IFN-gamma"]', "test = []", "",
        '[fewshot."parse.CD14 Mono"]', 'val = ["IL-6", "TNF-alpha"]', "test = []", ""]))
    cmd = [STATE, "tx", "train",
           f"data.kwargs.toml_config_path={W / 'split.toml'}", "data.kwargs.embed_key=null", "data.kwargs.output_space=gene",
           "data.kwargs.pert_col=cytokine", "data.kwargs.cell_type_key=cell_type", "data.kwargs.batch_col=donor",
           "data.kwargs.control_pert=PBS", "data.kwargs.num_workers=8",
           "model=state", "model.kwargs.hidden_dim=384", "model.kwargs.transformer_backbone_kwargs.hidden_size=384",
           "model.kwargs.cell_set_len=512",
           f"training.max_steps={steps}", "training.batch_size=32", "training.lr=0.0003", "training.weight_decay=0.0005",
           # validate every 2,000 steps on 10% of the held-back cells: at every 1,000 steps on all 321k cells, validation
           # took longer than training itself (training runs at ~7 steps/s on an A100)
           f"training.val_freq={min(2000, max(steps // 4, 50))}", f"training.ckpt_every_n_steps={min(4000, max(steps // 4, 50))}",
           "data.kwargs.val_subsample_fraction=0.1",
           "use_wandb=false", f"output_dir={W}", "name=run"]
    log(("resuming from last.ckpt: " if (W / "run" / "checkpoints" / "last.ckpt").exists() else "training: ") + " ".join(cmd[2:]))
    subprocess.run(cmd, check=True, cwd=W)
    (W / "TRAINED").write_text(f"{steps}\n")
    log("training finished")

else:
    assert (W / "TRAINED").exists(), "training has not finished"
    ck = W / "run" / "checkpoints" / "best.ckpt"
    cmd = [STATE, "tx", "infer", "--model-dir", str(W / "run"), "--adata", str(W / "query.h5ad"),
           "--pert-col", "cytokine", "--celltype-col", "cell_type", "--batch-col", "donor", "--control-pert", "PBS",
           "--output", str(W / "pred.h5ad")] + (["--checkpoint", str(ck)] if ck.exists() else [])
    log("infer: " + " ".join(cmd[2:]))
    # our own checkpoints store NumPy scalars (best validation score); allow exactly those types in torch's
    # weights-only loader (cache/statetx_full/pyhooks/sitecustomize.py) rather than disabling it
    env = dict(os.environ, PYTHONPATH=str(ROOT / "cache" / "statetx_full" / "pyhooks") + os.pathsep + os.environ.get("PYTHONPATH", ""))
    subprocess.run(cmd, check=True, cwd=W, env=env)
    q = ad.read_h5ad(W / "query.h5ad", backed="r").obs
    pr = ad.read_h5ad(W / "pred.h5ad")
    P = pr.X.toarray() if hasattr(pr.X, "toarray") else np.asarray(pr.X)
    P = np.asarray(P, dtype=np.float32)
    grp = q.reset_index(drop=True).groupby("item_id", observed=True).indices
    items = ad.read_h5ad(DATA / "items" / "parse_pbmc_cytokines.items.h5ad")
    meta, D, _ = item_table(items)
    hv = hvg_mask(items)
    tr, te = {f: (t, e) for f, t, e in fold_splits(meta, "context", 5)}[a.fold]
    ms = D[tr].mean(0)
    preds, ids, n_pred = [], [], 0
    for j in te:
        iid = meta.index[j]
        c = str(meta["context"].iloc[j])
        p = ms.copy()
        if iid in grp and f"control::{c}" in grp:
            p[hv] = P[grp[iid]].mean(0) - P[grp[f"control::{c}"]].mean(0)
            n_pred += 1
        preds.append(p.astype(np.float32)); ids.append(iid)
    out = RUNS / "pert_pool_v0" / a.respondent
    out.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(out / f"parse_pbmc_cytokines.context.fold{a.fold}{'.debug' if a.debug else ''}.npz",
                        item_ids=np.array(ids), pred=np.stack(preds), steps=steps)
    log(f"wrote {len(ids)} predictions ({n_pred} from STATE) to {out}")
    if not a.keep_data and not a.debug:
        shutil.rmtree(W / "data", ignore_errors=True)
        for f in ("query.h5ad", "pred.h5ad"):
            (W / f).unlink(missing_ok=True)
        log("deleted the fold's training, query and prediction files (checkpoints kept)")

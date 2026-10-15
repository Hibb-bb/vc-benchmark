#!/usr/bin/env python
"""Train scVI on the train panel and embed train + test cells (component A respondent).

  .venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel data/panels/ts2_panel_v0.h5ad --latent 30 --batch tissue

Protocol matches the classical pool: fit on train cells only, transform test cells with
the frozen model. HVGs: 2,000 seurat_v3 genes chosen on train counts. `--batch tissue`
uses a covariate present in both splits (donors are disjoint by design, so donor cannot be
the batch key without a query-mapping step). Output: cache/embeddings/<name>.npz with
obs_names and latent for train and test.
"""
import argparse
import time
from pathlib import Path

import anndata as ad
import numpy as np
import scanpy as sc
import scvi

from vcb import ROOT

ap = argparse.ArgumentParser()
ap.add_argument("--panel", required=True)
ap.add_argument("--latent", type=int, default=30)
ap.add_argument("--batch", default="tissue", help="obs column or 'none'")
ap.add_argument("--n-hvg", type=int, default=2000)
ap.add_argument("--max-epochs", type=int, default=None)
ap.add_argument("--debug", action="store_true")
ap.add_argument("--out-name", default=None, help="cache file name (default scvi_k<latent>_b<batch>)")
a = ap.parse_args()
t0 = time.time()
scvi.settings.seed = 0

panel = ad.read_h5ad(a.panel)
tr = (panel.obs["split"] == "train").values
te = (panel.obs["split"] == "test").values
if a.debug:
    rng = np.random.default_rng(0)
    tr = tr & (rng.random(len(tr)) < 0.03)
    te = te & (rng.random(len(te)) < 0.05)
train = panel[tr].copy()
test = panel[te].copy()
sc.pp.highly_variable_genes(train, n_top_genes=a.n_hvg, flavor="seurat_v3", subset=False)
hv = train.var["highly_variable"].values
train = train[:, hv].copy()
test = test[:, hv].copy()
batch = None if a.batch == "none" else a.batch
scvi.model.SCVI.setup_anndata(train, batch_key=batch)
model = scvi.model.SCVI(train, n_latent=a.latent, n_layers=2, gene_likelihood="nb")
model.train(max_epochs=2 if a.debug else a.max_epochs, early_stopping=True)
print(f"trained in {time.time()-t0:.0f}s; epochs {len(model.history['elbo_train'])}", flush=True)
Z_tr = model.get_latent_representation(train)
# test cells may carry batch categories absent from train (donor-disjoint panel); the
# encoder does not use the batch covariate (encode_covariates=False), so extending the
# category set is safe for latent extraction.
model._register_manager_for_instance(model.adata_manager.transfer_fields(test, extend_categories=True))
Z_te = model.get_latent_representation(test)
name = a.out_name or (f"scvi_k{a.latent}_b{a.batch}" + ("_debug" if a.debug else ""))
out = ROOT / "cache" / "embeddings"
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{name}.npz", train_ids=train.obs_names.values, Z_train=Z_tr.astype(np.float32), test_ids=test.obs_names.values, Z_test=Z_te.astype(np.float32))
print(f"wrote {out / name}.npz  train {Z_tr.shape} test {Z_te.shape}  {time.time()-t0:.0f}s", flush=True)

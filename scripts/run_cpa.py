#!/usr/bin/env python
"""CPA (Lotfollahi et al. 2023, cpa-tools 0.8.8) on one benchmark fold, with its own perturbation embedding or a
frozen text-card embedding.

  .venv-cpa/bin/python scripts/run_cpa.py --dataset NormanWeissman2019_filtered --scheme perturbation --fold 0 --emb learned
  .venv-cpa/bin/python scripts/run_cpa.py --dataset immune_dictionary --scheme context --fold 0 --emb text \
      --text-dir runs/pert_text/idict/emb

--emb learned: CPA's default, one trainable embedding per perturbation (an unseen perturbation keeps its random
initialisation; a combination of seen genes is the sum of their embeddings, as in the CPA paper).
--emb text: the perturbation's full Qwen3-Embedding-4B text card (2,560 numbers, unit length, no PCA) as a frozen
table, followed by a trained MLP (2,560 -> --proj-hidden -> CPA latent, ReLU) that maps the card into CPA's latent space.
cpa-tools 0.8.8 builds a linear map for its drug_embeddings but leaves it out of the optimizer (CPATrainingPlan only
optimizes pert_network.pert_embedding), so that map never trains; here the MLP sits inside pert_embedding, after the
frozen table, so the optimizer sees it, and CPA's own map is replaced by an identity.

Folds are the benchmark's (vcb.pert.folds). Training cells: up to --cells-per-item stored cells of every training item
plus all control cells; nothing from a test item. Genes: the benchmark's 2,000 HVGs, raw counts, NB likelihood.
Prediction: for each test item, the control cells of its context (up to --query-cells) are given the item's
perturbation, dose and covariates, and CPA predicts their expression; the predicted shift is the mean log1p CP10k of
those predictions minus the mean of the same cells predicted as control (CPA read through its own contrast). Genes
outside the HVGs get the training fold's mean shift. Output: <out>/<dataset>.<scheme>.fold<k>.npz (item_ids, pred).
Hyperparameters: the CPA tutorial settings (Norman / sciPlex), trained to early stopping.
"""
import argparse
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp
import torch

import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vcb.pert.folds import fold_splits, item_table  # noqa: E402
from vcb.pert.run import hvg_mask  # noqa: E402

DATA = ROOT / "data"
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--scheme", choices=["context", "perturbation"], required=True)
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--emb", choices=["learned", "text"], required=True)
ap.add_argument("--text-dir", default=str(ROOT / "runs" / "pert_text" / "emb"))
ap.add_argument("--text-model", default="Qwen3-Embedding-4B")
ap.add_argument("--proj-hidden", type=int, default=512)
ap.add_argument("--cells-per-item", type=int, default=200)
ap.add_argument("--query-cells", type=int, default=300)
ap.add_argument("--max-epochs", type=int, default=300)
ap.add_argument("--min-cells", type=int, default=50)
ap.add_argument("--out", default=str(ROOT / "runs" / "pert_text" / "cpa"))
ap.add_argument("--debug", action="store_true")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)
import cpa  # noqa: E402  (after argparse: importing cpa seeds and prints)

items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
meta, D, ctrl_rows = item_table(items)
hv = hvg_mask(items)
genes = items.var_names[hv].astype(str)
keep = meta["n_cells"].values >= a.min_cells if "n_cells" in meta else np.ones(len(meta), bool)
splits = {f: (tr, te) for f, tr, te in fold_splits(meta, a.scheme, 5)}
tr, te = splits[a.fold]
if a.debug:
    te = te[:8]
log(f"{a.dataset} {a.scheme} fold {a.fold} emb={a.emb}: {len(tr)} train items, {len(te)} test items")
del items

cells = ad.read_h5ad(DATA / "items" / f"{a.dataset}.cells.h5ad", backed="r")
co = cells.obs
gpos = pd.Index(cells.var_names.astype(str)).get_indexer(genes)
assert (gpos >= 0).all()
rng = np.random.default_rng(a.fold)
train_ids = set(meta.index[tr])
by_item = co.groupby("item_id", observed=True).indices
sel = [rng.choice(idx, min(a.cells_per_item, len(idx)), replace=False) for iid, idx in by_item.items() if iid in train_ids]
ctrl_idx = np.where(co["is_control"].values.astype(bool))[0]
sel = np.sort(np.concatenate(sel + [ctrl_idx]))
if a.debug:
    sel = np.sort(rng.choice(sel, min(6000, len(sel)), replace=False))
X = sp.csr_matrix(cells[sel].to_memory().X[:, gpos], dtype=np.float32)
o = co.iloc[sel]
log(f"training cells {X.shape}")

# ---- CPA labels: perturbation tokens (genes of a combination joined by '+'), doses, covariates ----
dataset_perts = meta["perturbation"].astype(str)
combo = a.dataset.startswith("NormanWeissman")
PLUS = "<plus>"                                          # CPA splits labels on '+'; some drug names contain it
def tokens(p):
    return [t.replace("+", PLUS) for t in (p.split("_") if combo else [p])]
def pert_label(p, is_ctrl):
    return "ctrl" if is_ctrl else "+".join(tokens(p))
dose_max = float(np.nanmax(meta["dose"].values)) if meta["dose"].notna().any() else 1.0
def dose_label(p, dose, is_ctrl):
    if is_ctrl:
        return "1.0"
    v = 1.0 if not np.isfinite(dose) or dose == 0 else float(dose) / dose_max
    return "+".join([f"{v:g}"] * len(tokens(p)))
use_time = meta["time_h"].nunique() > 1 if "time_h" in meta else False


def obs_frame(pert, dose, ctx, time_h, is_ctrl):
    df = pd.DataFrame({"condition": [pert_label(p, c) for p, c in zip(pert, is_ctrl)],
                       "dose_val": [dose_label(p, d, c) for p, d, c in zip(pert, dose, is_ctrl)],
                       "context": np.asarray(ctx, dtype=str)})
    if use_time:
        df["time"] = np.asarray(time_h).astype(str)
    return df


tobs = obs_frame(o["perturbation"].astype(str).values, o["dose"].astype(float).values, o["context"].astype(str).values,
                 o["time_h"].values if use_time else None, o["is_control"].values.astype(bool))
tobs["split"] = np.where(rng.random(len(tobs)) < 0.1, "valid", "train")

# ---- query cells: control cells of each test item's context, labelled with the item (and once as control) ----
ctrl_by_ctx = pd.Series(np.arange(len(o)))[o["is_control"].values.astype(bool)].groupby(o["context"].astype(str).values[o["is_control"].values.astype(bool)]).apply(np.asarray).to_dict()
qX, qobs, qitem = [], [], []
times = {}
for j in te:
    iid = meta.index[j]; c = str(meta["context"].iloc[j])
    if c not in ctrl_by_ctx:
        continue
    rows = ctrl_by_ctx[c]
    rows = rows if len(rows) <= a.query_cells else np.random.default_rng(j).choice(rows, a.query_cells, replace=False)
    th = meta["time_h"].iloc[j] if use_time else None
    times[c] = th
    for lab, is_c in ((iid, False), (f"control::{c}::{th}", True)):
        if is_c and lab in qitem:
            continue
        qX.append(X[rows])
        qobs.append(obs_frame([meta["perturbation"].iloc[j]] * len(rows), [meta["dose"].iloc[j]] * len(rows), [c] * len(rows),
                              [th] * len(rows), [is_c] * len(rows)))
        qitem += [lab] * len(rows)
Q = ad.AnnData(X=sp.vstack(qX).tocsr(), obs=pd.concat(qobs, ignore_index=True))
Q.obs["split"] = "ood"
T = ad.AnnData(X=X, obs=tobs.reset_index(drop=True))
A = ad.concat([T, Q], index_unique=None)
A.obs_names = [f"c{i}" for i in range(A.n_obs)]
A.var_names = genes
A.obs["item"] = [""] * T.n_obs + qitem
for c in A.obs.columns:
    if c not in ("item",):
        A.obs[c] = A.obs[c].astype("category")
log(f"anndata for CPA {A.shape}: {T.n_obs} training, {Q.n_obs} query cells")

covs = ["context"] + (["time"] if use_time else [])
cpa.CPA.setup_anndata(A, perturbation_key="condition", control_group="ctrl", dosage_key="dose_val",
                      categorical_covariate_keys=covs, is_count_data=True, max_comb_len=2 if combo else 1)

# CPA tutorial hyperparameters (Norman / sciPlex notebooks)
ae = {"n_latent": 64, "recon_loss": "nb", "doser_type": "logsigm" if dose_max > 1 else "linear",
      "n_hidden_encoder": 128, "n_layers_encoder": 2, "n_hidden_decoder": 512, "n_layers_decoder": 2,
      "use_batch_norm_encoder": True, "use_layer_norm_encoder": False, "use_batch_norm_decoder": False,
      "use_layer_norm_decoder": True, "dropout_rate_encoder": 0.0, "dropout_rate_decoder": 0.1,
      "variational": False, "seed": 6977}
plan = {"n_epochs_kl_warmup": None, "n_epochs_pretrain_ae": 30, "n_epochs_adv_warmup": 50, "n_epochs_mixup_warmup": 0,
        "mixup_alpha": 0.0, "adv_steps": None, "n_hidden_adv": 64, "n_layers_adv": 3, "use_batch_norm_adv": True,
        "use_layer_norm_adv": False, "dropout_rate_adv": 0.3, "reg_adv": 20.0, "pen_adv": 5.0, "lr": 0.0003,
        "wd": 4e-07, "adv_lr": 0.0003, "adv_wd": 4e-07, "adv_loss": "cce", "doser_lr": 0.0003, "doser_wd": 4e-07,
        "do_clip_grad": True, "gradient_clip_value": 1.0, "step_size_lr": 10}

if a.emb == "text":
    E = Path(a.text_dir)
    keys = (E / "keys.txt").read_text().splitlines()
    M = np.load(E / f"{a.text_model}.full.npy").astype(np.float32)
    kpos = {k: i for i, k in enumerate(keys)}
    ptype = str(meta["pert_type"].iloc[0])
    def vec(tok):
        tok = tok.replace(PLUS, "+")
        for t in ([ptype] + (["CRISPRi", "CRISPR_KO"] if ptype.startswith("CRISPR") else [])):
            if f"{t}::{tok}" in kpos:
                return M[kpos[f"{t}::{tok}"]]
        return None
    model_tokens = [t for t in cpa.CPA.pert_encoder.keys()]          # index order of CPA's perturbation table
    real = [t for t in model_tokens if t not in ("<PAD>",)]
    V = {t: vec(t) for t in real}
    missing = [t for t, v in V.items() if v is None]
    have = np.stack([v for v in V.values() if v is not None])
    k = have.shape[1]
    W = np.zeros((len(model_tokens), k), dtype=np.float32)
    for i, t in enumerate(model_tokens):
        if t in V and V[t] is not None:
            W[i] = V[t] / (np.linalg.norm(V[t]) + 1e-9)
    emb = torch.nn.Embedding(len(model_tokens), k, padding_idx=0)
    emb.weight.data.copy_(torch.tensor(W))
    emb.weight.requires_grad = False
    ae["drug_embeddings"] = emb
    log(f"text embedding table {W.shape}; tokens without a card (zero vector): {missing[:10]}{'...' if len(missing) > 10 else ''} ({len(missing)})")

model = cpa.CPA(A, split_key="split", train_split="train", valid_split="valid", test_split="ood", **ae)
if a.emb == "text":
    pn = model.module.pert_network
    mlp = torch.nn.Sequential(torch.nn.Linear(k, a.proj_hidden), torch.nn.ReLU(), torch.nn.Linear(a.proj_hidden, ae["n_latent"]))
    pn.pert_embedding = torch.nn.Sequential(pn.pert_embedding, mlp)   # frozen card table, then the trained MLP
    pn.pert_transformation = torch.nn.Identity()
    log(f"projection MLP {k} -> {a.proj_hidden} -> {ae['n_latent']}, trainable parameters "
        f"{sum(q.numel() for q in pn.pert_embedding.parameters() if q.requires_grad)}")
    w0 = mlp[0].weight.detach().clone()
    _conf = cpa._task.CPATrainingPlan.configure_optimizers
    def _conf_with_mlp(self):                     # put the MLP in the autoencoder optimizer if CPA left it out
        out = _conf(self)
        opt = (out[0] if isinstance(out, tuple) else out)[0]
        have_ids = {id(q) for g in opt.param_groups for q in g["params"]}
        extra = [q for q in mlp.parameters() if id(q) not in have_ids]
        if extra:
            opt.add_param_group({"params": extra, "lr": self.lr, "weight_decay": self.wd})
        log(f"projection MLP tensors added to the optimizer: {len(extra)}")
        return out
    cpa._task.CPATrainingPlan.configure_optimizers = _conf_with_mlp
model.train(max_epochs=3 if a.debug else a.max_epochs, use_gpu=torch.cuda.is_available(), batch_size=512,
            plan_kwargs=plan, early_stopping_patience=10, check_val_every_n_epoch=5,
            save_path=None)
log("trained")
if a.emb == "text":
    log(f"projection MLP first-layer weight change (relative): {float((mlp[0].weight.detach().cpu() - w0.cpu()).norm() / w0.norm()):.3f}")

qi = np.where(A.obs["split"].values == "ood")[0]
qA = A[qi].copy()
model.predict(qA, batch_size=2048)
P = np.asarray(qA.obsm["CPA_pred"])
P = np.log1p(P / np.maximum(P.sum(1, keepdims=True), 1e-9) * 1e4)    # predicted counts -> log1p CP10k over HVGs
qlab = A.obs["item"].values[qi]
grp = pd.Series(np.arange(len(qi))).groupby(qlab).apply(np.asarray).to_dict()
ms = D[tr].mean(0)
preds, ids, n_pred = [], [], 0
for j in te:
    iid = meta.index[j]; c = str(meta["context"].iloc[j])
    th = meta["time_h"].iloc[j] if use_time else None
    p = ms.copy()
    cl = f"control::{c}::{th}"
    if iid in grp and cl in grp:
        p[hv] = P[grp[iid]].mean(0) - P[grp[cl]].mean(0)
        n_pred += 1
    preds.append(p.astype(np.float32)); ids.append(iid)
out = Path(a.out) / f"cpa_{a.emb}"
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{a.dataset}.{a.scheme}.fold{a.fold}{'.debug' if a.debug else ''}.npz", item_ids=np.array(ids), pred=np.stack(preds))
log(f"wrote {len(ids)} predictions ({n_pred} from CPA) to {out}")

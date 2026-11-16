#!/usr/bin/env python
"""CellFlow (Klein et al. 2025, cellflow-tools 0.0.9, flow matching) on one benchmark fold, with a one-hot
perturbation representation or the text card.

  .venv-cellflow/bin/python scripts/run_cellflow.py --dataset immune_dictionary --scheme perturbation --fold 0 --emb text \
      --text-dir runs/pert_text/idict/emb --min-cells 30

CellFlow needs a vector for every perturbation (`perturbation_covariate_reps`):
--emb onehot: one-hot over all perturbations of the screen. A perturbation held out in the test fold has a one-hot
  position the network never saw in training, the counterpart of CPA's own embedding.
--emb text: the full Qwen3-Embedding-4B text card (2,560 numbers, unit length). CellFlow's condition encoder (an MLP
  per covariate group, attention pooling, an MLP after pooling) is trained on top of it; the card itself is fixed.
Combinations (Norman) are two perturbation tokens; a single perturbation has a zero "none" token in the second slot.
Dose (log scale, divided by the screen's maximum) and, for sciPlex3, time are numeric covariates linked to each token.
The context (cell line or cell type) is a sample covariate (one-hot) and a split covariate, so CellFlow maps the
control cells of a context to the perturbed cells of the same context.

Folds are the benchmark's (vcb.pert.folds). Training cells: up to --cells-per-item cells of every training item plus up
to --ctrl-per-context control cells per context; nothing from a test item. Cells are log1p CP10k (totals over all
genes, as for the benchmark's item profiles) on the benchmark's 2,000 HVGs, then PCA (--n-pcs, fitted on training
cells). CellFlow works in this PCA space. Prediction: for each test item, the control cells of its context (up to
--query-cells) are pushed through the learned flow; the predicted shift is (mean predicted PCs - mean control PCs)
mapped back through the PCA loadings. Genes outside the HVGs get the training fold's mean shift.
Output: <out>/cellflow_<emb>/<dataset>.<scheme>.fold<k>.npz (item_ids, pred), the same layout as the CPA runs.
"""
import argparse
import sys
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from vcb.pert.folds import fold_splits, item_table  # noqa: E402
from vcb.pert.run import hvg_mask  # noqa: E402

DATA = ROOT / "data"
ap = argparse.ArgumentParser()
ap.add_argument("--dataset", required=True)
ap.add_argument("--scheme", choices=["context", "perturbation"], required=True)
ap.add_argument("--fold", type=int, required=True)
ap.add_argument("--emb", choices=["onehot", "text"], required=True)
ap.add_argument("--text-dir", default=str(ROOT / "runs" / "pert_text" / "emb"))
ap.add_argument("--text-model", default="Qwen3-Embedding-4B")
ap.add_argument("--min-cells", type=int, default=50)
ap.add_argument("--cells-per-item", type=int, default=200)
ap.add_argument("--ctrl-per-context", type=int, default=5000)
ap.add_argument("--query-cells", type=int, default=500)
ap.add_argument("--n-pcs", type=int, default=100)
ap.add_argument("--iterations", type=int, default=40000)
ap.add_argument("--batch-size", type=int, default=1024)
ap.add_argument("--out", default=str(ROOT / "runs" / "pert_text" / "cellflow"))
ap.add_argument("--preset", choices=["small", "combosciplex"], default="small",
                help="small: the first runs (1024-wide networks, attention pooling, capped cells). combosciplex: the model "
                     "settings of CellFlow's docs/notebooks/500_combosciplex.ipynb and all training cells (--cells-per-item "
                     "and --ctrl-per-context are ignored); outputs go to cellflow_cs_<emb>")
ap.add_argument("--debug", action="store_true", help="few iterations and test items, writes *.debug.npz")
a = ap.parse_args()
t0 = time.time()
log = lambda s: print(f"[{time.time()-t0:6.0f}s] {s}", flush=True)

import jax  # noqa: E402
log(f"jax devices: {jax.devices()}")
from cellflow.model import CellFlow  # noqa: E402

# ---- items, folds, genes ----
items = ad.read_h5ad(DATA / "items" / f"{a.dataset}.items.h5ad")
meta, D, ctrl_rows = item_table(items, min_cells=a.min_cells)
hv = hvg_mask(items)
genes = items.var_names[hv].astype(str)
del items
splits = {f: (tr, te) for f, tr, te in fold_splits(meta, a.scheme, 5)}
tr, te = splits[a.fold]
if a.debug:
    te = te[:12]
log(f"{a.dataset} {a.scheme} fold {a.fold} emb={a.emb}: {len(tr)} train items, {len(te)} test items")

combo = a.dataset.startswith("NormanWeissman")
NONE = "none"
def toks(p):
    t = p.split("_") if combo else [p]
    return (t + [NONE])[:2] if combo else t
dose_raw = pd.to_numeric(meta["dose"], errors="coerce")
has_dose = dose_raw.notna().any() and dose_raw.nunique() > 1
dmax = float(np.log1p(dose_raw.max())) if has_dose else 1.0
def dose_v(x):
    x = float(x)
    return float(np.log1p(x) / dmax) if has_dose and np.isfinite(x) else 1.0
use_time = "time_h" in meta and meta["time_h"].nunique() > 1
tmax = float(meta["time_h"].max()) if use_time else 1.0

# ---- training cells: chunked reads, log1p CP10k over all genes, keep HVGs ----
cells = ad.read_h5ad(DATA / "items" / f"{a.dataset}.cells.h5ad", backed="r")
co = cells.obs
gpos = pd.Index(cells.var_names.astype(str)).get_indexer(genes)
assert (gpos >= 0).all()
if a.preset == "combosciplex":
    a.cells_per_item = a.ctrl_per_context = 10**9         # all training cells, as in the CellFlow examples
rng = np.random.default_rng(a.fold)
train_ids = set(meta.index[tr])
by_item = co.groupby("item_id", observed=True).indices
sel = [rng.choice(idx, min(a.cells_per_item, len(idx)), replace=False) for iid, idx in by_item.items() if iid in train_ids]
is_ctrl_all = co["is_control"].values.astype(bool)
ctx_all = co["context"].astype(str).values
ctrl_sel = []
for c in np.unique(ctx_all[is_ctrl_all]):
    idx = np.where(is_ctrl_all & (ctx_all == c))[0]
    ctrl_sel.append(rng.choice(idx, min(a.ctrl_per_context, len(idx)), replace=False))
sel = np.sort(np.concatenate(sel + ctrl_sel))
if a.debug:
    sel = np.sort(rng.choice(sel, min(30000, len(sel)), replace=False))


def read_rows(rows, chunk=20000):
    out = []
    for s in range(0, len(rows), chunk):
        r = rows[s:s + chunk]
        X = cells.X[r] if not isinstance(cells.X, np.ndarray) else cells.X[r]
        X = sp.csr_matrix(X, dtype=np.float32)
        tot = np.asarray(X.sum(1)).ravel()
        X = sp.diags((1e4 / np.maximum(tot, 1)).astype(np.float32)) @ X[:, gpos]
        X.data = np.log1p(X.data)
        out.append(X.tocsr())
    return sp.vstack(out).tocsr()


X = read_rows(sel)
o = co.iloc[sel]
log(f"training cells {X.shape}")

# ---- PCA on training cells ----
from sklearn.decomposition import PCA  # noqa: E402
fit_rows = rng.choice(X.shape[0], min(200000, X.shape[0]), replace=False)
pca = PCA(n_components=a.n_pcs, random_state=0).fit(X[fit_rows].toarray())
def to_pc(M, chunk=50000):
    return np.concatenate([pca.transform(M[s:s + chunk].toarray()) for s in range(0, M.shape[0], chunk)]).astype(np.float32)
Z = to_pc(X)
log(f"PCA {a.n_pcs}: explained variance {pca.explained_variance_ratio_.sum():.3f}")

# ---- obs for CellFlow ----
item_meta = meta[["perturbation", "dose"] + (["time_h"] if use_time else [])]
pert_cols = ["pert1", "pert2"] if combo else ["pert1"]
dose_cols = ["dose1", "dose2"] if combo else ["dose1"]
time_cols = ["time1", "time2"] if combo else ["time1"]


def obs_rows(perts, doses, times, ctxs, is_ctrl):
    rows = []
    for p, d, t, c, ic in zip(perts, doses, times, ctxs, is_ctrl):
        tk = [NONE] * len(pert_cols) if ic else toks(p)
        r = {"context": c, "control": bool(ic)}
        for k, col in enumerate(pert_cols):
            r[col] = tk[k]
            r[dose_cols[k]] = 0.0 if (ic or tk[k] == NONE) else dose_v(d)
            r[time_cols[k]] = 0.0 if (ic or tk[k] == NONE) else (float(t) / tmax if use_time else 1.0)
        rows.append(r)
    return pd.DataFrame(rows)


o_item = o["item_id"].astype(str).values
im = item_meta.reindex(o_item)
tobs = obs_rows(np.where(o["is_control"].values.astype(bool), "", im["perturbation"].astype(str).values),
                im["dose"].values, im["time_h"].values if use_time else np.ones(len(o)), o["context"].astype(str).values,
                o["is_control"].values.astype(bool))

# ---- representations ----
all_tokens = sorted({t for p in meta["perturbation"].astype(str) for t in toks(p)} - {NONE})
if a.emb == "text":
    E = Path(a.text_dir)
    keys = (E / "keys.txt").read_text().splitlines()
    M = np.load(E / f"{a.text_model}.full.npy").astype(np.float32)
    kpos = {k: i for i, k in enumerate(keys)}
    ptype = str(meta["pert_type"].iloc[0])
    def vec(tok):
        for t in ([ptype] + (["CRISPRi", "CRISPR_KO"] if ptype.startswith("CRISPR") else [])):
            if f"{t}::{tok}" in kpos:
                v = M[kpos[f"{t}::{tok}"]]
                return v / (np.linalg.norm(v) + 1e-9)
        return None
    reps = {t: vec(t) for t in all_tokens}
    missing = [t for t, v in reps.items() if v is None]
    dim = M.shape[1]
    reps = {t: (v if v is not None else np.zeros(dim, np.float32)) for t, v in reps.items()}
    log(f"text cards for {len(all_tokens) - len(missing)} of {len(all_tokens)} perturbations; missing (zero vector): {missing[:10]}")
else:
    dim = len(all_tokens)
    reps = {t: np.eye(dim, dtype=np.float32)[i] for i, t in enumerate(all_tokens)}
reps[NONE] = np.zeros(dim, np.float32)
ctxs = sorted(meta["context"].astype(str).unique())
ctx_rep = {c: np.eye(len(ctxs), dtype=np.float32)[i] for i, c in enumerate(ctxs)}

# CellFlow needs a perturbed target for every control population it trains on; controls of a context with no training
# items (possible in the context split) are kept out of training but still serve as the source at prediction time
tgt_ctx = set(tobs.loc[~tobs["control"], "context"])
trn = (~tobs["control"].values) | tobs["context"].isin(tgt_ctx).values
T = ad.AnnData(X=np.zeros((int(trn.sum()), 1), np.float32), obs=tobs[trn].reset_index(drop=True))
T.obsm["X_pca"] = Z[trn]
log(f"CellFlow training cells {T.n_obs} ({int(T.obs['control'].sum())} controls, {len(tgt_ctx)} contexts with targets)")
# categories cover every perturbation and context of the screen, so test items keep their names at prediction time
CATS = {**{c: [NONE] + all_tokens for c in pert_cols}, "context": ctxs}
for c in pert_cols + ["context"]:
    T.obs[c] = pd.Categorical(T.obs[c], categories=CATS[c])
T.uns["pert_emb"] = reps
T.uns["ctx_emb"] = ctx_rep

pcov = {"pert": pert_cols, "dose": dose_cols}
if use_time:
    pcov["time"] = time_cols
cf = CellFlow(T, solver="otfm")
cf.prepare_data(sample_rep="X_pca", control_key="control", perturbation_covariates=pcov,
                perturbation_covariate_reps={"pert": "pert_emb"}, sample_covariates=["context"],
                sample_covariate_reps={"context": "ctx_emb"}, split_covariates=["context"],
                max_combination_length=len(pert_cols), null_value=0.0)
if a.preset == "combosciplex":
    # docs/notebooks/500_combosciplex.ipynb: 256x2 MLP before mean pooling (the same for our dose, time and context
    # groups, which that example does not have), 256x2 after, condition embedding 64 with output dropout 0.9,
    # flow network 2048x3, decoder 4096x3, constant noise 1.5, linear projection before concatenation,
    # match_linear with epsilon = tau_a = tau_b = 1
    import functools
    from cellflow.utils import match_linear
    mlp256 = {"layer_type": "mlp", "dims": [256, 256], "dropout_rate": 0.0}
    before = {g: dict(mlp256) for g in list(pcov) + ["context"]}
    model_kw = dict(condition_mode="deterministic", regularization=0.0, pooling="mean", layers_before_pool=before,
                    layers_after_pool=dict(mlp256), condition_embedding_dim=64, cond_output_dropout=0.9,
                    hidden_dims=[2048, 2048, 2048], conditioning="concatenation", decoder_dims=[4096, 4096, 4096],
                    probability_path={"constant_noise": 1.5},
                    match_fn=functools.partial(match_linear, epsilon=1.0, tau_a=1.0, tau_b=1.0),
                    linear_projection_before_concatenation=True, seed=a.fold)
before_small = {"pert": {"layer_type": "mlp", "dims": [1024, 1024], "dropout_rate": 0.2},
          "dose": {"layer_type": "mlp", "dims": [64, 64], "dropout_rate": 0.0},
          "context": {"layer_type": "mlp", "dims": [128, 128], "dropout_rate": 0.2}}
if use_time:
    before_small["time"] = {"layer_type": "mlp", "dims": [64, 64], "dropout_rate": 0.0}
if a.preset == "small":
    model_kw = dict(condition_embedding_dim=256, cond_output_dropout=0.5, pooling="attention_token",
                    layers_before_pool=before_small, layers_after_pool={"layer_type": "mlp", "dims": [1024], "dropout_rate": 0.2},
                    hidden_dims=(1024, 1024, 1024), decoder_dims=(1024, 1024, 1024), time_encoder_dims=(512, 512, 512),
                    probability_path={"constant_noise": 0.5}, seed=a.fold)
log(f"preset {a.preset}")
cf.prepare_model(**model_kw)
n_it = 200 if a.debug else a.iterations
log(f"training {n_it} iterations, batch {a.batch_size}")
cf.train(num_iterations=n_it, batch_size=a.batch_size, valid_freq=10 * n_it)
log("trained")

# ---- prediction: per context, all test items of that context at once ----
ms = D[tr].mean(0)
comps = pca.components_.astype(np.float32)
o_ctrl = np.where(tobs["control"].values)[0]
ctrl_by_ctx = pd.Series(o_ctrl).groupby(tobs["context"].values[o_ctrl]).apply(np.asarray).to_dict()
keys_order = list(cf._dm.perturb_covar_keys)
log(f"prediction key order: {keys_order}")
test_meta = meta.iloc[te]
pred_shift = {}
for c, grp in test_meta.groupby(test_meta["context"].astype(str)):
    if c not in ctrl_by_ctx:
        continue
    rows = ctrl_by_ctx[c]
    rows = rows if len(rows) <= a.query_cells else np.random.default_rng(0).choice(rows, a.query_cells, replace=False)
    Q = ad.AnnData(X=np.zeros((len(rows), 1), np.float32), obs=tobs.iloc[rows].reset_index(drop=True))
    Q.obsm["X_pca"] = Z[rows]
    Q.uns["pert_emb"] = reps
    Q.uns["ctx_emb"] = ctx_rep
    for col in pert_cols + ["context"]:
        Q.obs[col] = pd.Categorical(Q.obs[col], categories=CATS[col])
    cov = obs_rows(grp["perturbation"].astype(str).values, grp["dose"].values,
                   grp["time_h"].values if use_time else np.ones(len(grp)), [c] * len(grp), [False] * len(grp))
    for col in pert_cols + ["context"]:
        cov[col] = pd.Categorical(cov[col], categories=CATS[col])
    assert not cov[pert_cols + ["context"]].isna().any().any()
    want = {}
    for iid, (_, r) in zip(grp.index, cov.iterrows()):
        want.setdefault(tuple(str(r[k]) for k in keys_order), []).append(iid)
    ucov = cov.drop_duplicates(subset=keys_order).reset_index(drop=True)
    P = cf.predict(Q, covariate_data=ucov, sample_rep="X_pca")
    base = Z[rows].mean(0)
    for k, v in P.items():
        kk = tuple(str(x) for x in (k if isinstance(k, tuple) else (k,)))
        for iid in want.get(kk, []):
            pred_shift[iid] = (np.asarray(v).mean(0) - base) @ comps
    log(f"context {c}: {len(grp)} test items, {len(P)} predicted conditions, matched {sum(i in pred_shift for i in grp.index)}")

preds, ids = [], []
for j in te:
    iid = meta.index[j]
    p = ms.copy()
    if iid in pred_shift:
        p[hv] = pred_shift[iid]
    preds.append(p.astype(np.float32)); ids.append(iid)
out = Path(a.out) / f"cellflow{'_cs' if a.preset == 'combosciplex' else ''}_{a.emb}"
out.mkdir(parents=True, exist_ok=True)
np.savez_compressed(out / f"{a.dataset}.{a.scheme}.fold{a.fold}{'.debug' if a.debug else ''}.npz",
                    item_ids=np.array(ids), pred=np.stack(preds))
log(f"wrote {len(ids)} predictions ({len(pred_shift)} from CellFlow) to {out}")
if a.debug:
    from vcb.pert.metrics import score_items
    pos = [meta.index.get_loc(i) for i in ids]
    s = score_items(np.stack(preds), D[pos], np.tile(ms, (len(pos), 1)), genes_mask=hv)
    log("debug pearson_delta@hvg: " + " ".join(f"{x:.2f}" for x in s.get("pearson_delta", [])))

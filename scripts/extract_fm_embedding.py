#!/usr/bin/env python
"""Embed a component-A panel with a single-cell foundation model from the scfm-irt repository.

Runs inside that model's isolated venv in scfm-irt (for example `$SCFM_IRT/.venv-scgpt/bin/python`),
never in this repo's `.venv`: the only things imported here are numpy, anndata and `scfm_irt`.
`slurm/fm_embed.sh` resolves the venv and the work-dir environment variables per model.

  $SCFM_IRT/.venv-scgpt/bin/python scripts/extract_fm_embedding.py --panel data/panels/hao_pbmc_l2.h5ad --embedder scgpt

Protocol, identical to the scVI route: every cell of the panel (train and test) is embedded with the
frozen model, in chunks so that host and GPU memory stay bounded; nothing is fitted on the panel
(every registered foundation model is zero-shot, `requires_dataset_fit = False`). The output is
`cache/embeddings/<out-name>.npz` in the format `append_repr_responses.py` reads (`train_ids`,
`Z_train`, `test_ids`, `Z_test`), plus a JSON sidecar with the model name, version and dimension.
Chunks are written to `cache/embeddings/_parts/<out-name>/` as they finish, so a crashed run
resumes where it stopped.

Gene identifiers: the embedders expect gene *symbols* as `var_names` and, for the Ensembl-tokenised
models (Geneformer, TranscriptFormer, LangCell, scFoundation's vocabulary), an `ensembl_id` column.
Panels built by this repo have symbols as `var_names`; the Ensembl id is taken from whichever `var`
column carries it (`ensembl_id`, `gene_ids`, `feature_id`, or an Ensembl-indexed `var` with a
`gene_symbols` / `feature_name` column). If none exists the embedder's own resolver (Geneformer's
dictionary, else mygene online) is left to map symbols, and a warning is printed.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def harmonise_var(adata):
    """Symbols as var_names, `gene_name` column, `ensembl_id` column where it can be found."""
    import pandas as pd

    var = adata.var
    names = pd.Index(var.index.astype(str))
    ens_col = None
    if names.str.startswith("ENSG").mean() > 0.5:
        var["ensembl_id"] = names.str.split(".").str[0]
        for c in ("gene_symbols", "feature_name", "gene_name", "gene_symbol", "symbol"):
            if c in var.columns:
                adata.var_names = var[c].astype(str).values
                break
        else:
            print("warning: Ensembl-indexed var without a symbol column; models that need symbols will match nothing", flush=True)
    else:
        for c in ("ensembl_id", "gene_ids", "feature_id", "ensembl", "gene_id"):
            if c in var.columns and var[c].astype(str).str.startswith("ENSG").mean() > 0.5:
                ens_col = c
                break
        if ens_col is None:
            for c in var.columns:
                if var[c].dtype == object and var[c].astype(str).str.startswith("ENSG").mean() > 0.5:
                    ens_col = c
                    break
        if ens_col is not None:
            adata.var["ensembl_id"] = adata.var[ens_col].astype(str).str.split(".").str[0].values
        else:
            print("warning: no Ensembl id column in var; Ensembl-tokenised models will resolve symbols themselves (mygene / Geneformer dictionary)", flush=True)
    adata.var["gene_name"] = adata.var_names.astype(str)
    adata.var_names_make_unique()
    return adata


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--panel", required=True, help="panel h5ad with raw counts in X and obs.split")
    ap.add_argument("--embedder", required=True, help="scfm-irt registry name: scgpt, geneformer_v2_316m, uce, state, scprint_large_v1, ...")
    ap.add_argument("--out-name", default=None, help="cache file name and respondent id (default fm_<embedder>)")
    ap.add_argument("--chunk", type=int, default=20000, help="cells per embedding call")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--batch-size", type=int, default=None, help="override the embedder's batch size (smaller for 11 GB GPUs)")
    ap.add_argument("--cache-dir", default=str(ROOT / "cache" / "embeddings"))
    ap.add_argument("--debug", action="store_true", help="2 % of train and 5 % of test cells, name suffixed _debug")
    ap.add_argument("--force", action="store_true", help="ignore finished chunks")
    a = ap.parse_args()

    import anndata as ad
    from scfm_irt.embedders.base import align_embedding_rows
    from scfm_irt.embedders.registry import get_embedder

    t0 = time.time()
    name = a.out_name or f"fm_{a.embedder}"
    if a.debug:
        name += "_debug"
    cache = Path(a.cache_dir)
    parts = cache / "_parts" / name
    parts.mkdir(parents=True, exist_ok=True)

    panel = ad.read_h5ad(a.panel)
    tr = (panel.obs["split"] == "train").values
    te = (panel.obs["split"] == "test").values
    if a.debug:
        rng = np.random.default_rng(0)
        tr &= rng.random(len(tr)) < 0.02
        te &= rng.random(len(te)) < 0.05
    keep = tr | te
    cells = panel[keep].copy()
    del panel
    cells = harmonise_var(cells)
    for k in list(cells.obsm.keys()):
        del cells.obsm[k]
    for k in list(cells.layers.keys()):
        del cells.layers[k]
    print(f"[{name}] {cells.n_obs} cells ({tr.sum()} train, {te.sum()} test), {cells.n_vars} genes, "
          f"ensembl ids: {'yes' if 'ensembl_id' in cells.var else 'no'}; read in {time.time()-t0:.0f}s", flush=True)

    emb = get_embedder(a.embedder)
    if hasattr(emb, "device"):
        emb.device = a.device
    if a.batch_size is not None and hasattr(emb, "batch_size"):
        emb.batch_size = a.batch_size
    if getattr(emb, "requires_dataset_fit", False):
        emb.fit(emb.preprocess(cells[tr[keep]].copy()))
    if getattr(emb, "label_supervised", False):
        print(f"note: {a.embedder} was trained with cell-type labels (label_supervised); report it apart from the zero-shot models", flush=True)

    ids = np.asarray(cells.obs_names, dtype=str)
    n = cells.n_obs
    Z = None
    for c0 in range(0, n, a.chunk):
        c1 = min(c0 + a.chunk, n)
        part = parts / f"{c0:09d}_{c1:09d}.npy"
        if part.exists() and not a.force:
            z = np.load(part)
        else:
            tc = time.time()
            sub = cells[c0:c1].copy()
            z = np.asarray(emb.embed(emb.preprocess(sub)), dtype=np.float32)
            if z.shape[0] != sub.n_obs:
                raise RuntimeError(f"{a.embedder} returned {z.shape[0]} rows for {sub.n_obs} cells in chunk {c0}:{c1}")
            np.save(part, z)
            print(f"  cells {c1}/{n}  dim {z.shape[1]}  {time.time()-tc:.0f}s", flush=True)
        if Z is None:
            Z = np.zeros((n, z.shape[1]), dtype=np.float32)
        Z[c0:c1] = z
    Z = align_embedding_rows(Z, ids, ids, a.embedder)
    tr_k, te_k = tr[keep], te[keep]
    cache.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(cache / f"{name}.npz", train_ids=ids[tr_k], Z_train=Z[tr_k], test_ids=ids[te_k], Z_test=Z[te_k])
    meta = {"respondent": name, "embedder": a.embedder, "version": str(getattr(emb, "version", "unknown")), "dim": int(Z.shape[1]), "n_train": int(tr_k.sum()), "n_test": int(te_k.sum()),
            "panel": str(a.panel), "label_supervised": bool(getattr(emb, "label_supervised", False)), "seconds": round(time.time() - t0), "python": sys.executable}
    (cache / f"{name}.json").write_text(json.dumps(meta, indent=1))
    print(f"[{name}] wrote {cache / name}.npz  train {int(tr_k.sum())} test {int(te_k.sum())} dim {Z.shape[1]}  {time.time()-t0:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

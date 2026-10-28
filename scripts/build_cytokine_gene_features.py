#!/usr/bin/env python
"""Gene-level representations of the Parse cytokines' ligand and receptor genes from pretrained models.

  $SCFM_IRT/.venv-state/bin/python scripts/build_cytokine_gene_features.py

Writes runs/pert_pool_v0/cytokine_features/<source>.parquet: one row per gene (symbol index), one column
per dimension, for the genes listed in src/vcb/data/parse_cytokines.tsv. These describe a cytokine by
its own genes and its receptor's, which is what lets a model predict a cytokine it never saw.

Sources (all read with weights-only loading; nothing in the files can execute):
- scgpt: the gene token embedding of scGPT whole-human (encoder.embedding.weight, vocab.json)
- geneformer: the token embedding of Geneformer V2-316M (Ensembl tokens, 104M dictionary)
- scfoundation: the gene position embedding of scFoundation (pos_emb, 19,264-gene index)
- esm2: the ESM2 protein embedding UCE uses for each human gene (also TranscriptFormer's gene input)
"""
import gzip
import json
import os
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
SCFM = Path(os.environ.get("SCFM_IRT", ROOT.parent / "scfm-irt")) / "cache"
OUT = ROOT / "runs" / "pert_pool_v0" / "cytokine_features"
OUT.mkdir(parents=True, exist_ok=True)
ref = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False)
GENES = sorted({g for col in ("ligand_genes", "receptor_genes") for s in ref[col] for g in s.split(",") if g})
print(len(GENES), "genes")


def save(name, table):
    df = pd.DataFrame({g: np.asarray(v, dtype=np.float32) for g, v in table.items()}).T
    df.columns = [f"{name}{i}" for i in range(df.shape[1])]
    df.to_parquet(OUT / f"{name}.parquet")
    missing = sorted(set(GENES) - set(table))
    print(f"{name}: {len(table)}/{len(GENES)} genes, dim {df.shape[1]}; missing {missing}")


# scGPT
vocab = json.loads((SCFM / "scgpt_workdir" / "scGPT_human" / "vocab.json").read_text())
sd = torch.load(SCFM / "scgpt_workdir" / "scGPT_human" / "best_model.pt", map_location="cpu", weights_only=True)
W = sd["encoder.embedding.weight"].float().numpy()
save("scgpt", {g: W[vocab[g]] for g in GENES if g in vocab})

# Geneformer V2-316M
from safetensors.numpy import load_file  # noqa: E402

gf = SCFM / "geneformer_workdir" / "Geneformer"
tok = pickle.load(open(gf / "geneformer" / "token_dictionary_gc104M.pkl", "rb"))
st = load_file(str(gf / "Geneformer-V2-316M" / "model.safetensors"))
key = next(k for k in st if k.endswith("word_embeddings.weight"))
W = st[key].astype(np.float32)
sym2ens = pd.read_csv(ROOT / "src" / "vcb" / "data" / "symbol_to_ensembl.tsv.gz", sep="\t")
sym2ens = dict(zip(sym2ens["symbol"].astype(str), sym2ens["ensembl_id"].astype(str)))
save("geneformer", {g: W[tok[sym2ens[g]]] for g in GENES if g in sym2ens and sym2ens[g] in tok})

# scFoundation: the gene identity is its position embedding
ck = torch.load(SCFM / "scfoundation_workdir" / "scFoundation" / "model" / "models" / "models.ckpt", map_location="cpu", weights_only=True)
P = ck["cell"]["state_dict"]["model.pos_emb.weight"].float().numpy()
idx = pd.read_csv(SCFM / "scfoundation_workdir" / "scFoundation" / "model" / "OS_scRNA_gene_index.19264.tsv", sep="\t")
pos = dict(zip(idx["gene_name"].astype(str), idx["index"].astype(int)))
save("scfoundation", {g: P[pos[g]] for g in GENES if g in pos})

# ESM2 protein embeddings (UCE's gene input)
esm = torch.load(SCFM / "uce_workdir" / "UCE" / "model_files" / "protein_embeddings" / "Homo_sapiens.GRCh38.gene_symbol_to_embedding_ESM2.pt", map_location="cpu", weights_only=True)
save("esm2", {g: esm[g].float().numpy() for g in GENES if g in esm})

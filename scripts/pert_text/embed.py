#!/usr/bin/env python
"""Step 3 of the text perturbation encoder: embed every perturbation card with a text model.

  HF_HOME=cache/hf .venv-text/bin/python scripts/pert_text/embed.py --model Qwen/Qwen3-Embedding-4B

Writes runs/pert_text/emb/<tag>.<field>.npy (float32, L2-normalised, rows in cards.jsonl order) and
keys.txt. Two fields per card: `full` (name, type, targets, database descriptions) and `name` (name and
type only), so the value of the description can be separated from the value of the name.
Cards are embedded as documents, without an instruction prefix (Qwen3-Embedding uses instructions only
for queries).
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch
from sentence_transformers import SentenceTransformer

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True)
ap.add_argument("--batch-size", type=int, default=16)
ap.add_argument("--max-len", type=int, default=1024)
a = ap.parse_args()
OUT = ROOT / "runs" / "pert_text" / "emb"
OUT.mkdir(parents=True, exist_ok=True)
cards = [json.loads(l) for l in open(ROOT / "runs" / "pert_text" / "cards.jsonl")]
(OUT / "keys.txt").write_text("\n".join(c["key"] for c in cards) + "\n")
tag = a.model.split("/")[-1]
dev = "cuda" if torch.cuda.is_available() else "cpu"
kw = {"torch_dtype": torch.bfloat16} if dev == "cuda" else {}
m = SentenceTransformer(a.model, device=dev, model_kwargs=kw)
m.max_seq_length = min(a.max_len, m.max_seq_length or a.max_len)
t0 = time.time()
for field in ("full", "name"):
    texts = [c[f"text_{field}"] for c in cards]
    order = np.argsort([len(t) for t in texts])          # length-sorted batches waste less padding
    E = m.encode([texts[i] for i in order], batch_size=a.batch_size, normalize_embeddings=True, show_progress_bar=False, convert_to_numpy=True)
    out = np.empty_like(E)
    out[order] = E
    np.save(OUT / f"{tag}.{field}.npy", out.astype(np.float32))
    print(f"{tag} {field}: {out.shape} on {dev} in {time.time() - t0:.0f}s", flush=True)

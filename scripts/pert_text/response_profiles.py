#!/usr/bin/env python
"""Measured response profile of every perturbation, per screen, plus the non-text baselines.

  .venv/bin/python scripts/pert_text/response_profiles.py        # under Slurm: reads every items file

For each screen: the shift of each item (treated minus control, log1p CP10k) on the screen's 2,000 HVGs,
averaged over the perturbation's contexts -> runs/pert_text/profiles/<dataset>.npz (names, P).
Baselines written next to it:
- genetic screens: the control-cell gene embedding the benchmark already uses (vcb.pert.features), for the
  target gene(s) -> base_ctrlpca;
- Tahoe drugs: 2048-bit Morgan fingerprints from Tahoe's SMILES -> base_morgan.
"""
import glob
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd

from vcb import DATA
from vcb.pert.features import gene_embedding_from_controls
from vcb.pert.folds import item_table
from vcb.pert.run import hvg_mask

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "runs" / "pert_text" / "profiles"
OUT.mkdir(parents=True, exist_ok=True)

for f in sorted(glob.glob(str(DATA / "items" / "*.items.h5ad"))):
    ds = Path(f).name.replace(".items.h5ad", "")
    items = ad.read_h5ad(f)
    meta, D, _ = item_table(items)
    hv = hvg_mask(items)
    Dh = pd.DataFrame(D[:, hv]).groupby(meta["perturbation"].astype(str).values).mean()
    extra = {}
    ptype = meta["pert_type"].astype(str).value_counts().index[0]
    if ptype in ("CRISPRi", "CRISPR_KO", "CRISPRa"):
        cells = ad.read_h5ad(DATA / "items" / f"{ds}.cells.h5ad", backed="r")
        ctrl = np.where(cells.obs["is_control"].values.astype(bool))[0]
        rng = np.random.default_rng(0)
        pick = np.sort(rng.choice(ctrl, min(5000, len(ctrl)), replace=False))
        emb = gene_embedding_from_controls(cells[pick].to_memory().X, cells.var_names.astype(str), dim=64)
        tg = meta.groupby(meta["perturbation"].astype(str))["targets"].first().reindex(Dh.index).astype(str)
        B, ok = [], []
        for t in tg:
            gs = [g for g in t.split("|") if g in emb.index]
            B.append(emb.loc[gs].values.mean(0) if gs else np.zeros(emb.shape[1])); ok.append(bool(gs))
        extra["base_ctrlpca"] = np.asarray(B, np.float32); extra["base_ctrlpca_ok"] = np.asarray(ok)
    if ds == "tahoe100m":
        from rdkit import Chem, RDLogger
        from rdkit.Chem import rdFingerprintGenerator
        RDLogger.DisableLog("rdApp.*")
        smi = pd.read_parquet(DATA / "raw" / "tahoe" / "meta" / "drug_metadata.parquet").set_index("drug")["canonical_smiles"]
        gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
        B, ok = [], []
        for n in Dh.index:
            mol = Chem.MolFromSmiles(str(smi.get(n, ""))) if n in smi.index else None
            B.append(np.array(gen.GetFingerprintAsNumPy(mol), np.float32) if mol is not None else np.zeros(2048, np.float32)); ok.append(mol is not None)
        extra["base_morgan"] = np.asarray(B, np.float32); extra["base_morgan_ok"] = np.asarray(ok)
    np.savez_compressed(OUT / f"{ds}.npz", names=np.asarray(Dh.index, dtype="U"), P=Dh.values.astype(np.float32), pert_type=ptype, **extra)
    print(f"{ds}: {Dh.shape[0]} perturbations ({ptype}), baselines {sorted(k for k in extra if not k.endswith('_ok'))}", flush=True)

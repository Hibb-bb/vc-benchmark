"""Common obs schema for perturbation datasets (component B).

Every raw dataset is mapped onto these columns before items are built:

    perturbation   str   canonical perturbation label; 'control' for controls
    targets        str   '|'-joined gene symbols for genetic perturbations, '' otherwise
    pert_type      str   CRISPRi | CRISPRa | CRISPR_KO | drug | cytokine | other
    context        str   cell line / cell type / tissue the condition lives in
    dose           float dose value (NaN if absent); dose_unit str
    time_h         float hours since perturbation (NaN if absent)
    is_control     bool

`condition_key` concatenates the non-constant fields so an item is unique within a dataset.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

CONTROL = "control"

_PERT_TYPE_MAP = {
    "crispri": "CRISPRi",
    "crispra": "CRISPRa",
    "crispr": "CRISPR_KO",
    "crispr ko": "CRISPR_KO",
    "crispr-cas9": "CRISPR_KO",
    "drug": "drug",
    "chemical": "drug",
    "cytokine": "cytokine",
}


# scPerturb labels every CRISPR screen 'CRISPR'; the modality matters for the on-target rule.
PERT_TYPE_OVERRIDE = {
    "NormanWeissman2019_filtered": "CRISPRa",
    "AdamsonWeissman2016_GSM2406681_10X010": "CRISPRi",
    "ReplogleWeissman2022_K562_gwps": "CRISPRi",
    "ReplogleWeissman2022_K562_essential": "CRISPRi",
    "ReplogleWeissman2022_rpe1": "CRISPRi",
    "NadigOConner2024_hepg2": "CRISPRi",
    "NadigOConner2024_jurkat": "CRISPRi",
    "TianKampmann2019_iPSC": "CRISPRi",
    "TianKampmann2019_day7neuron": "CRISPRi",
    "TianKampmann2021_CRISPRi": "CRISPRi",
    "FrangiehIzar2021_RNA": "CRISPR_KO",
}

# Adamson 2016: labels are '<gene>_<plasmid>'; '63(mod)', '62(mod)', 'Gal4-4(mod)' are
# non-targeting controls; 'nan' / '*' are unassigned cells.
_ADAMSON_CONTROLS = {"63(mod)", "62(mod)", "Gal4-4(mod)"}


def _dataset_specific_labels(pert: pd.Series, dataset_id: str) -> pd.Series:
    if dataset_id.startswith("AdamsonWeissman2016"):
        gene = pert.str.split("_p").str[0]
        gene = gene.where(~gene.isin(_ADAMSON_CONTROLS), CONTROL)
        gene = gene.where(~pert.isin(["nan", "*", "None"]), "unassigned")
        return gene
    return pert


def _first_present(obs: pd.DataFrame, candidates: list[str]) -> str | None:
    for c in candidates:
        if c in obs.columns:
            return c
    return None


def harmonize_scperturb(obs: pd.DataFrame, dataset_id: str) -> pd.DataFrame:
    """Map a scPerturb obs frame to the common schema. Returns a new frame (same index)."""
    out = pd.DataFrame(index=obs.index)
    pert = _dataset_specific_labels(obs["perturbation"].astype(str).str.strip(), dataset_id)
    out["perturbation"] = pert
    out["is_control"] = pert.str.lower().eq(CONTROL)

    pt_col = _first_present(obs, ["perturbation_type"])
    if pt_col is not None:
        pt = obs[pt_col].astype(str).str.lower().map(lambda s: _PERT_TYPE_MAP.get(s, s))
        out["pert_type"] = pt.where(~out["is_control"], "control")
    else:
        out["pert_type"] = "other"
    if dataset_id in PERT_TYPE_OVERRIDE:
        out["pert_type"] = np.where(out["is_control"], "control", PERT_TYPE_OVERRIDE[dataset_id])

    # Genetic targets: scPerturb joins multi-gene perturbations with '_' (Norman) or '+'.
    genetic = out["pert_type"].isin(["CRISPRi", "CRISPRa", "CRISPR_KO"])
    targets = pert.str.replace("+", "_", regex=False).str.replace("_", "|", regex=False)
    out["targets"] = np.where(genetic & ~out["is_control"], targets, "")

    # scPerturb puts a second perturbation axis (e.g. Frangieh: Control / Co-culture / IFNg)
    # in perturbation_2; that is the context an item lives in. Otherwise the cell line / type.
    ctx_col = _first_present(obs, ["perturbation_2", "cell_line", "celltype", "cell_type", "tissue_type"])
    # "/" is not allowed: contexts key the control-stats dict stored in h5ad uns, where h5py treats "/" as a group separator
    out["context"] = obs[ctx_col].astype(str).str.replace("/", "-") if ctx_col else dataset_id

    dose_col = _first_present(obs, ["dose_value", "dose", "concentration"])
    out["dose"] = pd.to_numeric(obs[dose_col], errors="coerce") if dose_col else np.nan
    unit_col = _first_present(obs, ["dose_unit"])
    out["dose_unit"] = obs[unit_col].astype(str) if unit_col else ""

    time_col = _first_present(obs, ["time", "time_h", "timepoint"])
    if time_col:
        t = obs[time_col]
        if t.dtype == object or str(t.dtype) == "category":
            t = t.astype(str).str.extract(r"([\d.]+)")[0]
        out["time_h"] = pd.to_numeric(t, errors="coerce")
    else:
        out["time_h"] = np.nan

    for c in ["ncounts", "ngenes", "percent_mito"]:
        if c in obs.columns:
            out[c] = obs[c].values
    out["dataset_id"] = dataset_id
    return out


def condition_key(h: pd.DataFrame) -> pd.Series:
    """Unique item key within a dataset: perturbation plus whichever of context/dose/time vary."""
    parts = [h["perturbation"].astype(str)]
    if h["context"].nunique() > 1:
        parts.append("ctx=" + h["context"].astype(str))
    if h["dose"].notna().any() and h["dose"].nunique(dropna=True) > 1:
        parts.append("dose=" + h["dose"].astype(str))
    if h["time_h"].notna().any() and h["time_h"].nunique(dropna=True) > 1:
        parts.append("t=" + h["time_h"].astype(str))
    key = parts[0]
    for p in parts[1:]:
        key = key + "::" + p
    return key


def make_generic_harmonizer(pert_col: str, control_label: str, context_col: str | None = None, pert_type: str = "cytokine", dose_col: str | None = None, time_col: str | None = None):
    """Harmonizer for any h5ad: perturbation from `pert_col` (rows equal to `control_label`
    are controls), context from `context_col` (e.g. donor, or donor|cell type), fixed modality."""
    def harmonize(obs: pd.DataFrame, dataset_id: str) -> pd.DataFrame:
        out = pd.DataFrame(index=obs.index)
        pert = obs[pert_col].astype(str).str.strip()
        out["is_control"] = pert == control_label
        out["perturbation"] = pert.where(~out["is_control"], CONTROL)
        out["pert_type"] = np.where(out["is_control"], "control", pert_type)
        out["targets"] = ""
        if context_col:
            cols = context_col.split("|")
            ctx = obs[cols[0]].astype(str)
            for c in cols[1:]:
                ctx = ctx + "|" + obs[c].astype(str)
            out["context"] = ctx.astype(str).str.replace("/", "-").values  # "/" would nest the uns control_stats groups
        else:
            out["context"] = dataset_id
        out["dose"] = pd.to_numeric(obs[dose_col], errors="coerce") if dose_col else np.nan
        out["dose_unit"] = ""
        out["time_h"] = pd.to_numeric(obs[time_col], errors="coerce") if time_col else np.nan
        for c in ["ncounts", "ngenes", "percent_mito", "nCount_RNA", "nFeature_RNA"]:
            if c in obs.columns:
                out[{"nCount_RNA": "ncounts", "nFeature_RNA": "ngenes"}.get(c, c)] = obs[c].values
        out["dataset_id"] = dataset_id
        return out
    return harmonize

"""Display names and families for respondents (paper figures and tables)."""
import re


# scfm-irt registry name -> display name (respondent id is fm_<registry name>)
FM_NAMES = {
    "scgpt": "scGPT (whole-human)", "geneformer": "Geneformer V1-10M", "geneformer_v2": "Geneformer V2-104M", "geneformer_v2_316m": "Geneformer V2-316M",
    "uce": "UCE (4 layer)", "scimilarity": "SCimilarity v1.1", "cellplm": "CellPLM 85M", "scfoundation": "scFoundation", "scprint": "scPRINT medium v1.5",
    "scprint2": "scPRINT small v2", "scprint_small_v1": "scPRINT small v1", "scprint_medium_v1": "scPRINT medium v1", "scprint_large_v1": "scPRINT large v1",
    "transcriptformer": "TranscriptFormer (sapiens)", "langcell": "LangCell", "state": "STATE SE-600M",
}


def display_name(rid: str) -> str:
    r = rid
    m = re.fullmatch(r"pca_k(\d+)", r)
    if m:
        return f"PCA-{m[1]}D"
    m = re.fullmatch(r"rproj_k(\d+)_s(\d)", r)
    if m:
        return f"Random projection-{m[1]}D (seed {m[2]})"
    m = re.fullmatch(r"nystroem_k(\d+)_g([\d.]+)", r)
    if m:
        return f"Nyström-{m[1]}D (kernel width = {m[2]})"
    m = re.fullmatch(r"nmf_k(\d+)", r)
    if m:
        return f"NMF-{m[1]}D"
    m = re.fullmatch(r"ica_k(\d+)", r)
    if m:
        return f"ICA-{m[1]}D"
    m = re.fullmatch(r"gmm_k(\d+)", r)
    if m:
        return f"GMM-{m[1]} memberships"
    if r == "depth2":
        return "Depth only (2D)"
    m = re.fullmatch(r"random_k(\d+)_s(\d)", r)
    if m:
        return f"Random-{m[1]}D (seed {m[2]})"
    m = re.fullmatch(r"scvi_k(\d+)_b(\w+)", r)
    if m:
        return f"scVI-{m[1]}D" + (" (tissue-corrected)" if m[2] == "tissue" else "")
    if r == "control_mean":
        return "No change"
    if r == "mean_shift":
        return "Mean shift"
    if r == "target_kd":
        return "Mean shift + on-target change"
    m = re.fullmatch(r"random_shift_s(\d)", r)
    if m:
        return f"Random shift (seed {m[1]})"
    m = re.fullmatch(r"knn_k(\d+)(_tf([\d.]+))?", r)
    if m:
        return f"KNN (K={m[1]})" + (f", {int(float(m[3])*100)}\\% train" if m[3] else "")
    m = re.fullmatch(r"ridge_d(\d+)_lam([\d.]+)(_tf([\d.]+))?", r)
    if m:
        return f"Ridge (d={m[1]}, $\\lambda$={m[2]})" + (f", {int(float(m[4])*100)}\\% train" if m[4] else "")
    m = re.fullmatch(r"gp_d(\d+)_ls([\d.]+)", r)
    if m:
        return f"Gaussian process (kernel width = {m[2]})"
    m = re.fullmatch(r"lowrank_r(\d+)", r)
    if m:
        return f"Low-rank completion, rank {m[1]}"
    m = re.fullmatch(r"pcareg_k(\d+)", r)
    if m:
        return f"PCA regression-{m[1]}D"
    if r == "scgen":
        return "scGen"
    if r == "scvi_cf":
        return "scVI counterfactual"
    m = re.fullmatch(r"mlp_h(\d+)_d(\d+)", r)
    if m:
        return f"MLP ({m[1]} hidden, d={m[2]})"
    m = re.fullmatch(r"latent_(.+)", r)
    if m:
        return "Latent shift on " + display_name(m[1])
    if r.startswith("fm_"):
        return FM_NAMES.get(r[3:], r[3:])
    return r


def plain_name(rid: str) -> str:
    """Same as display_name without LaTeX markup (for matplotlib)."""
    s = display_name(rid)
    return s.replace("$\\lambda$", "λ").replace("$", "").replace("\\%", "%")


def family(rid: str) -> str:
    if rid.startswith("fm_"):
        return "Foundation model"
    if rid.startswith("latent_"):
        return "Latent shift"
    for key, fam in [("pca_k", "PCA"), ("rproj", "Random projection"), ("nystroem", "Kernel features"), ("nmf", "NMF"), ("ica", "ICA"), ("gmm", "GMM"), ("depth", "Floor"), ("random_k", "Floor"), ("scvi", "scVI"),
                     ("control_mean", "Floor"), ("random_shift", "Floor"), ("mean_shift", "Mean shift"), ("target_kd", "Mean shift"), ("knn", "KNN"), ("ridge", "Ridge"), ("pcareg", "PCA regression"), ("gp_", "Gaussian process"), ("lowrank", "Low-rank"), ("scgen", "scGen"), ("scvi_cf", "scVI"), ("mlp", "MLP")]:
        if rid.startswith(key):
            return fam
    return "Other"

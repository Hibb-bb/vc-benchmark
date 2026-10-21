#!/usr/bin/env python
"""Foundation models next to the best simple models, panel by panel -> paper/bench/tab_fm.tex (+ tab_fm_acc.tex).

  python scripts/paper_fm_table.py
"""
import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.names import display_name

PANELS = [("repr_hao_pbmc_l2", "Hao PBMC"), ("repr_parse_pbmc_celltype", "Parse PBMC"), ("repr_heart_states", "Heart"),
          ("repr_hlca_core_donor", "HLCA d."), ("repr_hlca_core_study", "HLCA s."), ("repr_immune_atlas_donor", "Immune d."),
          ("repr_immune_atlas_tissue", "Immune t."), ("repr_pool_v0", "Tabula S.")]
ROWS = ["fm_transcriptformer", "fm_geneformer_v2_316m", "fm_scgpt", "fm_state", "fm_uce", "fm_cellplm", "fm_scprint_large_v1",
        "scvi_k30_bnone", "nystroem_k256_g0.5", "pca_k128", "random_k32_s0"]
OUT = RUNS.parent / "paper" / "bench"

ab, acc = {}, {}
for run, lab in PANELS:
    f = RUNS / run / "rasch" / "cell_level.abilities.csv"
    if not f.exists():
        continue
    a = pd.read_csv(f).set_index("respondent_id")
    ab[lab] = {r: a.loc[r, "ability"] if r in a.index else np.nan for r in ROWS}
    acc[lab] = {r: a.loc[r, "p_correct"] if r in a.index else np.nan for r in ROWS}


def write(table: dict, name: str, fmt):
    df = pd.DataFrame(table)
    cols = list(df.columns)
    L = ["\\begin{tabular}{@{}l" + "r" * len(cols) + "@{}}", "\\toprule", "Model & " + " & ".join(cols) + " \\\\", "\\midrule"]
    for i, r in enumerate(ROWS):
        if r == "scvi_k30_bnone":
            L.append("\\midrule")
        cells = [fmt(df.loc[r, c]) if np.isfinite(df.loc[r, c]) else "--" for c in cols]
        L.append(display_name(r).replace("&", "\\&") + " & " + " & ".join(cells) + " \\\\")
    L += ["\\bottomrule", "\\end{tabular}"]
    (OUT / name).write_text("\n".join(L) + "\n")
    print("wrote", OUT / name)


write(ab, "tab_fm.tex", lambda x: f"${x:+.2f}$")
write(acc, "tab_fm_acc.tex", lambda x: f"{x:.3f}")

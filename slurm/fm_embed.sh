#!/bin/bash
# Embed one panel with one foundation model from scfm-irt, then run the frozen probe and refit.
#
#   bash slurm/fm_embed.sh <embedder> <panel-name> [extra args for extract_fm_embedding.py]
#   e.g.  bash slurm/fm_embed.sh scgpt scbasecount_human200_blood
#         bash slurm/fm_embed.sh geneformer_v2_316m hao_pbmc_l2 --debug
#
# Environment: SCFM_IRT (path to the scfm-irt checkout, default ../scfm-irt), CUDA_VISIBLE_DEVICES,
# VCB_PY (this repo's interpreter, default .venv/bin/python), SKIP_REFIT=1 to only embed and append,
# PLACE=refit for a full refit instead of the default anchored placement (scripts/place_anchored.py).
# Works with or without Slurm; slurm/fm_embed.slurm wraps it for Quest's gengpu partition.
set -euo pipefail
EMBEDDER="${1:?embedder registry name}"; PANEL="${2:?panel name (data/panels/<name>.h5ad)}"; shift 2
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
SCFM_IRT="${SCFM_IRT:-$REPO_ROOT/../scfm-irt}"
SCFM_IRT="$(cd "$SCFM_IRT" && pwd)"
VCB_PY="${VCB_PY:-$REPO_ROOT/.venv/bin/python}"
PANEL_FILE="data/panels/${PANEL}.h5ad"
RUN="repr_${PANEL}"
[ "$PANEL" = "ts2_panel_v0" ] && RUN="repr_pool_v0"
[ -f "$PANEL_FILE" ] || { echo "[fm] missing $PANEL_FILE"; exit 1; }
[ -d "runs/$RUN" ] || { echo "[fm] missing runs/$RUN (run the classical pool first)"; exit 1; }

# ---- resolve the model's venv and work-dir variables (mirrors scfm-irt/slurm/extract_new_model.slurm) ----
export SCFM_GENEFORMER_WORKDIR="$SCFM_IRT/cache/geneformer_workdir"
case "$EMBEDDER" in
  scgpt)              VENV=.venv-scgpt;           PYMOD=python/3.10.1; export SCFM_SCGPT_WORKDIR="$SCFM_IRT/cache/scgpt_workdir" ;;
  geneformer|geneformer_v2|geneformer_v2_316m) VENV=.venv-geneformer; PYMOD=python/3.10.1 ;;
  uce)                VENV=.venv-uce;             PYMOD=python/3.10.1; export SCFM_UCE_WORKDIR="$SCFM_IRT/cache/uce_workdir" ;;
  scimilarity)        VENV=.venv-scimilarity;     PYMOD=python/3.10.1; export SCFM_SCIMILARITY_WORKDIR="$SCFM_IRT/cache/scimilarity_workdir" ;;
  cellplm)            VENV=.venv-cellplm;         PYMOD=python/3.10.1; export SCFM_CELLPLM_WORKDIR="$SCFM_IRT/cache/cellplm_workdir" ;;
  scfoundation)       VENV=.venv-scfoundation;    PYMOD=python/3.10.1; export SCFM_SCFOUNDATION_WORKDIR="$SCFM_IRT/cache/scfoundation_workdir" ;;
  scprint|scprint2|scprint_small_v1|scprint_medium_v1|scprint_large_v1)
                      VENV=.venv-scprint;         PYMOD=python/3.10.1; export SCFM_SCPRINT_WORKDIR="$SCFM_IRT/cache/scprint_workdir"
                      export LAMINDB_STORAGE="$SCFM_IRT/cache/scprint_workdir/lamindb" LAMIN_CACHE_DIR="$SCFM_IRT/cache/scprint_workdir/lamin_cache" ;;
  transcriptformer)   VENV=.venv-transcriptformer; PYMOD=python/3.12.10; export SCFM_TRANSCRIPTFORMER_WORKDIR="$SCFM_IRT/cache/tf_workdir" ;;
  langcell)           VENV=.venv-langcell;        PYMOD=python/3.10.1; export SCFM_LANGCELL_WORKDIR="$SCFM_IRT/cache/langcell_workdir" ;;
  state)              VENV=.venv-state;           PYMOD=python/3.12.10; export SCFM_STATE_WORKDIR="$SCFM_IRT/cache/state_workdir" ;;
  *) echo "[fm] unknown embedder $EMBEDDER"; exit 1 ;;
esac
PY="$SCFM_IRT/$VENV/bin/python"
[ -x "$PY" ] || { echo "[fm] $PY missing: build it with  (cd $SCFM_IRT && bash scripts/setup_embedder_venv.sh ${VENV#.venv-})"; exit 1; }
# Quest keeps the interpreter's shared libraries behind a module; elsewhere the venv is self-contained.
if command -v module >/dev/null 2>&1; then
  module load "$PYMOD" 2>/dev/null || true
  case "$PYMOD" in python/3.10.1) export LD_LIBRARY_PATH="/software/python/3.10.1/lib:${LD_LIBRARY_PATH:-}";; python/3.12.10) export LD_LIBRARY_PATH="/software/python/3.12.10/lib:${LD_LIBRARY_PATH:-}";; esac
fi
export PYTHONPATH="$SCFM_IRT/src:${PYTHONPATH:-}"
export PATH="$SCFM_IRT/$VENV/bin:$PATH"   # embedders that shell out to a CLI (transcriptformer) find it here
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-$SCFM_IRT/cache/pip}"
mkdir -p logs cache/embeddings

NAME="fm_${EMBEDDER}"
case " $* " in *" --debug "*) NAME="${NAME}_debug";; esac
echo "[fm] $EMBEDDER on $PANEL -> cache/embeddings/$PANEL/$NAME.npz  (python $PY, gpu ${CUDA_VISIBLE_DEVICES:-all}) $(date)"
"$PY" scripts/extract_fm_embedding.py --panel "$PANEL_FILE" --embedder "$EMBEDDER" "$@"

# ---- frozen probe + Rasch, in this repo's own env ----
"$VCB_PY" scripts/append_repr_responses.py --panel "$PANEL_FILE" --run "$RUN" --embedding "$PANEL/$NAME" --respondent "$NAME"
if [ "${NAME}" != "fm_${EMBEDDER}" ]; then
  # a debug respondent must not stay in the run's response table
  "$VCB_PY" -c "import pandas as pd; p='runs/$RUN/responses.parquet'; d=pd.read_parquet(p); d[d.respondent_id!='$NAME'].to_parquet(p, index=False); print('[fm] debug rows removed from', p)"
elif [ "${SKIP_REFIT:-0}" != "1" ]; then
  if [ "${PLACE:-anchored}" = "refit" ]; then
    "$VCB_PY" scripts/fit_rasch.py repr --run "$RUN" > /dev/null      # full refit: moves the scale, reserved for version bumps
  else
    "$VCB_PY" scripts/place_anchored.py repr --run "$RUN" --respondents "$NAME"   # difficulties held fixed, published abilities unchanged
  fi
  "$VCB_PY" scripts/summarize.py repr --run "$RUN" > /dev/null || true
  grep -E "^\| (fm_|pca_k128|nystroem_k256_g0.5|scvi_k30|random_k32_s0)" "runs/$RUN/summary.md" | head -12
fi
echo "[fm] done $(date)"

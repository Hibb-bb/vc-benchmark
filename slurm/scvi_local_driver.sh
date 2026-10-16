#!/bin/bash
# scVI (3 settings) on each panel, appended to its run, then Rasch refit. Local (no scheduler) version of
# slurm/scvi_panels.slurm. One stream per GPU:
#   CUDA_VISIBLE_DEVICES=0 nohup bash slurm/scvi_local_driver.sh scbasecount_human_lung scbasecount_human_skin > logs/scvi_gpu0.log 2>&1 &
# Env: CPUS (default 8), MAX_EPOCHS (scvi default).
set -uo pipefail
cd "$(dirname "$0")/.."
export CPUS=${CPUS:-8}
export OMP_NUM_THREADS=$CPUS OPENBLAS_NUM_THREADS=$CPUS MKL_NUM_THREADS=$CPUS
mkdir -p logs cache/embeddings
for NAME in "$@"; do
  PANEL=data/panels/$NAME.h5ad; RUN=repr_$NAME
  echo "=== $NAME  $(date)"
  for cfg in "10 tissue" "30 tissue" "30 none"; do
    set -- $cfg
    EMB=scvi_k$1_b$2__$NAME
    if [ ! -f cache/embeddings/$EMB.npz ]; then
      .venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel $PANEL --latent $1 --batch $2 --out-name $EMB ${MAX_EPOCHS:+--max-epochs $MAX_EPOCHS} \
        > logs/scvi_${EMB}.log 2>&1 || { echo "scvi failed for $EMB (see logs/scvi_${EMB}.log)"; continue; }
      grep -E "^trained|^wrote" logs/scvi_${EMB}.log
    fi
    .venv/bin/python scripts/append_repr_responses.py --panel $PANEL --run $RUN --embedding $EMB --respondent scvi_k$1_b$2 2>&1 | grep -E "^scvi|Error|Traceback"
  done
  .venv/bin/python scripts/fit_rasch.py repr --run $RUN > logs/rasch_scvi_$NAME.log 2>&1
  .venv/bin/python scripts/summarize.py repr --run $RUN > /dev/null
  echo "scvi done for $NAME $(date)"
done
echo "=== driver done $(date)"

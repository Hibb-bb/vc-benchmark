#!/bin/bash
#SBATCH --account=p32234
#SBATCH --nodes=1 --ntasks=1
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
# Faithful STATE rerun on Parse. STAGE=data (CPU), train (GPU, resumable), predict (GPU).
#   sbatch --partition=normal --cpus-per-task=4 --mem=160G --time=08:00:00 --export=ALL,STAGE=data,FOLD=0 slurm/state_full.slurm
#   sbatch --partition=gengpu --gres=gpu:a100:1 --cpus-per-task=12 --mem=160G --time=12:00:00 --export=ALL,STAGE=train,FOLD=0 slurm/state_full.slurm
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
export PYTHONNOUSERSITE=1 WANDB_MODE=disabled
module load python/3.12.10 2>/dev/null || true
export LD_LIBRARY_PATH="/software/python/3.12.10/lib:${LD_LIBRARY_PATH:-}"
case "$STAGE" in
  data) .venv/bin/python scripts/state_full_fold_data.py --fold "$FOLD" ${EXTRA:-} ;;
  train|predict) .venv/bin/python scripts/run_state_full.py --fold "$FOLD" --stage "$STAGE" ${EXTRA:-} ;;
esac

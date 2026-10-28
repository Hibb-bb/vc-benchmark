#!/bin/bash
#SBATCH --job-name=statetx
#SBATCH --account=p32234
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:a100:1
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=160G --time=12:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
# One fold of a STATE transition-model respondent (scripts/run_state_tx.py).
#   sbatch --export=ALL,FOLD=0,MODEL=state,EXTRA="--debug" slurm/state_tx.slurm
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
module load python/3.12.10 2>/dev/null || true
export LD_LIBRARY_PATH="/software/python/3.12.10/lib:${LD_LIBRARY_PATH:-}"
export PYTHONNOUSERSITE=1 WANDB_MODE=disabled
.venv/bin/python scripts/run_state_tx.py --dataset "${DATASET:-parse_pbmc_cytokines}" --fold "${FOLD:?}" --model "${MODEL:-state}" ${EXTRA:-}

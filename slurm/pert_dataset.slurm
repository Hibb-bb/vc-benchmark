#!/bin/bash
#SBATCH --job-name=vcb-pert
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=12:00:00
#SBATCH --output=logs/pert_%x_%j.out
#SBATCH --error=logs/pert_%x_%j.err

# Build items + run the simple-model pool for one scPerturb dataset.
#   sbatch --export=ALL,DATASET=NormanWeissman2019_filtered --job-name=pert-norman slurm/pert_dataset.slurm
# Optional: SCHEME=context (multi-context datasets), MIN_CELLS=50, MEM override via sbatch --mem.
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
: "${DATASET:?set DATASET}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
if [ ! -f "data/items/${DATASET}.items.h5ad" ]; then
  $PY scripts/build_pert_items.py --dataset "$DATASET" --min-cells "${MIN_CELLS:-50}" --cells-per-condition "${CELLS_PER_CONDITION:-500}"
fi
for scheme in ${SCHEME:-perturbation}; do
  $PY scripts/run_pert_pool.py --dataset "$DATASET" --scheme "$scheme" --min-cells "${MIN_CELLS:-50}"
done

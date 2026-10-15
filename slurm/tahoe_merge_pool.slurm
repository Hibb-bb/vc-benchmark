#!/bin/bash
#SBATCH --job-name=vcb-tahoe-merge
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=180G
#SBATCH --time=1-12:00:00
#SBATCH --output=logs/tahoe_merge_%j.out
#SBATCH --error=logs/tahoe_merge_%j.err

# Merge the 48 Tahoe parts into items + cells, run the pool in both schemes, refit Rasch.
#   sbatch --dependency=afterok:<array job> slurm/tahoe_merge_pool.slurm
set -uo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
[ -f data/items/tahoe100m.items.h5ad ] || $PY scripts/tahoe_merge.py
$PY scripts/run_pert_pool.py --dataset tahoe100m --scheme perturbation
$PY scripts/run_pert_pool.py --dataset tahoe100m --scheme context
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "tahoe merge+pool done $(date)"

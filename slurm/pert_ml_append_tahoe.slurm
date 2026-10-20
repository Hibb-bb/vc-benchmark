#!/bin/bash
#SBATCH --job-name=vcb-pertml-append
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=120G --time=04:00:00
#SBATCH --output=logs/pertml_append_%j.out
#SBATCH --error=logs/pertml_append_%j.err
# After the Tahoe scVI rerun: score its predictions, refit both pooled scales, summarize.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
$PY scripts/append_pert_scores.py --dataset tahoe100m --respondent scvi_cf --scheme context || echo "APPEND FAIL scvi_cf tahoe100m"
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "pert ml append done $(date)"

#!/bin/bash
#SBATCH --job-name=vcb-parse-widen
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=120G --time=1-00:00:00
#SBATCH --output=logs/parse_widen_%j.out
#SBATCH --error=logs/parse_widen_%j.err
# Add the featured respondents (one-hot features) and the PCA-regression ladder to the Parse cytokine runs.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python; DS=${DS:-parse_pbmc_cytokines}
for scheme in context perturbation; do
  $PY scripts/run_pert_pool.py --dataset $DS --scheme $scheme --pool featured || exit 1
  $PY scripts/run_pert_pool.py --dataset $DS --scheme $scheme --pool pca_ladder || exit 1
done
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "parse widen done $(date)"

#!/bin/bash
#SBATCH --job-name=vcb-latent-test
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=48G --time=02:00:00
#SBATCH --output=logs/latent_test_%j.out
#SBATCH --error=logs/latent_test_%j.err
# Smoke test of the shared-encoder family on the smallest screens, written to runs/pert_latent_v0.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
$PY scripts/run_pert_pool.py --dataset TianKampmann2019_iPSC --scheme perturbation --pool latent --out-run pert_latent_v0
$PY scripts/run_pert_pool.py --dataset AdamsonWeissman2016_GSM2406681_10X010 --scheme perturbation --pool latent --out-run pert_latent_v0
echo "latent test done $(date)"

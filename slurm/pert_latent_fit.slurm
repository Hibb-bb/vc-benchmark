#!/bin/bash
#SBATCH --job-name=vcb-latent-fit
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=120G --time=06:00:00
#SBATCH --output=logs/latent_fit_%j.out
#SBATCH --error=logs/latent_fit_%j.err
# Joint Rasch fit of the main pool plus the shared-encoder family (runs/pert_joint_v0), then the A->B link analysis.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
$PY scripts/fit_rasch.py pert --run pert_joint_v0 --scores-from pert_pool_v0,pert_latent_v0
$PY scripts/link_repr_pert.py
echo "latent fit done $(date)"

#!/bin/bash
#SBATCH --job-name=vcb-anatomy
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=96G --time=04:00:00
#SBATCH --output=logs/anatomy_%j.out
#SBATCH --error=logs/anatomy_%j.err
# Anatomy of difficulty: confusions + ontology (A), reaction decomposition (B). Writes runs/anatomy_v0.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
.venv/bin/python scripts/item_anatomy.py
echo "anatomy done $(date)"

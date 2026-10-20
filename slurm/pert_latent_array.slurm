#!/bin/bash
#SBATCH --job-name=vcb-latent
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=180G --time=40:00:00
#SBATCH --array=0-19
#SBATCH --output=logs/latent_%A_%a.out
#SBATCH --error=logs/latent_%A_%a.err
# Shared-encoder perturbation respondents (latent_<embedder>) on every screen; one (dataset, scheme) per task,
# from configs/pert_latent_tasks.txt. Scores go to runs/pert_latent_v0; the joint fit is slurm/pert_latent_fit.slurm.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
read -r DS SCHEME CAP < <(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" configs/pert_latent_tasks.txt)
echo "task $SLURM_ARRAY_TASK_ID: $DS $SCHEME cap=$CAP $(date)"
.venv/bin/python scripts/run_pert_pool.py --dataset "$DS" --scheme "$SCHEME" --pool latent --cells-per-item "$CAP" --out-run pert_latent_v0 || echo "LATENT FAIL $DS $SCHEME"
echo "done $(date)"

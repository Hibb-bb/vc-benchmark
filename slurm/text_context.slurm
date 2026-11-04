#!/bin/bash
#SBATCH -A p32234
#SBATCH -p normal
#SBATCH -c 8
#SBATCH --mem=180G
#SBATCH -t 12:00:00
#SBATCH -J txt-ctx
#SBATCH -o logs/txt-ctx_%A_%a.out
#SBATCH -e logs/txt-ctx_%A_%a.err
#SBATCH --array=0-3
# Text cards on the unseen-combination split (scheme "context") for the non-cytokine screens that have one.
# Two versions per screen: text card in place of the built-in perturbation feature (txt4b), and text card added to the
# one-hot perturbation label (txt4boh). Scores go to runs/pert_text/predict_ctx; the published tables are not touched.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
DS=(SrivatsanTrapnell2020_sciplex3 tahoe100m FrangiehIzar2021_RNA McFarlandTsherniak2020)
D=${DS[$SLURM_ARRAY_TASK_ID]}
.venv/bin/python scripts/pert_text/predict_eval.py --dataset $D --scheme context --out runs/pert_text/predict_ctx
.venv/bin/python scripts/pert_text/predict_eval.py --dataset $D --scheme context --with-onehot --out runs/pert_text/predict_ctx
echo "$D done $(date)"

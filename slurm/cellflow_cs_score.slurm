#!/bin/bash
#SBATCH -A p32234
#SBATCH -p short
#SBATCH -c 4
#SBATCH --mem=64G
#SBATCH -t 2:00:00
#SBATCH -J cellflow-cs-score
#SBATCH -o logs/cellflow-cs-score_%j.out
# Score CellFlow with the combosciplex settings (one-hot vs text card) on the published scales.
cd "${SLURM_SUBMIT_DIR}"
.venv/bin/python scripts/pert_text/cellflow_score.py combosciplex

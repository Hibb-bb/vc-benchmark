#!/bin/bash
#SBATCH -A p32234
#SBATCH -p short
#SBATCH -c 4
#SBATCH --mem=64G
#SBATCH -t 2:00:00
#SBATCH -J cellflow-score
#SBATCH -o logs/cellflow-score_%j.out
# Score CellFlow (one-hot vs text card) and place both arms on the published scales.
cd "${SLURM_SUBMIT_DIR}"
.venv/bin/python scripts/pert_text/cellflow_score.py

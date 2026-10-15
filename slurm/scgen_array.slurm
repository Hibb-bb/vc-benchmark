#!/bin/bash
#SBATCH --job-name=vcb-scgen
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64G
#SBATCH --time=06:00:00
#SBATCH --array=0-14
#SBATCH --output=logs/scgen_%A_%a.out
#SBATCH --error=logs/scgen_%A_%a.err

# Component B ML respondent: scGen, one (dataset, fold) per array task, unseen-context scheme.
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
DATASETS=(FrangiehIzar2021_RNA McFarlandTsherniak2020 SrivatsanTrapnell2020_sciplex3)
ds=${DATASETS[$((SLURM_ARRAY_TASK_ID / 5))]}
fold=$((SLURM_ARRAY_TASK_ID % 5))
.venv-scvi/bin/python scripts/run_scgen.py --dataset "$ds" --fold "$fold"

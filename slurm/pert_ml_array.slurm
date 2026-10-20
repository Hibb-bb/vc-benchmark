#!/bin/bash
#SBATCH --job-name=vcb-pertml
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=qgpu2014
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=120G --time=08:00:00
#SBATCH --array=0-34
#SBATCH --output=logs/pertml_%A_%a.out
#SBATCH --error=logs/pertml_%A_%a.err
# Learned perturbation respondents (scVI counterfactual, scGen) in the unseen-combination scheme.
# One (script, dataset, fold) per array task, read from configs/pert_ml_tasks.txt.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
LINE=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" configs/pert_ml_tasks.txt)
echo "task $SLURM_ARRAY_TASK_ID: $LINE"
.venv-scvi/bin/python scripts/$LINE

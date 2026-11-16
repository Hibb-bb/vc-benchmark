#!/bin/bash
#SBATCH -A p32234
#SBATCH -p normal
#SBATCH -c 16
#SBATCH --mem=96G
#SBATCH -t 16:00:00
#SBATCH -J cpa-norm-cpu
#SBATCH -o logs/cpa-norm-cpu_%A_%a.out
#SBATCH -e logs/cpa-norm-cpu_%A_%a.err
#SBATCH --array=0-4
# Norman text-card CPA runs (one fold per task) on CPU, because the A100 queue was a day and a half long.
# Same settings as slurm/cpa_text.slurm; CPA uses the CPU when no GPU is visible.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
fold=$SLURM_ARRAY_TASK_ID
f=runs/pert_text/cpa/cpa_text/NormanWeissman2019_filtered.perturbation.fold$fold.npz
[ -f "$f" ] && { echo "done already: $f"; exit 0; }
.venv-cpa/bin/python scripts/run_cpa.py --dataset NormanWeissman2019_filtered --scheme perturbation --fold $fold --emb text \
  --min-cells 50 --text-dir runs/pert_text/emb --cells-per-item 200 --max-epochs 150

#!/bin/bash
#SBATCH -A p32234
#SBATCH -p normal
#SBATCH -c 8
#SBATCH --mem=180G
#SBATCH -t 24:00:00
#SBATCH -J txt-de
#SBATCH -o logs/txt-de_%A_%a.out
#SBATCH -e logs/txt-de_%A_%a.err
#SBATCH --array=0-11
# Refit the feature-driven pool on the unseen-perturbation split with the built-in features and with the text card,
# scoring the DE-gene metrics too (top-k DE precision and direction accuracy, Pearson and Spearman on DE genes).
# Built-in and text go to separate directories so the two tasks of a screen never write one table at once.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
SETS=("NormanWeissman2019_filtered 50 runs/pert_text/emb"
      "ReplogleWeissman2022_K562_essential 50 runs/pert_text/emb"
      "SrivatsanTrapnell2020_sciplex3 50 runs/pert_text/emb"
      "tahoe100m 50 runs/pert_text/emb"
      "parse_pbmc_cytokines 50 runs/pert_text/emb"
      "immune_dictionary 30 runs/pert_text/idict/emb")
i=$SLURM_ARRAY_TASK_ID
read ds mc emb <<< "${SETS[$((i / 2))]}"
if [ $((i % 2)) -eq 0 ]; then arm=builtin; flag=--builtin; else arm=text; flag=; fi
.venv/bin/python scripts/pert_text/predict_eval.py --dataset $ds --scheme perturbation --min-cells $mc --emb-dir $emb \
    --extra-metrics $flag --out runs/pert_text/de/$arm
echo "$ds $arm done $(date)"

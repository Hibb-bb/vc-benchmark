#!/bin/bash
#SBATCH -A p32234
#SBATCH -p gengpu
#SBATCH --gres=gpu:1
#SBATCH -c 8
#SBATCH --mem=160G
#SBATCH -t 12:00:00
#SBATCH -J cellflow-text
#SBATCH -o logs/cellflow-text_%A_%a.out
#SBATCH -e logs/cellflow-text_%A_%a.err
#SBATCH --array=0-69%10
# CellFlow (scripts/run_cellflow.py) with a one-hot perturbation vs the text card, one (dataset, split, fold, arm) per
# task: Norman (unseen perturbation), sciPlex3, Immune Dictionary and Tahoe-100M (both splits).
# Task i: set = i / 10, fold = (i % 10) / 2, even i = one-hot, odd i = text card.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
# dataset scheme min-cells text-dir cells-per-training-item
SETS=("NormanWeissman2019_filtered perturbation 50 runs/pert_text/emb 200"
      "SrivatsanTrapnell2020_sciplex3 perturbation 50 runs/pert_text/emb 100"
      "SrivatsanTrapnell2020_sciplex3 context 50 runs/pert_text/emb 100"
      "immune_dictionary perturbation 30 runs/pert_text/idict/emb 200"
      "immune_dictionary context 30 runs/pert_text/idict/emb 200"
      "tahoe100m perturbation 50 runs/pert_text/emb 30"
      "tahoe100m context 50 runs/pert_text/emb 30")
i=$SLURM_ARRAY_TASK_ID
set=${SETS[$((i / 10))]}; fold=$(((i % 10) / 2)); arm=$([ $((i % 2)) -eq 0 ] && echo onehot || echo text)
read ds scheme mc emb cpi <<< "$set"
f=runs/pert_text/cellflow/cellflow_$arm/$ds.$scheme.fold$fold.npz
[ -f "$f" ] && { echo "done already: $f"; exit 0; }
nvidia-smi --query-gpu=name --format=csv,noheader
.venv-cellflow/bin/python scripts/run_cellflow.py --dataset $ds --scheme $scheme --fold $fold --emb $arm --min-cells $mc --text-dir $emb --cells-per-item $cpi

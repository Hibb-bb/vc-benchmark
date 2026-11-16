#!/bin/bash
#SBATCH -A p32234
#SBATCH -p gengpu
#SBATCH --gres=gpu:1
#SBATCH -c 8
#SBATCH --mem=200G
#SBATCH -t 36:00:00
#SBATCH -J cellflow-cs
#SBATCH -o logs/cellflow-cs_%A_%a.out
#SBATCH -e logs/cellflow-cs_%A_%a.err
#SBATCH --array=0-69%10
# CellFlow with the model settings of its combosciplex example (scripts/run_cellflow.py --preset combosciplex), all
# training cells, one-hot perturbation vs text card. Training steps scale with dataset size (the example used 300k):
# Norman (84k cells) and Immune Dictionary (95k) 50k, sciPlex3 (733k) 100k, Tahoe-100M (1.7M) 150k.
# Task i: set = i / 10, fold = (i % 10) / 2, even i = one-hot, odd i = text card.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
# dataset scheme min-cells text-dir iterations
SETS=("NormanWeissman2019_filtered perturbation 50 runs/pert_text/emb 50000"
      "SrivatsanTrapnell2020_sciplex3 perturbation 50 runs/pert_text/emb 100000"
      "SrivatsanTrapnell2020_sciplex3 context 50 runs/pert_text/emb 100000"
      "immune_dictionary perturbation 30 runs/pert_text/idict/emb 50000"
      "immune_dictionary context 30 runs/pert_text/idict/emb 50000"
      "tahoe100m perturbation 50 runs/pert_text/emb 150000"
      "tahoe100m context 50 runs/pert_text/emb 150000")
i=$SLURM_ARRAY_TASK_ID
set=${SETS[$((i / 10))]}; fold=$(((i % 10) / 2)); arm=$([ $((i % 2)) -eq 0 ] && echo onehot || echo text)
read ds scheme mc emb iters <<< "$set"
f=runs/pert_text/cellflow/cellflow_cs_$arm/$ds.$scheme.fold$fold.npz
[ -f "$f" ] && { echo "done already: $f"; exit 0; }
nvidia-smi --query-gpu=name --format=csv,noheader
.venv-cellflow/bin/python scripts/run_cellflow.py --dataset $ds --scheme $scheme --fold $fold --emb $arm --min-cells $mc --text-dir $emb --preset combosciplex --iterations $iters

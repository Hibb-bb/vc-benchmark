#!/bin/bash
#SBATCH -A p32234
#SBATCH -p gengpu
#SBATCH --gres=gpu:a100:1          # torch 2.0.0+cu117 in .venv-cpa has no H100 (sm_90) kernels
#SBATCH -c 8
#SBATCH --mem=120G
#SBATCH -t 24:00:00
#SBATCH -J cpa-text
#SBATCH -o logs/cpa-text_%A_%a.out
#SBATCH -e logs/cpa-text_%A_%a.err
#SBATCH --array=0-49%8
# CPA with its own perturbation embedding vs a frozen text-card embedding (scripts/run_cpa.py), one
# (dataset, split, fold, arm) per task: Norman (unseen perturbation), sciPlex3 and Immune Dictionary (both splits).
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
# dataset scheme min-cells text-dir cells-per-training-item  (sciPlex3 has ~1,900 training items: 200 cells each gave
# 376k cells and ~7 min per epoch, so it is cut to 50; the Immune Dictionary to 100)
SETS=("NormanWeissman2019_filtered perturbation 50 runs/pert_text/emb 200"
      "SrivatsanTrapnell2020_sciplex3 perturbation 50 runs/pert_text/emb 50"
      "SrivatsanTrapnell2020_sciplex3 context 50 runs/pert_text/emb 50"
      "immune_dictionary perturbation 30 runs/pert_text/idict/emb 100"
      "immune_dictionary context 30 runs/pert_text/idict/emb 100")
i=$SLURM_ARRAY_TASK_ID
set=${SETS[$((i / 10))]}; fold=$(((i % 10) / 2)); arm=$([ $((i % 2)) -eq 0 ] && echo learned || echo text)
read ds scheme mc emb cpi <<< "$set"
f=runs/pert_text/cpa/cpa_$arm/$ds.$scheme.fold$fold.npz
[ -f "$f" ] && { echo "done already: $f"; exit 0; }
.venv-cpa/bin/python scripts/run_cpa.py --dataset $ds --scheme $scheme --fold $fold --emb $arm --min-cells $mc --text-dir $emb --cells-per-item $cpi --max-epochs 150

#!/bin/bash
#SBATCH -A p32234
#SBATCH -p normal
#SBATCH -c 8
#SBATCH --mem=180G
#SBATCH -t 24:00:00
#SBATCH -J idict-pert
#SBATCH -o logs/idict-pert_%j.out
#SBATCH -e logs/idict-pert_%j.err
# Immune Dictionary (mouse lymph node, in vivo) as a cytokine-perturbation set: item = (cytokine, cell type), mice pooled;
# control = PBS mice of the same cell type. Own run directory, so the published scales are untouched.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python; DS=immune_dictionary; RUN=pert_idict_v0
[ -f data/items/$DS.items.h5ad ] || $PY scripts/build_pert_items.py --dataset $DS --h5ad data/raw/immune_dictionary/immune_dictionary.h5ad --pert-col cytokine --control-label PBS --context-col cell_type --pert-type cytokine --cells-per-condition 100 --min-cells 30 || exit 1
for S in context perturbation; do
  $PY scripts/run_pert_pool.py --dataset $DS --scheme $S --min-cells 30 --out-run $RUN || exit 1
  $PY scripts/run_pert_pool.py --dataset $DS --scheme $S --min-cells 30 --out-run $RUN --pool mlp || exit 1
  $PY scripts/pert_text/predict_eval.py --dataset $DS --scheme $S --emb-dir runs/pert_text/idict/emb --out runs/pert_text/predict_idict || exit 1
done
$PY scripts/pert_text/predict_eval.py --dataset $DS --scheme context --with-onehot --emb-dir runs/pert_text/idict/emb --out runs/pert_text/predict_idict
$PY scripts/fit_rasch.py pert --run $RUN
$PY scripts/summarize.py pert --run $RUN > /dev/null
$PY scripts/pert_text/rank.py --pred runs/pert_text/predict_idict --pub-run $RUN --out runs/pert_text/rank_idict
echo "idict pert done $(date)"

#!/bin/bash
#SBATCH --job-name=vcb-parse-pert
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=180G --time=1-12:00:00
#SBATCH --output=logs/parse_pert_%j.out
#SBATCH --error=logs/parse_pert_%j.err
# Parse 10M PBMC as a cytokine-perturbation set: item = (cytokine, donor, cell type), control = PBS per (donor, cell type).
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python; DS=parse_pbmc_cytokines
[ -f data/items/$DS.items.h5ad ] || $PY scripts/build_pert_items.py --dataset $DS --h5ad data/raw/parse_pbmc/20260203_Parse_10M_PBMC_cytokines.h5ad --pert-col cytokine --control-label PBS --context-col "donor|cell_type" --pert-type cytokine --cells-per-condition 30 --min-cells 50 || exit 1
$PY scripts/run_pert_pool.py --dataset $DS --scheme context
$PY scripts/run_pert_pool.py --dataset $DS --scheme perturbation
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "parse pert done $(date)"

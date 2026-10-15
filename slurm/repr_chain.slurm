#!/bin/bash
#SBATCH --job-name=vcb-repr
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=160G
#SBATCH --time=1-12:00:00
#SBATCH --output=logs/repr_%j.out
#SBATCH --error=logs/repr_%j.err

# Component A: build the Tabula Sapiens v2 panel (donor-disjoint, stratified), run the
# embedding pool + frozen probe, fit Rasch (cell-level and stratum-binomial).
#   sbatch --dependency=afterok:<ts2_download_job> slurm/repr_chain.slurm
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
PANEL=data/panels/ts2_panel_v0.h5ad
[ -f "$PANEL" ] || $PY scripts/build_repr_panel.py --out "$PANEL"
$PY scripts/run_repr_pool.py --panel "$PANEL" --run repr_pool_v0
$PY scripts/fit_rasch.py repr --run repr_pool_v0

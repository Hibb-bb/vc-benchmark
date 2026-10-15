#!/bin/bash
#SBATCH --job-name=vcb-pert-sweep
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=160G
#SBATCH --time=2-00:00:00
#SBATCH --output=logs/pert_sweep_%j.out
#SBATCH --error=logs/pert_sweep_%j.err

# Process every verified scPerturb dataset that has no pool output yet, smallest first.
# Multi-context datasets also get the unseen-context scheme.
#   sbatch --dependency=afterany:<dl_job1>:<dl_job2> slurm/pert_sweep.slurm
set -uo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
MULTI="SrivatsanTrapnell2020_sciplex3 McFarlandTsherniak2020 FrangiehIzar2021_RNA"
for ok in $(ls -S -r data/raw/scperturb/*.h5ad.ok); do
  ds=$(basename "$ok" .h5ad.ok)
  if [ -f "runs/pert_pool_v0/${ds}.perturbation.scores.parquet" ]; then echo "[done] $ds"; continue; fi
  echo "=== $ds  $(date)"
  [ -f "data/items/${ds}.items.h5ad" ] || $PY scripts/build_pert_items.py --dataset "$ds" || { echo "[fail build] $ds"; continue; }
  $PY scripts/run_pert_pool.py --dataset "$ds" --scheme perturbation || echo "[fail pool] $ds"
  case " $MULTI " in *" $ds "*) $PY scripts/run_pert_pool.py --dataset "$ds" --scheme context || echo "[fail ctx] $ds";; esac
done
$PY scripts/fit_rasch.py pert --run pert_pool_v0 || true
$PY scripts/summarize.py pert --run pert_pool_v0 || true
echo "sweep finished $(date)"

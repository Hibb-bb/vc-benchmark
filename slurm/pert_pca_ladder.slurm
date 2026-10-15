#!/bin/bash
#SBATCH --job-name=vcb-pcaladder
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=120G --time=12:00:00
#SBATCH --output=logs/pcaladder_%j.out
#SBATCH --error=logs/pcaladder_%j.err
# Add the PCA-regression ladder (k = 2..200) to every scPerturb dataset's score tables, then refit.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
for f in $(ls -S -r data/items/*.items.h5ad); do
  ds=$(basename "$f" .items.h5ad)
  [ "$ds" = "tahoe100m" ] && continue
  echo "=== $ds $(date)"
  $PY scripts/run_pert_pool.py --dataset "$ds" --pool pca_ladder --scheme perturbation || echo "[fail] $ds"
  case $ds in SrivatsanTrapnell2020_sciplex3|McFarlandTsherniak2020|FrangiehIzar2021_RNA) $PY scripts/run_pert_pool.py --dataset "$ds" --pool pca_ladder --scheme context || echo "[fail ctx] $ds";; esac
done
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "pca ladder done $(date)"

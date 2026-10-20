#!/bin/bash
#SBATCH --job-name=vcb-pertml-append
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=120G --time=12:00:00
#SBATCH --output=logs/pertml_append_%j.out
#SBATCH --error=logs/pertml_append_%j.err
# After the GPU array: MLP merge on every screen (both schemes), score scVI/scGen predictions, refit, summarize.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
for f in data/items/*.items.h5ad; do ds=$(basename $f .items.h5ad)
  $PY scripts/run_pert_pool.py --dataset $ds --scheme perturbation --pool mlp || echo "MLP FAIL $ds perturbation"
  [ -f runs/pert_pool_v0/$ds.context.scores.parquet ] && { $PY scripts/run_pert_pool.py --dataset $ds --scheme context --pool mlp || echo "MLP FAIL $ds context"; }
done
for ds in tahoe100m parse_pbmc_cytokines McFarlandTsherniak2020 SrivatsanTrapnell2020_sciplex3 FrangiehIzar2021_RNA; do
  $PY scripts/append_pert_scores.py --dataset $ds --respondent scvi_cf --scheme context || echo "APPEND FAIL scvi_cf $ds"
  $PY scripts/append_pert_scores.py --dataset $ds --respondent scgen --scheme context || echo "APPEND FAIL scgen $ds"
done
$PY scripts/fit_rasch.py pert --run pert_pool_v0
$PY scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "pert ml append done $(date)"

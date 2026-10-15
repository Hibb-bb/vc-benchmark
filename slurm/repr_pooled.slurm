#!/bin/bash
#SBATCH --job-name=vcb-repr-pooled
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=64G --time=03:00:00
#SBATCH --output=logs/repr_pooled_%j.out
#SBATCH --error=logs/repr_pooled_%j.err
# Pooled component-A scale over all annotation panels (one item namespace per run).
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
RUN=${RUN:-repr_pooled_v1}
POOL=${POOL:-repr_pool_v0,repr_hao_pbmc_l2,repr_heart_states,repr_hlca_core_donor,repr_hlca_core_study,repr_immune_atlas_donor,repr_immune_atlas_tissue,repr_parse_pbmc_celltype}
.venv/bin/python scripts/fit_rasch.py repr --run $RUN --pool-runs $POOL
.venv/bin/python scripts/summarize.py repr --run $RUN > /dev/null
echo "pooled repr done $RUN $(date)"

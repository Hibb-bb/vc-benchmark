#!/bin/bash
#SBATCH --job-name=fm-place-pooled
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=120G --time=02:00:00
#SBATCH --output=logs/fm_%x_%j.out
#SBATCH --error=logs/fm_%x_%j.err
# Place the foundation-model respondents on the pooled representation scale from the curated panel runs on Quest.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
POOL="${POOL_RUNS:-repr_pool_v0,repr_hao_pbmc_l2,repr_heart_states,repr_hlca_core_donor,repr_hlca_core_study,repr_immune_atlas_donor,repr_immune_atlas_tissue,repr_parse_pbmc_celltype}"
.venv/bin/python scripts/place_anchored.py repr --run "${POOLED_RUN:-repr_pooled_v3}" --respondents auto --pool-runs "$POOL"

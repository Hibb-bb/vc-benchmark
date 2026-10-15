#!/bin/bash
#SBATCH --job-name=vcb-scvi-panels
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=qgpu2014
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=96G --time=06:00:00
#SBATCH --array=0-5
#SBATCH --output=logs/scvi_panels_%A_%a.out
#SBATCH --error=logs/scvi_panels_%A_%a.err
# scVI (3 settings) on each new annotation panel, appended to that panel's run, then refit.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
NAMES=(${PANELS:-hao_pbmc_l2 heart_states hlca_core_donor hlca_core_study immune_atlas_donor immune_atlas_tissue})
NAME=${NAMES[$SLURM_ARRAY_TASK_ID]}; PANEL=data/panels/$NAME.h5ad; RUN=repr_$NAME
for cfg in "10 tissue" "30 tissue" "30 none"; do
  set -- $cfg
  .venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel $PANEL --latent $1 --batch $2 --out-name scvi_k$1_b$2__$NAME
  .venv/bin/python scripts/append_repr_responses.py --panel $PANEL --run $RUN --embedding scvi_k$1_b$2__$NAME --respondent scvi_k$1_b$2
done
.venv/bin/python scripts/fit_rasch.py repr --run $RUN
.venv/bin/python scripts/summarize.py repr --run $RUN > /dev/null
echo "scvi done for $NAME $(date)"

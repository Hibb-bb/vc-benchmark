#!/bin/bash
#SBATCH --job-name=vcb-fm
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=120G --time=12:00:00
#SBATCH --output=logs/fm_%x_%j.out
#SBATCH --error=logs/fm_%x_%j.err
# Foundation-model respondent on one panel (Quest).
#   sbatch --export=ALL,EMBEDDER=scgpt,PANEL=hao_pbmc_l2 --job-name=fm-scgpt-hao slurm/fm_embed.slurm
#   EXTRA="--debug" or "--batch-size 16 --chunk 10000" is passed through to the extractor.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export SCFM_IRT="${SCFM_IRT:-/gpfs/projects/p32593/scfm-irt}"
bash slurm/fm_embed.sh "${EMBEDDER:?}" "${PANEL:?}" ${EXTRA:-}

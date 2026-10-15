#!/bin/bash
#SBATCH --job-name=vcb-scvi
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:a100:1
#SBATCH --exclude=qgpu2014
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=08:00:00
#SBATCH --output=logs/scvi_%j.out
#SBATCH --error=logs/scvi_%j.err

# Component A ML respondents: scVI at three settings, then probe + Rasch + summary.
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
PANEL=data/panels/ts2_panel_v0.h5ad
for cfg in "10 tissue" "30 tissue" "30 none"; do
  set -- $cfg
  .venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel $PANEL --latent $1 --batch $2
  .venv/bin/python scripts/append_repr_responses.py --panel $PANEL --run repr_pool_v0 --embedding scvi_k$1_b$2
done
.venv/bin/python scripts/fit_rasch.py repr --run repr_pool_v0
.venv/bin/python scripts/summarize.py repr --run repr_pool_v0 > /dev/null
echo "scvi chain done $(date)"

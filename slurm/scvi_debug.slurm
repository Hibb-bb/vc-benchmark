#!/bin/bash
#SBATCH --job-name=vcb-scvi-debug
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=qgpu2014
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=48G --time=00:40:00
#SBATCH --output=logs/scvi_debug_%j.out
#SBATCH --error=logs/scvi_debug_%j.err
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
.venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel data/panels/ts2_panel_v0.h5ad --latent 10 --batch tissue --debug
.venv/bin/python scripts/append_repr_responses.py --panel data/panels/ts2_panel_v0.h5ad --run repr_debug --embedding scvi_k10_btissue_debug
echo "=== debug done ==="

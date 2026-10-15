#!/bin/bash
#SBATCH --job-name=vcb-ml-debug
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=48G --time=01:00:00
#SBATCH --output=logs/ml_debug_%j.out
#SBATCH --error=logs/ml_debug_%j.err
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
nvidia-smi --query-gpu=name,driver_version,compute_mode,memory.used --format=csv,noheader; hostname
.venv-scvi/bin/python -c "import torch; print('cuda available', torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"
echo "=== scgen debug ==="
.venv-scvi/bin/python scripts/run_scgen.py --dataset FrangiehIzar2021_RNA --fold 0 --debug
echo "=== scvi debug ==="
.venv-scvi/bin/python scripts/extract_scvi_embedding.py --panel data/panels/ts2_panel_v0.h5ad --latent 10 --batch tissue --debug
.venv/bin/python scripts/append_repr_responses.py --panel data/panels/ts2_panel_v0.h5ad --run repr_debug --embedding scvi_k10_btissue_debug
echo "=== debug done ==="

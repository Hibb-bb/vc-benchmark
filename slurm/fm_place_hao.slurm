#!/bin/bash
#SBATCH --job-name=fm-place-hao
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=32G --time=01:00:00
#SBATCH --output=logs/fm_%x_%j.out
#SBATCH --error=logs/fm_%x_%j.err
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
.venv/bin/python scripts/place_anchored.py repr --run repr_hao_pbmc_l2 --respondents auto
.venv/bin/python scripts/summarize.py repr --run repr_hao_pbmc_l2 > /dev/null || true
grep -E "^\| (fm_|pca_k128|nystroem_k256_g0.5|scvi_k30|random_k32_s0)" runs/repr_hao_pbmc_l2/summary.md | head -24

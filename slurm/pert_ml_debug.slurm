#!/bin/bash
#SBATCH --job-name=vcb-pertml-debug
#SBATCH --account=p32593
#SBATCH --partition=gengpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=qgpu2014
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=48G --time=00:40:00
#SBATCH --output=logs/pertml_debug_%j.out
#SBATCH --error=logs/pertml_debug_%j.err
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
.venv-scvi/bin/python scripts/run_scvi_pert.py --dataset FrangiehIzar2021_RNA --fold 0 --debug || exit 1
.venv-scvi/bin/python scripts/run_scvi_pert.py --dataset parse_pbmc_cytokines --fold 0 --debug --cells-per-item 20 || exit 1
.venv/bin/python scripts/run_pert_pool.py --dataset TianKampmann2019_iPSC --scheme perturbation --pool mlp || exit 1
echo "debug done $(date)"

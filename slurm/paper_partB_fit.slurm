#!/bin/bash
#SBATCH --job-name=paper-partB
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=96G --time=01:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
# Paper-scope Part B fits (pooled + per-screen unseen-combination), without the 2026-10-20 respondents.
cd /gpfs/projects/p32593/vc-benchmark
.venv/bin/python scripts/paper_partB_fit.py && .venv/bin/python scripts/paper_stats.py > logs/paper_stats_last.txt 2>&1 && echo "[paper-partB] done"

#!/bin/bash
#SBATCH --job-name=vcb-tahoe
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --array=0-47%16
#SBATCH --output=logs/tahoe_%A_%a.out
#SBATCH --error=logs/tahoe_%A_%a.err

# Stream Tahoe-100M from HuggingFace: 48 tasks x ~71 shards, at most 16 concurrently.
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
export HF_HUB_DISABLE_TELEMETRY=1 HF_HUB_ENABLE_HF_TRANSFER=0
export TMPDIR=${TMPDIR:-/tmp/$USER/$SLURM_JOB_ID}
mkdir -p "$TMPDIR"
.venv/bin/python scripts/tahoe_shard_task.py --task "$SLURM_ARRAY_TASK_ID" --n-tasks 48

#!/bin/bash
#SBATCH --job-name=vcb-scgen-append
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/scgen_append_%j.out
#SBATCH --error=logs/scgen_append_%j.err

# After the scGen array: score every dataset, append to the context score tables, refit.
#   sbatch --dependency=afterok:<array job id> slurm/scgen_append.slurm
set -uo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
for ds in FrangiehIzar2021_RNA McFarlandTsherniak2020 SrivatsanTrapnell2020_sciplex3; do
  .venv/bin/python scripts/append_pert_scores.py --dataset $ds --respondent scgen --scheme context || echo "[fail] $ds"
done
.venv/bin/python scripts/fit_rasch.py pert --run pert_pool_v0
.venv/bin/python scripts/summarize.py pert --run pert_pool_v0 > /dev/null
echo "scgen append done $(date)"

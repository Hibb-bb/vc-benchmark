#!/bin/bash
#SBATCH --job-name=vcb-dl-cxg
#SBATCH --account=p32593
#SBATCH --partition=data-transfer
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=1-00:00:00
#SBATCH --output=logs/dl_cxg_%j.out
#SBATCH --error=logs/dl_cxg_%j.err

# Downloads Tabula Sapiens v2 (28 per-tissue h5ad, 57 GB) from figshare, smallest first,
# with resume + MD5 check. Safe to resubmit.
set -euo pipefail
REPO_ROOT="${SLURM_SUBMIT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
cd "$REPO_ROOT"
mkdir -p logs data/raw
.venv/bin/python scripts/download_data.py --group cellxgene_repr

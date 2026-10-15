#!/bin/bash
#SBATCH --job-name=vcb-dl-parse
#SBATCH --account=p32593
#SBATCH --partition=data-transfer
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=8G --time=2-00:00:00
#SBATCH --output=logs/dl_parse_%j.out
#SBATCH --error=logs/dl_parse_%j.err
# Parse Biosciences 10M PBMC (12 donors x 90 cytokines), CC BY-NC 4.0. Parallel byte-range
# download; integrity by `unzip -t`; extract; remove the zip.
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
D=data/raw/parse_pbmc; mkdir -p $D
for f in pseudobulks_20260203.zip 10M_PBMC_12donor_90cytokines_h5ad_20260203.zip; do
  [ -f "$D/$f.ok" ] && { echo "[skip] $f"; continue; }
  .venv/bin/python scripts/parallel_download.py "https://parse-wget.s3.us-west-2.amazonaws.com/10m/$f" "$D/$f" --threads 16 || { echo "[fail dl] $f"; continue; }
  if unzip -tq "$D/$f" > /dev/null; then
    unzip -o -q "$D/$f" -d "$D" && touch "$D/$f.ok" && rm -f "$D/$f" "$D/$f.parts" && echo "[ok] $f extracted"
  else
    echo "[fail zip test] $f"
  fi
done
ls -la "$D"; du -sh "$D"

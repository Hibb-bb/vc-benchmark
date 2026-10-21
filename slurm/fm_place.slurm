#!/bin/bash
#SBATCH --job-name=fm-place
#SBATCH --account=p32593
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=48G --time=01:00:00
#SBATCH --output=logs/fm_%x_%j.out
#SBATCH --error=logs/fm_%x_%j.err
# Anchored placement of every respondent in runs/repr_<PANEL>/responses.parquet that is not yet in its abilities table.
#   sbatch --export=ALL,PANEL=heart_states --job-name=fm-place-heart slurm/fm_place.slurm
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
RUN="repr_${PANEL:?}"; [ "$PANEL" = "ts2_panel_v0" ] && RUN="repr_pool_v0"
.venv/bin/python scripts/place_anchored.py repr --run "$RUN" --respondents auto
.venv/bin/python scripts/summarize.py repr --run "$RUN" > /dev/null || true
grep -E "^\| (fm_|pca_k128|nystroem_k256_g0.5|scvi_k30|random_k32_s0)" "runs/$RUN/summary.md" | head -24

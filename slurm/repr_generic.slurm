#!/bin/bash
#SBATCH --job-name=vcb-reprg
#SBATCH --account=p32593
#SBATCH --partition=normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=16 --mem=160G --time=1-12:00:00
#SBATCH --output=logs/reprg_%x_%j.out
#SBATCH --error=logs/reprg_%x_%j.err

# Component A on any annotated h5ad: build panel -> classical pool + probe -> Rasch -> summary.
#   sbatch --export=ALL,NAME=hlca_core,H5AD=data/raw/cellxgene_repr/hlca_core.h5ad,LABEL=ann_finest_level,DONOR=donor_id,CONTEXT=study,SPLIT=context,COUNTS=raw --job-name=reprg-hlca slurm/repr_generic.slurm
# Optional: FILTER (pandas query), TEST_GROUPS, TEST_FRAC, TEST_CAP, TRAIN_CAP, MIN_STRATUM, RUN (default repr_<NAME>).
set -uo pipefail
cd "${SLURM_SUBMIT_DIR}"
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
PY=.venv/bin/python
: "${NAME:?}" "${H5AD:?}" "${LABEL:?}" "${DONOR:?}"
RUN=${RUN:-repr_${NAME}}
PANEL=data/panels/${NAME}.h5ad
ARGS=(--h5ad "$H5AD" --name "$NAME" --label-key "$LABEL" --donor-key "$DONOR" --counts "${COUNTS:-raw}" --split-by "${SPLIT:-donor}" --test-frac "${TEST_FRAC:-0.25}" --test-cap "${TEST_CAP:-50}" --train-cap "${TRAIN_CAP:-200}" --min-stratum "${MIN_STRATUM:-20}")
[ -n "${CONTEXT:-}" ] && ARGS+=(--context-key "$CONTEXT")
[ -n "${FILTER:-}" ] && ARGS+=(--filter "$FILTER")
[ -n "${TEST_GROUPS:-}" ] && ARGS+=(--test-groups "$TEST_GROUPS")
[ -f "$PANEL" ] || $PY scripts/build_repr_panel_generic.py "${ARGS[@]}" || exit 1
$PY scripts/run_repr_pool.py --panel "$PANEL" --run "$RUN"
$PY scripts/fit_rasch.py repr --run "$RUN"
$PY scripts/summarize.py repr --run "$RUN" > /dev/null
echo "repr chain done for $NAME $(date)"

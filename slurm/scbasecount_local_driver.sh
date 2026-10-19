#!/bin/bash
# Run the scBaseCount component-A slices end to end on a machine without a scheduler:
# concat per-sample h5ad (labels joined from the obs metadata table) -> panel -> pool -> Rasch -> summary.
#   nohup bash slurm/scbasecount_local_driver.sh human_blood human_lung ... > logs/driver_human.log 2>&1 &
# Env: CPUS (default 8), PER_FILE_CAP (3000), TEST_FRAC (0.4), TEST_CAP (100), TRAIN_CAP (200), MIN_STRATUM (20), ARC (/datasets/arc).
set -uo pipefail
cd "$(dirname "$0")/.."
ARC=${ARC:-/datasets/arc}
export CPUS=${CPUS:-8}
export OMP_NUM_THREADS=$CPUS OPENBLAS_NUM_THREADS=$CPUS MKL_NUM_THREADS=$CPUS
PY=.venv/bin/python
mkdir -p logs data/raw/scbasecount data/panels
for SLICE in "$@"; do
  echo "=== $SLICE  $(date)"
  case $SLICE in human*) ORG=Homo_sapiens;; mouse_*) ORG=Mus_musculus;; zebrafish_*) ORG=Danio_rerio;; fly_*) ORG=Drosophila_melanogaster;; *) echo "unknown organism for $SLICE"; continue;; esac
  LIST=data/raw/scbasecount/lists/${SLICE}.txt
  H5AD=data/raw/scbasecount/${SLICE}.h5ad
  if [ ! -f "$H5AD" ]; then
    $PY scripts/concat_h5ad.py --files "$LIST" --out "$H5AD" \
      --meta "$ARC/metadata/GeneFull_Ex50pAS/$ORG/sample_metadata.parquet" \
      --meta-cols tissue,tissue_ontology_term_id,disease,disease_ontology_term_id,perturbation,cell_line,organism,single_disease_confidence,tech_10x,czi_collection_id \
      --obs-meta "data/raw/scbasecount/labels_${ORG}.parquet" \
      --per-file-cap "${PER_FILE_CAP:-3000}" --min-cells 200 --filter "cell_type.notna() & (cell_type != '') & (cell_type != 'artefact')" \
      > "logs/concat_${SLICE}.log" 2>&1 || { echo "concat failed for $SLICE (see logs/concat_${SLICE}.log)"; continue; }
    tail -n 1 "logs/concat_${SLICE}.log"
  fi
  case $SLICE in *multitissue*) SPLIT=context;; *) SPLIT=donor;; esac
  NAME=scbasecount_${SLICE} H5AD=$H5AD LABEL=cell_type DONOR=srx_accession CONTEXT=tissue_ontology_term_id SPLIT=$SPLIT COUNTS=X \
    TEST_FRAC=${TEST_FRAC:-0.4} TEST_CAP=${TEST_CAP:-100} TRAIN_CAP=${TRAIN_CAP:-200} MIN_STRATUM=${MIN_STRATUM:-20} \
    bash slurm/local_run.sh slurm/repr_generic.slurm > "logs/chain_${SLICE}.log" 2>&1
  grep -E "^scbasecount_|repr chain done|Error|Traceback" "logs/chain_${SLICE}.log" | tail -n 3
done
echo "=== driver done $(date)"

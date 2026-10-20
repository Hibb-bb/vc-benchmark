#!/bin/bash
# Foundation-model respondents on a machine without a scheduler (the Arc workstation): one stream
# per GPU, every (embedder, panel) pair in turn, then the pooled refit.
#
#   nohup bash slurm/fm_local_driver.sh "scgpt geneformer_v2_316m uce state" \
#       "scbasecount_human200_blood scbasecount_human200_lung" > logs/fm_driver.log 2>&1 &
#
# Env: GPUS="0 1 2" (default: every GPU nvidia-smi lists), SCFM_IRT, EXTRA (passed to the extractor),
# POOL_RUNS (comma-separated runs for the pooled refit; default: the panels given, prefixed repr_).
set -uo pipefail
EMBEDDERS="${1:?space-separated embedders}"; PANELS="${2:?space-separated panel names}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$REPO_ROOT"; mkdir -p logs
GPUS="${GPUS:-$(nvidia-smi --query-gpu=index --format=csv,noheader 2>/dev/null | tr '\n' ' ')}"
GPUS="${GPUS:-0}"
jobs_list=(); for e in $EMBEDDERS; do for p in $PANELS; do jobs_list+=("$e $p"); done; done
n=${#jobs_list[@]}; i=0
for g in $GPUS; do
  (
    j=$i
    while [ $j -lt $n ]; do
      set -- ${jobs_list[$j]}
      echo "[gpu $g] $1 $2 $(date)"
      SKIP_REFIT=1 CUDA_VISIBLE_DEVICES=$g bash slurm/fm_embed.sh "$1" "$2" ${EXTRA:-} > "logs/fm_${1}_${2}.log" 2>&1 || echo "[gpu $g] FAIL $1 $2"
      j=$((j + $(echo $GPUS | wc -w)))
    done
  ) &
  i=$((i + 1))
done
wait
# refits in the light env, one panel at a time, then pooled
PY="${VCB_PY:-$REPO_ROOT/.venv/bin/python}"
runs=""
for p in $PANELS; do r="repr_$p"; [ "$p" = "ts2_panel_v0" ] && r="repr_pool_v0"; runs="$runs,$r"
  $PY scripts/fit_rasch.py repr --run "$r" > /dev/null && $PY scripts/summarize.py repr --run "$r" > /dev/null || echo "refit FAIL $r"
done
runs="${POOL_RUNS:-${runs#,}}"
$PY scripts/fit_rasch.py repr --run repr_pooled_fm_v0 --pool-runs "$runs" > /dev/null && $PY scripts/summarize.py repr --run repr_pooled_fm_v0 > /dev/null
echo "driver done $(date); pooled scale runs/repr_pooled_fm_v0"

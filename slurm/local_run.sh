#!/bin/bash
# Run one of the slurm/*.slurm job scripts on a machine without a scheduler, with the same
# Python commands. Env vars are passed exactly as with `sbatch --export`:
#   NAME=foo H5AD=... LABEL=cell_type DONOR=srx_accession bash slurm/local_run.sh slurm/repr_generic.slurm
# Runs in the foreground; wrap with nohup / a driver script for background use. CPUS (default 16).
set -uo pipefail
JOB=$1; shift
cd "$(dirname "$0")/.."
export SLURM_SUBMIT_DIR=$PWD SLURM_CPUS_PER_TASK=${CPUS:-16} SLURM_JOB_ID=${SLURM_JOB_ID:-local}
mkdir -p logs
echo "[local_run] $(date) $JOB NAME=${NAME:-} CPUS=$SLURM_CPUS_PER_TASK host=$(hostname)"
bash "$JOB"

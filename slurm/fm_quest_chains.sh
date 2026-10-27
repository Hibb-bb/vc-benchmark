#!/bin/bash
# Queue the foundation models on every curated panel on Quest: one sequential chain per panel (no two jobs
# append to one response table at once), per-panel anchored placement, then placement on the pooled scale.
#   bash slurm/fm_quest_chains.sh                       # all seven remaining panels, seven models
#   MODELS="scgpt uce" PANELS="heart_states" bash slurm/fm_quest_chains.sh
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
MODELS="${MODELS:-scgpt geneformer_v2_316m uce state scprint_large_v1 cellplm transcriptformer}"
PANELS="${PANELS:-ts2_panel_v0 heart_states hlca_core_donor hlca_core_study immune_atlas_donor immune_atlas_tissue parse_pbmc_celltype}"
place_ids=""
for p in $PANELS; do
  prev=""
  for m in $MODELS; do
    extra=""; case $m in scprint_large_v1|transcriptformer) extra="--batch-size 16";; esac
    dep=""; [ -n "$prev" ] && dep="--dependency=afterany:$prev"
    jid=$(sbatch --parsable $dep --export=ALL,EMBEDDER=$m,PANEL=$p,EXTRA="$extra",SKIP_REFIT=1 --job-name="fm-$m-$p" slurm/fm_embed.slurm)
    echo "$p $m -> $jid"; prev=$jid
  done
  pid=$(sbatch --parsable --dependency=afterany:$prev --export=ALL,PANEL=$p --job-name="fm-place-$p" slurm/fm_place.slurm)
  echo "$p placement -> $pid"; place_ids="${place_ids:+$place_ids:}$pid"
done
# name the respondents explicitly ("auto" once found nothing to place); space-separated for --export
resp=$(for m in $MODELS; do printf 'fm_%s ' "$m"; done)
pool=$(sbatch --parsable --dependency=afterany:$place_ids --export=ALL,RESPONDENTS="${resp% }" slurm/fm_place_pooled.slurm)
echo "pooled placement -> $pool"

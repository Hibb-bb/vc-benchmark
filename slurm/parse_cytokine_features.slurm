#!/bin/bash
#SBATCH --job-name=parse-cytfeat
#SBATCH --account=p32234
#SBATCH --partition=short
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8 --mem=96G --time=04:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
# Cytokine-gene-feature respondents on Parse, all sources in sequence (they merge into one scores table,
# so they must not run in parallel). The items tables are restored afterwards: evaluate_dataset rewrites
# them and would flip target_in_var for every Parse item.
set -euo pipefail
cd "${SLURM_SUBMIT_DIR}"
R=runs/pert_pool_v0
for s in context perturbation; do cp $R/parse_pbmc_cytokines.$s.items.parquet $R/parse_pbmc_cytokines.$s.items.parquet.bak; done
for src in ${SOURCES:-ctrlpca scgpt geneformer scfoundation esm2}; do
  .venv/bin/python scripts/run_parse_cytokine_features.py --source $src
done
for s in context perturbation; do mv $R/parse_pbmc_cytokines.$s.items.parquet.bak $R/parse_pbmc_cytokines.$s.items.parquet; done
# anchored placement on the Parse per-screen scales (published abilities and difficulties do not move)
resp=$(for src in ${SOURCES:-ctrlpca scgpt geneformer scfoundation esm2}; do for m in ridge_d50_lam100 knn_k20 gp_d50_ls1 mlp_h256_d50; do printf '%s_g%s,' $m $src; done; done)
.venv/bin/python scripts/place_anchored_pert.py --dataset parse_pbmc_cytokines --respondents "${resp%,}"
echo "[parse-cytfeat] done"

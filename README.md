# vc-benchmark

Living IRT benchmark for virtual cell models. Two components share one response format
`(item_id, respondent_id, k, n)` and one Rasch fitter.

| | Component A: representation | Component B: perturbation |
|---|---|---|
| item | one cell from a fixed donor-disjoint panel (Tabula Sapiens v2) | one (perturbation, context, dose, time) condition with >= 50 cells |
| respondent | an unsupervised embedding + the frozen probe | a predictor of the post-perturbation pseudobulk |
| response | probe labels the cell correctly (0/1) | metric beats the mean-shift baseline on that item (0/1) |
| pool | PCA / random projection / Nystroem / NMF / ICA / GMM ladders + floors | control-mean / mean-shift / target-KD / kNN / ridge / GP / low-rank ladders + floors |

Docs: `01_dataset_survey.md` (what exists), `02_plan.md` (the quarter plan),
`03_implementation.md` (what is built, how each respondent is trained, the splits).
Theory: `paper/paper2_rewrite.tex`.

## Layout

```
configs/datasets.yaml        download registry (URL, size, MD5 per file)
src/vcb/data/schema.py       common obs schema for perturbation sets
src/vcb/data/pert_items.py   raw h5ad -> items (condition pseudobulks) + cell subsample
src/vcb/data/repr_panel.py   Tabula Sapiens v2 -> stratified donor-disjoint panel
src/vcb/pert/{features,baselines,metrics,run}.py   component-B pool and cross-fitting
src/vcb/repr/{embedders,probe,run}.py              component-A pool and frozen probe
src/vcb/scoring.py           continuous score -> Rasch response (binary / graded)
src/vcb/irt/rasch.py         1PL fit (dichotomous + binomial), SEs, outfit
scripts/                     one CLI per stage; slurm/ one job per stage
data/raw|items|panels        inputs and derived item banks (not in git)
runs/<run>/                  long response tables, item covariates, rasch/ reports
```

## Run

```bash
# env
uv venv --python /software/2025/python/3.12.10/bin/python3.12 .venv
uv pip install --python .venv/bin/python -e . && uv pip install --python .venv/bin/python scanpy

# data
sbatch slurm/download_scperturb.slurm; sbatch --export=ALL,REVERSE=--reverse slurm/download_scperturb.slurm
sbatch slurm/download_ts2.slurm

# component B, one dataset
sbatch --export=ALL,DATASET=NormanWeissman2019_filtered slurm/pert_dataset.slurm
# ... or everything that has finished downloading
sbatch --dependency=afterany:<dl jobs> slurm/pert_sweep.slurm

# component A
sbatch --dependency=afterok:<ts2 dl job> slurm/repr_chain.slurm

# Rasch reports
.venv/bin/python scripts/fit_rasch.py pert --run pert_pool_v0
.venv/bin/python scripts/fit_rasch.py repr --run repr_pool_v0
```

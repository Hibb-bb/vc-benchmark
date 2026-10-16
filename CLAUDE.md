# vc-benchmark: notes for Claude Code

Living Item Response Theory (IRT) benchmark for virtual cell models. Read `README.md` for the
layout and `03_implementation.md` for what each stage does and the results so far. Task-specific
runbooks live in `docs/` (for example `docs/remote_scbasecount.md` for evaluating scBaseCount on
another cluster).

## Setup on a new machine

```bash
uv venv --python 3.12 .venv            # or: python3.12 -m venv .venv
uv pip install -p .venv/bin/python -e . pyarrow   # or: .venv/bin/pip install -e . pyarrow
```

Only Python 3.12 or newer is supported (anndata 0.12, scanpy 1.12, scikit-learn 1.9 were used
here). `src/vcb/__init__.py` resolves `DATA = <repo>/data` and `RUNS = <repo>/runs`; keep raw
data under `data/raw/<source>/`, panels under `data/panels/`, run outputs under `runs/<run>/`.
`data/`, `logs/`, `cache/` and long response tables are git-ignored. Torch and scvi-tools live
in a separate `.venv-scvi` and are optional.

## How a component-A (representation) evaluation works

1. **Panel**: `scripts/build_repr_panel_generic.py` turns one annotated h5ad with raw counts into
   `data/panels/<name>.h5ad`. It needs three obs columns: the label (`--label-key`), the
   split unit (`--donor-key`: donor, sample, SRX accession ...) and optionally a context
   (`--context-key`: tissue, study, batch). Strata are context x label x donor; each stratum
   is capped (`--train-cap`, `--test-cap`) and dropped below `--min-stratum` cells.
   `--split-by donor` holds out whole donors; `--split-by context` holds out whole contexts.
2. **Pool**: `scripts/run_repr_pool.py --panel ... --run repr_<name>` preprocesses once
   (HVG, log, scale on train cells), fits 27 classical embeddings (PCA, ICA, NMF, Nystroem,
   random projection, GMM, depth and random floors) and scores every test cell with a frozen
   multinomial probe. Output: `runs/repr_<name>/responses.parquet` (item_id, respondent_id,
   k, n, p_true, pred, dataset_id) and `items.parquet` (item covariates).
3. **Rasch**: `scripts/fit_rasch.py repr --run repr_<name>` fits the 1PL model at cell level
   and at stratum level (binomial); `scripts/summarize.py repr --run repr_<name>` writes
   `runs/repr_<name>/summary.md`. Several runs go on one scale with
   `fit_rasch.py repr --run repr_pooled_vN --pool-runs a,b,c` (item ids are namespaced by run).
4. `slurm/repr_generic.slurm` chains 1 to 3 (env vars NAME, H5AD, LABEL, DONOR, CONTEXT, SPLIT,
   COUNTS, FILTER, TEST_CAP, TRAIN_CAP, MIN_STRATUM). Adapt `#SBATCH` account, partition and
   paths to the local cluster; the Python commands are the same everywhere.
   `TEST_FRAC` (default 0.25) sets the share of cells whose donors/contexts are held out. Without
   a scheduler, `slurm/local_run.sh slurm/repr_generic.slurm` runs the same chain in the foreground
   (wrap in `nohup`), and `slurm/scbasecount_local_driver.sh` chains concat + panel + pool + Rasch
   for scBaseCount slices.
5. Learned embeddings are added afterwards: `scripts/extract_scvi_embedding.py` (in
   `.venv-scvi`) then `scripts/append_repr_responses.py --respondent <name>` and a refit.
   `slurm/scvi_panels.slurm` does the three standard settings per panel; without a scheduler,
   `slurm/scvi_local_driver.sh <panel ...>` runs the same loop (one stream per GPU via
   `CUDA_VISIBLE_DEVICES`).

Component B (perturbation) follows the same pattern with `scripts/build_pert_items.py`
(`--h5ad --pert-col --control-label --context-col`), `scripts/run_pert_pool.py`,
`scripts/fit_rasch.py pert`.

## Conventions

- Respondent names are stable strings shared across runs (`pca_k128`, `scvi_k30_bnone`, ...);
  `src/vcb/names.py` maps them to display names. Never rename a respondent in one run only.
- A new dataset gets a short snake_case name used for the panel, the run (`repr_<name>`) and
  `dataset_id`. Record the source, licence and the obs columns used in `03_implementation.md`.
- Keep panels in the tens of thousands of test items (TEST_CAP 50 to 100 per stratum); the
  probe on 150k train cells takes about 1.5 h on 16 CPUs, Rasch fits take seconds.
- Do not commit anything under `data/`; results to share are `runs/<run>/responses.parquet`,
  `items.parquet` and `rasch/` (parquet files are git-ignored, so use `git add -f` for the two
  small parquet files when shipping a run back, and keep them under GitHub's 100 MB limit).
- Login nodes kill large processes; run anything that touches a full h5ad under the scheduler.
  On a dedicated workstation without Slurm (e.g. the Arc workspace) run it directly with `nohup`.
- The `.gitignore` rule for data is anchored (`/data/`); `src/vcb/data/` is source and must be
  committed (the unanchored rule had silently dropped it from the first commit).

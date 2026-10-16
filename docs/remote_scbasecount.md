# Runbook: evaluating scBaseCount as component-A panels (remote cluster)

Goal: add scBaseCount (Arc Institute, uniformly reprocessed SRA single-cell data) to the
representation item bank. The output we need back is one or more runs
`runs/repr_scbasecount_<slice>/` containing `responses.parquet`, `items.parquet`, `rasch/` and
`summary.md`, built with the code in this repo so the respondent names match and the runs can
be pooled onto the shared scale with `fit_rasch.py repr --pool-runs`.

Read `CLAUDE.md` first. Everything below runs in `.venv` (Python 3.12) created as described
there. Do not modify `src/vcb/repr/*` or the respondent pool; only add data-loading code.

## 0. Inspect what was downloaded (before anything else)

scBaseCount ships STARsolo output per SRX sample (feature types `Gene`, `GeneFull*`,
`Velocyto`) plus sample-level metadata parquet tables (columns include `srx_accession`,
`organism`, `tissue`, `disease`, `perturbation`, `cell_line`, `cell_prep`, `lib_prep`,
`tech_10x`, `obs_count`, `file_path`; later releases add `tissue_ontology_term_id`,
`disease_ontology_term_id`, `single_disease_confidence`). Cell-type labels (`cell_type`,
`cell_type_ontology_term_id`) exist only in the publication release and are "if available".
Record exactly what is present:

```bash
find <download_dir> -maxdepth 3 | head -50
ls <download_dir>/**/*.parquet
.venv/bin/python - <<'PY'
import anndata as ad, glob, pandas as pd
f = sorted(glob.glob("<download_dir>/**/*.h5ad", recursive=True))[0]
a = ad.read_h5ad(f, backed="r")
print(a); print(a.obs.head()); print(a.var.head()); print(a.X[:5].toarray().max())
for m in glob.glob("<download_dir>/**/*.parquet", recursive=True):
    d = pd.read_parquet(m); print(m, d.shape); print(d.columns.tolist()); print(d.head(3).T)
PY
```

Decide and write down:

- **Counts**: which feature type (prefer `GeneFull_Ex50pAS` if present, else `Gene`) and
  that `X` is integer counts (the panel builder warns if not).
- **Genes**: whether `var` is indexed by Ensembl ids or symbols. Either works within a panel
  (every panel is self-contained); if a `feature_name`/`gene_symbols` column exists the
  builder will use it as the index.
- **Label**: the cell-type column. In the 2026-01-12 release the per-sample h5ad files carry an
  `obs.cell_type` column that is *empty* for every cell; the real labels (`cell_type`,
  `cell_ontology_term_id`) are in `metadata/GeneFull_Ex50pAS/<organism>/obs_metadata.parquet`
  (one row per cell, keyed by `SRX_accession` + `cell_barcode`; 302 M rows / 6 GB for human).
  Pull the rows for the selected samples into a small parquet (row-group streaming with pyarrow,
  about 2 min) and pass it to `concat_h5ad.py --obs-meta`, which overwrites the empty h5ad
  columns. If a future release has no labels anywhere, stop and report back.
- **Split unit**: `srx_accession` (one sample = one donor/library) is the donor key.
- **Context**: `tissue` (and optionally `disease` or the study/BioProject id if present).

## 1. Choose slices

Do not build one giant panel. Build one panel per slice so that difficulty can be compared
across sources, keeping each panel at roughly 20k to 60k cells and 10k to 40k test items:

| slice name | filter (pandas query on sample metadata) | split | why |
|---|---|---|---|
| `scbasecount_human_<tissue>` for the 3 to 5 largest human tissues with labels | `organism == "Homo sapiens" and tissue == "<tissue>" and cell_type.notna()` | by sample (`SPLIT=donor`) | donor-held-out annotation, comparable to the CELLxGENE atlases |
| `scbasecount_human_multitissue_tissueheldout` | human, labelled, 8 to 15 tissues | `SPLIT=context` with CONTEXT=tissue | cross-tissue transfer |
| `scbasecount_mouse_<tissue>` (one or two) | `organism == "Mus musculus" ...` | by sample | first non-human panel |
| `scbasecount_human_disease_heldout` (optional) | labelled, several diseases | `SPLIT=context` with CONTEXT=disease | disease-held-out transfer |

Prefer samples with `single_disease_confidence == "high"` when that column exists. Exclude
`perturbation != "none"` and `cell_line` samples from annotation panels (they are component-B
material; see step 5).

## 2. Build one h5ad per slice

Per-SRX files are concatenated with the helper (inner join on genes, per-sample cap, metadata
join). Run it under the scheduler (memory: roughly 1 GB per 10k cells kept):

```bash
.venv/bin/python scripts/concat_h5ad.py \
  --glob '<download_dir>/<feature_type>/Homo_sapiens/*.h5ad' \
  --meta <download_dir>/<sample_metadata>.parquet --meta-key srx_accession \
  --meta-cols tissue,disease,perturbation,cell_line,organism,single_disease_confidence \
  --sample-key srx_accession --per-file-cap 3000 --min-cells 200 \
  --filter "cell_type.notna()" \
  --out data/raw/scbasecount/human_lung.h5ad
```

Select files from the sample metadata and pass them as a list: `--files list.txt` (one path per
line) replaces `--glob`. Filter on `tissue_ontology_term_id` (UBERON) rather than the free-text
`tissue` (dozens of spellings of PBMC), and treat `perturbation` / `cell_line` as free text
matched by regex (`none`, `none reported`, `not applicable`, `untreated`, ...). The script reads
only `X`, `obs` and `var` of each file; the two multi-mapper layers that make up two thirds of
every file are skipped.

## 3. Panel, pool, Rasch

Copy `slurm/repr_generic.slurm`, change `#SBATCH` lines for the local cluster (16 CPUs,
120 to 160 GB, several hours), and submit per slice. On a machine without a scheduler use
`slurm/local_run.sh <job script>` with the same env vars, or `slurm/scbasecount_local_driver.sh
<slice ...>` which chains concat, panel, pool and Rasch for the slice lists in
`data/raw/scbasecount/lists/`. With 60 samples per slice, 40 % held out (`TEST_FRAC=0.4`) and
`TEST_CAP=100`, a panel has 11k to 21k test items and the whole chain takes 3 to 5 min on 8 CPUs.

```bash
sbatch --export=ALL,NAME=scbasecount_human_lung,H5AD=data/raw/scbasecount/human_lung.h5ad,\
LABEL=cell_type,DONOR=srx_accession,CONTEXT=tissue,SPLIT=donor,COUNTS=X,\
TEST_CAP=50,TRAIN_CAP=200,MIN_STRATUM=20 --job-name=reprg-scb-lung slurm/repr_generic.slurm
```

For a context-held-out slice use `SPLIT=context` (and `CONTEXT=tissue` or `disease`). The chain
prints the panel summary (`train / test; strata; types; unseen types`), one accuracy line per
respondent, then writes `runs/repr_<NAME>/`. Sanity checks on each run:

- top raw accuracy well above chance and `random_k32_*` near chance (`summary.md`);
- `pca_k128`, `nystroem_k256_g0.5`, `ica_k64` within about 0.3 logits of each other at the
  top (that is the pattern on every panel so far); if a floor model is high, labels are leaking
  through depth or the split is wrong;
- share of items passed by no model: report it (20 to 40 % is typical for noisy labels).

## 4. Ship results back

```bash
git checkout -b scbasecount-runs
git add -f runs/repr_scbasecount_*/responses.parquet runs/repr_scbasecount_*/items.parquet
git add runs/repr_scbasecount_*/rasch runs/repr_scbasecount_*/summary.md
git commit -m "scBaseCount component-A runs: <slices>" && git push -u origin scbasecount-runs
```

Also append a short section to `03_implementation.md` (dataset version/release date, feature
type, slices, filters, panel sizes, top abilities, oddities) and, if any scripts were changed
or added, note them there. Do not push the h5ad or panel files.

## 5. Optional: component-B items from perturbation studies

Samples with `perturbation != "none"` that share a study with control samples can become
perturbation items (`scripts/build_pert_items.py --h5ad ... --pert-col perturbation
--control-label <control label> --context-col "tissue|cell_type"`). This needs a study id to
pair controls with treated samples and consistent perturbation labels, which scBaseCount's
LLM-extracted metadata may not give. Inspect feasibility and report before building.

## Compute expectations (from the panels built so far)

| step | size | time | memory |
|---|---|---|---|
| concat 200 SRX x 3k cells | 600k cells | 10 to 20 min | 40 to 60 GB |
| panel build | 60k cells kept | 5 to 15 min | depends on file size |
| pool + probe | 45k train / 17k test | 6 min | 11 GB |
| pool + probe | 147k train / 20k test | 90 min | 40 GB |
| Rasch fits | any | seconds to minutes | small |

## 6. scVI on the scBaseCount panels

With a GPU, `slurm/scvi_local_driver.sh <panel ...>` (or `slurm/scvi_panels.slurm` under Slurm)
trains the three standard scVI settings on each panel's train cells, embeds train and test cells,
appends `scvi_k10_btissue`, `scvi_k30_btissue`, `scvi_k30_bnone` to the run and refits Rasch.
`.venv-scvi` is built with `python3 -m venv .venv-scvi && .venv-scvi/bin/pip install torch
--index-url https://download.pytorch.org/whl/cu126 && .venv-scvi/bin/pip install scvi-tools scanpy
pyarrow -e .`. On the single-tissue panels `tissue` has one category, so the two latent-30 settings
differ only by seed path; they are kept so respondent names stay identical across runs.

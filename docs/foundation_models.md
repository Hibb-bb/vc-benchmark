# Runbook: foundation-model respondents on the representation panels (any machine)

Goal: place single-cell foundation models (scGPT, Geneformer, UCE, STATE, scPRINT, ...) on the
component-A scale next to the classical pool and scVI, starting with the scBaseCount `human200`
panels. The output to ship back is, per panel, `runs/repr_<panel>/responses.parquet` with new rows
`respondent_id = fm_<model>` plus the refit `rasch/` and `summary.md`, exactly as the scVI route.

Read `CLAUDE.md` first. The models and their isolated environments come from the sibling repository
`scfm-irt` (https://github.com/Hibb-bb/scfm-irt; on Quest `/gpfs/projects/p32593/scfm-irt`). Nothing
in this repo imports a model: `scripts/extract_fm_embedding.py` runs *inside* a scfm-irt venv and writes
`cache/embeddings/fm_<model>.npz`; `scripts/append_repr_responses.py` runs the frozen probe in this
repo's `.venv`; `fit_rasch.py` refits. `slurm/fm_embed.sh` chains the three.

## 0. What exists in scfm-irt (do not rebuild)

| registry name | model | venv | weights under `cache/` | needs | batch size default |
|---|---|---|---|---|---|
| `scgpt` | scGPT whole-human | `.venv-scgpt` | `scgpt_workdir/scGPT_human` | symbols | 64 |
| `geneformer_v2_316m` (`geneformer_v2`, `geneformer`) | Geneformer V2 316M (104M, V1 10M) | `.venv-geneformer` | `geneformer_workdir/Geneformer` | Ensembl ids | 32 |
| `uce` | UCE 4-layer | `.venv-uce` | `uce_workdir/UCE` | symbols, raw counts | 25 |
| `state` | STATE SE-600M | `.venv-state` | `state_workdir/SE-600M` | symbols | model default |
| `scprint_small_v1` / `scprint_medium_v1` / `scprint_large_v1` / `scprint` (medium v1.5) / `scprint2` (small v2) | scPRINT | `.venv-scprint` | `scprint_workdir/*.ckpt` + lamindb | Ensembl ids | 32 (16 large) |
| `scfoundation` | scFoundation | `.venv-scfoundation` | `scfoundation_workdir/scFoundation` | symbols (19k vocabulary) | model default |
| `cellplm` | CellPLM 85M | `.venv-cellplm` | `cellplm_workdir/ckpt` | symbols | 128 |
| `transcriptformer` | TranscriptFormer sapiens | `.venv-transcriptformer` | `tf_workdir/checkpoints` | Ensembl ids | 8 |
| `scimilarity` | SCimilarity v1.1 | `.venv-scimilarity` | `scimilarity_workdir/model_v1.1` | symbols | model default |
| `langcell` | LangCell | `.venv-langcell` | `langcell_workdir` + Geneformer dictionaries | Ensembl ids | 32 |

`scimilarity` and `langcell` were trained with cell-type labels (`label_supervised = True` in their
embedder classes): keep them on the scale but report them apart from the zero-shot models and never
use them as anchors. The embedder code is `scfm-irt/src/scfm_irt/embedders/<model>.py`; the registry
is `registry.py`; every class follows `preprocess(adata) -> fit (no-op) -> embed(adata) -> (n, d)`,
rows aligned to `obs_names`.

Priority order for the first pass: `scgpt`, `geneformer_v2_316m`, `uce`, `state`, `scprint_large_v1`,
then `scfoundation`, `cellplm`, `transcriptformer`, and the two label-supervised ones last.

## 1. Set up on a new machine

The embedder code, downloaders and venv builder were pushed to `https://github.com/Hibb-bb/scfm-irt`
on 2026-10-20 (commit 44d75d3), so a clone works. The downloaded weights are not in git; copying
`cache/*_workdir` from Quest saves the downloads in step 1b but is optional: scGPT, Geneformer, scPRINT,
CellPLM, scFoundation and TranscriptFormer are under 3 GB each, UCE and STATE 12 GB each, SCimilarity
70 GB (skip it unless needed). The venvs are 5 to 9 GB each and must be rebuilt, not copied.

```bash
rsync -av quest:/gpfs/projects/p32593/scfm-irt/cache/scgpt_workdir ../scfm-irt/cache/   # optional, per model
```

```bash
# next to this repo (or set SCFM_IRT=/path/to/scfm-irt)
git clone https://github.com/Hibb-bb/scfm-irt ../scfm-irt
cd ../scfm-irt
```

The venv builder `scripts/setup_embedder_venv.sh` hard-codes Quest's interpreters
(`PY310=/software/python/3.10.1/bin/python`, `PY312=/software/2025/python/3.12.10/bin/python3.12`).
On another machine edit those two lines to local Python 3.10 and 3.12 binaries (uv can provide them:
`uv python install 3.10 3.12`, then `uv python find 3.10`), remove the `module load` lines, and run
one target at a time with network access:

```bash
bash scripts/setup_embedder_venv.sh scgpt
bash scripts/setup_embedder_venv.sh geneformer
bash scripts/setup_embedder_venv.sh uce
bash scripts/setup_embedder_venv.sh state
bash scripts/setup_embedder_venv.sh scprint
```

Each venv must import `scfm_irt` (the builder installs the repo in editable mode; if not,
`<venv>/bin/pip install -e . --no-deps`). Then download weights into `cache/` (sizes are a few hundred
MB to a few GB each; scPRINT also populates a lamindb instance on first use):

```bash
.venv-scgpt/bin/python scripts/download_scgpt_assets.py          # Google Drive via gdown
.venv-geneformer/bin/python scripts/download_geneformer_assets.py
.venv-uce/bin/python scripts/download_uce_assets.py
.venv-state/bin/python scripts/download_state_assets.py
.venv-scprint/bin/python scripts/download_scprint_assets.py --which all
```

Check one env before queueing anything: `SCFM_IRT=../scfm-irt bash slurm/fm_embed.sh scgpt <small panel> --debug`
(2 % of cells; respondent `fm_scgpt_debug`, not refit). On Quest the same check is
`sbatch --export=ALL,EMBEDDER=scgpt,PANEL=hao_pbmc_l2,EXTRA="--debug" slurm/fm_embed.slurm`.

CUDA: the venvs pin torch builds for Quest's drivers (cu118 / cu121 / cu126). On a machine with another
driver generation, reinstall torch inside the failing venv with the matching index URL and nothing else.

## 2. Panels

Panels live in `data/panels/<name>.h5ad` with raw counts in `X`, `obs.split` (train / test),
`obs.type_in_train`, `obs.cell_type`; their classical runs are `runs/repr_<name>/` (the Tabula Sapiens
panel is `ts2_panel_v0` with run `repr_pool_v0`). The scBaseCount `human200` panels are on the Arc
workstation (built there, see `docs/remote_scbasecount.md` and section 7.7 of `03_implementation.md`):
`scbasecount_human200_{blood,lung,bone_marrow,skin,liver,multitissue}`, 50k to 180k training cells and
18k to 79k test cells each. Gene ids: the extractor accepts symbols as `var_names` with an Ensembl column,
or an Ensembl-indexed `var` with a `gene_symbols` / `feature_name` column, and prints which case it found.
If a panel has neither, the Ensembl-tokenised models fall back to Geneformer's dictionary or mygene
(online), which maps most but not all symbols; the extractor warns, and the run log of the embedder
reports how many genes matched its vocabulary. Below about 100 matched genes stop and fix the ids.

## 3. Run

One (model, panel) pair, embedding then probe then refit of that panel:

```bash
export SCFM_IRT=/path/to/scfm-irt
CUDA_VISIBLE_DEVICES=0 bash slurm/fm_embed.sh scgpt scbasecount_human200_blood
```

Everything, one stream per GPU, then the per-panel refits and one pooled scale
`runs/repr_pooled_fm_v0` over the panels given (set `POOL_RUNS` to pool other runs in as well):

```bash
nohup bash slurm/fm_local_driver.sh \
  "scgpt geneformer_v2_316m uce state scprint_large_v1" \
  "scbasecount_human200_blood scbasecount_human200_bone_marrow scbasecount_human200_lung scbasecount_human200_skin scbasecount_human200_liver scbasecount_human200_multitissue" \
  > logs/fm_driver.log 2>&1 &
```

Memory. The extractor embeds in chunks of 20,000 cells (`--chunk`) and writes each chunk to
`cache/embeddings/_parts/<name>/`, so a crash resumes. On 11 GB GPUs (RTX 2080 Ti) pass
`EXTRA="--batch-size 16"` for `scprint_large_v1`, `transcriptformer` and `scfoundation`, and
`--batch-size 8` if they still fail; scGPT, Geneformer, UCE, STATE and CellPLM run at their defaults.
Host memory: a 260k-cell panel is a few GB sparse, the embedders copy a chunk at a time. Expect roughly
one to three hours per large panel per model on a 2080 Ti (scGPT and UCE are the slow ones).

Respondent ids are `fm_<registry name>` (`fm_scgpt`, `fm_geneformer_v2_316m`, ...); display names and
the family "Foundation model" are in `src/vcb/names.py`. Never rename a respondent in one run only.

Placement. By default `fm_embed.sh` places the new respondent with every item difficulty held at its
current value (`scripts/place_anchored.py`, `placement = anchored` in the abilities table), so nothing
already published moves. `PLACE=refit` runs the full refit instead; that is reserved for scale version
bumps, because a refit shifts every ability by a common offset (about one logit on Hao PBMC when the
first two foundation models joined). To place several models appended with `SKIP_REFIT=1` in one go:
`python scripts/place_anchored.py repr --run repr_<panel> --respondents auto`. On a pooled scale use
`--run repr_pooled_v3 --pool-runs repr_a,repr_b` to gather the rows from the panel runs.

## 4. Check each run

`runs/repr_<panel>/summary.md` after the refit:

- `fm_*` rows sit somewhere between the random floor and the top of the classical ladder; a value
  below `depth2` means the gene mapping failed (vocabulary match near zero) or the embedding is constant.
- raw accuracy of the frozen probe is printed by `append_repr_responses.py` (`acc=`); compare with
  `pca_k128` on the same panel (`summary.md`), both are on identical items.
- outfit of the new respondent: 0.5 to 1.5 is normal; above 2 means its passes do not follow the
  scale's order (report it, do not drop it).
- `cache/embeddings/fm_<model>.json` records model version, dimension and runtime; keep it.

## 5. Ship back

```bash
git checkout -b fm-runs
git add -f runs/repr_scbasecount_human200_*/responses.parquet
git add runs/repr_scbasecount_human200_*/rasch runs/repr_scbasecount_human200_*/summary.md runs/repr_pooled_fm_v0/rasch runs/repr_pooled_fm_v0/summary.md
git add cache/embeddings/*.json      # sidecars only; the .npz embeddings stay out of git
git commit -m "Foundation-model respondents on scBaseCount human200 panels"
git push -u origin fm-runs
```

Back on Quest the runs are pooled with the rest (`fit_rasch.py repr --run repr_pooled_v4 --pool-runs ...`),
the contamination register is filled in (which of these models saw scBaseCount, CELLxGENE or Tabula
Sapiens in pretraining: scGPT, Geneformer, UCE, SCimilarity and STATE all trained on CELLxGENE-derived
corpora; note it per model in `03_implementation.md`), and the site is re-exported.

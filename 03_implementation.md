# Implementation notes, v0 (built 2026-10-13, runs completed 2026-10-14)

What exists, how each respondent is trained, what it is trained on, and how the data are
split. Component A = representation, component B = perturbation. Numbers in the Results
section are filled in as runs finish.

## 0. Environment and compute

- Python 3.12 venv at `.venv` (uv; scanpy 1.12, anndata 0.12, scikit-learn 1.9). No torch
  needed: the Rasch fit is numpy.
- Quest SLURM, account p32593. Downloads run on `data-transfer`; processing on `normal`
  (8 to 16 CPUs, 64 to 160 GB). Nothing in v0 needs a GPU.
- Storage: scPerturb subset 21 GB, Tabula Sapiens v2 57 GB, derived items and panels a few GB.

## 1. Data

### 1.1 Component B raw sets (scPerturb v1.4, Zenodo 13350497)

| dataset | type | context | note |
|---|---|---|---|
| ReplogleWeissman2022_K562_gwps | CRISPRi | K562 | genome-wide, ~10k perturbations; the item-count backbone |
| ReplogleWeissman2022_K562_essential | CRISPRi | K562 | standard unseen-perturbation split source |
| ReplogleWeissman2022_rpe1 | CRISPRi | RPE1 | only non-cancer line among the classics |
| NormanWeissman2019_filtered | CRISPRa | K562 | single + double perturbations |
| AdamsonWeissman2016_GSM2406681 | CRISPRi | K562 | small anchor candidate |
| NadigOConner2024_{jurkat,hepg2} | CRISPRi | Jurkat, HepG2 | newer, less contaminated |
| TianKampmann2019_{iPSC,day7neuron}, TianKampmann2021_CRISPRi | CRISPRi | iPSC, neurons | clean anchor candidates (not in most FM corpora) |
| FrangiehIzar2021_RNA | CRISPR KO | melanoma co-culture, 3 conditions | multi-context |
| SrivatsanTrapnell2020_sciplex3 | drug | A549, K562, MCF7; doses | chemical, multi-context |
| McFarlandTsherniak2020 | drug + CRISPRi | many lines | multi-context, few perturbations |

Excluded for now: X-Atlas/Orion (560 GB, storage), Tahoe-100M and VCC 2025 (requester-pays
GCS bucket; needs a GCP billing project), Gasperini (enhancer items are a different item
type).

### 1.2 Component A raw set

Tabula Sapiens v2 (figshare 27921984, CC BY 4.0): 28 per-tissue h5ad files, ~1.1M cells, 24
donors, `cell_ontology_class` labels, raw counts in `layers['raw_counts']`. v0 uses 10X cells
only.

### 1.3 Common schema (component B)

`src/vcb/data/schema.py` maps every raw obs to: `perturbation`, `targets` (|-joined gene
symbols), `pert_type` (CRISPRi/CRISPRa/CRISPR_KO/drug), `context`, `dose`, `dose_unit`,
`time_h`, `is_control`. An item key concatenates perturbation with whichever of context,
dose, time vary within the dataset.

## 2. Items

### 2.1 Component B items (`src/vcb/data/pert_items.py`)

- Cell QC: `ncounts >= 500`, `ngenes >= 200` (scPerturb ships unfiltered barcodes; e.g.
  Tian day-7 neurons keep 26k of 183k).
- An item is a condition with >= 50 QC cells (`min_cells`, recorded in obs so stricter
  thresholds can be applied downstream). Controls are kept per context.
- Response matrix for the item: the pseudobulk mean of log1p(CP10k) over all its cells,
  computed in one streaming pass (gene-chunked because scPerturb stores CSC). Also stored:
  per-context control mean and variance per gene, `delta_l2` (L2 norm of pseudobulk delta vs
  matched control) as an effect-size covariate, `n_cells`.
- A cell subsample (<= 500 cells per condition, 2000 per control) with raw counts is written
  alongside, for cell-level metrics later and for the gene embedding below.

### 2.2 Component A panel (`src/vcb/data/repr_panel.py`)

- Cells: 10X, with a cell-ontology label. Stratum = (tissue, cell type, donor).
- Donor split: donors are split globally into train and test (about 25 % of cells in test),
  chosen greedily so test donors cover as many tissues as possible. No donor appears in
  both. This is what stops the probe from learning donor identity.
- Caps: 50 test cells per stratum, 200 train cells per stratum, strata with < 20 cells
  dropped. Test cells whose type has no train cells are kept but flagged
  (`type_in_train = False`) and excluded from the probe.
- Items are the test cells; the training half exists only to fit the probe.

## 3. Respondents

### 3.1 Component B pool (`src/vcb/pert/baselines.py`)

All respondents predict the pseudobulk delta (perturbed mean minus matched control mean, in
log1p CP10k space, over all genes of the dataset). They are trained on the training folds'
items only. Inputs: item features F and training deltas D.

Features for genetic items (`features.py`): a 64-d target-gene embedding learned from
*control cells only*: genes as rows, up to 5000 control cells as columns, per-gene z-score,
PCA across cells. Multi-gene perturbations average their targets. Appended: control mean
expression and detection fraction of the target. Nothing from perturbed cells enters the
features, so there is no leakage. Chemical / categorical items get one-hot perturbation,
one-hot context and log-dose (this only supports the unseen-context scheme).

| respondent | trained on | prediction | capacity knob |
|---|---|---|---|
| control_mean | nothing | delta = 0 | floor |
| random_shift_s{0,1} | train deltas | a random train item's delta | floor (2 seeds) |
| mean_shift | train deltas | mean train delta, per context | Systema baseline; also the pass/fail reference |
| target_kd | train deltas + control mean | mean_shift, then target gene set to -80 % of control (CRISPRi/KO) or +50 % (CRISPRa) | cheap on-target biology |
| knn_k{1,5,20} | F, D | mean delta of k nearest train items (cosine on standardized F) | k |
| ridge_d{10,50}_lam{1,100} | F, D | ridge from F to PCA-d coordinates of train deltas, reconstructed to gene space (Ahlmann-Eltze style) | d, lambda |
| gp_d50_ls{0.5,2} | F (<= 3000 train items), D | GP with fixed RBF lengthscale (median heuristic x multiplier) + white noise, outputs = PCA-50 of deltas | lengthscale |
| lowrank_r{2,5,10} | D arranged as (perturbation x context) | soft-impute of the PCA-50 coordinate tensor; multi-context datasets only | rank |
| ridge_d50_lam100_tf{0.3,0.1}, knn_k20_tf{0.3,0.1} | a random 30 % / 10 % of the training items | same models, less training data | training fraction (the monotone ability axis) |

Dataset-specific handling that was needed: scPerturb labels every CRISPR screen "CRISPR",
so a per-dataset modality table sets CRISPRi / CRISPRa / KO (Norman is CRISPRa). Adamson
labels are guide-level strings (`<gene>_<plasmid>`) with non-targeting guides named
63(mod), 62(mod), Gal4-4(mod); they are collapsed to genes and controls. Frangieh's three
conditions (Control, Co-culture, IFNg) live in `perturbation_2` and become the context.
The genome-wide Replogle set needs a 100-cell cap per condition (9,327 conditions) to stay
under 170 GB during the item build.

### 3.2 Component A pool (`src/vcb/repr/embedders.py`)

Preprocessing is shared and fit on the train panel: log1p(CP10k), 2000 HVGs (seurat
flavor), per-gene z-score with train statistics, clip at 10. Every embedder has `fit` on
train cells and `transform` for any cells, so test cells never shape the embedding.

| respondent | fit on | embedding | knob |
|---|---|---|---|
| pca_k{4..256} | train HVG matrix | top-k PCs | k (7 levels) |
| rproj_k{8,32,128}_s{0,1} | train | Gaussian random projection | k, seed |
| nystroem_k{64,256}_g{0.5,2} | train PCA-50 | RBF Nystroem features | landmarks, bandwidth |
| nmf_k{16,64} | 30k train cells, log matrix | NMF loadings | k |
| ica_k{16,64} | train PCA-k | FastICA rotation | k |
| gmm_k{10,30,100} | 30k train cells, PCA-50 | GMM responsibilities | components |
| depth2 | nothing | [log total counts, log n genes] | technical floor |
| random_k32_s{0,1} | nothing | i.i.d. Gaussian | absolute floor |

Probe (`probe.py`): one multinomial logistic regression (C = 1, standardized inputs,
1000 iterations) trained on the train panel's embedding, applied to the test panel. Same
settings for every respondent. Response k = 1 if the predicted label equals the cell
ontology class; `p_true` (probability of the true class) is kept for a graded model later.

### 3.3 ML respondents (added 2026-10-14)

Both run in a second environment (`.venv-scvi`: torch CUDA 12.6, scvi-tools 1.5) and hand
their outputs to the same probe / metrics / pass rule as the classical pool, so nothing in
the scoring path changes.

**scVI (component A).** `scripts/extract_scvi_embedding.py` trains scvi-tools SCVI
(negative-binomial likelihood, 2 layers) on the *train panel only*, on 2,000 seurat_v3 HVGs
chosen on train counts, then embeds train and test cells with the frozen model. Three
settings act as the capacity / correction knobs: latent 10 and 30 with `tissue` as the
batch key, and latent 30 with no batch key. Donors cannot be the batch key because the
panel is donor-disjoint by design; tissue is present in both splits. Test cells whose
tissue is absent from train are handled by extending the category set (the encoder does
not consume the batch covariate, so latents are unaffected). The cached embedding goes
through `scripts/append_repr_responses.py`: identical multinomial probe, identical items.

**scGen (component B, unseen-context scheme).** The scgen package on PyPI targets an old
scvi-tools API and does not import, so `src/vcb/pert/scgen.py` re-implements it in torch
with the published architecture (VAE, 800-800-100, MSE reconstruction on log1p CP10k,
dropout 0.2, KL weight 5e-5, early stopping on a 10 % validation split) and the published
rule: latent delta = mean z(perturbed cells, training contexts) - mean z(control cells,
same contexts, balanced), predicted cells = decode(z(control cells of the target context) +
delta). The benchmark response is the pseudobulk delta of the decoded cells. Per (dataset,
fold) it trains on 100 stored cells per *training* item plus all control cells, on the
benchmark's own 2,000 HVGs; non-HVG genes fall back to the fold's mean shift so all-gene
metrics stay defined (the pass rule uses the HVG metrics). Folds are the exact ones of the
classical pool (`vcb.pert.folds`, verified identical). Items whose perturbation is unseen
in every training context get the mean-shift fallback, which is why the model cannot run
in the unseen-perturbation scheme. `scripts/append_pert_scores.py` scores the fold
predictions with the same metrics against a recomputed mean-shift reference (validated: a
fake respondent built from mean-shift predictions reproduces mean_shift's scores exactly).

## 4. Splits

**Component B, scheme `perturbation` (default).** 5-fold GroupKFold over perturbation
identity, deterministic in the seed. Every perturbation is held out exactly once, so every
condition is an item with an out-of-fold prediction from every respondent. This is the
unseen-perturbation scenario of scPerturBench and the in-the-wild benchmark. For
multi-context datasets (sciPlex3, McFarland, Frangieh) the `context` scheme additionally
holds out (perturbation, context) pairs while the same perturbation stays visible in other
contexts: the unseen-context scenario.

**Component A.** Donor-disjoint train/test as in 2.2. The probe is fit once per respondent
on train and scored on test. Cells within a stratum are not independent items; the Rasch
report therefore gives both a cell-level fit and a stratum-level binomial fit (k correct of
n cells), the latter being the one to trust for difficulty SEs.

## 5. Scores and responses

**Component B metrics** (`metrics.py`, each on the 2000 control-dispersion HVGs and on all
genes): `pearson_delta` (VCC/State style), `pearson_delta_sys` (after removing the training
mean shift from both prediction and truth: credit only for the perturbation-specific part),
`mse`, `l2_ratio`, `deg_overlap50` (overlap of top-50 |delta| genes).

**Binarization** (`scoring.py`): respondent passes item i if `pearson_delta@hvg` exceeds the
mean_shift respondent's value on i by margin m (default 0). mean_shift itself is removed
from the fit. Difficulty therefore means "how far past the shared shift do you need to be on
this condition". A graded 4-bin variant (control_mean / mean_shift / ridge ladder) is
implemented but not yet fit.

## 6. Rasch fit (`src/vcb/irt/rasch.py`)

1PL, P(correct) = sigmoid(theta_j - b_i), joint maximum likelihood by alternating Newton
steps. Respondents carry a N(0, 3^2) ridge, items a weak N(0, 4^2) ridge (which also fixes
the location of the scale). Dichotomous and binomial (k of n) inputs share one code path;
missing pairs have n = 0. Outputs: ability and difficulty with Fisher SEs, outfit statistics,
and a `degenerate` flag for items passed by nobody or by everybody. Synthetic recovery (80
respondents x 2000 items, 30 % missing): ability correlation 0.998, difficulty correlation
0.969 with RMSE 0.40 against a median reported SE of 0.33.

## 7. Results (v0 runs, 2026-10-14)

Full reports: `runs/pert_pool_v0/summary.md`, `runs/repr_pool_v0/summary.md`, and the
per-dataset `rasch/*.md` files.

### 7.1 Item bank

| | component A | component B |
|---|---|---|
| raw data | Tabula Sapiens v2, 28 tissues, 57 GB | 13 scPerturb sets, 21 GB |
| panel / items | 167,670 cells (146,800 train, 20,026 test items), 145 types, 433 strata | 20,225 conditions (+ 16 extra context items files); 15,561 informative on the pooled scale |
| largest contributor | Immune compartment (10,229 test cells) | Replogle K562 genome-wide (9,326 items) |
| respondents | 27 + 3 scVI | 18 per genetic dataset, 8 per chemical (+ scGen on 3 multi-context sets), 20 pooled |

Per dataset (unseen-perturbation scheme; "nobody" = items no respondent beats mean_shift on):

| dataset | items | informative | nobody | contexts | top respondent |
|---|---|---|---|---|---|
| Replogle K562 genome-wide | 9326 | 7893 | 1364 | 1 | ridge_d10_lam100 |
| Replogle K562 essential | 1832 | 1569 | 259 | 1 | ridge_d10_lam100 |
| Replogle RPE1 | 1611 | 1298 | 309 | 1 | gp_d50_ls2 |
| Nadig Jurkat | 1815 | 1517 | 293 | 1 | gp_d50_ls2 |
| Nadig HepG2 | 1061 | 924 | 133 | 1 | gp_d50_ls2 |
| sciPlex3 (drug, 3 lines, doses) | 2423 | 1287 | 1136 | 3 | lowrank_r10 |
| McFarland (drug, 154 lines) | 866 | 213 | 653 | 154 | (degenerate: no compound features) |
| Frangieh (KO, 3 conditions) | 669 | 435 | 234 | 3 | lowrank_r5 |
| Norman (CRISPRa, singles + doubles) | 236 | 225 | 9 | 1 | gp_d50_ls0.5 |
| Adamson | 87 | 80 | 7 | 1 | gp_d50_ls2 |
| Tian 2021 CRISPRi neurons | 183 | 62 | 121 | 1 | gp_d50_ls2 |
| Tian 2019 iPSC | 81 | 31 | 50 | 1 | ridge_d10_lam100 |
| Tian 2019 day-7 neurons | 35 | 27 | 8 | 1 | knn_k20 |

### 7.2 Component A (Tabula Sapiens v2)

- Cell-level 1PL: 20,026 items, 27 respondents, converged; 2,517 cells (12.6 %) are
  labelled correctly by no respondent; none by all. Difficulty 5/50/95 percentiles
  -3.1 / -1.1 / +2.4, median item SE 0.52.
- Ability ladder is monotone where it should be: pca_k128 (0.97) > k64 (0.80) > k32 (0.55)
  > k16 (-0.12) > k8 (-1.34) > k4 (-2.14); random projections sit 0.6 to 0.9 logits below PCA
  at equal dimension; nystroem and ICA match PCA-64 to PCA-128; GMM responsibilities are the
  weakest learned family; depth-only (-2.96) and random (-4.13) pin the floor. Random
  embeddings misfit (outfit 3.9), as a pure-guess respondent should.
- Predictions from the plan hold: difficulty falls with the type's training support
  (Spearman -0.34 cell level, -0.47 stratum level) and with sequencing depth (-0.11). The
  hardest types are sibling immune states (activated / naive CD8 T, gamma-delta T,
  innate lymphoid, intermediate monocyte) and stromal types that share a lineage (mural,
  muscle, mesenchymal stem cell).
- Stratum-level binomial fit (433 strata): same ability order, median SE 0.07, but
  respondent outfit 3 to 10, i.e. strong overdispersion. Cells in a stratum are not
  exchangeable trials. The SEs from this fit are too small; a beta-binomial or testlet
  random effect is the next step (plan risk 6 / MATH section 11.2 in scfm-irt).

### 7.3 Component B (13 scPerturb sets)

- Pooled 1PL: 20,225 items, 20 respondents, converged; 4,576 items (22.6 %) are passed by
  nobody (the mean shift is unbeatable there), 88 by everybody. Difficulty 5/50/95
  percentiles -4.2 / -0.9 / +1.6, median item SE 0.60 (as expected with ~18 respondents).
- Ability order on the pooled scale: ridge_d10_lam100 (-0.31) ~ ridge_d10_lam1 ~ gp_d50_ls2
  > ridge_d50 > gp_d50_ls0.5 > training-fraction ladders > kNN > random shift (-2.2) >
  control_mean (-2.4) > target_kd (-3.3). The training-fraction ladder is monotone (tf1 >
  tf0.3 > tf0.1) in every dataset. The low-rank respondents top the pooled table but were
  only run on the three multi-context sets, so their 0.21 is not comparable.
- Systema's finding reproduces: on raw Pearson-delta the mean shift is the best or
  second-best respondent in 9 of 13 datasets. Norman is the exception (GP and kNN far ahead,
  because a double's two singles are in training).
- target_kd is a misfit respondent (outfit 4.6): it ties mean_shift unless the target is
  among the scored genes, and a tie counts as a fail. It is kept as a diagnostic, not as a
  rung of the ladder.
- The dataset factor is real: mean difficulty ranges from -1.74 (Norman) to +0.99 (Tian 2021),
  about 2.7 logits, within-dataset SD about 1.5. A single pooled scale is therefore only a
  first approximation; linking through shared perturbations (K562 sets share thousands of
  targets) is needed before cross-dataset difficulties are compared.
- Effect size: under the baseline-relative pass rule, difficulty is weakly *positively*
  correlated with effect size in the large genetic sets (Spearman 0.09 to 0.30), the opposite
  of the plan's raw-metric prediction. Large-effect items are the ones the shared shift
  already captures, so beating it there is hard; small-effect items are near coin flips.
  The binarization choice changes what difficulty means (plan risk 1); the graded model is
  the way to keep both readings.
- Chemical sets without compound descriptors (sciPlex3, McFarland) can only be scored by
  shift, low-rank and floor respondents; McFarland's unseen-perturbation scheme is
  degenerate (653 of 866 items passed by nobody) and should be ignored until descriptors
  are added. Their unseen-context scheme is informative.

### 7.35 ML respondents (runs of 2026-10-14)

**scVI on Tabula Sapiens v2** (54 epochs each, ~10 min per setting on one A100):

| respondent | ability | probe accuracy | placement |
|---|---|---|---|
| scvi_k30_bnone | 0.74 | 0.627 | between pca_k64 (0.81) and pca_k32 (0.55) |
| scvi_k30_btissue | 0.47 | 0.596 | just below nmf_k64, above rproj_k128 |
| scvi_k10_btissue | 0.10 | 0.552 | between pca_k16 (-0.12) and rproj_k128 (0.35) |

scVI does not beat the PCA ladder on this donor-disjoint annotation panel: its best
setting sits a quarter logit below pca_k64 and a full logit below pca_k128. Tissue as a
batch key *hurts* (0.47 vs 0.74), because tissue carries type information the probe can
use, and correcting it away removes signal. This matches the 2025 to 2026 representation
literature (parameter-free pipelines on par with learned ones for annotation) and is
exactly the kind of statement the scale is for: scVI is a legitimate mid-ladder respondent,
not the ceiling. Its outfit (0.7 to 0.8) is unremarkable, so it is also not idiosyncratic.
With 30 respondents the cell-level difficulties have median SE 0.49.

**scGen on the three multi-context sets** (unseen-context scheme; 15 GPU tasks, 2 to 8 min
each). Items whose perturbation was unseen in every training context fell back to the mean
shift (3 to 10 % of items on Frangieh, 0 to 5 % on sciPlex3, none on McFarland).

| dataset | scGen raw Pearson (mean_shift) | scGen ability (rank) | top respondent |
|---|---|---|---|
| McFarland, 154 lines | 0.527 (0.324) | +2.75, rank 1 of 9, p_correct 0.81 | scgen |
| sciPlex3, 3 lines x doses | 0.129 (0.261) | -1.76, rank 4 of 9 | lowrank_r10 (-0.57) |
| Frangieh, 3 conditions | 0.180 (0.315) | -2.77, rank 10 of 22 | lowrank_r5 (-0.79) |

The split result is informative. On McFarland, where every drug is seen in many of the 154
cell lines, latent arithmetic transfers the response to a new line far better than any
shift or low-rank baseline: it is the only respondent so far that beats mean_shift on most
items of a dataset (81 %). On sciPlex3 and Frangieh, with only three contexts, scGen is
below the mean shift on raw Pearson and the low-rank completion of the (perturbation x
context) tensor is the better transfer model. So the value of a learned latent space here
scales with the number of contexts a perturbation has been observed in, which is the
Tahoe-100M regime (50 lines) and argues for bringing that set in next. scGen's outfit is
0.5 to 1.2: it behaves like a Rasch respondent, unlike target_kd.

### 7.5 Component A on new atlases and Parse 10M PBMC (runs of 2026-10-15)

Six CELLxGENE panels and two Parse panels were built with the generic builder
(`src/vcb/data/repr_generic.py`, `slurm/repr_generic.slurm`) and scored with the 27
classical embeddings plus three scVI settings (`slurm/scvi_panels.slurm`; the PANELS env var
selects panels). Each panel is its own Rasch fit; abilities below are per panel and are
not comparable across rows until the pooled fit.

| panel | held out | items | top model (ability) | PCA-128D | best scVI |
|---|---|---|---|---|---|
| Hao PBMC (level-2 labels) | donors | 7,999 | scVI-30D tissue-corrected (3.57) | 2.93 | 3.57 |
| heart states | donors | 14,396 | Nystroem k256 (0.63) | 0.57 | 0.55 |
| HLCA core | donors | 11,389 | PCA-128D (2.69) | 2.69 | 2.62 |
| HLCA core | studies | 32,221 | scVI-30D study-corrected (2.82) | ~2.5 | 2.82 |
| immune atlas | donors | 20,548 | Nystroem k256 (2.01) | 2.00 | 1.82 |
| immune atlas | tissues | 23,038 | scVI-30D tissue-corrected (2.17) | 2.04 | 2.17 |
| Parse 10M PBMC (18 types) | donors | 16,811 | Nystroem k256 (3.39) | 3.31 | pending |
| Parse 10M PBMC (91 cytokines as labels) | donors | 2,275 | NMF k64 (-4.44) | -4.72 | not run |

Observations.

- scVI is on top exactly on the panels whose held-out unit is its batch key (study-held-out
  HLCA with `batch=study`; tissue-held-out immune atlas with `batch=tissue`) and on Hao PBMC,
  whose 24 donors x 8 batches is the regime scVI was designed for. On donor-held-out panels
  with many cell types (HLCA, immune atlas) it is level with or slightly below PCA-128D, as on
  Tabula Sapiens. A learned batch-aware latent space earns its ability when the evaluation
  holds out the batch; otherwise a linear projection does the same job.
- Parse annotation (donor-held-out, 12 donors, 18 PBMC types, 90 cytokine treatments mixed
  into every stratum) is an easy panel: raw accuracy 0.89 for the top models, abilities above
  3. The 90 treatments do not confuse the type probe.
- The cytokine-state panel (label = cytokine, strata = cell type x donor) is at the floor:
  top raw accuracy 0.043 against a 1/91 chance rate, 76 % of items passed by no model,
  abilities -4.4 to -6.4. A single cell does not carry enough signal to name its cytokine
  from a frozen embedding and a linear probe. This is the component-B question and is
  answered there with pseudobulk shift items (`parse_pbmc_cytokines`, 30 cells per
  condition, contexts = donor x cell type). The panel is kept as a floor check and is
  excluded from the pooled scale.
- Pooling bug found and fixed: the first pooled scale (`runs/repr_pooled_v0`, 122,159 items)
  merged 7,458 cells that are test items in two panels from the same atlas (HLCA donor/study
  1,672; immune donor/tissue 5,786) because item ids were the cell barcodes. The pooled fit
  now namespaces item and stratum ids by run (`fit_rasch.py repr --pool-runs`), and
  `runs/repr_pooled_v1` (eight panels, 146,428 items) replaces v0.
- The TS2-only compartment block in `scripts/summarize.py` is now guarded; it had failed on
  every non-TS2 run (the Rasch fits themselves were fine).

### 7.4 Compute actually used

Downloads 2.5 h wall (Zenodo throttles to ~1 MB/s per connection; two parallel jobs).
Item builds 13 s (Tian) to 14 min (genome-wide, 94 GB peak RSS with the 100-cell cap).
Pool runs 15 s to 8 min per dataset; the component-A pool 87 min on 16 CPUs (the probe on
146k cells dominates). Rasch fits are seconds. Disk: raw 74 GB, items 76 GB, panel 4 GB.

## 8. Known gaps for v1

- Pool width: 18 respondents per genetic B dataset and 27 for A give item SEs of ~0.6 and
  ~0.5 logits; the plan's target is 50 to 100 respondents. Next additions: scVI (A), GBT and
  GMM mixture-of-shifts (B), training-fraction ladders (both).
- No chemical descriptors, so sciPlex/McFarland cannot run the unseen-perturbation scheme.
- E-distance and other cell-level metrics are not computed yet (cells are stored for it).
- Component A stratum fit is overdispersed; replace binomial with beta-binomial / testlet.
- Test-donor choice is greedy on tissue coverage; donors unique to a tissue should be kept
  in train (the small-panel test showed Ear losing all its train cells).
- Linking across datasets: v0 pools datasets by sharing respondent names only; shared
  perturbations across K562 sets and across Tian/Nadig contexts are the planned anchors.
- Contamination register not started (irrelevant for the classical pool, required before
  foundation models are placed on the scale).

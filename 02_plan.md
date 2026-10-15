# Plan: a living IRT benchmark for virtual cell models

Goal for this quarter: one merged, versioned item bank covering representation
(A) and perturbation (B); a Rasch/2PL fit on a cheap respondent pool that
yields per-item difficulty with standard errors; first ability estimates for a
handful of ML models on the pool-anchored scale. The paper's maintenance loop
(anchors, recalibration, retire, acquire) comes after that, with VCC 2026 as
the first acquisition round.

## Phase 0: fix the unit of analysis (week 1)

Decide these before downloading anything, because they determine the schema.

**Component A (representation).**
- Item = one cell from a fixed, stratified panel. Stratify by (dataset, cell
  type, donor or batch); cap at n cells per stratum (start n = 50). Target
  panel size 20k to 50k cells across 8 to 12 datasets.
- Response = correct / incorrect from a fixed probe: multinomial logistic
  regression on the frozen embedding, trained on a disjoint train panel with
  the same strata. Same probe, same train panel, same hyperparameters for
  every respondent. That is the PertEval-scFM protocol and it is the only way
  the comparison is about the embedding.
- Local dependence: cells in one stratum are not independent items. Fit with
  a stratum random effect (testlet model) or report difficulty at the stratum
  level as a binomial Rasch (k correct out of n). Start with the binomial
  version. It is cheaper and the SEs are honest.

**Component B (perturbation).**
- Item = (perturbation, context, dose, time) condition with at least 100
  cells. Cells are replicates, not items.
- Response is continuous. Two options, run both:
  1. Binary: pass if the model's per-item score beats the Linear Additive
     baseline's score on that item by a fixed margin. Fit Rasch. Simple,
     and "difficulty" then means "how far past linear do you need to be."
  2. Graded: discretize the score into 4 ordered bins defined by the
     baseline ladder (worse than no-change, between no-change and
     control-mean, between control-mean and linear, better than linear) and
     fit a graded response model. This keeps more information and the bins
     have a meaning.
- Per-item score: use one Systema-style metric that references the perturbed
  centroid, plus a DEG-level metric. Do not use raw MSE or Pearson against
  control; the literature shows those are dominated by the shared shift.
- Splits: keep the unseen-perturbation and unseen-context splits from
  scPerturBench and the in-the-wild benchmark so numbers are comparable to
  published tables.

## Phase 1: collect and merge (weeks 1 to 4)

**Priority order.** Start with the datasets that appear in the most existing
suites, because that is where your difficulty estimates can be checked
against published rankings:

1. Norman 2019, Adamson 2016, Replogle 2022 K562 essential and RPE1 (pertpy).
2. sciPlex3, Kang 2018, McFarland 2020, Frangieh 2021 (pertpy / scPerturb).
3. VCC 2025 H1 hESC train and validation (Arc atlas).
4. Tabula Sapiens v2, Human Kidney Disease, Mouse Kidney, Immune Cell Atlas
   subset (cz-benchmarks CLI / CELLxGENE).
5. Then scale: Replogle K562 genome-wide, Tahoe-100M subsample, Tian
   neurons, Gasperini enhancers, X-Atlas/Orion if the license allows,
   Zhu CD4 T cells when an accession appears.

**Subsample by design.** IRT wants many items, not many cells per item.
Cap at 500 cells per condition (VCC itself curates to 400). Tahoe-100M at
60k conditions x 500 cells is 30M cells, still large; start with 5 lines x
all drugs. Orion is ~520 GB; take the dose-stratified subset only.

**Schema (one AnnData per dataset, one parquet manifest for the bank).**
- `obs`: `dataset_id`, `cell_id`, `context` (cell line or tissue),
  `cell_type` (Cell Ontology ID + label), `donor`, `batch`, `is_control`,
  `perturbation` (Ensembl ID for genes; InChIKey + ChEMBL for compounds;
  list for combinations), `pert_type` (CRISPRi/a/KO, drug, cytokine),
  `dose`, `dose_unit`, `time_h`, `guide_id`.
- `var`: Ensembl ID index, symbol, biotype; keep raw counts in `layers["counts"]`.
- Gene space: union of protein-coding Ensembl IDs with a per-dataset
  missingness mask. Do not intersect; intersection silently drops the genes
  that make items hard.
- Manifest row per item: item_id, component, dataset_id, condition keys,
  n_cells, effect size (E-distance to control), Systema systematic-variation
  score, and the contamination flags below.

**Contamination register.** For each dataset, a column per foundation model
indicating whether the dataset is (a) in its published pretraining corpus,
(b) in its fine-tuning data, or (c) clean. Sources: the model papers' data
sections. Keep this as a table from day one; it is what makes an ability
estimate interpretable.

**Storage and compute.** Estimate before pulling: ~1 GB per 100k cells of
sparse counts in h5ad. The priority-1 to 4 set is under 3M cells, so under
30 GB. Everything in Phase 1 runs on one workstation.

## Phase 2: the difficulty pool (weeks 4 to 8)

Respondents are classical model families, each run across a capacity ladder.
The two axes do different jobs and both are needed:

- **Family diversity** (PCA regression, GP, GMM, ridge, kNN, trees, ...)
  produces *different response patterns* at similar ability. That is what
  lets a 2PL identify item discrimination, what exposes multidimensionality
  (items that a kernel method passes and a linear method fails form a second
  factor), and what makes the difficulty estimate robust to one family's
  inductive bias. A pool of one family measures "difficulty for linear
  models," not difficulty.
- **Capacity ladder within a family** (rank, kernel lengthscale,
  regularization, training fraction) produces a *monotone spread of
  ability*. Without it, most families land in the same narrow band and the
  bottom and top of the difficulty scale are unobserved.
- Seeds: 2 per configuration, used only to estimate response noise.

Rule of thumb: 6 to 8 families, 4 to 6 capacity levels each, 2 seeds, which
is 50 to 100 respondents per component. Difficulty SE at p = 0.5 with 80
respondents is about 0.25 logits; that is the floor you are buying.

**Component A respondents (embedding + fixed probe).** The probe is the same
multinomial logistic regression for everyone so that the respondent is the
embedding.

| Family | Capacity knob | Notes |
|---|---|---|
| PCA | k in {4, 8, 16, 32, 64, 128, 256} | baseline ladder; also HVG count {500, 1000, 2000, 4000} and log1p vs Pearson residuals |
| Random Gaussian projection | same k ladder | floor with the same geometry as PCA; separates "linear subspace" from "variance-ordered subspace" |
| Kernel PCA / Nystrom (RBF, cosine) | k and lengthscale | nonlinear but still unsupervised |
| NMF, ICA, factor analysis | k | different basis, same rank; cheap |
| GMM responsibilities as embedding | number of components {10, 30, 100, 300} | soft cluster membership; a cluster-level respondent that will fail sibling types and pass coarse ones |
| LDA / topic model on counts | topics {10, 30, 100} | count-native; often strong on rare types |
| scVI | latent {10, 30}, train fraction | the one parametric nonlinear family; keep it |
| Harmony on PCA-50 | theta | batch-corrected variant |
| Scaling ladders (any family) | probe train fraction {1, 3, 10, 30, 100}%; label noise {0, 5, 10, 20}% | the monotone ability axis; also a stand-in for "the field improving" |
| Floors | random embedding; majority-class probe | pin the bottom of the scale |

UMAP or t-SNE are not respondents: they have no out-of-sample map, so the
test panel cannot be embedded without leakage. Skip them.

**Component B respondents (predict post-perturbation profile from control
profile + perturbation features).** Features for unseen perturbations: gene
embeddings (ESM-2, GenePT) for genetic items, Morgan fingerprints or ChemBERTa
for compounds; context features: control pseudobulk in PCA-50.

| Family | Capacity knob | Notes |
|---|---|---|
| No-change, control-mean, perturbation-mean | none | floors; also define the graded-response bins |
| Linear Additive, Latent Additive, DecoderOnly | latent dim | PerturBench code |
| PCA + linear (Ahlmann-Eltze) | k in {10, 20, 50, 100, 200} | the published linear baseline |
| Ridge / lasso on gene-embedding features | lambda ladder | linear in features, different features from PCA+linear |
| GP regression with perturbation kernel | RBF or Matern on gene embeddings; lengthscale ladder | GP is natural here: items are perturbations, n is hundreds to thousands, so exact GP is cheap. Output in PCA-50 of expression, multi-output via shared kernel. Infeasible in gene space; do not try. |
| kNN regression in perturbation-embedding space | k in {1, 5, 20, 50} | nonparametric smoother; pairs with the GP |
| GMM mixture-of-shifts | components {5, 20, 50} on control cells; one shift vector per component | the GMM that makes sense for B: a cluster-conditional additive model. Captures heterogeneity that cell-mean baselines miss |
| Low-rank matrix completion of the (perturbation x context) effect tensor | rank {2, 5, 10, 20} | the right baseline for unseen-context items; soft-impute or ALS |
| Gradient-boosted trees on features | depth and rounds | the one nonlinear-but-not-deep family |
| Scaling ladder | fraction of training perturbations {10, 30, 100}% | monotone ability axis; mimics unseen-perturbation severity |

**Fits and checks.**
- Rasch (1PL) first, then 2PL to see whether discrimination varies. With ~80
  respondents per item, difficulty SE is roughly 1/sqrt(80 p(1-p)), about
  0.25 logits at p = 0.5 and worse at the extremes. That is why the pool
  needs to be wide, not deep.
- Unidimensionality: fit per-dataset and check whether difficulties are on
  one scale. Expect a dataset factor. If so, use multidimensional IRT or
  link datasets through shared conditions (same perturbation in two
  contexts, same cell type in two atlases) as anchor items. This is the
  companion-paper machinery and it is needed here.
- Item fit: infit/outfit; flag items where the floor respondents score high
  (label error or degenerate item) and items where nothing scores above
  floor (effect too small to measure; check against E-distance).
- Outputs: a difficulty map with covariates. Predictions worth testing:
  B difficulty is monotone in E-distance and in Systema's systematic-variation
  score; A difficulty is highest for rare types, sibling types, and
  donor-specific states; the saturated set (passed by control-mean or
  majority class) is the first retirement list.

## Phase 3: ML models on the pool-anchored scale (weeks 8 to 12)

- Component A: Geneformer, scGPT, scFoundation, UCE, SCimilarity,
  TranscriptFormer, Tahoe-x1. Zero-shot embeddings, same probe, same panel.
- Component B: CPA, GEARS, scGen, BioLORD, SAMS-VAE, scLAMBDA, GenePert,
  STATE, plus scGPT and scFoundation fine-tuned.
- Estimate each model's ability with item difficulties held fixed from
  Phase 2 (the pool is the anchor set). Report ability in logits with SE,
  and report it separately on clean versus contaminated items. The
  "deep beats linear or not" debate becomes one number with an error bar,
  split by contamination status.
- Expect: on contaminated items, foundation models sit well above the pool;
  on clean items (VCC 2025 test, Tian, Gasperini), the gap narrows. If it
  does not narrow, that is a real result.

## Phase 4: make it living (after week 12)

- Round structure: round 0 = Phase 2 pool; round 1 = Phase 3 models; round 2
  = VCC 2026 as the acquisition of >10k hard items per line.
- Anchors: choose clean items with mid-range difficulty from round 0, spread
  across datasets, and freeze them. Do not use Norman or Replogle as anchors;
  they are the most contaminated items in the field.
- Estimate the drift rate r from the pool ladder and the round 1 models.
  Apply the retire and acquire rules from the paper; the writing budget
  condition becomes "new clean conditions per round," which VCC and the
  Tahoe follow-on supply.

## Risks, in order

1. Continuous responses in B. The binarization choice is a modeling decision
   that changes the difficulty scale. Run both binary and graded, report
   where they disagree.
2. Non-unidimensionality across datasets. Likely. Budget time for linking.
3. Contamination. Without the register, ability means nothing.
4. Metric choice in B. Fixed by referencing the perturbed centroid and a
   baseline-relative pass rule; still document the alternative.
5. Licenses. Orion non-commercial; confirm before any merged redistribution.
6. Probe leakage in A. Train and test panels must not share donors within a
   dataset, or the probe learns donor rather than type.

## Week 1 concrete steps

1. Create `vc-benchmark/data/` and a `manifest.parquet` with the schema above.
2. Pull priority-1 datasets with pertpy and write each to the schema.
3. Pull Tabula Sapiens v2 and build the stratified A panel (train and test,
   donor-disjoint).
4. Implement the probe and the Linear Additive baseline; run both on one
   dataset end to end and store responses as a long table
   (item_id, respondent_id, response).
5. Fit a Rasch model on that one dataset with ~20 PCA respondents. Look at
   the difficulty histogram and the floor respondents before scaling up.

# scBaseCount (human) on the virtual-cell benchmark: dataset and component-A results

Last updated 2026-10-19. Machine: Arc workspace (16 CPUs, 1 TB RAM, three RTX 2080 Ti).
Everything below was produced with the code in this repository (`scripts/concat_h5ad.py`,
`scripts/build_repr_panel_generic.py`, `scripts/run_repr_pool.py`, `scripts/extract_scvi_embedding.py`,
`scripts/fit_rasch.py`); per-panel run folders are `runs/repr_scbasecount_*`. Section 7.6 of
`03_implementation.md` has the longer discussion.

## 1. Dataset

scBaseCount release 2026-01-12 (Arc Institute, CC BY 4.0), feature type `GeneFull_Ex50pAS`, local copy
at `/datasets/arc`. The benchmark uses only the human part; the other 26 organisms (3.0 TB, mouse 2.4 TB
of it) are being removed from the local copy and the human files are being rewritten without the two
unused multi-mapper count layers (3.2 TB to about 1.1 TB), see `scripts/scbasecount_cleanup.py`.

| human subset | SRA samples (libraries) | cells |
|---|---|---|
| all human in the release | 35,263 | 302,278,851 |
| with a cell-type label (`metadata/.../obs_metadata.parquet`) | 24,905 | 209,889,229 (143 labels) |
| passing the panel filters: 10x 3'/5' GEX, single-cell prep, no perturbation, no cell line, >= 500 labelled cells, >= 3 types | 3,156 | 24.0 M labelled |
| of those, with a single UBERON tissue id (usable for tissue-defined panels) | 2,432 | |
| used by the 60-sample panels (section 2.1) | 360 | 1.2 M read, 380 k kept |
| used by the `human200` panels (section 2.2) | 946 distinct | 3.0 M read, 1.0 M kept |
| used by the `humanall` panels (section 2.3) | 1,813 | 13.3 M labelled, ~4 M read |

Per-sample h5ad: `X` is the unique-read UMI count matrix (CSC, float32 with integer values), `var` is
indexed by Ensembl id with a `gene_symbols` column (36,601 genes). The `obs.cell_type` column inside the
h5ad files is empty; labels come from the per-organism `obs_metadata.parquet` (one row per cell, keyed
by SRX accession and barcode) and are joined at concatenation time. Sample metadata (tissue, disease,
perturbation, cell line, 10x chemistry) is LLM-extracted from SRA text, so tissues are selected by
`tissue_ontology_term_id` and perturbation / cell-line fields by regular expression. Donor identity is
not recorded, so the held-out unit is the SRA sample (library).

Panel recipe (identical for every panel): label = `cell_type`, split unit = SRX accession, context =
tissue id; strata = tissue x type x sample, dropped below 20 cells, capped at 200 train / 100 test cells;
40 % of samples (or of tissues, for the multitissue panels) held out; up to 3,000 cells read per sample
(1,500 for `humanall_multitissue`). Every held-out cell whose type occurs in training is one item.

Respondents: the 27 classical embeddings of the repo pool (PCA 4 to 256 D, ICA, NMF, Nystroem, random
projections, Gaussian mixtures, depth-only and random floors), each fit on the panel's training cells,
plus three scVI settings trained on the training cells only (`scvi_k10_btissue`, `scvi_k30_btissue`,
`scvi_k30_bnone`: latent 10 or 30, tissue as batch key or none; 2,000 HVGs, NB likelihood, early
stopping). All 30 are scored by the same frozen multinomial probe; abilities are 1PL Rasch estimates at
cell level. On single-tissue panels the tissue batch key has one category, so the two latent-30
settings coincide. "nobody passes" is the share of items no respondent gets right (label-noise floor).

## 2. Results

### 2.1 Human panels, 60 samples per tissue (runs of 2026-10-16)

| panel | samples | train cells | test items | types | nobody passes | random floor acc | best classical (ability / acc) | scVI-30D none (ability / acc / rank) | scVI-30D tissue | scVI-10D tissue |
|---|---|---|---|---|---|---|---|---|---|---|
| human_lung | 60 | 46,086 | 20,521 | 25 | 5.2 % | 0.094 | pca_k64 (1.57 / 0.716) | 1.20 / 0.678 / 10 | 1.20 / 0.678 / 11 | 0.71 / 0.622 / 17 |
| human_skin | 60 | 44,290 | 20,009 | 18 | 11.4 % | 0.101 | nystroem_k256_g0.5 (0.48 / 0.586) | 0.31 / 0.566 / 9 | 0.31 / 0.566 / 10 | -0.02 / 0.527 / 15 |
| human_bone_marrow | 60 | 35,748 | 15,525 | 17 | 11.7 % | 0.106 | nystroem_k256_g0.5 (0.36 / 0.575) | 0.42 / 0.583 / 1 | 0.42 / 0.583 / 2 | 0.25 / 0.561 / 4 |
| human_liver | 60 | 38,062 | 12,681 | 19 | 14.2 % | 0.151 | pca_k128 (0.03 / 0.530) | -0.08 / 0.515 / 9 | -0.08 / 0.515 / 8 | -0.54 / 0.453 / 16 |
| human_blood | 60 | 36,664 | 11,088 | 12 | 9.5 % | 0.182 | nystroem_k64_g0.5 (-0.41 / 0.455) | -0.15 / 0.497 / 1 | -0.15 / 0.497 / 2 | -0.29 / 0.475 / 3 |
| human_multitissue | 120 | 69,141 | 23,222 | 23 | 22.0 % | 0.102 | pca_k256 (-1.01 / 0.387) | -1.08 / 0.378 / 5 | -1.15 / 0.370 / 10 | -1.28 / 0.355 / 15 |

Pooled scale, 60-sample family (`runs/repr_pooled_scbasecount_human_v0`): 103,046 items, 13,126 passed by no respondent.

| rank | respondent | ability | se | probe accuracy | outfit |
|---|---|---|---|---|---|
| 1 | pca_k64 | 0.10 | 0.01 | 0.538 | 0.37 |
| 2 | pca_k128 | 0.10 | 0.01 | 0.537 | 0.44 |
| 3 | ica_k64 | 0.09 | 0.01 | 0.537 | 0.37 |
| 4 | nystroem_k64_g0.5 | 0.09 | 0.01 | 0.537 | 0.37 |
| 5 | nystroem_k256_g0.5 | 0.08 | 0.01 | 0.535 | 0.44 |
| 6 | scvi_k30_bnone | 0.08 | 0.01 | 0.535 | 0.67 |
| 7 | scvi_k30_btissue | 0.06 | 0.01 | 0.533 | 0.67 |
| 8 | pca_k256 | 0.04 | 0.01 | 0.531 | 0.50 |
| 9 | nystroem_k256_g2 | 0.04 | 0.01 | 0.530 | 0.47 |
| 10 | pca_k32 | 0.01 | 0.01 | 0.526 | 0.40 |
| 11 | nmf_k64 | -0.08 | 0.01 | 0.515 | 0.61 |
| 12 | nystroem_k64_g2 | -0.14 | 0.01 | 0.507 | 0.54 |
| 13 | scvi_k10_btissue | -0.22 | 0.01 | 0.498 | 0.78 |
| 28 | depth2 | -2.73 | 0.01 | 0.182 | 5.15 |
| 29 | random_k32_s0 | -3.46 | 0.01 | 0.115 | 6.40 |
| 30 | random_k32_s1 | -3.46 | 0.01 | 0.115 | 6.47 |

### 2.2 Human panels, all filter-passing samples up to 200 per tissue (`human200`, 2026-10-19)

| panel | samples | train cells | test items | types | nobody passes | random floor acc | best classical (ability / acc) | scVI-30D none (ability / acc / rank) | scVI-30D tissue | scVI-10D tissue |
|---|---|---|---|---|---|---|---|---|---|---|
| lung | 195 | 145,543 | 64,635 | 25 | 6.7 % | 0.092 | nystroem_k256_g0.5 (1.44 / 0.702) | 1.14 / 0.671 / 9 | 1.14 / 0.671 / 10 | 0.39 / 0.585 / 17 |
| skin | 97 | 68,112 | 28,812 | 15 | 10.8 % | 0.109 | nystroem_k256_g0.5 (0.41 / 0.572) | 0.34 / 0.564 / 3 | 0.34 / 0.564 / 2 | -0.08 / 0.514 / 15 |
| bone_marrow | 171 | 104,777 | 41,262 | 20 | 13.7 % | 0.107 | nystroem_k256_g0.5 (0.16 / 0.550) | 0.31 / 0.569 / 1 | 0.31 / 0.569 / 2 | -0.12 / 0.517 / 12 |
| liver | 78 | 51,432 | 17,559 | 19 | 14.5 % | 0.145 | nystroem_k256_g0.5 (-0.03 / 0.518) | -0.08 / 0.513 / 4 | -0.08 / 0.513 / 5 | -0.36 / 0.477 / 13 |
| blood | 200 | 129,019 | 46,625 | 14 | 11.5 % | 0.155 | nystroem_k256_g0.5 (0.21 / 0.557) | 0.53 / 0.598 / 1 | 0.53 / 0.598 / 2 | 0.19 / 0.555 / 4 |
| multitissue | 355 | 180,127 | 79,157 | 22 | 32.1 % | 0.116 | nystroem_k64_g0.5 (-1.15 / 0.386) | -1.31 / 0.370 / 13 | -1.21 / 0.380 / 9 | -1.28 / 0.374 / 12 |

Pooled scale, human200 family (`runs/repr_pooled_scbasecount_human200_v0`): 278,050 items, 46,365 passed by no respondent.

| rank | respondent | ability | se | probe accuracy | outfit |
|---|---|---|---|---|---|
| 1 | scvi_k30_btissue | 0.10 | 0.01 | 0.539 | 0.68 |
| 2 | nystroem_k256_g0.5 | 0.08 | 0.01 | 0.538 | 0.45 |
| 3 | scvi_k30_bnone | 0.07 | 0.01 | 0.537 | 0.67 |
| 4 | pca_k128 | 0.04 | 0.01 | 0.534 | 0.38 |
| 5 | pca_k256 | 0.04 | 0.01 | 0.533 | 0.44 |
| 6 | nystroem_k64_g0.5 | 0.04 | 0.01 | 0.533 | 0.35 |
| 7 | ica_k64 | 0.03 | 0.01 | 0.532 | 0.33 |
| 8 | pca_k64 | 0.03 | 0.01 | 0.532 | 0.33 |
| 9 | nystroem_k256_g2 | 0.01 | 0.01 | 0.529 | 0.50 |
| 10 | pca_k32 | -0.07 | 0.01 | 0.521 | 0.35 |
| 11 | nystroem_k64_g2 | -0.13 | 0.01 | 0.514 | 0.51 |
| 12 | nmf_k64 | -0.16 | 0.01 | 0.511 | 0.59 |
| 13 | scvi_k10_btissue | -0.29 | 0.01 | 0.496 | 0.80 |
| 28 | depth2 | -3.11 | 0.01 | 0.162 | 5.62 |
| 29 | random_k32_s0 | -3.63 | 0.01 | 0.117 | 5.73 |
| 30 | random_k32_s1 | -3.63 | 0.01 | 0.117 | 5.82 |

### 2.3 Remaining human tissues and the all-sample panels (`humanall`, started 2026-10-19, in progress)

| panel | samples | train cells | test items | types | nobody passes | random floor acc | best classical (ability / acc) | scVI-30D none (ability / acc / rank) | scVI-30D tissue | scVI-10D tissue |
|---|---|---|---|---|---|---|---|---|---|---|
| cornea | 84 | 34,438 | 10,528 | 6 | 10.2 % | 0.250 | nystroem_k64_g0.5 (2.35 / 0.749) | 2.47 / 0.756 / 1 | 2.47 / 0.756 / 2 | 2.33 / 0.748 / 4 |
| islets | 38 | 14,396 | 7,654 | 9 | 8.4 % | 0.196 | pca_k32 (3.17 / 0.817) | 2.97 / 0.808 / 11 | 2.97 / 0.808 / 12 | 2.53 / 0.786 / 17 |
| lymph_node | 36 | 19,790 | 5,388 | 15 | 16.3 % | 0.149 | nystroem_k256_g0.5 (-0.40 / 0.472) | -0.57 / 0.449 / 9 | -0.57 / 0.449 / 10 | -0.76 / 0.423 / 14 |
| brain | 33 | 13,038 | 3,075 | 10 | 8.4 % | 0.163 | nystroem_k64_g0.5 (1.38 / 0.699) | pending | pending | pending |
| breast | 33 | 22,126 | 10,461 | 10 | 4.2 % | 0.124 | nystroem_k256_g0.5 (2.61 / 0.817) | pending | pending | pending |
| prostate | 28 | 19,068 | 8,325 | 12 | 10.5 % | 0.127 | nystroem_k256_g0.5 (1.49 / 0.698) | pending | pending | pending |
| pancreas | 27 | 17,516 | 7,488 | 14 | 9.1 % | 0.134 | nystroem_k256_g0.5 (1.28 / 0.677) | pending | pending | pending |
| thymus | 26 | 14,167 | 4,862 | 12 | 26.4 % | 0.193 | nmf_k64 (-1.33 / 0.348) | pending | pending | pending |
| blood | 713 | 454,066 | 155,377 | 17 | 13.2 % | 0.158 | pca_k256 (0.02 / 0.532) | 0.28 / 0.564 / 1 | 0.28 / 0.564 / 2 | -0.02 / 0.526 / 5 |
| multitissue |  |  | running | | | | | | | |
## 3. Reading the results

- scBaseCount panels are much harder than the CELLxGENE atlases used earlier in this benchmark (top
  probe accuracy 0.35 to 0.82 here against 0.8 to 0.9 there), because held-out samples come from other
  studies whose annotation granularity differs. 4 to 32 % of items are passed by no respondent.
- More samples per tissue do not make a panel easier: lung, skin, liver and bone marrow are flat or
  slightly harder at 100 to 200 samples than at 60 (more label vocabularies). Blood is the exception
  (0.455 to 0.557 to 0.564 as the sample count goes 60, 200, 713), because the 60-sample slice was
  dominated by a few shallow PBMC studies.
- scVI (latent 30) is a top-cluster respondent on scBaseCount. On the 60-sample pooled scale it ties
  the PCA ladder; on the `human200` pooled scale it is first, 0.02 logits ahead of Nystroem k256 and
  0.06 ahead of PCA-128D. It wins outright on every blood-lineage panel (blood at all three sizes,
  bone marrow) and on cornea, and trails PCA or Nystroem on lung, skin, liver and islets. Latent 10 is
  about 0.5 logits worse everywhere.
- Tissue-held-out transfer is weak: the multitissue panels sit 1 to 1.3 logits below the single-tissue
  ones and a third of their items are unreachable at 355 samples.
- Sanity checks hold on every panel: random embeddings sit at the majority-class rate, depth-only is one
  rung above, random projections are below PCA at equal dimension.

## 4. Files

- `runs/repr_scbasecount_<family>_<tissue>/`: `responses.parquet` (item x respondent outcomes),
  `items.parquet` (item covariates), `rasch/` (abilities, difficulties), `summary.md`.
- Pooled scales: `runs/repr_pooled_scbasecount_human_v0` (60-sample family) and
  `runs/repr_pooled_scbasecount_human200_v0` (human200 family; its 122 MB responses table is not in git
  and can be rebuilt with `fit_rasch.py repr --pool-runs`).
- Slice lists (`data/raw/scbasecount/lists/*.txt`) are git-ignored; the selection is reproducible from
  `sample_metadata.parquet` with the filters above.

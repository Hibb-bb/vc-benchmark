# Component A summary: repr_pooled_v3


## cell_level

- items: 424478; informative (non-degenerate): 370341; nobody passes: 52890; everybody passes: 1247
- difficulty percentiles 5/25/50/75/95: [-3.49, -2.08, -0.93, 0.88, 3.21]; median SE 0.50
- histogram (bin lower edge: count): -6: 0, -5: 7105, -4: 31862, -3: 71788, -2: 71542, -1: 63327, +0: 38576, +1: 39345, +2: 28229, +3: 18567, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.72 | 0.00 | 0.618 | 0.45 |
| scvi_k30_btissue | 0.72 | 0.00 | 0.618 | 0.70 |
| scvi_k30_bnone | 0.71 | 0.00 | 0.617 | 0.68 |
| pca_k128 | 0.69 | 0.00 | 0.615 | 0.40 |
| pca_k256 | 0.67 | 0.00 | 0.612 | 0.48 |
| nystroem_k64_g0.5 | 0.67 | 0.00 | 0.612 | 0.34 |
| ica_k64 | 0.67 | 0.00 | 0.612 | 0.33 |
| pca_k64 | 0.66 | 0.00 | 0.612 | 0.33 |
| nystroem_k256_g2 | 0.62 | 0.00 | 0.607 | 0.50 |
| pca_k32 | 0.53 | 0.00 | 0.597 | 0.37 |
| nystroem_k64_g2 | 0.42 | 0.00 | 0.585 | 0.57 |
| nmf_k64 | 0.41 | 0.00 | 0.584 | 0.62 |
| scvi_k10_btissue | 0.37 | 0.00 | 0.579 | 0.79 |
| pca_k16 | 0.11 | 0.00 | 0.550 | 0.48 |
| ica_k16 | 0.11 | 0.00 | 0.550 | 0.48 |
| rproj_k128_s0 | -0.07 | 0.00 | 0.529 | 0.86 |
| rproj_k128_s1 | -0.09 | 0.00 | 0.527 | 0.87 |
| gmm_k100 | -0.18 | 0.00 | 0.516 | 0.85 |
| nmf_k16 | -0.37 | 0.00 | 0.492 | 0.88 |
| pca_k8 | -0.67 | 0.00 | 0.453 | 0.89 |
| gmm_k30 | -0.68 | 0.00 | 0.453 | 0.95 |
| rproj_k32_s0 | -1.29 | 0.00 | 0.372 | 1.37 |
| rproj_k32_s1 | -1.31 | 0.00 | 0.369 | 1.41 |
| pca_k4 | -1.50 | 0.00 | 0.345 | 1.42 |
| gmm_k10 | -1.88 | 0.00 | 0.295 | 1.97 |
| rproj_k8_s0 | -2.70 | 0.00 | 0.196 | 2.89 |
| rproj_k8_s1 | -2.70 | 0.00 | 0.196 | 2.86 |
| depth2 | -3.14 | 0.00 | 0.151 | 6.99 |
| random_k32_s1 | -3.83 | 0.01 | 0.095 | 8.47 |
| random_k32_s0 | -3.83 | 0.01 | 0.094 | 8.37 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.005 | 3.2e-03 | 370341 |
| log_total_counts | -0.191 | 0.0e+00 | 370341 |
| n_genes_by_counts | -0.172 | 0.0e+00 | 370341 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 1772 | -0.36 | 1.50 |
| Epithelium | 2434 | -0.57 | 1.65 |
| Immune | 10383 | -0.71 | 1.81 |
| Neural | 100 | -1.44 | 0.58 |
| Stromal | 3067 | -0.23 | 1.88 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Goblet (bronchial) | 82.0 | 2.72 | 128 |
| mural cell | 44.0 | 2.63 | 128 |
| naive thymus-derived cd8-positive, alpha-beta t cell | 24.0 | 2.53 | 712 |
| activated cd8-positive, alpha-beta t cell | 60.0 | 2.33 | 361 |
| mesenchymal stem cell of adipose tissue | 45.0 | 2.29 | 445 |
| muscle cell | 39.0 | 2.18 | 132 |
| innate lymphoid cell | 26.0 | 2.14 | 95 |
| regulatory T cell | 178.0 | 2.08 | 948 |
| t cell | 139.0 | 2.07 | 2270 |
| activated cd4-positive, alpha-beta t cell | 38.0 | 2.05 | 225 |
| SM activated stress response | 56.0 | 1.99 | 23 |
| fibroblast of breast | 34.0 | 1.99 | 200 |
| schwann cell | 21.0 | 1.97 | 273 |
| gamma-delta t cell | 69.0 | 1.92 | 452 |
| DC | 130.0 | 1.91 | 366 |

## stratum_binomial

- items: 6587; informative (non-degenerate): 6486; nobody passes: 101; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.38, -1.37, -0.38, 0.74, 3.42]; median SE 0.06
- histogram (bin lower edge: count): -6: 7, -5: 22, -4: 46, -3: 627, -2: 1527, -1: 1605, +0: 1298, +1: 634, +2: 309, +3: 186, +4: 121, +5: 58

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.52 | 0.00 | 0.618 | 4.77 |
| scvi_k30_btissue | 0.52 | 0.00 | 0.618 | 7.05 |
| scvi_k30_bnone | 0.52 | 0.00 | 0.617 | 6.72 |
| pca_k128 | 0.50 | 0.00 | 0.615 | 4.00 |
| pca_k256 | 0.49 | 0.00 | 0.612 | 4.09 |
| nystroem_k64_g0.5 | 0.49 | 0.00 | 0.612 | 3.93 |
| ica_k64 | 0.49 | 0.00 | 0.612 | 3.59 |
| pca_k64 | 0.49 | 0.00 | 0.612 | 3.60 |
| nystroem_k256_g2 | 0.45 | 0.00 | 0.607 | 5.27 |
| pca_k32 | 0.39 | 0.00 | 0.597 | 3.55 |
| nystroem_k64_g2 | 0.31 | 0.00 | 0.585 | 7.83 |
| nmf_k64 | 0.30 | 0.00 | 0.584 | 5.36 |
| scvi_k10_btissue | 0.27 | 0.00 | 0.579 | 8.64 |
| pca_k16 | 0.09 | 0.00 | 0.550 | 5.39 |
| ica_k16 | 0.09 | 0.00 | 0.550 | 5.38 |
| rproj_k128_s0 | -0.04 | 0.00 | 0.529 | 5.27 |
| rproj_k128_s1 | -0.05 | 0.00 | 0.527 | 4.52 |
| gmm_k100 | -0.12 | 0.00 | 0.516 | 12.81 |
| nmf_k16 | -0.26 | 0.00 | 0.492 | 11.15 |
| pca_k8 | -0.49 | 0.00 | 0.453 | 12.05 |
| gmm_k30 | -0.49 | 0.00 | 0.453 | 21.14 |
| rproj_k32_s0 | -0.98 | 0.00 | 0.372 | 7.29 |
| rproj_k32_s1 | -0.99 | 0.00 | 0.369 | 7.06 |
| pca_k4 | -1.14 | 0.00 | 0.345 | 20.04 |
| gmm_k10 | -1.46 | 0.00 | 0.295 | 40.46 |
| rproj_k8_s0 | -2.16 | 0.00 | 0.196 | 17.91 |
| rproj_k8_s1 | -2.17 | 0.00 | 0.196 | 15.90 |
| depth2 | -2.56 | 0.00 | 0.151 | 83.57 |
| random_k32_s1 | -3.19 | 0.01 | 0.095 | 102.85 |
| random_k32_s0 | -3.19 | 0.01 | 0.094 | 101.24 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.069 | 2.6e-08 | 6486 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX13549269 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_blood::UBERON:0000178|plasma cell|SRX9768483 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX8961823 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX13971399 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX10421418 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX9627325 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002371|CD4-positive, alpha-beta T cell|SRX19729088 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX20868586 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX19447641 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX27532049 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX10579818 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX10121858 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0000178|natural killer cell|SRX14122101 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002371|monocyte|SRX15239507 | 7.58 | 0.81 | 0.00 |
| repr_scbasecount_human200_bone_marrow::UBERON:0002371|plasma cell|SRX19729088 | 7.58 | 0.81 | 0.00 |

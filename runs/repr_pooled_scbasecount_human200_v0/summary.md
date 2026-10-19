# Component A summary: repr_pooled_scbasecount_human200_v0


## cell_level

- items: 278050; informative (non-degenerate): 231347; nobody passes: 46365; everybody passes: 338
- difficulty percentiles 5/25/50/75/95: [-3.66, -2.41, -1.18, 0.76, 2.68]; median SE 0.50
- histogram (bin lower edge: count): -6: 0, -5: 4728, -4: 18161, -3: 51439, -2: 48957, -1: 32043, +0: 22669, +1: 26686, +2: 26664, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 0.10 | 0.01 | 0.539 | 0.68 |
| nystroem_k256_g0.5 | 0.08 | 0.01 | 0.538 | 0.45 |
| scvi_k30_bnone | 0.07 | 0.01 | 0.537 | 0.67 |
| pca_k128 | 0.04 | 0.01 | 0.534 | 0.38 |
| pca_k256 | 0.04 | 0.01 | 0.533 | 0.44 |
| nystroem_k64_g0.5 | 0.04 | 0.01 | 0.533 | 0.35 |
| ica_k64 | 0.03 | 0.01 | 0.532 | 0.33 |
| pca_k64 | 0.03 | 0.01 | 0.532 | 0.33 |
| nystroem_k256_g2 | 0.01 | 0.01 | 0.529 | 0.50 |
| pca_k32 | -0.07 | 0.01 | 0.521 | 0.35 |
| nystroem_k64_g2 | -0.13 | 0.01 | 0.514 | 0.51 |
| nmf_k64 | -0.16 | 0.01 | 0.511 | 0.59 |
| scvi_k10_btissue | -0.29 | 0.01 | 0.496 | 0.80 |
| pca_k16 | -0.34 | 0.01 | 0.489 | 0.44 |
| ica_k16 | -0.34 | 0.01 | 0.489 | 0.44 |
| gmm_k100 | -0.59 | 0.01 | 0.460 | 0.84 |
| rproj_k128_s0 | -0.67 | 0.01 | 0.450 | 0.85 |
| rproj_k128_s1 | -0.70 | 0.01 | 0.447 | 0.86 |
| nmf_k16 | -0.74 | 0.01 | 0.442 | 0.82 |
| gmm_k30 | -0.95 | 0.01 | 0.416 | 0.86 |
| pca_k8 | -0.97 | 0.01 | 0.413 | 0.82 |
| pca_k4 | -1.70 | 0.01 | 0.322 | 1.25 |
| rproj_k32_s0 | -1.75 | 0.01 | 0.317 | 1.35 |
| rproj_k32_s1 | -1.79 | 0.01 | 0.312 | 1.39 |
| gmm_k10 | -1.94 | 0.01 | 0.293 | 1.61 |
| rproj_k8_s0 | -2.85 | 0.01 | 0.189 | 2.53 |
| rproj_k8_s1 | -2.90 | 0.01 | 0.183 | 2.52 |
| depth2 | -3.11 | 0.01 | 0.162 | 5.62 |
| random_k32_s0 | -3.63 | 0.01 | 0.117 | 5.73 |
| random_k32_s1 | -3.63 | 0.01 | 0.117 | 5.82 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.077 | 6.3e-303 | 231347 |
| log_total_counts | -0.228 | 0.0e+00 | 231347 |
| n_genes_by_counts | -0.200 | 0.0e+00 | 231347 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| regulatory T cell | 178.0 | 1.55 | 948 |
| Langerhans cell | 25.0 | 0.60 | 328 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 5748.0 | 0.57 | 14419 |
| mature NK T cell | 3236.0 | 0.57 | 1113 |
| T cell | 4522.0 | 0.40 | 1138 |
| club cell | 522.0 | 0.16 | 979 |
| intermediate monocyte | 3735.0 | 0.14 | 1332 |
| myeloid dendritic cell | 886.0 | 0.04 | 236 |
| common myeloid progenitor | 2546.0 | 0.02 | 5085 |
| natural killer cell | 15024.0 | -0.02 | 18452 |
| non-classical monocyte | 1730.0 | -0.07 | 1642 |
| neutrophil | 5035.0 | -0.07 | 2952 |
| melanocyte | 2221.0 | -0.14 | 6170 |
| basal cell | 2875.0 | -0.24 | 2640 |
| hematopoietic precursor cell | 3590.0 | -0.39 | 764 |

## stratum_binomial

- items: 3526; informative (non-degenerate): 3431; nobody passes: 95; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.64, -1.56, -0.48, 0.77, 3.64]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 63, -3: 477, -2: 744, -1: 796, +0: 613, +1: 289, +2: 196, +3: 124, +4: 63, +5: 39

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | -0.16 | 0.00 | 0.539 | 9.31 |
| nystroem_k256_g0.5 | -0.17 | 0.00 | 0.538 | 5.86 |
| scvi_k30_bnone | -0.17 | 0.00 | 0.537 | 9.12 |
| pca_k128 | -0.19 | 0.00 | 0.534 | 4.62 |
| pca_k256 | -0.19 | 0.00 | 0.533 | 4.71 |
| nystroem_k64_g0.5 | -0.20 | 0.00 | 0.533 | 4.99 |
| ica_k64 | -0.20 | 0.00 | 0.532 | 4.35 |
| pca_k64 | -0.21 | 0.00 | 0.532 | 4.34 |
| nystroem_k256_g2 | -0.22 | 0.00 | 0.529 | 6.67 |
| pca_k32 | -0.27 | 0.00 | 0.521 | 4.28 |
| nystroem_k64_g2 | -0.31 | 0.00 | 0.514 | 8.39 |
| nmf_k64 | -0.34 | 0.00 | 0.511 | 6.51 |
| scvi_k10_btissue | -0.43 | 0.00 | 0.496 | 11.40 |
| pca_k16 | -0.47 | 0.00 | 0.489 | 6.63 |
| ica_k16 | -0.47 | 0.00 | 0.489 | 6.62 |
| gmm_k100 | -0.65 | 0.00 | 0.460 | 15.50 |
| rproj_k128_s0 | -0.71 | 0.00 | 0.450 | 6.73 |
| rproj_k128_s1 | -0.73 | 0.00 | 0.447 | 5.33 |
| nmf_k16 | -0.76 | 0.00 | 0.442 | 13.66 |
| gmm_k30 | -0.92 | 0.00 | 0.416 | 22.10 |
| pca_k8 | -0.93 | 0.00 | 0.413 | 15.02 |
| pca_k4 | -1.50 | 0.00 | 0.322 | 24.38 |
| rproj_k32_s0 | -1.54 | 0.00 | 0.317 | 9.01 |
| rproj_k32_s1 | -1.57 | 0.00 | 0.312 | 8.55 |
| gmm_k10 | -1.69 | 0.00 | 0.293 | 41.78 |
| rproj_k8_s0 | -2.45 | 0.01 | 0.189 | 21.17 |
| rproj_k8_s1 | -2.50 | 0.01 | 0.183 | 19.56 |
| depth2 | -2.69 | 0.01 | 0.162 | 91.33 |
| random_k32_s0 | -3.15 | 0.01 | 0.117 | 98.97 |
| random_k32_s1 | -3.15 | 0.01 | 0.117 | 100.80 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.246 | 1.4e-48 | 3431 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_human200_bone_marrow::UBERON:0002371|plasma cell|SRX19729088 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002371|monocyte|SRX15239507 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX20868586 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_blood::UBERON:0000178|plasma cell|SRX9768483 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX9627325 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX10121858 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX8961823 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX19447641 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX13971399 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX10579818 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0000178|natural killer cell|SRX14122101 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX10421418 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002371|CD4-positive, alpha-beta T cell|SRX19729088 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002097|neutrophil|SRX27532049 | 6.98 | 0.82 | 0.00 |
| repr_scbasecount_human200_multitissue::UBERON:0002107|monocyte|SRX13549269 | 6.98 | 0.82 | 0.00 |

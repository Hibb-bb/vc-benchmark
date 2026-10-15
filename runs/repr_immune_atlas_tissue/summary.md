# Component A summary: repr_immune_atlas_tissue


## cell_level

- items: 23038; informative (non-degenerate): 21829; nobody passes: 1202; everybody passes: 7
- difficulty percentiles 5/25/50/75/95: [-3.39, -1.98, -0.69, 0.9, 3.67]; median SE 0.56
- histogram (bin lower edge: count): -6: 0, -5: 226, -4: 895, -3: 2820, -2: 4864, -1: 4294, +0: 3335, +1: 1996, +2: 1669, +3: 1085, +4: 645, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 2.17 | 0.02 | 0.776 | 0.87 |
| nystroem_k256_g0.5 | 2.14 | 0.02 | 0.773 | 0.50 |
| scvi_k30_bnone | 2.12 | 0.02 | 0.771 | 0.79 |
| pca_k128 | 2.04 | 0.02 | 0.765 | 0.45 |
| pca_k64 | 2.00 | 0.02 | 0.761 | 0.32 |
| ica_k64 | 1.99 | 0.02 | 0.761 | 0.32 |
| pca_k256 | 1.99 | 0.02 | 0.761 | 0.61 |
| nystroem_k64_g0.5 | 1.94 | 0.02 | 0.756 | 0.36 |
| pca_k32 | 1.80 | 0.02 | 0.743 | 0.44 |
| scvi_k10_btissue | 1.67 | 0.02 | 0.732 | 0.90 |
| nystroem_k256_g2 | 1.63 | 0.02 | 0.728 | 0.62 |
| nmf_k64 | 1.32 | 0.02 | 0.697 | 0.84 |
| nystroem_k64_g2 | 1.22 | 0.02 | 0.686 | 1.05 |
| ica_k16 | 1.00 | 0.02 | 0.663 | 0.55 |
| pca_k16 | 1.00 | 0.02 | 0.663 | 0.54 |
| rproj_k128_s0 | 0.82 | 0.02 | 0.642 | 1.00 |
| rproj_k128_s1 | 0.76 | 0.02 | 0.635 | 0.98 |
| gmm_k100 | 0.39 | 0.02 | 0.589 | 0.97 |
| nmf_k16 | 0.09 | 0.02 | 0.551 | 1.09 |
| pca_k8 | -0.07 | 0.02 | 0.529 | 0.95 |
| gmm_k30 | -0.41 | 0.02 | 0.483 | 0.96 |
| rproj_k32_s0 | -0.67 | 0.02 | 0.446 | 1.45 |
| rproj_k32_s1 | -0.92 | 0.02 | 0.410 | 1.82 |
| pca_k4 | -1.20 | 0.02 | 0.370 | 1.79 |
| gmm_k10 | -1.77 | 0.02 | 0.291 | 1.55 |
| rproj_k8_s0 | -2.52 | 0.02 | 0.197 | 2.94 |
| rproj_k8_s1 | -2.76 | 0.02 | 0.171 | 3.45 |
| depth2 | -2.99 | 0.02 | 0.147 | 5.22 |
| random_k32_s1 | -4.48 | 0.03 | 0.048 | 6.97 |
| random_k32_s0 | -4.49 | 0.03 | 0.048 | 5.55 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.123 | 2.5e-74 | 21829 |
| log_total_counts | -0.019 | 5.7e-03 | 21829 |
| n_genes_by_counts | -0.029 | 2.4e-05 | 21829 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Cycling | 123.0 | 3.78 | 24 |
| Alveolar macrophages | 302.0 | 3.15 | 47 |
| migDC | 52.0 | 2.83 | 20 |
| ABCs | 284.0 | 2.56 | 247 |
| DC1 | 62.0 | 2.16 | 33 |
| MNP/B doublets | 166.0 | 2.04 | 208 |
| T/B doublets | 290.0 | 1.85 | 471 |
| Tnaive/CM_CD4_activated | 236.0 | 1.70 | 1048 |
| Tfh | 634.0 | 1.40 | 3656 |
| Tgd_CRTAM+ | 728.0 | 1.33 | 725 |
| Progenitor | 385.0 | 1.27 | 55 |
| Trm_Th1/Th17 | 827.0 | 1.17 | 3430 |
| Trm_gut_CD8 | 430.0 | 1.07 | 2311 |
| Teffector/EM_CD4 | 1326.0 | 1.00 | 3943 |
| GC_B (I) | 65.0 | 0.84 | 111 |

## stratum_binomial

- items: 521; informative (non-degenerate): 521; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.14, -1.19, -0.16, 0.96, 2.66]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 41, -2: 111, -1: 127, +0: 117, +1: 72, +2: 34, +3: 9, +4: 6, +5: 4

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 1.58 | 0.02 | 0.776 | 3.24 |
| nystroem_k256_g0.5 | 1.56 | 0.02 | 0.773 | 3.73 |
| scvi_k30_bnone | 1.55 | 0.02 | 0.771 | 2.64 |
| pca_k128 | 1.49 | 0.02 | 0.765 | 2.10 |
| pca_k64 | 1.47 | 0.02 | 0.761 | 1.83 |
| ica_k64 | 1.46 | 0.02 | 0.761 | 1.83 |
| pca_k256 | 1.46 | 0.02 | 0.761 | 2.72 |
| nystroem_k64_g0.5 | 1.42 | 0.02 | 0.756 | 2.05 |
| pca_k32 | 1.33 | 0.02 | 0.743 | 2.34 |
| scvi_k10_btissue | 1.25 | 0.02 | 0.732 | 3.45 |
| nystroem_k256_g2 | 1.22 | 0.02 | 0.728 | 4.06 |
| nmf_k64 | 1.01 | 0.02 | 0.697 | 3.38 |
| nystroem_k64_g2 | 0.93 | 0.02 | 0.686 | 13.57 |
| ica_k16 | 0.78 | 0.02 | 0.663 | 3.52 |
| pca_k16 | 0.78 | 0.02 | 0.663 | 3.48 |
| rproj_k128_s0 | 0.65 | 0.02 | 0.642 | 2.72 |
| rproj_k128_s1 | 0.61 | 0.02 | 0.635 | 3.09 |
| gmm_k100 | 0.34 | 0.02 | 0.589 | 7.94 |
| nmf_k16 | 0.12 | 0.02 | 0.551 | 8.09 |
| pca_k8 | -0.00 | 0.02 | 0.529 | 6.89 |
| gmm_k30 | -0.26 | 0.02 | 0.483 | 13.22 |
| rproj_k32_s0 | -0.47 | 0.02 | 0.446 | 4.35 |
| rproj_k32_s1 | -0.67 | 0.02 | 0.410 | 6.06 |
| pca_k4 | -0.90 | 0.02 | 0.370 | 10.49 |
| gmm_k10 | -1.38 | 0.02 | 0.291 | 21.02 |
| rproj_k8_s0 | -2.03 | 0.02 | 0.197 | 8.43 |
| rproj_k8_s1 | -2.24 | 0.02 | 0.171 | 6.45 |
| depth2 | -2.45 | 0.02 | 0.147 | 27.50 |
| random_k32_s1 | -3.82 | 0.03 | 0.048 | 20.32 |
| random_k32_s0 | -3.83 | 0.03 | 0.048 | 18.89 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.255 | 3.8e-09 | 521 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| spleen|Cycling|A29 | 5.33 | 0.40 | 0.01 |
| lung|Cycling|D496 | 5.20 | 0.28 | 0.01 |
| lung|Cycling|A29 | 5.14 | 0.31 | 0.01 |
| bone marrow|Cycling|A36 | 5.06 | 0.31 | 0.01 |
| bone marrow|Cycling|640C | 4.89 | 0.22 | 0.02 |
| bone marrow|Cycling|A29 | 4.82 | 0.22 | 0.02 |
| lung|Cycling|A36 | 4.81 | 0.20 | 0.02 |
| bone marrow|Cycling|D503 | 4.54 | 0.17 | 0.02 |
| bone marrow|Cycling|D496 | 4.51 | 0.17 | 0.02 |
| lung|Cycling|A31 | 4.21 | 0.21 | 0.03 |
| spleen|Tfh|A52 | 3.65 | 0.18 | 0.05 |
| lung|Alveolar macrophages|A37 | 3.62 | 0.16 | 0.05 |
| lung|Alveolar macrophages|D496 | 3.46 | 0.11 | 0.06 |
| lung|Cycling|D503 | 3.34 | 0.13 | 0.07 |
| bone marrow|Tnaive/CM_CD4_activated|D496 | 3.29 | 0.15 | 0.07 |

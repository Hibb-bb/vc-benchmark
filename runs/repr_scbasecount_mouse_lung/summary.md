# Component A summary: repr_scbasecount_mouse_lung


## cell_level

- items: 19238; informative (non-degenerate): 14530; nobody passes: 4691; everybody passes: 17
- difficulty percentiles 5/25/50/75/95: [-4.01, -2.92, -1.49, 0.55, 2.28]; median SE 0.52
- histogram (bin lower edge: count): -6: 272, -5: 1153, -4: 1481, -3: 3070, -2: 2528, -1: 1701, +0: 1580, +1: 1353, +2: 1392, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.13 | 0.02 | 0.504 | 0.41 |
| nystroem_k64_g0.5 | -0.15 | 0.02 | 0.502 | 0.33 |
| ica_k64 | -0.16 | 0.02 | 0.501 | 0.28 |
| pca_k64 | -0.17 | 0.02 | 0.500 | 0.28 |
| pca_k128 | -0.17 | 0.02 | 0.500 | 0.36 |
| nystroem_k256_g2 | -0.20 | 0.02 | 0.497 | 0.45 |
| pca_k256 | -0.23 | 0.02 | 0.494 | 0.47 |
| pca_k32 | -0.26 | 0.02 | 0.492 | 0.34 |
| nmf_k64 | -0.36 | 0.02 | 0.481 | 0.53 |
| pca_k16 | -0.62 | 0.02 | 0.456 | 0.36 |
| ica_k16 | -0.62 | 0.02 | 0.456 | 0.36 |
| nystroem_k64_g2 | -0.67 | 0.02 | 0.451 | 0.58 |
| rproj_k128_s0 | -0.70 | 0.02 | 0.447 | 0.66 |
| rproj_k128_s1 | -0.72 | 0.02 | 0.446 | 0.73 |
| gmm_k100 | -0.90 | 0.02 | 0.427 | 1.03 |
| nmf_k16 | -0.99 | 0.02 | 0.418 | 0.67 |
| pca_k8 | -1.32 | 0.02 | 0.382 | 0.85 |
| gmm_k30 | -1.43 | 0.02 | 0.371 | 0.99 |
| rproj_k32_s0 | -1.59 | 0.02 | 0.353 | 1.01 |
| rproj_k32_s1 | -1.71 | 0.02 | 0.341 | 1.23 |
| pca_k4 | -2.39 | 0.02 | 0.266 | 1.63 |
| gmm_k10 | -2.47 | 0.02 | 0.258 | 2.41 |
| rproj_k8_s0 | -2.82 | 0.02 | 0.222 | 1.85 |
| rproj_k8_s1 | -3.20 | 0.02 | 0.185 | 3.17 |
| depth2 | -3.86 | 0.03 | 0.128 | 5.61 |
| random_k32_s1 | -4.30 | 0.03 | 0.097 | 3.01 |
| random_k32_s0 | -4.30 | 0.03 | 0.097 | 2.88 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.257 | 1.2e-217 | 14530 |
| log_total_counts | -0.054 | 9.2e-11 | 14530 |
| n_genes_by_counts | -0.052 | 2.7e-10 | 14530 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mature NK T cell | 168.0 | 0.84 | 389 |
| plasmacytoid dendritic cell | 79.0 | 0.75 | 461 |
| plasma cell | 20.0 | 0.58 | 20 |
| leukocyte | 816.0 | 0.48 | 3583 |
| basophil | 37.0 | 0.44 | 272 |
| intermediate monocyte | 565.0 | 0.08 | 2710 |
| T cell | 489.0 | 0.03 | 943 |
| club cell | 753.0 | -0.13 | 2858 |
| lymphocyte | 226.0 | -0.13 | 232 |
| myeloid dendritic cell | 281.0 | -0.23 | 1467 |
| classical monocyte | 906.0 | -0.23 | 3707 |
| non-classical monocyte | 229.0 | -0.42 | 1496 |
| pulmonary alveolar type 1 cell | 277.0 | -0.43 | 118 |
| CD8-positive, alpha-beta T cell | 603.0 | -0.50 | 2131 |
| natural killer cell | 405.0 | -0.51 | 2101 |

## stratum_binomial

- items: 268; informative (non-degenerate): 254; nobody passes: 14; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.99, -1.64, -0.51, 0.81, 3.42]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 3, -4: 10, -3: 34, -2: 50, -1: 54, +0: 48, +1: 22, +2: 11, +3: 13, +4: 2, +5: 3

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.32 | 0.02 | 0.504 | 4.03 |
| nystroem_k64_g0.5 | -0.33 | 0.02 | 0.502 | 3.69 |
| ica_k64 | -0.34 | 0.02 | 0.501 | 2.74 |
| pca_k64 | -0.34 | 0.02 | 0.500 | 2.75 |
| pca_k128 | -0.34 | 0.02 | 0.500 | 3.08 |
| nystroem_k256_g2 | -0.36 | 0.02 | 0.497 | 4.69 |
| pca_k256 | -0.39 | 0.02 | 0.494 | 3.29 |
| pca_k32 | -0.40 | 0.02 | 0.492 | 3.15 |
| nmf_k64 | -0.48 | 0.02 | 0.481 | 3.86 |
| pca_k16 | -0.65 | 0.02 | 0.456 | 3.77 |
| ica_k16 | -0.65 | 0.02 | 0.456 | 3.77 |
| nystroem_k64_g2 | -0.69 | 0.02 | 0.451 | 12.26 |
| rproj_k128_s0 | -0.71 | 0.02 | 0.447 | 2.61 |
| rproj_k128_s1 | -0.72 | 0.02 | 0.446 | 3.43 |
| gmm_k100 | -0.85 | 0.02 | 0.427 | 26.30 |
| nmf_k16 | -0.92 | 0.02 | 0.418 | 10.28 |
| pca_k8 | -1.16 | 0.02 | 0.382 | 11.52 |
| gmm_k30 | -1.24 | 0.02 | 0.371 | 24.93 |
| rproj_k32_s0 | -1.37 | 0.02 | 0.353 | 5.54 |
| rproj_k32_s1 | -1.46 | 0.02 | 0.341 | 10.94 |
| pca_k4 | -2.01 | 0.02 | 0.266 | 31.71 |
| gmm_k10 | -2.07 | 0.02 | 0.258 | 71.39 |
| rproj_k8_s0 | -2.37 | 0.02 | 0.222 | 12.42 |
| rproj_k8_s1 | -2.70 | 0.02 | 0.185 | 20.83 |
| depth2 | -3.30 | 0.02 | 0.128 | 58.37 |
| random_k32_s1 | -3.70 | 0.03 | 0.097 | 56.66 |
| random_k32_s0 | -3.71 | 0.03 | 0.097 | 56.90 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.242 | 1.0e-04 | 254 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002048|plasmacytoid dendritic cell|SRX15126716 | 6.48 | 0.83 | 0.00 |
| UBERON:0002048|club cell|SRX23858293 | 6.23 | 0.83 | 0.00 |
| UBERON:0002048|fibroblast of lung|SRX27018920 | 6.15 | 0.64 | 0.00 |
| UBERON:0002048|mature NK T cell|SRX8497592 | 6.15 | 0.64 | 0.00 |
| UBERON:0002048|regulatory T cell|SRX18178210 | 5.92 | 0.64 | 0.00 |
| UBERON:0002048|CD8-positive, alpha-beta T cell|SRX8497592 | 5.34 | 0.43 | 0.00 |
| UBERON:0002048|natural killer cell|SRX18178210 | 5.34 | 0.43 | 0.00 |
| UBERON:0002048|plasmacytoid dendritic cell|SRX13218105 | 4.74 | 0.48 | 0.00 |
| UBERON:0002048|intermediate monocyte|SRX25402867 | 4.68 | 0.31 | 0.00 |
| UBERON:0002048|natural killer cell|SRX9148779 | 3.78 | 0.20 | 0.01 |
| UBERON:0002048|natural killer cell|SRX25402867 | 3.74 | 0.20 | 0.01 |
| UBERON:0002048|neutrophil|SRX9724294 | 3.59 | 0.35 | 0.01 |
| UBERON:0002048|T cell|SRX12876594 | 3.47 | 0.17 | 0.01 |
| UBERON:0002048|club cell|SRX29063259 | 3.39 | 0.26 | 0.01 |
| UBERON:0002048|dendritic cell|SRX9148781 | 3.34 | 0.19 | 0.01 |

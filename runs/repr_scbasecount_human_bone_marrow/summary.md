# Component A summary: repr_scbasecount_human_bone_marrow


## cell_level

- items: 15525; informative (non-degenerate): 13708; nobody passes: 1817; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.19, -2.08, -0.91, 0.91, 2.83]; median SE 0.48
- histogram (bin lower edge: count): -6: 0, -5: 84, -4: 644, -3: 3028, -2: 2765, -1: 2178, +0: 1909, +1: 1577, +2: 1523, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.42 | 0.02 | 0.583 | 0.69 |
| scvi_k30_btissue | 0.42 | 0.02 | 0.583 | 0.69 |
| nystroem_k256_g0.5 | 0.36 | 0.02 | 0.575 | 0.47 |
| scvi_k10_btissue | 0.25 | 0.02 | 0.561 | 0.80 |
| nystroem_k64_g0.5 | 0.23 | 0.02 | 0.559 | 0.40 |
| nystroem_k256_g2 | 0.22 | 0.02 | 0.557 | 0.55 |
| pca_k128 | 0.21 | 0.02 | 0.556 | 0.40 |
| ica_k64 | 0.18 | 0.02 | 0.553 | 0.35 |
| pca_k64 | 0.18 | 0.02 | 0.553 | 0.35 |
| pca_k256 | 0.17 | 0.02 | 0.552 | 0.50 |
| nystroem_k64_g2 | 0.03 | 0.02 | 0.534 | 0.61 |
| pca_k32 | -0.02 | 0.02 | 0.528 | 0.46 |
| nmf_k64 | -0.17 | 0.02 | 0.509 | 0.69 |
| ica_k16 | -0.31 | 0.02 | 0.490 | 0.51 |
| pca_k16 | -0.31 | 0.02 | 0.490 | 0.52 |
| gmm_k100 | -0.37 | 0.02 | 0.482 | 0.97 |
| nmf_k16 | -0.47 | 0.02 | 0.468 | 0.89 |
| rproj_k128_s0 | -0.84 | 0.02 | 0.420 | 1.03 |
| rproj_k128_s1 | -0.87 | 0.02 | 0.415 | 1.00 |
| pca_k8 | -1.01 | 0.02 | 0.396 | 0.89 |
| gmm_k30 | -1.01 | 0.02 | 0.396 | 1.07 |
| gmm_k10 | -1.67 | 0.02 | 0.306 | 1.47 |
| pca_k4 | -1.74 | 0.02 | 0.297 | 1.41 |
| rproj_k32_s0 | -1.85 | 0.02 | 0.282 | 1.69 |
| rproj_k32_s1 | -1.93 | 0.02 | 0.272 | 1.61 |
| depth2 | -2.60 | 0.02 | 0.190 | 4.48 |
| rproj_k8_s0 | -2.72 | 0.02 | 0.177 | 2.91 |
| rproj_k8_s1 | -3.04 | 0.03 | 0.144 | 3.73 |
| random_k32_s1 | -3.48 | 0.03 | 0.106 | 5.54 |
| random_k32_s0 | -3.49 | 0.03 | 0.105 | 5.70 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.140 | 9.8e-61 | 13708 |
| log_total_counts | -0.143 | 1.1e-63 | 13708 |
| n_genes_by_counts | -0.075 | 1.1e-18 | 13708 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| classical monocyte | 63.0 | 2.26 | 652 |
| T cell | 116.0 | 2.08 | 325 |
| intermediate monocyte | 335.0 | 0.89 | 606 |
| common myeloid progenitor | 668.0 | 0.68 | 1456 |
| plasmacytoid dendritic cell | 58.0 | 0.41 | 710 |
| macrophage | 494.0 | 0.31 | 723 |
| hematopoietic precursor cell | 986.0 | -0.16 | 2902 |
| CD4-positive, alpha-beta T cell | 1607.0 | -0.31 | 4511 |
| natural killer cell | 1142.0 | -0.45 | 2882 |
| plasma cell | 960.0 | -0.51 | 2582 |
| erythrocyte | 624.0 | -0.71 | 1317 |
| hematopoietic stem cell | 1096.0 | -0.80 | 1934 |
| CD8-positive, alpha-beta T cell | 1638.0 | -0.92 | 4734 |
| B cell | 1419.0 | -1.04 | 3693 |
| monocyte | 1457.0 | -1.09 | 4410 |

## stratum_binomial

- items: 200; informative (non-degenerate): 197; nobody passes: 3; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.1, -1.23, -0.36, 0.94, 3.8]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 14, -2: 51, -1: 46, +0: 39, +1: 19, +2: 11, +3: 10, +4: 6, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.02 | 0.02 | 0.583 | 7.18 |
| scvi_k30_btissue | 0.02 | 0.02 | 0.583 | 7.18 |
| nystroem_k256_g0.5 | -0.02 | 0.02 | 0.575 | 5.30 |
| scvi_k10_btissue | -0.11 | 0.02 | 0.561 | 8.05 |
| nystroem_k64_g0.5 | -0.12 | 0.02 | 0.559 | 4.21 |
| nystroem_k256_g2 | -0.13 | 0.02 | 0.557 | 6.79 |
| pca_k128 | -0.14 | 0.02 | 0.556 | 3.43 |
| ica_k64 | -0.15 | 0.02 | 0.553 | 3.04 |
| pca_k64 | -0.15 | 0.02 | 0.553 | 3.04 |
| pca_k256 | -0.16 | 0.02 | 0.552 | 3.58 |
| nystroem_k64_g2 | -0.26 | 0.02 | 0.534 | 8.54 |
| pca_k32 | -0.30 | 0.02 | 0.528 | 3.51 |
| nmf_k64 | -0.40 | 0.02 | 0.509 | 5.21 |
| ica_k16 | -0.51 | 0.02 | 0.490 | 5.71 |
| pca_k16 | -0.51 | 0.02 | 0.490 | 5.68 |
| gmm_k100 | -0.55 | 0.02 | 0.482 | 13.41 |
| nmf_k16 | -0.63 | 0.02 | 0.468 | 12.22 |
| rproj_k128_s0 | -0.89 | 0.02 | 0.420 | 4.19 |
| rproj_k128_s1 | -0.92 | 0.02 | 0.415 | 4.53 |
| pca_k8 | -1.02 | 0.02 | 0.396 | 14.43 |
| gmm_k30 | -1.02 | 0.02 | 0.396 | 29.17 |
| gmm_k10 | -1.54 | 0.02 | 0.306 | 32.67 |
| pca_k4 | -1.59 | 0.02 | 0.297 | 24.44 |
| rproj_k32_s0 | -1.68 | 0.02 | 0.282 | 10.87 |
| rproj_k32_s1 | -1.74 | 0.02 | 0.272 | 7.27 |
| depth2 | -2.30 | 0.02 | 0.190 | 72.54 |
| rproj_k8_s0 | -2.40 | 0.02 | 0.177 | 20.21 |
| rproj_k8_s1 | -2.69 | 0.02 | 0.144 | 22.63 |
| random_k32_s1 | -3.08 | 0.03 | 0.106 | 41.71 |
| random_k32_s0 | -3.09 | 0.03 | 0.105 | 38.54 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.401 | 5.4e-09 | 197 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002371|classical monocyte|SRX11342146 | 5.49 | 0.84 | 0.00 |
| UBERON:0002371|plasma cell|SRX12493324 | 4.87 | 0.35 | 0.00 |
| UBERON:0002371|classical monocyte|SRX15239507 | 4.73 | 0.48 | 0.00 |
| UBERON:0002371|myeloid dendritic cell|SRX13037848 | 4.50 | 0.48 | 0.01 |
| UBERON:0002371|classical monocyte|SRX15239512 | 4.48 | 0.43 | 0.01 |
| UBERON:0002371|plasma cell|SRX13037861 | 4.32 | 0.48 | 0.01 |
| UBERON:0002371|T cell|SRX15239512 | 4.02 | 0.30 | 0.01 |
| UBERON:0002371|classical monocyte|SRX13037848 | 3.97 | 0.31 | 0.01 |
| UBERON:0002371|T cell|SRX12493324 | 3.90 | 0.24 | 0.01 |
| UBERON:0002371|plasma cell|SRX12493331 | 3.85 | 0.30 | 0.01 |
| UBERON:0002371|plasma cell|SRX9619664 | 3.79 | 0.17 | 0.01 |
| UBERON:0002371|T cell|SRX12493331 | 3.61 | 0.17 | 0.01 |
| UBERON:0002371|classical monocyte|SRX15246037 | 3.53 | 0.30 | 0.02 |
| UBERON:0002371|erythrocyte|SRX12493324 | 3.51 | 0.21 | 0.02 |
| UBERON:0002371|T cell|SRX15246037 | 3.36 | 0.28 | 0.02 |

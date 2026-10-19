# Component A summary: repr_scbasecount_human200_bone_marrow


## cell_level

- items: 41262; informative (non-degenerate): 35613; nobody passes: 5649; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.99, -2.21, -1.03, 0.78, 2.71]; median SE 0.48
- histogram (bin lower edge: count): -6: 0, -5: 81, -4: 1430, -3: 8185, -2: 8478, -1: 4453, +0: 4475, +1: 4276, +2: 4235, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.31 | 0.01 | 0.569 | 0.75 |
| scvi_k30_btissue | 0.31 | 0.01 | 0.569 | 0.75 |
| nystroem_k256_g0.5 | 0.16 | 0.01 | 0.550 | 0.46 |
| nystroem_k256_g2 | 0.10 | 0.01 | 0.543 | 0.51 |
| nystroem_k64_g0.5 | 0.07 | 0.01 | 0.540 | 0.37 |
| pca_k256 | 0.06 | 0.01 | 0.538 | 0.43 |
| pca_k128 | 0.05 | 0.01 | 0.537 | 0.37 |
| ica_k64 | 0.03 | 0.01 | 0.535 | 0.34 |
| pca_k64 | 0.03 | 0.01 | 0.535 | 0.34 |
| nystroem_k64_g2 | -0.05 | 0.01 | 0.525 | 0.49 |
| pca_k32 | -0.06 | 0.01 | 0.524 | 0.37 |
| scvi_k10_btissue | -0.12 | 0.01 | 0.517 | 0.93 |
| ica_k16 | -0.25 | 0.01 | 0.501 | 0.42 |
| pca_k16 | -0.25 | 0.01 | 0.501 | 0.42 |
| nmf_k64 | -0.31 | 0.01 | 0.494 | 0.71 |
| nmf_k16 | -0.61 | 0.01 | 0.455 | 0.77 |
| gmm_k100 | -0.63 | 0.01 | 0.452 | 0.74 |
| pca_k8 | -0.77 | 0.01 | 0.433 | 0.73 |
| rproj_k128_s1 | -1.03 | 0.01 | 0.399 | 1.02 |
| rproj_k128_s0 | -1.03 | 0.01 | 0.399 | 0.99 |
| gmm_k30 | -1.17 | 0.01 | 0.381 | 1.18 |
| pca_k4 | -1.48 | 0.01 | 0.339 | 1.32 |
| rproj_k32_s1 | -2.18 | 0.01 | 0.249 | 2.00 |
| rproj_k32_s0 | -2.19 | 0.01 | 0.246 | 1.91 |
| gmm_k10 | -2.25 | 0.01 | 0.240 | 2.48 |
| depth2 | -2.56 | 0.01 | 0.202 | 2.99 |
| rproj_k8_s0 | -2.98 | 0.02 | 0.156 | 3.45 |
| rproj_k8_s1 | -3.07 | 0.02 | 0.147 | 3.80 |
| random_k32_s0 | -3.53 | 0.02 | 0.107 | 4.76 |
| random_k32_s1 | -3.53 | 0.02 | 0.107 | 5.00 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.029 | 4.3e-08 | 35613 |
| log_total_counts | -0.234 | 0.0e+00 | 35613 |
| n_genes_by_counts | -0.152 | 5.5e-184 | 35613 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| classical monocyte | 68.0 | 2.09 | 1069 |
| basophil | 38.0 | 2.07 | 422 |
| myeloid dendritic cell | 116.0 | 1.40 | 236 |
| T cell | 526.0 | 0.81 | 1138 |
| intermediate monocyte | 531.0 | 0.68 | 1332 |
| common myeloid progenitor | 2546.0 | 0.02 | 5085 |
| macrophage | 572.0 | -0.28 | 1650 |
| CD4-positive, alpha-beta T cell | 3261.0 | -0.29 | 12785 |
| hematopoietic precursor cell | 3156.0 | -0.38 | 9367 |
| plasma cell | 2594.0 | -0.61 | 6250 |
| natural killer cell | 2452.0 | -0.69 | 8671 |
| plasmacytoid dendritic cell | 396.0 | -0.72 | 1087 |
| B cell | 3147.0 | -0.72 | 8464 |
| monocyte | 3515.0 | -0.77 | 12012 |
| CD8-positive, alpha-beta T cell | 4467.0 | -0.79 | 14263 |

## stratum_binomial

- items: 513; informative (non-degenerate): 504; nobody passes: 9; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.16, -1.31, -0.39, 0.81, 3.11]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 37, -2: 135, -1: 129, +0: 94, +1: 48, +2: 29, +3: 18, +4: 6, +5: 6

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.03 | 0.01 | 0.569 | 9.92 |
| scvi_k30_btissue | 0.03 | 0.01 | 0.569 | 9.92 |
| nystroem_k256_g0.5 | -0.08 | 0.01 | 0.550 | 4.99 |
| nystroem_k256_g2 | -0.12 | 0.01 | 0.543 | 6.04 |
| nystroem_k64_g0.5 | -0.14 | 0.01 | 0.540 | 4.21 |
| pca_k256 | -0.15 | 0.01 | 0.538 | 3.80 |
| pca_k128 | -0.15 | 0.01 | 0.537 | 3.79 |
| pca_k64 | -0.17 | 0.01 | 0.535 | 3.74 |
| ica_k64 | -0.17 | 0.01 | 0.535 | 3.77 |
| nystroem_k64_g2 | -0.23 | 0.01 | 0.525 | 6.14 |
| pca_k32 | -0.23 | 0.01 | 0.524 | 4.06 |
| scvi_k10_btissue | -0.27 | 0.01 | 0.517 | 13.71 |
| ica_k16 | -0.36 | 0.01 | 0.501 | 4.84 |
| pca_k16 | -0.36 | 0.01 | 0.501 | 4.86 |
| nmf_k64 | -0.41 | 0.01 | 0.494 | 6.68 |
| nmf_k16 | -0.63 | 0.01 | 0.455 | 7.07 |
| gmm_k100 | -0.64 | 0.01 | 0.452 | 11.37 |
| pca_k8 | -0.75 | 0.01 | 0.433 | 10.17 |
| rproj_k128_s1 | -0.94 | 0.01 | 0.399 | 4.32 |
| rproj_k128_s0 | -0.94 | 0.01 | 0.399 | 4.59 |
| gmm_k30 | -1.04 | 0.01 | 0.381 | 24.86 |
| pca_k4 | -1.28 | 0.01 | 0.339 | 21.09 |
| rproj_k32_s1 | -1.85 | 0.01 | 0.249 | 11.55 |
| rproj_k32_s0 | -1.86 | 0.01 | 0.246 | 10.66 |
| gmm_k10 | -1.90 | 0.01 | 0.240 | 42.58 |
| depth2 | -2.17 | 0.01 | 0.202 | 40.16 |
| rproj_k8_s0 | -2.54 | 0.01 | 0.156 | 28.94 |
| rproj_k8_s1 | -2.62 | 0.01 | 0.147 | 28.58 |
| random_k32_s0 | -3.04 | 0.02 | 0.107 | 112.86 |
| random_k32_s1 | -3.04 | 0.02 | 0.107 | 113.92 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.235 | 9.2e-08 | 504 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002371|plasma cell|SRX19729088 | 7.03 | 0.82 | 0.00 |
| UBERON:0002371|basophil|SRX11489343 | 6.25 | 0.83 | 0.00 |
| UBERON:0002371|T cell|SRX12493321 | 5.92 | 0.48 | 0.00 |
| UBERON:0002371|basophil|SRX9444976 | 5.72 | 0.43 | 0.00 |
| UBERON:0002371|classical monocyte|SRX15239512 | 5.31 | 0.65 | 0.00 |
| UBERON:0002371|basophil|SRX23352644 | 5.30 | 0.54 | 0.00 |
| UBERON:0002371|classical monocyte|SRX13037846 | 5.28 | 0.54 | 0.00 |
| UBERON:0002371|neutrophil|SRX23414228 | 5.28 | 0.35 | 0.00 |
| UBERON:0002371|T cell|SRX11489343 | 4.69 | 0.55 | 0.00 |
| UBERON:0002371|T cell|SRX26220436 | 4.50 | 0.29 | 0.01 |
| UBERON:0002371|basophil|SRX18022824 | 4.33 | 0.48 | 0.01 |
| UBERON:0002371|CD4-positive, alpha-beta T cell|SRX19729088 | 4.29 | 0.21 | 0.01 |
| UBERON:0002371|intermediate monocyte|SRX10112698 | 4.21 | 0.23 | 0.01 |
| UBERON:0002371|T cell|SRX12493319 | 4.20 | 0.20 | 0.01 |
| UBERON:0002371|B cell|SRX9444976 | 3.98 | 0.18 | 0.01 |

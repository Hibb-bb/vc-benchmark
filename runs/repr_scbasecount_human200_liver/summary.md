# Component A summary: repr_scbasecount_human200_liver


## cell_level

- items: 17559; informative (non-degenerate): 14890; nobody passes: 2553; everybody passes: 116
- difficulty percentiles 5/25/50/75/95: [-3.21, -1.97, -0.92, 0.66, 2.57]; median SE 0.47
- histogram (bin lower edge: count): -6: 0, -5: 277, -4: 837, -3: 2554, -2: 3398, -1: 2376, +0: 2256, +1: 2225, +2: 967, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.03 | 0.02 | 0.518 | 0.44 |
| pca_k64 | -0.05 | 0.02 | 0.515 | 0.37 |
| ica_k64 | -0.06 | 0.02 | 0.515 | 0.38 |
| scvi_k30_bnone | -0.08 | 0.02 | 0.513 | 0.58 |
| scvi_k30_btissue | -0.08 | 0.02 | 0.513 | 0.58 |
| pca_k128 | -0.08 | 0.02 | 0.512 | 0.46 |
| nystroem_k64_g0.5 | -0.10 | 0.02 | 0.510 | 0.39 |
| pca_k256 | -0.11 | 0.02 | 0.509 | 0.55 |
| pca_k32 | -0.21 | 0.02 | 0.496 | 0.38 |
| nystroem_k256_g2 | -0.22 | 0.02 | 0.495 | 0.58 |
| nystroem_k64_g2 | -0.26 | 0.02 | 0.489 | 0.60 |
| nmf_k64 | -0.28 | 0.02 | 0.487 | 0.65 |
| scvi_k10_btissue | -0.36 | 0.02 | 0.477 | 0.72 |
| gmm_k100 | -0.54 | 0.02 | 0.453 | 1.25 |
| ica_k16 | -0.59 | 0.02 | 0.447 | 0.49 |
| pca_k16 | -0.59 | 0.02 | 0.447 | 0.49 |
| rproj_k128_s0 | -0.69 | 0.02 | 0.434 | 0.82 |
| rproj_k128_s1 | -0.69 | 0.02 | 0.434 | 0.77 |
| nmf_k16 | -0.76 | 0.02 | 0.425 | 0.81 |
| gmm_k30 | -0.97 | 0.02 | 0.397 | 0.83 |
| pca_k8 | -1.14 | 0.02 | 0.375 | 0.75 |
| rproj_k32_s0 | -1.81 | 0.02 | 0.289 | 1.17 |
| gmm_k10 | -1.87 | 0.02 | 0.281 | 2.43 |
| rproj_k32_s1 | -1.88 | 0.02 | 0.280 | 1.46 |
| pca_k4 | -1.90 | 0.02 | 0.278 | 1.44 |
| rproj_k8_s0 | -2.58 | 0.02 | 0.199 | 1.91 |
| rproj_k8_s1 | -2.70 | 0.02 | 0.187 | 2.21 |
| depth2 | -3.08 | 0.03 | 0.149 | 5.72 |
| random_k32_s0 | -3.13 | 0.03 | 0.145 | 3.49 |
| random_k32_s1 | -3.13 | 0.03 | 0.145 | 3.49 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.042 | 3.3e-07 | 14890 |
| log_total_counts | -0.184 | 9.0e-114 | 14890 |
| n_genes_by_counts | -0.165 | 9.5e-92 | 14890 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| classical monocyte | 136.0 | 1.51 | 388 |
| intermediate monocyte | 594.0 | 0.77 | 1559 |
| neutrophil | 544.0 | 0.55 | 2538 |
| plasma cell | 252.0 | 0.04 | 842 |
| CD4-positive, alpha-beta T cell | 814.0 | -0.05 | 4085 |
| natural killer cell | 816.0 | -0.07 | 3456 |
| CD8-positive, alpha-beta T cell | 1747.0 | -0.16 | 5982 |
| myeloid dendritic cell | 770.0 | -0.24 | 1088 |
| mature NK T cell | 851.0 | -0.31 | 3371 |
| non-classical monocyte | 607.0 | -0.49 | 751 |
| hematopoietic precursor cell | 392.0 | -0.80 | 822 |
| monocyte | 1747.0 | -0.84 | 5870 |
| B cell | 1205.0 | -0.84 | 3605 |
| macrophage | 2430.0 | -1.19 | 8247 |
| intrahepatic cholangiocyte | 233.0 | -1.37 | 1425 |

## stratum_binomial

- items: 227; informative (non-degenerate): 220; nobody passes: 7; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.54, -1.31, -0.46, 0.79, 3.61]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 30, -2: 34, -1: 76, +0: 32, +1: 18, +2: 15, +3: 6, +4: 8, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.23 | 0.02 | 0.518 | 5.66 |
| pca_k64 | -0.25 | 0.02 | 0.515 | 5.42 |
| ica_k64 | -0.25 | 0.02 | 0.515 | 5.40 |
| scvi_k30_bnone | -0.26 | 0.02 | 0.513 | 6.64 |
| scvi_k30_btissue | -0.26 | 0.02 | 0.513 | 6.64 |
| pca_k128 | -0.26 | 0.02 | 0.512 | 5.72 |
| nystroem_k64_g0.5 | -0.28 | 0.02 | 0.510 | 6.40 |
| pca_k256 | -0.28 | 0.02 | 0.509 | 6.17 |
| pca_k32 | -0.36 | 0.02 | 0.496 | 4.62 |
| nystroem_k256_g2 | -0.36 | 0.02 | 0.495 | 10.38 |
| nystroem_k64_g2 | -0.40 | 0.02 | 0.489 | 13.76 |
| nmf_k64 | -0.41 | 0.02 | 0.487 | 9.65 |
| scvi_k10_btissue | -0.46 | 0.02 | 0.477 | 10.71 |
| gmm_k100 | -0.60 | 0.02 | 0.453 | 40.63 |
| ica_k16 | -0.64 | 0.02 | 0.447 | 7.59 |
| pca_k16 | -0.64 | 0.02 | 0.447 | 7.61 |
| rproj_k128_s0 | -0.71 | 0.02 | 0.434 | 6.62 |
| rproj_k128_s1 | -0.71 | 0.02 | 0.434 | 4.44 |
| nmf_k16 | -0.76 | 0.02 | 0.425 | 12.57 |
| gmm_k30 | -0.92 | 0.02 | 0.397 | 21.24 |
| pca_k8 | -1.05 | 0.02 | 0.375 | 16.35 |
| rproj_k32_s0 | -1.57 | 0.02 | 0.289 | 8.12 |
| gmm_k10 | -1.63 | 0.02 | 0.281 | 96.73 |
| rproj_k32_s1 | -1.63 | 0.02 | 0.280 | 13.97 |
| pca_k4 | -1.64 | 0.02 | 0.278 | 29.94 |
| rproj_k8_s0 | -2.21 | 0.02 | 0.199 | 22.40 |
| rproj_k8_s1 | -2.31 | 0.02 | 0.187 | 27.71 |
| depth2 | -2.63 | 0.02 | 0.149 | 121.42 |
| random_k32_s0 | -2.67 | 0.02 | 0.145 | 93.62 |
| random_k32_s1 | -2.68 | 0.02 | 0.145 | 93.56 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.193 | 4.1e-03 | 220 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002107|intermediate monocyte|SRX9665017 | 5.20 | 0.65 | 0.00 |
| UBERON:0002107|natural killer cell|SRX11523864 | 4.60 | 0.37 | 0.00 |
| UBERON:0002107|monocyte|SRX15625585 | 4.44 | 0.40 | 0.01 |
| UBERON:0002107|intermediate monocyte|SRX10421418 | 4.40 | 0.31 | 0.01 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX8838566 | 4.19 | 0.35 | 0.01 |
| UBERON:0002107|neutrophil|SRX15765186 | 4.17 | 0.21 | 0.01 |
| UBERON:0002107|neutrophil|SRX24258454 | 4.00 | 0.20 | 0.01 |
| UBERON:0002107|plasma cell|SRX24258454 | 4.00 | 0.20 | 0.01 |
| UBERON:0002107|classical monocyte|SRX13549266 | 4.00 | 0.20 | 0.01 |
| UBERON:0002107|intermediate monocyte|SRX13549256 | 3.97 | 0.25 | 0.01 |
| UBERON:0002107|erythrocyte|SRX15625585 | 3.88 | 0.40 | 0.01 |
| UBERON:0002107|natural killer cell|SRX24258454 | 3.59 | 0.31 | 0.01 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX8838573 | 3.37 | 0.17 | 0.02 |
| UBERON:0002107|B cell|SRX10421418 | 3.35 | 0.14 | 0.02 |
| UBERON:0002107|classical monocyte|SRX13549267 | 3.11 | 0.13 | 0.02 |

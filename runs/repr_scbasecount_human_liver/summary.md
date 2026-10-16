# Component A summary: repr_scbasecount_human_liver


## cell_level

- items: 12681; informative (non-degenerate): 10795; nobody passes: 1807; everybody passes: 79
- difficulty percentiles 5/25/50/75/95: [-3.42, -1.85, -0.82, 0.53, 2.65]; median SE 0.45
- histogram (bin lower edge: count): -6: 0, -5: 106, -4: 940, -3: 1508, -2: 2432, -1: 2010, +0: 1873, +1: 1323, +2: 603, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 0.03 | 0.02 | 0.530 | 0.53 |
| ica_k64 | 0.03 | 0.02 | 0.529 | 0.46 |
| pca_k64 | 0.02 | 0.02 | 0.529 | 0.47 |
| nystroem_k256_g0.5 | 0.00 | 0.02 | 0.526 | 0.44 |
| pca_k256 | -0.01 | 0.02 | 0.525 | 0.58 |
| nystroem_k64_g0.5 | -0.03 | 0.02 | 0.521 | 0.38 |
| nystroem_k256_g2 | -0.07 | 0.02 | 0.517 | 0.53 |
| scvi_k30_btissue | -0.08 | 0.02 | 0.515 | 0.63 |
| scvi_k30_bnone | -0.08 | 0.02 | 0.515 | 0.63 |
| nmf_k64 | -0.16 | 0.02 | 0.504 | 0.64 |
| nystroem_k64_g2 | -0.16 | 0.02 | 0.504 | 0.61 |
| pca_k32 | -0.17 | 0.02 | 0.503 | 0.40 |
| rproj_k128_s0 | -0.43 | 0.02 | 0.468 | 0.73 |
| ica_k16 | -0.46 | 0.02 | 0.464 | 0.53 |
| pca_k16 | -0.47 | 0.02 | 0.463 | 0.53 |
| scvi_k10_btissue | -0.54 | 0.02 | 0.453 | 0.84 |
| rproj_k128_s1 | -0.56 | 0.02 | 0.450 | 0.80 |
| nmf_k16 | -0.66 | 0.02 | 0.438 | 0.84 |
| gmm_k100 | -0.68 | 0.02 | 0.434 | 0.92 |
| gmm_k30 | -0.89 | 0.02 | 0.406 | 0.93 |
| pca_k8 | -1.05 | 0.02 | 0.384 | 0.81 |
| rproj_k32_s0 | -1.33 | 0.02 | 0.345 | 1.18 |
| rproj_k32_s1 | -1.54 | 0.02 | 0.318 | 1.26 |
| gmm_k10 | -1.80 | 0.02 | 0.284 | 2.16 |
| pca_k4 | -1.87 | 0.03 | 0.275 | 1.47 |
| rproj_k8_s0 | -2.32 | 0.03 | 0.221 | 1.68 |
| rproj_k8_s1 | -2.39 | 0.03 | 0.212 | 1.89 |
| random_k32_s0 | -3.00 | 0.03 | 0.151 | 3.67 |
| random_k32_s1 | -3.00 | 0.03 | 0.151 | 3.67 |
| depth2 | -3.01 | 0.03 | 0.150 | 4.88 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.027 | 5.8e-03 | 10795 |
| log_total_counts | -0.129 | 5.6e-41 | 10795 |
| n_genes_by_counts | -0.115 | 6.6e-33 | 10795 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| plasma cell | 161.0 | 0.96 | 639 |
| intermediate monocyte | 325.0 | 0.88 | 1335 |
| classical monocyte | 164.0 | 0.70 | 446 |
| CD4-positive, alpha-beta T cell | 678.0 | 0.02 | 3006 |
| neutrophil | 540.0 | -0.02 | 1606 |
| mature NK T cell | 705.0 | -0.30 | 2035 |
| monocyte | 1208.0 | -0.49 | 4523 |
| intrahepatic cholangiocyte | 125.0 | -0.49 | 1212 |
| myeloid dendritic cell | 422.0 | -0.58 | 1103 |
| natural killer cell | 782.0 | -0.58 | 2843 |
| B cell | 827.0 | -0.61 | 2656 |
| hematopoietic precursor cell | 288.0 | -0.63 | 622 |
| CD8-positive, alpha-beta T cell | 1079.0 | -0.65 | 4054 |
| non-classical monocyte | 457.0 | -0.77 | 625 |
| fibroblast | 423.0 | -1.00 | 2792 |

## stratum_binomial

- items: 164; informative (non-degenerate): 158; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.7, -1.29, -0.48, 0.56, 3.84]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 3, -3: 11, -2: 31, -1: 62, +0: 21, +1: 13, +2: 3, +3: 7, +4: 3, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | -0.25 | 0.02 | 0.530 | 11.86 |
| ica_k64 | -0.25 | 0.02 | 0.529 | 11.69 |
| pca_k64 | -0.25 | 0.02 | 0.529 | 11.60 |
| nystroem_k256_g0.5 | -0.27 | 0.02 | 0.526 | 6.55 |
| pca_k256 | -0.27 | 0.02 | 0.525 | 9.40 |
| nystroem_k64_g0.5 | -0.29 | 0.02 | 0.521 | 6.11 |
| nystroem_k256_g2 | -0.32 | 0.02 | 0.517 | 8.87 |
| scvi_k30_btissue | -0.33 | 0.02 | 0.515 | 7.77 |
| scvi_k30_bnone | -0.33 | 0.02 | 0.515 | 7.77 |
| nmf_k64 | -0.39 | 0.02 | 0.504 | 12.33 |
| nystroem_k64_g2 | -0.39 | 0.02 | 0.504 | 12.16 |
| pca_k32 | -0.39 | 0.02 | 0.503 | 4.88 |
| rproj_k128_s0 | -0.59 | 0.02 | 0.468 | 5.26 |
| ica_k16 | -0.61 | 0.02 | 0.464 | 8.14 |
| pca_k16 | -0.61 | 0.02 | 0.463 | 8.11 |
| scvi_k10_btissue | -0.66 | 0.02 | 0.453 | 15.68 |
| rproj_k128_s1 | -0.68 | 0.02 | 0.450 | 5.44 |
| nmf_k16 | -0.75 | 0.02 | 0.438 | 20.39 |
| gmm_k100 | -0.77 | 0.02 | 0.434 | 18.28 |
| gmm_k30 | -0.93 | 0.02 | 0.406 | 23.12 |
| pca_k8 | -1.05 | 0.02 | 0.384 | 17.64 |
| rproj_k32_s0 | -1.27 | 0.02 | 0.345 | 10.19 |
| rproj_k32_s1 | -1.43 | 0.02 | 0.318 | 7.48 |
| gmm_k10 | -1.63 | 0.02 | 0.284 | 69.71 |
| pca_k4 | -1.69 | 0.02 | 0.275 | 27.58 |
| rproj_k8_s0 | -2.06 | 0.02 | 0.221 | 16.73 |
| rproj_k8_s1 | -2.12 | 0.02 | 0.212 | 20.88 |
| random_k32_s0 | -2.64 | 0.03 | 0.151 | 101.77 |
| random_k32_s1 | -2.64 | 0.03 | 0.151 | 101.59 |
| depth2 | -2.65 | 0.03 | 0.150 | 91.40 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.097 | 2.2e-01 | 158 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002107|plasma cell|SRX10112709 | 6.92 | 0.82 | 0.00 |
| UBERON:0002107|intermediate monocyte|SRX13549256 | 6.48 | 0.83 | 0.00 |
| UBERON:0002107|plasma cell|SRX10112705 | 6.40 | 0.64 | 0.00 |
| UBERON:0002107|classical monocyte|SRX10421418 | 5.01 | 0.65 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX10112709 | 4.45 | 0.27 | 0.01 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX10112705 | 4.36 | 0.30 | 0.01 |
| UBERON:0002107|non-classical monocyte|SRX13549256 | 4.05 | 0.44 | 0.01 |
| UBERON:0002107|B cell|SRX10421418 | 3.96 | 0.19 | 0.01 |
| UBERON:0002107|intermediate monocyte|SRX9207568 | 3.82 | 0.37 | 0.01 |
| UBERON:0002107|natural killer cell|SRX11523864 | 3.69 | 0.24 | 0.01 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX8838566 | 3.36 | 0.22 | 0.02 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX8838573 | 3.36 | 0.16 | 0.02 |
| UBERON:0002107|intermediate monocyte|SRX10421418 | 3.17 | 0.15 | 0.02 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX8838572 | 3.01 | 0.17 | 0.02 |
| UBERON:0002107|plasma cell|SRX8838566 | 2.80 | 0.13 | 0.03 |

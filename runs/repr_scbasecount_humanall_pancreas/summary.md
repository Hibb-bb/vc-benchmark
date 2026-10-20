# Component A summary: repr_scbasecount_humanall_pancreas


## cell_level

- items: 7488; informative (non-degenerate): 6852; nobody passes: 622; everybody passes: 14
- difficulty percentiles 5/25/50/75/95: [-3.36, -2.34, -1.07, 0.98, 3.79]; median SE 0.56
- histogram (bin lower edge: count): -6: 0, -5: 118, -4: 271, -3: 1374, -2: 1685, -1: 973, +0: 724, +1: 516, +2: 496, +3: 695, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 1.29 | 0.04 | 0.677 | 0.38 |
| pca_k128 | 1.26 | 0.04 | 0.674 | 0.34 |
| nystroem_k64_g0.5 | 1.24 | 0.04 | 0.673 | 0.26 |
| ica_k64 | 1.24 | 0.04 | 0.673 | 0.26 |
| pca_k64 | 1.24 | 0.04 | 0.673 | 0.26 |
| pca_k32 | 1.16 | 0.04 | 0.665 | 0.30 |
| nystroem_k256_g2 | 1.15 | 0.04 | 0.665 | 0.46 |
| pca_k256 | 1.14 | 0.04 | 0.663 | 0.49 |
| nmf_k64 | 1.08 | 0.04 | 0.658 | 0.43 |
| scvi_k30_bnone | 1.07 | 0.04 | 0.657 | 0.51 |
| scvi_k30_btissue | 1.07 | 0.04 | 0.657 | 0.51 |
| nystroem_k64_g2 | 0.98 | 0.04 | 0.648 | 0.54 |
| pca_k16 | 0.94 | 0.04 | 0.644 | 0.35 |
| ica_k16 | 0.94 | 0.04 | 0.644 | 0.35 |
| rproj_k128_s1 | 0.68 | 0.04 | 0.618 | 0.74 |
| nmf_k16 | 0.66 | 0.04 | 0.616 | 0.58 |
| rproj_k128_s0 | 0.63 | 0.04 | 0.613 | 0.78 |
| gmm_k100 | 0.50 | 0.04 | 0.599 | 0.97 |
| scvi_k10_btissue | 0.48 | 0.04 | 0.598 | 0.77 |
| gmm_k30 | 0.06 | 0.03 | 0.551 | 0.74 |
| pca_k8 | 0.05 | 0.03 | 0.550 | 0.78 |
| rproj_k32_s0 | -0.22 | 0.03 | 0.518 | 1.08 |
| rproj_k32_s1 | -0.33 | 0.03 | 0.505 | 1.31 |
| pca_k4 | -0.40 | 0.03 | 0.496 | 1.20 |
| gmm_k10 | -0.84 | 0.03 | 0.440 | 1.13 |
| rproj_k8_s0 | -1.39 | 0.03 | 0.367 | 2.32 |
| rproj_k8_s1 | -1.95 | 0.03 | 0.291 | 3.92 |
| depth2 | -2.84 | 0.03 | 0.183 | 18.11 |
| random_k32_s0 | -3.33 | 0.04 | 0.134 | 12.64 |
| random_k32_s1 | -3.39 | 0.04 | 0.129 | 12.79 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.143 | 1.1e-32 | 6852 |
| log_total_counts | -0.464 | 0.0e+00 | 6852 |
| n_genes_by_counts | -0.478 | 0.0e+00 | 6852 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| classical monocyte | 94.0 | 2.37 | 421 |
| plasma cell | 70.0 | 1.34 | 293 |
| fibroblast | 331.0 | 0.89 | 638 |
| natural killer cell | 222.0 | 0.81 | 1173 |
| CD4-positive, alpha-beta T cell | 480.0 | 0.66 | 1604 |
| B cell | 844.0 | 0.42 | 1841 |
| CD8-positive, alpha-beta T cell | 733.0 | 0.18 | 1850 |
| macrophage | 1090.0 | -0.18 | 2528 |
| pancreatic acinar cell | 246.0 | -0.90 | 555 |
| neutrophil | 352.0 | -0.92 | 434 |
| type B pancreatic cell | 159.0 | -1.11 | 400 |
| pancreatic stellate cell | 833.0 | -1.41 | 2035 |
| endothelial cell | 572.0 | -1.87 | 1276 |
| pancreatic ductal cell | 826.0 | -1.90 | 2468 |

## stratum_binomial

- items: 94; informative (non-degenerate): 94; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.91, -1.18, -0.33, 0.73, 3.16]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 3, -2: 25, -1: 27, +0: 18, +1: 8, +2: 7, +3: 3, +4: 2, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.67 | 0.03 | 0.677 | 3.83 |
| pca_k128 | 0.65 | 0.03 | 0.674 | 2.81 |
| nystroem_k64_g0.5 | 0.64 | 0.03 | 0.673 | 2.76 |
| ica_k64 | 0.63 | 0.03 | 0.673 | 2.39 |
| pca_k64 | 0.63 | 0.03 | 0.673 | 2.37 |
| pca_k32 | 0.58 | 0.03 | 0.665 | 2.91 |
| nystroem_k256_g2 | 0.58 | 0.03 | 0.665 | 3.58 |
| pca_k256 | 0.57 | 0.03 | 0.663 | 2.59 |
| nmf_k64 | 0.54 | 0.03 | 0.658 | 3.25 |
| scvi_k30_bnone | 0.53 | 0.03 | 0.657 | 3.97 |
| scvi_k30_btissue | 0.53 | 0.03 | 0.657 | 3.97 |
| nystroem_k64_g2 | 0.47 | 0.03 | 0.648 | 3.87 |
| pca_k16 | 0.45 | 0.03 | 0.644 | 3.61 |
| ica_k16 | 0.45 | 0.03 | 0.644 | 3.59 |
| rproj_k128_s1 | 0.29 | 0.03 | 0.618 | 2.44 |
| nmf_k16 | 0.28 | 0.03 | 0.616 | 6.30 |
| rproj_k128_s0 | 0.26 | 0.03 | 0.613 | 3.48 |
| gmm_k100 | 0.18 | 0.03 | 0.599 | 11.46 |
| scvi_k10_btissue | 0.17 | 0.03 | 0.598 | 9.60 |
| gmm_k30 | -0.10 | 0.03 | 0.551 | 14.04 |
| pca_k8 | -0.11 | 0.03 | 0.550 | 7.54 |
| rproj_k32_s0 | -0.28 | 0.03 | 0.518 | 2.97 |
| rproj_k32_s1 | -0.35 | 0.03 | 0.505 | 5.17 |
| pca_k4 | -0.40 | 0.03 | 0.496 | 12.63 |
| gmm_k10 | -0.70 | 0.03 | 0.440 | 28.56 |
| rproj_k8_s0 | -1.09 | 0.03 | 0.367 | 13.19 |
| rproj_k8_s1 | -1.52 | 0.03 | 0.291 | 18.13 |
| depth2 | -2.24 | 0.03 | 0.183 | 301.55 |
| random_k32_s0 | -2.66 | 0.04 | 0.134 | 54.41 |
| random_k32_s1 | -2.71 | 0.04 | 0.129 | 55.43 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.316 | 1.9e-03 | 94 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0001264|classical monocyte|SRX8778048 | 6.35 | 0.83 | 0.00 |
| UBERON:0001264|CD8-positive, alpha-beta T cell|SRX19176933 | 4.77 | 0.18 | 0.01 |
| UBERON:0001264|classical monocyte|SRX17495379 | 4.48 | 0.33 | 0.01 |
| UBERON:0001264|classical monocyte|SRX28908367 | 3.32 | 0.16 | 0.04 |
| UBERON:0001264|CD8-positive, alpha-beta T cell|SRX13880395 | 3.17 | 0.19 | 0.05 |
| UBERON:0001264|CD8-positive, alpha-beta T cell|SRX8778048 | 3.16 | 0.09 | 0.05 |
| UBERON:0001264|pancreatic stellate cell|SRX19176933 | 2.91 | 0.08 | 0.06 |
| UBERON:0001264|B cell|SRX8778048 | 2.71 | 0.08 | 0.07 |
| UBERON:0001264|CD4-positive, alpha-beta T cell|SRX28908367 | 2.46 | 0.06 | 0.09 |
| UBERON:0001264|B cell|SRX19176933 | 2.36 | 0.06 | 0.10 |
| UBERON:0001264|natural killer cell|SRX8778057 | 2.35 | 0.07 | 0.10 |
| UBERON:0001264|classical monocyte|SRX8778057 | 2.13 | 0.07 | 0.12 |
| UBERON:0001264|B cell|SRX13880395 | 2.00 | 0.09 | 0.14 |
| UBERON:0001264|B cell|SRX24412175 | 1.99 | 0.07 | 0.14 |
| UBERON:0001264|fibroblast|SRX8778048 | 1.93 | 0.08 | 0.14 |

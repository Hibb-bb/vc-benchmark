# Component A summary: repr_hao_pbmc_l2


## cell_level

- items: 7999; informative (non-degenerate): 7798; nobody passes: 198; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-2.78, -1.69, -0.47, 1.0, 3.7]; median SE 0.59
- histogram (bin lower edge: count): -6: 0, -5: 50, -4: 292, -3: 1292, -2: 1229, -1: 1672, +0: 1160, +1: 1006, +2: 461, +3: 357, +4: 187, +5: 92

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 3.57 | 0.05 | 0.887 | 0.73 |
| scvi_k30_bnone | 3.52 | 0.05 | 0.884 | 0.78 |
| scvi_k10_btissue | 3.26 | 0.05 | 0.870 | 0.92 |
| nystroem_k64_g0.5 | 3.02 | 0.04 | 0.856 | 0.22 |
| nystroem_k256_g0.5 | 3.01 | 0.04 | 0.855 | 0.29 |
| nystroem_k256_g2 | 2.94 | 0.04 | 0.850 | 0.44 |
| ica_k64 | 2.93 | 0.04 | 0.850 | 0.23 |
| pca_k64 | 2.92 | 0.04 | 0.849 | 0.23 |
| pca_k128 | 2.91 | 0.04 | 0.848 | 0.34 |
| pca_k32 | 2.81 | 0.04 | 0.842 | 0.28 |
| nystroem_k64_g2 | 2.79 | 0.04 | 0.840 | 0.54 |
| nmf_k64 | 2.78 | 0.04 | 0.839 | 0.84 |
| pca_k256 | 2.77 | 0.04 | 0.839 | 0.55 |
| ica_k16 | 1.86 | 0.04 | 0.763 | 0.52 |
| pca_k16 | 1.86 | 0.04 | 0.763 | 0.53 |
| gmm_k100 | 1.78 | 0.04 | 0.756 | 0.84 |
| rproj_k128_s1 | 1.55 | 0.03 | 0.732 | 1.07 |
| rproj_k128_s0 | 1.50 | 0.03 | 0.727 | 1.04 |
| gmm_k30 | 1.08 | 0.03 | 0.678 | 1.14 |
| nmf_k16 | 1.05 | 0.03 | 0.675 | 1.06 |
| pca_k8 | 0.16 | 0.03 | 0.556 | 0.98 |
| rproj_k32_s1 | -0.10 | 0.03 | 0.519 | 1.82 |
| pca_k4 | -0.22 | 0.03 | 0.501 | 1.16 |
| rproj_k32_s0 | -0.22 | 0.03 | 0.501 | 1.90 |
| gmm_k10 | -1.20 | 0.03 | 0.357 | 1.45 |
| rproj_k8_s1 | -1.99 | 0.03 | 0.248 | 4.76 |
| rproj_k8_s0 | -2.02 | 0.03 | 0.245 | 3.26 |
| depth2 | -2.24 | 0.03 | 0.217 | 3.38 |
| random_k32_s1 | -4.18 | 0.05 | 0.058 | 14.60 |
| random_k32_s0 | -4.19 | 0.05 | 0.058 | 11.80 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.395 | 7.8e-289 | 7798 |
| log_total_counts | -0.170 | 2.1e-51 | 7798 |
| n_genes_by_counts | -0.255 | 2.8e-116 | 7798 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| dnT | 74.0 | 3.80 | 47 |
| CD8 TCM | 429.0 | 2.02 | 1676 |
| Doublet | 102.0 | 1.88 | 317 |
| Treg | 436.0 | 1.54 | 1139 |
| CD4 TEM | 436.0 | 1.27 | 2430 |
| CD4 CTL | 149.0 | 1.23 | 1345 |
| gdT | 292.0 | 1.02 | 2006 |
| MAIT | 448.0 | 1.01 | 1004 |
| B intermediate | 434.0 | 0.95 | 1789 |
| CD4 TCM | 450.0 | 0.77 | 3000 |
| CD8 TEM | 443.0 | 0.28 | 2876 |
| NK Proliferating | 63.0 | -0.26 | 292 |
| NK_CD56bright | 219.0 | -0.30 | 690 |
| CD8 Naive | 450.0 | -0.39 | 2913 |
| B memory | 409.0 | -0.48 | 2092 |

## stratum_binomial

- items: 171; informative (non-degenerate): 171; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.13, -1.36, -0.32, 0.72, 1.68]; median SE 0.08
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 10, -2: 43, -1: 40, +0: 49, +1: 23, +2: 3, +3: 2, +4: 1, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 2.43 | 0.04 | 0.887 | 2.36 |
| scvi_k30_bnone | 2.40 | 0.04 | 0.884 | 2.47 |
| scvi_k10_btissue | 2.24 | 0.04 | 0.870 | 2.41 |
| nystroem_k64_g0.5 | 2.09 | 0.04 | 0.856 | 1.20 |
| nystroem_k256_g0.5 | 2.08 | 0.03 | 0.855 | 1.27 |
| nystroem_k256_g2 | 2.03 | 0.03 | 0.850 | 1.64 |
| ica_k64 | 2.03 | 0.03 | 0.850 | 1.17 |
| pca_k64 | 2.03 | 0.03 | 0.849 | 1.16 |
| pca_k128 | 2.02 | 0.03 | 0.848 | 1.27 |
| pca_k32 | 1.95 | 0.03 | 0.842 | 1.25 |
| nystroem_k64_g2 | 1.94 | 0.03 | 0.840 | 2.70 |
| nmf_k64 | 1.93 | 0.03 | 0.839 | 3.45 |
| pca_k256 | 1.93 | 0.03 | 0.839 | 1.58 |
| ica_k16 | 1.34 | 0.03 | 0.763 | 1.96 |
| pca_k16 | 1.34 | 0.03 | 0.763 | 1.95 |
| gmm_k100 | 1.29 | 0.03 | 0.756 | 4.43 |
| rproj_k128_s1 | 1.12 | 0.03 | 0.732 | 1.95 |
| rproj_k128_s0 | 1.09 | 0.03 | 0.727 | 2.20 |
| gmm_k30 | 0.79 | 0.03 | 0.678 | 14.33 |
| nmf_k16 | 0.77 | 0.03 | 0.675 | 5.22 |
| pca_k8 | 0.10 | 0.03 | 0.556 | 6.14 |
| rproj_k32_s1 | -0.10 | 0.03 | 0.519 | 2.68 |
| pca_k4 | -0.19 | 0.03 | 0.501 | 6.94 |
| rproj_k32_s0 | -0.20 | 0.03 | 0.501 | 3.03 |
| gmm_k10 | -0.99 | 0.03 | 0.357 | 17.16 |
| rproj_k8_s1 | -1.66 | 0.03 | 0.248 | 5.83 |
| rproj_k8_s0 | -1.68 | 0.03 | 0.245 | 5.31 |
| depth2 | -1.88 | 0.03 | 0.217 | 16.47 |
| random_k32_s1 | -3.59 | 0.05 | 0.058 | 14.92 |
| random_k32_s0 | -3.60 | 0.05 | 0.058 | 8.39 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.486 | 1.7e-11 | 171 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| 0|dnT|P2 | 4.33 | 0.14 | 0.05 |
| 7|dnT|P2 | 3.58 | 0.09 | 0.10 |
| 3|dnT|P2 | 3.21 | 0.08 | 0.14 |
| 3|Doublet|P3 | 2.98 | 0.09 | 0.16 |
| 0|Doublet|P3 | 2.29 | 0.08 | 0.26 |
| 7|Doublet|P2 | 2.05 | 0.09 | 0.30 |
| 0|CD8 TCM|P4 | 1.74 | 0.06 | 0.36 |
| 3|Doublet|P2 | 1.68 | 0.08 | 0.37 |
| 0|Doublet|P2 | 1.68 | 0.07 | 0.37 |
| 3|CD8 TCM|P4 | 1.67 | 0.06 | 0.37 |
| 0|CD8 TCM|P3 | 1.65 | 0.06 | 0.37 |
| 3|CD8 TCM|P3 | 1.62 | 0.06 | 0.38 |
| 3|Treg|P2 | 1.56 | 0.06 | 0.39 |
| 7|Treg|P2 | 1.52 | 0.06 | 0.40 |
| 3|CD4 TEM|P4 | 1.46 | 0.06 | 0.41 |

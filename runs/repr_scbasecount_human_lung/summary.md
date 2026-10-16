# Component A summary: repr_scbasecount_human_lung


## cell_level

- items: 20521; informative (non-degenerate): 19411; nobody passes: 1064; everybody passes: 46
- difficulty percentiles 5/25/50/75/95: [-2.92, -1.7, -0.6, 1.11, 3.33]; median SE 0.54
- histogram (bin lower edge: count): -6: 0, -5: 146, -4: 639, -3: 3819, -2: 3783, -1: 3097, +0: 2742, +1: 1816, +2: 2058, +3: 1311, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k64 | 1.57 | 0.02 | 0.716 | 0.31 |
| ica_k64 | 1.56 | 0.02 | 0.715 | 0.31 |
| nystroem_k64_g0.5 | 1.55 | 0.02 | 0.714 | 0.32 |
| pca_k128 | 1.50 | 0.02 | 0.709 | 0.41 |
| nystroem_k256_g0.5 | 1.50 | 0.02 | 0.709 | 0.41 |
| pca_k32 | 1.49 | 0.02 | 0.708 | 0.35 |
| pca_k256 | 1.44 | 0.02 | 0.703 | 0.54 |
| nystroem_k256_g2 | 1.36 | 0.02 | 0.695 | 0.44 |
| nmf_k64 | 1.28 | 0.02 | 0.686 | 0.53 |
| scvi_k30_bnone | 1.20 | 0.02 | 0.678 | 0.70 |
| scvi_k30_btissue | 1.20 | 0.02 | 0.678 | 0.70 |
| ica_k16 | 1.19 | 0.02 | 0.676 | 0.39 |
| pca_k16 | 1.19 | 0.02 | 0.676 | 0.40 |
| nystroem_k64_g2 | 0.93 | 0.02 | 0.647 | 0.64 |
| rproj_k128_s1 | 0.78 | 0.02 | 0.630 | 0.84 |
| rproj_k128_s0 | 0.77 | 0.02 | 0.628 | 0.86 |
| scvi_k10_btissue | 0.71 | 0.02 | 0.622 | 0.85 |
| nmf_k16 | 0.57 | 0.02 | 0.605 | 0.79 |
| gmm_k100 | 0.53 | 0.02 | 0.600 | 0.82 |
| pca_k8 | 0.20 | 0.02 | 0.558 | 0.97 |
| gmm_k30 | 0.15 | 0.02 | 0.551 | 0.97 |
| rproj_k32_s1 | -0.36 | 0.02 | 0.484 | 1.40 |
| rproj_k32_s0 | -0.48 | 0.02 | 0.467 | 1.54 |
| pca_k4 | -0.83 | 0.02 | 0.418 | 1.58 |
| gmm_k10 | -1.42 | 0.02 | 0.335 | 2.02 |
| rproj_k8_s1 | -2.07 | 0.02 | 0.248 | 3.27 |
| rproj_k8_s0 | -2.15 | 0.02 | 0.239 | 3.47 |
| depth2 | -2.34 | 0.02 | 0.215 | 7.56 |
| random_k32_s1 | -3.64 | 0.03 | 0.094 | 15.31 |
| random_k32_s0 | -3.67 | 0.03 | 0.092 | 14.93 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.156 | 8.6e-106 | 19411 |
| log_total_counts | -0.278 | 0.0e+00 | 19411 |
| n_genes_by_counts | -0.249 | 3.0e-272 | 19411 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mature NK T cell | 43.0 | 3.40 | 314 |
| natural killer cell | 394.0 | 1.64 | 736 |
| classical monocyte | 798.0 | 1.24 | 2559 |
| endothelial cell of artery | 600.0 | 1.23 | 495 |
| alveolar adventitial fibroblast | 366.0 | 1.18 | 188 |
| club cell | 167.0 | 1.05 | 292 |
| intermediate monocyte | 771.0 | 1.01 | 2965 |
| CD8-positive, alpha-beta T cell | 941.0 | 0.88 | 1702 |
| plasma cell | 1958.0 | 0.77 | 4562 |
| B cell | 2065.0 | 0.26 | 6798 |
| pericyte | 269.0 | 0.18 | 326 |
| bronchial smooth muscle cell | 291.0 | 0.05 | 198 |
| capillary endothelial cell | 825.0 | -0.05 | 1038 |
| neutrophil | 35.0 | -0.29 | 195 |
| pulmonary alveolar type 1 cell | 297.0 | -0.36 | 483 |

## stratum_binomial

- items: 283; informative (non-degenerate): 282; nobody passes: 1; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.03, -1.05, -0.21, 0.76, 2.32]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 15, -2: 64, -1: 69, +0: 75, +1: 38, +2: 12, +3: 5, +4: 1, +5: 2

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k64 | 1.01 | 0.02 | 0.716 | 2.32 |
| ica_k64 | 1.00 | 0.02 | 0.715 | 2.28 |
| nystroem_k64_g0.5 | 1.00 | 0.02 | 0.714 | 2.91 |
| pca_k128 | 0.97 | 0.02 | 0.709 | 2.71 |
| nystroem_k256_g0.5 | 0.96 | 0.02 | 0.709 | 3.43 |
| pca_k32 | 0.96 | 0.02 | 0.708 | 3.20 |
| pca_k256 | 0.92 | 0.02 | 0.703 | 2.80 |
| nystroem_k256_g2 | 0.87 | 0.02 | 0.695 | 3.41 |
| nmf_k64 | 0.82 | 0.02 | 0.686 | 2.76 |
| scvi_k30_bnone | 0.77 | 0.02 | 0.678 | 4.23 |
| scvi_k30_btissue | 0.77 | 0.02 | 0.678 | 4.23 |
| ica_k16 | 0.76 | 0.02 | 0.676 | 2.93 |
| pca_k16 | 0.76 | 0.02 | 0.676 | 2.93 |
| nystroem_k64_g2 | 0.59 | 0.02 | 0.647 | 9.37 |
| rproj_k128_s1 | 0.49 | 0.02 | 0.630 | 2.79 |
| rproj_k128_s0 | 0.48 | 0.02 | 0.628 | 3.14 |
| scvi_k10_btissue | 0.44 | 0.02 | 0.622 | 8.20 |
| nmf_k16 | 0.34 | 0.02 | 0.605 | 6.83 |
| gmm_k100 | 0.32 | 0.02 | 0.600 | 10.78 |
| pca_k8 | 0.09 | 0.02 | 0.558 | 12.48 |
| gmm_k30 | 0.05 | 0.02 | 0.551 | 19.75 |
| rproj_k32_s1 | -0.31 | 0.02 | 0.484 | 4.40 |
| rproj_k32_s0 | -0.40 | 0.02 | 0.467 | 7.16 |
| pca_k4 | -0.66 | 0.02 | 0.418 | 18.50 |
| gmm_k10 | -1.12 | 0.02 | 0.335 | 34.94 |
| rproj_k8_s1 | -1.65 | 0.02 | 0.248 | 13.85 |
| rproj_k8_s0 | -1.71 | 0.02 | 0.239 | 14.10 |
| depth2 | -1.88 | 0.02 | 0.215 | 62.70 |
| random_k32_s1 | -3.01 | 0.03 | 0.094 | 83.48 |
| random_k32_s0 | -3.04 | 0.03 | 0.092 | 77.61 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.161 | 6.9e-03 | 282 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002048|mature NK T cell|SRX13061245 | 8.03 | 0.80 | 0.00 |
| UBERON:0002048|mature NK T cell|SRX13198727 | 5.42 | 0.30 | 0.01 |
| UBERON:0002048|mature NK T cell|SRX10425169 | 5.19 | 0.40 | 0.01 |
| UBERON:0002048|capillary endothelial cell|SRX9276335 | 4.55 | 0.25 | 0.02 |
| UBERON:0002048|mature NK T cell|SRX25038170 | 3.71 | 0.11 | 0.04 |
| UBERON:0002048|basal cell|SRX29072177 | 3.63 | 0.21 | 0.04 |
| UBERON:0002048|plasma cell|SRX13061245 | 3.52 | 0.09 | 0.04 |
| UBERON:0002048|pulmonary alveolar type 1 cell|SRX9276306 | 3.17 | 0.17 | 0.06 |
| UBERON:0002048|capillary endothelial cell|SRX9276294 | 3.06 | 0.12 | 0.07 |
| UBERON:0002048|CD4-positive, alpha-beta T cell|SRX9276323 | 2.54 | 0.09 | 0.10 |
| UBERON:0002048|classical monocyte|SRX23724094 | 2.45 | 0.10 | 0.11 |
| UBERON:0002048|alveolar adventitial fibroblast|SRX9276306 | 2.43 | 0.06 | 0.11 |
| UBERON:0002048|natural killer cell|SRX23724098 | 2.43 | 0.09 | 0.11 |
| UBERON:0002048|B cell|SRX14767852 | 2.39 | 0.12 | 0.12 |
| UBERON:0002048|intermediate monocyte|SRX9276294 | 2.32 | 0.12 | 0.13 |

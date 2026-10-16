# Component A summary: repr_scbasecount_human_multitissue


## cell_level

- items: 23222; informative (non-degenerate): 18109; nobody passes: 5104; everybody passes: 9
- difficulty percentiles 5/25/50/75/95: [-3.76, -2.42, -0.87, 0.69, 1.78]; median SE 0.46
- histogram (bin lower edge: count): -6: 45, -5: 463, -4: 1855, -3: 3916, -2: 2746, -1: 2603, +0: 3029, +1: 3452, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k256 | -1.01 | 0.02 | 0.387 | 0.47 |
| pca_k128 | -1.03 | 0.02 | 0.384 | 0.42 |
| pca_k64 | -1.06 | 0.02 | 0.381 | 0.35 |
| ica_k64 | -1.07 | 0.02 | 0.380 | 0.35 |
| scvi_k30_bnone | -1.08 | 0.02 | 0.378 | 0.66 |
| nmf_k64 | -1.09 | 0.02 | 0.377 | 0.53 |
| pca_k32 | -1.10 | 0.02 | 0.377 | 0.41 |
| rproj_k128_s1 | -1.12 | 0.02 | 0.374 | 0.76 |
| nystroem_k64_g0.5 | -1.14 | 0.02 | 0.372 | 0.36 |
| scvi_k30_btissue | -1.15 | 0.02 | 0.370 | 0.66 |
| nystroem_k256_g0.5 | -1.17 | 0.02 | 0.368 | 0.40 |
| nystroem_k256_g2 | -1.18 | 0.02 | 0.367 | 0.39 |
| nystroem_k64_g2 | -1.20 | 0.02 | 0.364 | 0.42 |
| gmm_k100 | -1.26 | 0.02 | 0.357 | 0.56 |
| scvi_k10_btissue | -1.28 | 0.02 | 0.355 | 0.59 |
| rproj_k128_s0 | -1.32 | 0.02 | 0.351 | 0.65 |
| nmf_k16 | -1.38 | 0.02 | 0.343 | 0.79 |
| ica_k16 | -1.43 | 0.02 | 0.338 | 0.48 |
| pca_k16 | -1.43 | 0.02 | 0.338 | 0.48 |
| gmm_k30 | -1.73 | 0.02 | 0.304 | 0.97 |
| rproj_k32_s0 | -1.74 | 0.02 | 0.302 | 0.88 |
| rproj_k32_s1 | -1.84 | 0.02 | 0.291 | 1.01 |
| pca_k8 | -1.87 | 0.02 | 0.287 | 0.91 |
| pca_k4 | -2.19 | 0.02 | 0.252 | 1.48 |
| gmm_k10 | -2.37 | 0.02 | 0.232 | 1.86 |
| rproj_k8_s0 | -2.90 | 0.02 | 0.179 | 1.71 |
| depth2 | -3.09 | 0.02 | 0.161 | 4.56 |
| rproj_k8_s1 | -3.14 | 0.02 | 0.156 | 1.72 |
| random_k32_s0 | -3.82 | 0.02 | 0.102 | 4.24 |
| random_k32_s1 | -3.83 | 0.02 | 0.102 | 4.27 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.246 | 5.8e-248 | 18109 |
| log_total_counts | -0.063 | 3.5e-17 | 18109 |
| n_genes_by_counts | -0.025 | 6.9e-04 | 18109 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| pericyte | 52.0 | 1.27 | 241 |
| monocyte | 88.0 | 0.96 | 2131 |
| fibroblast | 999.0 | 0.90 | 1493 |
| mast cell | 180.0 | 0.74 | 44 |
| mature NK T cell | 414.0 | 0.66 | 649 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 715.0 | 0.43 | 1182 |
| classical monocyte | 382.0 | 0.10 | 719 |
| non-classical monocyte | 215.0 | 0.09 | 76 |
| CD8-positive, alpha-beta T cell | 4561.0 | -0.48 | 6278 |
| plasma cell | 896.0 | -0.84 | 3564 |
| natural killer cell | 920.0 | -1.04 | 3781 |
| erythrocyte | 364.0 | -1.13 | 914 |
| neutrophil | 417.0 | -1.27 | 688 |
| CD4-positive, alpha-beta T cell | 3454.0 | -1.27 | 6082 |
| common myeloid progenitor | 59.0 | -1.29 | 191 |

## stratum_binomial

- items: 283; informative (non-degenerate): 279; nobody passes: 4; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.83, -1.49, -0.36, 1.31, 4.68]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 13, -3: 29, -2: 56, -1: 61, +0: 35, +1: 39, +2: 17, +3: 14, +4: 4, +5: 9

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k256 | -0.96 | 0.02 | 0.387 | 6.24 |
| pca_k128 | -0.98 | 0.02 | 0.384 | 6.40 |
| pca_k64 | -1.00 | 0.02 | 0.381 | 5.09 |
| ica_k64 | -1.01 | 0.02 | 0.380 | 5.01 |
| scvi_k30_bnone | -1.02 | 0.02 | 0.378 | 10.05 |
| nmf_k64 | -1.03 | 0.02 | 0.377 | 7.46 |
| pca_k32 | -1.03 | 0.02 | 0.377 | 5.00 |
| rproj_k128_s1 | -1.05 | 0.02 | 0.374 | 7.17 |
| nystroem_k64_g0.5 | -1.06 | 0.02 | 0.372 | 5.69 |
| scvi_k30_btissue | -1.07 | 0.02 | 0.370 | 9.68 |
| nystroem_k256_g0.5 | -1.09 | 0.02 | 0.368 | 5.66 |
| nystroem_k256_g2 | -1.09 | 0.02 | 0.367 | 5.30 |
| nystroem_k64_g2 | -1.11 | 0.02 | 0.364 | 7.16 |
| gmm_k100 | -1.16 | 0.02 | 0.357 | 12.88 |
| scvi_k10_btissue | -1.18 | 0.02 | 0.355 | 7.02 |
| rproj_k128_s0 | -1.20 | 0.02 | 0.351 | 6.18 |
| nmf_k16 | -1.25 | 0.02 | 0.343 | 15.91 |
| ica_k16 | -1.29 | 0.02 | 0.338 | 9.11 |
| pca_k16 | -1.29 | 0.02 | 0.338 | 9.16 |
| gmm_k30 | -1.52 | 0.02 | 0.304 | 24.36 |
| rproj_k32_s0 | -1.53 | 0.02 | 0.302 | 6.65 |
| rproj_k32_s1 | -1.61 | 0.02 | 0.291 | 7.99 |
| pca_k8 | -1.64 | 0.02 | 0.287 | 16.18 |
| pca_k4 | -1.89 | 0.02 | 0.252 | 35.04 |
| gmm_k10 | -2.05 | 0.02 | 0.232 | 75.51 |
| rproj_k8_s0 | -2.49 | 0.02 | 0.179 | 17.41 |
| depth2 | -2.66 | 0.02 | 0.161 | 118.21 |
| rproj_k8_s1 | -2.70 | 0.02 | 0.156 | 9.52 |
| random_k32_s0 | -3.31 | 0.02 | 0.102 | 44.90 |
| random_k32_s1 | -3.32 | 0.02 | 0.102 | 46.19 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.523 | 5.4e-21 | 279 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002097|neutrophil|SRX27532049 | 6.32 | 0.83 | 0.00 |
| UBERON:0000029|natural killer cell|ERX12093805 | 6.14 | 0.83 | 0.00 |
| UBERON:0002370|erythrocyte|SRX15829407 | 5.79 | 0.64 | 0.00 |
| UBERON:0002370|erythrocyte|SRX25183951 | 5.79 | 0.64 | 0.00 |
| UBERON:0001969|naive thymus-derived CD4-positive, alpha-beta T cell|SRX10977992 | 5.79 | 0.64 | 0.00 |
| UBERON:0002370|erythrocyte|SRX7691515 | 5.45 | 0.54 | 0.00 |
| UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|SRX26161096 | 5.45 | 0.54 | 0.00 |
| UBERON:0002370|erythrocyte|SRX15829410 | 5.45 | 0.54 | 0.00 |
| UBERON:0002097|classical monocyte|SRX10104848 | 5.19 | 0.48 | 0.00 |
| UBERON:0002097|classical monocyte|SRX10104846 | 5.19 | 0.48 | 0.00 |
| UBERON:0002370|erythrocyte|SRX24338654 | 5.19 | 0.48 | 0.00 |
| UBERON:0000029|monocyte|ERX12093805 | 4.98 | 0.43 | 0.00 |
| UBERON:0002370|erythrocyte|SRX25183953 | 4.81 | 0.40 | 0.00 |
| UBERON:0002097|naive thymus-derived CD4-positive, alpha-beta T cell|SRX10104846 | 4.81 | 0.40 | 0.00 |
| UBERON:0002370|erythrocyte|SRX25183952 | 4.66 | 0.37 | 0.00 |

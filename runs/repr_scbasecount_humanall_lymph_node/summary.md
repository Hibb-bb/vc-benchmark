# Component A summary: repr_scbasecount_humanall_lymph_node


## cell_level

- items: 5388; informative (non-degenerate): 4512; nobody passes: 876; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.08, -2.04, -0.92, 0.55, 2.23]; median SE 0.44
- histogram (bin lower edge: count): -6: 0, -5: 20, -4: 273, -3: 861, -2: 997, -1: 872, +0: 690, +1: 479, +2: 320, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.40 | 0.04 | 0.472 | 0.58 |
| nystroem_k256_g2 | -0.42 | 0.04 | 0.469 | 0.61 |
| pca_k128 | -0.43 | 0.04 | 0.468 | 0.49 |
| pca_k256 | -0.46 | 0.04 | 0.465 | 0.58 |
| ica_k64 | -0.46 | 0.04 | 0.464 | 0.41 |
| pca_k64 | -0.47 | 0.04 | 0.463 | 0.41 |
| nystroem_k64_g0.5 | -0.47 | 0.04 | 0.462 | 0.45 |
| nystroem_k64_g2 | -0.54 | 0.04 | 0.453 | 0.54 |
| scvi_k30_bnone | -0.57 | 0.04 | 0.449 | 0.73 |
| scvi_k30_btissue | -0.57 | 0.04 | 0.449 | 0.73 |
| pca_k32 | -0.60 | 0.04 | 0.445 | 0.44 |
| nmf_k64 | -0.62 | 0.04 | 0.442 | 0.72 |
| gmm_k100 | -0.71 | 0.04 | 0.429 | 0.86 |
| scvi_k10_btissue | -0.76 | 0.04 | 0.423 | 0.86 |
| ica_k16 | -0.92 | 0.04 | 0.400 | 0.48 |
| pca_k16 | -0.92 | 0.04 | 0.400 | 0.48 |
| pca_k8 | -1.16 | 0.04 | 0.367 | 0.63 |
| nmf_k16 | -1.23 | 0.04 | 0.357 | 0.95 |
| gmm_k30 | -1.41 | 0.04 | 0.332 | 0.84 |
| rproj_k128_s0 | -1.44 | 0.04 | 0.328 | 1.10 |
| rproj_k128_s1 | -1.47 | 0.04 | 0.324 | 1.08 |
| pca_k4 | -1.89 | 0.04 | 0.268 | 1.20 |
| rproj_k32_s1 | -2.14 | 0.04 | 0.236 | 1.22 |
| rproj_k32_s0 | -2.16 | 0.04 | 0.234 | 1.46 |
| gmm_k10 | -2.22 | 0.04 | 0.226 | 0.99 |
| depth2 | -2.38 | 0.04 | 0.207 | 2.17 |
| rproj_k8_s0 | -2.77 | 0.04 | 0.164 | 2.16 |
| rproj_k8_s1 | -2.90 | 0.04 | 0.151 | 2.03 |
| random_k32_s0 | -2.92 | 0.04 | 0.149 | 3.07 |
| random_k32_s1 | -2.92 | 0.04 | 0.149 | 3.24 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.051 | 6.1e-04 | 4512 |
| log_total_counts | -0.111 | 8.8e-14 | 4512 |
| n_genes_by_counts | -0.068 | 5.5e-06 | 4512 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| natural killer cell | 40.0 | 1.35 | 348 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 286.0 | 0.86 | 706 |
| regulatory T cell | 221.0 | 0.54 | 683 |
| monocyte | 176.0 | -0.16 | 1395 |
| CD4-positive, alpha-beta T cell | 904.0 | -0.55 | 2127 |
| stromal cell | 199.0 | -0.66 | 1000 |
| CD8-positive, alpha-beta T cell | 1035.0 | -0.68 | 2518 |
| T cell | 765.0 | -0.75 | 2923 |
| plasma cell | 274.0 | -1.76 | 1518 |
| endothelial cell | 200.0 | -1.95 | 1479 |
| B cell | 345.0 | -2.14 | 2093 |
| erythrocyte | 21.0 | -2.80 | 1127 |
| neutrophil | 39.0 | -3.09 | 610 |

## stratum_binomial

- items: 72; informative (non-degenerate): 69; nobody passes: 3; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.92, -0.98, -0.38, 1.19, 3.25]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 4, -2: 13, -1: 23, +0: 10, +1: 11, +2: 4, +3: 3, +4: 0, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.39 | 0.03 | 0.472 | 4.86 |
| nystroem_k256_g2 | -0.40 | 0.03 | 0.469 | 6.19 |
| pca_k128 | -0.41 | 0.03 | 0.468 | 3.97 |
| pca_k256 | -0.43 | 0.03 | 0.465 | 3.64 |
| ica_k64 | -0.43 | 0.03 | 0.464 | 3.95 |
| pca_k64 | -0.43 | 0.03 | 0.463 | 4.08 |
| nystroem_k64_g0.5 | -0.44 | 0.03 | 0.462 | 4.93 |
| nystroem_k64_g2 | -0.49 | 0.03 | 0.453 | 6.25 |
| scvi_k30_bnone | -0.51 | 0.03 | 0.449 | 8.06 |
| scvi_k30_btissue | -0.51 | 0.03 | 0.449 | 8.06 |
| pca_k32 | -0.53 | 0.03 | 0.445 | 4.39 |
| nmf_k64 | -0.55 | 0.03 | 0.442 | 5.33 |
| gmm_k100 | -0.62 | 0.03 | 0.429 | 12.03 |
| scvi_k10_btissue | -0.66 | 0.03 | 0.423 | 9.53 |
| ica_k16 | -0.78 | 0.03 | 0.400 | 6.51 |
| pca_k16 | -0.78 | 0.03 | 0.400 | 6.50 |
| pca_k8 | -0.96 | 0.03 | 0.367 | 6.92 |
| nmf_k16 | -1.02 | 0.03 | 0.357 | 7.89 |
| gmm_k30 | -1.16 | 0.03 | 0.332 | 21.40 |
| rproj_k128_s0 | -1.18 | 0.03 | 0.328 | 3.57 |
| rproj_k128_s1 | -1.21 | 0.03 | 0.324 | 4.31 |
| pca_k4 | -1.54 | 0.03 | 0.268 | 17.66 |
| rproj_k32_s1 | -1.75 | 0.04 | 0.236 | 9.30 |
| rproj_k32_s0 | -1.76 | 0.04 | 0.234 | 8.31 |
| gmm_k10 | -1.82 | 0.04 | 0.226 | 23.74 |
| depth2 | -1.95 | 0.04 | 0.207 | 38.40 |
| rproj_k8_s0 | -2.28 | 0.04 | 0.164 | 21.01 |
| rproj_k8_s1 | -2.39 | 0.04 | 0.151 | 19.36 |
| random_k32_s0 | -2.41 | 0.04 | 0.149 | 51.53 |
| random_k32_s1 | -2.41 | 0.04 | 0.149 | 57.71 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.315 | 8.4e-03 | 69 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|SRX11485406 | 5.56 | 0.84 | 0.00 |
| UBERON:0000029|macrophage|ERX12093805 | 3.69 | 0.33 | 0.01 |
| UBERON:0000029|monocyte|SRX17467518 | 3.67 | 0.37 | 0.01 |
| UBERON:0000029|natural killer cell|ERX12093805 | 3.47 | 0.17 | 0.01 |
| UBERON:0000029|plasma cell|SRX11485423 | 2.91 | 0.24 | 0.02 |
| UBERON:0000029|CD8-positive, alpha-beta T cell|ERX12093805 | 2.26 | 0.17 | 0.04 |
| UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|ERX12093794 | 2.23 | 0.09 | 0.04 |
| UBERON:0000029|plasma cell|SRX23425669 | 2.22 | 0.14 | 0.04 |
| UBERON:0000029|B cell|SRX17467518 | 1.85 | 0.17 | 0.06 |
| UBERON:0000029|CD4-positive, alpha-beta T cell|ERX12093805 | 1.74 | 0.07 | 0.07 |
| UBERON:0000029|plasma cell|SRX17467518 | 1.62 | 0.13 | 0.07 |
| UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|ERX12093807 | 1.55 | 0.07 | 0.08 |
| UBERON:0000029|regulatory T cell|ERX12093794 | 1.54 | 0.08 | 0.08 |
| UBERON:0000029|CD4-positive, alpha-beta T cell|SRX11485423 | 1.45 | 0.10 | 0.09 |
| UBERON:0000029|CD8-positive, alpha-beta T cell|SRX13722302 | 1.41 | 0.09 | 0.09 |

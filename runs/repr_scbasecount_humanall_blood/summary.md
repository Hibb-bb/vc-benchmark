# Component A summary: repr_scbasecount_humanall_blood


## cell_level

- items: 155377; informative (non-degenerate): 134767; nobody passes: 20556; everybody passes: 54
- difficulty percentiles 5/25/50/75/95: [-3.0, -2.0, -0.78, 0.77, 2.68]; median SE 0.45
- histogram (bin lower edge: count): -6: 0, -5: 285, -4: 13112, -3: 24150, -2: 23282, -1: 23663, +0: 20421, +1: 15702, +2: 14152, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.28 | 0.01 | 0.564 | 0.87 |
| scvi_k30_btissue | 0.28 | 0.01 | 0.564 | 0.87 |
| pca_k256 | 0.02 | 0.01 | 0.532 | 0.51 |
| nystroem_k256_g0.5 | 0.01 | 0.01 | 0.530 | 0.55 |
| scvi_k10_btissue | -0.02 | 0.01 | 0.526 | 1.08 |
| pca_k128 | -0.04 | 0.01 | 0.524 | 0.46 |
| nystroem_k64_g0.5 | -0.10 | 0.01 | 0.516 | 0.45 |
| pca_k64 | -0.11 | 0.01 | 0.515 | 0.40 |
| ica_k64 | -0.11 | 0.01 | 0.515 | 0.40 |
| nmf_k64 | -0.11 | 0.01 | 0.514 | 0.61 |
| nystroem_k256_g2 | -0.12 | 0.01 | 0.512 | 0.63 |
| pca_k32 | -0.18 | 0.01 | 0.505 | 0.44 |
| nystroem_k64_g2 | -0.31 | 0.01 | 0.487 | 0.60 |
| nmf_k16 | -0.49 | 0.01 | 0.463 | 0.72 |
| pca_k16 | -0.53 | 0.01 | 0.458 | 0.53 |
| ica_k16 | -0.53 | 0.01 | 0.458 | 0.53 |
| gmm_k100 | -0.66 | 0.01 | 0.441 | 1.01 |
| rproj_k128_s1 | -0.69 | 0.01 | 0.437 | 0.83 |
| rproj_k128_s0 | -0.73 | 0.01 | 0.431 | 0.89 |
| gmm_k30 | -0.95 | 0.01 | 0.401 | 0.72 |
| pca_k8 | -0.97 | 0.01 | 0.398 | 0.72 |
| gmm_k10 | -1.30 | 0.01 | 0.353 | 1.12 |
| pca_k4 | -1.41 | 0.01 | 0.338 | 0.84 |
| rproj_k32_s1 | -1.70 | 0.01 | 0.300 | 1.42 |
| rproj_k32_s0 | -1.72 | 0.01 | 0.297 | 1.36 |
| rproj_k8_s0 | -2.41 | 0.01 | 0.211 | 1.78 |
| rproj_k8_s1 | -2.49 | 0.01 | 0.202 | 2.13 |
| depth2 | -2.50 | 0.01 | 0.201 | 5.04 |
| random_k32_s1 | -2.90 | 0.01 | 0.158 | 2.40 |
| random_k32_s0 | -2.90 | 0.01 | 0.158 | 2.40 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.046 | 1.8e-64 | 134767 |
| log_total_counts | -0.126 | 0.0e+00 | 134767 |
| n_genes_by_counts | -0.087 | 5.5e-225 | 134767 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| intermediate monocyte | 82.0 | 2.34 | 226 |
| mature NK T cell | 929.0 | 1.38 | 4088 |
| hematopoietic stem cell | 105.0 | 0.83 | 587 |
| CD8-positive, alpha-beta T cell | 15383.0 | 0.80 | 64372 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 16358.0 | 0.48 | 55494 |
| hematopoietic precursor cell | 910.0 | 0.45 | 3007 |
| macrophage | 8436.0 | 0.41 | 27673 |
| non-classical monocyte | 4166.0 | -0.15 | 7281 |
| natural killer cell | 21031.0 | -0.24 | 64825 |
| plasma cell | 4143.0 | -1.00 | 7396 |
| CD4-positive, alpha-beta T cell | 24564.0 | -1.09 | 83656 |
| neutrophil | 2205.0 | -1.12 | 6827 |
| platelet | 4449.0 | -1.67 | 12027 |
| B cell | 16412.0 | -1.77 | 58136 |
| classical monocyte | 12750.0 | -2.25 | 47712 |

## stratum_binomial

- items: 1947; informative (non-degenerate): 1905; nobody passes: 42; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.57, -1.49, -0.2, 0.76, 3.36]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 14, -3: 298, -2: 317, -1: 471, +0: 408, +1: 195, +2: 91, +3: 43, +4: 30, +5: 26

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.01 | 0.01 | 0.564 | 15.84 |
| scvi_k30_btissue | 0.01 | 0.01 | 0.564 | 15.84 |
| pca_k256 | -0.18 | 0.01 | 0.532 | 7.03 |
| nystroem_k256_g0.5 | -0.19 | 0.01 | 0.530 | 9.08 |
| scvi_k10_btissue | -0.21 | 0.01 | 0.526 | 24.50 |
| pca_k128 | -0.23 | 0.01 | 0.524 | 6.52 |
| nystroem_k64_g0.5 | -0.27 | 0.01 | 0.516 | 7.11 |
| pca_k64 | -0.28 | 0.01 | 0.515 | 5.88 |
| ica_k64 | -0.28 | 0.01 | 0.515 | 5.89 |
| nmf_k64 | -0.29 | 0.01 | 0.514 | 7.69 |
| nystroem_k256_g2 | -0.29 | 0.01 | 0.512 | 9.64 |
| pca_k32 | -0.33 | 0.01 | 0.505 | 6.10 |
| nystroem_k64_g2 | -0.44 | 0.01 | 0.487 | 10.64 |
| nmf_k16 | -0.58 | 0.01 | 0.463 | 11.52 |
| pca_k16 | -0.61 | 0.01 | 0.458 | 12.87 |
| ica_k16 | -0.61 | 0.01 | 0.458 | 12.87 |
| gmm_k100 | -0.71 | 0.01 | 0.441 | 16.97 |
| rproj_k128_s1 | -0.73 | 0.01 | 0.437 | 5.13 |
| rproj_k128_s0 | -0.77 | 0.01 | 0.431 | 8.79 |
| gmm_k30 | -0.95 | 0.01 | 0.401 | 18.81 |
| pca_k8 | -0.96 | 0.01 | 0.398 | 17.38 |
| gmm_k10 | -1.23 | 0.01 | 0.353 | 25.22 |
| pca_k4 | -1.33 | 0.01 | 0.338 | 21.02 |
| rproj_k32_s1 | -1.57 | 0.01 | 0.300 | 13.72 |
| rproj_k32_s0 | -1.59 | 0.01 | 0.297 | 15.42 |
| rproj_k8_s0 | -2.20 | 0.01 | 0.211 | 32.96 |
| rproj_k8_s1 | -2.26 | 0.01 | 0.202 | 32.00 |
| depth2 | -2.27 | 0.01 | 0.201 | 102.92 |
| random_k32_s1 | -2.63 | 0.01 | 0.158 | 94.60 |
| random_k32_s0 | -2.63 | 0.01 | 0.158 | 94.60 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.160 | 1.9e-12 | 1905 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000178|B cell|SRX28608227 | 7.00 | 0.82 | 0.00 |
| UBERON:0000178|B cell|SRX22540099 | 7.00 | 0.82 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX10335843 | 6.82 | 0.82 | 0.00 |
| UBERON:0000178|erythrocyte|SRX16061177 | 6.63 | 0.82 | 0.00 |
| UBERON:0000178|B cell|SRX26317347 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX19447590 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|B cell|SRX15699285 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|plasma cell|SRX9768483 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|B cell|SRX10151476 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX15498675 | 6.48 | 0.64 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX10335837 | 6.33 | 0.83 | 0.00 |
| UBERON:0000178|B cell|SRX12708382 | 6.14 | 0.54 | 0.00 |
| UBERON:0000178|hematopoietic precursor cell|SRX9711331 | 5.88 | 0.48 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX9711331 | 5.88 | 0.48 | 0.00 |
| UBERON:0000178|B cell|SRX28608223 | 5.88 | 0.48 | 0.00 |

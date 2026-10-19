# Component A summary: repr_scbasecount_human200_blood


## cell_level

- items: 46625; informative (non-degenerate): 41284; nobody passes: 5339; everybody passes: 2
- difficulty percentiles 5/25/50/75/95: [-2.96, -1.93, -0.82, 0.94, 2.85]; median SE 0.47
- histogram (bin lower edge: count): -6: 0, -5: 17, -4: 1319, -3: 8837, -2: 8243, -1: 7231, +0: 6123, +1: 5598, +2: 3916, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.53 | 0.01 | 0.598 | 0.86 |
| scvi_k30_btissue | 0.53 | 0.01 | 0.598 | 0.86 |
| nystroem_k256_g0.5 | 0.21 | 0.01 | 0.557 | 0.48 |
| scvi_k10_btissue | 0.19 | 0.01 | 0.555 | 0.81 |
| pca_k256 | 0.18 | 0.01 | 0.554 | 0.42 |
| pca_k128 | 0.14 | 0.01 | 0.549 | 0.37 |
| nystroem_k64_g0.5 | 0.13 | 0.01 | 0.547 | 0.38 |
| pca_k64 | 0.11 | 0.01 | 0.545 | 0.33 |
| ica_k64 | 0.11 | 0.01 | 0.545 | 0.34 |
| nystroem_k256_g2 | 0.07 | 0.01 | 0.540 | 0.57 |
| pca_k32 | -0.01 | 0.01 | 0.529 | 0.38 |
| nystroem_k64_g2 | -0.02 | 0.01 | 0.528 | 0.65 |
| nmf_k64 | -0.02 | 0.01 | 0.528 | 0.66 |
| ica_k16 | -0.20 | 0.01 | 0.505 | 0.43 |
| pca_k16 | -0.20 | 0.01 | 0.505 | 0.43 |
| nmf_k16 | -0.26 | 0.01 | 0.496 | 0.71 |
| gmm_k100 | -0.58 | 0.01 | 0.453 | 0.91 |
| rproj_k128_s0 | -0.59 | 0.01 | 0.451 | 1.06 |
| rproj_k128_s1 | -0.66 | 0.01 | 0.441 | 0.92 |
| pca_k8 | -0.82 | 0.01 | 0.420 | 1.01 |
| gmm_k30 | -0.83 | 0.01 | 0.418 | 0.90 |
| gmm_k10 | -1.42 | 0.01 | 0.336 | 1.15 |
| rproj_k32_s1 | -1.61 | 0.01 | 0.310 | 1.27 |
| rproj_k32_s0 | -1.68 | 0.01 | 0.301 | 1.40 |
| pca_k4 | -1.75 | 0.01 | 0.292 | 1.41 |
| rproj_k8_s1 | -2.46 | 0.01 | 0.202 | 2.23 |
| rproj_k8_s0 | -2.49 | 0.01 | 0.199 | 1.99 |
| depth2 | -2.62 | 0.01 | 0.183 | 6.50 |
| random_k32_s0 | -2.89 | 0.01 | 0.155 | 3.26 |
| random_k32_s1 | -2.90 | 0.01 | 0.155 | 3.26 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.174 | 5.0e-279 | 41284 |
| log_total_counts | -0.228 | 0.0e+00 | 41284 |
| n_genes_by_counts | -0.198 | 0.0e+00 | 41284 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| hematopoietic precursor cell | 42.0 | 2.27 | 764 |
| mature NK T cell | 251.0 | 1.99 | 1113 |
| CD8-positive, alpha-beta T cell | 4304.0 | 0.77 | 17817 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 4476.0 | 0.60 | 14419 |
| macrophage | 2267.0 | 0.57 | 6863 |
| natural killer cell | 6501.0 | 0.19 | 18452 |
| non-classical monocyte | 979.0 | 0.11 | 1642 |
| CD4-positive, alpha-beta T cell | 7217.0 | -0.72 | 21724 |
| neutrophil | 1359.0 | -1.35 | 2952 |
| platelet | 1955.0 | -1.40 | 4929 |
| plasma cell | 2117.0 | -1.48 | 3265 |
| B cell | 5128.0 | -1.76 | 16576 |
| erythrocyte | 708.0 | -2.23 | 4135 |
| classical monocyte | 3980.0 | -2.24 | 13800 |

## stratum_binomial

- items: 578; informative (non-degenerate): 565; nobody passes: 13; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.43, -1.48, -0.31, 0.84, 3.43]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 2, -3: 80, -2: 114, -1: 118, +0: 127, +1: 60, +2: 25, +3: 21, +4: 13, +5: 3

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.21 | 0.01 | 0.598 | 20.41 |
| scvi_k30_btissue | 0.21 | 0.01 | 0.598 | 20.41 |
| nystroem_k256_g0.5 | -0.03 | 0.01 | 0.557 | 7.28 |
| scvi_k10_btissue | -0.04 | 0.01 | 0.555 | 14.03 |
| pca_k256 | -0.05 | 0.01 | 0.554 | 4.93 |
| pca_k128 | -0.08 | 0.01 | 0.549 | 4.92 |
| nystroem_k64_g0.5 | -0.09 | 0.01 | 0.547 | 5.79 |
| pca_k64 | -0.10 | 0.01 | 0.545 | 4.88 |
| ica_k64 | -0.10 | 0.01 | 0.545 | 4.88 |
| nystroem_k256_g2 | -0.13 | 0.01 | 0.540 | 8.39 |
| pca_k32 | -0.20 | 0.01 | 0.529 | 7.16 |
| nystroem_k64_g2 | -0.20 | 0.01 | 0.528 | 17.24 |
| nmf_k64 | -0.21 | 0.01 | 0.528 | 9.38 |
| ica_k16 | -0.34 | 0.01 | 0.505 | 8.06 |
| pca_k16 | -0.34 | 0.01 | 0.505 | 8.06 |
| nmf_k16 | -0.39 | 0.01 | 0.496 | 12.63 |
| gmm_k100 | -0.64 | 0.01 | 0.453 | 16.39 |
| rproj_k128_s0 | -0.65 | 0.01 | 0.451 | 16.42 |
| rproj_k128_s1 | -0.71 | 0.01 | 0.441 | 6.03 |
| pca_k8 | -0.84 | 0.01 | 0.420 | 27.98 |
| gmm_k30 | -0.84 | 0.01 | 0.418 | 20.76 |
| gmm_k10 | -1.33 | 0.01 | 0.336 | 27.42 |
| rproj_k32_s1 | -1.50 | 0.01 | 0.310 | 8.82 |
| rproj_k32_s0 | -1.56 | 0.01 | 0.301 | 13.05 |
| pca_k4 | -1.61 | 0.01 | 0.292 | 31.93 |
| rproj_k8_s1 | -2.25 | 0.01 | 0.202 | 27.43 |
| rproj_k8_s0 | -2.27 | 0.01 | 0.199 | 27.00 |
| depth2 | -2.39 | 0.01 | 0.183 | 132.04 |
| random_k32_s0 | -2.64 | 0.01 | 0.155 | 114.37 |
| random_k32_s1 | -2.65 | 0.01 | 0.155 | 114.43 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.036 | 3.9e-01 | 565 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000178|plasma cell|SRX9768483 | 7.13 | 0.81 | 0.00 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX10335837 | 6.21 | 0.83 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX9756239 | 5.92 | 0.64 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX13061529 | 5.65 | 0.64 | 0.00 |
| UBERON:0000178|hematopoietic precursor cell|SRX9756239 | 5.19 | 0.54 | 0.00 |
| UBERON:0000178|hematopoietic precursor cell|SRX13061342 | 4.61 | 0.48 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX10977998 | 4.53 | 0.48 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX9756245 | 4.53 | 0.48 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX12219249 | 4.43 | 0.48 | 0.01 |
| UBERON:0000178|hematopoietic precursor cell|SRX10335837 | 4.40 | 0.33 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX10519950 | 4.36 | 0.44 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX11515844 | 4.27 | 0.44 | 0.01 |
| UBERON:0000178|hematopoietic precursor cell|SRX10124641 | 4.22 | 0.44 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX10977988 | 4.22 | 0.44 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX16311443 | 4.14 | 0.24 | 0.01 |

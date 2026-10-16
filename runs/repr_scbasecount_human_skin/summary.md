# Component A summary: repr_scbasecount_human_skin


## cell_level

- items: 20009; informative (non-degenerate): 17726; nobody passes: 2278; everybody passes: 5
- difficulty percentiles 5/25/50/75/95: [-2.96, -2.3, -0.95, 1.16, 3.05]; median SE 0.51
- histogram (bin lower edge: count): -6: 0, -5: 21, -4: 760, -3: 5160, -2: 2666, -1: 2308, +0: 2371, +1: 2606, +2: 832, +3: 1002, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.48 | 0.02 | 0.586 | 0.41 |
| nystroem_k64_g0.5 | 0.45 | 0.02 | 0.582 | 0.33 |
| nystroem_k256_g2 | 0.43 | 0.02 | 0.580 | 0.45 |
| pca_k64 | 0.41 | 0.02 | 0.577 | 0.33 |
| ica_k64 | 0.40 | 0.02 | 0.576 | 0.33 |
| pca_k128 | 0.39 | 0.02 | 0.575 | 0.38 |
| pca_k256 | 0.35 | 0.02 | 0.571 | 0.45 |
| pca_k32 | 0.33 | 0.02 | 0.569 | 0.34 |
| scvi_k30_bnone | 0.31 | 0.02 | 0.566 | 0.65 |
| scvi_k30_btissue | 0.31 | 0.02 | 0.566 | 0.65 |
| nystroem_k64_g2 | 0.24 | 0.02 | 0.558 | 0.46 |
| pca_k16 | 0.18 | 0.02 | 0.551 | 0.37 |
| ica_k16 | 0.18 | 0.02 | 0.550 | 0.37 |
| nmf_k64 | 0.16 | 0.02 | 0.548 | 0.62 |
| scvi_k10_btissue | -0.02 | 0.02 | 0.527 | 0.87 |
| gmm_k100 | -0.04 | 0.02 | 0.525 | 0.75 |
| nmf_k16 | -0.18 | 0.02 | 0.509 | 0.78 |
| pca_k8 | -0.23 | 0.02 | 0.503 | 0.60 |
| gmm_k30 | -0.31 | 0.02 | 0.493 | 0.88 |
| rproj_k128_s1 | -0.38 | 0.02 | 0.484 | 0.87 |
| rproj_k128_s0 | -0.40 | 0.02 | 0.482 | 0.89 |
| pca_k4 | -0.92 | 0.02 | 0.416 | 1.11 |
| gmm_k10 | -1.15 | 0.02 | 0.386 | 1.15 |
| rproj_k32_s0 | -1.48 | 0.02 | 0.344 | 1.51 |
| rproj_k32_s1 | -1.55 | 0.02 | 0.335 | 1.59 |
| rproj_k8_s0 | -2.47 | 0.02 | 0.219 | 2.79 |
| rproj_k8_s1 | -2.69 | 0.02 | 0.194 | 4.21 |
| depth2 | -2.73 | 0.02 | 0.189 | 5.92 |
| random_k32_s0 | -3.67 | 0.03 | 0.101 | 12.27 |
| random_k32_s1 | -3.70 | 0.03 | 0.099 | 12.36 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.050 | 2.7e-11 | 17726 |
| log_total_counts | -0.351 | 0.0e+00 | 17726 |
| n_genes_by_counts | -0.354 | 0.0e+00 | 17726 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| classical monocyte | 46.0 | 1.96 | 160 |
| regulatory T cell | 34.0 | 1.80 | 177 |
| CD4-positive, alpha-beta T cell | 979.0 | 0.99 | 3569 |
| neutrophil | 1036.0 | 0.86 | 3541 |
| mature NK T cell | 21.0 | 0.67 | 252 |
| CD8-positive, alpha-beta T cell | 1981.0 | 0.38 | 6197 |
| T cell | 1964.0 | 0.22 | 5716 |
| melanocyte | 1764.0 | 0.02 | 3674 |
| plasma cell | 259.0 | -0.33 | 313 |
| sebocyte | 1591.0 | -0.44 | 3239 |
| smooth muscle cell | 1880.0 | -0.70 | 3882 |
| macrophage | 1595.0 | -1.73 | 3515 |
| endothelial cell | 1991.0 | -1.82 | 4467 |
| fibroblast | 1950.0 | -1.97 | 4212 |
| mast cell | 614.0 | -2.00 | 860 |

## stratum_binomial

- items: 242; informative (non-degenerate): 240; nobody passes: 2; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.93, -1.09, -0.18, 0.81, 2.32]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 9, -2: 57, -1: 64, +0: 65, +1: 28, +2: 10, +3: 4, +4: 1, +5: 2

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.28 | 0.02 | 0.586 | 3.11 |
| nystroem_k64_g0.5 | 0.26 | 0.02 | 0.582 | 3.02 |
| nystroem_k256_g2 | 0.24 | 0.02 | 0.580 | 3.40 |
| pca_k64 | 0.23 | 0.02 | 0.577 | 2.76 |
| ica_k64 | 0.23 | 0.02 | 0.576 | 2.74 |
| pca_k128 | 0.22 | 0.02 | 0.575 | 2.66 |
| pca_k256 | 0.20 | 0.02 | 0.571 | 2.67 |
| pca_k32 | 0.19 | 0.02 | 0.569 | 2.78 |
| scvi_k30_bnone | 0.17 | 0.02 | 0.566 | 5.84 |
| scvi_k30_btissue | 0.17 | 0.02 | 0.566 | 5.84 |
| nystroem_k64_g2 | 0.13 | 0.02 | 0.558 | 3.28 |
| pca_k16 | 0.09 | 0.02 | 0.551 | 2.86 |
| ica_k16 | 0.09 | 0.02 | 0.550 | 2.89 |
| nmf_k64 | 0.07 | 0.02 | 0.548 | 4.24 |
| scvi_k10_btissue | -0.04 | 0.02 | 0.527 | 10.34 |
| gmm_k100 | -0.05 | 0.02 | 0.525 | 6.83 |
| nmf_k16 | -0.14 | 0.02 | 0.509 | 6.18 |
| pca_k8 | -0.17 | 0.02 | 0.503 | 6.34 |
| gmm_k30 | -0.22 | 0.02 | 0.493 | 12.85 |
| rproj_k128_s1 | -0.27 | 0.02 | 0.484 | 2.00 |
| rproj_k128_s0 | -0.28 | 0.02 | 0.482 | 2.28 |
| pca_k4 | -0.63 | 0.02 | 0.416 | 13.87 |
| gmm_k10 | -0.79 | 0.02 | 0.386 | 26.48 |
| rproj_k32_s0 | -1.02 | 0.02 | 0.344 | 5.15 |
| rproj_k32_s1 | -1.07 | 0.02 | 0.335 | 5.03 |
| rproj_k8_s0 | -1.79 | 0.02 | 0.219 | 13.87 |
| rproj_k8_s1 | -1.97 | 0.02 | 0.194 | 18.93 |
| depth2 | -2.01 | 0.02 | 0.189 | 64.70 |
| random_k32_s0 | -2.83 | 0.02 | 0.101 | 155.82 |
| random_k32_s1 | -2.86 | 0.02 | 0.099 | 165.94 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.099 | 1.3e-01 | 240 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002097|B cell|SRX10104846 | 5.94 | 0.64 | 0.00 |
| UBERON:0002097|naive thymus-derived CD4-positive, alpha-beta T cell|SRX10104846 | 5.83 | 0.37 | 0.00 |
| UBERON:0002097|natural killer cell|SRX10104846 | 4.17 | 0.16 | 0.01 |
| UBERON:0002097|regulatory T cell|SRX7974889 | 3.79 | 0.24 | 0.02 |
| UBERON:0002097|regulatory T cell|SRX20868583 | 3.74 | 0.29 | 0.02 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX27532049 | 3.16 | 0.10 | 0.03 |
| UBERON:0002097|melanocyte|ERX12445729 | 3.07 | 0.18 | 0.04 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX9673536 | 2.96 | 0.10 | 0.04 |
| UBERON:0002097|plasma cell|SRX10104846 | 2.53 | 0.12 | 0.06 |
| UBERON:0002097|classical monocyte|SRX10104846 | 2.51 | 0.08 | 0.06 |
| UBERON:0002097|melanocyte|SRX19961073 | 2.48 | 0.09 | 0.06 |
| UBERON:0002097|neutrophil|SRX28908423 | 2.40 | 0.07 | 0.07 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX26083196 | 2.32 | 0.07 | 0.07 |
| UBERON:0002097|regulatory T cell|SRX18267533 | 2.29 | 0.10 | 0.08 |
| UBERON:0002097|neutrophil|SRX9673536 | 2.27 | 0.12 | 0.08 |

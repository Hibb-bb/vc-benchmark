# Component A summary: repr_scbasecount_humanall_breast


## cell_level

- items: 10461; informative (non-degenerate): 10077; nobody passes: 374; everybody passes: 10
- difficulty percentiles 5/25/50/75/95: [-2.32, -1.77, -0.86, 0.86, 3.98]; median SE 0.63
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 104, -3: 1576, -2: 2745, -1: 2003, +0: 1318, +1: 784, +2: 481, +3: 586, +4: 480, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 2.62 | 0.04 | 0.817 | 0.25 |
| nystroem_k64_g0.5 | 2.61 | 0.04 | 0.817 | 0.19 |
| nystroem_k256_g2 | 2.59 | 0.04 | 0.816 | 0.27 |
| pca_k128 | 2.59 | 0.04 | 0.815 | 0.25 |
| ica_k64 | 2.58 | 0.04 | 0.815 | 0.20 |
| pca_k64 | 2.58 | 0.04 | 0.815 | 0.20 |
| pca_k32 | 2.48 | 0.04 | 0.808 | 0.24 |
| nystroem_k64_g2 | 2.47 | 0.04 | 0.808 | 0.37 |
| pca_k256 | 2.46 | 0.04 | 0.807 | 0.35 |
| nmf_k64 | 2.40 | 0.04 | 0.803 | 0.37 |
| scvi_k30_bnone | 2.25 | 0.04 | 0.792 | 0.59 |
| scvi_k30_btissue | 2.25 | 0.04 | 0.792 | 0.59 |
| pca_k16 | 2.13 | 0.04 | 0.783 | 0.32 |
| ica_k16 | 2.11 | 0.04 | 0.782 | 0.31 |
| gmm_k30 | 1.96 | 0.03 | 0.769 | 0.54 |
| scvi_k10_btissue | 1.84 | 0.03 | 0.760 | 0.83 |
| gmm_k100 | 1.81 | 0.03 | 0.757 | 0.68 |
| rproj_k128_s0 | 1.67 | 0.03 | 0.745 | 0.92 |
| rproj_k128_s1 | 1.65 | 0.03 | 0.744 | 0.76 |
| nmf_k16 | 1.56 | 0.03 | 0.735 | 0.67 |
| pca_k8 | 1.12 | 0.03 | 0.692 | 0.63 |
| pca_k4 | 0.62 | 0.03 | 0.637 | 0.82 |
| gmm_k10 | 0.58 | 0.03 | 0.632 | 1.25 |
| rproj_k32_s1 | 0.02 | 0.03 | 0.559 | 1.79 |
| rproj_k32_s0 | -0.10 | 0.03 | 0.541 | 2.29 |
| rproj_k8_s1 | -1.53 | 0.03 | 0.324 | 6.19 |
| rproj_k8_s0 | -1.91 | 0.03 | 0.268 | 8.34 |
| depth2 | -2.36 | 0.03 | 0.207 | 11.71 |
| random_k32_s1 | -3.12 | 0.03 | 0.124 | 18.12 |
| random_k32_s0 | -3.12 | 0.03 | 0.124 | 20.41 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.337 | 1.3e-265 | 10077 |
| log_total_counts | -0.334 | 7.8e-261 | 10077 |
| n_genes_by_counts | -0.380 | 0.0e+00 | 10077 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| CD4-positive, alpha-beta T cell | 900.0 | 1.34 | 1603 |
| plasma cell | 543.0 | 0.46 | 244 |
| macrophage | 1204.0 | 0.41 | 3014 |
| basal cell | 1127.0 | -0.04 | 2310 |
| CD8-positive, alpha-beta T cell | 1338.0 | -0.09 | 3188 |
| endothelial cell | 1318.0 | -0.39 | 3426 |
| vascular associated smooth muscle cell | 1124.0 | -0.55 | 1440 |
| luminal epithelial cell of mammary gland | 1285.0 | -0.98 | 3414 |
| fibroblast of breast | 1232.0 | -1.44 | 3418 |

## stratum_binomial

- items: 120; informative (non-degenerate): 120; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.79, -0.85, -0.39, 0.44, 1.67]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 3, -2: 20, -1: 49, +0: 34, +1: 9, +2: 2, +3: 0, +4: 0, +5: 2

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 1.46 | 0.03 | 0.817 | 3.39 |
| nystroem_k64_g0.5 | 1.46 | 0.03 | 0.817 | 3.05 |
| nystroem_k256_g2 | 1.45 | 0.03 | 0.816 | 3.59 |
| pca_k128 | 1.45 | 0.03 | 0.815 | 3.28 |
| ica_k64 | 1.44 | 0.03 | 0.815 | 3.14 |
| pca_k64 | 1.44 | 0.03 | 0.815 | 3.15 |
| pca_k32 | 1.39 | 0.03 | 0.808 | 3.21 |
| nystroem_k64_g2 | 1.39 | 0.03 | 0.808 | 6.26 |
| pca_k256 | 1.38 | 0.03 | 0.807 | 2.51 |
| nmf_k64 | 1.35 | 0.03 | 0.803 | 2.95 |
| scvi_k30_bnone | 1.26 | 0.03 | 0.792 | 5.11 |
| scvi_k30_btissue | 1.26 | 0.03 | 0.792 | 5.11 |
| pca_k16 | 1.20 | 0.03 | 0.783 | 3.18 |
| ica_k16 | 1.19 | 0.03 | 0.782 | 3.15 |
| gmm_k30 | 1.11 | 0.03 | 0.769 | 6.62 |
| scvi_k10_btissue | 1.04 | 0.03 | 0.760 | 8.39 |
| gmm_k100 | 1.02 | 0.03 | 0.757 | 6.00 |
| rproj_k128_s0 | 0.94 | 0.02 | 0.745 | 3.36 |
| rproj_k128_s1 | 0.94 | 0.02 | 0.744 | 2.77 |
| nmf_k16 | 0.89 | 0.02 | 0.735 | 7.18 |
| pca_k8 | 0.63 | 0.02 | 0.692 | 18.47 |
| pca_k4 | 0.33 | 0.02 | 0.637 | 20.49 |
| gmm_k10 | 0.30 | 0.02 | 0.632 | 31.55 |
| rproj_k32_s1 | -0.06 | 0.02 | 0.559 | 7.57 |
| rproj_k32_s0 | -0.15 | 0.02 | 0.541 | 14.98 |
| rproj_k8_s1 | -1.22 | 0.02 | 0.324 | 20.78 |
| rproj_k8_s0 | -1.53 | 0.02 | 0.268 | 40.30 |
| depth2 | -1.91 | 0.03 | 0.207 | 41.90 |
| random_k32_s1 | -2.59 | 0.03 | 0.124 | 21.57 |
| random_k32_s0 | -2.59 | 0.03 | 0.124 | 23.14 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.427 | 1.2e-06 | 120 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000310|plasma cell|SRX10867705 | 7.41 | 0.63 | 0.00 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX10867705 | 5.94 | 0.40 | 0.01 |
| UBERON:0000310|mast cell|SRX28122265 | 5.53 | 0.37 | 0.01 |
| UBERON:0000310|macrophage|SRX10867705 | 2.97 | 0.06 | 0.11 |
| UBERON:0000310|endothelial cell|SRX10867705 | 2.01 | 0.04 | 0.24 |
| UBERON:0000310|plasma cell|SRX9856813 | 1.87 | 0.10 | 0.27 |
| UBERON:0000310|macrophage|ERX11900695 | 1.66 | 0.04 | 0.30 |
| UBERON:0000310|macrophage|SRX20733009 | 1.65 | 0.07 | 0.31 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX28122273 | 1.35 | 0.04 | 0.37 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX20732918 | 1.29 | 0.04 | 0.38 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX20732884 | 1.21 | 0.05 | 0.39 |
| UBERON:0000310|macrophage|SRX24993349 | 1.18 | 0.06 | 0.40 |
| UBERON:0000310|basal cell|SRX10867705 | 1.17 | 0.04 | 0.40 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX9856813 | 1.15 | 0.04 | 0.41 |
| UBERON:0000310|CD4-positive, alpha-beta T cell|SRX20732914 | 0.89 | 0.04 | 0.46 |

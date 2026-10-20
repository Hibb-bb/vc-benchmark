# Component A summary: repr_scbasecount_humanall_cornea


## cell_level

- items: 10528; informative (non-degenerate): 9151; nobody passes: 1070; everybody passes: 307
- difficulty percentiles 5/25/50/75/95: [-3.29, -2.48, -1.38, 0.25, 4.26]; median SE 0.67
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 976, -3: 1358, -2: 2716, -1: 1696, +0: 378, +1: 370, +2: 368, +3: 598, +4: 691, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 2.47 | 0.04 | 0.756 | 0.54 |
| scvi_k30_btissue | 2.47 | 0.04 | 0.756 | 0.54 |
| nystroem_k64_g0.5 | 2.35 | 0.04 | 0.749 | 0.19 |
| scvi_k10_btissue | 2.33 | 0.04 | 0.748 | 0.49 |
| pca_k32 | 2.29 | 0.04 | 0.746 | 0.18 |
| nystroem_k256_g0.5 | 2.26 | 0.04 | 0.744 | 0.41 |
| pca_k128 | 2.24 | 0.04 | 0.743 | 0.22 |
| pca_k64 | 2.23 | 0.04 | 0.743 | 0.16 |
| ica_k64 | 2.23 | 0.04 | 0.743 | 0.16 |
| pca_k16 | 2.21 | 0.04 | 0.742 | 0.15 |
| pca_k256 | 2.20 | 0.04 | 0.741 | 0.43 |
| ica_k16 | 2.20 | 0.04 | 0.741 | 0.15 |
| nystroem_k256_g2 | 2.11 | 0.04 | 0.737 | 0.57 |
| nmf_k64 | 2.08 | 0.04 | 0.735 | 0.36 |
| nmf_k16 | 1.80 | 0.04 | 0.720 | 0.21 |
| nystroem_k64_g2 | 1.76 | 0.04 | 0.717 | 0.58 |
| pca_k8 | 1.73 | 0.04 | 0.716 | 0.14 |
| rproj_k128_s0 | 1.62 | 0.04 | 0.709 | 0.58 |
| rproj_k128_s1 | 1.51 | 0.04 | 0.702 | 0.61 |
| pca_k4 | 1.49 | 0.04 | 0.701 | 0.33 |
| gmm_k100 | 1.27 | 0.04 | 0.687 | 0.33 |
| gmm_k30 | 0.94 | 0.04 | 0.664 | 0.48 |
| gmm_k10 | 0.70 | 0.03 | 0.645 | 0.61 |
| rproj_k32_s1 | 0.54 | 0.03 | 0.633 | 0.81 |
| rproj_k32_s0 | 0.52 | 0.03 | 0.631 | 0.97 |
| rproj_k8_s1 | -0.69 | 0.03 | 0.504 | 1.95 |
| rproj_k8_s0 | -1.05 | 0.03 | 0.458 | 2.74 |
| depth2 | -1.97 | 0.03 | 0.329 | 24.70 |
| random_k32_s1 | -2.56 | 0.03 | 0.250 | 9.88 |
| random_k32_s0 | -2.57 | 0.03 | 0.248 | 9.55 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.609 | 0.0e+00 | 9151 |
| log_total_counts | -0.273 | 2.9e-156 | 9151 |
| n_genes_by_counts | -0.295 | 4.5e-183 | 9151 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| erythrocyte | 539.0 | 3.94 | 484 |
| plasma cell | 672.0 | 3.29 | 420 |
| corneal epithelial cell | 2537.0 | -0.63 | 9942 |
| conjunctival epithelial cell | 2652.0 | -1.03 | 11016 |
| microglial cell | 404.0 | -1.31 | 1265 |
| fibroblast | 2347.0 | -1.97 | 11311 |

## stratum_binomial

- items: 143; informative (non-degenerate): 143; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.92, -1.81, -1.23, 2.35, 4.6]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 5, -3: 21, -2: 57, -1: 11, +0: 0, +1: 7, +2: 17, +3: 7, +4: 17, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 0.90 | 0.03 | 0.756 | 3.62 |
| scvi_k30_btissue | 0.90 | 0.03 | 0.756 | 3.62 |
| nystroem_k64_g0.5 | 0.82 | 0.03 | 0.749 | 1.75 |
| scvi_k10_btissue | 0.81 | 0.03 | 0.748 | 3.23 |
| pca_k32 | 0.78 | 0.03 | 0.746 | 2.10 |
| nystroem_k256_g0.5 | 0.76 | 0.03 | 0.744 | 2.32 |
| pca_k128 | 0.75 | 0.03 | 0.743 | 1.58 |
| pca_k64 | 0.75 | 0.03 | 0.743 | 1.47 |
| ica_k64 | 0.75 | 0.03 | 0.743 | 1.42 |
| pca_k16 | 0.73 | 0.03 | 0.742 | 1.57 |
| pca_k256 | 0.72 | 0.03 | 0.741 | 2.54 |
| ica_k16 | 0.72 | 0.03 | 0.741 | 1.53 |
| nystroem_k256_g2 | 0.67 | 0.03 | 0.737 | 2.05 |
| nmf_k64 | 0.65 | 0.03 | 0.735 | 1.51 |
| nmf_k16 | 0.48 | 0.03 | 0.720 | 2.45 |
| nystroem_k64_g2 | 0.46 | 0.03 | 0.717 | 2.29 |
| pca_k8 | 0.44 | 0.03 | 0.716 | 3.04 |
| rproj_k128_s0 | 0.38 | 0.03 | 0.709 | 2.66 |
| rproj_k128_s1 | 0.31 | 0.03 | 0.702 | 2.51 |
| pca_k4 | 0.30 | 0.03 | 0.701 | 4.39 |
| gmm_k100 | 0.17 | 0.03 | 0.687 | 3.82 |
| gmm_k30 | -0.03 | 0.03 | 0.664 | 7.28 |
| gmm_k10 | -0.18 | 0.03 | 0.645 | 7.80 |
| rproj_k32_s1 | -0.28 | 0.03 | 0.633 | 2.50 |
| rproj_k32_s0 | -0.29 | 0.03 | 0.631 | 2.94 |
| rproj_k8_s1 | -1.11 | 0.02 | 0.504 | 2.97 |
| rproj_k8_s0 | -1.37 | 0.02 | 0.458 | 3.80 |
| depth2 | -2.09 | 0.02 | 0.329 | 223.46 |
| random_k32_s1 | -2.57 | 0.02 | 0.250 | 12.55 |
| random_k32_s0 | -2.58 | 0.02 | 0.248 | 13.26 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.770 | 2.6e-29 | 143 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000964|erythrocyte|SRX14335965 | 5.97 | 0.64 | 0.00 |
| UBERON:0000964|erythrocyte|SRX14335976 | 5.00 | 0.35 | 0.01 |
| UBERON:0000964|plasma cell|SRX14335994 | 4.97 | 0.30 | 0.01 |
| UBERON:0000964|plasma cell|SRX11077088 | 4.88 | 0.33 | 0.01 |
| UBERON:0000964|erythrocyte|SRX14335962 | 4.84 | 0.35 | 0.01 |
| UBERON:0000964|erythrocyte|SRX14336007 | 4.71 | 0.35 | 0.01 |
| UBERON:0000964|erythrocyte|SRX14335966 | 4.66 | 0.35 | 0.01 |
| UBERON:0000964|plasma cell|SRX14335980 | 4.61 | 0.27 | 0.01 |
| UBERON:0000964|erythrocyte|SRX14336012 | 4.52 | 0.29 | 0.02 |
| UBERON:0000964|plasma cell|SRX14336003 | 4.52 | 0.28 | 0.02 |
| UBERON:0000964|erythrocyte|SRX14335968 | 4.44 | 0.29 | 0.02 |
| UBERON:0000964|erythrocyte|SRX14336023 | 4.33 | 0.24 | 0.02 |
| UBERON:0000964|plasma cell|SRX14336005 | 4.32 | 0.28 | 0.02 |
| UBERON:0000964|erythrocyte|SRX14335978 | 4.28 | 0.23 | 0.02 |
| UBERON:0000964|plasma cell|SRX14335983 | 4.26 | 0.26 | 0.02 |

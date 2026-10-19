# Component A summary: repr_scbasecount_human200_multitissue


## cell_level

- items: 79157; informative (non-degenerate): 53648; nobody passes: 25391; everybody passes: 118
- difficulty percentiles 5/25/50/75/95: [-4.56, -3.18, -1.77, 0.14, 1.58]; median SE 0.48
- histogram (bin lower edge: count): -6: 464, -5: 4741, -4: 8355, -3: 10478, -2: 8302, -1: 7220, +0: 8440, +1: 5648, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | -1.15 | 0.01 | 0.386 | 0.34 |
| pca_k32 | -1.16 | 0.01 | 0.385 | 0.33 |
| ica_k64 | -1.17 | 0.01 | 0.384 | 0.31 |
| pca_k64 | -1.18 | 0.01 | 0.383 | 0.32 |
| pca_k128 | -1.18 | 0.01 | 0.383 | 0.38 |
| nystroem_k256_g2 | -1.21 | 0.01 | 0.381 | 0.48 |
| nmf_k64 | -1.21 | 0.01 | 0.381 | 0.53 |
| pca_k256 | -1.21 | 0.01 | 0.380 | 0.45 |
| scvi_k30_btissue | -1.21 | 0.01 | 0.380 | 0.59 |
| nystroem_k256_g0.5 | -1.24 | 0.01 | 0.377 | 0.45 |
| nystroem_k64_g2 | -1.25 | 0.01 | 0.376 | 0.44 |
| scvi_k10_btissue | -1.28 | 0.01 | 0.374 | 0.54 |
| scvi_k30_bnone | -1.31 | 0.01 | 0.370 | 0.55 |
| gmm_k100 | -1.43 | 0.01 | 0.358 | 0.77 |
| pca_k16 | -1.61 | 0.01 | 0.340 | 0.46 |
| ica_k16 | -1.61 | 0.01 | 0.340 | 0.46 |
| rproj_k128_s0 | -1.68 | 0.01 | 0.333 | 0.76 |
| rproj_k128_s1 | -1.70 | 0.01 | 0.332 | 0.82 |
| nmf_k16 | -1.88 | 0.01 | 0.314 | 0.82 |
| gmm_k30 | -1.93 | 0.01 | 0.309 | 0.61 |
| pca_k8 | -2.25 | 0.01 | 0.277 | 0.71 |
| rproj_k32_s1 | -2.65 | 0.01 | 0.238 | 1.18 |
| rproj_k32_s0 | -2.72 | 0.01 | 0.232 | 1.17 |
| pca_k4 | -2.76 | 0.01 | 0.228 | 0.99 |
| gmm_k10 | -2.85 | 0.01 | 0.219 | 1.25 |
| rproj_k8_s0 | -3.68 | 0.01 | 0.147 | 1.73 |
| rproj_k8_s1 | -3.75 | 0.01 | 0.142 | 1.53 |
| random_k32_s1 | -4.10 | 0.01 | 0.116 | 2.95 |
| random_k32_s0 | -4.10 | 0.01 | 0.116 | 2.97 |
| depth2 | -4.26 | 0.01 | 0.105 | 4.29 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.427 | 0.0e+00 | 53648 |
| log_total_counts | -0.176 | 0.0e+00 | 53648 |
| n_genes_by_counts | -0.151 | 5.8e-270 | 53648 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| monocyte | 273.0 | 1.11 | 1432 |
| regulatory T cell | 86.0 | 0.84 | 948 |
| T cell | 800.0 | 0.82 | 3168 |
| basal cell | 711.0 | 0.77 | 3969 |
| non-classical monocyte | 144.0 | 0.35 | 130 |
| smooth muscle cell | 838.0 | 0.20 | 2129 |
| fibroblast | 1875.0 | 0.05 | 7138 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 1272.0 | 0.01 | 1501 |
| natural killer cell | 3967.0 | -0.42 | 2077 |
| mature NK T cell | 1930.0 | -0.48 | 3542 |
| erythrocyte | 927.0 | -0.63 | 2723 |
| classical monocyte | 1365.0 | -0.82 | 1084 |
| CD4-positive, alpha-beta T cell | 8107.0 | -0.87 | 11642 |
| platelet | 60.0 | -1.00 | 44 |
| plasma cell | 2679.0 | -1.11 | 4280 |

## stratum_binomial

- items: 979; informative (non-degenerate): 918; nobody passes: 61; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.48, -2.0, -0.7, 1.04, 3.82]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 9, -4: 76, -3: 145, -2: 179, -1: 146, +0: 125, +1: 91, +2: 67, +3: 37, +4: 21, +5: 9

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | -1.24 | 0.01 | 0.386 | 6.33 |
| pca_k32 | -1.25 | 0.01 | 0.385 | 3.93 |
| ica_k64 | -1.26 | 0.01 | 0.384 | 5.72 |
| pca_k64 | -1.26 | 0.01 | 0.383 | 5.70 |
| pca_k128 | -1.26 | 0.01 | 0.383 | 6.34 |
| nystroem_k256_g2 | -1.28 | 0.01 | 0.381 | 7.92 |
| nmf_k64 | -1.28 | 0.01 | 0.381 | 6.85 |
| pca_k256 | -1.28 | 0.01 | 0.380 | 6.46 |
| scvi_k30_btissue | -1.29 | 0.01 | 0.380 | 7.13 |
| nystroem_k256_g0.5 | -1.31 | 0.01 | 0.377 | 7.23 |
| nystroem_k64_g2 | -1.32 | 0.01 | 0.376 | 7.57 |
| scvi_k10_btissue | -1.33 | 0.01 | 0.374 | 7.23 |
| scvi_k30_bnone | -1.36 | 0.01 | 0.370 | 6.10 |
| gmm_k100 | -1.45 | 0.01 | 0.358 | 15.13 |
| pca_k16 | -1.59 | 0.01 | 0.340 | 9.34 |
| ica_k16 | -1.59 | 0.01 | 0.340 | 9.31 |
| rproj_k128_s0 | -1.64 | 0.01 | 0.333 | 5.26 |
| rproj_k128_s1 | -1.65 | 0.01 | 0.332 | 6.97 |
| nmf_k16 | -1.79 | 0.01 | 0.314 | 16.17 |
| gmm_k30 | -1.83 | 0.01 | 0.309 | 25.62 |
| pca_k8 | -2.08 | 0.01 | 0.277 | 15.01 |
| rproj_k32_s1 | -2.40 | 0.01 | 0.238 | 7.73 |
| rproj_k32_s0 | -2.46 | 0.01 | 0.232 | 9.63 |
| pca_k4 | -2.49 | 0.01 | 0.228 | 25.73 |
| gmm_k10 | -2.56 | 0.01 | 0.219 | 43.68 |
| rproj_k8_s0 | -3.27 | 0.01 | 0.147 | 12.93 |
| rproj_k8_s1 | -3.33 | 0.01 | 0.142 | 11.19 |
| random_k32_s1 | -3.63 | 0.01 | 0.116 | 34.36 |
| random_k32_s0 | -3.63 | 0.01 | 0.116 | 34.33 |
| depth2 | -3.77 | 0.01 | 0.105 | 86.41 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.607 | 1.5e-93 | 918 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002107|monocyte|SRX10579818 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX27532049 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX10121858 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX19447641 | 6.00 | 0.83 | 0.00 |
| UBERON:0002371|monocyte|SRX15239507 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX13971399 | 6.00 | 0.83 | 0.00 |
| UBERON:0002107|monocyte|SRX13549269 | 6.00 | 0.83 | 0.00 |
| UBERON:0002107|monocyte|SRX10421418 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX20868586 | 6.00 | 0.83 | 0.00 |
| UBERON:0002371|CD4-positive, alpha-beta T cell|SRX19729088 | 6.00 | 0.83 | 0.00 |
| UBERON:0000178|natural killer cell|SRX14122101 | 6.00 | 0.83 | 0.00 |
| UBERON:0002107|monocyte|SRX9627325 | 6.00 | 0.83 | 0.00 |
| UBERON:0002107|monocyte|SRX8961823 | 6.00 | 0.83 | 0.00 |
| UBERON:0002097|neutrophil|SRX10121872 | 5.47 | 0.65 | 0.00 |
| UBERON:0002107|monocyte|SRX9172137 | 5.47 | 0.65 | 0.00 |

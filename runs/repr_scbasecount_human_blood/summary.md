# Component A summary: repr_scbasecount_human_blood


## cell_level

- items: 11088; informative (non-degenerate): 10032; nobody passes: 1056; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.52, -1.61, -0.25, 0.72, 1.73]; median SE 0.43
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 157, -3: 1339, -2: 2468, -1: 1712, +0: 2849, +1: 1032, +2: 475, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -0.15 | 0.02 | 0.497 | 0.81 |
| scvi_k30_btissue | -0.15 | 0.02 | 0.497 | 0.81 |
| scvi_k10_btissue | -0.29 | 0.02 | 0.475 | 0.83 |
| nystroem_k64_g0.5 | -0.41 | 0.02 | 0.455 | 0.49 |
| pca_k128 | -0.41 | 0.02 | 0.455 | 0.59 |
| nystroem_k256_g2 | -0.42 | 0.02 | 0.454 | 0.61 |
| ica_k64 | -0.43 | 0.02 | 0.453 | 0.45 |
| pca_k64 | -0.43 | 0.02 | 0.452 | 0.45 |
| nmf_k64 | -0.44 | 0.02 | 0.450 | 0.82 |
| pca_k32 | -0.45 | 0.02 | 0.449 | 0.46 |
| nystroem_k256_g0.5 | -0.58 | 0.02 | 0.428 | 0.55 |
| nystroem_k64_g2 | -0.61 | 0.02 | 0.423 | 0.66 |
| pca_k256 | -0.64 | 0.02 | 0.419 | 0.53 |
| gmm_k100 | -0.71 | 0.02 | 0.408 | 0.93 |
| pca_k16 | -0.74 | 0.02 | 0.403 | 0.42 |
| ica_k16 | -0.74 | 0.02 | 0.403 | 0.42 |
| nmf_k16 | -0.85 | 0.02 | 0.385 | 0.97 |
| gmm_k30 | -1.08 | 0.02 | 0.348 | 1.16 |
| pca_k8 | -1.09 | 0.02 | 0.348 | 0.73 |
| rproj_k128_s1 | -1.26 | 0.02 | 0.322 | 1.32 |
| rproj_k128_s0 | -1.31 | 0.02 | 0.315 | 1.12 |
| pca_k4 | -1.41 | 0.02 | 0.300 | 1.18 |
| gmm_k10 | -1.66 | 0.03 | 0.264 | 1.19 |
| rproj_k32_s1 | -1.73 | 0.03 | 0.254 | 1.79 |
| rproj_k32_s0 | -1.74 | 0.03 | 0.252 | 1.36 |
| rproj_k8_s0 | -2.04 | 0.03 | 0.213 | 1.67 |
| rproj_k8_s1 | -2.21 | 0.03 | 0.192 | 2.02 |
| random_k32_s0 | -2.29 | 0.03 | 0.182 | 2.17 |
| random_k32_s1 | -2.29 | 0.03 | 0.182 | 2.32 |
| depth2 | -2.31 | 0.03 | 0.181 | 2.40 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.109 | 9.0e-28 | 10032 |
| log_total_counts | -0.181 | 1.0e-74 | 10032 |
| n_genes_by_counts | -0.188 | 9.2e-81 | 10032 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| CD8-positive, alpha-beta T cell | 789.0 | 0.75 | 5801 |
| macrophage | 352.0 | 0.49 | 1136 |
| non-classical monocyte | 103.0 | 0.44 | 155 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 1588.0 | -0.17 | 5349 |
| natural killer cell | 1947.0 | -0.19 | 6347 |
| CD4-positive, alpha-beta T cell | 2060.0 | -0.42 | 7000 |
| plasma cell | 228.0 | -0.52 | 640 |
| erythrocyte | 51.0 | -0.84 | 880 |
| B cell | 2021.0 | -0.90 | 5389 |
| platelet | 255.0 | -1.16 | 622 |
| classical monocyte | 621.0 | -1.93 | 3130 |

## stratum_binomial

- items: 141; informative (non-degenerate): 140; nobody passes: 1; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.06, -0.82, -0.29, 0.72, 3.63]; median SE 0.04
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 9, -2: 18, -1: 53, +0: 31, +1: 9, +2: 4, +3: 11, +4: 5, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -0.30 | 0.02 | 0.497 | 17.60 |
| scvi_k30_btissue | -0.30 | 0.02 | 0.497 | 17.60 |
| scvi_k10_btissue | -0.41 | 0.02 | 0.475 | 17.79 |
| nystroem_k64_g0.5 | -0.51 | 0.02 | 0.455 | 11.73 |
| pca_k128 | -0.51 | 0.02 | 0.455 | 18.88 |
| nystroem_k256_g2 | -0.52 | 0.02 | 0.454 | 10.73 |
| ica_k64 | -0.52 | 0.02 | 0.453 | 10.88 |
| pca_k64 | -0.53 | 0.02 | 0.452 | 10.91 |
| nmf_k64 | -0.54 | 0.02 | 0.450 | 16.42 |
| pca_k32 | -0.54 | 0.02 | 0.449 | 11.34 |
| nystroem_k256_g0.5 | -0.65 | 0.02 | 0.428 | 7.85 |
| nystroem_k64_g2 | -0.67 | 0.02 | 0.423 | 12.34 |
| pca_k256 | -0.70 | 0.02 | 0.419 | 6.84 |
| gmm_k100 | -0.75 | 0.02 | 0.408 | 18.29 |
| pca_k16 | -0.78 | 0.02 | 0.403 | 8.53 |
| ica_k16 | -0.78 | 0.02 | 0.403 | 8.55 |
| nmf_k16 | -0.87 | 0.02 | 0.385 | 21.52 |
| gmm_k30 | -1.06 | 0.02 | 0.348 | 32.84 |
| pca_k8 | -1.06 | 0.02 | 0.348 | 15.96 |
| rproj_k128_s1 | -1.20 | 0.02 | 0.322 | 30.98 |
| rproj_k128_s0 | -1.25 | 0.02 | 0.315 | 11.80 |
| pca_k4 | -1.33 | 0.02 | 0.300 | 38.48 |
| gmm_k10 | -1.54 | 0.02 | 0.264 | 26.45 |
| rproj_k32_s1 | -1.61 | 0.02 | 0.254 | 47.91 |
| rproj_k32_s0 | -1.61 | 0.02 | 0.252 | 20.64 |
| rproj_k8_s0 | -1.88 | 0.03 | 0.213 | 36.10 |
| rproj_k8_s1 | -2.03 | 0.03 | 0.192 | 41.19 |
| random_k32_s0 | -2.10 | 0.03 | 0.182 | 74.55 |
| random_k32_s1 | -2.10 | 0.03 | 0.182 | 69.35 |
| depth2 | -2.11 | 0.03 | 0.181 | 38.80 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.142 | 9.3e-02 | 140 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000178|platelet|SRX14122105 | 4.78 | 0.65 | 0.00 |
| UBERON:0000178|mature NK T cell|SRX26317326 | 4.53 | 0.48 | 0.00 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX14122104 | 4.33 | 0.55 | 0.01 |
| UBERON:0000178|platelet|SRX14122102 | 4.28 | 0.48 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX10519950 | 4.20 | 0.48 | 0.01 |
| UBERON:0000178|mature NK T cell|SRX11515844 | 3.90 | 0.44 | 0.01 |
| UBERON:0000178|platelet|SRX14122101 | 3.80 | 0.30 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX14122116 | 3.62 | 0.33 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX12219249 | 3.45 | 0.26 | 0.01 |
| UBERON:0000178|platelet|SRX14122104 | 3.43 | 0.24 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX14122105 | 3.42 | 0.33 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX14122081 | 3.33 | 0.29 | 0.01 |
| UBERON:0000178|platelet|SRX14122078 | 3.32 | 0.28 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX14122078 | 3.30 | 0.16 | 0.01 |
| UBERON:0000178|CD8-positive, alpha-beta T cell|SRX24216824 | 3.21 | 0.14 | 0.02 |

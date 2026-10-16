# Component A summary: repr_scbasecount_mouse_spleen


## cell_level

- items: 18468; informative (non-degenerate): 14303; nobody passes: 4165; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.45, -2.42, -1.14, 0.24, 1.95]; median SE 0.48
- histogram (bin lower edge: count): -6: 0, -5: 5, -4: 1868, -3: 3141, -2: 2375, -1: 3019, +0: 1986, +1: 1909, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.43 | 0.02 | 0.472 | 0.55 |
| nystroem_k64_g0.5 | -0.58 | 0.02 | 0.454 | 0.42 |
| nystroem_k256_g2 | -0.59 | 0.02 | 0.453 | 0.63 |
| pca_k128 | -0.66 | 0.02 | 0.443 | 0.42 |
| pca_k256 | -0.69 | 0.02 | 0.439 | 0.52 |
| nmf_k64 | -0.70 | 0.02 | 0.438 | 0.59 |
| pca_k64 | -0.73 | 0.02 | 0.435 | 0.38 |
| ica_k64 | -0.73 | 0.02 | 0.435 | 0.38 |
| nystroem_k64_g2 | -0.81 | 0.02 | 0.425 | 0.59 |
| pca_k32 | -0.96 | 0.02 | 0.406 | 0.41 |
| gmm_k100 | -0.96 | 0.02 | 0.406 | 0.75 |
| nmf_k16 | -1.02 | 0.02 | 0.398 | 0.60 |
| rproj_k128_s0 | -1.19 | 0.02 | 0.377 | 0.66 |
| ica_k16 | -1.20 | 0.02 | 0.376 | 0.43 |
| pca_k16 | -1.20 | 0.02 | 0.376 | 0.43 |
| rproj_k128_s1 | -1.25 | 0.02 | 0.370 | 0.66 |
| gmm_k30 | -1.29 | 0.02 | 0.365 | 0.73 |
| pca_k8 | -1.56 | 0.02 | 0.330 | 0.56 |
| gmm_k10 | -1.74 | 0.02 | 0.308 | 0.96 |
| rproj_k32_s1 | -1.80 | 0.02 | 0.301 | 0.89 |
| rproj_k32_s0 | -1.81 | 0.02 | 0.299 | 1.04 |
| pca_k4 | -1.91 | 0.02 | 0.287 | 0.76 |
| rproj_k8_s1 | -2.71 | 0.02 | 0.195 | 1.89 |
| rproj_k8_s0 | -2.83 | 0.02 | 0.182 | 2.17 |
| depth2 | -2.95 | 0.02 | 0.170 | 4.06 |
| random_k32_s0 | -3.72 | 0.03 | 0.103 | 4.40 |
| random_k32_s1 | -3.72 | 0.03 | 0.103 | 4.54 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.231 | 1.9e-172 | 14303 |
| log_total_counts | -0.241 | 1.2e-188 | 14303 |
| n_genes_by_counts | -0.214 | 4.3e-148 | 14303 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| CD8-positive, alpha-beta T cell | 790.0 | 0.52 | 2619 |
| macrophage dendritic cell progenitor | 540.0 | 0.18 | 882 |
| CD4-positive, alpha-beta T cell | 1619.0 | -0.20 | 4861 |
| erythroblast | 1914.0 | -0.45 | 5993 |
| T cell | 1548.0 | -0.70 | 5176 |
| proerythroblast | 1099.0 | -1.00 | 1771 |
| megakaryocyte-erythroid progenitor cell | 661.0 | -1.31 | 1044 |
| mature NK T cell | 787.0 | -1.34 | 3420 |
| natural killer cell | 754.0 | -1.39 | 897 |
| plasma cell | 614.0 | -1.49 | 385 |
| B cell | 1923.0 | -1.78 | 4173 |
| macrophage | 1125.0 | -2.31 | 1405 |
| granulocyte | 917.0 | -2.39 | 1318 |

## stratum_binomial

- items: 231; informative (non-degenerate): 223; nobody passes: 8; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.16, -1.33, -0.57, 0.53, 3.18]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 14, -2: 60, -1: 70, +0: 31, +1: 20, +2: 13, +3: 6, +4: 3, +5: 3

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.42 | 0.02 | 0.472 | 6.90 |
| nystroem_k64_g0.5 | -0.52 | 0.02 | 0.454 | 5.36 |
| nystroem_k256_g2 | -0.53 | 0.02 | 0.453 | 8.28 |
| pca_k128 | -0.59 | 0.02 | 0.443 | 4.47 |
| pca_k256 | -0.61 | 0.02 | 0.439 | 4.91 |
| nmf_k64 | -0.61 | 0.02 | 0.438 | 5.90 |
| pca_k64 | -0.63 | 0.02 | 0.435 | 4.98 |
| ica_k64 | -0.64 | 0.02 | 0.435 | 5.05 |
| nystroem_k64_g2 | -0.69 | 0.02 | 0.425 | 8.95 |
| pca_k32 | -0.80 | 0.02 | 0.406 | 5.21 |
| gmm_k100 | -0.80 | 0.02 | 0.406 | 13.00 |
| nmf_k16 | -0.84 | 0.02 | 0.398 | 8.83 |
| rproj_k128_s0 | -0.96 | 0.02 | 0.377 | 3.52 |
| ica_k16 | -0.97 | 0.02 | 0.376 | 7.12 |
| pca_k16 | -0.97 | 0.02 | 0.376 | 7.05 |
| rproj_k128_s1 | -1.01 | 0.02 | 0.370 | 4.08 |
| gmm_k30 | -1.04 | 0.02 | 0.365 | 21.41 |
| pca_k8 | -1.24 | 0.02 | 0.330 | 12.25 |
| gmm_k10 | -1.37 | 0.02 | 0.308 | 27.28 |
| rproj_k32_s1 | -1.42 | 0.02 | 0.301 | 4.47 |
| rproj_k32_s0 | -1.43 | 0.02 | 0.299 | 7.64 |
| pca_k4 | -1.51 | 0.02 | 0.287 | 12.97 |
| rproj_k8_s1 | -2.14 | 0.02 | 0.195 | 16.81 |
| rproj_k8_s0 | -2.24 | 0.02 | 0.182 | 20.37 |
| depth2 | -2.34 | 0.02 | 0.170 | 73.86 |
| random_k32_s0 | -3.01 | 0.03 | 0.103 | 123.91 |
| random_k32_s1 | -3.01 | 0.03 | 0.103 | 133.27 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.034 | 6.1e-01 | 223 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002106|CD8-positive, alpha-beta T cell|SRX9091058 | 6.03 | 0.83 | 0.00 |
| UBERON:0002106|CD8-positive, alpha-beta T cell|SRX19818527 | 6.03 | 0.64 | 0.00 |
| UBERON:0002106|granulocyte|SRX9091058 | 5.68 | 0.54 | 0.00 |
| UBERON:0002106|macrophage dendritic cell progenitor|SRX27257796 | 5.05 | 0.40 | 0.00 |
| UBERON:0002106|megakaryocyte-erythroid progenitor cell|SRX9091058 | 5.05 | 0.40 | 0.00 |
| UBERON:0002106|CD8-positive, alpha-beta T cell|SRX18787571 | 4.90 | 0.37 | 0.00 |
| UBERON:0002106|megakaryocyte-erythroid progenitor cell|SRX19067523 | 4.81 | 0.55 | 0.00 |
| UBERON:0002106|natural killer cell|SRX9091058 | 4.51 | 0.65 | 0.00 |
| UBERON:0002106|CD8-positive, alpha-beta T cell|SRX11430811 | 3.42 | 0.30 | 0.01 |
| UBERON:0002106|immature NK T cell|SRX19067523 | 3.34 | 0.26 | 0.01 |
| UBERON:0002106|macrophage dendritic cell progenitor|SRX26044421 | 3.32 | 0.17 | 0.01 |
| UBERON:0002106|macrophage dendritic cell progenitor|SRX24059961 | 3.18 | 0.16 | 0.01 |
| UBERON:0002106|CD8-positive, alpha-beta T cell|SRX26044405 | 3.11 | 0.15 | 0.02 |
| UBERON:0002106|granulocyte|SRX27257796 | 3.11 | 0.15 | 0.02 |
| UBERON:0002106|CD4-positive, alpha-beta T cell|SRX18787571 | 2.86 | 0.14 | 0.02 |

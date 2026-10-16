# Component A summary: repr_scbasecount_mouse_bone_marrow


## cell_level

- items: 20531; informative (non-degenerate): 16264; nobody passes: 4235; everybody passes: 32
- difficulty percentiles 5/25/50/75/95: [-3.9, -2.37, -1.17, 0.72, 2.16]; median SE 0.50
- histogram (bin lower edge: count): -6: 134, -5: 292, -4: 1838, -3: 3336, -2: 2760, -1: 2650, +0: 1770, +1: 1974, +2: 1510, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.27 | 0.02 | 0.486 | 0.52 |
| nystroem_k256_g2 | -0.34 | 0.02 | 0.478 | 0.53 |
| pca_k128 | -0.36 | 0.02 | 0.475 | 0.40 |
| nystroem_k64_g0.5 | -0.37 | 0.02 | 0.474 | 0.38 |
| pca_k64 | -0.38 | 0.02 | 0.473 | 0.33 |
| ica_k64 | -0.38 | 0.02 | 0.473 | 0.33 |
| pca_k256 | -0.41 | 0.02 | 0.470 | 0.51 |
| nmf_k64 | -0.48 | 0.02 | 0.461 | 0.53 |
| pca_k32 | -0.53 | 0.02 | 0.456 | 0.37 |
| nystroem_k64_g2 | -0.58 | 0.02 | 0.450 | 0.49 |
| nmf_k16 | -0.71 | 0.02 | 0.436 | 0.59 |
| rproj_k128_s1 | -0.83 | 0.02 | 0.421 | 0.73 |
| rproj_k128_s0 | -0.86 | 0.02 | 0.418 | 0.71 |
| gmm_k100 | -0.90 | 0.02 | 0.413 | 1.01 |
| ica_k16 | -0.95 | 0.02 | 0.407 | 0.49 |
| pca_k16 | -0.95 | 0.02 | 0.407 | 0.49 |
| gmm_k30 | -1.33 | 0.02 | 0.363 | 1.00 |
| pca_k8 | -1.43 | 0.02 | 0.351 | 0.84 |
| rproj_k32_s0 | -1.67 | 0.02 | 0.323 | 1.12 |
| rproj_k32_s1 | -1.72 | 0.02 | 0.317 | 1.19 |
| gmm_k10 | -2.10 | 0.02 | 0.273 | 1.39 |
| pca_k4 | -2.11 | 0.02 | 0.272 | 1.39 |
| rproj_k8_s1 | -2.97 | 0.02 | 0.180 | 2.98 |
| depth2 | -3.16 | 0.02 | 0.162 | 3.38 |
| rproj_k8_s0 | -3.17 | 0.02 | 0.162 | 2.79 |
| random_k32_s0 | -4.12 | 0.03 | 0.088 | 5.27 |
| random_k32_s1 | -4.13 | 0.03 | 0.087 | 4.99 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.174 | 1.5e-110 | 16264 |
| log_total_counts | 0.002 | 8.0e-01 | 16264 |
| n_genes_by_counts | -0.020 | 1.2e-02 | 16264 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| lymphoid lineage restricted progenitor cell | 36.0 | 1.35 | 437 |
| natural killer cell | 55.0 | 1.00 | 149 |
| CD4-positive, alpha-beta T cell | 54.0 | 0.97 | 156 |
| granulocyte monocyte progenitor cell | 811.0 | 0.87 | 1762 |
| proerythroblast | 280.0 | 0.49 | 939 |
| hematopoietic stem cell | 984.0 | 0.39 | 4184 |
| megakaryocyte-erythroid progenitor cell | 474.0 | 0.03 | 1051 |
| early pro-B cell | 203.0 | -0.06 | 945 |
| plasma cell | 615.0 | -0.13 | 1703 |
| late pro-B cell | 59.0 | -0.13 | 454 |
| granulocytopoietic cell | 1356.0 | -0.25 | 5255 |
| immature B cell | 499.0 | -0.81 | 1564 |
| precursor B cell | 1046.0 | -0.94 | 3954 |
| macrophage | 1121.0 | -1.07 | 2284 |
| promonocyte | 1204.0 | -1.11 | 3657 |

## stratum_binomial

- items: 280; informative (non-degenerate): 261; nobody passes: 19; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.93, -1.71, -0.63, 0.81, 3.0]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 11, -3: 33, -2: 66, -1: 50, +0: 46, +1: 35, +2: 6, +3: 3, +4: 5, +5: 5

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.66 | 0.02 | 0.486 | 5.91 |
| nystroem_k256_g2 | -0.72 | 0.02 | 0.478 | 6.72 |
| pca_k128 | -0.73 | 0.02 | 0.475 | 3.95 |
| nystroem_k64_g0.5 | -0.74 | 0.02 | 0.474 | 4.49 |
| pca_k64 | -0.74 | 0.02 | 0.473 | 3.71 |
| ica_k64 | -0.74 | 0.02 | 0.473 | 3.70 |
| pca_k256 | -0.77 | 0.02 | 0.470 | 4.36 |
| nmf_k64 | -0.82 | 0.02 | 0.461 | 5.91 |
| pca_k32 | -0.85 | 0.02 | 0.456 | 3.72 |
| nystroem_k64_g2 | -0.89 | 0.02 | 0.450 | 7.53 |
| nmf_k16 | -0.98 | 0.02 | 0.436 | 6.07 |
| rproj_k128_s1 | -1.07 | 0.02 | 0.421 | 3.42 |
| rproj_k128_s0 | -1.09 | 0.02 | 0.418 | 3.97 |
| gmm_k100 | -1.12 | 0.02 | 0.413 | 22.34 |
| ica_k16 | -1.15 | 0.02 | 0.407 | 6.27 |
| pca_k16 | -1.16 | 0.02 | 0.407 | 6.24 |
| gmm_k30 | -1.43 | 0.02 | 0.363 | 21.48 |
| pca_k8 | -1.51 | 0.02 | 0.351 | 13.13 |
| rproj_k32_s0 | -1.69 | 0.02 | 0.323 | 6.69 |
| rproj_k32_s1 | -1.73 | 0.02 | 0.317 | 7.10 |
| gmm_k10 | -2.02 | 0.02 | 0.273 | 29.77 |
| pca_k4 | -2.02 | 0.02 | 0.272 | 24.06 |
| rproj_k8_s1 | -2.71 | 0.02 | 0.180 | 23.11 |
| depth2 | -2.87 | 0.02 | 0.162 | 51.71 |
| rproj_k8_s0 | -2.88 | 0.02 | 0.162 | 17.15 |
| random_k32_s0 | -3.70 | 0.03 | 0.088 | 49.39 |
| random_k32_s1 | -3.71 | 0.03 | 0.087 | 47.64 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.380 | 2.1e-10 | 261 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002371|mature alpha-beta T cell|SRX15637240 | 6.35 | 0.83 | 0.00 |
| UBERON:0002371|late pro-B cell|SRX11609965 | 5.94 | 0.84 | 0.00 |
| UBERON:0002371|granulocyte monocyte progenitor cell|SRX8581825 | 5.82 | 0.64 | 0.00 |
| UBERON:0002371|immature B cell|SRX20572293 | 5.52 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX11609965 | 5.20 | 0.85 | 0.00 |
| UBERON:0002371|immature B cell|SRX22513090 | 5.01 | 0.43 | 0.00 |
| UBERON:0002371|proerythroblast|SRX10048883 | 4.60 | 0.55 | 0.00 |
| UBERON:0002371|basophil|SRX22853046 | 4.43 | 0.35 | 0.00 |
| UBERON:0002371|precursor B cell|SRX22853046 | 4.39 | 0.35 | 0.00 |
| UBERON:0002371|proerythroblast|SRX17738217 | 4.34 | 0.66 | 0.00 |
| UBERON:0002371|lymphoid lineage restricted progenitor cell|SRX10944242 | 4.19 | 0.55 | 0.00 |
| UBERON:0002371|natural killer cell|SRX10944242 | 3.71 | 0.44 | 0.01 |
| UBERON:0002371|megakaryocyte-erythroid progenitor cell|SRX13257130 | 3.29 | 0.19 | 0.01 |
| UBERON:0002371|precursor B cell|SRX15637240 | 3.00 | 0.35 | 0.01 |
| UBERON:0002371|late pro-B cell|SRX13160591 | 2.94 | 0.30 | 0.02 |

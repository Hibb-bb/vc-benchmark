# Component A summary: repr_scbasecount_mouse_liver


## cell_level

- items: 19040; informative (non-degenerate): 13367; nobody passes: 5423; everybody passes: 250
- difficulty percentiles 5/25/50/75/95: [-4.59, -2.99, -1.98, 0.48, 2.2]; median SE 0.55
- histogram (bin lower edge: count): -6: 422, -5: 1144, -4: 1578, -3: 3277, -2: 1682, -1: 1158, +0: 1213, +1: 1408, +2: 1485, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | -0.27 | 0.03 | 0.480 | 0.34 |
| nystroem_k256_g0.5 | -0.32 | 0.03 | 0.476 | 0.62 |
| pca_k64 | -0.35 | 0.03 | 0.473 | 0.28 |
| ica_k64 | -0.35 | 0.03 | 0.473 | 0.28 |
| nystroem_k256_g2 | -0.38 | 0.03 | 0.471 | 0.88 |
| pca_k128 | -0.38 | 0.03 | 0.471 | 0.35 |
| nystroem_k64_g2 | -0.38 | 0.03 | 0.471 | 0.43 |
| nmf_k64 | -0.41 | 0.03 | 0.468 | 0.65 |
| pca_k32 | -0.41 | 0.03 | 0.468 | 0.28 |
| pca_k256 | -0.44 | 0.03 | 0.466 | 0.50 |
| pca_k16 | -0.66 | 0.02 | 0.447 | 0.33 |
| ica_k16 | -0.66 | 0.02 | 0.447 | 0.33 |
| nmf_k16 | -0.69 | 0.02 | 0.445 | 0.44 |
| gmm_k100 | -0.72 | 0.02 | 0.443 | 0.64 |
| pca_k8 | -0.81 | 0.02 | 0.435 | 0.38 |
| gmm_k30 | -0.86 | 0.02 | 0.430 | 0.55 |
| rproj_k128_s0 | -1.20 | 0.02 | 0.401 | 0.74 |
| rproj_k128_s1 | -1.33 | 0.02 | 0.390 | 0.85 |
| pca_k4 | -1.73 | 0.02 | 0.352 | 0.82 |
| rproj_k32_s0 | -2.19 | 0.02 | 0.308 | 1.10 |
| gmm_k10 | -2.42 | 0.02 | 0.285 | 2.39 |
| rproj_k32_s1 | -2.50 | 0.02 | 0.277 | 1.47 |
| rproj_k8_s0 | -3.24 | 0.02 | 0.206 | 2.36 |
| rproj_k8_s1 | -3.27 | 0.02 | 0.203 | 2.42 |
| depth2 | -3.40 | 0.02 | 0.192 | 3.71 |
| random_k32_s1 | -4.47 | 0.03 | 0.109 | 5.16 |
| random_k32_s0 | -4.50 | 0.03 | 0.107 | 5.35 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.426 | 0.0e+00 | 13367 |
| log_total_counts | -0.222 | 1.5e-148 | 13367 |
| n_genes_by_counts | -0.147 | 3.8e-65 | 13367 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| duct epithelial cell | 151.0 | 1.59 | 482 |
| T cell | 516.0 | 1.25 | 2636 |
| CD8-positive, alpha-beta T cell | 459.0 | 0.92 | 2021 |
| CD4-positive, alpha-beta T cell | 581.0 | 0.49 | 1801 |
| mature NK T cell | 407.0 | 0.44 | 1203 |
| hepatic stellate cell | 182.0 | -0.67 | 592 |
| B cell | 1654.0 | -0.95 | 3689 |
| Kupffer cell | 1393.0 | -1.30 | 3624 |
| plasmacytoid dendritic cell | 517.0 | -1.46 | 874 |
| neutrophil | 958.0 | -1.62 | 1741 |
| endothelial cell of hepatic sinusoid | 1401.0 | -1.69 | 3681 |
| myeloid leukocyte | 1615.0 | -1.73 | 3706 |
| natural killer cell | 1558.0 | -2.24 | 4476 |
| hepatocyte | 1975.0 | -3.19 | 4764 |

## stratum_binomial

- items: 241; informative (non-degenerate): 235; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.35, -1.91, -0.51, 1.96, 4.97]; median SE 0.07
- histogram (bin lower edge: count): -6: 2, -5: 4, -4: 11, -3: 39, -2: 55, -1: 18, +0: 22, +1: 26, +2: 26, +3: 11, +4: 9, +5: 10

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | -0.62 | 0.02 | 0.480 | 3.35 |
| nystroem_k256_g0.5 | -0.65 | 0.02 | 0.476 | 6.39 |
| pca_k64 | -0.68 | 0.02 | 0.473 | 2.70 |
| ica_k64 | -0.68 | 0.02 | 0.473 | 2.71 |
| nystroem_k256_g2 | -0.69 | 0.02 | 0.471 | 9.21 |
| pca_k128 | -0.69 | 0.02 | 0.471 | 3.21 |
| nystroem_k64_g2 | -0.69 | 0.02 | 0.471 | 4.81 |
| nmf_k64 | -0.71 | 0.02 | 0.468 | 7.79 |
| pca_k32 | -0.72 | 0.02 | 0.468 | 3.00 |
| pca_k256 | -0.73 | 0.02 | 0.466 | 3.99 |
| pca_k16 | -0.88 | 0.02 | 0.447 | 5.56 |
| ica_k16 | -0.88 | 0.02 | 0.447 | 5.58 |
| nmf_k16 | -0.90 | 0.02 | 0.445 | 5.29 |
| gmm_k100 | -0.92 | 0.02 | 0.443 | 7.90 |
| pca_k8 | -0.98 | 0.02 | 0.435 | 4.91 |
| gmm_k30 | -1.02 | 0.02 | 0.430 | 9.70 |
| rproj_k128_s0 | -1.24 | 0.02 | 0.401 | 3.11 |
| rproj_k128_s1 | -1.33 | 0.02 | 0.390 | 4.39 |
| pca_k4 | -1.62 | 0.02 | 0.352 | 13.03 |
| rproj_k32_s0 | -1.96 | 0.02 | 0.308 | 4.81 |
| gmm_k10 | -2.13 | 0.02 | 0.285 | 63.59 |
| rproj_k32_s1 | -2.19 | 0.02 | 0.277 | 6.53 |
| rproj_k8_s0 | -2.79 | 0.02 | 0.206 | 11.64 |
| rproj_k8_s1 | -2.81 | 0.02 | 0.203 | 13.77 |
| depth2 | -2.92 | 0.02 | 0.192 | 48.98 |
| random_k32_s1 | -3.84 | 0.03 | 0.109 | 65.26 |
| random_k32_s0 | -3.87 | 0.03 | 0.107 | 57.33 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.532 | 1.5e-18 | 235 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002107|T cell|SRX13549189 | 6.43 | 0.83 | 0.00 |
| UBERON:0002107|mature NK T cell|SRX10605823 | 6.34 | 0.83 | 0.00 |
| UBERON:0002107|mature NK T cell|SRX10593160 | 5.69 | 0.84 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX20602726 | 5.56 | 0.54 | 0.00 |
| UBERON:0002107|plasmacytoid dendritic cell|SRX10605823 | 5.34 | 0.85 | 0.00 |
| UBERON:0002107|CD4-positive, alpha-beta T cell|SRX13549189 | 5.31 | 0.48 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX13549198 | 5.27 | 0.65 | 0.00 |
| UBERON:0002107|endothelial cell of hepatic sinusoid|SRX15473825 | 5.25 | 0.85 | 0.00 |
| UBERON:0002107|endothelial cell of hepatic sinusoid|SRX19958841 | 5.25 | 0.85 | 0.00 |
| UBERON:0002107|Kupffer cell|SRX19958841 | 5.10 | 0.43 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX20602728 | 5.10 | 0.43 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX13549191 | 5.08 | 0.54 | 0.00 |
| UBERON:0002107|T cell|SRX10329628 | 4.93 | 0.40 | 0.00 |
| UBERON:0002107|T cell|SRX21831072 | 4.78 | 0.37 | 0.00 |
| UBERON:0002107|CD8-positive, alpha-beta T cell|SRX21831073 | 4.78 | 0.37 | 0.00 |

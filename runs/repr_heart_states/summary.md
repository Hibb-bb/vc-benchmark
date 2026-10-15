# Component A summary: repr_heart_states


## cell_level

- items: 14396; informative (non-degenerate): 13310; nobody passes: 1086; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.82, -1.66, -0.6, 0.91, 3.06]; median SE 0.49
- histogram (bin lower edge: count): -6: 3, -5: 98, -4: 520, -3: 1806, -2: 2817, -1: 2956, +0: 1788, +1: 1943, +2: 631, +3: 748, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.63 | 0.02 | 0.611 | 0.50 |
| nystroem_k64_g0.5 | 0.59 | 0.02 | 0.605 | 0.41 |
| pca_k128 | 0.57 | 0.02 | 0.603 | 0.53 |
| pca_k256 | 0.57 | 0.02 | 0.603 | 0.70 |
| pca_k64 | 0.55 | 0.02 | 0.601 | 0.40 |
| ica_k64 | 0.55 | 0.02 | 0.601 | 0.40 |
| scvi_k30_bnone | 0.55 | 0.02 | 0.601 | 0.79 |
| nystroem_k256_g2 | 0.55 | 0.02 | 0.601 | 0.52 |
| scvi_k30_btissue | 0.54 | 0.02 | 0.598 | 0.90 |
| pca_k32 | 0.37 | 0.02 | 0.577 | 0.49 |
| nystroem_k64_g2 | 0.37 | 0.02 | 0.576 | 0.58 |
| scvi_k10_btissue | 0.31 | 0.02 | 0.568 | 0.95 |
| nmf_k64 | 0.24 | 0.02 | 0.559 | 0.75 |
| pca_k16 | -0.15 | 0.02 | 0.505 | 0.62 |
| ica_k16 | -0.15 | 0.02 | 0.504 | 0.62 |
| rproj_k128_s1 | -0.29 | 0.02 | 0.485 | 1.02 |
| rproj_k128_s0 | -0.32 | 0.02 | 0.480 | 1.09 |
| gmm_k100 | -0.51 | 0.02 | 0.453 | 0.98 |
| nmf_k16 | -0.54 | 0.02 | 0.449 | 1.09 |
| pca_k8 | -0.89 | 0.02 | 0.397 | 1.08 |
| gmm_k30 | -1.52 | 0.02 | 0.308 | 1.82 |
| pca_k4 | -1.57 | 0.02 | 0.301 | 1.66 |
| rproj_k32_s1 | -1.63 | 0.02 | 0.292 | 1.70 |
| rproj_k32_s0 | -1.67 | 0.02 | 0.287 | 1.82 |
| gmm_k10 | -2.78 | 0.03 | 0.154 | 3.37 |
| rproj_k8_s1 | -2.90 | 0.03 | 0.142 | 3.26 |
| rproj_k8_s0 | -3.29 | 0.03 | 0.109 | 4.20 |
| depth2 | -4.21 | 0.04 | 0.053 | 4.35 |
| random_k32_s1 | -4.92 | 0.05 | 0.029 | 8.38 |
| random_k32_s0 | -4.97 | 0.05 | 0.028 | 8.70 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.035 | 4.6e-05 | 13310 |
| log_total_counts | -0.136 | 2.4e-56 | 13310 |
| n_genes_by_counts | -0.125 | 9.1e-48 | 13310 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| DC | 130.0 | 1.75 | 366 |
| aCM4 | 130.0 | 1.18 | 934 |
| CD4+T_cytox | 274.0 | 1.12 | 1144 |
| LYVE1+MØ2 | 223.0 | 1.08 | 1151 |
| EC4_immune | 308.0 | 1.07 | 2000 |
| LYVE1+MØ3 | 277.0 | 1.02 | 1179 |
| vCM5 | 113.0 | 1.00 | 407 |
| EC10_CMC-like | 112.0 | 0.96 | 1048 |
| NKT | 75.0 | 0.95 | 640 |
| Mo_pi | 83.0 | 0.92 | 591 |
| vCM4 | 234.0 | 0.59 | 1732 |
| aCM3 | 229.0 | 0.36 | 1632 |
| Adip3 | 68.0 | 0.35 | 166 |
| LYVE1+MØ1 | 311.0 | 0.33 | 1554 |
| vCM3 | 239.0 | 0.29 | 1800 |

## stratum_binomial

- items: 315; informative (non-degenerate): 315; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.74, -0.77, 0.03, 0.85, 2.04]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 14, -2: 41, -1: 100, +0: 94, +1: 49, +2: 12, +3: 2, +4: 3, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.60 | 0.02 | 0.611 | 2.36 |
| nystroem_k64_g0.5 | 0.56 | 0.02 | 0.605 | 1.99 |
| pca_k128 | 0.56 | 0.02 | 0.603 | 2.28 |
| pca_k256 | 0.55 | 0.02 | 0.603 | 2.46 |
| pca_k64 | 0.54 | 0.02 | 0.601 | 2.08 |
| ica_k64 | 0.54 | 0.02 | 0.601 | 2.06 |
| scvi_k30_bnone | 0.54 | 0.02 | 0.601 | 3.61 |
| nystroem_k256_g2 | 0.54 | 0.02 | 0.601 | 2.49 |
| scvi_k30_btissue | 0.53 | 0.02 | 0.598 | 4.23 |
| pca_k32 | 0.42 | 0.02 | 0.577 | 2.02 |
| nystroem_k64_g2 | 0.41 | 0.02 | 0.576 | 3.28 |
| scvi_k10_btissue | 0.37 | 0.02 | 0.568 | 5.16 |
| nmf_k64 | 0.32 | 0.02 | 0.559 | 2.77 |
| pca_k16 | 0.04 | 0.02 | 0.505 | 3.25 |
| ica_k16 | 0.04 | 0.02 | 0.504 | 3.24 |
| rproj_k128_s1 | -0.06 | 0.02 | 0.485 | 2.46 |
| rproj_k128_s0 | -0.09 | 0.02 | 0.480 | 3.40 |
| gmm_k100 | -0.23 | 0.02 | 0.453 | 11.43 |
| nmf_k16 | -0.25 | 0.02 | 0.449 | 6.19 |
| pca_k8 | -0.52 | 0.02 | 0.397 | 6.87 |
| gmm_k30 | -1.02 | 0.02 | 0.308 | 31.00 |
| pca_k4 | -1.06 | 0.02 | 0.301 | 11.72 |
| rproj_k32_s1 | -1.11 | 0.02 | 0.292 | 4.17 |
| rproj_k32_s0 | -1.14 | 0.02 | 0.287 | 4.87 |
| gmm_k10 | -2.10 | 0.03 | 0.154 | 47.32 |
| rproj_k8_s1 | -2.21 | 0.03 | 0.142 | 7.42 |
| rproj_k8_s0 | -2.57 | 0.03 | 0.109 | 9.46 |
| depth2 | -3.44 | 0.04 | 0.053 | 22.08 |
| random_k32_s1 | -4.13 | 0.05 | 0.029 | 18.51 |
| random_k32_s0 | -4.17 | 0.05 | 0.028 | 17.94 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.146 | 9.2e-03 | 315 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Harvard-Nuclei|CD4+T_tem|H2 | 4.42 | 0.26 | 0.01 |
| Sanger-CD45|EC10_CMC-like|D7 | 4.21 | 0.22 | 0.01 |
| Harvard-Nuclei|CD4+T_tem|H4 | 4.02 | 0.32 | 0.02 |
| Sanger-Nuclei|Mo_pi|D3 | 3.39 | 0.15 | 0.03 |
| Sanger-Nuclei|CD16+Mo|D3 | 3.22 | 0.15 | 0.04 |
| Sanger-Cells|FB2|D7 | 2.89 | 0.19 | 0.05 |
| Sanger-Nuclei|DC|D7 | 2.72 | 0.11 | 0.06 |
| Harvard-Nuclei|EC4_immune|H4 | 2.58 | 0.11 | 0.07 |
| Harvard-Nuclei|EC4_immune|H2 | 2.57 | 0.10 | 0.07 |
| Sanger-Nuclei|LYVE1+MØ2|D3 | 2.33 | 0.10 | 0.08 |
| Sanger-CD45|DC|D7 | 2.31 | 0.09 | 0.08 |
| Sanger-CD45|CD8+T_tem|D7 | 2.25 | 0.09 | 0.09 |
| Sanger-Nuclei|CD4+T_cytox|D7 | 2.25 | 0.09 | 0.09 |
| Sanger-Nuclei|aCM2|D1 | 2.18 | 0.09 | 0.10 |
| Sanger-Nuclei|FB2|D1 | 2.15 | 0.09 | 0.10 |

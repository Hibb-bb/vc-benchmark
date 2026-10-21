# Component A summary: repr_hao_pbmc_l2


## cell_level

- items: 7999; informative (non-degenerate): 7842; nobody passes: 154; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-2.77, -1.68, -0.48, 1.16, 3.82]; median SE 0.59
- histogram (bin lower edge: count): -6: 0, -5: 50, -4: 292, -3: 1278, -2: 1205, -1: 1591, +0: 1447, +1: 879, +2: 443, +3: 330, +4: 245, +5: 82

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 3.51 | 0.05 | 0.887 | 0.64 |
| scvi_k30_bnone | 3.46 | 0.05 | 0.884 | 0.68 |
| fm_transcriptformer | 3.44 | 0.05 | 0.885 | 2.84 |
| scvi_k10_btissue | 3.21 | 0.05 | 0.870 | 0.80 |
| fm_geneformer_v2_316m | 3.09 | 0.04 | 0.862 | 1.21 |
| nystroem_k64_g0.5 | 2.99 | 0.04 | 0.856 | 0.22 |
| nystroem_k256_g0.5 | 2.97 | 0.04 | 0.855 | 0.28 |
| nystroem_k256_g2 | 2.90 | 0.04 | 0.850 | 0.43 |
| ica_k64 | 2.90 | 0.04 | 0.850 | 0.23 |
| pca_k64 | 2.89 | 0.04 | 0.849 | 0.23 |
| pca_k128 | 2.88 | 0.04 | 0.848 | 0.33 |
| pca_k32 | 2.78 | 0.04 | 0.842 | 0.28 |
| nystroem_k64_g2 | 2.76 | 0.04 | 0.840 | 0.54 |
| nmf_k64 | 2.75 | 0.04 | 0.839 | 0.80 |
| pca_k256 | 2.74 | 0.04 | 0.839 | 0.52 |
| fm_state | 2.56 | 0.04 | 0.827 | 1.72 |
| fm_scgpt | 2.43 | 0.04 | 0.815 | 1.01 |
| fm_uce | 2.32 | 0.04 | 0.806 | 1.90 |
| ica_k16 | 1.86 | 0.04 | 0.763 | 0.52 |
| pca_k16 | 1.86 | 0.04 | 0.763 | 0.52 |
| gmm_k100 | 1.79 | 0.04 | 0.756 | 0.83 |
| rproj_k128_s1 | 1.56 | 0.03 | 0.732 | 1.04 |
| rproj_k128_s0 | 1.51 | 0.03 | 0.727 | 1.01 |
| fm_cellplm | 1.12 | 0.03 | 0.682 | 1.07 |
| gmm_k30 | 1.09 | 0.03 | 0.678 | 1.12 |
| nmf_k16 | 1.06 | 0.03 | 0.675 | 1.01 |
| fm_scprint_large_v1 | 0.99 | 0.03 | 0.667 | 1.99 |
| pca_k8 | 0.18 | 0.03 | 0.556 | 0.95 |
| rproj_k32_s1 | -0.07 | 0.03 | 0.519 | 1.73 |
| pca_k4 | -0.19 | 0.03 | 0.501 | 1.12 |
| rproj_k32_s0 | -0.20 | 0.03 | 0.501 | 1.79 |
| gmm_k10 | -1.17 | 0.03 | 0.357 | 1.43 |
| rproj_k8_s1 | -1.97 | 0.03 | 0.248 | 4.36 |
| rproj_k8_s0 | -2.00 | 0.03 | 0.245 | 3.17 |
| depth2 | -2.22 | 0.03 | 0.217 | 3.28 |
| random_k32_s1 | -4.16 | 0.05 | 0.058 | 13.66 |
| random_k32_s0 | -4.17 | 0.05 | 0.058 | 10.80 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.397 | 2.3e-294 | 7842 |
| log_total_counts | -0.174 | 1.4e-54 | 7842 |
| n_genes_by_counts | -0.259 | 5.9e-120 | 7842 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| dnT | 86.0 | 3.83 | 47 |
| CD8 TCM | 435.0 | 2.01 | 1676 |
| Doublet | 105.0 | 1.95 | 317 |
| Treg | 442.0 | 1.51 | 1139 |
| CD4 TEM | 442.0 | 1.31 | 2430 |
| CD4 CTL | 149.0 | 1.23 | 1345 |
| gdT | 297.0 | 1.13 | 2006 |
| MAIT | 449.0 | 1.06 | 1004 |
| B intermediate | 434.0 | 1.02 | 1789 |
| CD4 TCM | 450.0 | 0.77 | 3000 |
| CD8 TEM | 446.0 | 0.31 | 2876 |
| NK Proliferating | 64.0 | -0.14 | 292 |
| NK_CD56bright | 219.0 | -0.30 | 690 |
| CD8 Naive | 450.0 | -0.39 | 2913 |
| B memory | 410.0 | -0.44 | 2092 |

## stratum_binomial

- items: 171; informative (non-degenerate): 171; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.15, -1.38, -0.34, 0.69, 1.61]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 10, -2: 43, -1: 40, +0: 49, +1: 23, +2: 3, +3: 2, +4: 1, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 2.39 | 0.04 | 0.887 | 2.19 |
| fm_transcriptformer | 2.37 | 0.04 | 0.885 | 3.36 |
| scvi_k30_bnone | 2.36 | 0.04 | 0.884 | 2.30 |
| scvi_k10_btissue | 2.21 | 0.04 | 0.870 | 2.24 |
| fm_geneformer_v2_316m | 2.13 | 0.04 | 0.862 | 3.08 |
| nystroem_k64_g0.5 | 2.06 | 0.03 | 0.856 | 1.15 |
| nystroem_k256_g0.5 | 2.05 | 0.03 | 0.855 | 1.20 |
| nystroem_k256_g2 | 2.01 | 0.03 | 0.850 | 1.55 |
| ica_k64 | 2.00 | 0.03 | 0.850 | 1.13 |
| pca_k64 | 2.00 | 0.03 | 0.849 | 1.11 |
| pca_k128 | 1.99 | 0.03 | 0.848 | 1.22 |
| pca_k32 | 1.93 | 0.03 | 0.842 | 1.20 |
| nystroem_k64_g2 | 1.91 | 0.03 | 0.840 | 2.65 |
| nmf_k64 | 1.91 | 0.03 | 0.839 | 3.50 |
| pca_k256 | 1.90 | 0.03 | 0.839 | 1.48 |
| fm_state | 1.80 | 0.03 | 0.827 | 1.77 |
| fm_scgpt | 1.70 | 0.03 | 0.815 | 1.87 |
| fm_uce | 1.63 | 0.03 | 0.806 | 2.65 |
| ica_k16 | 1.31 | 0.03 | 0.763 | 1.95 |
| pca_k16 | 1.31 | 0.03 | 0.763 | 1.94 |
| gmm_k100 | 1.26 | 0.03 | 0.756 | 4.51 |
| rproj_k128_s1 | 1.10 | 0.03 | 0.732 | 1.91 |
| rproj_k128_s0 | 1.07 | 0.03 | 0.727 | 2.16 |
| fm_cellplm | 0.79 | 0.03 | 0.682 | 4.58 |
| gmm_k30 | 0.77 | 0.03 | 0.678 | 14.57 |
| nmf_k16 | 0.75 | 0.03 | 0.675 | 5.20 |
| fm_scprint_large_v1 | 0.70 | 0.03 | 0.667 | 3.67 |
| pca_k8 | 0.08 | 0.03 | 0.556 | 6.05 |
| rproj_k32_s1 | -0.12 | 0.03 | 0.519 | 2.69 |
| pca_k4 | -0.21 | 0.03 | 0.501 | 6.89 |
| rproj_k32_s0 | -0.21 | 0.03 | 0.501 | 3.09 |
| gmm_k10 | -1.01 | 0.03 | 0.357 | 17.34 |
| rproj_k8_s1 | -1.68 | 0.03 | 0.248 | 5.93 |
| rproj_k8_s0 | -1.70 | 0.03 | 0.245 | 5.43 |
| depth2 | -1.89 | 0.03 | 0.217 | 16.66 |
| random_k32_s1 | -3.61 | 0.05 | 0.058 | 14.83 |
| random_k32_s0 | -3.61 | 0.05 | 0.058 | 8.39 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.485 | 1.7e-11 | 171 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| 0|dnT|P2 | 4.06 | 0.12 | 0.07 |
| 7|dnT|P2 | 3.34 | 0.08 | 0.13 |
| 3|dnT|P2 | 3.06 | 0.07 | 0.16 |
| 3|Doublet|P3 | 2.95 | 0.08 | 0.17 |
| 0|Doublet|P3 | 2.24 | 0.08 | 0.28 |
| 7|Doublet|P2 | 2.02 | 0.09 | 0.32 |
| 0|Doublet|P2 | 1.66 | 0.07 | 0.38 |
| 0|CD8 TCM|P4 | 1.64 | 0.06 | 0.38 |
| 3|Doublet|P2 | 1.63 | 0.08 | 0.39 |
| 0|CD8 TCM|P3 | 1.59 | 0.06 | 0.39 |
| 3|CD8 TCM|P4 | 1.59 | 0.06 | 0.39 |
| 3|CD8 TCM|P3 | 1.59 | 0.06 | 0.39 |
| 3|Treg|P2 | 1.49 | 0.06 | 0.41 |
| 7|Treg|P2 | 1.43 | 0.06 | 0.42 |
| 3|CD4 TEM|P4 | 1.43 | 0.06 | 0.42 |

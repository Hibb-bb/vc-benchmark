# Component A summary: repr_parse_pbmc_celltype


## cell_level

- items: 16811; informative (non-degenerate): 16637; nobody passes: 174; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.35, -1.1, -0.59, 0.59, 4.15]; median SE 0.69
- histogram (bin lower edge: count): -6: 0, -5: 23, -4: 489, -3: 1439, -2: 4374, -1: 4077, +0: 2862, +1: 1193, +2: 718, +3: 588, +4: 484, +5: 390

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 3.41 | 0.03 | 0.892 | 0.21 |
| nystroem_k64_g0.5 | 3.40 | 0.03 | 0.891 | 0.15 |
| nystroem_k256_g2 | 3.36 | 0.03 | 0.889 | 0.23 |
| scvi_k30_bnone | 3.34 | 0.03 | 0.888 | 0.42 |
| ica_k64 | 3.34 | 0.03 | 0.888 | 0.17 |
| pca_k128 | 3.33 | 0.03 | 0.888 | 0.22 |
| pca_k64 | 3.33 | 0.03 | 0.888 | 0.17 |
| fm_transcriptformer | 3.31 | 0.03 | 0.890 | 1.55 |
| pca_k32 | 3.31 | 0.03 | 0.886 | 0.18 |
| scvi_k30_btissue | 3.29 | 0.03 | 0.886 | 0.48 |
| fm_geneformer_v2_316m | 3.28 | 0.03 | 0.887 | 1.52 |
| nystroem_k64_g2 | 3.23 | 0.03 | 0.883 | 0.44 |
| pca_k256 | 3.22 | 0.03 | 0.882 | 0.34 |
| nmf_k64 | 3.15 | 0.03 | 0.878 | 0.39 |
| scvi_k10_btissue | 3.13 | 0.03 | 0.877 | 0.46 |
| pca_k16 | 2.97 | 0.03 | 0.868 | 0.30 |
| ica_k16 | 2.96 | 0.03 | 0.867 | 0.30 |
| fm_uce | 2.75 | 0.03 | 0.856 | 1.58 |
| fm_scgpt | 2.75 | 0.03 | 0.856 | 1.51 |
| fm_state | 2.70 | 0.03 | 0.853 | 1.48 |
| gmm_k100 | 2.60 | 0.03 | 0.844 | 0.80 |
| nmf_k16 | 2.56 | 0.03 | 0.842 | 0.69 |
| rproj_k128_s0 | 2.36 | 0.03 | 0.827 | 0.78 |
| rproj_k128_s1 | 2.33 | 0.03 | 0.825 | 0.74 |
| fm_cellplm | 2.27 | 0.03 | 0.820 | 1.37 |
| gmm_k30 | 1.93 | 0.03 | 0.791 | 0.95 |
| fm_scprint_large_v1 | 1.71 | 0.02 | 0.773 | 2.00 |
| pca_k8 | 1.48 | 0.02 | 0.747 | 0.99 |
| rproj_k32_s0 | 0.59 | 0.02 | 0.633 | 1.56 |
| rproj_k32_s1 | 0.57 | 0.02 | 0.630 | 1.52 |
| pca_k4 | 0.54 | 0.02 | 0.625 | 1.66 |
| gmm_k10 | -0.38 | 0.02 | 0.478 | 2.58 |
| rproj_k8_s1 | -1.30 | 0.02 | 0.325 | 3.30 |
| rproj_k8_s0 | -1.50 | 0.02 | 0.294 | 5.12 |
| depth2 | -2.63 | 0.02 | 0.147 | 18.90 |
| random_k32_s1 | -3.80 | 0.03 | 0.059 | 39.63 |
| random_k32_s0 | -3.82 | 0.03 | 0.058 | 41.22 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.506 | 0.0e+00 | 16637 |
| log_total_counts | -0.288 | 0.0e+00 | 16637 |
| n_genes_by_counts | -0.279 | 6.6e-295 | 16637 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| CD4 Memory | 939.0 | 2.39 | 2800 |
| CD8 Memory | 928.0 | 2.14 | 2800 |
| CD4 Naive | 989.0 | 1.57 | 2800 |
| MAIT | 987.0 | 0.64 | 2800 |
| B Intermediate/Memory | 997.0 | 0.24 | 2800 |
| NK | 987.0 | 0.21 | 2800 |
| CD8 Naive | 1000.0 | 0.03 | 2800 |
| NKT | 957.0 | 0.02 | 2800 |
| NK CD56bright | 999.0 | 0.01 | 2800 |
| Treg | 1000.0 | -0.10 | 2800 |
| CD16 Mono | 1000.0 | -0.50 | 2648 |
| B Naive | 1000.0 | -0.68 | 2800 |
| CD14 Mono | 1000.0 | -0.69 | 2800 |
| Plasmablast | 578.0 | -1.08 | 1593 |
| pDC | 601.0 | -1.31 | 1858 |

## stratum_binomial

- items: 176; informative (non-degenerate): 176; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.93, -1.12, -0.28, 0.32, 1.85]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 8, -2: 38, -1: 70, +0: 26, +1: 26, +2: 8, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 2.39 | 0.03 | 0.892 | 1.65 |
| nystroem_k64_g0.5 | 2.39 | 0.03 | 0.891 | 1.72 |
| fm_transcriptformer | 2.37 | 0.03 | 0.890 | 2.36 |
| nystroem_k256_g2 | 2.36 | 0.03 | 0.889 | 1.75 |
| scvi_k30_bnone | 2.35 | 0.03 | 0.888 | 2.05 |
| ica_k64 | 2.35 | 0.03 | 0.888 | 1.45 |
| pca_k128 | 2.35 | 0.03 | 0.888 | 1.44 |
| pca_k64 | 2.35 | 0.03 | 0.888 | 1.45 |
| fm_geneformer_v2_316m | 2.34 | 0.03 | 0.887 | 2.70 |
| pca_k32 | 2.33 | 0.03 | 0.886 | 1.31 |
| scvi_k30_btissue | 2.32 | 0.03 | 0.886 | 1.98 |
| nystroem_k64_g2 | 2.29 | 0.03 | 0.883 | 2.35 |
| pca_k256 | 2.28 | 0.03 | 0.882 | 1.52 |
| nmf_k64 | 2.24 | 0.03 | 0.878 | 1.59 |
| scvi_k10_btissue | 2.22 | 0.03 | 0.877 | 2.41 |
| pca_k16 | 2.12 | 0.02 | 0.868 | 1.92 |
| ica_k16 | 2.12 | 0.02 | 0.867 | 1.96 |
| fm_uce | 2.01 | 0.02 | 0.856 | 1.92 |
| fm_scgpt | 2.00 | 0.02 | 0.856 | 1.75 |
| fm_state | 1.98 | 0.02 | 0.853 | 2.82 |
| gmm_k100 | 1.90 | 0.02 | 0.844 | 4.40 |
| nmf_k16 | 1.87 | 0.02 | 0.842 | 2.97 |
| rproj_k128_s0 | 1.75 | 0.02 | 0.827 | 1.59 |
| rproj_k128_s1 | 1.73 | 0.02 | 0.825 | 1.48 |
| fm_cellplm | 1.69 | 0.02 | 0.820 | 3.76 |
| gmm_k30 | 1.46 | 0.02 | 0.791 | 15.40 |
| fm_scprint_large_v1 | 1.33 | 0.02 | 0.773 | 3.90 |
| pca_k8 | 1.15 | 0.02 | 0.747 | 7.07 |
| rproj_k32_s0 | 0.47 | 0.02 | 0.633 | 4.90 |
| rproj_k32_s1 | 0.45 | 0.02 | 0.630 | 3.24 |
| pca_k4 | 0.43 | 0.02 | 0.625 | 11.45 |
| gmm_k10 | -0.33 | 0.02 | 0.478 | 52.39 |
| rproj_k8_s1 | -1.13 | 0.02 | 0.325 | 8.87 |
| rproj_k8_s0 | -1.30 | 0.02 | 0.294 | 10.21 |
| depth2 | -2.32 | 0.02 | 0.147 | 66.06 |
| random_k32_s1 | -3.42 | 0.03 | 0.059 | 30.08 |
| random_k32_s0 | -3.44 | 0.03 | 0.058 | 30.51 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.710 | 3.0e-28 | 176 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| cytokine|CD4 Memory|Donor9 | 2.29 | 0.04 | 0.34 |
| cytokine|CD8 Memory|Donor11 | 2.21 | 0.04 | 0.35 |
| PBS|CD8 Memory|Donor9 | 2.18 | 0.04 | 0.36 |
| PBS|CD4 Memory|Donor9 | 2.15 | 0.04 | 0.37 |
| PBS|CD8 Memory|Donor11 | 2.12 | 0.04 | 0.37 |
| PBS|CD4 Memory|Donor10 | 2.07 | 0.04 | 0.38 |
| cytokine|CD8 Memory|Donor9 | 2.07 | 0.04 | 0.38 |
| cytokine|CD4 Memory|Donor10 | 2.05 | 0.04 | 0.38 |
| PBS|CD8 Memory|Donor8 | 1.88 | 0.04 | 0.42 |
| cytokine|CD8 Memory|Donor8 | 1.84 | 0.04 | 0.42 |
| PBS|CD4 Memory|Donor11 | 1.83 | 0.04 | 0.42 |
| PBS|CD4 Memory|Donor4 | 1.80 | 0.04 | 0.43 |
| cytokine|NKT|Donor4 | 1.77 | 0.04 | 0.44 |
| cytokine|CD4 Memory|Donor11 | 1.73 | 0.04 | 0.44 |
| cytokine|CD4 Memory|Donor4 | 1.66 | 0.04 | 0.46 |

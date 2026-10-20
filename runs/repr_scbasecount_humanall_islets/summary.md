# Component A summary: repr_scbasecount_humanall_islets


## cell_level

- items: 7654; informative (non-degenerate): 6312; nobody passes: 643; everybody passes: 699
- difficulty percentiles 5/25/50/75/95: [-3.28, -1.63, -0.48, 0.35, 4.33]; median SE 0.76
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 368, -3: 265, -2: 2520, -1: 1348, +0: 548, +1: 275, +2: 262, +3: 297, +4: 217, +5: 212

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k32 | 3.17 | 0.05 | 0.817 | 0.17 |
| ica_k64 | 3.15 | 0.05 | 0.817 | 0.17 |
| pca_k64 | 3.14 | 0.05 | 0.816 | 0.17 |
| nystroem_k64_g0.5 | 3.13 | 0.05 | 0.816 | 0.17 |
| nmf_k64 | 3.13 | 0.05 | 0.816 | 0.35 |
| pca_k128 | 3.12 | 0.05 | 0.815 | 0.31 |
| nystroem_k256_g0.5 | 3.10 | 0.05 | 0.814 | 0.25 |
| ica_k16 | 3.05 | 0.05 | 0.812 | 0.14 |
| pca_k16 | 3.04 | 0.05 | 0.812 | 0.14 |
| nystroem_k256_g2 | 3.04 | 0.05 | 0.811 | 0.28 |
| scvi_k30_bnone | 2.97 | 0.05 | 0.808 | 0.39 |
| scvi_k30_btissue | 2.97 | 0.05 | 0.808 | 0.39 |
| pca_k256 | 2.92 | 0.05 | 0.806 | 0.37 |
| nmf_k16 | 2.85 | 0.05 | 0.802 | 0.28 |
| nystroem_k64_g2 | 2.79 | 0.05 | 0.800 | 0.36 |
| pca_k8 | 2.70 | 0.05 | 0.795 | 0.27 |
| scvi_k10_btissue | 2.53 | 0.05 | 0.786 | 0.62 |
| rproj_k128_s0 | 2.37 | 0.05 | 0.777 | 0.66 |
| pca_k4 | 2.32 | 0.05 | 0.774 | 1.11 |
| rproj_k128_s1 | 2.26 | 0.05 | 0.771 | 0.70 |
| gmm_k100 | 2.17 | 0.05 | 0.765 | 0.64 |
| gmm_k30 | 2.01 | 0.05 | 0.756 | 0.85 |
| gmm_k10 | 1.92 | 0.04 | 0.750 | 0.47 |
| rproj_k32_s1 | 1.17 | 0.04 | 0.692 | 1.25 |
| rproj_k32_s0 | 0.91 | 0.04 | 0.668 | 1.28 |
| rproj_k8_s1 | -0.64 | 0.03 | 0.477 | 2.82 |
| rproj_k8_s0 | -0.92 | 0.03 | 0.437 | 3.32 |
| depth2 | -1.68 | 0.03 | 0.331 | 8.13 |
| random_k32_s1 | -2.88 | 0.04 | 0.196 | 14.41 |
| random_k32_s0 | -2.88 | 0.04 | 0.196 | 14.45 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.233 | 6.6e-79 | 6312 |
| log_total_counts | -0.401 | 7.2e-243 | 6312 |
| n_genes_by_counts | -0.380 | 1.6e-215 | 6312 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| B cell | 338.0 | 4.13 | 645 |
| macrophage | 1381.0 | 0.45 | 2859 |
| pancreatic acinar cell | 711.0 | -0.27 | 689 |
| pancreatic stellate cell | 1203.0 | -0.51 | 2066 |
| endothelial cell | 855.0 | -0.55 | 761 |
| pancreatic ductal cell | 1013.0 | -0.61 | 2666 |
| type B pancreatic cell | 801.0 | -1.52 | 4600 |

## stratum_binomial

- items: 96; informative (non-degenerate): 92; nobody passes: 4; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.92, -1.67, -1.31, -0.37, 4.66]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 3, -3: 12, -2: 41, -1: 16, +0: 4, +1: 1, +2: 4, +3: 4, +4: 3, +5: 3

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k32 | 1.26 | 0.04 | 0.817 | 3.86 |
| ica_k64 | 1.24 | 0.04 | 0.817 | 3.67 |
| pca_k64 | 1.24 | 0.04 | 0.816 | 3.70 |
| nystroem_k64_g0.5 | 1.23 | 0.04 | 0.816 | 3.35 |
| nmf_k64 | 1.23 | 0.04 | 0.816 | 3.72 |
| pca_k128 | 1.23 | 0.04 | 0.815 | 3.94 |
| nystroem_k256_g0.5 | 1.21 | 0.04 | 0.814 | 3.27 |
| ica_k16 | 1.18 | 0.04 | 0.812 | 3.34 |
| pca_k16 | 1.18 | 0.04 | 0.812 | 3.34 |
| nystroem_k256_g2 | 1.18 | 0.04 | 0.811 | 3.40 |
| scvi_k30_bnone | 1.13 | 0.04 | 0.808 | 2.78 |
| scvi_k30_btissue | 1.13 | 0.04 | 0.808 | 2.78 |
| pca_k256 | 1.10 | 0.04 | 0.806 | 3.31 |
| nmf_k16 | 1.06 | 0.04 | 0.802 | 2.95 |
| nystroem_k64_g2 | 1.02 | 0.04 | 0.800 | 3.87 |
| pca_k8 | 0.97 | 0.04 | 0.795 | 3.83 |
| scvi_k10_btissue | 0.87 | 0.04 | 0.786 | 4.91 |
| rproj_k128_s0 | 0.77 | 0.04 | 0.777 | 2.98 |
| pca_k4 | 0.74 | 0.04 | 0.774 | 7.13 |
| rproj_k128_s1 | 0.70 | 0.04 | 0.771 | 3.45 |
| gmm_k100 | 0.65 | 0.04 | 0.765 | 5.97 |
| gmm_k30 | 0.55 | 0.04 | 0.756 | 7.77 |
| gmm_k10 | 0.50 | 0.03 | 0.750 | 6.81 |
| rproj_k32_s1 | 0.02 | 0.03 | 0.692 | 5.64 |
| rproj_k32_s0 | -0.15 | 0.03 | 0.668 | 5.36 |
| rproj_k8_s1 | -1.25 | 0.03 | 0.477 | 6.11 |
| rproj_k8_s0 | -1.46 | 0.03 | 0.437 | 5.24 |
| depth2 | -2.03 | 0.03 | 0.331 | 61.95 |
| random_k32_s1 | -2.88 | 0.03 | 0.196 | 33.45 |
| random_k32_s0 | -2.88 | 0.03 | 0.196 | 33.35 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.606 | 1.6e-10 | 92 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000006|B cell|SRX12030196 | 7.00 | 0.47 | 0.00 |
| UBERON:0000006|natural killer cell|SRX6875730 | 6.00 | 0.40 | 0.01 |
| UBERON:0000006|natural killer cell|SRX6802637 | 5.77 | 0.35 | 0.01 |
| UBERON:0000006|B cell|SRX12030182 | 5.39 | 0.37 | 0.01 |
| UBERON:0000006|B cell|SRX18735813 | 4.71 | 0.24 | 0.02 |
| UBERON:0000006|B cell|SRX6802637 | 4.63 | 0.15 | 0.02 |
| UBERON:0000006|B cell|SRX6875730 | 4.07 | 0.14 | 0.04 |
| UBERON:0000006|B cell|SRX18735832 | 3.71 | 0.13 | 0.05 |
| UBERON:0000006|B cell|SRX18735790 | 3.32 | 0.12 | 0.07 |
| UBERON:0000006|B cell|SRX14493532 | 3.08 | 0.08 | 0.09 |
| UBERON:0000006|B cell|SRX18735838 | 3.02 | 0.13 | 0.10 |
| UBERON:0000006|B cell|SRX12030179 | 2.74 | 0.09 | 0.12 |
| UBERON:0000006|B cell|SRX18735792 | 2.70 | 0.06 | 0.13 |
| UBERON:0000006|B cell|SRX18735788 | 2.36 | 0.05 | 0.17 |
| UBERON:0000006|B cell|SRX24818035 | 2.14 | 0.05 | 0.20 |

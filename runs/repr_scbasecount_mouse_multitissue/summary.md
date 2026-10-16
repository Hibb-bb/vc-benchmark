# Component A summary: repr_scbasecount_mouse_multitissue


## cell_level

- items: 21148; informative (non-degenerate): 8543; nobody passes: 12605; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.48, -3.11, -2.03, -0.83, -0.83]; median SE 0.62
- histogram (bin lower edge: count): -6: 136, -5: 593, -4: 1515, -3: 2399, -2: 1384, -1: 2496, +0: 0, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gmm_k100 | -3.53 | 0.03 | 0.110 | 0.43 |
| nystroem_k64_g2 | -3.61 | 0.03 | 0.104 | 0.25 |
| nystroem_k64_g0.5 | -3.77 | 0.03 | 0.095 | 0.22 |
| pca_k64 | -3.79 | 0.03 | 0.094 | 0.19 |
| nystroem_k256_g2 | -3.79 | 0.03 | 0.094 | 0.33 |
| ica_k64 | -3.79 | 0.03 | 0.094 | 0.19 |
| pca_k32 | -3.82 | 0.03 | 0.093 | 0.26 |
| nmf_k64 | -3.83 | 0.03 | 0.092 | 0.36 |
| pca_k128 | -3.85 | 0.03 | 0.091 | 0.27 |
| pca_k16 | -3.88 | 0.03 | 0.089 | 0.26 |
| ica_k16 | -3.88 | 0.03 | 0.089 | 0.26 |
| pca_k256 | -3.88 | 0.03 | 0.089 | 0.33 |
| nystroem_k256_g0.5 | -3.89 | 0.03 | 0.089 | 0.32 |
| rproj_k128_s0 | -4.06 | 0.03 | 0.080 | 0.44 |
| nmf_k16 | -4.21 | 0.03 | 0.072 | 0.44 |
| pca_k8 | -4.26 | 0.03 | 0.070 | 0.61 |
| rproj_k128_s1 | -4.36 | 0.03 | 0.066 | 0.51 |
| rproj_k32_s0 | -4.39 | 0.03 | 0.064 | 0.59 |
| gmm_k30 | -4.52 | 0.03 | 0.059 | 0.47 |
| pca_k4 | -4.60 | 0.03 | 0.055 | 0.92 |
| rproj_k32_s1 | -4.65 | 0.04 | 0.053 | 0.65 |
| rproj_k8_s0 | -4.74 | 0.04 | 0.050 | 0.87 |
| depth2 | -4.96 | 0.04 | 0.043 | 0.85 |
| random_k32_s0 | -5.13 | 0.04 | 0.038 | 1.20 |
| rproj_k8_s1 | -5.13 | 0.04 | 0.038 | 0.93 |
| random_k32_s1 | -5.23 | 0.04 | 0.035 | 1.19 |
| gmm_k10 | -7.00 | 0.08 | 0.008 | 2.22 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.056 | 2.2e-07 | 8543 |
| log_total_counts | -0.115 | 1.4e-26 | 8543 |
| n_genes_by_counts | -0.122 | 7.4e-30 | 8543 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| fibroblast of cardiac tissue | 50.0 | -0.86 | 2000 |
| mature NK T cell | 45.0 | -0.92 | 742 |
| fibrocyte | 26.0 | -0.95 | 846 |
| aortic endothelial cell | 51.0 | -1.00 | 1911 |
| granulocytopoietic cell | 30.0 | -1.03 | 1129 |
| epithelial cell | 31.0 | -1.04 | 591 |
| fibroblast | 148.0 | -1.13 | 631 |
| hematopoietic precursor cell | 134.0 | -1.22 | 1434 |
| plasma cell | 70.0 | -1.29 | 1274 |
| DN4 thymocyte | 44.0 | -1.29 | 1605 |
| granulocyte | 179.0 | -1.45 | 1093 |
| naive B cell | 78.0 | -1.52 | 1033 |
| monocyte | 40.0 | -1.57 | 293 |
| promonocyte | 40.0 | -1.70 | 664 |
| lymphoid lineage restricted progenitor cell | 24.0 | -1.76 | 292 |

## stratum_binomial

- items: 259; informative (non-degenerate): 231; nobody passes: 28; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.77, -1.64, -0.11, 1.54, 3.57]; median SE 0.12
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 7, -3: 37, -2: 40, -1: 37, +0: 32, +1: 31, +2: 23, +3: 15, +4: 9, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gmm_k100 | -3.00 | 0.03 | 0.110 | 7.21 |
| nystroem_k64_g2 | -3.07 | 0.03 | 0.104 | 3.19 |
| nystroem_k64_g0.5 | -3.20 | 0.03 | 0.095 | 2.61 |
| pca_k64 | -3.22 | 0.03 | 0.094 | 2.21 |
| nystroem_k256_g2 | -3.22 | 0.03 | 0.094 | 5.46 |
| ica_k64 | -3.22 | 0.03 | 0.094 | 2.24 |
| pca_k32 | -3.24 | 0.03 | 0.093 | 3.35 |
| nmf_k64 | -3.26 | 0.03 | 0.092 | 3.97 |
| pca_k128 | -3.28 | 0.03 | 0.091 | 3.28 |
| pca_k16 | -3.29 | 0.03 | 0.089 | 3.85 |
| ica_k16 | -3.29 | 0.03 | 0.089 | 3.78 |
| pca_k256 | -3.30 | 0.03 | 0.089 | 4.15 |
| nystroem_k256_g0.5 | -3.30 | 0.03 | 0.089 | 5.31 |
| rproj_k128_s0 | -3.45 | 0.03 | 0.080 | 3.40 |
| nmf_k16 | -3.58 | 0.03 | 0.072 | 7.20 |
| pca_k8 | -3.62 | 0.03 | 0.070 | 14.74 |
| rproj_k128_s1 | -3.70 | 0.03 | 0.066 | 4.55 |
| rproj_k32_s0 | -3.73 | 0.03 | 0.064 | 4.92 |
| gmm_k30 | -3.84 | 0.03 | 0.059 | 13.72 |
| pca_k4 | -3.91 | 0.03 | 0.055 | 24.33 |
| rproj_k32_s1 | -3.96 | 0.03 | 0.053 | 5.06 |
| rproj_k8_s0 | -4.03 | 0.03 | 0.050 | 14.11 |
| depth2 | -4.22 | 0.04 | 0.043 | 19.10 |
| random_k32_s0 | -4.37 | 0.04 | 0.038 | 20.61 |
| rproj_k8_s1 | -4.37 | 0.04 | 0.038 | 13.44 |
| random_k32_s1 | -4.47 | 0.04 | 0.035 | 15.62 |
| gmm_k10 | -6.10 | 0.08 | 0.008 | 40.12 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.590 | 4.6e-23 | 231 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000178|granulocyte monocyte progenitor cell|SRX17682016 | 4.14 | 0.87 | 0.00 |
| UBERON:0000955|mature NK T cell|SRX10944181 | 4.14 | 0.87 | 0.00 |
| UBERON:0000955|mature NK T cell|SRX10722417 | 4.14 | 0.87 | 0.00 |
| UBERON:0002106|proerythroblast|SRX21144753 | 4.14 | 0.87 | 0.00 |
| UBERON:0002421|mature NK T cell|SRX14397751 | 4.14 | 0.87 | 0.00 |
| UBERON:0002421|mature NK T cell|SRX14647723 | 4.14 | 0.87 | 0.00 |
| UBERON:0002097|luminal epithelial cell of mammary gland|SRX23996461 | 4.14 | 0.87 | 0.00 |
| UBERON:0002421|mature NK T cell|SRX27438117 | 4.14 | 0.87 | 0.00 |
| UBERON:0002106|mature alpha-beta T cell|SRX23858146 | 4.08 | 0.87 | 0.00 |
| UBERON:0002421|mature NK T cell|SRX9670667 | 3.92 | 0.87 | 0.00 |
| UBERON:0002106|erythroblast|SRX21144753 | 3.57 | 0.66 | 0.00 |
| UBERON:0002106|plasma cell|SRX27257796 | 3.57 | 0.66 | 0.00 |
| UBERON:0002421|CD8-positive, alpha-beta T cell|SRX11706398 | 3.57 | 0.66 | 0.00 |
| UBERON:0002421|mature NK T cell|SRX11706403 | 3.57 | 0.66 | 0.00 |
| UBERON:0002106|CD4-positive, alpha-beta T cell|SRX18787571 | 3.57 | 0.66 | 0.00 |

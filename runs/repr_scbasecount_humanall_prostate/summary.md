# Component A summary: repr_scbasecount_humanall_prostate


## cell_level

- items: 8325; informative (non-degenerate): 7424; nobody passes: 849; everybody passes: 52
- difficulty percentiles 5/25/50/75/95: [-3.32, -2.21, -1.1, 0.77, 3.44]; median SE 0.60
- histogram (bin lower edge: count): -6: 0, -5: 203, -4: 367, -3: 1577, -2: 1956, -1: 964, +0: 625, +1: 544, +2: 381, +3: 468, +4: 339, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 1.51 | 0.04 | 0.698 | 0.33 |
| nystroem_k64_g0.5 | 1.44 | 0.04 | 0.693 | 0.25 |
| nystroem_k256_g2 | 1.44 | 0.04 | 0.693 | 0.34 |
| pca_k64 | 1.43 | 0.04 | 0.692 | 0.26 |
| ica_k64 | 1.42 | 0.04 | 0.692 | 0.26 |
| pca_k128 | 1.41 | 0.04 | 0.691 | 0.50 |
| scvi_k30_bnone | 1.39 | 0.04 | 0.689 | 0.37 |
| scvi_k30_btissue | 1.39 | 0.04 | 0.689 | 0.37 |
| scvi_k10_btissue | 1.36 | 0.04 | 0.687 | 0.43 |
| nmf_k64 | 1.35 | 0.04 | 0.686 | 0.62 |
| nystroem_k64_g2 | 1.34 | 0.04 | 0.685 | 0.31 |
| pca_k32 | 1.33 | 0.04 | 0.684 | 0.30 |
| pca_k256 | 1.31 | 0.04 | 0.682 | 0.82 |
| ica_k16 | 1.17 | 0.04 | 0.671 | 0.30 |
| pca_k16 | 1.17 | 0.04 | 0.671 | 0.30 |
| nmf_k16 | 1.10 | 0.04 | 0.665 | 0.71 |
| rproj_k128_s1 | 0.90 | 0.04 | 0.648 | 0.76 |
| rproj_k128_s0 | 0.87 | 0.04 | 0.645 | 0.70 |
| gmm_k100 | 0.82 | 0.04 | 0.641 | 0.57 |
| gmm_k30 | 0.57 | 0.04 | 0.617 | 0.83 |
| pca_k8 | 0.45 | 0.03 | 0.605 | 0.78 |
| gmm_k10 | 0.21 | 0.03 | 0.581 | 1.23 |
| pca_k4 | -0.12 | 0.03 | 0.544 | 1.31 |
| rproj_k32_s1 | -0.23 | 0.03 | 0.532 | 1.37 |
| rproj_k32_s0 | -0.25 | 0.03 | 0.529 | 1.26 |
| rproj_k8_s0 | -1.72 | 0.03 | 0.335 | 2.93 |
| rproj_k8_s1 | -1.83 | 0.03 | 0.320 | 3.52 |
| depth2 | -2.78 | 0.03 | 0.199 | 6.91 |
| random_k32_s0 | -3.49 | 0.04 | 0.127 | 11.73 |
| random_k32_s1 | -3.53 | 0.04 | 0.124 | 11.90 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.020 | 8.0e-02 | 7424 |
| log_total_counts | -0.196 | 2.3e-65 | 7424 |
| n_genes_by_counts | -0.202 | 7.1e-69 | 7424 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| erythrocyte | 49.0 | 3.69 | 125 |
| CD4-positive, alpha-beta T cell | 834.0 | 1.20 | 1786 |
| mature NK T cell | 785.0 | 0.82 | 1967 |
| basal cell of prostate epithelium | 516.0 | 0.22 | 807 |
| CD8-positive, alpha-beta T cell | 1090.0 | -0.25 | 3034 |
| B cell | 801.0 | -0.31 | 1536 |
| fibroblast | 198.0 | -0.53 | 527 |
| luminal cell of prostate epithelium | 703.0 | -1.14 | 1497 |
| mast cell | 527.0 | -1.47 | 811 |
| smooth muscle cell | 494.0 | -1.78 | 1361 |
| endothelial cell | 542.0 | -1.91 | 1761 |
| macrophage | 885.0 | -2.43 | 2907 |

## stratum_binomial

- items: 102; informative (non-degenerate): 100; nobody passes: 2; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.37, -1.51, -0.51, 0.48, 3.55]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 16, -2: 23, -1: 22, +0: 23, +1: 4, +2: 3, +3: 5, +4: 2, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.89 | 0.03 | 0.698 | 3.76 |
| nystroem_k64_g0.5 | 0.86 | 0.03 | 0.693 | 3.56 |
| nystroem_k256_g2 | 0.85 | 0.03 | 0.693 | 3.16 |
| pca_k64 | 0.85 | 0.03 | 0.692 | 2.98 |
| ica_k64 | 0.84 | 0.03 | 0.692 | 2.93 |
| pca_k128 | 0.84 | 0.03 | 0.691 | 8.22 |
| scvi_k30_bnone | 0.82 | 0.03 | 0.689 | 3.77 |
| scvi_k30_btissue | 0.82 | 0.03 | 0.689 | 3.77 |
| scvi_k10_btissue | 0.80 | 0.03 | 0.687 | 3.38 |
| nmf_k64 | 0.80 | 0.03 | 0.686 | 5.25 |
| nystroem_k64_g2 | 0.79 | 0.03 | 0.685 | 3.36 |
| pca_k32 | 0.79 | 0.03 | 0.684 | 2.87 |
| pca_k256 | 0.77 | 0.03 | 0.682 | 11.93 |
| ica_k16 | 0.69 | 0.03 | 0.671 | 3.70 |
| pca_k16 | 0.69 | 0.03 | 0.671 | 3.67 |
| nmf_k16 | 0.65 | 0.03 | 0.665 | 7.31 |
| rproj_k128_s1 | 0.53 | 0.03 | 0.648 | 3.65 |
| rproj_k128_s0 | 0.51 | 0.03 | 0.645 | 2.62 |
| gmm_k100 | 0.48 | 0.03 | 0.641 | 7.02 |
| gmm_k30 | 0.32 | 0.03 | 0.617 | 12.07 |
| pca_k8 | 0.25 | 0.03 | 0.605 | 13.07 |
| gmm_k10 | 0.10 | 0.03 | 0.581 | 28.70 |
| pca_k4 | -0.12 | 0.03 | 0.544 | 30.12 |
| rproj_k32_s1 | -0.20 | 0.03 | 0.532 | 6.69 |
| rproj_k32_s0 | -0.22 | 0.03 | 0.529 | 9.38 |
| rproj_k8_s0 | -1.36 | 0.03 | 0.335 | 18.85 |
| rproj_k8_s1 | -1.45 | 0.03 | 0.320 | 48.28 |
| depth2 | -2.28 | 0.03 | 0.199 | 82.99 |
| random_k32_s0 | -2.91 | 0.04 | 0.127 | 97.59 |
| random_k32_s1 | -2.94 | 0.04 | 0.124 | 99.72 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.009 | 9.3e-01 | 100 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002367|erythrocyte|SRX21474135 | 7.09 | 0.63 | 0.00 |
| UBERON:0002367|erythrocyte|SRX8890106 | 5.50 | 0.25 | 0.01 |
| UBERON:0002367|mature NK T cell|SRX21474135 | 4.75 | 0.16 | 0.01 |
| UBERON:0002367|erythrocyte|SRX8890105 | 4.21 | 0.12 | 0.02 |
| UBERON:0002367|mast cell|SRX21474135 | 3.66 | 0.17 | 0.04 |
| UBERON:0002367|CD4-positive, alpha-beta T cell|SRX21474135 | 3.54 | 0.10 | 0.04 |
| UBERON:0002367|luminal cell of prostate epithelium|SRX21474135 | 3.33 | 0.16 | 0.05 |
| UBERON:0002367|mature NK T cell|SRX8890106 | 3.31 | 0.08 | 0.05 |
| UBERON:0002367|B cell|SRX21474135 | 3.06 | 0.07 | 0.07 |
| UBERON:0002367|basal cell of prostate epithelium|SRX10168166 | 2.77 | 0.06 | 0.09 |
| UBERON:0002367|B cell|SRX8890106 | 2.67 | 0.14 | 0.10 |
| UBERON:0002367|CD4-positive, alpha-beta T cell|SRX8675114 | 2.10 | 0.05 | 0.16 |
| UBERON:0002367|CD8-positive, alpha-beta T cell|SRX21474135 | 1.84 | 0.05 | 0.19 |
| UBERON:0002367|mature NK T cell|SRX8890105 | 1.50 | 0.05 | 0.25 |
| UBERON:0002367|CD4-positive, alpha-beta T cell|SRX8890105 | 1.38 | 0.04 | 0.27 |

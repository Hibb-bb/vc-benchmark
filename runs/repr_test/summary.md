# Component A summary: repr_test


## cell_level

- items: 698; informative (non-degenerate): 672; nobody passes: 23; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.18, -1.85, -0.88, 1.68, 4.0]; median SE 0.69
- histogram (bin lower edge: count): -6: 0, -5: 13, -4: 35, -3: 75, -2: 184, -1: 130, +0: 48, +1: 34, +2: 77, +3: 61, +4: 15, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k16 | 2.53 | 0.14 | 0.795 | 0.72 |
| ica_k16 | 2.42 | 0.14 | 0.787 | 0.31 |
| pca_k16 | 2.42 | 0.14 | 0.787 | 0.31 |
| gmm_k30 | 2.18 | 0.13 | 0.768 | 1.33 |
| pca_k8 | 2.11 | 0.13 | 0.762 | 0.92 |
| gmm_k100 | 2.09 | 0.13 | 0.761 | 0.89 |
| nystroem_k64_g0.5 | 2.09 | 0.13 | 0.761 | 0.21 |
| nystroem_k64_g2 | 2.05 | 0.13 | 0.758 | 0.46 |
| pca_k128 | 1.91 | 0.13 | 0.746 | 0.34 |
| nystroem_k256_g2 | 1.91 | 0.13 | 0.746 | 0.28 |
| nystroem_k256_g0.5 | 1.88 | 0.13 | 0.744 | 0.22 |
| pca_k256 | 1.86 | 0.13 | 0.742 | 0.45 |
| nmf_k64 | 1.83 | 0.13 | 0.739 | 0.39 |
| pca_k64 | 1.81 | 0.13 | 0.738 | 0.21 |
| pca_k32 | 1.79 | 0.13 | 0.736 | 0.22 |
| ica_k64 | 1.78 | 0.13 | 0.735 | 0.20 |
| rproj_k128_s0 | 1.26 | 0.12 | 0.689 | 0.71 |
| rproj_k128_s1 | 1.23 | 0.12 | 0.686 | 0.78 |
| pca_k4 | 1.01 | 0.12 | 0.666 | 1.75 |
| gmm_k10 | 0.11 | 0.11 | 0.569 | 0.77 |
| rproj_k32_s0 | 0.05 | 0.11 | 0.562 | 1.32 |
| rproj_k32_s1 | -0.07 | 0.11 | 0.546 | 1.27 |
| rproj_k8_s0 | -1.40 | 0.10 | 0.361 | 2.19 |
| rproj_k8_s1 | -1.40 | 0.10 | 0.361 | 3.63 |
| depth2 | -2.99 | 0.12 | 0.156 | 4.71 |
| random_k32_s1 | -3.54 | 0.14 | 0.107 | 5.88 |
| random_k32_s0 | -3.67 | 0.14 | 0.097 | 16.63 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.448 | 1.6e-34 | 672 |
| log_total_counts | -0.200 | 1.7e-07 | 672 |
| n_genes_by_counts | -0.167 | 1.3e-05 | 672 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 99 | -1.86 | 1.06 |
| Epithelium | 25 | -0.05 | 1.22 |
| Germline | 0 | nan | nan |
| Immune | 384 | -0.07 | 2.27 |
| Stromal | 164 | 0.32 | 2.19 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| cd4-positive, alpha-beta t cell | 42.0 | 2.96 | 409 |
| regulatory t cell | 46.0 | 2.91 | 185 |
| melanocyte | 65.0 | 2.17 | 44 |
| t cell | 48.0 | 1.19 | 400 |
| sebum secreting cell | 25.0 | -0.05 | 38 |
| cd8-positive, alpha-beta t cell | 50.0 | -0.11 | 600 |
| smooth muscle cell | 49.0 | -0.69 | 307 |
| fibroblast | 50.0 | -1.11 | 435 |
| neutrophil | 50.0 | -1.16 | 86 |
| mast cell | 50.0 | -1.35 | 319 |
| endothelial cell | 99.0 | -1.86 | 501 |
| macrophage | 98.0 | -2.15 | 570 |

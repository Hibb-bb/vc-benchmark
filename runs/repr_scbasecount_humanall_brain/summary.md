# Component A summary: repr_scbasecount_humanall_brain


## cell_level

- items: 3075; informative (non-degenerate): 2818; nobody passes: 229; everybody passes: 28
- difficulty percentiles 5/25/50/75/95: [-2.57, -2.13, -0.86, 1.17, 3.33]; median SE 0.56
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 72, -3: 652, -2: 644, -1: 490, +0: 213, +1: 290, +2: 281, +3: 176, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | 1.38 | 0.06 | 0.699 | 0.27 |
| scvi_k30_btissue | 1.36 | 0.06 | 0.698 | 0.90 |
| scvi_k30_bnone | 1.36 | 0.06 | 0.698 | 0.90 |
| pca_k128 | 1.34 | 0.06 | 0.695 | 0.37 |
| ica_k64 | 1.33 | 0.06 | 0.694 | 0.25 |
| nystroem_k64_g2 | 1.33 | 0.06 | 0.694 | 0.37 |
| pca_k64 | 1.33 | 0.06 | 0.694 | 0.25 |
| nystroem_k256_g0.5 | 1.32 | 0.06 | 0.694 | 0.37 |
| nystroem_k256_g2 | 1.30 | 0.06 | 0.692 | 0.56 |
| pca_k256 | 1.23 | 0.06 | 0.685 | 0.51 |
| pca_k32 | 1.19 | 0.06 | 0.681 | 0.28 |
| nmf_k64 | 1.14 | 0.06 | 0.676 | 0.52 |
| scvi_k10_btissue | 1.09 | 0.06 | 0.671 | 0.73 |
| ica_k16 | 1.08 | 0.06 | 0.670 | 0.38 |
| pca_k16 | 1.08 | 0.06 | 0.670 | 0.38 |
| nmf_k16 | 1.01 | 0.06 | 0.663 | 0.38 |
| rproj_k128_s1 | 0.78 | 0.05 | 0.638 | 0.61 |
| rproj_k128_s0 | 0.76 | 0.05 | 0.636 | 0.74 |
| gmm_k30 | 0.56 | 0.05 | 0.614 | 1.26 |
| gmm_k100 | 0.45 | 0.05 | 0.602 | 0.89 |
| pca_k8 | 0.42 | 0.05 | 0.598 | 0.69 |
| pca_k4 | -0.03 | 0.05 | 0.544 | 0.81 |
| rproj_k32_s0 | -0.18 | 0.05 | 0.524 | 1.36 |
| gmm_k10 | -0.29 | 0.05 | 0.511 | 1.01 |
| rproj_k32_s1 | -0.32 | 0.05 | 0.507 | 1.11 |
| rproj_k8_s0 | -1.37 | 0.05 | 0.359 | 2.33 |
| rproj_k8_s1 | -1.81 | 0.05 | 0.295 | 2.82 |
| random_k32_s0 | -2.86 | 0.06 | 0.163 | 9.01 |
| random_k32_s1 | -2.86 | 0.06 | 0.163 | 8.97 |
| depth2 | -2.87 | 0.06 | 0.162 | 13.69 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.149 | 2.2e-15 | 2818 |
| log_total_counts | 0.115 | 9.5e-10 | 2818 |
| n_genes_by_counts | 0.094 | 6.1e-07 | 2818 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| ependymal cell | 171.0 | 1.86 | 318 |
| astrocyte | 228.0 | 1.41 | 883 |
| oligodendrocyte precursor cell | 30.0 | 1.20 | 670 |
| vascular associated smooth muscle cell | 189.0 | 1.12 | 597 |
| neuron | 328.0 | 0.32 | 1076 |
| oligodendrocyte | 474.0 | -0.02 | 3647 |
| leukocyte | 500.0 | -0.95 | 2413 |
| pericyte | 100.0 | -1.69 | 498 |
| central nervous system macrophage | 600.0 | -1.72 | 2228 |
| endothelial cell | 198.0 | -1.99 | 498 |

## stratum_binomial

- items: 35; informative (non-degenerate): 35; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.19, -1.71, -0.49, 1.05, 3.87]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 5, -2: 9, -1: 8, +0: 3, +1: 4, +2: 2, +3: 2, +4: 2, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k64_g0.5 | 0.86 | 0.05 | 0.699 | 8.24 |
| scvi_k30_btissue | 0.85 | 0.05 | 0.698 | 21.26 |
| scvi_k30_bnone | 0.85 | 0.05 | 0.698 | 21.26 |
| pca_k128 | 0.83 | 0.05 | 0.695 | 6.34 |
| nystroem_k64_g2 | 0.83 | 0.05 | 0.694 | 9.65 |
| ica_k64 | 0.83 | 0.05 | 0.694 | 6.04 |
| pca_k64 | 0.83 | 0.05 | 0.694 | 5.98 |
| nystroem_k256_g0.5 | 0.82 | 0.05 | 0.694 | 11.00 |
| nystroem_k256_g2 | 0.81 | 0.05 | 0.692 | 11.39 |
| pca_k256 | 0.76 | 0.05 | 0.685 | 5.44 |
| pca_k32 | 0.73 | 0.05 | 0.681 | 6.74 |
| nmf_k64 | 0.69 | 0.05 | 0.676 | 9.64 |
| scvi_k10_btissue | 0.65 | 0.05 | 0.671 | 10.96 |
| ica_k16 | 0.64 | 0.05 | 0.670 | 7.28 |
| pca_k16 | 0.64 | 0.05 | 0.670 | 7.27 |
| nmf_k16 | 0.59 | 0.05 | 0.663 | 6.82 |
| rproj_k128_s1 | 0.41 | 0.05 | 0.638 | 4.52 |
| rproj_k128_s0 | 0.40 | 0.05 | 0.636 | 3.59 |
| gmm_k30 | 0.25 | 0.05 | 0.614 | 38.18 |
| gmm_k100 | 0.17 | 0.05 | 0.602 | 17.09 |
| pca_k8 | 0.14 | 0.05 | 0.598 | 26.22 |
| pca_k4 | -0.20 | 0.04 | 0.544 | 26.20 |
| rproj_k32_s0 | -0.32 | 0.04 | 0.524 | 20.58 |
| gmm_k10 | -0.41 | 0.04 | 0.511 | 37.55 |
| rproj_k32_s1 | -0.43 | 0.04 | 0.507 | 8.85 |
| rproj_k8_s0 | -1.30 | 0.04 | 0.359 | 48.55 |
| rproj_k8_s1 | -1.68 | 0.04 | 0.295 | 41.13 |
| random_k32_s0 | -2.62 | 0.05 | 0.163 | 234.31 |
| random_k32_s1 | -2.62 | 0.05 | 0.163 | 229.70 |
| depth2 | -2.63 | 0.05 | 0.162 | 308.17 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.150 | 3.9e-01 | 35 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000955|leukocyte|SRX9345265 | 4.95 | 0.18 | 0.01 |
| UBERON:0000955|oligodendrocyte precursor cell|SRX23721824 | 4.18 | 0.21 | 0.02 |
| UBERON:0000955|leukocyte|SRX23341379 | 3.74 | 0.22 | 0.03 |
| UBERON:0000955|neuron|SRX11788522 | 3.42 | 0.13 | 0.05 |
| UBERON:0000955|vascular associated smooth muscle cell|SRX9345265 | 2.58 | 0.06 | 0.10 |
| UBERON:0000955|astrocyte|SRX23721824 | 2.30 | 0.06 | 0.13 |
| UBERON:0000955|ependymal cell|SRX9345265 | 1.49 | 0.05 | 0.24 |
| UBERON:0000955|ependymal cell|SRX23341379 | 1.22 | 0.04 | 0.28 |
| UBERON:0000955|astrocyte|SRX9345265 | 1.07 | 0.04 | 0.31 |
| UBERON:0000955|oligodendrocyte|SRX9345265 | 1.02 | 0.04 | 0.32 |
| UBERON:0000955|astrocyte|SRX23341379 | 0.77 | 0.04 | 0.37 |
| UBERON:0000955|oligodendrocyte precursor cell|SRX23341379 | 0.46 | 0.08 | 0.44 |
| UBERON:0000955|oligodendrocyte|SRX9908734 | 0.01 | 0.04 | 0.53 |
| UBERON:0000955|neuron|SRX23341379 | -0.10 | 0.04 | 0.55 |
| UBERON:0000955|oligodendrocyte|SRX23721824 | -0.14 | 0.05 | 0.56 |

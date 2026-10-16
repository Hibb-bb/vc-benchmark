# Component A summary: repr_scbasecount_mouse_brain


## cell_level

- items: 16843; informative (non-degenerate): 13895; nobody passes: 2948; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.36, -2.4, -0.99, 0.47, 2.4]; median SE 0.48
- histogram (bin lower edge: count): -6: 0, -5: 19, -4: 1261, -3: 2864, -2: 2771, -1: 2322, +0: 2291, +1: 1323, +2: 1044, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.10 | 0.02 | 0.515 | 0.54 |
| nystroem_k256_g2 | -0.11 | 0.02 | 0.515 | 0.59 |
| nystroem_k64_g0.5 | -0.22 | 0.02 | 0.501 | 0.39 |
| pca_k128 | -0.24 | 0.02 | 0.498 | 0.49 |
| nmf_k64 | -0.26 | 0.02 | 0.496 | 0.56 |
| ica_k64 | -0.28 | 0.02 | 0.494 | 0.37 |
| pca_k64 | -0.28 | 0.02 | 0.494 | 0.38 |
| pca_k256 | -0.32 | 0.02 | 0.489 | 0.62 |
| nystroem_k64_g2 | -0.33 | 0.02 | 0.487 | 0.55 |
| pca_k32 | -0.39 | 0.02 | 0.481 | 0.40 |
| gmm_k100 | -0.56 | 0.02 | 0.459 | 0.56 |
| ica_k16 | -0.58 | 0.02 | 0.456 | 0.48 |
| rproj_k128_s1 | -0.58 | 0.02 | 0.456 | 0.65 |
| pca_k16 | -0.58 | 0.02 | 0.456 | 0.48 |
| rproj_k128_s0 | -0.61 | 0.02 | 0.452 | 0.66 |
| nmf_k16 | -0.74 | 0.02 | 0.436 | 0.61 |
| gmm_k30 | -0.76 | 0.02 | 0.434 | 0.81 |
| rproj_k32_s0 | -1.01 | 0.02 | 0.401 | 0.83 |
| rproj_k32_s1 | -1.08 | 0.02 | 0.393 | 0.85 |
| pca_k8 | -1.25 | 0.02 | 0.371 | 1.04 |
| gmm_k10 | -1.34 | 0.02 | 0.359 | 1.36 |
| pca_k4 | -1.48 | 0.02 | 0.342 | 1.08 |
| rproj_k8_s1 | -1.95 | 0.02 | 0.282 | 1.55 |
| rproj_k8_s0 | -2.01 | 0.02 | 0.274 | 1.61 |
| depth2 | -2.73 | 0.02 | 0.190 | 4.99 |
| random_k32_s1 | -3.50 | 0.03 | 0.118 | 3.63 |
| random_k32_s0 | -3.51 | 0.03 | 0.117 | 3.58 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.143 | 4.0e-64 | 13895 |
| log_total_counts | -0.228 | 1.6e-163 | 13895 |
| n_genes_by_counts | -0.220 | 1.4e-151 | 13895 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| neuroepithelial stem cell | 1015.0 | 0.25 | 3035 |
| interneuron | 533.0 | 0.23 | 1401 |
| endothelial cell | 1596.0 | 0.10 | 3952 |
| T cell | 440.0 | 0.05 | 1974 |
| neural stem cell | 816.0 | -0.37 | 2036 |
| neuron | 890.0 | -0.38 | 1830 |
| microglial cell | 1861.0 | -0.78 | 4691 |
| Bergmann glial cell | 167.0 | -0.81 | 281 |
| CD8-positive, alpha-beta T cell | 478.0 | -0.91 | 1556 |
| mature NK T cell | 1993.0 | -0.92 | 4919 |
| macrophage | 1063.0 | -1.01 | 2770 |
| oligodendrocyte precursor cell | 528.0 | -1.87 | 1379 |
| ependymal cell | 317.0 | -1.98 | 827 |
| astrocyte | 872.0 | -2.07 | 2393 |
| brain pericyte | 604.0 | -2.13 | 1918 |

## stratum_binomial

- items: 214; informative (non-degenerate): 213; nobody passes: 1; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.54, -1.3, -0.5, 0.98, 4.37]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 3, -3: 20, -2: 54, -1: 49, +0: 35, +1: 16, +2: 12, +3: 8, +4: 9, +5: 4

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.24 | 0.02 | 0.515 | 8.28 |
| nystroem_k256_g2 | -0.24 | 0.02 | 0.515 | 9.45 |
| nystroem_k64_g0.5 | -0.33 | 0.02 | 0.501 | 4.98 |
| pca_k128 | -0.34 | 0.02 | 0.498 | 6.36 |
| nmf_k64 | -0.36 | 0.02 | 0.496 | 6.63 |
| ica_k64 | -0.37 | 0.02 | 0.494 | 5.28 |
| pca_k64 | -0.37 | 0.02 | 0.494 | 5.33 |
| pca_k256 | -0.40 | 0.02 | 0.489 | 7.17 |
| nystroem_k64_g2 | -0.41 | 0.02 | 0.487 | 11.21 |
| pca_k32 | -0.45 | 0.02 | 0.481 | 5.38 |
| gmm_k100 | -0.58 | 0.02 | 0.459 | 10.94 |
| ica_k16 | -0.59 | 0.02 | 0.456 | 8.33 |
| rproj_k128_s1 | -0.60 | 0.02 | 0.456 | 3.44 |
| pca_k16 | -0.60 | 0.02 | 0.456 | 8.30 |
| rproj_k128_s0 | -0.62 | 0.02 | 0.452 | 3.29 |
| nmf_k16 | -0.72 | 0.02 | 0.436 | 10.38 |
| gmm_k30 | -0.73 | 0.02 | 0.434 | 25.31 |
| rproj_k32_s0 | -0.92 | 0.02 | 0.401 | 6.04 |
| rproj_k32_s1 | -0.97 | 0.02 | 0.393 | 6.67 |
| pca_k8 | -1.10 | 0.02 | 0.371 | 33.85 |
| gmm_k10 | -1.17 | 0.02 | 0.359 | 40.44 |
| pca_k4 | -1.28 | 0.02 | 0.342 | 30.77 |
| rproj_k8_s1 | -1.65 | 0.02 | 0.282 | 16.49 |
| rproj_k8_s0 | -1.70 | 0.02 | 0.274 | 15.40 |
| depth2 | -2.31 | 0.02 | 0.190 | 119.65 |
| random_k32_s1 | -3.00 | 0.03 | 0.118 | 59.38 |
| random_k32_s0 | -3.01 | 0.03 | 0.117 | 57.99 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.098 | 1.6e-01 | 213 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000955|T cell|SRX26076718 | 6.82 | 0.82 | 0.00 |
| UBERON:0000955|oligodendrocyte precursor cell|SRX19355853 | 6.82 | 0.82 | 0.00 |
| UBERON:0000955|CD8-positive, alpha-beta T cell|SRX19355853 | 6.30 | 0.64 | 0.00 |
| UBERON:0000955|oligodendrocyte precursor cell|SRX16088103 | 5.96 | 0.54 | 0.00 |
| UBERON:0000955|CD8-positive, alpha-beta T cell|SRX26076718 | 5.77 | 0.64 | 0.00 |
| UBERON:0000955|CD8-positive, alpha-beta T cell|SRX25166448 | 5.70 | 0.48 | 0.00 |
| UBERON:0000955|CD8-positive, alpha-beta T cell|SRX27471551 | 5.06 | 0.65 | 0.00 |
| UBERON:0000955|interneuron|SRX5584534 | 4.54 | 0.48 | 0.00 |
| UBERON:0000955|T cell|SRX25634759 | 4.45 | 0.43 | 0.01 |
| UBERON:0000955|interneuron|SRX18122875 | 4.44 | 0.26 | 0.01 |
| UBERON:0000955|interneuron|SRX19355853 | 4.44 | 0.26 | 0.01 |
| UBERON:0000955|interneuron|SRX27471562 | 4.32 | 0.24 | 0.01 |
| UBERON:0000955|Bergmann glial cell|SRX14746983 | 4.23 | 0.44 | 0.01 |
| UBERON:0000955|Bergmann glial cell|SRX12705136 | 4.09 | 0.40 | 0.01 |
| UBERON:0000955|T cell|SRX14746983 | 4.04 | 0.44 | 0.01 |

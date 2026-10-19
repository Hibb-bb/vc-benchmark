# Component A summary: repr_scbasecount_human200_skin


## cell_level

- items: 28812; informative (non-degenerate): 25708; nobody passes: 3104; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.97, -2.32, -0.8, 1.11, 2.99]; median SE 0.51
- histogram (bin lower edge: count): -6: 0, -5: 3, -4: 1273, -3: 7497, -2: 3071, -1: 3262, +0: 3708, +1: 3989, +2: 2905, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.41 | 0.02 | 0.572 | 0.43 |
| scvi_k30_btissue | 0.34 | 0.02 | 0.564 | 0.64 |
| scvi_k30_bnone | 0.34 | 0.02 | 0.564 | 0.64 |
| nystroem_k256_g2 | 0.33 | 0.02 | 0.563 | 0.50 |
| nystroem_k64_g0.5 | 0.31 | 0.02 | 0.560 | 0.35 |
| pca_k256 | 0.27 | 0.02 | 0.556 | 0.46 |
| ica_k64 | 0.27 | 0.02 | 0.555 | 0.34 |
| pca_k64 | 0.27 | 0.02 | 0.555 | 0.34 |
| pca_k128 | 0.26 | 0.02 | 0.555 | 0.39 |
| pca_k32 | 0.21 | 0.02 | 0.548 | 0.37 |
| nystroem_k64_g2 | 0.14 | 0.02 | 0.540 | 0.48 |
| pca_k16 | 0.09 | 0.02 | 0.535 | 0.40 |
| ica_k16 | 0.09 | 0.02 | 0.535 | 0.40 |
| nmf_k64 | 0.07 | 0.02 | 0.533 | 0.55 |
| scvi_k10_btissue | -0.08 | 0.02 | 0.514 | 0.97 |
| gmm_k100 | -0.09 | 0.02 | 0.513 | 0.63 |
| gmm_k30 | -0.23 | 0.02 | 0.496 | 0.83 |
| pca_k8 | -0.28 | 0.02 | 0.490 | 0.61 |
| rproj_k128_s1 | -0.37 | 0.02 | 0.479 | 0.85 |
| rproj_k128_s0 | -0.38 | 0.02 | 0.478 | 0.86 |
| nmf_k16 | -0.48 | 0.02 | 0.466 | 0.81 |
| gmm_k10 | -0.67 | 0.02 | 0.442 | 0.90 |
| pca_k4 | -0.83 | 0.02 | 0.422 | 0.96 |
| rproj_k32_s0 | -1.35 | 0.02 | 0.358 | 1.38 |
| rproj_k32_s1 | -1.52 | 0.02 | 0.336 | 1.59 |
| rproj_k8_s0 | -2.64 | 0.02 | 0.200 | 3.42 |
| rproj_k8_s1 | -2.74 | 0.02 | 0.189 | 3.74 |
| depth2 | -2.93 | 0.02 | 0.169 | 7.82 |
| random_k32_s0 | -3.58 | 0.02 | 0.109 | 11.34 |
| random_k32_s1 | -3.58 | 0.02 | 0.109 | 11.44 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | 0.057 | 8.5e-20 | 25708 |
| log_total_counts | -0.378 | 0.0e+00 | 25708 |
| n_genes_by_counts | -0.378 | 0.0e+00 | 25708 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| regulatory T cell | 92.0 | 1.51 | 140 |
| neutrophil | 2098.0 | 1.24 | 5540 |
| CD4-positive, alpha-beta T cell | 1274.0 | 0.98 | 4953 |
| Langerhans cell | 25.0 | 0.95 | 328 |
| CD8-positive, alpha-beta T cell | 3099.0 | 0.37 | 9221 |
| T cell | 3196.0 | 0.31 | 8538 |
| melanocyte | 2221.0 | 0.21 | 6170 |
| plasma cell | 165.0 | -0.17 | 596 |
| sebocyte | 1998.0 | -0.68 | 4876 |
| macrophage | 2228.0 | -1.18 | 5123 |
| smooth muscle cell | 2398.0 | -1.19 | 5299 |
| mast cell | 819.0 | -1.84 | 1169 |
| fibroblast | 2938.0 | -1.96 | 6809 |
| endothelial cell | 3149.0 | -2.01 | 7667 |

## stratum_binomial

- items: 346; informative (non-degenerate): 344; nobody passes: 2; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.15, -1.29, -0.06, 0.91, 2.8]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 29, -2: 74, -1: 75, +0: 87, +1: 45, +2: 21, +3: 5, +4: 4, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.18 | 0.01 | 0.572 | 4.49 |
| scvi_k30_btissue | 0.13 | 0.01 | 0.564 | 6.93 |
| scvi_k30_bnone | 0.13 | 0.01 | 0.564 | 6.93 |
| nystroem_k256_g2 | 0.13 | 0.01 | 0.563 | 4.97 |
| nystroem_k64_g0.5 | 0.11 | 0.01 | 0.560 | 3.61 |
| pca_k256 | 0.09 | 0.01 | 0.556 | 2.77 |
| ica_k64 | 0.09 | 0.01 | 0.555 | 2.53 |
| pca_k64 | 0.08 | 0.01 | 0.555 | 2.53 |
| pca_k128 | 0.08 | 0.01 | 0.555 | 2.59 |
| pca_k32 | 0.04 | 0.01 | 0.548 | 2.94 |
| nystroem_k64_g2 | -0.00 | 0.01 | 0.540 | 5.24 |
| pca_k16 | -0.03 | 0.01 | 0.535 | 4.32 |
| ica_k16 | -0.03 | 0.01 | 0.535 | 4.32 |
| nmf_k64 | -0.04 | 0.01 | 0.533 | 3.92 |
| scvi_k10_btissue | -0.15 | 0.01 | 0.514 | 14.24 |
| gmm_k100 | -0.16 | 0.01 | 0.513 | 8.35 |
| gmm_k30 | -0.25 | 0.01 | 0.496 | 14.04 |
| pca_k8 | -0.29 | 0.01 | 0.490 | 9.07 |
| rproj_k128_s1 | -0.35 | 0.01 | 0.479 | 2.44 |
| rproj_k128_s0 | -0.35 | 0.01 | 0.478 | 3.84 |
| nmf_k16 | -0.42 | 0.01 | 0.466 | 10.64 |
| gmm_k10 | -0.56 | 0.01 | 0.442 | 18.32 |
| pca_k4 | -0.67 | 0.01 | 0.422 | 17.86 |
| rproj_k32_s0 | -1.04 | 0.01 | 0.358 | 4.98 |
| rproj_k32_s1 | -1.18 | 0.01 | 0.336 | 7.27 |
| rproj_k8_s0 | -2.08 | 0.02 | 0.200 | 21.32 |
| rproj_k8_s1 | -2.17 | 0.02 | 0.189 | 21.98 |
| depth2 | -2.34 | 0.02 | 0.169 | 133.30 |
| random_k32_s0 | -2.92 | 0.02 | 0.109 | 180.79 |
| random_k32_s1 | -2.92 | 0.02 | 0.109 | 195.66 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.116 | 3.1e-02 | 344 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX28908424 | 7.28 | 0.81 | 0.00 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX28908423 | 6.91 | 0.82 | 0.00 |
| UBERON:0002097|regulatory T cell|SRX7974889 | 6.28 | 0.83 | 0.00 |
| UBERON:0002097|mature NK T cell|SRX11781407 | 5.00 | 0.55 | 0.00 |
| UBERON:0002097|regulatory T cell|SRX28363575 | 4.96 | 0.55 | 0.00 |
| UBERON:0002097|regulatory T cell|SRX20125352 | 4.36 | 0.35 | 0.01 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX10121870 | 4.35 | 0.19 | 0.01 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX28908463 | 4.09 | 0.26 | 0.01 |
| UBERON:0002097|regulatory T cell|SRX18267533 | 3.91 | 0.21 | 0.01 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX28768967 | 3.72 | 0.30 | 0.02 |
| UBERON:0002097|neutrophil|SRX20125352 | 3.71 | 0.20 | 0.02 |
| UBERON:0002097|mature NK T cell|SRX11095720 | 3.40 | 0.24 | 0.02 |
| UBERON:0002097|CD4-positive, alpha-beta T cell|SRX26536507 | 3.05 | 0.10 | 0.03 |
| UBERON:0002097|melanocyte|SRX19961073 | 2.94 | 0.12 | 0.04 |
| UBERON:0002097|neutrophil|SRX26536507 | 2.92 | 0.10 | 0.04 |

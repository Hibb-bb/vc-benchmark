# Component A summary: repr_pooled_v2


## cell_level

- items: 249474; informative (non-degenerate): 228775; nobody passes: 19651; everybody passes: 1048
- difficulty percentiles 5/25/50/75/95: [-3.29, -1.77, -0.77, 1.1, 2.99]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 982, -4: 11149, -3: 42711, -2: 42553, -1: 43505, +0: 30465, +1: 26284, +2: 21806, +3: 9320, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 1.16 | 0.01 | 0.673 | 0.43 |
| scvi_k30_bnone | 1.16 | 0.01 | 0.673 | 0.68 |
| pca_k128 | 1.16 | 0.01 | 0.673 | 0.44 |
| pca_k64 | 1.14 | 0.01 | 0.671 | 0.34 |
| ica_k64 | 1.14 | 0.01 | 0.671 | 0.34 |
| scvi_k30_btissue | 1.13 | 0.01 | 0.670 | 0.70 |
| nystroem_k64_g0.5 | 1.13 | 0.01 | 0.669 | 0.35 |
| pca_k256 | 1.10 | 0.01 | 0.667 | 0.53 |
| nystroem_k256_g2 | 1.06 | 0.01 | 0.662 | 0.47 |
| pca_k32 | 0.97 | 0.01 | 0.652 | 0.40 |
| scvi_k10_btissue | 0.85 | 0.01 | 0.639 | 0.76 |
| nmf_k64 | 0.83 | 0.01 | 0.637 | 0.65 |
| nystroem_k64_g2 | 0.79 | 0.01 | 0.632 | 0.64 |
| pca_k16 | 0.47 | 0.01 | 0.594 | 0.51 |
| ica_k16 | 0.47 | 0.01 | 0.594 | 0.51 |
| rproj_k128_s1 | 0.41 | 0.01 | 0.586 | 0.88 |
| rproj_k128_s0 | 0.39 | 0.01 | 0.584 | 0.86 |
| gmm_k100 | 0.19 | 0.01 | 0.560 | 0.83 |
| nmf_k16 | 0.00 | 0.01 | 0.535 | 0.94 |
| pca_k8 | -0.39 | 0.01 | 0.483 | 0.93 |
| gmm_k30 | -0.41 | 0.01 | 0.480 | 1.07 |
| rproj_k32_s0 | -0.84 | 0.01 | 0.421 | 1.38 |
| rproj_k32_s1 | -0.86 | 0.01 | 0.418 | 1.44 |
| pca_k4 | -1.24 | 0.01 | 0.365 | 1.64 |
| gmm_k10 | -1.70 | 0.01 | 0.301 | 2.26 |
| rproj_k8_s0 | -2.43 | 0.01 | 0.209 | 3.05 |
| rproj_k8_s1 | -2.44 | 0.01 | 0.208 | 3.24 |
| depth2 | -2.97 | 0.01 | 0.151 | 7.59 |
| random_k32_s1 | -3.91 | 0.01 | 0.079 | 11.68 |
| random_k32_s0 | -3.92 | 0.01 | 0.078 | 11.62 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.068 | 2.6e-231 | 228775 |
| log_total_counts | -0.146 | 0.0e+00 | 228775 |
| n_genes_by_counts | -0.135 | 0.0e+00 | 228775 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 1772 | 0.01 | 1.55 |
| Epithelium | 2434 | -0.21 | 1.69 |
| Immune | 10383 | -0.36 | 1.87 |
| Neural | 100 | -1.10 | 0.60 |
| Stromal | 3067 | 0.13 | 1.93 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Goblet (bronchial) | 82.0 | 3.13 | 128 |
| mural cell | 44.0 | 3.04 | 128 |
| naive thymus-derived cd8-positive, alpha-beta t cell | 24.0 | 2.94 | 712 |
| activated cd8-positive, alpha-beta t cell | 60.0 | 2.74 | 361 |
| mesenchymal stem cell of adipose tissue | 45.0 | 2.70 | 445 |
| muscle cell | 39.0 | 2.59 | 132 |
| innate lymphoid cell | 26.0 | 2.55 | 95 |
| t cell | 139.0 | 2.48 | 2270 |
| activated cd4-positive, alpha-beta t cell | 38.0 | 2.46 | 225 |
| SM activated stress response | 56.0 | 2.40 | 23 |
| fibroblast of breast | 34.0 | 2.40 | 200 |
| schwann cell | 21.0 | 2.38 | 273 |
| regulatory T cell | 34.0 | 2.36 | 177 |
| gamma-delta t cell | 69.0 | 2.33 | 452 |
| DC | 130.0 | 2.33 | 366 |

## stratum_binomial

- items: 4374; informative (non-degenerate): 4351; nobody passes: 23; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.19, -1.16, -0.24, 0.77, 2.98]; median SE 0.06
- histogram (bin lower edge: count): -6: 4, -5: 19, -4: 18, -3: 289, -2: 954, -1: 1172, +0: 985, +1: 490, +2: 206, +3: 87, +4: 70, +5: 33

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.89 | 0.01 | 0.673 | 3.91 |
| scvi_k30_bnone | 0.89 | 0.01 | 0.673 | 5.17 |
| pca_k128 | 0.89 | 0.01 | 0.673 | 4.16 |
| pca_k64 | 0.87 | 0.01 | 0.671 | 3.44 |
| ica_k64 | 0.87 | 0.01 | 0.671 | 3.42 |
| scvi_k30_btissue | 0.87 | 0.01 | 0.670 | 5.56 |
| nystroem_k64_g0.5 | 0.86 | 0.01 | 0.669 | 3.37 |
| pca_k256 | 0.85 | 0.01 | 0.667 | 3.81 |
| nystroem_k256_g2 | 0.82 | 0.01 | 0.662 | 4.09 |
| pca_k32 | 0.75 | 0.01 | 0.652 | 3.26 |
| scvi_k10_btissue | 0.67 | 0.01 | 0.639 | 6.80 |
| nmf_k64 | 0.66 | 0.01 | 0.637 | 4.91 |
| nystroem_k64_g2 | 0.62 | 0.00 | 0.632 | 7.67 |
| pca_k16 | 0.39 | 0.00 | 0.594 | 4.58 |
| ica_k16 | 0.39 | 0.00 | 0.594 | 4.58 |
| rproj_k128_s1 | 0.35 | 0.00 | 0.586 | 4.48 |
| rproj_k128_s0 | 0.34 | 0.00 | 0.584 | 4.00 |
| gmm_k100 | 0.19 | 0.00 | 0.560 | 10.40 |
| nmf_k16 | 0.05 | 0.00 | 0.535 | 9.85 |
| pca_k8 | -0.24 | 0.00 | 0.483 | 9.79 |
| gmm_k30 | -0.26 | 0.00 | 0.480 | 20.51 |
| rproj_k32_s0 | -0.59 | 0.00 | 0.421 | 6.84 |
| rproj_k32_s1 | -0.61 | 0.00 | 0.418 | 7.58 |
| pca_k4 | -0.92 | 0.00 | 0.365 | 19.25 |
| gmm_k10 | -1.30 | 0.01 | 0.301 | 41.08 |
| rproj_k8_s0 | -1.93 | 0.01 | 0.209 | 16.72 |
| rproj_k8_s1 | -1.94 | 0.01 | 0.208 | 14.73 |
| depth2 | -2.41 | 0.01 | 0.151 | 74.03 |
| random_k32_s1 | -3.28 | 0.01 | 0.079 | 94.53 |
| random_k32_s0 | -3.29 | 0.01 | 0.078 | 93.99 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.204 | 3.4e-42 | 4351 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_human_lung::UBERON:0002048|mature NK T cell|SRX13061245 | 7.92 | 0.80 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|neutrophil|SRX27532049 | 7.92 | 0.80 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|plasma cell|SRX10112709 | 7.92 | 0.80 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0000029|natural killer cell|ERX12093805 | 7.74 | 0.80 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|intermediate monocyte|SRX13549256 | 7.47 | 0.81 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|plasma cell|SRX10112705 | 7.42 | 0.63 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX15829407 | 7.42 | 0.63 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0001969|naive thymus-derived CD4-positive, alpha-beta T cell|SRX10977992 | 7.42 | 0.63 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX25183951 | 7.42 | 0.63 | 0.00 |
| repr_pool_v0::Testis|stromal cell|TSP25 | 7.25 | 0.81 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX15829410 | 7.08 | 0.53 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX7691515 | 7.08 | 0.53 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|SRX26161096 | 7.08 | 0.53 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX24338654 | 6.83 | 0.47 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|classical monocyte|SRX10104846 | 6.83 | 0.47 | 0.00 |

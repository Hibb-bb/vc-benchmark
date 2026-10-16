# Component A summary: repr_pooled_scbasecount_human_v0


## cell_level

- items: 103046; informative (non-degenerate): 89781; nobody passes: 13126; everybody passes: 139
- difficulty percentiles 5/25/50/75/95: [-3.08, -2.0, -0.89, 0.85, 2.75]; median SE 0.47
- histogram (bin lower edge: count): -6: 0, -5: 325, -4: 7999, -3: 18280, -2: 16534, -1: 12526, +0: 12807, +1: 11284, +2: 10026, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k64 | 0.10 | 0.01 | 0.538 | 0.37 |
| pca_k128 | 0.10 | 0.01 | 0.537 | 0.44 |
| ica_k64 | 0.09 | 0.01 | 0.537 | 0.37 |
| nystroem_k64_g0.5 | 0.09 | 0.01 | 0.537 | 0.37 |
| nystroem_k256_g0.5 | 0.08 | 0.01 | 0.535 | 0.44 |
| scvi_k30_bnone | 0.08 | 0.01 | 0.535 | 0.67 |
| scvi_k30_btissue | 0.06 | 0.01 | 0.533 | 0.67 |
| pca_k256 | 0.04 | 0.01 | 0.531 | 0.50 |
| nystroem_k256_g2 | 0.04 | 0.01 | 0.530 | 0.47 |
| pca_k32 | 0.01 | 0.01 | 0.526 | 0.40 |
| nmf_k64 | -0.08 | 0.01 | 0.515 | 0.61 |
| nystroem_k64_g2 | -0.14 | 0.01 | 0.507 | 0.54 |
| scvi_k10_btissue | -0.22 | 0.01 | 0.498 | 0.78 |
| ica_k16 | -0.26 | 0.01 | 0.492 | 0.45 |
| pca_k16 | -0.27 | 0.01 | 0.492 | 0.45 |
| gmm_k100 | -0.42 | 0.01 | 0.472 | 0.79 |
| nmf_k16 | -0.49 | 0.01 | 0.462 | 0.82 |
| rproj_k128_s1 | -0.54 | 0.01 | 0.456 | 0.89 |
| rproj_k128_s0 | -0.57 | 0.01 | 0.452 | 0.83 |
| gmm_k30 | -0.81 | 0.01 | 0.421 | 0.98 |
| pca_k8 | -0.83 | 0.01 | 0.418 | 0.81 |
| rproj_k32_s0 | -1.43 | 0.01 | 0.340 | 1.30 |
| rproj_k32_s1 | -1.47 | 0.01 | 0.335 | 1.39 |
| pca_k4 | -1.49 | 0.01 | 0.332 | 1.39 |
| gmm_k10 | -1.71 | 0.01 | 0.303 | 1.68 |
| rproj_k8_s0 | -2.50 | 0.01 | 0.207 | 2.37 |
| rproj_k8_s1 | -2.65 | 0.01 | 0.191 | 2.70 |
| depth2 | -2.73 | 0.01 | 0.182 | 5.15 |
| random_k32_s0 | -3.46 | 0.01 | 0.115 | 6.40 |
| random_k32_s1 | -3.46 | 0.01 | 0.115 | 6.47 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.011 | 7.1e-04 | 89781 |
| log_total_counts | -0.194 | 0.0e+00 | 89781 |
| n_genes_by_counts | -0.168 | 0.0e+00 | 89781 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| regulatory T cell | 34.0 | 1.49 | 177 |
| common myeloid progenitor | 727.0 | 0.56 | 1456 |
| mature NK T cell | 1200.0 | 0.56 | 170 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 2307.0 | 0.53 | 5349 |
| plasmacytoid dendritic cell | 58.0 | 0.38 | 710 |
| intermediate monocyte | 1435.0 | 0.36 | 606 |
| neutrophil | 2028.0 | 0.21 | 1606 |
| endothelial cell of artery | 600.0 | 0.09 | 495 |
| CD8-positive, alpha-beta T cell | 10989.0 | 0.07 | 5801 |
| T cell | 2080.0 | 0.04 | 325 |
| alveolar adventitial fibroblast | 366.0 | 0.03 | 188 |
| non-classical monocyte | 775.0 | -0.01 | 155 |
| club cell | 167.0 | -0.09 | 292 |
| natural killer cell | 5200.0 | -0.12 | 6347 |
| classical monocyte | 2074.0 | -0.14 | 3130 |

## stratum_binomial

- items: 1313; informative (non-degenerate): 1296; nobody passes: 17; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.41, -1.32, -0.37, 0.73, 3.73]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 12, -3: 125, -2: 269, -1: 372, +0: 239, +1: 119, +2: 60, +3: 46, +4: 30, +5: 12

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k64 | -0.14 | 0.01 | 0.538 | 5.33 |
| pca_k128 | -0.14 | 0.01 | 0.537 | 6.54 |
| ica_k64 | -0.15 | 0.01 | 0.537 | 5.31 |
| nystroem_k64_g0.5 | -0.15 | 0.01 | 0.537 | 5.25 |
| nystroem_k256_g0.5 | -0.16 | 0.01 | 0.535 | 5.30 |
| scvi_k30_bnone | -0.16 | 0.01 | 0.535 | 8.34 |
| scvi_k30_btissue | -0.17 | 0.01 | 0.533 | 8.28 |
| pca_k256 | -0.18 | 0.01 | 0.531 | 5.00 |
| nystroem_k256_g2 | -0.19 | 0.01 | 0.530 | 5.89 |
| pca_k32 | -0.21 | 0.01 | 0.526 | 4.74 |
| nmf_k64 | -0.27 | 0.01 | 0.515 | 7.15 |
| nystroem_k64_g2 | -0.32 | 0.01 | 0.507 | 8.35 |
| scvi_k10_btissue | -0.37 | 0.01 | 0.498 | 10.82 |
| ica_k16 | -0.40 | 0.01 | 0.492 | 6.08 |
| pca_k16 | -0.41 | 0.01 | 0.492 | 6.08 |
| gmm_k100 | -0.52 | 0.01 | 0.472 | 12.79 |
| nmf_k16 | -0.57 | 0.01 | 0.462 | 12.86 |
| rproj_k128_s1 | -0.60 | 0.01 | 0.456 | 7.45 |
| rproj_k128_s0 | -0.63 | 0.01 | 0.452 | 5.38 |
| gmm_k30 | -0.81 | 0.01 | 0.421 | 22.91 |
| pca_k8 | -0.82 | 0.01 | 0.418 | 13.64 |
| rproj_k32_s0 | -1.27 | 0.01 | 0.340 | 9.95 |
| rproj_k32_s1 | -1.31 | 0.01 | 0.335 | 11.85 |
| pca_k4 | -1.32 | 0.01 | 0.332 | 27.02 |
| gmm_k10 | -1.49 | 0.01 | 0.303 | 47.82 |
| rproj_k8_s0 | -2.15 | 0.01 | 0.207 | 21.59 |
| rproj_k8_s1 | -2.27 | 0.01 | 0.191 | 21.18 |
| depth2 | -2.34 | 0.01 | 0.182 | 85.53 |
| random_k32_s0 | -2.98 | 0.01 | 0.115 | 90.76 |
| random_k32_s1 | -2.99 | 0.01 | 0.115 | 91.81 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.183 | 3.2e-11 | 1296 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_human_liver::UBERON:0002107|plasma cell|SRX10112709 | 7.05 | 0.82 | 0.00 |
| repr_scbasecount_human_lung::UBERON:0002048|mature NK T cell|SRX13061245 | 7.05 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|neutrophil|SRX27532049 | 7.05 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0000029|natural killer cell|ERX12093805 | 6.87 | 0.82 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|intermediate monocyte|SRX13549256 | 6.60 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0001969|naive thymus-derived CD4-positive, alpha-beta T cell|SRX10977992 | 6.53 | 0.64 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX25183951 | 6.53 | 0.64 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX15829407 | 6.53 | 0.64 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|plasma cell|SRX10112705 | 6.53 | 0.64 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0000029|naive thymus-derived CD4-positive, alpha-beta T cell|SRX26161096 | 6.19 | 0.54 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX15829410 | 6.19 | 0.54 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX7691515 | 6.19 | 0.54 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|classical monocyte|SRX10104848 | 5.94 | 0.48 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX24338654 | 5.94 | 0.48 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|classical monocyte|SRX10104846 | 5.94 | 0.48 | 0.00 |

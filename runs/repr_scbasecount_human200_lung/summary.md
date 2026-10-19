# Component A summary: repr_scbasecount_human200_lung


## cell_level

- items: 64635; informative (non-degenerate): 60204; nobody passes: 4329; everybody passes: 102
- difficulty percentiles 5/25/50/75/95: [-3.04, -1.84, -0.76, 1.13, 3.19]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 408, -4: 4885, -3: 7949, -2: 12187, -1: 11902, +0: 7459, +1: 5798, +2: 5290, +3: 4326, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 1.44 | 0.01 | 0.702 | 0.38 |
| pca_k128 | 1.44 | 0.01 | 0.701 | 0.36 |
| pca_k256 | 1.42 | 0.01 | 0.699 | 0.42 |
| pca_k64 | 1.38 | 0.01 | 0.696 | 0.29 |
| ica_k64 | 1.38 | 0.01 | 0.696 | 0.29 |
| nystroem_k64_g0.5 | 1.35 | 0.01 | 0.693 | 0.30 |
| nystroem_k256_g2 | 1.32 | 0.01 | 0.690 | 0.40 |
| pca_k32 | 1.19 | 0.01 | 0.676 | 0.33 |
| scvi_k30_bnone | 1.14 | 0.01 | 0.671 | 0.67 |
| scvi_k30_btissue | 1.14 | 0.01 | 0.671 | 0.67 |
| nmf_k64 | 1.10 | 0.01 | 0.666 | 0.54 |
| nystroem_k64_g2 | 1.06 | 0.01 | 0.662 | 0.48 |
| pca_k16 | 0.90 | 0.01 | 0.644 | 0.40 |
| ica_k16 | 0.90 | 0.01 | 0.644 | 0.41 |
| rproj_k128_s0 | 0.66 | 0.01 | 0.618 | 0.76 |
| rproj_k128_s1 | 0.61 | 0.01 | 0.611 | 0.82 |
| scvi_k10_btissue | 0.39 | 0.01 | 0.585 | 0.91 |
| gmm_k100 | 0.28 | 0.01 | 0.572 | 0.85 |
| nmf_k16 | 0.08 | 0.01 | 0.546 | 0.92 |
| pca_k8 | 0.02 | 0.01 | 0.538 | 1.06 |
| gmm_k30 | 0.01 | 0.01 | 0.538 | 0.99 |
| rproj_k32_s0 | -0.53 | 0.01 | 0.466 | 1.36 |
| rproj_k32_s1 | -0.69 | 0.01 | 0.444 | 1.41 |
| pca_k4 | -0.88 | 0.01 | 0.417 | 1.60 |
| gmm_k10 | -1.56 | 0.01 | 0.322 | 2.19 |
| rproj_k8_s0 | -2.12 | 0.01 | 0.247 | 3.66 |
| rproj_k8_s1 | -2.18 | 0.01 | 0.241 | 3.18 |
| depth2 | -2.60 | 0.01 | 0.191 | 8.83 |
| random_k32_s0 | -3.70 | 0.02 | 0.092 | 17.35 |
| random_k32_s1 | -3.70 | 0.02 | 0.092 | 18.02 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.021 | 3.1e-07 | 60204 |
| log_total_counts | -0.230 | 0.0e+00 | 60204 |
| n_genes_by_counts | -0.210 | 0.0e+00 | 60204 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mature NK T cell | 189.0 | 2.95 | 770 |
| neutrophil | 409.0 | 1.57 | 220 |
| classical monocyte | 2238.0 | 1.33 | 8202 |
| club cell | 522.0 | 1.26 | 979 |
| intermediate monocyte | 2610.0 | 0.96 | 9583 |
| alveolar adventitial fibroblast | 1312.0 | 0.63 | 2627 |
| CD8-positive, alpha-beta T cell | 2404.0 | 0.63 | 4556 |
| B cell | 6301.0 | 0.31 | 20974 |
| plasma cell | 5983.0 | 0.23 | 16346 |
| endothelial cell of artery | 1978.0 | 0.17 | 2727 |
| pericyte | 1195.0 | 0.12 | 1909 |
| basal cell | 2164.0 | 0.08 | 2640 |
| natural killer cell | 1288.0 | 0.08 | 2273 |
| bronchial smooth muscle cell | 1150.0 | -0.07 | 2111 |
| capillary endothelial cell | 2699.0 | -0.19 | 5862 |

## stratum_binomial

- items: 883; informative (non-degenerate): 880; nobody passes: 3; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.15, -1.07, -0.16, 0.84, 2.59]; median SE 0.05
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 63, -2: 171, -1: 235, +0: 218, +1: 131, +2: 27, +3: 20, +4: 8, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | 0.94 | 0.01 | 0.702 | 3.68 |
| pca_k128 | 0.93 | 0.01 | 0.701 | 2.87 |
| pca_k256 | 0.92 | 0.01 | 0.699 | 2.82 |
| pca_k64 | 0.90 | 0.01 | 0.696 | 2.75 |
| ica_k64 | 0.90 | 0.01 | 0.696 | 2.75 |
| nystroem_k64_g0.5 | 0.88 | 0.01 | 0.693 | 3.23 |
| nystroem_k256_g2 | 0.86 | 0.01 | 0.690 | 3.52 |
| pca_k32 | 0.77 | 0.01 | 0.676 | 3.00 |
| scvi_k30_bnone | 0.74 | 0.01 | 0.671 | 4.95 |
| scvi_k30_btissue | 0.74 | 0.01 | 0.671 | 4.95 |
| nmf_k64 | 0.72 | 0.01 | 0.666 | 3.91 |
| nystroem_k64_g2 | 0.69 | 0.01 | 0.662 | 4.39 |
| pca_k16 | 0.58 | 0.01 | 0.644 | 3.86 |
| ica_k16 | 0.58 | 0.01 | 0.644 | 3.87 |
| rproj_k128_s0 | 0.43 | 0.01 | 0.618 | 3.52 |
| rproj_k128_s1 | 0.39 | 0.01 | 0.611 | 3.67 |
| scvi_k10_btissue | 0.25 | 0.01 | 0.585 | 9.81 |
| gmm_k100 | 0.17 | 0.01 | 0.572 | 11.59 |
| nmf_k16 | 0.03 | 0.01 | 0.546 | 15.69 |
| pca_k8 | -0.01 | 0.01 | 0.538 | 11.56 |
| gmm_k30 | -0.01 | 0.01 | 0.538 | 19.31 |
| rproj_k32_s0 | -0.40 | 0.01 | 0.466 | 5.06 |
| rproj_k32_s1 | -0.51 | 0.01 | 0.444 | 5.72 |
| pca_k4 | -0.66 | 0.01 | 0.417 | 19.66 |
| gmm_k10 | -1.19 | 0.01 | 0.322 | 35.81 |
| rproj_k8_s0 | -1.66 | 0.01 | 0.247 | 21.36 |
| rproj_k8_s1 | -1.71 | 0.01 | 0.241 | 14.48 |
| depth2 | -2.07 | 0.01 | 0.191 | 74.75 |
| random_k32_s0 | -3.04 | 0.01 | 0.092 | 140.55 |
| random_k32_s1 | -3.05 | 0.01 | 0.092 | 144.83 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.031 | 3.6e-01 | 880 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002048|mature NK T cell|SRX13198727 | 6.55 | 0.54 | 0.00 |
| UBERON:0002048|mature NK T cell|SRX22996317 | 6.48 | 0.64 | 0.00 |
| UBERON:0002048|endothelial cell of artery|SRX9127142 | 6.22 | 0.43 | 0.00 |
| UBERON:0002048|mature NK T cell|SRX10425169 | 6.10 | 0.64 | 0.00 |
| UBERON:0002048|capillary endothelial cell|SRX9276335 | 6.05 | 0.54 | 0.00 |
| UBERON:0002048|mature NK T cell|SRX22996309 | 5.69 | 0.30 | 0.00 |
| UBERON:0002048|capillary endothelial cell|SRX13061245 | 4.97 | 0.27 | 0.01 |
| UBERON:0002048|mature NK T cell|SRX25038170 | 4.82 | 0.20 | 0.01 |
| UBERON:0002048|basal cell|SRX19704153 | 4.59 | 0.33 | 0.01 |
| UBERON:0002048|mature NK T cell|SRX17689207 | 4.49 | 0.31 | 0.02 |
| UBERON:0002048|capillary endothelial cell|SRX9276299 | 4.32 | 0.18 | 0.02 |
| UBERON:0002048|mature NK T cell|SRX13198726 | 4.28 | 0.27 | 0.02 |
| UBERON:0002048|pulmonary alveolar type 2 cell|SRX9127144 | 4.23 | 0.13 | 0.02 |
| UBERON:0002048|mature NK T cell|SRX19704153 | 4.14 | 0.13 | 0.02 |
| UBERON:0002048|endothelial cell of artery|SRX9849885 | 3.94 | 0.11 | 0.03 |

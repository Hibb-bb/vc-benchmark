# Component A summary: repr_hlca_core_study


## cell_level

- items: 32221; informative (non-degenerate): 30839; nobody passes: 636; everybody passes: 746
- difficulty percentiles 5/25/50/75/95: [-3.16, -1.42, -0.3, 1.19, 3.87]; median SE 0.56
- histogram (bin lower edge: count): -6: 0, -5: 415, -4: 1506, -3: 1728, -2: 4627, -1: 9453, +0: 4741, +1: 3268, +2: 1920, +3: 1984, +4: 1197, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 2.82 | 0.02 | 0.835 | 0.86 |
| scvi_k30_bnone | 2.80 | 0.02 | 0.834 | 0.80 |
| scvi_k10_btissue | 2.61 | 0.02 | 0.819 | 0.73 |
| nystroem_k256_g0.5 | 2.53 | 0.02 | 0.812 | 0.36 |
| ica_k64 | 2.52 | 0.02 | 0.812 | 0.35 |
| pca_k64 | 2.52 | 0.02 | 0.811 | 0.39 |
| nystroem_k64_g0.5 | 2.50 | 0.02 | 0.810 | 0.30 |
| pca_k128 | 2.46 | 0.02 | 0.806 | 0.61 |
| nystroem_k256_g2 | 2.42 | 0.02 | 0.803 | 0.39 |
| pca_k256 | 2.33 | 0.02 | 0.795 | 0.72 |
| nmf_k64 | 2.18 | 0.02 | 0.782 | 0.79 |
| pca_k32 | 2.17 | 0.02 | 0.781 | 0.75 |
| nystroem_k64_g2 | 2.08 | 0.02 | 0.772 | 0.67 |
| rproj_k128_s1 | 1.93 | 0.02 | 0.757 | 0.94 |
| rproj_k128_s0 | 1.90 | 0.02 | 0.754 | 0.93 |
| ica_k16 | 1.51 | 0.02 | 0.712 | 0.65 |
| pca_k16 | 1.51 | 0.02 | 0.712 | 0.65 |
| gmm_k100 | 1.42 | 0.02 | 0.702 | 0.84 |
| nmf_k16 | 0.73 | 0.02 | 0.616 | 1.17 |
| pca_k8 | 0.42 | 0.01 | 0.574 | 1.11 |
| gmm_k30 | 0.42 | 0.01 | 0.573 | 1.01 |
| rproj_k32_s1 | 0.26 | 0.01 | 0.551 | 1.64 |
| rproj_k32_s0 | 0.24 | 0.01 | 0.548 | 1.53 |
| pca_k4 | -0.84 | 0.01 | 0.388 | 1.98 |
| gmm_k10 | -1.22 | 0.01 | 0.335 | 3.19 |
| rproj_k8_s1 | -1.85 | 0.02 | 0.253 | 4.22 |
| rproj_k8_s0 | -1.97 | 0.02 | 0.239 | 3.33 |
| depth2 | -3.70 | 0.02 | 0.095 | 8.62 |
| random_k32_s1 | -4.78 | 0.03 | 0.052 | 5.82 |
| random_k32_s0 | -4.82 | 0.03 | 0.051 | 4.90 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.284 | 0.0e+00 | 30839 |
| log_total_counts | -0.024 | 3.4e-05 | 30839 |
| n_genes_by_counts | -0.034 | 2.0e-09 | 30839 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Goblet (bronchial) | 49.0 | 4.34 | 128 |
| SM activated stress response | 47.0 | 3.49 | 122 |
| T cells proliferating | 77.0 | 3.28 | 55 |
| Multiciliated (nasal) | 172.0 | 3.22 | 857 |
| Subpleural fibroblasts | 32.0 | 2.85 | 204 |
| DC1 | 49.0 | 2.45 | 85 |
| Alveolar Mph CCL3+ | 66.0 | 2.20 | 1027 |
| Non-classical monocytes | 1353.0 | 2.08 | 1835 |
| Interstitial Mph perivascular | 842.0 | 2.06 | 1240 |
| Alveolar Mph proliferating | 205.0 | 2.01 | 482 |
| AT2 proliferating | 244.0 | 1.94 | 373 |
| Peribronchial fibroblasts | 406.0 | 1.79 | 298 |
| Migratory DCs | 27.0 | 1.66 | 58 |
| Club (nasal) | 206.0 | 1.65 | 3053 |
| Deuterosomal | 278.0 | 1.65 | 318 |

## stratum_binomial

- items: 724; informative (non-degenerate): 724; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.48, -0.77, -0.04, 0.81, 2.07]; median SE 0.07
- histogram (bin lower edge: count): -6: 6, -5: 19, -4: 6, -3: 11, -2: 93, -1: 237, +0: 194, +1: 116, +2: 34, +3: 3, +4: 3, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_btissue | 2.03 | 0.02 | 0.835 | 4.48 |
| scvi_k30_bnone | 2.02 | 0.02 | 0.834 | 4.09 |
| scvi_k10_btissue | 1.89 | 0.02 | 0.819 | 4.33 |
| nystroem_k256_g0.5 | 1.83 | 0.02 | 0.812 | 2.60 |
| ica_k64 | 1.83 | 0.02 | 0.812 | 2.69 |
| pca_k64 | 1.83 | 0.02 | 0.811 | 2.80 |
| nystroem_k64_g0.5 | 1.81 | 0.02 | 0.810 | 2.41 |
| pca_k128 | 1.79 | 0.02 | 0.806 | 4.09 |
| nystroem_k256_g2 | 1.76 | 0.02 | 0.803 | 2.82 |
| pca_k256 | 1.70 | 0.02 | 0.795 | 4.14 |
| nmf_k64 | 1.60 | 0.02 | 0.782 | 4.12 |
| pca_k32 | 1.59 | 0.02 | 0.781 | 3.98 |
| nystroem_k64_g2 | 1.53 | 0.01 | 0.772 | 4.27 |
| rproj_k128_s1 | 1.43 | 0.01 | 0.757 | 3.00 |
| rproj_k128_s0 | 1.40 | 0.01 | 0.754 | 3.37 |
| ica_k16 | 1.13 | 0.01 | 0.712 | 5.26 |
| pca_k16 | 1.13 | 0.01 | 0.712 | 5.27 |
| gmm_k100 | 1.07 | 0.01 | 0.702 | 7.50 |
| nmf_k16 | 0.57 | 0.01 | 0.616 | 9.02 |
| pca_k8 | 0.35 | 0.01 | 0.574 | 7.28 |
| gmm_k30 | 0.34 | 0.01 | 0.573 | 16.55 |
| rproj_k32_s1 | 0.23 | 0.01 | 0.551 | 6.52 |
| rproj_k32_s0 | 0.21 | 0.01 | 0.548 | 5.54 |
| pca_k4 | -0.64 | 0.01 | 0.388 | 13.61 |
| gmm_k10 | -0.94 | 0.01 | 0.335 | 30.61 |
| rproj_k8_s1 | -1.47 | 0.01 | 0.253 | 10.40 |
| rproj_k8_s0 | -1.57 | 0.02 | 0.239 | 8.48 |
| depth2 | -3.10 | 0.02 | 0.095 | 24.61 |
| random_k32_s1 | -4.07 | 0.03 | 0.052 | 6.73 |
| random_k32_s0 | -4.10 | 0.03 | 0.051 | 6.20 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.342 | 2.9e-21 | 724 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Banovich_Kropski_2020|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747VUHD92 | 5.09 | 0.27 | 0.02 |
| Misharin_2021|Goblet (bronchial)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 4.68 | 0.15 | 0.03 |
| Nawijn_2021|Goblet (bronchial)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 4.33 | 0.13 | 0.04 |
| Banovich_Kropski_2020|Goblet (nasal)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747VUHD103 | 4.18 | 0.17 | 0.05 |
| Nawijn_2021|Club (nasal)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-01 | 3.31 | 0.10 | 0.11 |
| Misharin_2021|Peribronchial fibroblasts|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI02 | 3.23 | 0.12 | 0.11 |
| Nawijn_2021|Multiciliated (nasal)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-03 | 3.10 | 0.08 | 0.13 |
| Nawijn_2021|T cells proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 2.95 | 0.08 | 0.14 |
| Misharin_2021|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 2.92 | 0.08 | 0.15 |
| Nawijn_2021|Multiciliated (nasal)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 2.91 | 0.08 | 0.15 |
| Misharin_2021|Peribronchial fibroblasts|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 2.83 | 0.07 | 0.16 |
| Nawijn_2021|Multiciliated (nasal)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-04 | 2.82 | 0.07 | 0.16 |
| Banovich_Kropski_2020|Peribronchial fibroblasts|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747VUHD94 | 2.81 | 0.11 | 0.16 |
| Banovich_Kropski_2020|T cells proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747VUHD67 | 2.78 | 0.07 | 0.16 |
| Nawijn_2021|Interstitial Mph perivascular|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-10 | 2.78 | 0.10 | 0.16 |

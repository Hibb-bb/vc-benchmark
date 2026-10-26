# Component A summary: repr_hlca_core_donor


## cell_level

- items: 11389; informative (non-degenerate): 10827; nobody passes: 409; everybody passes: 153
- difficulty percentiles 5/25/50/75/95: [-3.29, -1.57, -0.42, 1.11, 3.85]; median SE 0.60
- histogram (bin lower edge: count): -6: 110, -5: 156, -4: 468, -3: 1321, -2: 2130, -1: 2228, +0: 1608, +1: 1090, +2: 743, +3: 542, +4: 431, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 2.69 | 0.03 | 0.820 | 0.47 |
| fm_scgpt | 2.67 | 0.03 | 0.820 | 2.19 |
| pca_k256 | 2.67 | 0.03 | 0.818 | 0.51 |
| fm_geneformer_v2_316m | 2.65 | 0.03 | 0.821 | 2.21 |
| scvi_k30_btissue | 2.62 | 0.03 | 0.815 | 1.38 |
| nystroem_k256_g0.5 | 2.61 | 0.03 | 0.814 | 0.64 |
| ica_k64 | 2.60 | 0.03 | 0.813 | 0.32 |
| pca_k64 | 2.59 | 0.03 | 0.812 | 0.31 |
| scvi_k30_bnone | 2.57 | 0.03 | 0.811 | 0.98 |
| fm_transcriptformer | 2.49 | 0.03 | 0.809 | 3.76 |
| nystroem_k64_g0.5 | 2.46 | 0.03 | 0.803 | 0.35 |
| fm_uce | 2.43 | 0.03 | 0.802 | 2.15 |
| nystroem_k256_g2 | 2.40 | 0.03 | 0.798 | 0.91 |
| scvi_k10_btissue | 2.37 | 0.03 | 0.796 | 1.50 |
| pca_k32 | 2.22 | 0.03 | 0.783 | 0.38 |
| rproj_k128_s0 | 2.11 | 0.03 | 0.774 | 0.87 |
| rproj_k128_s1 | 2.10 | 0.03 | 0.772 | 1.04 |
| fm_state | 2.09 | 0.03 | 0.774 | 2.69 |
| nmf_k64 | 2.07 | 0.03 | 0.770 | 0.73 |
| nystroem_k64_g2 | 1.84 | 0.03 | 0.749 | 1.09 |
| fm_cellplm | 1.72 | 0.03 | 0.739 | 1.95 |
| pca_k16 | 1.32 | 0.03 | 0.696 | 0.55 |
| ica_k16 | 1.32 | 0.03 | 0.696 | 0.55 |
| fm_scprint_large_v1 | 1.29 | 0.03 | 0.695 | 2.42 |
| gmm_k100 | 0.82 | 0.03 | 0.638 | 0.82 |
| nmf_k16 | 0.58 | 0.03 | 0.608 | 1.13 |
| rproj_k32_s1 | 0.44 | 0.03 | 0.589 | 1.47 |
| rproj_k32_s0 | 0.42 | 0.03 | 0.586 | 1.46 |
| gmm_k30 | 0.26 | 0.03 | 0.565 | 1.16 |
| pca_k8 | 0.09 | 0.03 | 0.542 | 1.03 |
| pca_k4 | -1.10 | 0.02 | 0.370 | 2.37 |
| gmm_k10 | -1.79 | 0.03 | 0.275 | 5.01 |
| rproj_k8_s1 | -1.93 | 0.03 | 0.257 | 4.19 |
| rproj_k8_s0 | -2.14 | 0.03 | 0.231 | 3.32 |
| depth2 | -3.53 | 0.04 | 0.106 | 10.35 |
| random_k32_s0 | -5.00 | 0.06 | 0.042 | 4.02 |
| random_k32_s1 | -5.02 | 0.06 | 0.041 | 2.97 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.329 | 3.6e-272 | 10827 |
| log_total_counts | -0.019 | 5.3e-02 | 10827 |
| n_genes_by_counts | -0.015 | 1.1e-01 | 10827 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Goblet (bronchial) | 33.0 | 4.53 | 128 |
| T cells proliferating | 81.0 | 3.06 | 34 |
| Lymphatic EC differentiating | 46.0 | 2.53 | 79 |
| Alveolar Mph CCL3+ | 71.0 | 2.47 | 977 |
| Migratory DCs | 45.0 | 2.41 | 27 |
| AT2 proliferating | 113.0 | 2.22 | 595 |
| Myofibroblasts | 167.0 | 2.19 | 114 |
| AT0 | 144.0 | 1.84 | 615 |
| Deuterosomal | 154.0 | 1.64 | 469 |
| Multiciliated (nasal) | 141.0 | 1.61 | 1213 |
| Non-classical monocytes | 348.0 | 1.43 | 4324 |
| Smooth muscle FAM83D+ | 67.0 | 1.37 | 164 |
| Interstitial Mph perivascular | 218.0 | 1.32 | 2176 |
| Monocyte-derived Mph | 367.0 | 1.20 | 7330 |
| Alveolar Mph proliferating | 100.0 | 1.05 | 732 |

## stratum_binomial

- items: 247; informative (non-degenerate): 247; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.6, -1.0, -0.21, 0.89, 2.07]; median SE 0.07
- histogram (bin lower edge: count): -6: 1, -5: 3, -4: 4, -3: 11, -2: 43, -1: 71, +0: 60, +1: 39, +2: 10, +3: 1, +4: 1, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| fm_geneformer_v2_316m | 1.88 | 0.03 | 0.821 | 7.64 |
| fm_scgpt | 1.88 | 0.03 | 0.820 | 5.92 |
| pca_k128 | 1.87 | 0.03 | 0.820 | 3.19 |
| pca_k256 | 1.86 | 0.03 | 0.818 | 3.04 |
| scvi_k30_btissue | 1.83 | 0.03 | 0.815 | 6.61 |
| nystroem_k256_g0.5 | 1.83 | 0.03 | 0.814 | 3.13 |
| ica_k64 | 1.82 | 0.03 | 0.813 | 2.89 |
| pca_k64 | 1.81 | 0.03 | 0.812 | 2.91 |
| scvi_k30_bnone | 1.80 | 0.03 | 0.811 | 4.26 |
| fm_transcriptformer | 1.78 | 0.03 | 0.809 | 20.00 |
| nystroem_k64_g0.5 | 1.73 | 0.03 | 0.803 | 2.60 |
| fm_uce | 1.72 | 0.03 | 0.802 | 5.50 |
| nystroem_k256_g2 | 1.69 | 0.03 | 0.798 | 3.75 |
| scvi_k10_btissue | 1.67 | 0.03 | 0.796 | 6.60 |
| pca_k32 | 1.57 | 0.03 | 0.783 | 2.54 |
| fm_state | 1.50 | 0.03 | 0.774 | 4.64 |
| rproj_k128_s0 | 1.49 | 0.03 | 0.774 | 3.41 |
| rproj_k128_s1 | 1.49 | 0.03 | 0.772 | 3.89 |
| nmf_k64 | 1.47 | 0.03 | 0.770 | 4.14 |
| nystroem_k64_g2 | 1.32 | 0.02 | 0.749 | 9.25 |
| fm_cellplm | 1.24 | 0.02 | 0.739 | 9.58 |
| pca_k16 | 0.96 | 0.02 | 0.696 | 3.83 |
| ica_k16 | 0.96 | 0.02 | 0.696 | 3.83 |
| fm_scprint_large_v1 | 0.95 | 0.02 | 0.695 | 8.20 |
| gmm_k100 | 0.60 | 0.02 | 0.638 | 9.00 |
| nmf_k16 | 0.43 | 0.02 | 0.608 | 7.33 |
| rproj_k32_s1 | 0.32 | 0.02 | 0.589 | 6.36 |
| rproj_k32_s0 | 0.31 | 0.02 | 0.586 | 6.31 |
| gmm_k30 | 0.19 | 0.02 | 0.565 | 17.12 |
| pca_k8 | 0.06 | 0.02 | 0.542 | 7.96 |
| pca_k4 | -0.89 | 0.02 | 0.370 | 13.86 |
| gmm_k10 | -1.47 | 0.02 | 0.275 | 37.81 |
| rproj_k8_s1 | -1.59 | 0.02 | 0.257 | 9.52 |
| rproj_k8_s0 | -1.77 | 0.03 | 0.231 | 10.05 |
| depth2 | -2.99 | 0.03 | 0.106 | 26.40 |
| random_k32_s0 | -4.28 | 0.05 | 0.042 | 9.84 |
| random_k32_s1 | -4.30 | 0.05 | 0.041 | 9.43 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.422 | 4.3e-12 | 247 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Meyer_2019|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747390C | 6.62 | 0.39 | 0.00 |
| Misharin_2021|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 6.62 | 0.39 | 0.00 |
| Misharin_2021|Goblet (bronchial)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 5.35 | 0.21 | 0.01 |
| Nawijn_2021|Goblet (bronchial)|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 4.91 | 0.17 | 0.02 |
| Banovich_Kropski_2020|T cells proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747VUHD67 | 3.54 | 0.10 | 0.08 |
| Nawijn_2021|T cells proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 2.68 | 0.07 | 0.16 |
| Nawijn_2021|Interstitial Mph perivascular|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747GRO-09 | 2.63 | 0.11 | 0.17 |
| Meyer_2019|Smooth muscle FAM83D+|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747390C | 2.62 | 0.11 | 0.17 |
| Meyer_2019|Myofibroblasts|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747390C | 2.62 | 0.07 | 0.17 |
| Misharin_Budinger_2018|Alveolar Mph CCL3+|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747Donor_07 | 2.17 | 0.08 | 0.24 |
| Krasnow_2020|AT0|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747donor 3 | 2.11 | 0.06 | 0.25 |
| Teichmann_Meyer_2019|Interstitial Mph perivascular|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747296C | 2.10 | 0.09 | 0.25 |
| Meyer_2019|AT2 proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747390C | 2.09 | 0.10 | 0.25 |
| Misharin_2021|Lymphatic EC differentiating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 2.01 | 0.06 | 0.26 |
| Krasnow_2020|T cells proliferating|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747donor 3 | 2.01 | 0.10 | 0.26 |

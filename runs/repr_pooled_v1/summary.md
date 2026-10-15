# Component A summary: repr_pooled_v1


## cell_level

- items: 146428; informative (non-degenerate): 138994; nobody passes: 6525; everybody passes: 909
- difficulty percentiles 5/25/50/75/95: [-3.23, -1.78, -0.5, 1.04, 3.73]; median SE 0.55
- histogram (bin lower edge: count): -6: 0, -5: 657, -4: 7297, -3: 18155, -2: 32147, -1: 27713, +0: 16701, +1: 13413, +2: 12691, +3: 6450, +4: 3770, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 2.06 | 0.01 | 0.770 | 0.73 |
| nystroem_k256_g0.5 | 2.06 | 0.01 | 0.770 | 0.42 |
| pca_k128 | 2.04 | 0.01 | 0.768 | 0.47 |
| scvi_k30_btissue | 2.02 | 0.01 | 0.766 | 0.79 |
| ica_k64 | 2.00 | 0.01 | 0.765 | 0.33 |
| pca_k64 | 2.00 | 0.01 | 0.765 | 0.33 |
| nystroem_k64_g0.5 | 1.98 | 0.01 | 0.763 | 0.33 |
| pca_k256 | 1.97 | 0.01 | 0.762 | 0.61 |
| nystroem_k256_g2 | 1.89 | 0.01 | 0.755 | 0.49 |
| pca_k32 | 1.74 | 0.01 | 0.741 | 0.45 |
| scvi_k10_btissue | 1.72 | 0.01 | 0.738 | 0.78 |
| nmf_k64 | 1.56 | 0.01 | 0.723 | 0.73 |
| nystroem_k64_g2 | 1.52 | 0.01 | 0.719 | 0.80 |
| rproj_k128_s1 | 1.14 | 0.01 | 0.678 | 0.92 |
| rproj_k128_s0 | 1.14 | 0.01 | 0.677 | 0.93 |
| pca_k16 | 1.04 | 0.01 | 0.666 | 0.57 |
| ica_k16 | 1.04 | 0.01 | 0.666 | 0.57 |
| gmm_k100 | 0.67 | 0.01 | 0.622 | 0.86 |
| nmf_k16 | 0.40 | 0.01 | 0.587 | 1.02 |
| pca_k8 | -0.03 | 0.01 | 0.529 | 1.02 |
| gmm_k30 | -0.08 | 0.01 | 0.522 | 1.10 |
| rproj_k32_s0 | -0.39 | 0.01 | 0.478 | 1.45 |
| rproj_k32_s1 | -0.39 | 0.01 | 0.477 | 1.49 |
| pca_k4 | -1.01 | 0.01 | 0.388 | 1.72 |
| gmm_k10 | -1.63 | 0.01 | 0.299 | 2.46 |
| rproj_k8_s1 | -2.25 | 0.01 | 0.220 | 3.27 |
| rproj_k8_s0 | -2.33 | 0.01 | 0.210 | 3.05 |
| depth2 | -3.14 | 0.01 | 0.130 | 5.45 |
| random_k32_s1 | -4.39 | 0.01 | 0.053 | 10.15 |
| random_k32_s0 | -4.41 | 0.01 | 0.052 | 10.14 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.209 | 0.0e+00 | 138994 |
| log_total_counts | -0.075 | 7.5e-174 | 138994 |
| n_genes_by_counts | -0.083 | 1.1e-208 | 138994 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 1772 | 0.57 | 1.70 |
| Epithelium | 2434 | 0.33 | 1.85 |
| Immune | 10383 | 0.15 | 2.06 |
| Neural | 100 | -0.63 | 0.68 |
| Stromal | 3067 | 0.68 | 2.11 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| Goblet (bronchial) | 82.0 | 3.87 | 128 |
| mural cell | 44.0 | 3.77 | 128 |
| naive thymus-derived cd8-positive, alpha-beta t cell | 24.0 | 3.68 | 712 |
| activated cd8-positive, alpha-beta t cell | 60.0 | 3.48 | 361 |
| mesenchymal stem cell of adipose tissue | 45.0 | 3.44 | 445 |
| muscle cell | 39.0 | 3.33 | 132 |
| intermediate monocyte | 56.0 | 3.32 | 2195 |
| innate lymphoid cell | 26.0 | 3.29 | 95 |
| t cell | 139.0 | 3.22 | 2270 |
| activated cd4-positive, alpha-beta t cell | 38.0 | 3.20 | 225 |
| fibroblast of breast | 34.0 | 3.13 | 200 |
| SM activated stress response | 56.0 | 3.13 | 23 |
| schwann cell | 21.0 | 3.12 | 273 |
| gamma-delta t cell | 69.0 | 3.06 | 452 |
| DC | 130.0 | 3.06 | 366 |

## stratum_binomial

- items: 3061; informative (non-degenerate): 3055; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.15, -1.05, -0.1, 0.88, 2.53]; median SE 0.07
- histogram (bin lower edge: count): -6: 7, -5: 22, -4: 12, -3: 161, -2: 600, -1: 837, +0: 718, +1: 426, +2: 176, +3: 50, +4: 30, +5: 11

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | 1.50 | 0.01 | 0.770 | 3.46 |
| nystroem_k256_g0.5 | 1.50 | 0.01 | 0.770 | 2.94 |
| pca_k128 | 1.48 | 0.01 | 0.768 | 2.87 |
| scvi_k30_btissue | 1.47 | 0.01 | 0.766 | 4.20 |
| ica_k64 | 1.46 | 0.01 | 0.765 | 2.27 |
| pca_k64 | 1.46 | 0.01 | 0.765 | 2.31 |
| nystroem_k64_g0.5 | 1.44 | 0.01 | 0.763 | 2.27 |
| pca_k256 | 1.44 | 0.01 | 0.762 | 3.11 |
| nystroem_k256_g2 | 1.39 | 0.01 | 0.755 | 3.15 |
| pca_k32 | 1.28 | 0.01 | 0.741 | 2.58 |
| scvi_k10_btissue | 1.26 | 0.01 | 0.738 | 4.73 |
| nmf_k64 | 1.15 | 0.01 | 0.723 | 3.91 |
| nystroem_k64_g2 | 1.13 | 0.01 | 0.719 | 8.07 |
| rproj_k128_s1 | 0.86 | 0.01 | 0.678 | 3.10 |
| rproj_k128_s0 | 0.85 | 0.01 | 0.677 | 3.30 |
| pca_k16 | 0.78 | 0.01 | 0.666 | 4.07 |
| ica_k16 | 0.78 | 0.01 | 0.666 | 4.06 |
| gmm_k100 | 0.51 | 0.01 | 0.622 | 9.01 |
| nmf_k16 | 0.31 | 0.01 | 0.587 | 7.89 |
| pca_k8 | -0.02 | 0.01 | 0.529 | 7.58 |
| gmm_k30 | -0.05 | 0.01 | 0.522 | 18.29 |
| rproj_k32_s0 | -0.30 | 0.01 | 0.478 | 5.36 |
| rproj_k32_s1 | -0.30 | 0.01 | 0.477 | 5.57 |
| pca_k4 | -0.80 | 0.01 | 0.388 | 13.14 |
| gmm_k10 | -1.33 | 0.01 | 0.299 | 31.02 |
| rproj_k8_s1 | -1.86 | 0.01 | 0.220 | 8.25 |
| rproj_k8_s0 | -1.94 | 0.01 | 0.210 | 8.78 |
| depth2 | -2.66 | 0.01 | 0.130 | 28.90 |
| random_k32_s1 | -3.82 | 0.01 | 0.053 | 37.08 |
| random_k32_s0 | -3.84 | 0.01 | 0.052 | 36.77 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.311 | 1.2e-69 | 3055 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_pool_v0::Testis|stromal cell|TSP25 | 7.75 | 0.80 | 0.00 |
| repr_pool_v0::Heart|regular atrial cardiac myocyte|TSP25 | 6.41 | 0.47 | 0.00 |
| repr_hlca_core_donor::Meyer_2019|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747390C | 6.28 | 0.39 | 0.00 |
| repr_hlca_core_donor::Misharin_2021|SM activated stress response|homosapiens_None_2023_None_sikkemalisa_001_d10_1101_2022_03_10_483747NU_CZI01 | 6.28 | 0.39 | 0.00 |
| repr_pool_v0::Salivary_Gland|t cell|TSP25 | 6.10 | 0.43 | 0.00 |
| repr_pool_v0::Small_Intestine|innate lymphoid cell|TSP27 | 5.74 | 0.48 | 0.01 |
| repr_immune_atlas_tissue::spleen|Cycling|A29 | 5.36 | 0.40 | 0.01 |
| repr_heart_states::Harvard-Nuclei|CD4+T_tem|H2 | 5.27 | 0.26 | 0.01 |
| repr_immune_atlas_tissue::lung|Cycling|D496 | 5.23 | 0.28 | 0.01 |
| repr_immune_atlas_tissue::lung|Cycling|A29 | 5.17 | 0.31 | 0.01 |
| repr_immune_atlas_tissue::bone marrow|Cycling|A36 | 5.10 | 0.31 | 0.01 |
| repr_pool_v0::Bone_Marrow|intermediate monocyte|TSP25 | 5.10 | 0.31 | 0.01 |
| repr_pool_v0::Stomach|t cell|TSP25 | 5.09 | 0.24 | 0.01 |
| repr_pool_v0::Ear|melanocyte|TSP25 | 5.06 | 0.22 | 0.01 |
| repr_heart_states::Sanger-CD45|EC10_CMC-like|D7 | 5.06 | 0.22 | 0.01 |

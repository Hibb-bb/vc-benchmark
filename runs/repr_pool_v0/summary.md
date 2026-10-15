# Component A summary: repr_pool_v0


## cell_level

- items: 20026; informative (non-degenerate): 17756; nobody passes: 2270; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.15, -2.15, -0.97, 0.71, 2.62]; median SE 0.49
- histogram (bin lower edge: count): -6: 0, -5: 96, -4: 1129, -3: 3473, -2: 3606, -1: 3418, +0: 2226, +1: 1837, +2: 1160, +3: 811, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 0.98 | 0.02 | 0.654 | 0.55 |
| pca_k256 | 0.94 | 0.02 | 0.650 | 0.68 |
| nystroem_k256_g0.5 | 0.85 | 0.02 | 0.640 | 0.53 |
| ica_k64 | 0.81 | 0.02 | 0.636 | 0.39 |
| pca_k64 | 0.81 | 0.02 | 0.635 | 0.40 |
| nystroem_k256_g2 | 0.80 | 0.02 | 0.634 | 0.58 |
| nystroem_k64_g0.5 | 0.76 | 0.02 | 0.630 | 0.43 |
| scvi_k30_bnone | 0.74 | 0.02 | 0.627 | 0.73 |
| pca_k32 | 0.55 | 0.02 | 0.606 | 0.46 |
| nmf_k64 | 0.49 | 0.02 | 0.599 | 0.68 |
| scvi_k30_btissue | 0.47 | 0.02 | 0.596 | 0.79 |
| rproj_k128_s0 | 0.35 | 0.02 | 0.582 | 0.85 |
| rproj_k128_s1 | 0.34 | 0.02 | 0.581 | 0.86 |
| nystroem_k64_g2 | 0.28 | 0.02 | 0.574 | 0.83 |
| scvi_k10_btissue | 0.10 | 0.02 | 0.552 | 0.73 |
| ica_k16 | -0.11 | 0.02 | 0.526 | 0.63 |
| pca_k16 | -0.11 | 0.02 | 0.526 | 0.63 |
| gmm_k100 | -0.57 | 0.02 | 0.464 | 0.72 |
| nmf_k16 | -0.60 | 0.02 | 0.461 | 0.91 |
| rproj_k32_s1 | -0.75 | 0.02 | 0.440 | 1.11 |
| rproj_k32_s0 | -0.85 | 0.02 | 0.426 | 1.09 |
| gmm_k30 | -1.08 | 0.02 | 0.394 | 1.21 |
| pca_k8 | -1.34 | 0.02 | 0.359 | 1.04 |
| pca_k4 | -2.14 | 0.02 | 0.251 | 1.65 |
| gmm_k10 | -2.33 | 0.02 | 0.228 | 1.80 |
| rproj_k8_s0 | -2.47 | 0.02 | 0.211 | 1.49 |
| rproj_k8_s1 | -2.57 | 0.02 | 0.199 | 1.72 |
| depth2 | -2.97 | 0.02 | 0.156 | 2.00 |
| random_k32_s1 | -4.14 | 0.03 | 0.066 | 4.25 |
| random_k32_s0 | -4.14 | 0.03 | 0.066 | 4.25 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.349 | 0.0e+00 | 17756 |
| log_total_counts | -0.097 | 4.4e-38 | 17756 |
| n_genes_by_counts | -0.016 | 3.1e-02 | 17756 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 1772 | -0.38 | 1.54 |
| Epithelium | 2434 | -0.59 | 1.69 |
| Immune | 10383 | -0.74 | 1.86 |
| Neural | 100 | -1.50 | 0.60 |
| Stromal | 3067 | -0.25 | 1.93 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mural cell | 44.0 | 2.68 | 128 |
| naive thymus-derived cd8-positive, alpha-beta t cell | 24.0 | 2.58 | 712 |
| activated cd8-positive, alpha-beta t cell | 60.0 | 2.37 | 361 |
| mesenchymal stem cell of adipose tissue | 45.0 | 2.33 | 445 |
| muscle cell | 39.0 | 2.22 | 132 |
| intermediate monocyte | 56.0 | 2.21 | 2195 |
| innate lymphoid cell | 26.0 | 2.18 | 95 |
| t cell | 139.0 | 2.11 | 2270 |
| activated cd4-positive, alpha-beta t cell | 38.0 | 2.09 | 225 |
| fibroblast of breast | 34.0 | 2.03 | 200 |
| schwann cell | 21.0 | 2.01 | 273 |
| gamma-delta t cell | 69.0 | 1.95 | 452 |
| regulatory t cell | 99.0 | 1.93 | 1421 |
| naive thymus-derived cd4-positive, alpha-beta t cell | 156.0 | 1.87 | 2699 |
| cd8-positive, alpha-beta thymocyte | 37.0 | 1.84 | 400 |

## stratum_binomial

- items: 433; informative (non-degenerate): 427; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.27, -1.42, -0.4, 0.96, 3.41]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 46, -2: 106, -1: 91, +0: 77, +1: 49, +2: 30, +3: 17, +4: 7, +5: 2

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 0.80 | 0.02 | 0.654 | 3.82 |
| pca_k256 | 0.77 | 0.02 | 0.650 | 4.06 |
| nystroem_k256_g0.5 | 0.70 | 0.02 | 0.640 | 4.40 |
| ica_k64 | 0.67 | 0.02 | 0.636 | 3.02 |
| pca_k64 | 0.67 | 0.02 | 0.635 | 3.11 |
| nystroem_k256_g2 | 0.66 | 0.02 | 0.634 | 4.76 |
| nystroem_k64_g0.5 | 0.63 | 0.02 | 0.630 | 3.28 |
| scvi_k30_bnone | 0.62 | 0.02 | 0.627 | 4.55 |
| pca_k32 | 0.47 | 0.02 | 0.606 | 3.02 |
| nmf_k64 | 0.43 | 0.02 | 0.599 | 5.52 |
| scvi_k30_btissue | 0.40 | 0.02 | 0.596 | 5.69 |
| rproj_k128_s0 | 0.31 | 0.02 | 0.582 | 3.83 |
| rproj_k128_s1 | 0.30 | 0.02 | 0.581 | 3.74 |
| nystroem_k64_g2 | 0.26 | 0.02 | 0.574 | 10.06 |
| scvi_k10_btissue | 0.12 | 0.02 | 0.552 | 7.58 |
| ica_k16 | -0.05 | 0.02 | 0.526 | 5.85 |
| pca_k16 | -0.05 | 0.02 | 0.526 | 5.90 |
| gmm_k100 | -0.42 | 0.02 | 0.464 | 12.83 |
| nmf_k16 | -0.44 | 0.02 | 0.461 | 9.08 |
| rproj_k32_s1 | -0.57 | 0.02 | 0.440 | 5.66 |
| rproj_k32_s0 | -0.65 | 0.02 | 0.426 | 5.81 |
| gmm_k30 | -0.85 | 0.02 | 0.394 | 24.12 |
| pca_k8 | -1.06 | 0.02 | 0.359 | 10.61 |
| pca_k4 | -1.76 | 0.02 | 0.251 | 20.30 |
| gmm_k10 | -1.93 | 0.02 | 0.228 | 30.04 |
| rproj_k8_s0 | -2.05 | 0.02 | 0.211 | 8.01 |
| rproj_k8_s1 | -2.14 | 0.02 | 0.199 | 8.21 |
| depth2 | -2.51 | 0.02 | 0.156 | 23.26 |
| random_k32_s1 | -3.60 | 0.03 | 0.066 | 57.90 |
| random_k32_s0 | -3.60 | 0.03 | 0.066 | 57.57 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.460 | 8.5e-24 | 427 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Testis|stromal cell|TSP25 | 7.00 | 0.82 | 0.00 |
| Heart|regular atrial cardiac myocyte|TSP25 | 5.64 | 0.48 | 0.00 |
| Salivary_Gland|t cell|TSP25 | 5.33 | 0.43 | 0.00 |
| Small_Intestine|innate lymphoid cell|TSP27 | 4.98 | 0.48 | 0.01 |
| Bone_Marrow|intermediate monocyte|TSP25 | 4.32 | 0.31 | 0.01 |
| Stomach|t cell|TSP25 | 4.31 | 0.24 | 0.01 |
| Ear|melanocyte|TSP25 | 4.28 | 0.22 | 0.01 |
| Thymus|cd4-positive, alpha-beta thymocyte|TSP27 | 4.15 | 0.21 | 0.02 |
| Prostate|mature nk t cell|TSP25 | 4.10 | 0.24 | 0.02 |
| Small_Intestine|natural killer cell|TSP27 | 4.03 | 0.19 | 0.02 |
| Ear|pericyte|TSP25 | 3.99 | 0.19 | 0.02 |
| Vasculature|capillary endothelial cell|TSP25 | 3.92 | 0.18 | 0.02 |
| Large_Intestine|naive thymus-derived cd4-positive, alpha-beta t cell|TSP27 | 3.89 | 0.18 | 0.02 |
| Thymus|naive thymus-derived cd8-positive, alpha-beta t cell|TSP27 | 3.80 | 0.21 | 0.02 |
| Vasculature|basophil|TSP25 | 3.74 | 0.17 | 0.02 |

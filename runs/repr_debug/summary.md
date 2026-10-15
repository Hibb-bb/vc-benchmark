# Component A summary: repr_pool_v0


## cell_level

- items: 20026; informative (non-degenerate): 17509; nobody passes: 2517; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.11, -2.09, -1.06, 0.64, 2.44]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 101, -4: 1179, -3: 3635, -2: 3881, -1: 2556, +0: 2572, +1: 1508, +2: 1275, +3: 802, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 0.97 | 0.02 | 0.654 | 0.55 |
| pca_k256 | 0.94 | 0.02 | 0.650 | 0.68 |
| nystroem_k256_g0.5 | 0.84 | 0.02 | 0.640 | 0.52 |
| ica_k64 | 0.81 | 0.02 | 0.636 | 0.39 |
| pca_k64 | 0.80 | 0.02 | 0.635 | 0.39 |
| nystroem_k256_g2 | 0.80 | 0.02 | 0.634 | 0.58 |
| nystroem_k64_g0.5 | 0.75 | 0.02 | 0.630 | 0.42 |
| pca_k32 | 0.55 | 0.02 | 0.606 | 0.46 |
| nmf_k64 | 0.49 | 0.02 | 0.599 | 0.70 |
| rproj_k128_s0 | 0.34 | 0.02 | 0.582 | 0.85 |
| rproj_k128_s1 | 0.33 | 0.02 | 0.581 | 0.86 |
| nystroem_k64_g2 | 0.27 | 0.02 | 0.574 | 0.81 |
| ica_k16 | -0.12 | 0.02 | 0.526 | 0.61 |
| pca_k16 | -0.12 | 0.02 | 0.526 | 0.61 |
| gmm_k100 | -0.58 | 0.02 | 0.464 | 0.72 |
| nmf_k16 | -0.60 | 0.02 | 0.461 | 0.89 |
| rproj_k32_s1 | -0.76 | 0.02 | 0.440 | 1.10 |
| rproj_k32_s0 | -0.86 | 0.02 | 0.426 | 1.07 |
| gmm_k30 | -1.09 | 0.02 | 0.394 | 1.19 |
| pca_k8 | -1.34 | 0.02 | 0.359 | 0.99 |
| pca_k4 | -2.14 | 0.02 | 0.251 | 1.54 |
| gmm_k10 | -2.32 | 0.02 | 0.228 | 1.71 |
| rproj_k8_s0 | -2.47 | 0.02 | 0.211 | 1.42 |
| rproj_k8_s1 | -2.56 | 0.02 | 0.199 | 1.67 |
| depth2 | -2.96 | 0.02 | 0.156 | 1.94 |
| random_k32_s1 | -4.13 | 0.03 | 0.066 | 3.93 |
| random_k32_s0 | -4.13 | 0.03 | 0.066 | 3.94 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.342 | 0.0e+00 | 17509 |
| log_total_counts | -0.106 | 1.2e-44 | 17509 |
| n_genes_by_counts | -0.026 | 4.8e-04 | 17509 |

### Mean difficulty by compartment

| compartment | n | mean | sd |
|---|---|---|---|
| Endothelium | 1759 | -0.42 | 1.53 |
| Epithelium | 2420 | -0.63 | 1.65 |
| Immune | 10229 | -0.78 | 1.80 |
| Neural | 100 | -1.45 | 0.62 |
| Stromal | 3001 | -0.36 | 1.86 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mural cell | 29.0 | 2.39 | 128 |
| naive thymus-derived cd8-positive, alpha-beta t cell | 23.0 | 2.36 | 712 |
| mesenchymal stem cell of adipose tissue | 39.0 | 2.19 | 445 |
| activated cd8-positive, alpha-beta t cell | 54.0 | 2.16 | 361 |
| muscle cell | 38.0 | 2.10 | 132 |
| innate lymphoid cell | 25.0 | 2.01 | 95 |
| intermediate monocyte | 45.0 | 1.98 | 2195 |
| t cell | 126.0 | 1.97 | 2270 |
| fibroblast of breast | 34.0 | 1.95 | 200 |
| schwann cell | 20.0 | 1.91 | 273 |
| gamma-delta t cell | 66.0 | 1.89 | 452 |
| activated cd4-positive, alpha-beta t cell | 36.0 | 1.88 | 225 |
| naive thymus-derived cd4-positive, alpha-beta t cell | 146.0 | 1.71 | 2699 |
| regulatory t cell | 86.0 | 1.66 | 1421 |
| cd8-positive, alpha-beta thymocyte | 37.0 | 1.64 | 400 |

## stratum_binomial

- items: 433; informative (non-degenerate): 427; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.25, -1.43, -0.4, 1.03, 3.38]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 45, -2: 108, -1: 91, +0: 75, +1: 48, +2: 32, +3: 17, +4: 7, +5: 3

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pca_k128 | 0.80 | 0.02 | 0.654 | 3.96 |
| pca_k256 | 0.77 | 0.02 | 0.650 | 4.12 |
| nystroem_k256_g0.5 | 0.70 | 0.02 | 0.640 | 4.47 |
| ica_k64 | 0.67 | 0.02 | 0.636 | 3.14 |
| pca_k64 | 0.67 | 0.02 | 0.635 | 3.21 |
| nystroem_k256_g2 | 0.67 | 0.02 | 0.634 | 4.95 |
| nystroem_k64_g0.5 | 0.63 | 0.02 | 0.630 | 3.36 |
| pca_k32 | 0.48 | 0.02 | 0.606 | 3.11 |
| nmf_k64 | 0.43 | 0.02 | 0.599 | 5.51 |
| rproj_k128_s0 | 0.32 | 0.02 | 0.582 | 4.02 |
| rproj_k128_s1 | 0.30 | 0.02 | 0.581 | 3.90 |
| nystroem_k64_g2 | 0.26 | 0.02 | 0.574 | 9.84 |
| ica_k16 | -0.04 | 0.02 | 0.526 | 5.78 |
| pca_k16 | -0.04 | 0.02 | 0.526 | 5.84 |
| gmm_k100 | -0.42 | 0.02 | 0.464 | 12.86 |
| nmf_k16 | -0.44 | 0.02 | 0.461 | 8.91 |
| rproj_k32_s1 | -0.57 | 0.02 | 0.440 | 5.80 |
| rproj_k32_s0 | -0.65 | 0.02 | 0.426 | 6.13 |
| gmm_k30 | -0.84 | 0.02 | 0.394 | 23.92 |
| pca_k8 | -1.05 | 0.02 | 0.359 | 10.13 |
| pca_k4 | -1.75 | 0.02 | 0.251 | 19.37 |
| gmm_k10 | -1.91 | 0.02 | 0.228 | 29.67 |
| rproj_k8_s0 | -2.04 | 0.02 | 0.211 | 7.77 |
| rproj_k8_s1 | -2.12 | 0.02 | 0.199 | 8.16 |
| depth2 | -2.49 | 0.02 | 0.156 | 22.65 |
| random_k32_s1 | -3.57 | 0.03 | 0.066 | 54.58 |
| random_k32_s0 | -3.58 | 0.03 | 0.066 | 54.19 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.465 | 2.7e-24 | 427 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Testis|stromal cell|TSP25 | 6.85 | 0.82 | 0.00 |
| Heart|regular atrial cardiac myocyte|TSP25 | 5.49 | 0.48 | 0.00 |
| Salivary_Gland|t cell|TSP25 | 5.18 | 0.43 | 0.01 |
| Small_Intestine|innate lymphoid cell|TSP27 | 5.09 | 0.55 | 0.01 |
| Ear|melanocyte|TSP25 | 4.69 | 0.29 | 0.01 |
| Bone_Marrow|intermediate monocyte|TSP25 | 4.52 | 0.37 | 0.01 |
| Ear|pericyte|TSP25 | 4.29 | 0.24 | 0.01 |
| Small_Intestine|natural killer cell|TSP27 | 4.23 | 0.23 | 0.01 |
| Stomach|t cell|TSP25 | 4.21 | 0.24 | 0.01 |
| Prostate|mature nk t cell|TSP25 | 4.08 | 0.26 | 0.02 |
| Vasculature|basophil|TSP25 | 4.04 | 0.21 | 0.02 |
| Thymus|cd4-positive, alpha-beta thymocyte|TSP27 | 4.00 | 0.21 | 0.02 |
| Vasculature|capillary endothelial cell|TSP25 | 3.88 | 0.19 | 0.02 |
| Large_Intestine|naive thymus-derived cd4-positive, alpha-beta t cell|TSP27 | 3.77 | 0.18 | 0.02 |
| Thymus|naive thymus-derived cd8-positive, alpha-beta t cell|TSP27 | 3.64 | 0.21 | 0.03 |

# Component A summary: repr_scbasecount_humanall_thymus


## cell_level

- items: 4862; informative (non-degenerate): 3620; nobody passes: 1242; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.63, -2.6, -1.01, 0.5, 1.59]; median SE 0.49
- histogram (bin lower edge: count): -6: 0, -5: 39, -4: 614, -3: 710, -2: 502, -1: 603, +0: 755, +1: 397, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -1.34 | 0.04 | 0.348 | 0.52 |
| nystroem_k256_g0.5 | -1.37 | 0.04 | 0.345 | 0.56 |
| pca_k128 | -1.39 | 0.04 | 0.342 | 0.42 |
| nystroem_k64_g0.5 | -1.40 | 0.04 | 0.342 | 0.35 |
| ica_k64 | -1.41 | 0.04 | 0.340 | 0.34 |
| pca_k64 | -1.42 | 0.04 | 0.339 | 0.34 |
| pca_k32 | -1.42 | 0.04 | 0.339 | 0.32 |
| nystroem_k256_g2 | -1.42 | 0.04 | 0.339 | 0.46 |
| scvi_k30_bnone | -1.43 | 0.04 | 0.338 | 0.52 |
| scvi_k30_btissue | -1.43 | 0.04 | 0.338 | 0.52 |
| nystroem_k64_g2 | -1.46 | 0.04 | 0.334 | 0.43 |
| nmf_k16 | -1.48 | 0.04 | 0.332 | 0.56 |
| pca_k256 | -1.50 | 0.04 | 0.330 | 0.57 |
| pca_k16 | -1.50 | 0.04 | 0.330 | 0.34 |
| ica_k16 | -1.50 | 0.04 | 0.329 | 0.34 |
| depth2 | -1.62 | 0.04 | 0.317 | 1.73 |
| gmm_k100 | -1.66 | 0.04 | 0.312 | 0.49 |
| pca_k8 | -1.68 | 0.04 | 0.310 | 0.57 |
| rproj_k128_s0 | -1.70 | 0.04 | 0.308 | 0.82 |
| scvi_k10_btissue | -1.74 | 0.04 | 0.303 | 0.79 |
| rproj_k128_s1 | -1.85 | 0.04 | 0.291 | 0.86 |
| rproj_k32_s0 | -1.94 | 0.04 | 0.281 | 0.97 |
| pca_k4 | -1.97 | 0.04 | 0.278 | 0.94 |
| gmm_k30 | -1.98 | 0.04 | 0.277 | 0.85 |
| rproj_k32_s1 | -2.08 | 0.04 | 0.267 | 0.81 |
| gmm_k10 | -2.23 | 0.04 | 0.251 | 0.96 |
| rproj_k8_s0 | -2.40 | 0.04 | 0.233 | 1.65 |
| rproj_k8_s1 | -2.57 | 0.05 | 0.215 | 1.67 |
| random_k32_s0 | -2.79 | 0.05 | 0.193 | 2.28 |
| random_k32_s1 | -2.85 | 0.05 | 0.188 | 2.52 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.122 | 1.6e-13 | 3620 |
| log_total_counts | 0.013 | 4.2e-01 | 3620 |
| n_genes_by_counts | 0.010 | 5.6e-01 | 3620 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| plasma cell | 125.0 | 0.69 | 872 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 154.0 | 0.65 | 588 |
| CD8-positive, alpha-beta T cell | 238.0 | 0.42 | 2066 |
| naive thymus-derived CD8-positive, alpha-beta T cell | 184.0 | -0.19 | 781 |
| CD4-positive, alpha-beta thymocyte | 922.0 | -1.07 | 2800 |
| CD4-positive, alpha-beta T cell | 622.0 | -1.15 | 2540 |
| macrophage | 110.0 | -1.60 | 518 |
| erythrocyte | 965.0 | -1.61 | 2911 |
| B cell | 283.0 | -2.97 | 257 |

## stratum_binomial

- items: 68; informative (non-degenerate): 68; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.53, -1.26, 0.48, 2.0, 3.89]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 2, -3: 4, -2: 12, -1: 8, +0: 13, +1: 12, +2: 10, +3: 3, +4: 3, +5: 1

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -0.97 | 0.04 | 0.348 | 6.23 |
| nystroem_k256_g0.5 | -1.00 | 0.04 | 0.345 | 6.46 |
| pca_k128 | -1.01 | 0.04 | 0.342 | 3.73 |
| nystroem_k64_g0.5 | -1.02 | 0.04 | 0.342 | 4.78 |
| ica_k64 | -1.03 | 0.04 | 0.340 | 3.41 |
| pca_k64 | -1.03 | 0.04 | 0.339 | 3.39 |
| pca_k32 | -1.04 | 0.04 | 0.339 | 3.27 |
| nystroem_k256_g2 | -1.04 | 0.04 | 0.339 | 4.58 |
| scvi_k30_bnone | -1.05 | 0.04 | 0.338 | 6.65 |
| scvi_k30_btissue | -1.05 | 0.04 | 0.338 | 6.65 |
| nystroem_k64_g2 | -1.07 | 0.04 | 0.334 | 4.47 |
| nmf_k16 | -1.09 | 0.04 | 0.332 | 10.00 |
| pca_k256 | -1.10 | 0.04 | 0.330 | 3.53 |
| pca_k16 | -1.10 | 0.04 | 0.330 | 3.93 |
| ica_k16 | -1.10 | 0.04 | 0.329 | 3.94 |
| depth2 | -1.20 | 0.04 | 0.317 | 58.57 |
| gmm_k100 | -1.23 | 0.04 | 0.312 | 6.85 |
| pca_k8 | -1.25 | 0.04 | 0.310 | 6.98 |
| rproj_k128_s0 | -1.26 | 0.04 | 0.308 | 3.49 |
| scvi_k10_btissue | -1.30 | 0.04 | 0.303 | 9.82 |
| rproj_k128_s1 | -1.39 | 0.04 | 0.291 | 4.70 |
| rproj_k32_s0 | -1.46 | 0.04 | 0.281 | 5.23 |
| pca_k4 | -1.48 | 0.04 | 0.278 | 30.61 |
| gmm_k30 | -1.49 | 0.04 | 0.277 | 20.05 |
| rproj_k32_s1 | -1.57 | 0.04 | 0.267 | 2.99 |
| gmm_k10 | -1.70 | 0.04 | 0.251 | 39.98 |
| rproj_k8_s0 | -1.84 | 0.04 | 0.233 | 16.46 |
| rproj_k8_s1 | -1.98 | 0.04 | 0.215 | 15.80 |
| random_k32_s0 | -2.17 | 0.04 | 0.193 | 29.31 |
| random_k32_s1 | -2.22 | 0.04 | 0.188 | 30.60 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.547 | 1.4e-06 | 68 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002370|thymocyte|SRX13998821 | 5.11 | 0.65 | 0.00 |
| UBERON:0002370|capillary endothelial cell|SRX7691515 | 4.61 | 0.65 | 0.00 |
| UBERON:0002370|thymic fibroblast type 2|SRX13998822 | 4.06 | 0.48 | 0.00 |
| UBERON:0002370|plasma cell|SRX8604558 | 4.02 | 0.26 | 0.01 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX13998818 | 3.66 | 0.37 | 0.01 |
| UBERON:0002370|plasma cell|SRX8604557 | 3.64 | 0.21 | 0.01 |
| UBERON:0002370|thymic fibroblast type 2|SRX13998821 | 3.19 | 0.28 | 0.01 |
| UBERON:0002370|thymocyte|SRX13998818 | 2.94 | 0.30 | 0.01 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX7691515 | 2.71 | 0.20 | 0.02 |
| UBERON:0002370|CD8-positive, alpha-beta T cell|SRX8604557 | 2.69 | 0.13 | 0.02 |
| UBERON:0002370|CD8-positive, alpha-beta T cell|SRX7691515 | 2.39 | 0.12 | 0.03 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX13998822 | 2.37 | 0.24 | 0.03 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX11437846 | 2.36 | 0.22 | 0.03 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX8604557 | 2.35 | 0.11 | 0.03 |
| UBERON:0002370|naive thymus-derived CD4-positive, alpha-beta T cell|SRX13998821 | 2.17 | 0.14 | 0.03 |

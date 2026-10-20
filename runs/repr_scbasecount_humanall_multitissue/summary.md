# Component A summary: repr_scbasecount_humanall_multitissue


## cell_level

- items: 368818; informative (non-degenerate): 252092; nobody passes: 115492; everybody passes: 1234
- difficulty percentiles 5/25/50/75/95: [-4.37, -2.79, -1.46, 0.0, 1.46]; median SE 0.46
- histogram (bin lower edge: count): -6: 4182, -5: 14022, -4: 30686, -3: 53148, -2: 45161, -1: 37013, +0: 42348, +1: 25532, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -0.99 | 0.01 | 0.397 | 0.80 |
| nystroem_k256_g0.5 | -1.13 | 0.01 | 0.382 | 0.61 |
| scvi_k30_btissue | -1.15 | 0.01 | 0.380 | 0.75 |
| pca_k256 | -1.17 | 0.01 | 0.378 | 0.54 |
| pca_k128 | -1.18 | 0.01 | 0.376 | 0.44 |
| nystroem_k64_g0.5 | -1.20 | 0.01 | 0.375 | 0.49 |
| ica_k64 | -1.21 | 0.01 | 0.373 | 0.39 |
| pca_k64 | -1.22 | 0.01 | 0.373 | 0.39 |
| nystroem_k256_g2 | -1.27 | 0.01 | 0.366 | 0.66 |
| scvi_k10_btissue | -1.35 | 0.01 | 0.358 | 0.69 |
| pca_k32 | -1.37 | 0.01 | 0.356 | 0.42 |
| nmf_k64 | -1.60 | 0.01 | 0.331 | 0.61 |
| rproj_k128_s0 | -1.81 | 0.01 | 0.308 | 0.83 |
| rproj_k128_s1 | -1.85 | 0.01 | 0.305 | 0.89 |
| pca_k16 | -1.92 | 0.01 | 0.297 | 0.41 |
| ica_k16 | -1.92 | 0.01 | 0.297 | 0.41 |
| gmm_k100 | -1.95 | 0.01 | 0.294 | 0.66 |
| nystroem_k64_g2 | -2.06 | 0.01 | 0.282 | 0.74 |
| nmf_k16 | -2.26 | 0.01 | 0.261 | 0.58 |
| pca_k8 | -2.34 | 0.01 | 0.253 | 0.60 |
| gmm_k30 | -2.48 | 0.01 | 0.238 | 0.79 |
| rproj_k32_s1 | -2.86 | 0.01 | 0.201 | 1.08 |
| rproj_k32_s0 | -2.91 | 0.01 | 0.196 | 1.21 |
| pca_k4 | -2.97 | 0.01 | 0.191 | 0.90 |
| gmm_k10 | -3.50 | 0.01 | 0.145 | 0.98 |
| rproj_k8_s1 | -3.76 | 0.01 | 0.125 | 1.71 |
| depth2 | -4.00 | 0.01 | 0.108 | 2.18 |
| rproj_k8_s0 | -4.05 | 0.01 | 0.105 | 2.25 |
| random_k32_s1 | -4.14 | 0.01 | 0.099 | 1.43 |
| random_k32_s0 | -4.14 | 0.01 | 0.099 | 1.43 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.250 | 0.0e+00 | 252092 |
| log_total_counts | -0.193 | 0.0e+00 | 252092 |
| n_genes_by_counts | -0.149 | 0.0e+00 | 252092 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mast cell | 228.0 | 1.27 | 66 |
| mesenchymal stem cell of adipose tissue | 65.0 | 1.14 | 1433 |
| myofibroblast cell | 144.0 | 0.98 | 230 |
| monocyte | 940.0 | 0.94 | 2027 |
| oligodendrocyte | 267.0 | 0.91 | 480 |
| intermediate monocyte | 151.0 | 0.86 | 520 |
| basophil | 956.0 | 0.71 | 75 |
| regulatory T cell | 118.0 | 0.48 | 573 |
| smooth muscle cell | 1528.0 | 0.40 | 144 |
| club cell | 270.0 | 0.36 | 137 |
| alveolar adventitial fibroblast | 1208.0 | 0.35 | 396 |
| mature NK T cell | 1212.0 | 0.27 | 4321 |
| central nervous system macrophage | 750.0 | 0.22 | 1131 |
| pulmonary alveolar type 1 cell | 1801.0 | 0.22 | 274 |
| endothelial cell of lymphatic vessel | 958.0 | 0.11 | 138 |

## stratum_binomial

- items: 5103; informative (non-degenerate): 4639; nobody passes: 464; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.29, -2.16, -0.94, 0.53, 3.86]; median SE 0.06
- histogram (bin lower edge: count): -6: 0, -5: 49, -4: 352, -3: 893, -2: 973, -1: 850, +0: 569, +1: 324, +2: 225, +3: 202, +4: 141, +5: 61

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -1.35 | 0.00 | 0.397 | 10.76 |
| nystroem_k256_g0.5 | -1.45 | 0.00 | 0.382 | 10.67 |
| scvi_k30_btissue | -1.47 | 0.00 | 0.380 | 9.30 |
| pca_k256 | -1.49 | 0.00 | 0.378 | 7.16 |
| pca_k128 | -1.50 | 0.00 | 0.376 | 5.93 |
| nystroem_k64_g0.5 | -1.51 | 0.00 | 0.375 | 7.86 |
| ica_k64 | -1.52 | 0.00 | 0.373 | 5.84 |
| pca_k64 | -1.52 | 0.00 | 0.373 | 5.84 |
| nystroem_k256_g2 | -1.57 | 0.00 | 0.366 | 10.34 |
| scvi_k10_btissue | -1.62 | 0.00 | 0.358 | 11.03 |
| pca_k32 | -1.64 | 0.00 | 0.356 | 5.54 |
| nmf_k64 | -1.82 | 0.00 | 0.331 | 6.56 |
| rproj_k128_s0 | -1.98 | 0.00 | 0.308 | 6.27 |
| rproj_k128_s1 | -2.01 | 0.00 | 0.305 | 6.95 |
| pca_k16 | -2.07 | 0.00 | 0.297 | 6.96 |
| ica_k16 | -2.07 | 0.00 | 0.297 | 6.97 |
| gmm_k100 | -2.09 | 0.00 | 0.294 | 13.71 |
| nystroem_k64_g2 | -2.17 | 0.00 | 0.282 | 11.40 |
| nmf_k16 | -2.34 | 0.00 | 0.261 | 10.13 |
| pca_k8 | -2.40 | 0.00 | 0.253 | 10.45 |
| gmm_k30 | -2.51 | 0.00 | 0.238 | 19.34 |
| rproj_k32_s1 | -2.82 | 0.00 | 0.201 | 8.05 |
| rproj_k32_s0 | -2.86 | 0.00 | 0.196 | 8.86 |
| pca_k4 | -2.91 | 0.00 | 0.191 | 17.47 |
| gmm_k10 | -3.35 | 0.01 | 0.145 | 17.52 |
| rproj_k8_s1 | -3.57 | 0.01 | 0.125 | 18.32 |
| depth2 | -3.77 | 0.01 | 0.108 | 40.06 |
| rproj_k8_s0 | -3.81 | 0.01 | 0.105 | 22.05 |
| random_k32_s1 | -3.89 | 0.01 | 0.099 | 39.95 |
| random_k32_s0 | -3.89 | 0.01 | 0.099 | 39.95 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.453 | 4.0e-234 | 4639 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0002048|intermediate monocyte|SRX9276330 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX15246037 | 5.67 | 0.84 | 0.00 |
| UBERON:0002097|neutrophil|SRX10121878 | 5.67 | 0.84 | 0.00 |
| UBERON:0002048|intermediate monocyte|SRX9927818 | 5.67 | 0.84 | 0.00 |
| UBERON:0002048|intermediate monocyte|SRX17412814 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX9406149 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX21779377 | 5.67 | 0.84 | 0.00 |
| UBERON:0002107|intermediate monocyte|SRX14719058 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX27818977 | 5.67 | 0.84 | 0.00 |
| UBERON:0002107|mature NK T cell|SRX13549270 | 5.67 | 0.84 | 0.00 |
| UBERON:0002107|monocyte|SRX24258454 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX13209841 | 5.67 | 0.84 | 0.00 |
| UBERON:0002371|monocyte|SRX25157535 | 5.67 | 0.84 | 0.00 |
| UBERON:0000029|monocyte|ERX12093802 | 5.67 | 0.84 | 0.00 |
| UBERON:0002107|monocyte|SRX15239530 | 5.67 | 0.84 | 0.00 |

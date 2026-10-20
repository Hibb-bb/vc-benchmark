# Component A summary: repr_pooled_scbasecount_humanall_v0


## cell_level

- items: 581976; informative (non-degenerate): 437625; nobody passes: 141953; everybody passes: 2398
- difficulty percentiles 5/25/50/75/95: [-4.12, -2.53, -1.32, 0.34, 2.04]; median SE 0.47
- histogram (bin lower edge: count): -6: 4034, -5: 20047, -4: 52261, -3: 78443, -2: 88730, -1: 63819, +0: 69510, +1: 24895, +2: 35886, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -0.41 | 0.00 | 0.470 | 0.79 |
| scvi_k30_btissue | -0.51 | 0.00 | 0.459 | 0.76 |
| nystroem_k256_g0.5 | -0.56 | 0.00 | 0.453 | 0.58 |
| pca_k256 | -0.59 | 0.00 | 0.449 | 0.53 |
| pca_k128 | -0.62 | 0.00 | 0.447 | 0.43 |
| nystroem_k64_g0.5 | -0.64 | 0.00 | 0.444 | 0.46 |
| ica_k64 | -0.66 | 0.00 | 0.442 | 0.38 |
| pca_k64 | -0.66 | 0.00 | 0.442 | 0.38 |
| nystroem_k256_g2 | -0.70 | 0.00 | 0.437 | 0.63 |
| scvi_k10_btissue | -0.74 | 0.00 | 0.433 | 0.79 |
| pca_k32 | -0.78 | 0.00 | 0.428 | 0.41 |
| nmf_k64 | -0.90 | 0.00 | 0.414 | 0.59 |
| pca_k16 | -1.24 | 0.00 | 0.376 | 0.43 |
| ica_k16 | -1.24 | 0.00 | 0.376 | 0.43 |
| nystroem_k64_g2 | -1.24 | 0.00 | 0.376 | 0.65 |
| rproj_k128_s0 | -1.27 | 0.00 | 0.373 | 0.84 |
| rproj_k128_s1 | -1.28 | 0.00 | 0.372 | 0.85 |
| gmm_k100 | -1.32 | 0.00 | 0.366 | 0.75 |
| nmf_k16 | -1.44 | 0.00 | 0.353 | 0.60 |
| pca_k8 | -1.67 | 0.00 | 0.327 | 0.62 |
| gmm_k30 | -1.75 | 0.00 | 0.318 | 0.74 |
| pca_k4 | -2.21 | 0.00 | 0.268 | 0.84 |
| rproj_k32_s1 | -2.28 | 0.00 | 0.259 | 1.16 |
| rproj_k32_s0 | -2.32 | 0.00 | 0.255 | 1.24 |
| gmm_k10 | -2.46 | 0.00 | 0.240 | 0.97 |
| rproj_k8_s1 | -3.21 | 0.00 | 0.168 | 1.93 |
| rproj_k8_s0 | -3.33 | 0.00 | 0.157 | 2.10 |
| depth2 | -3.44 | 0.00 | 0.147 | 3.65 |
| random_k32_s0 | -3.77 | 0.00 | 0.122 | 2.19 |
| random_k32_s1 | -3.77 | 0.00 | 0.122 | 2.20 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.068 | 0.0e+00 | 437625 |
| log_total_counts | -0.154 | 0.0e+00 | 437625 |
| n_genes_by_counts | -0.115 | 0.0e+00 | 437625 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| mesenchymal stem cell of adipose tissue | 65.0 | 1.72 | 1433 |
| myofibroblast cell | 144.0 | 1.57 | 230 |
| intermediate monocyte | 233.0 | 1.54 | 226 |
| basophil | 956.0 | 1.31 | 75 |
| monocyte | 1116.0 | 1.23 | 1395 |
| club cell | 270.0 | 0.96 | 137 |
| alveolar adventitial fibroblast | 1208.0 | 0.95 | 396 |
| pulmonary alveolar type 1 cell | 1801.0 | 0.82 | 274 |
| endothelial cell of lymphatic vessel | 958.0 | 0.71 | 138 |
| adventitial cell | 2864.0 | 0.70 | 985 |
| regulatory T cell | 339.0 | 0.59 | 683 |
| endothelial cell of artery | 1977.0 | 0.50 | 908 |
| hematopoietic precursor cell | 5447.0 | 0.41 | 3007 |
| bronchial smooth muscle cell | 940.0 | 0.41 | 827 |
| plasmacytoid dendritic cell | 262.0 | 0.38 | 255 |

## stratum_binomial

- items: 7780; informative (non-degenerate): 7265; nobody passes: 515; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.35, -1.96, -0.79, 0.68, 3.93]; median SE 0.06
- histogram (bin lower edge: count): -6: 1, -5: 49, -4: 625, -3: 1107, -2: 1435, -1: 1469, +0: 1047, +1: 566, +2: 344, +3: 270, +4: 200, +5: 119

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| scvi_k30_bnone | -0.84 | 0.00 | 0.470 | 11.65 |
| scvi_k30_btissue | -0.91 | 0.00 | 0.459 | 10.61 |
| nystroem_k256_g0.5 | -0.95 | 0.00 | 0.453 | 9.74 |
| pca_k256 | -0.98 | 0.00 | 0.449 | 6.89 |
| pca_k128 | -0.99 | 0.00 | 0.447 | 5.93 |
| nystroem_k64_g0.5 | -1.01 | 0.00 | 0.444 | 7.33 |
| ica_k64 | -1.03 | 0.00 | 0.442 | 5.65 |
| pca_k64 | -1.03 | 0.00 | 0.442 | 5.65 |
| nystroem_k256_g2 | -1.06 | 0.00 | 0.437 | 9.66 |
| scvi_k10_btissue | -1.09 | 0.00 | 0.433 | 14.15 |
| pca_k32 | -1.12 | 0.00 | 0.428 | 5.50 |
| nmf_k64 | -1.21 | 0.00 | 0.414 | 6.61 |
| pca_k16 | -1.47 | 0.00 | 0.376 | 8.16 |
| ica_k16 | -1.47 | 0.00 | 0.376 | 8.17 |
| nystroem_k64_g2 | -1.47 | 0.00 | 0.376 | 10.77 |
| rproj_k128_s0 | -1.50 | 0.00 | 0.373 | 6.78 |
| rproj_k128_s1 | -1.50 | 0.00 | 0.372 | 6.24 |
| gmm_k100 | -1.54 | 0.00 | 0.366 | 13.99 |
| nmf_k16 | -1.63 | 0.00 | 0.353 | 10.27 |
| pca_k8 | -1.81 | 0.00 | 0.327 | 12.11 |
| gmm_k30 | -1.87 | 0.00 | 0.318 | 18.36 |
| pca_k4 | -2.24 | 0.00 | 0.268 | 18.03 |
| rproj_k32_s1 | -2.30 | 0.00 | 0.259 | 9.28 |
| rproj_k32_s0 | -2.34 | 0.00 | 0.255 | 10.42 |
| gmm_k10 | -2.46 | 0.00 | 0.240 | 20.38 |
| rproj_k8_s1 | -3.08 | 0.00 | 0.168 | 22.15 |
| rproj_k8_s0 | -3.19 | 0.00 | 0.157 | 24.75 |
| depth2 | -3.28 | 0.00 | 0.147 | 66.24 |
| random_k32_s0 | -3.56 | 0.00 | 0.122 | 59.87 |
| random_k32_s1 | -3.56 | 0.00 | 0.122 | 59.99 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.290 | 1.3e-140 | 7265 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_humanall_multitissue::UBERON:0002107|monocyte|SRX24258454 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000955|oligodendrocyte|SRX11788520 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002371|monocyte|SRX13209841 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000029|monocyte|ERX12093795 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000029|monocyte|ERX12093802 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000955|leukocyte|SRX10868892 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000029|monocyte|ERX12093784 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0000955|leukocyte|SRX8530546 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_blood::UBERON:0000178|B cell|SRX22540099 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002371|monocyte|SRX25157535 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002107|monocyte|SRX15239530 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002371|monocyte|SRX27818977 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002371|monocyte|SRX15246037 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002107|mature NK T cell|SRX13549270 | 6.19 | 0.83 | 0.00 |
| repr_scbasecount_humanall_multitissue::UBERON:0002371|monocyte|SRX21779377 | 6.19 | 0.83 | 0.00 |

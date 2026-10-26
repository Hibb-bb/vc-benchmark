# Component A summary: repr_immune_atlas_donor


## cell_level

- items: 20548; informative (non-degenerate): 19998; nobody passes: 550; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.69, -1.57, -0.46, 1.02, 3.15]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 9, -4: 748, -3: 1999, -2: 4024, -1: 4282, +0: 3723, +1: 2217, +2: 1613, +3: 933, +4: 450, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| fm_geneformer_v2_316m | 2.42 | 0.02 | 0.828 | 1.81 |
| fm_scgpt | 2.26 | 0.02 | 0.814 | 1.60 |
| fm_transcriptformer | 2.20 | 0.02 | 0.808 | 1.64 |
| fm_uce | 2.13 | 0.02 | 0.802 | 1.75 |
| nystroem_k256_g0.5 | 2.01 | 0.02 | 0.782 | 0.45 |
| pca_k128 | 2.00 | 0.02 | 0.781 | 0.47 |
| pca_k64 | 1.94 | 0.02 | 0.775 | 0.37 |
| pca_k256 | 1.94 | 0.02 | 0.775 | 0.64 |
| ica_k64 | 1.94 | 0.02 | 0.775 | 0.37 |
| nystroem_k64_g0.5 | 1.93 | 0.02 | 0.774 | 0.38 |
| fm_state | 1.86 | 0.02 | 0.774 | 1.66 |
| nystroem_k256_g2 | 1.85 | 0.02 | 0.766 | 0.52 |
| scvi_k30_bnone | 1.82 | 0.02 | 0.763 | 0.81 |
| scvi_k30_btissue | 1.79 | 0.02 | 0.760 | 0.83 |
| pca_k32 | 1.59 | 0.02 | 0.739 | 0.49 |
| scvi_k10_btissue | 1.47 | 0.02 | 0.725 | 0.86 |
| nystroem_k64_g2 | 1.39 | 0.02 | 0.716 | 1.12 |
| fm_cellplm | 1.22 | 0.02 | 0.700 | 1.43 |
| nmf_k64 | 1.21 | 0.02 | 0.694 | 0.97 |
| rproj_k128_s1 | 0.77 | 0.02 | 0.638 | 1.00 |
| rproj_k128_s0 | 0.72 | 0.02 | 0.631 | 1.05 |
| pca_k16 | 0.71 | 0.02 | 0.629 | 0.67 |
| ica_k16 | 0.71 | 0.02 | 0.629 | 0.67 |
| fm_scprint_large_v1 | 0.71 | 0.02 | 0.633 | 1.82 |
| gmm_k100 | 0.23 | 0.02 | 0.561 | 1.10 |
| nmf_k16 | 0.12 | 0.02 | 0.544 | 1.12 |
| pca_k8 | -0.04 | 0.02 | 0.520 | 0.95 |
| gmm_k30 | -0.45 | 0.02 | 0.458 | 1.07 |
| rproj_k32_s1 | -0.82 | 0.02 | 0.401 | 1.48 |
| rproj_k32_s0 | -0.87 | 0.02 | 0.392 | 1.53 |
| pca_k4 | -0.98 | 0.02 | 0.375 | 1.44 |
| gmm_k10 | -1.69 | 0.02 | 0.271 | 2.27 |
| rproj_k8_s1 | -2.39 | 0.02 | 0.184 | 2.64 |
| rproj_k8_s0 | -2.62 | 0.02 | 0.159 | 2.58 |
| depth2 | -2.64 | 0.02 | 0.156 | 3.69 |
| random_k32_s1 | -3.86 | 0.03 | 0.064 | 7.51 |
| random_k32_s0 | -3.90 | 0.03 | 0.061 | 8.35 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.245 | 3.3e-271 | 19998 |
| log_total_counts | -0.106 | 1.1e-50 | 19998 |
| n_genes_by_counts | -0.120 | 1.6e-65 | 19998 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| T/B doublets | 262.0 | 2.08 | 584 |
| MNP/T doublets | 85.0 | 2.06 | 1262 |
| Tfh | 781.0 | 1.74 | 2713 |
| ABCs | 296.0 | 1.69 | 391 |
| Tnaive/CM_CD4_activated | 351.0 | 1.60 | 730 |
| MNP/B doublets | 215.0 | 1.39 | 243 |
| Trm_gut_CD8 | 549.0 | 1.34 | 2031 |
| migDC | 38.0 | 1.26 | 54 |
| Tnaive/CM_CD8 | 877.0 | 1.01 | 1805 |
| Trm_Th1/Th17 | 807.0 | 1.00 | 3378 |
| GC_B (I) | 107.0 | 0.89 | 47 |
| Cycling | 103.0 | 0.77 | 518 |
| Tgd_CRTAM+ | 512.0 | 0.71 | 1518 |
| MAIT | 468.0 | 0.66 | 1890 |
| DC1 | 21.0 | 0.59 | 98 |

## stratum_binomial

- items: 474; informative (non-degenerate): 474; nobody passes: 0; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.75, -0.89, -0.05, 0.77, 1.94]; median SE 0.07
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 13, -2: 91, -1: 144, +0: 133, +1: 71, +2: 20, +3: 2, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| fm_geneformer_v2_316m | 1.86 | 0.02 | 0.828 | 4.94 |
| fm_scgpt | 1.75 | 0.02 | 0.814 | 4.48 |
| fm_transcriptformer | 1.70 | 0.02 | 0.808 | 6.00 |
| fm_uce | 1.65 | 0.02 | 0.802 | 4.52 |
| nystroem_k256_g0.5 | 1.50 | 0.02 | 0.782 | 2.58 |
| pca_k128 | 1.50 | 0.02 | 0.781 | 2.16 |
| pca_k64 | 1.46 | 0.02 | 0.775 | 2.09 |
| pca_k256 | 1.46 | 0.02 | 0.775 | 2.35 |
| ica_k64 | 1.45 | 0.02 | 0.775 | 2.10 |
| fm_state | 1.45 | 0.02 | 0.774 | 3.89 |
| nystroem_k64_g0.5 | 1.45 | 0.02 | 0.774 | 2.06 |
| nystroem_k256_g2 | 1.39 | 0.02 | 0.766 | 2.63 |
| scvi_k30_bnone | 1.37 | 0.02 | 0.763 | 2.67 |
| scvi_k30_btissue | 1.36 | 0.02 | 0.760 | 3.01 |
| pca_k32 | 1.21 | 0.02 | 0.739 | 2.14 |
| scvi_k10_btissue | 1.13 | 0.02 | 0.725 | 3.53 |
| nystroem_k64_g2 | 1.08 | 0.02 | 0.716 | 10.59 |
| fm_cellplm | 0.98 | 0.02 | 0.700 | 6.81 |
| nmf_k64 | 0.94 | 0.02 | 0.694 | 4.55 |
| rproj_k128_s1 | 0.63 | 0.02 | 0.638 | 2.84 |
| fm_scprint_large_v1 | 0.60 | 0.02 | 0.633 | 5.16 |
| rproj_k128_s0 | 0.59 | 0.02 | 0.631 | 3.27 |
| pca_k16 | 0.58 | 0.02 | 0.629 | 3.64 |
| ica_k16 | 0.58 | 0.02 | 0.629 | 3.64 |
| gmm_k100 | 0.22 | 0.02 | 0.561 | 9.78 |
| nmf_k16 | 0.14 | 0.02 | 0.544 | 7.07 |
| pca_k8 | 0.02 | 0.02 | 0.520 | 4.39 |
| gmm_k30 | -0.30 | 0.02 | 0.458 | 15.02 |
| rproj_k32_s1 | -0.59 | 0.02 | 0.401 | 3.44 |
| rproj_k32_s0 | -0.63 | 0.02 | 0.392 | 3.95 |
| pca_k4 | -0.72 | 0.02 | 0.375 | 8.95 |
| gmm_k10 | -1.31 | 0.02 | 0.271 | 24.65 |
| rproj_k8_s1 | -1.91 | 0.02 | 0.184 | 4.56 |
| rproj_k8_s0 | -2.11 | 0.02 | 0.159 | 4.40 |
| depth2 | -2.13 | 0.02 | 0.156 | 21.56 |
| random_k32_s1 | -3.24 | 0.03 | 0.064 | 22.40 |
| random_k32_s0 | -3.28 | 0.03 | 0.061 | 23.58 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.361 | 4.9e-16 | 474 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| thoracic lymph node|GC_B (II)|A35 | 3.67 | 0.16 | 0.05 |
| mesenteric lymph node|T/B doublets|A29 | 3.18 | 0.15 | 0.08 |
| thoracic lymph node|T/B doublets|621B | 2.76 | 0.13 | 0.11 |
| mesenteric lymph node|Tnaive/CM_CD4_activated|A35 | 2.65 | 0.09 | 0.12 |
| liver|T_CD4/CD8|A31 | 2.62 | 0.10 | 0.12 |
| thoracic lymph node|T/B doublets|582C | 2.56 | 0.08 | 0.13 |
| thoracic lymph node|MNP/B doublets|582C | 2.50 | 0.09 | 0.14 |
| thoracic lymph node|T/B doublets|A31 | 2.46 | 0.08 | 0.14 |
| thoracic lymph node|Tnaive/CM_CD4_activated|A29 | 2.44 | 0.11 | 0.14 |
| spleen|T/B doublets|582C | 2.35 | 0.07 | 0.15 |
| thoracic lymph node|Tnaive/CM_CD4_activated|A31 | 2.33 | 0.09 | 0.16 |
| thoracic lymph node|Tfh|582C | 2.31 | 0.07 | 0.16 |
| spleen|MNP/T doublets|582C | 2.31 | 0.10 | 0.16 |
| spleen|Tfh|582C | 2.27 | 0.07 | 0.16 |
| thoracic lymph node|ABCs|A31 | 2.25 | 0.10 | 0.17 |

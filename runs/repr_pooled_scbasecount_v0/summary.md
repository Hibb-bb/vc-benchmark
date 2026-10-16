# Component A summary: repr_pooled_scbasecount_v0


## cell_level

- items: 197166; informative (non-degenerate): 160894; nobody passes: 35831; everybody passes: 441
- difficulty percentiles 5/25/50/75/95: [-3.6, -2.34, -1.1, 0.67, 2.39]; median SE 0.50
- histogram (bin lower edge: count): -6: 0, -5: 3735, -4: 14150, -3: 34914, -2: 30566, -1: 21084, +0: 26454, +1: 17048, +2: 12943, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.09 | 0.01 | 0.514 | 0.48 |
| nystroem_k64_g0.5 | -0.12 | 0.01 | 0.510 | 0.37 |
| pca_k128 | -0.13 | 0.01 | 0.509 | 0.42 |
| pca_k64 | -0.14 | 0.01 | 0.508 | 0.35 |
| ica_k64 | -0.14 | 0.01 | 0.507 | 0.35 |
| nystroem_k256_g2 | -0.14 | 0.01 | 0.507 | 0.53 |
| pca_k256 | -0.18 | 0.01 | 0.502 | 0.51 |
| pca_k32 | -0.25 | 0.01 | 0.495 | 0.38 |
| nmf_k64 | -0.27 | 0.01 | 0.493 | 0.59 |
| nystroem_k64_g2 | -0.35 | 0.01 | 0.483 | 0.53 |
| ica_k16 | -0.53 | 0.01 | 0.461 | 0.43 |
| pca_k16 | -0.53 | 0.01 | 0.461 | 0.43 |
| gmm_k100 | -0.62 | 0.01 | 0.451 | 0.79 |
| nmf_k16 | -0.67 | 0.01 | 0.445 | 0.71 |
| rproj_k128_s1 | -0.73 | 0.01 | 0.437 | 0.80 |
| rproj_k128_s0 | -0.74 | 0.01 | 0.436 | 0.75 |
| gmm_k30 | -0.98 | 0.01 | 0.407 | 0.89 |
| pca_k8 | -1.06 | 0.01 | 0.397 | 0.76 |
| rproj_k32_s0 | -1.54 | 0.01 | 0.338 | 1.12 |
| rproj_k32_s1 | -1.60 | 0.01 | 0.330 | 1.21 |
| pca_k4 | -1.70 | 0.01 | 0.318 | 1.19 |
| gmm_k10 | -1.85 | 0.01 | 0.299 | 1.58 |
| rproj_k8_s0 | -2.64 | 0.01 | 0.207 | 2.13 |
| rproj_k8_s1 | -2.72 | 0.01 | 0.198 | 2.38 |
| depth2 | -2.95 | 0.01 | 0.175 | 4.49 |
| random_k32_s1 | -3.71 | 0.01 | 0.109 | 5.10 |
| random_k32_s0 | -3.71 | 0.01 | 0.109 | 5.08 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.031 | 2.3e-36 | 160894 |
| log_total_counts | -0.162 | 0.0e+00 | 160894 |
| n_genes_by_counts | -0.143 | 0.0e+00 | 160894 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| duct epithelial cell | 151.0 | 1.78 | 482 |
| lymphoid lineage restricted progenitor cell | 36.0 | 1.58 | 437 |
| granulocyte monocyte progenitor cell | 811.0 | 1.10 | 1762 |
| leukocyte | 816.0 | 0.62 | 3583 |
| macrophage dendritic cell progenitor | 540.0 | 0.60 | 882 |
| naive thymus-derived CD4-positive, alpha-beta T cell | 2242.0 | 0.29 | 5349 |
| common myeloid progenitor | 709.0 | 0.28 | 1456 |
| early pro-B cell | 203.0 | 0.18 | 945 |
| neuroepithelial stem cell | 1015.0 | 0.18 | 3035 |
| intermediate monocyte | 1952.0 | 0.17 | 606 |
| interneuron | 533.0 | 0.14 | 1401 |
| late pro-B cell | 59.0 | 0.11 | 454 |
| lymphocyte | 226.0 | 0.03 | 232 |
| granulocytopoietic cell | 1356.0 | -0.00 | 5255 |
| club cell | 918.0 | -0.03 | 292 |

## stratum_binomial

- items: 2547; informative (non-degenerate): 2478; nobody passes: 69; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.66, -1.51, -0.56, 0.8, 3.78]; median SE 0.05
- histogram (bin lower edge: count): -6: 1, -5: 6, -4: 44, -3: 287, -2: 599, -1: 611, +0: 368, +1: 235, +2: 130, +3: 84, +4: 52, +5: 35

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nystroem_k256_g0.5 | -0.37 | 0.01 | 0.514 | 6.06 |
| nystroem_k64_g0.5 | -0.39 | 0.01 | 0.510 | 5.10 |
| pca_k128 | -0.40 | 0.01 | 0.509 | 5.73 |
| pca_k64 | -0.41 | 0.01 | 0.508 | 4.83 |
| ica_k64 | -0.41 | 0.01 | 0.507 | 4.82 |
| nystroem_k256_g2 | -0.41 | 0.01 | 0.507 | 6.88 |
| pca_k256 | -0.44 | 0.01 | 0.502 | 5.12 |
| pca_k32 | -0.49 | 0.01 | 0.495 | 4.58 |
| nmf_k64 | -0.50 | 0.01 | 0.493 | 6.65 |
| nystroem_k64_g2 | -0.56 | 0.01 | 0.483 | 8.76 |
| ica_k16 | -0.69 | 0.01 | 0.461 | 6.21 |
| pca_k16 | -0.69 | 0.01 | 0.461 | 6.20 |
| gmm_k100 | -0.75 | 0.01 | 0.451 | 14.46 |
| nmf_k16 | -0.78 | 0.01 | 0.445 | 10.72 |
| rproj_k128_s1 | -0.83 | 0.01 | 0.437 | 5.76 |
| rproj_k128_s0 | -0.84 | 0.01 | 0.436 | 4.52 |
| gmm_k30 | -1.01 | 0.01 | 0.407 | 21.77 |
| pca_k8 | -1.07 | 0.01 | 0.397 | 13.99 |
| rproj_k32_s0 | -1.43 | 0.01 | 0.338 | 7.90 |
| rproj_k32_s1 | -1.48 | 0.01 | 0.330 | 9.60 |
| pca_k4 | -1.56 | 0.01 | 0.318 | 23.56 |
| gmm_k10 | -1.68 | 0.01 | 0.299 | 45.37 |
| rproj_k8_s0 | -2.33 | 0.01 | 0.207 | 17.87 |
| rproj_k8_s1 | -2.40 | 0.01 | 0.198 | 19.37 |
| depth2 | -2.59 | 0.01 | 0.175 | 74.85 |
| random_k32_s1 | -3.26 | 0.01 | 0.109 | 80.82 |
| random_k32_s0 | -3.26 | 0.01 | 0.109 | 78.72 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.225 | 1.1e-29 | 2478 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| repr_scbasecount_human_lung::UBERON:0002048|mature NK T cell|SRX13061245 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002370|erythrocyte|SRX7691515 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_mouse_liver::UBERON:0002107|T cell|SRX13549189 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_mouse_brain::UBERON:0000955|T cell|SRX26076718 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_mouse_brain::UBERON:0000955|oligodendrocyte precursor cell|SRX19355853 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0002097|neutrophil|SRX27532049 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_mouse_bone_marrow::UBERON:0002371|mature alpha-beta T cell|SRX15637240 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|plasma cell|SRX10112709 | 6.67 | 0.82 | 0.00 |
| repr_scbasecount_mouse_liver::UBERON:0002107|mature NK T cell|SRX10605823 | 6.58 | 0.82 | 0.00 |
| repr_scbasecount_human_multitissue::UBERON:0000029|natural killer cell|ERX12093805 | 6.49 | 0.83 | 0.00 |
| repr_scbasecount_mouse_lung::UBERON:0002048|plasmacytoid dendritic cell|SRX15126716 | 6.48 | 0.83 | 0.00 |
| repr_scbasecount_mouse_bone_marrow::UBERON:0002371|late pro-B cell|SRX11609965 | 6.26 | 0.83 | 0.00 |
| repr_scbasecount_mouse_lung::UBERON:0002048|club cell|SRX23858293 | 6.23 | 0.83 | 0.00 |
| repr_scbasecount_human_liver::UBERON:0002107|intermediate monocyte|SRX13549256 | 6.23 | 0.83 | 0.00 |
| repr_scbasecount_mouse_spleen::UBERON:0002106|CD8-positive, alpha-beta T cell|SRX19818527 | 6.15 | 0.64 | 0.00 |

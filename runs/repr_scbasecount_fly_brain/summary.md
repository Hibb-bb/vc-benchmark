# Component A summary: repr_scbasecount_fly_brain


## cell_level

- items: 4412; informative (non-degenerate): 3395; nobody passes: 943; everybody passes: 74
- difficulty percentiles 5/25/50/75/95: [-3.67, -2.38, -1.06, 0.4, 2.33]; median SE 0.48
- histogram (bin lower edge: count): -6: 0, -5: 117, -4: 360, -3: 553, -2: 746, -1: 660, +0: 353, +1: 319, +2: 287, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -0.17 | 0.04 | 0.501 | 1.03 |
| nmf_k16 | -0.23 | 0.04 | 0.495 | 0.72 |
| ica_k64 | -0.28 | 0.04 | 0.489 | 0.40 |
| nystroem_k64_g0.5 | -0.29 | 0.04 | 0.488 | 0.47 |
| pca_k64 | -0.29 | 0.04 | 0.488 | 0.40 |
| pca_k32 | -0.29 | 0.04 | 0.488 | 0.43 |
| pca_k128 | -0.29 | 0.04 | 0.488 | 0.50 |
| pca_k256 | -0.30 | 0.04 | 0.487 | 0.69 |
| nystroem_k256_g2 | -0.31 | 0.04 | 0.486 | 0.72 |
| nystroem_k256_g0.5 | -0.32 | 0.04 | 0.484 | 0.64 |
| nystroem_k64_g2 | -0.39 | 0.04 | 0.476 | 0.51 |
| gmm_k100 | -0.52 | 0.04 | 0.461 | 0.77 |
| pca_k16 | -0.79 | 0.04 | 0.429 | 0.49 |
| ica_k16 | -0.79 | 0.04 | 0.429 | 0.49 |
| rproj_k128_s1 | -0.95 | 0.04 | 0.410 | 0.92 |
| gmm_k30 | -0.99 | 0.04 | 0.405 | 0.61 |
| rproj_k128_s0 | -1.05 | 0.04 | 0.398 | 0.96 |
| pca_k8 | -1.24 | 0.04 | 0.376 | 0.53 |
| gmm_k10 | -1.42 | 0.04 | 0.353 | 0.64 |
| pca_k4 | -1.50 | 0.04 | 0.344 | 0.66 |
| rproj_k32_s1 | -1.61 | 0.04 | 0.332 | 1.13 |
| rproj_k32_s0 | -1.74 | 0.04 | 0.316 | 1.10 |
| depth2 | -2.03 | 0.04 | 0.282 | 1.72 |
| rproj_k8_s0 | -2.10 | 0.04 | 0.274 | 1.22 |
| rproj_k8_s1 | -2.21 | 0.05 | 0.262 | 1.69 |
| random_k32_s0 | -2.53 | 0.05 | 0.227 | 1.77 |
| random_k32_s1 | -2.53 | 0.05 | 0.227 | 1.56 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.426 | 5.5e-150 | 3395 |
| log_total_counts | 0.091 | 1.3e-07 | 3395 |
| n_genes_by_counts | 0.138 | 7.5e-16 | 3395 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| sensory neuron | 283.0 | 0.34 | 836 |
| epithelial cell | 504.0 | -0.21 | 894 |
| muscle cell | 374.0 | -0.43 | 859 |
| hemocyte | 467.0 | -0.77 | 1000 |
| glial cell | 836.0 | -0.80 | 2317 |
| neuron | 926.0 | -2.20 | 2800 |

## stratum_binomial

- items: 52; informative (non-degenerate): 48; nobody passes: 4; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.46, -1.51, -0.68, 0.3, 4.3]; median SE 0.04
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 7, -2: 10, -1: 14, +0: 5, +1: 2, +2: 2, +3: 3, +4: 2, +5: 2

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -0.66 | 0.04 | 0.501 | 8.61 |
| nmf_k16 | -0.69 | 0.04 | 0.495 | 6.88 |
| ica_k64 | -0.72 | 0.04 | 0.489 | 4.10 |
| nystroem_k64_g0.5 | -0.73 | 0.04 | 0.488 | 6.05 |
| pca_k64 | -0.73 | 0.04 | 0.488 | 4.18 |
| pca_k32 | -0.73 | 0.04 | 0.488 | 4.82 |
| pca_k128 | -0.73 | 0.04 | 0.488 | 4.45 |
| pca_k256 | -0.74 | 0.04 | 0.487 | 6.73 |
| nystroem_k256_g2 | -0.74 | 0.04 | 0.486 | 8.13 |
| nystroem_k256_g0.5 | -0.75 | 0.04 | 0.484 | 7.34 |
| nystroem_k64_g2 | -0.79 | 0.04 | 0.476 | 6.20 |
| gmm_k100 | -0.88 | 0.04 | 0.461 | 7.84 |
| pca_k16 | -1.05 | 0.04 | 0.429 | 3.07 |
| ica_k16 | -1.05 | 0.04 | 0.429 | 3.07 |
| rproj_k128_s1 | -1.16 | 0.04 | 0.410 | 4.45 |
| gmm_k30 | -1.18 | 0.04 | 0.405 | 6.56 |
| rproj_k128_s0 | -1.22 | 0.04 | 0.398 | 3.96 |
| pca_k8 | -1.35 | 0.04 | 0.376 | 6.69 |
| gmm_k10 | -1.48 | 0.04 | 0.353 | 14.41 |
| pca_k4 | -1.53 | 0.04 | 0.344 | 11.80 |
| rproj_k32_s1 | -1.60 | 0.04 | 0.332 | 3.78 |
| rproj_k32_s0 | -1.69 | 0.04 | 0.316 | 3.42 |
| depth2 | -1.90 | 0.04 | 0.282 | 16.95 |
| rproj_k8_s0 | -1.95 | 0.04 | 0.274 | 15.76 |
| rproj_k8_s1 | -2.02 | 0.04 | 0.262 | 16.33 |
| random_k32_s0 | -2.26 | 0.04 | 0.227 | 21.62 |
| random_k32_s1 | -2.26 | 0.04 | 0.227 | 21.26 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_n_train_same_type | -0.841 | 7.1e-14 | 48 |

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000955|sensory neuron|SRX24027819 | 5.68 | 0.84 | 0.00 |
| UBERON:0000955|sensory neuron|SRX24027829 | 5.31 | 0.65 | 0.00 |
| UBERON:0000955|muscle cell|SRX24027823 | 4.36 | 0.48 | 0.00 |
| UBERON:0000955|sensory neuron|SRX24027823 | 4.19 | 0.55 | 0.00 |
| UBERON:0000955|fat cell|SRX21466964 | 3.95 | 0.37 | 0.01 |
| UBERON:0000955|fat cell|SRX22169673 | 3.72 | 0.22 | 0.01 |
| UBERON:0000955|fat cell|SRX22169678 | 3.50 | 0.40 | 0.01 |
| UBERON:0000955|epithelial cell|SRX22169678 | 2.28 | 0.11 | 0.03 |
| UBERON:0000955|epithelial cell|SRX22169673 | 2.14 | 0.13 | 0.04 |
| UBERON:0000955|epithelial cell|SRX22169674 | 1.96 | 0.11 | 0.04 |
| UBERON:0000955|epithelial cell|SRX21466964 | 1.27 | 0.08 | 0.08 |
| UBERON:0000955|sensory neuron|SRX22169674 | 0.62 | 0.05 | 0.15 |
| UBERON:0000955|sensory neuron|SRX22169678 | 0.19 | 0.05 | 0.21 |
| UBERON:0000955|sensory neuron|SRX21466964 | 0.06 | 0.05 | 0.23 |
| UBERON:0000955|epithelial cell|SRX24027817 | 0.03 | 0.05 | 0.24 |

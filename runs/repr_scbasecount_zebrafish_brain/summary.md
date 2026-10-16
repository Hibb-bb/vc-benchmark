# Component A summary: repr_scbasecount_zebrafish_brain


## cell_level

- items: 3011; informative (non-degenerate): 2536; nobody passes: 456; everybody passes: 19
- difficulty percentiles 5/25/50/75/95: [-3.12, -2.13, -1.02, 0.86, 2.51]; median SE 0.49
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 201, -3: 568, -2: 515, -1: 303, +0: 367, +1: 397, +2: 185, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -0.20 | 0.05 | 0.499 | 1.22 |
| nmf_k16 | -0.26 | 0.05 | 0.492 | 1.36 |
| pca_k256 | -0.26 | 0.05 | 0.491 | 0.52 |
| pca_k128 | -0.39 | 0.05 | 0.476 | 0.40 |
| pca_k16 | -0.40 | 0.05 | 0.475 | 0.39 |
| ica_k16 | -0.40 | 0.05 | 0.475 | 0.39 |
| pca_k64 | -0.43 | 0.05 | 0.471 | 0.33 |
| ica_k64 | -0.43 | 0.05 | 0.470 | 0.34 |
| pca_k32 | -0.45 | 0.05 | 0.468 | 0.36 |
| nystroem_k64_g2 | -0.45 | 0.05 | 0.468 | 0.42 |
| gmm_k30 | -0.45 | 0.05 | 0.467 | 0.54 |
| pca_k8 | -0.49 | 0.05 | 0.463 | 0.52 |
| nystroem_k64_g0.5 | -0.50 | 0.05 | 0.462 | 0.36 |
| gmm_k10 | -0.54 | 0.05 | 0.456 | 0.47 |
| pca_k4 | -0.55 | 0.05 | 0.455 | 0.71 |
| nystroem_k256_g2 | -0.61 | 0.05 | 0.448 | 0.56 |
| rproj_k128_s0 | -0.61 | 0.05 | 0.447 | 0.95 |
| nystroem_k256_g0.5 | -0.63 | 0.05 | 0.445 | 0.54 |
| rproj_k128_s1 | -0.68 | 0.05 | 0.439 | 0.94 |
| gmm_k100 | -0.70 | 0.05 | 0.436 | 0.57 |
| depth2 | -0.90 | 0.05 | 0.411 | 1.81 |
| rproj_k32_s1 | -0.96 | 0.05 | 0.403 | 1.08 |
| rproj_k8_s1 | -1.06 | 0.05 | 0.390 | 1.24 |
| rproj_k32_s0 | -1.13 | 0.05 | 0.381 | 1.12 |
| rproj_k8_s0 | -1.25 | 0.05 | 0.366 | 1.25 |
| random_k32_s1 | -1.29 | 0.05 | 0.360 | 1.80 |
| random_k32_s0 | -1.38 | 0.05 | 0.349 | 1.93 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_total_counts | -0.225 | 1.5e-30 | 2536 |
| n_genes_by_counts | -0.210 | 9.6e-27 | 2536 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| lateral motor column neuron | 360.0 | 1.76 | 1582 |
| motor neuron | 1086.0 | -0.81 | 3000 |
| cranial motor neuron | 1090.0 | -1.36 | 3000 |

## stratum_binomial

- items: 33; informative (non-degenerate): 32; nobody passes: 1; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.9, -1.18, -0.52, 1.86, 2.88]; median SE 0.04
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 1, -2: 11, -1: 9, +0: 0, +1: 3, +2: 6, +3: 1, +4: 1, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -0.24 | 0.05 | 0.499 | 47.04 |
| nmf_k16 | -0.28 | 0.05 | 0.492 | 54.05 |
| pca_k256 | -0.28 | 0.05 | 0.491 | 4.06 |
| pca_k128 | -0.38 | 0.04 | 0.476 | 3.11 |
| pca_k16 | -0.38 | 0.04 | 0.475 | 4.54 |
| ica_k16 | -0.38 | 0.04 | 0.475 | 4.54 |
| pca_k64 | -0.41 | 0.04 | 0.471 | 2.94 |
| ica_k64 | -0.41 | 0.04 | 0.470 | 2.93 |
| pca_k32 | -0.42 | 0.04 | 0.468 | 4.04 |
| nystroem_k64_g2 | -0.42 | 0.04 | 0.468 | 2.13 |
| gmm_k30 | -0.43 | 0.04 | 0.467 | 7.16 |
| pca_k8 | -0.45 | 0.04 | 0.463 | 7.61 |
| nystroem_k64_g0.5 | -0.46 | 0.04 | 0.462 | 2.25 |
| gmm_k10 | -0.49 | 0.04 | 0.456 | 6.05 |
| pca_k4 | -0.50 | 0.04 | 0.455 | 14.07 |
| nystroem_k256_g2 | -0.54 | 0.04 | 0.448 | 2.20 |
| rproj_k128_s0 | -0.55 | 0.04 | 0.447 | 3.90 |
| nystroem_k256_g0.5 | -0.56 | 0.04 | 0.445 | 2.45 |
| rproj_k128_s1 | -0.59 | 0.04 | 0.439 | 3.76 |
| gmm_k100 | -0.61 | 0.04 | 0.436 | 6.52 |
| depth2 | -0.76 | 0.04 | 0.411 | 66.66 |
| rproj_k32_s1 | -0.81 | 0.04 | 0.403 | 3.25 |
| rproj_k8_s1 | -0.88 | 0.04 | 0.390 | 5.20 |
| rproj_k32_s0 | -0.93 | 0.04 | 0.381 | 8.06 |
| rproj_k8_s0 | -1.02 | 0.04 | 0.366 | 7.43 |
| random_k32_s1 | -1.05 | 0.04 | 0.360 | 14.48 |
| random_k32_s0 | -1.11 | 0.04 | 0.349 | 13.34 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| UBERON:0000955|lateral motor column neuron|SRX17478036 | 4.01 | 0.19 | 0.01 |
| UBERON:0000955|lateral motor column neuron|SRX9142589 | 3.10 | 0.12 | 0.03 |
| UBERON:0000955|lateral motor column neuron|SRX22323894 | 2.71 | 0.16 | 0.04 |
| UBERON:0000955|lateral motor column neuron|SRX9142587 | 2.46 | 0.15 | 0.05 |
| UBERON:0000955|lateral motor column neuron|SRX9142599 | 2.37 | 0.09 | 0.05 |
| UBERON:0000955|lateral motor column neuron|SRX9142602 | 2.19 | 0.16 | 0.06 |
| UBERON:0000955|lateral motor column neuron|SRX9142585 | 2.12 | 0.10 | 0.07 |
| UBERON:0000955|lateral motor column neuron|SRX9142593 | 2.03 | 0.08 | 0.07 |
| UBERON:0000955|lateral motor column neuron|SRX9142595 | 1.80 | 0.11 | 0.09 |
| UBERON:0000955|lateral motor column neuron|SRX9142632 | 1.64 | 0.06 | 0.10 |
| UBERON:0000955|motor neuron|SRX22323894 | 1.50 | 0.06 | 0.11 |
| UBERON:0000955|motor neuron|SRX9142585 | -0.23 | 0.04 | 0.42 |
| UBERON:0000955|cranial motor neuron|SRX9142599 | -0.34 | 0.04 | 0.44 |
| UBERON:0000955|cranial motor neuron|SRX9142602 | -0.43 | 0.04 | 0.47 |
| UBERON:0000955|motor neuron|SRX9142632 | -0.48 | 0.04 | 0.48 |

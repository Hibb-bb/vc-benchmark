# Component A summary: repr_parse_pbmc_cytokine


## cell_level

- items: 2275; informative (non-degenerate): 539; nobody passes: 1736; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.51, -3.06, -1.81, -1.81, -1.81]; median SE 1.05
- histogram (bin lower edge: count): -6: 15, -5: 31, -4: 123, -3: 93, -2: 276, -1: 0, +0: 0, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -4.44 | 0.12 | 0.043 | 0.30 |
| nystroem_k64_g0.5 | -4.70 | 0.13 | 0.035 | 0.18 |
| pca_k128 | -4.72 | 0.13 | 0.035 | 0.26 |
| pca_k64 | -4.92 | 0.14 | 0.030 | 0.12 |
| ica_k64 | -4.92 | 0.14 | 0.030 | 0.12 |
| nystroem_k256_g0.5 | -4.94 | 0.14 | 0.029 | 0.23 |
| pca_k32 | -4.94 | 0.14 | 0.029 | 0.17 |
| ica_k16 | -4.96 | 0.14 | 0.029 | 0.13 |
| pca_k16 | -4.98 | 0.14 | 0.029 | 0.13 |
| nmf_k16 | -4.98 | 0.14 | 0.029 | 0.20 |
| pca_k256 | -5.00 | 0.14 | 0.028 | 0.27 |
| gmm_k30 | -5.06 | 0.14 | 0.027 | 0.27 |
| pca_k8 | -5.06 | 0.14 | 0.027 | 0.22 |
| nystroem_k256_g2 | -5.10 | 0.15 | 0.026 | 0.24 |
| nystroem_k64_g2 | -5.12 | 0.15 | 0.025 | 0.20 |
| rproj_k128_s1 | -5.24 | 0.15 | 0.023 | 0.34 |
| gmm_k100 | -5.31 | 0.16 | 0.022 | 0.31 |
| pca_k4 | -5.36 | 0.16 | 0.021 | 0.28 |
| rproj_k128_s0 | -5.47 | 0.17 | 0.019 | 0.35 |
| rproj_k32_s0 | -5.71 | 0.18 | 0.016 | 0.36 |
| gmm_k10 | -5.78 | 0.19 | 0.015 | 0.32 |
| rproj_k8_s0 | -5.81 | 0.19 | 0.015 | 0.45 |
| rproj_k8_s1 | -5.96 | 0.20 | 0.013 | 0.46 |
| depth2 | -6.08 | 0.21 | 0.011 | 0.56 |
| random_k32_s0 | -6.08 | 0.21 | 0.011 | 0.68 |
| rproj_k32_s1 | -6.08 | 0.21 | 0.011 | 0.40 |
| random_k32_s1 | -6.43 | 0.24 | 0.008 | 0.69 |

### Difficulty vs covariates (prediction: rare types and shallow cells are hard)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| log_total_counts | -0.111 | 1.0e-02 | 539 |
| n_genes_by_counts | -0.102 | 1.8e-02 | 539 |

### Hardest 15 cell types (mean cell difficulty, >= 20 items)

| cell type | n | mean difficulty | train cells |
|---|---|---|---|
| CD40L | 23.0 | -2.63 | 70 |
| IL-4 | 20.0 | -4.74 | 70 |

## stratum_binomial

- items: 455; informative (non-degenerate): 296; nobody passes: 159; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.49, -1.15, -0.21, 0.45, 0.45]; median SE 0.70
- histogram (bin lower edge: count): -6: 0, -5: 1, -4: 7, -3: 21, -2: 60, -1: 105, +0: 102, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| nmf_k64 | -3.74 | 0.11 | 0.043 | 0.78 |
| nystroem_k64_g0.5 | -3.97 | 0.12 | 0.035 | 0.42 |
| pca_k128 | -3.98 | 0.12 | 0.035 | 0.54 |
| pca_k64 | -4.16 | 0.13 | 0.030 | 0.29 |
| ica_k64 | -4.16 | 0.13 | 0.030 | 0.29 |
| nystroem_k256_g0.5 | -4.18 | 0.13 | 0.029 | 0.42 |
| pca_k32 | -4.18 | 0.13 | 0.029 | 0.43 |
| ica_k16 | -4.19 | 0.13 | 0.029 | 0.35 |
| pca_k16 | -4.21 | 0.13 | 0.029 | 0.34 |
| nmf_k16 | -4.21 | 0.13 | 0.029 | 0.42 |
| pca_k256 | -4.23 | 0.13 | 0.028 | 0.72 |
| gmm_k30 | -4.28 | 0.14 | 0.027 | 0.67 |
| pca_k8 | -4.28 | 0.14 | 0.027 | 0.62 |
| nystroem_k256_g2 | -4.32 | 0.14 | 0.026 | 0.59 |
| nystroem_k64_g2 | -4.34 | 0.14 | 0.025 | 0.43 |
| rproj_k128_s1 | -4.45 | 0.15 | 0.023 | 0.88 |
| gmm_k100 | -4.51 | 0.15 | 0.022 | 0.79 |
| pca_k4 | -4.56 | 0.15 | 0.021 | 0.78 |
| rproj_k128_s0 | -4.65 | 0.16 | 0.019 | 1.04 |
| rproj_k32_s0 | -4.88 | 0.17 | 0.016 | 0.83 |
| gmm_k10 | -4.94 | 0.18 | 0.015 | 1.01 |
| rproj_k8_s0 | -4.97 | 0.18 | 0.015 | 1.24 |
| rproj_k8_s1 | -5.11 | 0.19 | 0.013 | 1.44 |
| depth2 | -5.23 | 0.20 | 0.011 | 1.80 |
| random_k32_s0 | -5.23 | 0.20 | 0.011 | 1.89 |
| rproj_k32_s1 | -5.23 | 0.20 | 0.011 | 1.21 |
| random_k32_s1 | -5.55 | 0.23 | 0.008 | 1.99 |

### Stratum difficulty vs train support

| covariate | Spearman rho | p | n |
|---|---|---|---|

### Hardest 15 strata

| stratum | difficulty | se | p_correct |
|---|---|---|---|
| Leptin|Leptin|Donor10 | 0.45 | 0.96 | 0.01 |
| IL-9|IL-9|Donor4 | 0.45 | 0.96 | 0.01 |
| GITRL|GITRL|Donor8 | 0.45 | 0.96 | 0.01 |
| GDNF|GDNF|Donor10 | 0.45 | 0.96 | 0.01 |
| PRL|PRL|Donor8 | 0.45 | 0.96 | 0.01 |
| ADSF|ADSF|Donor9 | 0.45 | 0.96 | 0.01 |
| TRAIL|TRAIL|Donor4 | 0.45 | 0.96 | 0.01 |
| IL-17A|IL-17A|Donor8 | 0.45 | 0.96 | 0.01 |
| TSLP|TSLP|Donor10 | 0.45 | 0.96 | 0.01 |
| IL-26|IL-26|Donor4 | 0.45 | 0.96 | 0.01 |
| IL-12|IL-12|Donor10 | 0.45 | 0.96 | 0.01 |
| IL-11|IL-11|Donor11 | 0.45 | 0.96 | 0.01 |
| TNF-alpha|TNF-alpha|Donor11 | 0.45 | 0.96 | 0.01 |
| TPO|TPO|Donor4 | 0.45 | 0.96 | 0.01 |
| Noggin|Noggin|Donor10 | 0.45 | 0.96 | 0.01 |

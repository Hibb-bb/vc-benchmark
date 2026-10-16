# Component B summary: pert_pool_v0


## AdamsonWeissman2016_GSM2406681_10X010.perturbation

- items: 87; informative (non-degenerate): 81; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.11, -1.23, 0.37, 1.38, 2.58]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 5, -2: 18, -1: 10, +0: 22, +1: 14, +2: 11, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | 1.54 | 0.28 | 0.667 | 0.88 |
| knn_k20 | 0.92 | 0.27 | 0.575 | 1.24 |
| gp_d50_ls0.5 | 0.77 | 0.27 | 0.552 | 0.62 |
| knn_k20_tf0.3 | 0.26 | 0.27 | 0.471 | 2.40 |
| ridge_d10_lam100 | 0.12 | 0.27 | 0.448 | 0.52 |
| ridge_d50_lam100 | -0.03 | 0.27 | 0.425 | 0.35 |
| ridge_d50_lam100_tf0.3 | -0.33 | 0.27 | 0.379 | 0.91 |
| knn_k5 | -0.56 | 0.28 | 0.345 | 0.86 |
| pcareg_k2 | -0.63 | 0.28 | 0.333 | 1.14 |
| pcareg_k10 | -0.79 | 0.28 | 0.310 | 0.36 |
| pcareg_k5 | -0.87 | 0.28 | 0.299 | 0.58 |
| knn_k20_tf0.1 | -1.12 | 0.29 | 0.264 | 1.48 |
| pcareg_k20 | -1.12 | 0.29 | 0.264 | 0.35 |
| pcareg_k50 | -1.48 | 0.31 | 0.218 | 0.34 |
| pcareg_k100 | -1.67 | 0.31 | 0.195 | 0.31 |
| pcareg_k200 | -1.67 | 0.31 | 0.195 | 0.31 |
| ridge_d50_lam100_tf0.1 | -1.67 | 0.31 | 0.195 | 1.25 |
| target_kd | -1.67 | 0.31 | 0.195 | 2.94 |
| knn_k1 | -1.77 | 0.32 | 0.184 | 0.63 |
| ridge_d10_lam1 | -1.87 | 0.33 | 0.172 | 0.59 |
| random_shift_s1 | -2.09 | 0.34 | 0.149 | 0.88 |
| random_shift_s0 | -2.34 | 0.36 | 0.126 | 3.45 |
| ridge_d50_lam1 | -2.62 | 0.39 | 0.103 | 0.67 |
| control_mean | -3.34 | 0.48 | 0.057 | 0.25 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.201 | 7.3e-02 | 81 |
| log_n_cells | -0.038 | 7.4e-01 | 81 |

## FrangiehIzar2021_RNA.context

- items: 669; informative (non-degenerate): 466; nobody passes: 200; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-4.89, -2.4, -0.21, 0.43, 1.14]; median SE 0.63
- histogram (bin lower edge: count): -6: 13, -5: 32, -4: 25, -3: 65, -2: 34, -1: 109, +0: 67, +1: 114, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r5 | -0.74 | 0.12 | 0.351 | 1.50 |
| lowrank_r10 | -0.91 | 0.12 | 0.333 | 2.12 |
| gp_d50_ls0.5 | -1.15 | 0.12 | 0.308 | 0.49 |
| lowrank_r2 | -1.40 | 0.13 | 0.284 | 2.09 |
| pcareg_k2 | -1.51 | 0.13 | 0.274 | 0.95 |
| pcareg_k5 | -1.51 | 0.13 | 0.274 | 0.61 |
| ridge_d10_lam100 | -1.52 | 0.13 | 0.272 | 0.41 |
| gp_d50_ls2 | -1.57 | 0.13 | 0.268 | 0.35 |
| pcareg_k10 | -1.64 | 0.13 | 0.262 | 0.28 |
| ridge_d10_lam1 | -1.69 | 0.13 | 0.257 | 0.28 |
| ridge_d50_lam100 | -1.89 | 0.13 | 0.239 | 0.23 |
| pcareg_k20 | -2.13 | 0.14 | 0.220 | 0.25 |
| pcareg_k50 | -2.34 | 0.14 | 0.203 | 0.19 |
| ridge_d50_lam1 | -2.44 | 0.14 | 0.196 | 0.19 |
| pcareg_k100 | -2.46 | 0.14 | 0.194 | 0.20 |
| pcareg_k200 | -2.65 | 0.15 | 0.181 | 0.20 |
| scgen | -2.94 | 0.15 | 0.161 | 0.69 |
| knn_k20 | -3.15 | 0.16 | 0.148 | 0.55 |
| knn_k5 | -3.22 | 0.16 | 0.143 | 0.41 |
| ridge_d50_lam100_tf0.3 | -3.22 | 0.16 | 0.143 | 0.48 |
| knn_k1 | -3.27 | 0.16 | 0.141 | 0.68 |
| knn_k20_tf0.3 | -3.84 | 0.17 | 0.109 | 0.56 |
| ridge_d50_lam100_tf0.1 | -4.22 | 0.18 | 0.091 | 0.29 |
| target_kd | -4.39 | 0.19 | 0.084 | 7.40 |
| knn_k20_tf0.1 | -4.42 | 0.19 | 0.082 | 0.76 |
| control_mean | -4.64 | 0.20 | 0.073 | 0.61 |
| random_shift_s0 | -4.89 | 0.20 | 0.064 | 0.32 |
| random_shift_s1 | -4.97 | 0.21 | 0.061 | 0.70 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.215 | 2.8e-06 | 466 |
| log_n_cells | 0.120 | 9.8e-03 | 466 |

## FrangiehIzar2021_RNA.perturbation

- items: 669; informative (non-degenerate): 457; nobody passes: 212; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.1, -1.6, -0.36, -0.36, 0.89]; median SE 0.66
- histogram (bin lower edge: count): -6: 3, -5: 23, -4: 26, -3: 52, -2: 58, -1: 214, +0: 81, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r10 | -0.64 | 0.10 | 0.378 | 2.57 |
| lowrank_r5 | -0.64 | 0.10 | 0.378 | 2.57 |
| lowrank_r2 | -0.64 | 0.10 | 0.378 | 2.57 |
| pcareg_k2 | -1.76 | 0.12 | 0.238 | 1.02 |
| ridge_d10_lam100 | -2.13 | 0.12 | 0.199 | 0.50 |
| pcareg_k5 | -2.20 | 0.13 | 0.193 | 0.49 |
| gp_d50_ls2 | -2.38 | 0.13 | 0.176 | 0.57 |
| pcareg_k10 | -2.39 | 0.13 | 0.175 | 0.38 |
| ridge_d10_lam1 | -2.48 | 0.13 | 0.167 | 0.39 |
| gp_d50_ls0.5 | -2.51 | 0.13 | 0.164 | 0.95 |
| ridge_d50_lam100 | -2.73 | 0.14 | 0.146 | 0.24 |
| pcareg_k20 | -2.73 | 0.14 | 0.146 | 0.25 |
| pcareg_k50 | -2.95 | 0.14 | 0.130 | 0.21 |
| ridge_d50_lam1 | -3.11 | 0.15 | 0.120 | 0.21 |
| pcareg_k100 | -3.20 | 0.15 | 0.114 | 0.18 |
| ridge_d50_lam100_tf0.3 | -3.31 | 0.16 | 0.106 | 0.51 |
| pcareg_k200 | -3.36 | 0.16 | 0.103 | 0.18 |
| knn_k20 | -3.46 | 0.16 | 0.097 | 0.39 |
| knn_k20_tf0.3 | -3.65 | 0.17 | 0.087 | 0.40 |
| target_kd | -3.71 | 0.17 | 0.084 | 4.04 |
| knn_k20_tf0.1 | -3.71 | 0.17 | 0.084 | 0.58 |
| ridge_d50_lam100_tf0.1 | -3.74 | 0.17 | 0.082 | 0.46 |
| knn_k5 | -3.83 | 0.17 | 0.078 | 0.58 |
| control_mean | -3.99 | 0.18 | 0.070 | 0.52 |
| knn_k1 | -4.05 | 0.18 | 0.067 | 0.31 |
| random_shift_s1 | -4.05 | 0.18 | 0.067 | 0.39 |
| random_shift_s0 | -4.12 | 0.19 | 0.064 | 0.71 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.156 | 7.9e-04 | 457 |
| log_n_cells | 0.156 | 8.3e-04 | 457 |

## McFarlandTsherniak2020.context

- items: 866; informative (non-degenerate): 815; nobody passes: 51; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-5.72, -2.32, -0.29, 1.6, 4.54]; median SE 0.83
- histogram (bin lower edge: count): -6: 50, -5: 29, -4: 51, -3: 88, -2: 96, -1: 173, +0: 105, +1: 53, +2: 72, +3: 52, +4: 46, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 4.73 | 0.16 | 0.900 | 0.21 |
| pcareg_k100 | 3.38 | 0.13 | 0.823 | 0.22 |
| scgen | 3.15 | 0.13 | 0.808 | 1.94 |
| pcareg_k50 | 2.65 | 0.12 | 0.773 | 0.19 |
| pcareg_k20 | 2.07 | 0.12 | 0.727 | 0.21 |
| pcareg_k10 | 1.43 | 0.11 | 0.672 | 0.27 |
| pcareg_k5 | 0.62 | 0.10 | 0.592 | 0.44 |
| pcareg_k2 | 0.01 | 0.10 | 0.524 | 0.71 |
| lowrank_r10 | -0.86 | 0.10 | 0.421 | 1.11 |
| lowrank_r5 | -1.19 | 0.10 | 0.381 | 1.24 |
| lowrank_r2 | -1.28 | 0.10 | 0.371 | 2.31 |
| random_shift_s0 | -3.13 | 0.12 | 0.178 | 4.40 |
| random_shift_s1 | -3.15 | 0.12 | 0.177 | 2.61 |
| control_mean | -4.31 | 0.15 | 0.100 | 1.79 |
| target_kd | -9.81 | 0.92 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.166 | 1.9e-06 | 815 |
| log_n_cells | -0.124 | 3.9e-04 | 815 |
| dose | -0.078 | 2.8e-02 | 794 |

## McFarlandTsherniak2020.perturbation

- items: 866; informative (non-degenerate): 385; nobody passes: 481; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.37, -3.24, -1.71, -1.17, -0.36]; median SE 0.69
- histogram (bin lower edge: count): -6: 0, -5: 26, -4: 85, -3: 79, -2: 130, -1: 65, +0: 0, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | -1.55 | 0.11 | 0.285 | 0.43 |
| pcareg_k100 | -2.16 | 0.11 | 0.226 | 0.33 |
| pcareg_k50 | -2.53 | 0.11 | 0.193 | 0.26 |
| pcareg_k2 | -2.70 | 0.12 | 0.178 | 0.39 |
| pcareg_k10 | -2.83 | 0.12 | 0.167 | 0.24 |
| pcareg_k20 | -2.97 | 0.12 | 0.156 | 0.23 |
| pcareg_k5 | -2.98 | 0.12 | 0.155 | 0.27 |
| random_shift_s0 | -3.17 | 0.12 | 0.140 | 0.83 |
| random_shift_s1 | -3.31 | 0.13 | 0.129 | 0.82 |
| control_mean | -3.68 | 0.13 | 0.104 | 0.64 |
| lowrank_r2 | -4.28 | 0.15 | 0.069 | 0.56 |
| lowrank_r5 | -4.28 | 0.15 | 0.069 | 0.56 |
| lowrank_r10 | -4.28 | 0.15 | 0.069 | 0.56 |
| target_kd | -8.80 | 0.96 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.299 | 2.2e-09 | 385 |
| log_n_cells | -0.035 | 5.0e-01 | 385 |
| dose | 0.039 | 4.5e-01 | 382 |

## NadigOConner2024_hepg2.perturbation

- items: 1061; informative (non-degenerate): 954; nobody passes: 104; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.09, -1.88, -0.43, 1.29, 2.4]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 24, -4: 40, -3: 132, -2: 229, -1: 113, +0: 160, +1: 156, +2: 100, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | 0.21 | 0.08 | 0.532 | 0.58 |
| pcareg_k2 | 0.17 | 0.08 | 0.527 | 1.33 |
| pcareg_k5 | -0.01 | 0.08 | 0.502 | 0.60 |
| ridge_d10_lam100 | -0.06 | 0.08 | 0.497 | 0.43 |
| gp_d50_ls0.5 | -0.08 | 0.08 | 0.493 | 0.78 |
| pcareg_k10 | -0.18 | 0.08 | 0.481 | 0.38 |
| ridge_d10_lam1 | -0.20 | 0.08 | 0.478 | 0.38 |
| ridge_d50_lam100 | -0.25 | 0.08 | 0.470 | 0.32 |
| pcareg_k20 | -0.30 | 0.08 | 0.464 | 0.36 |
| pcareg_k50 | -0.48 | 0.08 | 0.440 | 0.30 |
| ridge_d50_lam1 | -0.49 | 0.08 | 0.438 | 0.31 |
| knn_k20 | -0.54 | 0.08 | 0.432 | 1.35 |
| pcareg_k100 | -0.55 | 0.08 | 0.430 | 0.29 |
| pcareg_k200 | -0.64 | 0.08 | 0.418 | 0.31 |
| knn_k20_tf0.3 | -0.76 | 0.08 | 0.402 | 1.33 |
| ridge_d50_lam100_tf0.3 | -0.89 | 0.08 | 0.385 | 1.13 |
| knn_k20_tf0.1 | -1.04 | 0.08 | 0.365 | 1.82 |
| knn_k5 | -1.31 | 0.08 | 0.329 | 1.38 |
| ridge_d50_lam100_tf0.1 | -1.50 | 0.09 | 0.304 | 1.57 |
| knn_k1 | -1.85 | 0.09 | 0.260 | 1.52 |
| random_shift_s0 | -2.37 | 0.09 | 0.201 | 2.38 |
| random_shift_s1 | -2.39 | 0.09 | 0.199 | 2.33 |
| control_mean | -2.67 | 0.10 | 0.170 | 1.35 |
| target_kd | -3.10 | 0.11 | 0.131 | 8.63 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.084 | 9.9e-03 | 954 |
| log_n_cells | 0.016 | 6.3e-01 | 954 |

## NadigOConner2024_jurkat.perturbation

- items: 1815; informative (non-degenerate): 1585; nobody passes: 228; everybody passes: 2
- difficulty percentiles 5/25/50/75/95: [-3.75, -1.99, -1.05, 1.05, 2.52]; median SE 0.53
- histogram (bin lower edge: count): -6: 0, -5: 52, -4: 85, -3: 181, -2: 477, -1: 150, +0: 188, +1: 291, +2: 161, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 0.52 | 0.07 | 0.577 | 1.35 |
| gp_d50_ls2 | 0.19 | 0.07 | 0.538 | 0.40 |
| ridge_d10_lam100 | 0.14 | 0.07 | 0.532 | 0.45 |
| pcareg_k10 | 0.12 | 0.07 | 0.529 | 0.44 |
| ridge_d10_lam1 | 0.11 | 0.07 | 0.528 | 0.44 |
| pcareg_k5 | 0.06 | 0.07 | 0.522 | 0.80 |
| pcareg_k20 | 0.01 | 0.07 | 0.516 | 0.39 |
| ridge_d50_lam100 | -0.02 | 0.07 | 0.512 | 0.30 |
| gp_d50_ls0.5 | -0.05 | 0.07 | 0.509 | 0.85 |
| ridge_d50_lam1 | -0.10 | 0.07 | 0.502 | 0.30 |
| pcareg_k50 | -0.10 | 0.07 | 0.502 | 0.30 |
| pcareg_k100 | -0.21 | 0.07 | 0.489 | 0.31 |
| pcareg_k200 | -0.32 | 0.07 | 0.475 | 0.32 |
| ridge_d50_lam100_tf0.3 | -1.03 | 0.07 | 0.384 | 1.08 |
| knn_k20 | -1.07 | 0.07 | 0.378 | 1.27 |
| knn_k20_tf0.3 | -1.25 | 0.07 | 0.355 | 1.31 |
| knn_k20_tf0.1 | -1.49 | 0.07 | 0.325 | 2.04 |
| ridge_d50_lam100_tf0.1 | -1.68 | 0.07 | 0.300 | 1.62 |
| knn_k5 | -1.78 | 0.07 | 0.288 | 1.39 |
| knn_k1 | -2.42 | 0.07 | 0.213 | 1.86 |
| random_shift_s1 | -2.61 | 0.07 | 0.192 | 2.48 |
| random_shift_s0 | -2.65 | 0.07 | 0.188 | 2.75 |
| control_mean | -3.10 | 0.08 | 0.145 | 1.79 |
| target_kd | -3.21 | 0.08 | 0.136 | 9.82 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.175 | 2.4e-12 | 1585 |
| log_n_cells | -0.033 | 1.9e-01 | 1585 |

## NormanWeissman2019_filtered.perturbation

- items: 236; informative (non-degenerate): 225; nobody passes: 9; everybody passes: 2
- difficulty percentiles 5/25/50/75/95: [-2.33, -1.29, -0.88, 0.81, 3.52]; median SE 0.62
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 9, -3: 23, -2: 59, -1: 62, +0: 17, +1: 15, +2: 22, +3: 12, +4: 6, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls0.5 | 2.71 | 0.24 | 0.835 | 0.42 |
| gp_d50_ls2 | 2.37 | 0.23 | 0.809 | 0.41 |
| knn_k5 | 1.80 | 0.22 | 0.763 | 0.70 |
| ridge_d50_lam100 | 1.80 | 0.22 | 0.763 | 0.30 |
| knn_k20 | 1.75 | 0.22 | 0.758 | 0.93 |
| ridge_d50_lam1 | 1.52 | 0.21 | 0.737 | 0.28 |
| ridge_d10_lam100 | 1.48 | 0.21 | 0.733 | 0.34 |
| pcareg_k20 | 1.48 | 0.21 | 0.733 | 0.20 |
| pcareg_k50 | 1.43 | 0.21 | 0.729 | 0.21 |
| pcareg_k200 | 1.39 | 0.21 | 0.725 | 0.21 |
| pcareg_k10 | 1.39 | 0.21 | 0.725 | 0.22 |
| pcareg_k100 | 1.34 | 0.21 | 0.720 | 0.21 |
| ridge_d10_lam1 | 1.34 | 0.21 | 0.720 | 0.27 |
| ridge_d50_lam100_tf0.3 | 1.10 | 0.20 | 0.695 | 1.02 |
| pcareg_k5 | 1.10 | 0.20 | 0.695 | 0.30 |
| pcareg_k2 | 0.79 | 0.19 | 0.661 | 0.72 |
| knn_k1 | 0.75 | 0.19 | 0.657 | 1.20 |
| knn_k20_tf0.3 | 0.06 | 0.17 | 0.568 | 1.97 |
| ridge_d50_lam100_tf0.1 | -0.24 | 0.17 | 0.525 | 2.42 |
| knn_k20_tf0.1 | -1.05 | 0.16 | 0.398 | 5.60 |
| target_kd | -1.45 | 0.16 | 0.335 | 4.13 |
| random_shift_s0 | -2.65 | 0.20 | 0.169 | 4.14 |
| random_shift_s1 | -2.77 | 0.20 | 0.157 | 2.61 |
| control_mean | -4.17 | 0.31 | 0.055 | 1.05 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.177 | 7.9e-03 | 225 |
| log_n_cells | -0.006 | 9.3e-01 | 225 |

## ReplogleWeissman2022_K562_essential.perturbation

- items: 1832; informative (non-degenerate): 1653; nobody passes: 176; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.19, -1.84, -0.86, 1.58, 2.69]; median SE 0.55
- histogram (bin lower edge: count): -6: 0, -5: 36, -4: 82, -3: 267, -2: 421, -1: 203, +0: 166, +1: 155, +2: 323, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| ridge_d10_lam100 | 0.39 | 0.07 | 0.563 | 0.36 |
| pcareg_k5 | 0.38 | 0.07 | 0.563 | 0.55 |
| gp_d50_ls2 | 0.36 | 0.07 | 0.561 | 0.35 |
| ridge_d10_lam1 | 0.36 | 0.07 | 0.560 | 0.34 |
| pcareg_k10 | 0.35 | 0.07 | 0.559 | 0.34 |
| pcareg_k2 | 0.32 | 0.07 | 0.555 | 1.95 |
| pcareg_k20 | 0.23 | 0.07 | 0.545 | 0.31 |
| ridge_d50_lam100 | 0.19 | 0.07 | 0.540 | 0.30 |
| pcareg_k50 | 0.13 | 0.07 | 0.533 | 0.27 |
| ridge_d50_lam1 | 0.11 | 0.07 | 0.531 | 0.28 |
| pcareg_k100 | 0.02 | 0.07 | 0.519 | 0.29 |
| pcareg_k200 | -0.05 | 0.07 | 0.511 | 0.30 |
| gp_d50_ls0.5 | -0.13 | 0.07 | 0.501 | 0.83 |
| ridge_d50_lam100_tf0.3 | -0.50 | 0.07 | 0.455 | 1.04 |
| knn_k20 | -0.95 | 0.06 | 0.396 | 1.27 |
| knn_k20_tf0.3 | -1.05 | 0.06 | 0.383 | 1.46 |
| knn_k20_tf0.1 | -1.19 | 0.06 | 0.365 | 1.90 |
| ridge_d50_lam100_tf0.1 | -1.20 | 0.06 | 0.364 | 1.37 |
| knn_k5 | -1.74 | 0.07 | 0.293 | 1.54 |
| knn_k1 | -2.23 | 0.07 | 0.234 | 1.91 |
| random_shift_s1 | -2.76 | 0.07 | 0.175 | 3.48 |
| random_shift_s0 | -2.80 | 0.07 | 0.171 | 4.00 |
| target_kd | -2.96 | 0.08 | 0.155 | 9.87 |
| control_mean | -3.41 | 0.08 | 0.116 | 1.96 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.052 | 3.4e-02 | 1653 |
| log_n_cells | -0.062 | 1.1e-02 | 1653 |

## ReplogleWeissman2022_K562_gwps.perturbation

- items: 9326; informative (non-degenerate): 8273; nobody passes: 1011; everybody passes: 42
- difficulty percentiles 5/25/50/75/95: [-3.85, -1.81, -0.59, 1.13, 2.56]; median SE 0.51
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1049, -3: 780, -2: 1204, -1: 2102, +0: 1039, +1: 1260, +2: 839, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k5 | 0.04 | 0.03 | 0.517 | 0.69 |
| ridge_d10_lam100 | 0.04 | 0.03 | 0.516 | 0.45 |
| pcareg_k10 | 0.03 | 0.03 | 0.515 | 0.44 |
| ridge_d10_lam1 | 0.03 | 0.03 | 0.514 | 0.44 |
| ridge_d50_lam100 | 0.00 | 0.03 | 0.512 | 0.38 |
| pcareg_k20 | 0.00 | 0.03 | 0.511 | 0.43 |
| pcareg_k50 | -0.02 | 0.03 | 0.509 | 0.37 |
| ridge_d50_lam1 | -0.02 | 0.03 | 0.509 | 0.37 |
| pcareg_k100 | -0.02 | 0.03 | 0.508 | 0.38 |
| pcareg_k2 | -0.02 | 0.03 | 0.508 | 1.74 |
| pcareg_k200 | -0.04 | 0.03 | 0.505 | 0.38 |
| gp_d50_ls2 | -0.17 | 0.03 | 0.488 | 0.95 |
| ridge_d50_lam100_tf0.3 | -0.31 | 0.03 | 0.469 | 1.01 |
| gp_d50_ls0.5 | -0.44 | 0.03 | 0.452 | 1.10 |
| ridge_d50_lam100_tf0.1 | -0.71 | 0.03 | 0.415 | 1.20 |
| knn_k20 | -1.13 | 0.03 | 0.360 | 0.96 |
| knn_k20_tf0.3 | -1.13 | 0.03 | 0.359 | 0.98 |
| knn_k20_tf0.1 | -1.23 | 0.03 | 0.346 | 1.19 |
| knn_k5 | -1.24 | 0.03 | 0.345 | 0.96 |
| knn_k1 | -1.35 | 0.03 | 0.331 | 0.93 |
| random_shift_s0 | -1.44 | 0.03 | 0.320 | 1.11 |
| random_shift_s1 | -1.44 | 0.03 | 0.320 | 1.13 |
| control_mean | -1.55 | 0.03 | 0.305 | 0.77 |
| target_kd | -2.95 | 0.04 | 0.157 | 7.83 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.164 | 7.7e-51 | 8273 |
| log_n_cells | -0.058 | 1.6e-07 | 8273 |

## ReplogleWeissman2022_rpe1.perturbation

- items: 1611; informative (non-degenerate): 1375; nobody passes: 232; everybody passes: 4
- difficulty percentiles 5/25/50/75/95: [-3.53, -1.95, -0.9, 1.07, 2.19]; median SE 0.51
- histogram (bin lower edge: count): -6: 0, -5: 38, -4: 88, -3: 167, -2: 357, -1: 212, +0: 150, +1: 177, +2: 186, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 0.06 | 0.07 | 0.518 | 1.36 |
| pcareg_k5 | -0.18 | 0.07 | 0.487 | 0.72 |
| gp_d50_ls2 | -0.21 | 0.07 | 0.484 | 0.53 |
| ridge_d10_lam100 | -0.24 | 0.07 | 0.480 | 0.47 |
| pcareg_k10 | -0.28 | 0.07 | 0.475 | 0.44 |
| ridge_d10_lam1 | -0.29 | 0.07 | 0.472 | 0.44 |
| pcareg_k20 | -0.34 | 0.07 | 0.467 | 0.44 |
| ridge_d50_lam100 | -0.42 | 0.07 | 0.456 | 0.36 |
| pcareg_k50 | -0.50 | 0.07 | 0.446 | 0.36 |
| ridge_d50_lam1 | -0.51 | 0.07 | 0.444 | 0.36 |
| gp_d50_ls0.5 | -0.52 | 0.07 | 0.443 | 0.81 |
| pcareg_k100 | -0.59 | 0.07 | 0.434 | 0.37 |
| pcareg_k200 | -0.61 | 0.07 | 0.431 | 0.36 |
| knn_k20 | -1.27 | 0.07 | 0.345 | 1.30 |
| ridge_d50_lam100_tf0.3 | -1.31 | 0.07 | 0.340 | 1.12 |
| knn_k20_tf0.3 | -1.38 | 0.07 | 0.330 | 1.48 |
| knn_k20_tf0.1 | -1.69 | 0.07 | 0.291 | 1.95 |
| ridge_d50_lam100_tf0.1 | -1.89 | 0.07 | 0.266 | 1.40 |
| knn_k5 | -1.98 | 0.07 | 0.256 | 1.14 |
| knn_k1 | -2.40 | 0.08 | 0.207 | 1.17 |
| random_shift_s1 | -2.67 | 0.08 | 0.179 | 1.63 |
| random_shift_s0 | -2.69 | 0.08 | 0.178 | 1.31 |
| control_mean | -2.79 | 0.08 | 0.168 | 1.04 |
| target_kd | -3.27 | 0.09 | 0.126 | 9.24 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.196 | 2.1e-13 | 1375 |
| log_n_cells | -0.065 | 1.6e-02 | 1375 |

## SrivatsanTrapnell2020_sciplex3.context

- items: 2423; informative (non-degenerate): 1929; nobody passes: 494; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.83, -2.31, -1.08, 0.45, 1.7]; median SE 0.68
- histogram (bin lower edge: count): -6: 24, -5: 37, -4: 31, -3: 434, -2: 446, -1: 263, +0: 446, +1: 248, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k50 | 0.07 | 0.06 | 0.524 | 0.36 |
| pcareg_k100 | -0.04 | 0.06 | 0.509 | 0.37 |
| pcareg_k20 | -0.05 | 0.06 | 0.508 | 0.36 |
| pcareg_k200 | -0.18 | 0.06 | 0.492 | 0.39 |
| pcareg_k10 | -0.49 | 0.06 | 0.451 | 0.39 |
| lowrank_r10 | -0.72 | 0.06 | 0.420 | 1.16 |
| pcareg_k5 | -0.79 | 0.06 | 0.411 | 0.45 |
| lowrank_r5 | -0.88 | 0.06 | 0.399 | 1.00 |
| lowrank_r2 | -0.88 | 0.06 | 0.399 | 1.40 |
| pcareg_k2 | -0.89 | 0.06 | 0.397 | 0.63 |
| scgen | -2.04 | 0.06 | 0.248 | 1.50 |
| random_shift_s0 | -3.30 | 0.07 | 0.119 | 1.90 |
| random_shift_s1 | -3.36 | 0.07 | 0.114 | 2.28 |
| control_mean | -3.70 | 0.08 | 0.091 | 2.03 |
| target_kd | -9.75 | 0.92 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.105 | 4.0e-06 | 1929 |
| log_n_cells | 0.111 | 1.0e-06 | 1929 |
| dose | 0.002 | 9.4e-01 | 1929 |

## SrivatsanTrapnell2020_sciplex3.perturbation

- items: 2423; informative (non-degenerate): 2006; nobody passes: 417; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.7, -1.43, -0.3, 0.13, 1.4]; median SE 0.66
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 26, -3: 191, -2: 630, -1: 368, +0: 652, +1: 139, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k50 | -0.38 | 0.05 | 0.459 | 0.51 |
| pcareg_k100 | -0.38 | 0.05 | 0.459 | 0.52 |
| pcareg_k200 | -0.39 | 0.05 | 0.457 | 0.52 |
| lowrank_r2 | -0.54 | 0.05 | 0.431 | 0.97 |
| lowrank_r5 | -0.54 | 0.05 | 0.431 | 0.97 |
| lowrank_r10 | -0.54 | 0.05 | 0.431 | 0.97 |
| pcareg_k20 | -0.85 | 0.05 | 0.379 | 0.59 |
| pcareg_k10 | -1.40 | 0.05 | 0.291 | 0.56 |
| pcareg_k5 | -1.63 | 0.05 | 0.256 | 0.64 |
| pcareg_k2 | -1.73 | 0.05 | 0.242 | 1.30 |
| random_shift_s1 | -2.85 | 0.07 | 0.116 | 1.81 |
| random_shift_s0 | -2.90 | 0.07 | 0.112 | 2.05 |
| control_mean | -3.19 | 0.08 | 0.090 | 1.61 |
| target_kd | -8.89 | 0.95 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.230 | 1.5e-25 | 2006 |
| log_n_cells | 0.139 | 3.9e-10 | 2006 |
| dose | 0.153 | 5.2e-12 | 2006 |

## TianKampmann2019_day7neuron.perturbation

- items: 35; informative (non-degenerate): 28; nobody passes: 7; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.3, -0.16, 0.56, 2.2, 2.93]; median SE 0.56
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 3, -2: 3, -1: 3, +0: 9, +1: 2, +2: 8, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | 1.88 | 0.46 | 0.571 | 1.08 |
| pcareg_k2 | 1.66 | 0.46 | 0.543 | 0.48 |
| gp_d50_ls2 | 1.25 | 0.45 | 0.486 | 0.57 |
| ridge_d10_lam100 | 1.04 | 0.45 | 0.457 | 0.31 |
| pcareg_k5 | 0.83 | 0.45 | 0.429 | 0.47 |
| pcareg_k10 | -0.01 | 0.47 | 0.314 | 0.41 |
| ridge_d50_lam100 | -0.24 | 0.48 | 0.286 | 0.38 |
| ridge_d50_lam100_tf0.3 | -0.48 | 0.49 | 0.257 | 1.18 |
| ridge_d10_lam1 | -0.48 | 0.49 | 0.257 | 0.33 |
| knn_k20_tf0.3 | -0.72 | 0.51 | 0.229 | 2.08 |
| pcareg_k20 | -0.72 | 0.51 | 0.229 | 0.31 |
| ridge_d50_lam100_tf0.1 | -1.27 | 0.54 | 0.171 | 1.31 |
| pcareg_k200 | -1.27 | 0.54 | 0.171 | 0.19 |
| pcareg_k50 | -1.27 | 0.54 | 0.171 | 0.19 |
| pcareg_k100 | -1.27 | 0.54 | 0.171 | 0.19 |
| gp_d50_ls0.5 | -1.58 | 0.57 | 0.143 | 0.30 |
| ridge_d50_lam1 | -1.58 | 0.57 | 0.143 | 0.19 |
| random_shift_s0 | -1.93 | 0.61 | 0.114 | 2.19 |
| knn_k5 | -1.93 | 0.61 | 0.114 | 0.45 |
| knn_k20_tf0.1 | -2.32 | 0.66 | 0.086 | 1.39 |
| random_shift_s1 | -3.45 | 0.89 | 0.029 | 0.12 |
| knn_k1 | -4.57 | 1.31 | 0.000 | 0.02 |
| control_mean | -4.57 | 1.31 | 0.000 | 0.02 |
| target_kd | -4.57 | 1.31 | 0.000 | 0.02 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.428 | 2.3e-02 | 28 |
| log_n_cells | 0.223 | 2.5e-01 | 28 |

## TianKampmann2019_iPSC.perturbation

- items: 81; informative (non-degenerate): 45; nobody passes: 36; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.9, -1.17, 0.85, 1.76, 1.76]; median SE 0.86
- histogram (bin lower edge: count): -6: 0, -5: 1, -4: 4, -3: 1, -2: 7, -1: 5, +0: 7, +1: 20, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 1.74 | 0.30 | 0.457 | 0.41 |
| ridge_d10_lam100 | 0.18 | 0.36 | 0.272 | 0.33 |
| gp_d50_ls2 | -0.09 | 0.37 | 0.247 | 0.51 |
| ridge_d10_lam1 | -0.85 | 0.41 | 0.185 | 0.17 |
| pcareg_k10 | -1.03 | 0.42 | 0.173 | 0.18 |
| pcareg_k5 | -1.03 | 0.42 | 0.173 | 0.20 |
| pcareg_k20 | -1.83 | 0.48 | 0.123 | 0.34 |
| knn_k20 | -2.07 | 0.49 | 0.111 | 0.16 |
| ridge_d50_lam100 | -2.07 | 0.49 | 0.111 | 0.19 |
| gp_d50_ls0.5 | -2.32 | 0.51 | 0.099 | 0.20 |
| pcareg_k50 | -2.90 | 0.56 | 0.074 | 0.07 |
| pcareg_k100 | -3.23 | 0.59 | 0.062 | 0.06 |
| ridge_d50_lam1 | -3.23 | 0.59 | 0.062 | 0.06 |
| pcareg_k200 | -3.23 | 0.59 | 0.062 | 0.06 |
| target_kd | -4.49 | 0.73 | 0.025 | 7.27 |
| knn_k20_tf0.1 | -5.11 | 0.85 | 0.012 | 4.80 |
| ridge_d50_lam100_tf0.1 | -5.11 | 0.85 | 0.012 | 4.80 |
| random_shift_s1 | -5.11 | 0.85 | 0.012 | 0.66 |
| ridge_d50_lam100_tf0.3 | -5.11 | 0.85 | 0.012 | 0.05 |
| knn_k1 | -6.09 | 1.17 | 0.000 | 0.01 |
| knn_k5 | -6.09 | 1.17 | 0.000 | 0.01 |
| knn_k20_tf0.3 | -6.09 | 1.17 | 0.000 | 0.01 |
| control_mean | -6.09 | 1.17 | 0.000 | 0.01 |
| random_shift_s0 | -6.09 | 1.17 | 0.000 | 0.01 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.422 | 3.9e-03 | 45 |
| log_n_cells | 0.259 | 8.5e-02 | 45 |

## TianKampmann2021_CRISPRi.perturbation

- items: 183; informative (non-degenerate): 72; nobody passes: 111; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.44, -1.31, -0.72, 0.13, 0.13]; median SE 0.83
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 6, -3: 7, -2: 11, -1: 15, +0: 33, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | -0.75 | 0.23 | 0.224 | 0.42 |
| ridge_d10_lam100 | -1.25 | 0.25 | 0.175 | 0.30 |
| pcareg_k2 | -1.50 | 0.26 | 0.153 | 0.56 |
| pcareg_k5 | -2.37 | 0.31 | 0.093 | 0.18 |
| target_kd | -2.67 | 0.33 | 0.077 | 0.98 |
| gp_d50_ls0.5 | -2.78 | 0.34 | 0.071 | 0.26 |
| pcareg_k10 | -3.03 | 0.36 | 0.060 | 0.11 |
| ridge_d50_lam100 | -3.31 | 0.39 | 0.049 | 0.09 |
| ridge_d10_lam1 | -3.46 | 0.40 | 0.044 | 0.10 |
| pcareg_k20 | -3.83 | 0.45 | 0.033 | 0.09 |
| knn_k20 | -4.04 | 0.48 | 0.027 | 0.50 |
| knn_k20_tf0.3 | -4.29 | 0.52 | 0.022 | 0.40 |
| pcareg_k50 | -5.46 | 0.79 | 0.005 | 0.04 |
| knn_k20_tf0.1 | -5.46 | 0.79 | 0.005 | 0.36 |
| control_mean | -6.34 | 1.13 | 0.000 | 0.00 |
| knn_k1 | -6.34 | 1.13 | 0.000 | 0.00 |
| knn_k5 | -6.34 | 1.13 | 0.000 | 0.00 |
| random_shift_s0 | -6.34 | 1.13 | 0.000 | 0.00 |
| pcareg_k100 | -6.34 | 1.13 | 0.000 | 0.00 |
| pcareg_k200 | -6.34 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam1 | -6.34 | 1.13 | 0.000 | 0.00 |
| random_shift_s1 | -6.34 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam100_tf0.1 | -6.34 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam100_tf0.3 | -6.34 | 1.13 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.313 | 7.4e-03 | 72 |
| log_n_cells | 0.243 | 3.9e-02 | 72 |

## parse_pbmc_cytokines.context

- items: 13967; informative (non-degenerate): 13248; nobody passes: 719; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.55, -2.06, -0.54, 2.06, 3.49]; median SE 0.58
- histogram (bin lower edge: count): -6: 100, -5: 457, -4: 937, -3: 2382, -2: 2241, -1: 1427, +0: 1266, +1: 885, +2: 2143, +3: 1352, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 3.74 | 0.03 | 0.871 | 0.60 |
| pcareg_k100 | 1.88 | 0.03 | 0.711 | 0.46 |
| lowrank_r10 | 0.67 | 0.03 | 0.588 | 0.88 |
| ridge_d50_lam100 | 0.63 | 0.03 | 0.585 | 0.26 |
| pcareg_k50 | 0.63 | 0.03 | 0.584 | 0.26 |
| ridge_d50_lam1 | 0.63 | 0.03 | 0.584 | 0.26 |
| ridge_d50_lam100_tf0.3 | 0.23 | 0.03 | 0.542 | 0.37 |
| gp_d50_ls2 | 0.18 | 0.03 | 0.537 | 0.41 |
| gp_d50_ls0.5 | 0.14 | 0.03 | 0.532 | 0.43 |
| knn_k20_tf0.1 | 0.11 | 0.03 | 0.529 | 1.28 |
| pcareg_k20 | -0.26 | 0.03 | 0.488 | 0.31 |
| ridge_d50_lam100_tf0.1 | -0.53 | 0.02 | 0.457 | 0.69 |
| ridge_d10_lam100 | -0.73 | 0.02 | 0.434 | 0.30 |
| pcareg_k10 | -0.73 | 0.02 | 0.434 | 0.30 |
| ridge_d10_lam1 | -0.73 | 0.02 | 0.434 | 0.30 |
| lowrank_r5 | -0.90 | 0.02 | 0.414 | 1.15 |
| knn_k20_tf0.3 | -1.20 | 0.02 | 0.378 | 3.92 |
| knn_k20 | -1.31 | 0.02 | 0.365 | 4.91 |
| pcareg_k5 | -1.64 | 0.02 | 0.326 | 0.40 |
| lowrank_r2 | -1.68 | 0.02 | 0.321 | 1.31 |
| pcareg_k2 | -2.59 | 0.03 | 0.217 | 0.50 |
| knn_k5 | -2.65 | 0.03 | 0.211 | 3.90 |
| knn_k1 | -3.52 | 0.03 | 0.130 | 2.43 |
| random_shift_s1 | -4.43 | 0.04 | 0.072 | 1.18 |
| random_shift_s0 | -4.46 | 0.04 | 0.070 | 1.38 |
| control_mean | -5.03 | 0.05 | 0.047 | 0.68 |
| target_kd | -11.80 | 0.84 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.007 | 4.0e-01 | 13248 |
| log_n_cells | -0.399 | 0.0e+00 | 13248 |

## parse_pbmc_cytokines.perturbation

- items: 13967; informative (non-degenerate): 10600; nobody passes: 3367; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.24, -1.55, -0.3, 0.49, 0.49]; median SE 0.79
- histogram (bin lower edge: count): -6: 9, -5: 110, -4: 717, -3: 1165, -2: 1741, -1: 3439, +0: 3419, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | -0.21 | 0.02 | 0.466 | 2.56 |
| knn_k20_tf0.3 | -1.55 | 0.02 | 0.267 | 1.14 |
| knn_k5 | -1.61 | 0.02 | 0.259 | 1.17 |
| pcareg_k200 | -2.44 | 0.03 | 0.165 | 1.20 |
| knn_k1 | -2.52 | 0.03 | 0.158 | 0.90 |
| gp_d50_ls0.5 | -2.89 | 0.03 | 0.126 | 0.49 |
| ridge_d50_lam100_tf0.1 | -2.95 | 0.03 | 0.121 | 0.62 |
| pcareg_k100 | -3.13 | 0.03 | 0.108 | 0.58 |
| gp_d50_ls2 | -3.13 | 0.03 | 0.107 | 0.43 |
| ridge_d50_lam100_tf0.3 | -3.15 | 0.03 | 0.106 | 0.40 |
| knn_k20_tf0.1 | -3.19 | 0.03 | 0.103 | 0.77 |
| pcareg_k50 | -3.47 | 0.03 | 0.085 | 0.20 |
| lowrank_r5 | -3.48 | 0.03 | 0.085 | 0.19 |
| lowrank_r10 | -3.48 | 0.03 | 0.085 | 0.19 |
| lowrank_r2 | -3.48 | 0.03 | 0.085 | 0.19 |
| ridge_d50_lam1 | -3.48 | 0.03 | 0.085 | 0.20 |
| ridge_d50_lam100 | -3.49 | 0.03 | 0.084 | 0.19 |
| random_shift_s1 | -3.75 | 0.04 | 0.070 | 0.74 |
| random_shift_s0 | -3.76 | 0.04 | 0.069 | 0.73 |
| pcareg_k20 | -3.76 | 0.04 | 0.069 | 0.29 |
| ridge_d10_lam1 | -4.01 | 0.04 | 0.057 | 0.24 |
| pcareg_k10 | -4.02 | 0.04 | 0.057 | 0.24 |
| ridge_d10_lam100 | -4.02 | 0.04 | 0.057 | 0.23 |
| pcareg_k5 | -4.12 | 0.04 | 0.053 | 0.41 |
| control_mean | -4.24 | 0.04 | 0.048 | 0.53 |
| pcareg_k2 | -4.26 | 0.04 | 0.047 | 0.49 |
| target_kd | -10.85 | 0.87 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.303 | 2.0e-224 | 10600 |
| log_n_cells | -0.209 | 7.0e-105 | 10600 |

## pooled

- items: 88164; informative (non-degenerate): 66431; nobody passes: 21677; everybody passes: 56
- difficulty percentiles 5/25/50/75/95: [-3.41, -2.1, -0.86, 0.28, 1.37]; median SE 0.56
- histogram (bin lower edge: count): -6: 859, -5: 1120, -4: 4255, -3: 11651, -2: 12680, -1: 16092, +0: 14737, +1: 5037, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | -1.10 | 0.01 | 0.351 | 1.16 |
| knn_k5 | -1.19 | 0.01 | 0.339 | 0.93 |
| pcareg_k200 | -1.34 | 0.02 | 0.339 | 0.65 |
| gp_d50_ls0.5 | -1.38 | 0.01 | 0.314 | 0.69 |
| gp_d50_ls2 | -1.42 | 0.01 | 0.309 | 0.63 |
| pcareg_k100 | -1.52 | 0.02 | 0.316 | 0.39 |
| knn_k1 | -1.54 | 0.01 | 0.295 | 0.90 |
| ridge_d50_lam100 | -1.58 | 0.01 | 0.290 | 0.35 |
| pcareg_k50 | -1.58 | 0.02 | 0.309 | 0.30 |
| knn_k20_tf0.3 | -1.62 | 0.01 | 0.284 | 0.88 |
| ridge_d50_lam100_tf0.3 | -1.63 | 0.01 | 0.284 | 0.53 |
| ridge_d50_lam1 | -1.65 | 0.01 | 0.281 | 0.36 |
| pcareg_k20 | -1.66 | 0.02 | 0.301 | 0.35 |
| ridge_d10_lam100 | -1.67 | 0.01 | 0.279 | 0.39 |
| ridge_d10_lam1 | -1.71 | 0.01 | 0.274 | 0.39 |
| pcareg_k10 | -1.71 | 0.02 | 0.294 | 0.36 |
| pcareg_k2 | -1.72 | 0.02 | 0.293 | 1.11 |
| pcareg_k5 | -1.73 | 0.02 | 0.292 | 0.52 |
| ridge_d50_lam100_tf0.1 | -1.76 | 0.01 | 0.268 | 0.63 |
| knn_k20_tf0.1 | -2.00 | 0.01 | 0.240 | 0.75 |
| random_shift_s0 | -2.93 | 0.01 | 0.149 | 1.53 |
| random_shift_s1 | -2.93 | 0.01 | 0.148 | 1.55 |
| lowrank_r2 | -2.97 | 0.01 | 0.116 | 1.11 |
| lowrank_r10 | -2.97 | 0.01 | 0.116 | 1.11 |
| lowrank_r5 | -2.97 | 0.01 | 0.116 | 1.11 |
| control_mean | -3.88 | 0.01 | 0.081 | 0.92 |
| target_kd | -5.27 | 0.02 | 0.028 | 4.60 |

### Mean difficulty by dataset (dataset factor check)

| dataset | n items | mean difficulty | sd |
|---|---|---|---|
| AdamsonWeissman2016_GSM2406681_10X010 | 81 | -0.78 | 1.38 |
| FrangiehIzar2021_RNA | 457 | -0.31 | 1.31 |
| McFarlandTsherniak2020 | 385 | -1.30 | 1.17 |
| NadigOConner2024_hepg2 | 954 | -1.40 | 1.76 |
| NadigOConner2024_jurkat | 1585 | -1.56 | 1.76 |
| NormanWeissman2019_filtered | 225 | -2.55 | 1.50 |
| ReplogleWeissman2022_K562_essential | 1653 | -1.58 | 1.78 |
| ReplogleWeissman2022_K562_gwps | 8273 | -1.75 | 1.92 |
| ReplogleWeissman2022_rpe1 | 1375 | -1.35 | 1.74 |
| SrivatsanTrapnell2020_sciplex3 | 2006 | -1.62 | 1.03 |
| TianKampmann2019_day7neuron | 28 | -0.54 | 1.31 |
| TianKampmann2019_iPSC | 45 | 0.25 | 1.24 |
| TianKampmann2021_CRISPRi | 72 | 0.61 | 0.84 |
| parse_pbmc_cytokines | 10600 | 0.27 | 1.09 |
| tahoe100m | 38692 | -0.98 | 1.30 |

## tahoe100m.context

- items: 53972; informative (non-degenerate): 53803; nobody passes: 169; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.24, -1.22, 0.07, 1.82, 4.38]; median SE 0.97
- histogram (bin lower edge: count): -6: 0, -5: 2404, -4: 0, -3: 6847, -2: 16324, -1: 0, +0: 10910, +1: 4542, +2: 4304, +3: 4482, +4: 1583, +5: 873

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r10 | 7.98 | 0.06 | 0.992 | 0.73 |
| lowrank_r5 | 6.24 | 0.03 | 0.972 | 1.34 |
| knn_k20 | 4.65 | 0.02 | 0.924 | 0.26 |
| ridge_d50_lam100 | 4.05 | 0.02 | 0.895 | 0.26 |
| ridge_d50_lam1 | 4.04 | 0.02 | 0.894 | 0.28 |
| lowrank_r2 | 3.82 | 0.02 | 0.881 | 2.68 |
| ridge_d50_lam100_tf0.3 | 3.79 | 0.02 | 0.880 | 0.92 |
| knn_k5 | 3.70 | 0.02 | 0.874 | 0.58 |
| knn_k20_tf0.3 | 3.24 | 0.02 | 0.844 | 0.31 |
| ridge_d50_lam100_tf0.1 | 3.20 | 0.02 | 0.842 | 0.92 |
| gp_d50_ls0.5 | 2.53 | 0.02 | 0.790 | 0.52 |
| ridge_d10_lam1 | 2.20 | 0.01 | 0.762 | 0.27 |
| ridge_d10_lam100 | 2.19 | 0.01 | 0.762 | 0.27 |
| gp_d50_ls2 | 1.77 | 0.01 | 0.723 | 0.54 |
| knn_k1 | 1.68 | 0.01 | 0.714 | 1.22 |
| knn_k20_tf0.1 | 1.13 | 0.01 | 0.657 | 0.78 |
| random_shift_s0 | -3.20 | 0.02 | 0.145 | 3.99 |
| random_shift_s1 | -3.26 | 0.02 | 0.141 | 3.81 |
| control_mean | -5.16 | 0.03 | 0.043 | 1.45 |
| target_kd | -13.18 | 0.80 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.000 | 9.4e-01 | 53803 |
| log_n_cells | -0.177 | 0.0e+00 | 53803 |
| dose | -0.184 | 0.0e+00 | 53803 |

## tahoe100m.perturbation

- items: 53972; informative (non-degenerate): 38692; nobody passes: 15280; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.33, -1.99, -0.95, -0.27, 0.92]; median SE 0.56
- histogram (bin lower edge: count): -6: 52, -5: 584, -4: 4337, -3: 4554, -2: 8867, -1: 11146, +0: 9127, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k5 | -1.04 | 0.01 | 0.368 | 0.73 |
| knn_k1 | -1.28 | 0.01 | 0.335 | 0.78 |
| gp_d50_ls0.5 | -1.40 | 0.01 | 0.320 | 0.68 |
| knn_k20 | -1.42 | 0.01 | 0.318 | 0.65 |
| gp_d50_ls2 | -1.52 | 0.01 | 0.304 | 0.66 |
| ridge_d50_lam100_tf0.3 | -1.66 | 0.01 | 0.287 | 0.43 |
| ridge_d50_lam100 | -1.71 | 0.01 | 0.281 | 0.39 |
| ridge_d50_lam100_tf0.1 | -1.72 | 0.01 | 0.279 | 0.46 |
| ridge_d50_lam1 | -1.78 | 0.01 | 0.271 | 0.41 |
| knn_k20_tf0.3 | -1.80 | 0.01 | 0.269 | 0.56 |
| ridge_d10_lam100 | -1.83 | 0.01 | 0.266 | 0.41 |
| ridge_d10_lam1 | -1.87 | 0.01 | 0.260 | 0.42 |
| knn_k20_tf0.1 | -1.97 | 0.01 | 0.248 | 0.60 |
| random_shift_s0 | -3.02 | 0.01 | 0.139 | 1.82 |
| random_shift_s1 | -3.02 | 0.01 | 0.139 | 1.87 |
| lowrank_r5 | -3.41 | 0.02 | 0.108 | 1.58 |
| lowrank_r10 | -3.41 | 0.02 | 0.108 | 1.58 |
| lowrank_r2 | -3.41 | 0.02 | 0.108 | 1.58 |
| control_mean | -4.60 | 0.02 | 0.043 | 1.16 |
| target_kd | -12.31 | 0.82 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.034 | 1.2e-11 | 38692 |
| log_n_cells | -0.094 | 1.8e-76 | 38692 |
| dose | -0.147 | 5.4e-185 | 38692 |

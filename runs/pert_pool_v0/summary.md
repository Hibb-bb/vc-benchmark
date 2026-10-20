# Component B summary: pert_pool_v0


## AdamsonWeissman2016_GSM2406681_10X010.perturbation

- items: 87; informative (non-degenerate): 81; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.04, -1.05, 0.48, 1.46, 2.66]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 1, -3: 4, -2: 18, -1: 11, +0: 16, +1: 21, +2: 10, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | 1.58 | 0.28 | 0.667 | 0.91 |
| knn_k20 | 0.97 | 0.27 | 0.575 | 1.23 |
| gp_d50_ls0.5 | 0.83 | 0.27 | 0.552 | 0.63 |
| knn_k20_tf0.3 | 0.32 | 0.27 | 0.471 | 2.49 |
| ridge_d10_lam100 | 0.17 | 0.27 | 0.448 | 0.51 |
| ridge_d50_lam100 | 0.03 | 0.27 | 0.425 | 0.36 |
| ridge_d50_lam100_tf0.3 | -0.27 | 0.27 | 0.379 | 0.90 |
| knn_k5 | -0.49 | 0.28 | 0.345 | 0.87 |
| pcareg_k2 | -0.57 | 0.28 | 0.333 | 1.17 |
| pcareg_k10 | -0.73 | 0.28 | 0.310 | 0.37 |
| pcareg_k5 | -0.81 | 0.28 | 0.299 | 0.59 |
| knn_k20_tf0.1 | -1.06 | 0.29 | 0.264 | 1.36 |
| pcareg_k20 | -1.06 | 0.29 | 0.264 | 0.36 |
| pcareg_k50 | -1.41 | 0.31 | 0.218 | 0.36 |
| target_kd | -1.60 | 0.31 | 0.195 | 2.96 |
| ridge_d50_lam100_tf0.1 | -1.60 | 0.31 | 0.195 | 1.19 |
| pcareg_k100 | -1.60 | 0.31 | 0.195 | 0.33 |
| mlp_h1024_d50 | -1.60 | 0.31 | 0.195 | 1.04 |
| pcareg_k200 | -1.60 | 0.31 | 0.195 | 0.33 |
| knn_k1 | -1.70 | 0.32 | 0.184 | 0.62 |
| ridge_d10_lam1 | -1.81 | 0.33 | 0.172 | 0.59 |
| random_shift_s1 | -2.03 | 0.34 | 0.149 | 0.86 |
| random_shift_s0 | -2.28 | 0.36 | 0.126 | 2.70 |
| mlp_h256_d50 | -2.41 | 0.37 | 0.115 | 1.01 |
| ridge_d50_lam1 | -2.56 | 0.39 | 0.103 | 0.69 |
| control_mean | -3.29 | 0.48 | 0.057 | 0.22 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.232 | 3.7e-02 | 81 |
| log_n_cells | -0.058 | 6.1e-01 | 81 |

## FrangiehIzar2021_RNA.context

- items: 669; informative (non-degenerate): 470; nobody passes: 196; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-4.72, -2.34, -0.28, 0.52, 1.22]; median SE 0.62
- histogram (bin lower edge: count): -6: 16, -5: 27, -4: 33, -3: 45, -2: 54, -1: 58, +0: 117, +1: 113, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r5 | -0.72 | 0.12 | 0.351 | 1.54 |
| lowrank_r10 | -0.88 | 0.12 | 0.333 | 2.23 |
| gp_d50_ls0.5 | -1.13 | 0.12 | 0.308 | 0.44 |
| lowrank_r2 | -1.37 | 0.13 | 0.284 | 2.21 |
| pcareg_k2 | -1.49 | 0.13 | 0.274 | 1.02 |
| pcareg_k5 | -1.49 | 0.13 | 0.274 | 0.65 |
| ridge_d10_lam100 | -1.50 | 0.13 | 0.272 | 0.43 |
| gp_d50_ls2 | -1.55 | 0.13 | 0.268 | 0.35 |
| pcareg_k10 | -1.62 | 0.13 | 0.262 | 0.29 |
| ridge_d10_lam1 | -1.67 | 0.13 | 0.257 | 0.29 |
| ridge_d50_lam100 | -1.88 | 0.13 | 0.239 | 0.24 |
| pcareg_k20 | -2.11 | 0.14 | 0.220 | 0.26 |
| mlp_h256_d50 | -2.21 | 0.14 | 0.212 | 0.51 |
| mlp_h1024_d50 | -2.25 | 0.14 | 0.209 | 0.37 |
| pcareg_k50 | -2.33 | 0.14 | 0.203 | 0.19 |
| ridge_d50_lam1 | -2.43 | 0.14 | 0.196 | 0.19 |
| pcareg_k100 | -2.45 | 0.14 | 0.194 | 0.20 |
| pcareg_k200 | -2.63 | 0.15 | 0.181 | 0.19 |
| scgen | -2.92 | 0.15 | 0.161 | 0.64 |
| knn_k20 | -3.14 | 0.16 | 0.148 | 0.56 |
| knn_k5 | -3.21 | 0.16 | 0.143 | 0.40 |
| ridge_d50_lam100_tf0.3 | -3.21 | 0.16 | 0.143 | 0.49 |
| knn_k1 | -3.26 | 0.16 | 0.141 | 0.68 |
| knn_k20_tf0.3 | -3.84 | 0.17 | 0.109 | 0.56 |
| scvi_cf | -3.84 | 0.17 | 0.109 | 1.31 |
| ridge_d50_lam100_tf0.1 | -4.23 | 0.18 | 0.091 | 0.25 |
| target_kd | -4.40 | 0.19 | 0.084 | 8.00 |
| knn_k20_tf0.1 | -4.44 | 0.19 | 0.082 | 0.80 |
| control_mean | -4.66 | 0.20 | 0.073 | 0.53 |
| random_shift_s0 | -4.91 | 0.21 | 0.064 | 0.33 |
| random_shift_s1 | -4.99 | 0.21 | 0.061 | 0.58 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.223 | 1.1e-06 | 470 |
| log_n_cells | 0.135 | 3.3e-03 | 470 |

## FrangiehIzar2021_RNA.perturbation

- items: 669; informative (non-degenerate): 461; nobody passes: 208; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.21, -1.74, -0.3, -0.3, 0.94]; median SE 0.65
- histogram (bin lower edge: count): -6: 2, -5: 26, -4: 26, -3: 47, -2: 45, -1: 233, +0: 82, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r10 | -0.61 | 0.10 | 0.378 | 2.82 |
| lowrank_r2 | -0.61 | 0.10 | 0.378 | 2.82 |
| lowrank_r5 | -0.61 | 0.10 | 0.378 | 2.82 |
| pcareg_k2 | -1.73 | 0.12 | 0.238 | 1.07 |
| ridge_d10_lam100 | -2.11 | 0.12 | 0.199 | 0.53 |
| pcareg_k5 | -2.18 | 0.13 | 0.193 | 0.51 |
| gp_d50_ls2 | -2.36 | 0.13 | 0.176 | 0.59 |
| pcareg_k10 | -2.38 | 0.13 | 0.175 | 0.39 |
| ridge_d10_lam1 | -2.46 | 0.13 | 0.167 | 0.40 |
| gp_d50_ls0.5 | -2.50 | 0.13 | 0.164 | 0.89 |
| ridge_d50_lam100 | -2.72 | 0.14 | 0.146 | 0.24 |
| pcareg_k20 | -2.72 | 0.14 | 0.146 | 0.25 |
| pcareg_k50 | -2.95 | 0.15 | 0.130 | 0.20 |
| ridge_d50_lam1 | -3.10 | 0.15 | 0.120 | 0.20 |
| pcareg_k100 | -3.19 | 0.15 | 0.114 | 0.17 |
| mlp_h256_d50 | -3.22 | 0.15 | 0.112 | 0.64 |
| mlp_h1024_d50 | -3.24 | 0.15 | 0.111 | 0.40 |
| ridge_d50_lam100_tf0.3 | -3.31 | 0.16 | 0.106 | 0.52 |
| pcareg_k200 | -3.36 | 0.16 | 0.103 | 0.17 |
| knn_k20 | -3.47 | 0.16 | 0.097 | 0.36 |
| knn_k20_tf0.3 | -3.66 | 0.17 | 0.087 | 0.41 |
| target_kd | -3.72 | 0.17 | 0.084 | 4.27 |
| knn_k20_tf0.1 | -3.72 | 0.17 | 0.084 | 0.59 |
| ridge_d50_lam100_tf0.1 | -3.74 | 0.17 | 0.082 | 0.46 |
| knn_k5 | -3.84 | 0.18 | 0.078 | 0.50 |
| control_mean | -4.00 | 0.18 | 0.070 | 0.52 |
| knn_k1 | -4.06 | 0.18 | 0.067 | 0.30 |
| random_shift_s1 | -4.06 | 0.18 | 0.067 | 0.38 |
| random_shift_s0 | -4.13 | 0.19 | 0.064 | 0.71 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.169 | 2.6e-04 | 461 |
| log_n_cells | 0.175 | 1.6e-04 | 461 |

## McFarlandTsherniak2020.context

- items: 866; informative (non-degenerate): 815; nobody passes: 51; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-5.79, -2.45, -0.59, 1.34, 4.78]; median SE 0.76
- histogram (bin lower edge: count): -6: 50, -5: 28, -4: 50, -3: 77, -2: 182, -1: 132, +0: 68, +1: 52, +2: 48, +3: 85, +4: 43, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 4.92 | 0.16 | 0.900 | 0.24 |
| pcareg_k100 | 3.53 | 0.14 | 0.823 | 0.25 |
| scgen | 3.29 | 0.13 | 0.808 | 2.28 |
| pcareg_k50 | 2.74 | 0.13 | 0.773 | 0.17 |
| pcareg_k20 | 2.11 | 0.12 | 0.727 | 0.18 |
| mlp_h1024_d50 | 1.90 | 0.12 | 0.711 | 0.37 |
| mlp_h256_d50 | 1.72 | 0.12 | 0.697 | 0.66 |
| pcareg_k10 | 1.42 | 0.12 | 0.672 | 0.25 |
| scvi_cf | 0.64 | 0.11 | 0.600 | 0.68 |
| pcareg_k5 | 0.56 | 0.11 | 0.592 | 0.45 |
| pcareg_k2 | -0.08 | 0.10 | 0.524 | 0.72 |
| lowrank_r10 | -0.95 | 0.10 | 0.421 | 1.44 |
| lowrank_r5 | -1.28 | 0.10 | 0.381 | 1.78 |
| lowrank_r2 | -1.36 | 0.10 | 0.371 | 3.06 |
| random_shift_s0 | -3.21 | 0.12 | 0.178 | 5.16 |
| random_shift_s1 | -3.23 | 0.12 | 0.177 | 3.00 |
| control_mean | -4.39 | 0.15 | 0.100 | 1.66 |
| target_kd | -9.87 | 0.92 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.165 | 2.2e-06 | 815 |
| log_n_cells | -0.126 | 3.0e-04 | 815 |
| dose | -0.076 | 3.2e-02 | 794 |

## McFarlandTsherniak2020.perturbation

- items: 866; informative (non-degenerate): 393; nobody passes: 473; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.16, -3.2, -1.93, -1.0, -0.22]; median SE 0.61
- histogram (bin lower edge: count): -6: 0, -5: 34, -4: 75, -3: 73, -2: 144, -1: 67, +0: 0, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | -1.57 | 0.11 | 0.285 | 0.41 |
| pcareg_k100 | -2.20 | 0.11 | 0.226 | 0.31 |
| mlp_h1024_d50 | -2.55 | 0.12 | 0.195 | 0.34 |
| pcareg_k50 | -2.58 | 0.12 | 0.193 | 0.23 |
| pcareg_k2 | -2.76 | 0.12 | 0.178 | 0.41 |
| mlp_h256_d50 | -2.77 | 0.12 | 0.177 | 0.39 |
| pcareg_k10 | -2.88 | 0.12 | 0.167 | 0.23 |
| pcareg_k20 | -3.03 | 0.12 | 0.156 | 0.22 |
| pcareg_k5 | -3.04 | 0.12 | 0.155 | 0.27 |
| random_shift_s0 | -3.24 | 0.12 | 0.140 | 0.97 |
| random_shift_s1 | -3.38 | 0.13 | 0.129 | 0.97 |
| control_mean | -3.75 | 0.13 | 0.104 | 0.75 |
| lowrank_r2 | -4.35 | 0.15 | 0.069 | 0.64 |
| lowrank_r10 | -4.35 | 0.15 | 0.069 | 0.64 |
| lowrank_r5 | -4.35 | 0.15 | 0.069 | 0.64 |
| target_kd | -8.87 | 0.96 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.320 | 8.4e-11 | 393 |
| log_n_cells | -0.028 | 5.8e-01 | 393 |
| dose | 0.033 | 5.2e-01 | 390 |

## NadigOConner2024_hepg2.perturbation

- items: 1061; informative (non-degenerate): 958; nobody passes: 100; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.17, -1.77, -0.47, 1.37, 2.47]; median SE 0.50
- histogram (bin lower edge: count): -6: 0, -5: 22, -4: 37, -3: 126, -2: 235, -1: 101, +0: 139, +1: 203, +2: 95, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | 0.21 | 0.08 | 0.532 | 0.58 |
| pcareg_k2 | 0.18 | 0.08 | 0.527 | 1.36 |
| pcareg_k5 | -0.01 | 0.08 | 0.502 | 0.58 |
| ridge_d10_lam100 | -0.05 | 0.08 | 0.497 | 0.44 |
| gp_d50_ls0.5 | -0.08 | 0.08 | 0.493 | 0.76 |
| pcareg_k10 | -0.17 | 0.08 | 0.481 | 0.39 |
| ridge_d10_lam1 | -0.19 | 0.08 | 0.478 | 0.39 |
| ridge_d50_lam100 | -0.25 | 0.08 | 0.470 | 0.32 |
| pcareg_k20 | -0.30 | 0.08 | 0.464 | 0.36 |
| pcareg_k50 | -0.47 | 0.08 | 0.440 | 0.31 |
| ridge_d50_lam1 | -0.49 | 0.08 | 0.438 | 0.31 |
| knn_k20 | -0.53 | 0.08 | 0.432 | 1.39 |
| pcareg_k100 | -0.55 | 0.08 | 0.430 | 0.29 |
| pcareg_k200 | -0.64 | 0.08 | 0.418 | 0.31 |
| mlp_h1024_d50 | -0.71 | 0.08 | 0.408 | 0.72 |
| knn_k20_tf0.3 | -0.76 | 0.08 | 0.402 | 1.35 |
| ridge_d50_lam100_tf0.3 | -0.89 | 0.08 | 0.385 | 1.15 |
| mlp_h256_d50 | -0.97 | 0.08 | 0.374 | 0.74 |
| knn_k20_tf0.1 | -1.04 | 0.08 | 0.365 | 1.83 |
| knn_k5 | -1.31 | 0.09 | 0.329 | 1.40 |
| ridge_d50_lam100_tf0.1 | -1.50 | 0.09 | 0.304 | 1.64 |
| knn_k1 | -1.86 | 0.09 | 0.260 | 1.61 |
| random_shift_s0 | -2.38 | 0.09 | 0.201 | 2.50 |
| random_shift_s1 | -2.40 | 0.09 | 0.199 | 2.43 |
| control_mean | -2.68 | 0.10 | 0.170 | 1.38 |
| target_kd | -3.11 | 0.11 | 0.131 | 9.05 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.085 | 8.5e-03 | 958 |
| log_n_cells | 0.014 | 6.6e-01 | 958 |

## NadigOConner2024_jurkat.perturbation

- items: 1815; informative (non-degenerate): 1595; nobody passes: 218; everybody passes: 2
- difficulty percentiles 5/25/50/75/95: [-3.81, -1.87, -0.83, 1.14, 2.58]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 52, -4: 79, -3: 252, -2: 394, -1: 189, +0: 191, +1: 275, +2: 163, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 0.53 | 0.07 | 0.577 | 1.38 |
| gp_d50_ls2 | 0.20 | 0.07 | 0.538 | 0.41 |
| ridge_d10_lam100 | 0.15 | 0.07 | 0.532 | 0.46 |
| pcareg_k10 | 0.13 | 0.07 | 0.529 | 0.45 |
| ridge_d10_lam1 | 0.12 | 0.07 | 0.528 | 0.45 |
| pcareg_k5 | 0.07 | 0.07 | 0.522 | 0.82 |
| pcareg_k20 | 0.02 | 0.07 | 0.516 | 0.39 |
| ridge_d50_lam100 | -0.01 | 0.07 | 0.512 | 0.31 |
| gp_d50_ls0.5 | -0.04 | 0.07 | 0.509 | 0.83 |
| ridge_d50_lam1 | -0.09 | 0.07 | 0.502 | 0.31 |
| pcareg_k50 | -0.09 | 0.07 | 0.502 | 0.30 |
| pcareg_k100 | -0.20 | 0.07 | 0.489 | 0.31 |
| pcareg_k200 | -0.31 | 0.07 | 0.475 | 0.32 |
| mlp_h1024_d50 | -0.73 | 0.07 | 0.421 | 0.63 |
| mlp_h256_d50 | -1.01 | 0.07 | 0.385 | 0.91 |
| ridge_d50_lam100_tf0.3 | -1.02 | 0.07 | 0.384 | 1.09 |
| knn_k20 | -1.07 | 0.07 | 0.378 | 1.27 |
| knn_k20_tf0.3 | -1.25 | 0.07 | 0.355 | 1.31 |
| knn_k20_tf0.1 | -1.48 | 0.07 | 0.325 | 2.06 |
| ridge_d50_lam100_tf0.1 | -1.68 | 0.07 | 0.300 | 1.64 |
| knn_k5 | -1.78 | 0.07 | 0.288 | 1.40 |
| knn_k1 | -2.42 | 0.07 | 0.213 | 1.89 |
| random_shift_s1 | -2.62 | 0.07 | 0.192 | 2.43 |
| random_shift_s0 | -2.66 | 0.07 | 0.188 | 2.76 |
| control_mean | -3.11 | 0.08 | 0.145 | 1.81 |
| target_kd | -3.22 | 0.08 | 0.136 | 10.51 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.173 | 3.5e-12 | 1595 |
| log_n_cells | -0.030 | 2.3e-01 | 1595 |

## NormanWeissman2019_filtered.perturbation

- items: 236; informative (non-degenerate): 225; nobody passes: 9; everybody passes: 2
- difficulty percentiles 5/25/50/75/95: [-2.4, -1.36, -0.96, 0.88, 3.65]; median SE 0.61
- histogram (bin lower edge: count): -6: 0, -5: 3, -4: 6, -3: 23, -2: 57, -1: 67, +0: 14, +1: 17, +2: 20, +3: 12, +4: 6, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls0.5 | 2.74 | 0.25 | 0.835 | 0.41 |
| gp_d50_ls2 | 2.38 | 0.24 | 0.809 | 0.40 |
| knn_k5 | 1.80 | 0.22 | 0.763 | 0.72 |
| ridge_d50_lam100 | 1.80 | 0.22 | 0.763 | 0.28 |
| knn_k20 | 1.75 | 0.22 | 0.758 | 0.95 |
| mlp_h1024_d50 | 1.65 | 0.22 | 0.750 | 0.52 |
| mlp_h256_d50 | 1.56 | 0.22 | 0.742 | 0.35 |
| ridge_d50_lam1 | 1.51 | 0.21 | 0.737 | 0.28 |
| ridge_d10_lam100 | 1.47 | 0.21 | 0.733 | 0.32 |
| pcareg_k20 | 1.47 | 0.21 | 0.733 | 0.20 |
| pcareg_k50 | 1.42 | 0.21 | 0.729 | 0.20 |
| pcareg_k200 | 1.38 | 0.21 | 0.725 | 0.20 |
| pcareg_k10 | 1.38 | 0.21 | 0.725 | 0.23 |
| pcareg_k100 | 1.33 | 0.21 | 0.720 | 0.21 |
| ridge_d10_lam1 | 1.33 | 0.21 | 0.720 | 0.26 |
| ridge_d50_lam100_tf0.3 | 1.08 | 0.20 | 0.695 | 1.05 |
| pcareg_k5 | 1.08 | 0.20 | 0.695 | 0.31 |
| pcareg_k2 | 0.76 | 0.19 | 0.661 | 0.72 |
| knn_k1 | 0.73 | 0.19 | 0.657 | 1.26 |
| knn_k20_tf0.3 | 0.02 | 0.18 | 0.568 | 2.16 |
| ridge_d50_lam100_tf0.1 | -0.28 | 0.17 | 0.525 | 2.66 |
| knn_k20_tf0.1 | -1.09 | 0.16 | 0.398 | 6.35 |
| target_kd | -1.49 | 0.16 | 0.335 | 4.67 |
| random_shift_s0 | -2.71 | 0.20 | 0.169 | 4.42 |
| random_shift_s1 | -2.82 | 0.20 | 0.157 | 3.01 |
| control_mean | -4.23 | 0.31 | 0.055 | 1.40 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.184 | 5.6e-03 | 225 |
| log_n_cells | 0.007 | 9.2e-01 | 225 |

## ReplogleWeissman2022_K562_essential.perturbation

- items: 1832; informative (non-degenerate): 1660; nobody passes: 169; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.26, -1.96, -0.84, 1.32, 2.76]; median SE 0.52
- histogram (bin lower edge: count): -6: 0, -5: 36, -4: 74, -3: 249, -2: 431, -1: 211, +0: 140, +1: 214, +2: 305, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| ridge_d10_lam100 | 0.39 | 0.07 | 0.563 | 0.38 |
| pcareg_k5 | 0.39 | 0.07 | 0.563 | 0.55 |
| gp_d50_ls2 | 0.37 | 0.07 | 0.561 | 0.36 |
| ridge_d10_lam1 | 0.37 | 0.07 | 0.560 | 0.35 |
| pcareg_k10 | 0.36 | 0.07 | 0.559 | 0.35 |
| pcareg_k2 | 0.32 | 0.07 | 0.555 | 2.00 |
| pcareg_k20 | 0.24 | 0.07 | 0.545 | 0.31 |
| ridge_d50_lam100 | 0.20 | 0.07 | 0.540 | 0.31 |
| pcareg_k50 | 0.14 | 0.07 | 0.533 | 0.28 |
| ridge_d50_lam1 | 0.12 | 0.07 | 0.531 | 0.29 |
| pcareg_k100 | 0.02 | 0.07 | 0.519 | 0.30 |
| pcareg_k200 | -0.04 | 0.07 | 0.511 | 0.30 |
| gp_d50_ls0.5 | -0.12 | 0.07 | 0.501 | 0.79 |
| ridge_d50_lam100_tf0.3 | -0.49 | 0.07 | 0.455 | 1.04 |
| mlp_h1024_d50 | -0.54 | 0.07 | 0.449 | 0.66 |
| mlp_h256_d50 | -0.82 | 0.06 | 0.412 | 0.91 |
| knn_k20 | -0.95 | 0.06 | 0.396 | 1.26 |
| knn_k20_tf0.3 | -1.05 | 0.06 | 0.383 | 1.47 |
| knn_k20_tf0.1 | -1.19 | 0.06 | 0.365 | 1.90 |
| ridge_d50_lam100_tf0.1 | -1.19 | 0.06 | 0.364 | 1.37 |
| knn_k5 | -1.74 | 0.07 | 0.293 | 1.53 |
| knn_k1 | -2.23 | 0.07 | 0.234 | 1.90 |
| random_shift_s1 | -2.77 | 0.07 | 0.175 | 3.62 |
| random_shift_s0 | -2.81 | 0.07 | 0.171 | 4.10 |
| target_kd | -2.97 | 0.08 | 0.155 | 10.30 |
| control_mean | -3.43 | 0.08 | 0.116 | 2.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.056 | 2.2e-02 | 1660 |
| log_n_cells | -0.056 | 2.2e-02 | 1660 |

## ReplogleWeissman2022_K562_gwps.perturbation

- items: 9326; informative (non-degenerate): 8422; nobody passes: 872; everybody passes: 32
- difficulty percentiles 5/25/50/75/95: [-3.87, -1.66, -0.39, 0.97, 2.65]; median SE 0.49
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 965, -3: 759, -2: 1333, -1: 2040, +0: 1254, +1: 1316, +2: 755, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k5 | 0.05 | 0.03 | 0.517 | 0.70 |
| ridge_d10_lam100 | 0.05 | 0.03 | 0.516 | 0.47 |
| pcareg_k10 | 0.04 | 0.03 | 0.515 | 0.46 |
| ridge_d10_lam1 | 0.04 | 0.03 | 0.514 | 0.46 |
| ridge_d50_lam100 | 0.02 | 0.03 | 0.512 | 0.40 |
| pcareg_k20 | 0.01 | 0.03 | 0.511 | 0.45 |
| pcareg_k50 | -0.00 | 0.03 | 0.509 | 0.39 |
| ridge_d50_lam1 | -0.00 | 0.03 | 0.509 | 0.39 |
| pcareg_k100 | -0.01 | 0.03 | 0.508 | 0.40 |
| pcareg_k2 | -0.01 | 0.03 | 0.508 | 1.70 |
| pcareg_k200 | -0.03 | 0.03 | 0.505 | 0.40 |
| gp_d50_ls2 | -0.16 | 0.03 | 0.488 | 0.94 |
| ridge_d50_lam100_tf0.3 | -0.29 | 0.03 | 0.469 | 0.98 |
| gp_d50_ls0.5 | -0.42 | 0.03 | 0.452 | 1.01 |
| mlp_h256_d50 | -0.43 | 0.03 | 0.450 | 1.26 |
| mlp_h1024_d50 | -0.56 | 0.03 | 0.431 | 1.07 |
| ridge_d50_lam100_tf0.1 | -0.68 | 0.03 | 0.415 | 1.16 |
| knn_k20 | -1.09 | 0.03 | 0.360 | 0.91 |
| knn_k20_tf0.3 | -1.09 | 0.03 | 0.359 | 0.94 |
| knn_k20_tf0.1 | -1.19 | 0.03 | 0.346 | 1.12 |
| knn_k5 | -1.20 | 0.03 | 0.345 | 0.90 |
| knn_k1 | -1.31 | 0.03 | 0.331 | 0.88 |
| random_shift_s0 | -1.40 | 0.03 | 0.320 | 1.07 |
| random_shift_s1 | -1.40 | 0.03 | 0.320 | 1.06 |
| control_mean | -1.51 | 0.03 | 0.305 | 0.74 |
| target_kd | -2.90 | 0.04 | 0.157 | 7.57 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.172 | 4.7e-57 | 8422 |
| log_n_cells | -0.060 | 4.4e-08 | 8422 |

## ReplogleWeissman2022_rpe1.perturbation

- items: 1611; informative (non-degenerate): 1380; nobody passes: 228; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.48, -1.88, -0.74, 1.14, 2.25]; median SE 0.49
- histogram (bin lower edge: count): -6: 0, -5: 38, -4: 81, -3: 210, -2: 310, -1: 200, +0: 190, +1: 173, +2: 178, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 0.07 | 0.07 | 0.518 | 1.39 |
| pcareg_k5 | -0.17 | 0.07 | 0.487 | 0.75 |
| gp_d50_ls2 | -0.20 | 0.07 | 0.484 | 0.52 |
| ridge_d10_lam100 | -0.23 | 0.07 | 0.480 | 0.48 |
| pcareg_k10 | -0.27 | 0.07 | 0.475 | 0.45 |
| ridge_d10_lam1 | -0.29 | 0.07 | 0.472 | 0.45 |
| pcareg_k20 | -0.33 | 0.07 | 0.467 | 0.45 |
| ridge_d50_lam100 | -0.42 | 0.07 | 0.456 | 0.36 |
| pcareg_k50 | -0.49 | 0.07 | 0.446 | 0.37 |
| ridge_d50_lam1 | -0.51 | 0.07 | 0.444 | 0.37 |
| gp_d50_ls0.5 | -0.52 | 0.07 | 0.443 | 0.80 |
| pcareg_k100 | -0.59 | 0.07 | 0.434 | 0.37 |
| pcareg_k200 | -0.61 | 0.07 | 0.431 | 0.35 |
| mlp_h1024_d50 | -1.03 | 0.07 | 0.377 | 0.66 |
| mlp_h256_d50 | -1.22 | 0.07 | 0.352 | 0.69 |
| knn_k20 | -1.27 | 0.07 | 0.345 | 1.31 |
| ridge_d50_lam100_tf0.3 | -1.31 | 0.07 | 0.340 | 1.15 |
| knn_k20_tf0.3 | -1.39 | 0.07 | 0.330 | 1.48 |
| knn_k20_tf0.1 | -1.70 | 0.07 | 0.291 | 2.01 |
| ridge_d50_lam100_tf0.1 | -1.90 | 0.07 | 0.266 | 1.46 |
| knn_k5 | -1.99 | 0.07 | 0.256 | 1.14 |
| knn_k1 | -2.42 | 0.08 | 0.207 | 1.20 |
| random_shift_s1 | -2.69 | 0.08 | 0.179 | 1.62 |
| random_shift_s0 | -2.71 | 0.08 | 0.178 | 1.35 |
| control_mean | -2.81 | 0.08 | 0.168 | 1.07 |
| target_kd | -3.29 | 0.09 | 0.126 | 9.84 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.206 | 9.4e-15 | 1380 |
| log_n_cells | -0.067 | 1.3e-02 | 1380 |

## SrivatsanTrapnell2020_sciplex3.context

- items: 2423; informative (non-degenerate): 1975; nobody passes: 448; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.15, -1.93, -0.98, 0.65, 1.85]; median SE 0.60
- histogram (bin lower edge: count): -6: 17, -5: 36, -4: 84, -3: 247, -2: 531, -1: 452, +0: 212, +1: 396, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k50 | 0.06 | 0.06 | 0.524 | 0.36 |
| pcareg_k100 | -0.05 | 0.06 | 0.509 | 0.37 |
| pcareg_k20 | -0.06 | 0.06 | 0.508 | 0.38 |
| pcareg_k200 | -0.18 | 0.06 | 0.492 | 0.39 |
| pcareg_k10 | -0.49 | 0.06 | 0.451 | 0.42 |
| mlp_h256_d50 | -0.56 | 0.05 | 0.442 | 0.59 |
| lowrank_r10 | -0.71 | 0.05 | 0.420 | 1.26 |
| pcareg_k5 | -0.78 | 0.05 | 0.411 | 0.51 |
| lowrank_r5 | -0.87 | 0.05 | 0.399 | 1.11 |
| lowrank_r2 | -0.87 | 0.05 | 0.399 | 1.49 |
| pcareg_k2 | -0.88 | 0.05 | 0.397 | 0.70 |
| mlp_h1024_d50 | -0.96 | 0.05 | 0.386 | 0.95 |
| scgen | -2.00 | 0.06 | 0.248 | 1.35 |
| scvi_cf | -2.77 | 0.07 | 0.162 | 1.24 |
| random_shift_s0 | -3.26 | 0.07 | 0.119 | 1.72 |
| random_shift_s1 | -3.32 | 0.07 | 0.114 | 1.99 |
| control_mean | -3.66 | 0.08 | 0.091 | 1.65 |
| target_kd | -9.71 | 0.92 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.132 | 4.2e-09 | 1975 |
| log_n_cells | 0.100 | 8.0e-06 | 1975 |
| dose | -0.007 | 7.7e-01 | 1975 |

## SrivatsanTrapnell2020_sciplex3.perturbation

- items: 2423; informative (non-degenerate): 2092; nobody passes: 331; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.04, -1.08, -0.44, 0.31, 1.53]; median SE 0.59
- histogram (bin lower edge: count): -6: 0, -5: 8, -4: 8, -3: 211, -2: 589, -1: 629, +0: 480, +1: 167, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k50 | -0.36 | 0.05 | 0.459 | 0.56 |
| pcareg_k100 | -0.36 | 0.05 | 0.459 | 0.57 |
| pcareg_k200 | -0.37 | 0.05 | 0.457 | 0.57 |
| lowrank_r10 | -0.52 | 0.05 | 0.431 | 0.97 |
| lowrank_r5 | -0.52 | 0.05 | 0.431 | 0.97 |
| lowrank_r2 | -0.52 | 0.05 | 0.431 | 0.97 |
| pcareg_k20 | -0.81 | 0.05 | 0.379 | 0.65 |
| pcareg_k10 | -1.34 | 0.05 | 0.291 | 0.60 |
| mlp_h1024_d50 | -1.40 | 0.05 | 0.281 | 1.07 |
| mlp_h256_d50 | -1.45 | 0.05 | 0.272 | 1.20 |
| pcareg_k5 | -1.56 | 0.05 | 0.256 | 0.73 |
| pcareg_k2 | -1.65 | 0.05 | 0.242 | 1.43 |
| random_shift_s1 | -2.73 | 0.07 | 0.116 | 1.32 |
| random_shift_s0 | -2.77 | 0.07 | 0.112 | 1.45 |
| control_mean | -3.06 | 0.08 | 0.090 | 1.00 |
| target_kd | -8.76 | 0.96 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.280 | 4.8e-39 | 2092 |
| log_n_cells | 0.065 | 3.0e-03 | 2092 |
| dose | 0.162 | 8.4e-14 | 2092 |

## TianKampmann2019_day7neuron.perturbation

- items: 35; informative (non-degenerate): 29; nobody passes: 6; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-1.95, 0.15, 0.72, 2.33, 3.05]; median SE 0.55
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 0, -3: 2, -2: 4, -1: 1, +0: 8, +1: 5, +2: 3, +3: 6, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | 1.97 | 0.45 | 0.571 | 1.05 |
| pcareg_k2 | 1.76 | 0.45 | 0.543 | 0.48 |
| gp_d50_ls2 | 1.36 | 0.45 | 0.486 | 0.58 |
| ridge_d10_lam100 | 1.16 | 0.45 | 0.457 | 0.32 |
| pcareg_k5 | 0.96 | 0.45 | 0.429 | 0.46 |
| pcareg_k10 | 0.13 | 0.47 | 0.314 | 0.42 |
| ridge_d50_lam100 | -0.09 | 0.47 | 0.286 | 0.37 |
| ridge_d50_lam100_tf0.3 | -0.32 | 0.49 | 0.257 | 1.16 |
| ridge_d10_lam1 | -0.32 | 0.49 | 0.257 | 0.34 |
| knn_k20_tf0.3 | -0.56 | 0.50 | 0.229 | 2.00 |
| pcareg_k20 | -0.56 | 0.50 | 0.229 | 0.32 |
| pcareg_k200 | -1.10 | 0.54 | 0.171 | 0.20 |
| pcareg_k100 | -1.10 | 0.54 | 0.171 | 0.20 |
| pcareg_k50 | -1.10 | 0.54 | 0.171 | 0.20 |
| ridge_d50_lam100_tf0.1 | -1.10 | 0.54 | 0.171 | 1.28 |
| ridge_d50_lam1 | -1.40 | 0.56 | 0.143 | 0.20 |
| gp_d50_ls0.5 | -1.40 | 0.56 | 0.143 | 0.31 |
| knn_k5 | -1.74 | 0.60 | 0.114 | 0.45 |
| random_shift_s0 | -1.74 | 0.60 | 0.114 | 2.11 |
| knn_k20_tf0.1 | -2.13 | 0.65 | 0.086 | 1.35 |
| mlp_h1024_d50 | -2.61 | 0.73 | 0.057 | 8.89 |
| mlp_h256_d50 | -3.25 | 0.89 | 0.029 | 0.11 |
| random_shift_s1 | -3.25 | 0.89 | 0.029 | 0.13 |
| control_mean | -4.40 | 1.32 | 0.000 | 0.01 |
| knn_k1 | -4.40 | 1.32 | 0.000 | 0.01 |
| target_kd | -4.40 | 1.32 | 0.000 | 0.01 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.429 | 2.0e-02 | 29 |
| log_n_cells | 0.248 | 2.0e-01 | 29 |

## TianKampmann2019_iPSC.perturbation

- items: 81; informative (non-degenerate): 45; nobody passes: 36; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.63, -0.98, 1.01, 1.91, 1.91]; median SE 0.86
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 5, -3: 1, -2: 3, -1: 9, +0: 1, +1: 26, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 1.89 | 0.30 | 0.457 | 0.41 |
| ridge_d10_lam100 | 0.34 | 0.36 | 0.272 | 0.33 |
| gp_d50_ls2 | 0.07 | 0.37 | 0.247 | 0.51 |
| ridge_d10_lam1 | -0.68 | 0.41 | 0.185 | 0.17 |
| pcareg_k10 | -0.86 | 0.42 | 0.173 | 0.18 |
| pcareg_k5 | -0.86 | 0.42 | 0.173 | 0.20 |
| pcareg_k20 | -1.65 | 0.47 | 0.123 | 0.34 |
| ridge_d50_lam100 | -1.88 | 0.49 | 0.111 | 0.19 |
| knn_k20 | -1.88 | 0.49 | 0.111 | 0.16 |
| gp_d50_ls0.5 | -2.13 | 0.51 | 0.099 | 0.20 |
| pcareg_k50 | -2.69 | 0.56 | 0.074 | 0.07 |
| pcareg_k100 | -3.02 | 0.58 | 0.062 | 0.06 |
| ridge_d50_lam1 | -3.02 | 0.58 | 0.062 | 0.06 |
| pcareg_k200 | -3.02 | 0.58 | 0.062 | 0.06 |
| target_kd | -4.26 | 0.73 | 0.025 | 6.73 |
| ridge_d50_lam100_tf0.1 | -4.88 | 0.86 | 0.012 | 4.47 |
| knn_k20_tf0.1 | -4.88 | 0.86 | 0.012 | 4.47 |
| random_shift_s1 | -4.88 | 0.86 | 0.012 | 0.63 |
| ridge_d50_lam100_tf0.3 | -4.88 | 0.86 | 0.012 | 0.05 |
| mlp_h1024_d50 | -5.87 | 1.19 | 0.000 | 0.01 |
| mlp_h256_d50 | -5.87 | 1.19 | 0.000 | 0.01 |
| knn_k20_tf0.3 | -5.87 | 1.19 | 0.000 | 0.01 |
| knn_k1 | -5.87 | 1.19 | 0.000 | 0.01 |
| control_mean | -5.87 | 1.19 | 0.000 | 0.01 |
| knn_k5 | -5.87 | 1.19 | 0.000 | 0.01 |
| random_shift_s0 | -5.87 | 1.19 | 0.000 | 0.01 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.479 | 8.6e-04 | 45 |
| log_n_cells | 0.336 | 2.4e-02 | 45 |

## TianKampmann2021_CRISPRi.perturbation

- items: 183; informative (non-degenerate): 72; nobody passes: 111; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.28, -1.2, -0.61, 0.24, 0.24]; median SE 0.82
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 6, -3: 7, -2: 11, -1: 15, +0: 33, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | -0.65 | 0.23 | 0.224 | 0.42 |
| ridge_d10_lam100 | -1.15 | 0.25 | 0.175 | 0.30 |
| pcareg_k2 | -1.40 | 0.26 | 0.153 | 0.56 |
| pcareg_k5 | -2.26 | 0.31 | 0.093 | 0.18 |
| target_kd | -2.56 | 0.33 | 0.077 | 0.98 |
| gp_d50_ls0.5 | -2.67 | 0.34 | 0.071 | 0.26 |
| pcareg_k10 | -2.92 | 0.36 | 0.060 | 0.11 |
| ridge_d50_lam100 | -3.20 | 0.39 | 0.049 | 0.09 |
| ridge_d10_lam1 | -3.35 | 0.40 | 0.044 | 0.10 |
| pcareg_k20 | -3.72 | 0.45 | 0.033 | 0.09 |
| knn_k20 | -3.93 | 0.48 | 0.027 | 0.50 |
| knn_k20_tf0.3 | -4.18 | 0.52 | 0.022 | 0.41 |
| pcareg_k50 | -5.36 | 0.80 | 0.005 | 0.04 |
| mlp_h256_d50 | -5.36 | 0.80 | 0.005 | 0.04 |
| knn_k20_tf0.1 | -5.36 | 0.80 | 0.005 | 0.36 |
| knn_k5 | -6.24 | 1.13 | 0.000 | 0.00 |
| knn_k1 | -6.24 | 1.13 | 0.000 | 0.00 |
| control_mean | -6.24 | 1.13 | 0.000 | 0.00 |
| mlp_h1024_d50 | -6.24 | 1.13 | 0.000 | 0.00 |
| random_shift_s0 | -6.24 | 1.13 | 0.000 | 0.00 |
| pcareg_k100 | -6.24 | 1.13 | 0.000 | 0.00 |
| pcareg_k200 | -6.24 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam1 | -6.24 | 1.13 | 0.000 | 0.00 |
| random_shift_s1 | -6.24 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam100_tf0.1 | -6.24 | 1.13 | 0.000 | 0.00 |
| ridge_d50_lam100_tf0.3 | -6.24 | 1.13 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.218 | 6.5e-02 | 72 |
| log_n_cells | 0.162 | 1.7e-01 | 72 |

## parse_pbmc_cytokines.context

- items: 13967; informative (non-degenerate): 13366; nobody passes: 601; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.71, -2.07, -0.52, 1.97, 3.74]; median SE 0.54
- histogram (bin lower edge: count): -6: 99, -5: 410, -4: 745, -3: 2574, -2: 2035, -1: 1657, +0: 1122, +1: 1553, +2: 1913, +3: 1200, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 3.80 | 0.03 | 0.871 | 0.79 |
| pcareg_k100 | 1.90 | 0.03 | 0.711 | 0.52 |
| mlp_h256_d50 | 1.69 | 0.03 | 0.691 | 0.52 |
| mlp_h1024_d50 | 1.30 | 0.03 | 0.653 | 0.48 |
| lowrank_r10 | 0.66 | 0.03 | 0.588 | 0.82 |
| ridge_d50_lam100 | 0.63 | 0.03 | 0.585 | 0.28 |
| pcareg_k50 | 0.62 | 0.03 | 0.584 | 0.28 |
| ridge_d50_lam1 | 0.62 | 0.03 | 0.584 | 0.28 |
| ridge_d50_lam100_tf0.3 | 0.22 | 0.03 | 0.542 | 0.38 |
| gp_d50_ls2 | 0.17 | 0.03 | 0.537 | 0.42 |
| gp_d50_ls0.5 | 0.13 | 0.03 | 0.532 | 0.45 |
| knn_k20_tf0.1 | 0.10 | 0.03 | 0.529 | 1.26 |
| pcareg_k20 | -0.27 | 0.03 | 0.488 | 0.32 |
| ridge_d50_lam100_tf0.1 | -0.54 | 0.02 | 0.457 | 0.67 |
| ridge_d10_lam100 | -0.74 | 0.02 | 0.434 | 0.31 |
| ridge_d10_lam1 | -0.74 | 0.02 | 0.434 | 0.31 |
| pcareg_k10 | -0.74 | 0.02 | 0.434 | 0.31 |
| lowrank_r5 | -0.91 | 0.02 | 0.414 | 1.06 |
| knn_k20_tf0.3 | -1.22 | 0.02 | 0.378 | 4.36 |
| knn_k20 | -1.33 | 0.02 | 0.365 | 5.53 |
| pcareg_k5 | -1.66 | 0.02 | 0.326 | 0.41 |
| lowrank_r2 | -1.70 | 0.02 | 0.321 | 1.18 |
| scgen | -1.83 | 0.02 | 0.305 | 1.02 |
| scvi_cf | -1.98 | 0.02 | 0.287 | 0.76 |
| pcareg_k2 | -2.62 | 0.03 | 0.217 | 0.50 |
| knn_k5 | -2.67 | 0.03 | 0.211 | 3.85 |
| knn_k1 | -3.55 | 0.03 | 0.130 | 2.31 |
| random_shift_s1 | -4.47 | 0.04 | 0.072 | 0.92 |
| random_shift_s0 | -4.50 | 0.04 | 0.070 | 1.12 |
| control_mean | -5.07 | 0.05 | 0.047 | 0.52 |
| target_kd | -11.85 | 0.84 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.007 | 4.0e-01 | 13366 |
| log_n_cells | -0.399 | 0.0e+00 | 13366 |

## parse_pbmc_cytokines.perturbation

- items: 13967; informative (non-degenerate): 10744; nobody passes: 3223; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.39, -1.44, -0.23, 0.56, 0.56]; median SE 0.78
- histogram (bin lower edge: count): -6: 3, -5: 146, -4: 667, -3: 1006, -2: 2096, -1: 3483, +0: 3343, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | -0.20 | 0.02 | 0.466 | 2.74 |
| knn_k20_tf0.3 | -1.54 | 0.02 | 0.267 | 1.17 |
| knn_k5 | -1.60 | 0.02 | 0.259 | 1.21 |
| pcareg_k200 | -2.43 | 0.03 | 0.165 | 1.21 |
| knn_k1 | -2.51 | 0.03 | 0.158 | 0.91 |
| gp_d50_ls0.5 | -2.88 | 0.03 | 0.126 | 0.50 |
| ridge_d50_lam100_tf0.1 | -2.95 | 0.03 | 0.121 | 0.60 |
| mlp_h1024_d50 | -2.99 | 0.03 | 0.118 | 0.62 |
| pcareg_k100 | -3.12 | 0.03 | 0.108 | 0.57 |
| gp_d50_ls2 | -3.13 | 0.03 | 0.107 | 0.42 |
| ridge_d50_lam100_tf0.3 | -3.14 | 0.03 | 0.106 | 0.40 |
| mlp_h256_d50 | -3.15 | 0.03 | 0.105 | 0.63 |
| knn_k20_tf0.1 | -3.18 | 0.03 | 0.103 | 0.76 |
| pcareg_k50 | -3.47 | 0.03 | 0.085 | 0.19 |
| lowrank_r2 | -3.47 | 0.03 | 0.085 | 0.19 |
| lowrank_r10 | -3.47 | 0.03 | 0.085 | 0.19 |
| lowrank_r5 | -3.47 | 0.03 | 0.085 | 0.19 |
| ridge_d50_lam1 | -3.48 | 0.03 | 0.085 | 0.20 |
| ridge_d50_lam100 | -3.48 | 0.03 | 0.084 | 0.19 |
| random_shift_s1 | -3.75 | 0.04 | 0.070 | 0.72 |
| random_shift_s0 | -3.76 | 0.04 | 0.069 | 0.71 |
| pcareg_k20 | -3.76 | 0.04 | 0.069 | 0.27 |
| ridge_d10_lam1 | -4.01 | 0.04 | 0.057 | 0.23 |
| pcareg_k10 | -4.02 | 0.04 | 0.057 | 0.23 |
| ridge_d10_lam100 | -4.02 | 0.04 | 0.057 | 0.22 |
| pcareg_k5 | -4.12 | 0.04 | 0.053 | 0.39 |
| control_mean | -4.24 | 0.04 | 0.048 | 0.53 |
| pcareg_k2 | -4.26 | 0.04 | 0.047 | 0.48 |
| target_kd | -10.84 | 0.87 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.319 | 3.3e-252 | 10744 |
| log_n_cells | -0.209 | 9.6e-107 | 10744 |

## pooled

- items: 88164; informative (non-degenerate): 67855; nobody passes: 20264; everybody passes: 45
- difficulty percentiles 5/25/50/75/95: [-3.5, -2.06, -0.7, 0.41, 1.46]; median SE 0.54
- histogram (bin lower edge: count): -6: 786, -5: 1079, -4: 3779, -3: 11472, -2: 12500, -1: 17833, +0: 10386, +1: 10020, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | -1.10 | 0.01 | 0.351 | 1.21 |
| knn_k5 | -1.19 | 0.01 | 0.339 | 0.96 |
| pcareg_k200 | -1.31 | 0.02 | 0.339 | 0.66 |
| gp_d50_ls0.5 | -1.38 | 0.01 | 0.314 | 0.70 |
| gp_d50_ls2 | -1.42 | 0.01 | 0.309 | 0.64 |
| pcareg_k100 | -1.49 | 0.02 | 0.316 | 0.40 |
| knn_k1 | -1.54 | 0.01 | 0.295 | 0.90 |
| pcareg_k50 | -1.55 | 0.02 | 0.309 | 0.30 |
| ridge_d50_lam100 | -1.58 | 0.01 | 0.290 | 0.35 |
| knn_k20_tf0.3 | -1.62 | 0.01 | 0.284 | 0.92 |
| ridge_d50_lam100_tf0.3 | -1.62 | 0.01 | 0.284 | 0.52 |
| pcareg_k20 | -1.63 | 0.02 | 0.301 | 0.36 |
| mlp_h1024_d50 | -1.64 | 0.01 | 0.285 | 0.69 |
| ridge_d50_lam1 | -1.65 | 0.01 | 0.281 | 0.36 |
| ridge_d10_lam100 | -1.67 | 0.01 | 0.279 | 0.39 |
| pcareg_k10 | -1.68 | 0.02 | 0.294 | 0.36 |
| pcareg_k2 | -1.69 | 0.02 | 0.293 | 1.12 |
| pcareg_k5 | -1.70 | 0.02 | 0.292 | 0.53 |
| ridge_d10_lam1 | -1.71 | 0.01 | 0.274 | 0.39 |
| ridge_d50_lam100_tf0.1 | -1.76 | 0.01 | 0.268 | 0.61 |
| mlp_h256_d50 | -1.77 | 0.01 | 0.269 | 0.75 |
| knn_k20_tf0.1 | -2.00 | 0.01 | 0.240 | 0.77 |
| random_shift_s0 | -2.92 | 0.01 | 0.149 | 1.57 |
| random_shift_s1 | -2.92 | 0.01 | 0.148 | 1.59 |
| lowrank_r5 | -2.98 | 0.01 | 0.116 | 1.20 |
| lowrank_r10 | -2.98 | 0.01 | 0.116 | 1.20 |
| lowrank_r2 | -2.98 | 0.01 | 0.116 | 1.20 |
| control_mean | -3.87 | 0.01 | 0.081 | 0.92 |
| target_kd | -5.27 | 0.02 | 0.028 | 4.76 |

### Mean difficulty by dataset (dataset factor check)

| dataset | n items | mean difficulty | sd |
|---|---|---|---|
| AdamsonWeissman2016_GSM2406681_10X010 | 81 | -0.70 | 1.36 |
| FrangiehIzar2021_RNA | 461 | -0.23 | 1.34 |
| McFarlandTsherniak2020 | 393 | -1.21 | 1.26 |
| NadigOConner2024_hepg2 | 958 | -1.37 | 1.78 |
| NadigOConner2024_jurkat | 1595 | -1.52 | 1.79 |
| NormanWeissman2019_filtered | 225 | -2.59 | 1.54 |
| ReplogleWeissman2022_K562_essential | 1660 | -1.55 | 1.81 |
| ReplogleWeissman2022_K562_gwps | 8422 | -1.69 | 1.92 |
| ReplogleWeissman2022_rpe1 | 1380 | -1.32 | 1.77 |
| SrivatsanTrapnell2020_sciplex3 | 2092 | -1.41 | 1.03 |
| TianKampmann2019_day7neuron | 29 | -0.35 | 1.29 |
| TianKampmann2019_iPSC | 45 | 0.37 | 1.20 |
| TianKampmann2021_CRISPRi | 72 | 0.71 | 0.83 |
| parse_pbmc_cytokines | 10744 | 0.33 | 1.11 |
| tahoe100m | 39698 | -0.93 | 1.34 |

## pooled_context

- items: 71897; informative (non-degenerate): 70511; nobody passes: 1383; everybody passes: 3
- difficulty percentiles 5/25/50/75/95: [-3.32, -2.19, -0.52, 1.56, 4.81]; median SE 0.73
- histogram (bin lower edge: count): -6: 0, -5: 2324, -4: 5864, -3: 11203, -2: 8310, -1: 11284, +0: 9030, +1: 7677, +2: 5230, +3: 3251, +4: 2341, +5: 2962

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 5.41 | 0.02 | 0.795 | 0.80 |
| mlp_h256_d50 | 4.44 | 0.02 | 0.903 | 0.34 |
| mlp_h1024_d50 | 4.29 | 0.02 | 0.896 | 0.37 |
| pcareg_k100 | 4.10 | 0.02 | 0.670 | 0.50 |
| lowrank_r10 | 3.97 | 0.02 | 0.881 | 1.23 |
| pcareg_k50 | 3.11 | 0.02 | 0.571 | 0.29 |
| lowrank_r5 | 3.10 | 0.01 | 0.832 | 1.11 |
| ridge_d50_lam100 | 2.80 | 0.01 | 0.825 | 0.30 |
| ridge_d50_lam1 | 2.79 | 0.01 | 0.824 | 0.31 |
| ridge_d50_lam100_tf0.3 | 2.51 | 0.01 | 0.804 | 0.52 |
| knn_k20 | 2.50 | 0.01 | 0.803 | 1.55 |
| pcareg_k20 | 2.36 | 0.02 | 0.492 | 0.35 |
| lowrank_r2 | 1.97 | 0.01 | 0.744 | 1.69 |
| ridge_d50_lam100_tf0.1 | 1.94 | 0.01 | 0.756 | 0.62 |
| pcareg_k10 | 1.90 | 0.02 | 0.442 | 0.36 |
| knn_k20_tf0.3 | 1.79 | 0.01 | 0.742 | 1.24 |
| gp_d50_ls0.5 | 1.69 | 0.01 | 0.733 | 0.56 |
| knn_k5 | 1.68 | 0.01 | 0.732 | 0.92 |
| ridge_d10_lam1 | 1.26 | 0.01 | 0.690 | 0.33 |
| ridge_d10_lam100 | 1.26 | 0.01 | 0.690 | 0.34 |
| gp_d50_ls2 | 1.17 | 0.01 | 0.680 | 0.67 |
| pcareg_k5 | 1.06 | 0.02 | 0.348 | 0.66 |
| knn_k20_tf0.1 | 0.68 | 0.01 | 0.626 | 1.54 |
| knn_k1 | 0.38 | 0.01 | 0.590 | 0.95 |
| pcareg_k2 | 0.24 | 0.02 | 0.258 | 1.40 |
| scvi_cf | -0.08 | 0.01 | 0.520 | 1.00 |
| scgen | -0.42 | 0.01 | 0.477 | 1.76 |
| random_shift_s0 | -3.49 | 0.01 | 0.129 | 4.73 |
| random_shift_s1 | -3.54 | 0.01 | 0.126 | 4.98 |
| control_mean | -5.09 | 0.02 | 0.046 | 9.25 |
| target_kd | -9.77 | 0.13 | 0.001 | 1777.85 |

### Mean difficulty by dataset (dataset factor check)

| dataset | n items | mean difficulty | sd |
|---|---|---|---|
| FrangiehIzar2021_RNA | 470 | 3.47 | 2.75 |
| McFarlandTsherniak2020 | 815 | 0.42 | 3.11 |
| SrivatsanTrapnell2020_sciplex3 | 1975 | 2.14 | 2.52 |
| parse_pbmc_cytokines | 13366 | 2.16 | 2.49 |
| tahoe100m | 53885 | -0.83 | 2.08 |

## tahoe100m.context

- items: 53972; informative (non-degenerate): 53885; nobody passes: 87; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.22, -1.63, -0.6, 1.53, 4.27]; median SE 0.92
- histogram (bin lower edge: count): -6: 0, -5: 2153, -4: 0, -3: 5618, -2: 10954, -1: 7864, +0: 9111, +1: 6201, +2: 3953, +3: 4124, +4: 1418, +5: 1163

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| mlp_h1024_d50 | 8.18 | 0.06 | 0.994 | 0.25 |
| lowrank_r10 | 7.93 | 0.06 | 0.992 | 1.05 |
| mlp_h256_d50 | 7.56 | 0.05 | 0.990 | 0.41 |
| lowrank_r5 | 6.12 | 0.03 | 0.972 | 1.59 |
| knn_k20 | 4.53 | 0.02 | 0.924 | 0.25 |
| ridge_d50_lam100 | 3.92 | 0.02 | 0.895 | 0.31 |
| ridge_d50_lam1 | 3.92 | 0.02 | 0.894 | 0.33 |
| lowrank_r2 | 3.70 | 0.02 | 0.881 | 3.25 |
| ridge_d50_lam100_tf0.3 | 3.67 | 0.02 | 0.880 | 0.83 |
| knn_k5 | 3.58 | 0.02 | 0.874 | 0.65 |
| knn_k20_tf0.3 | 3.13 | 0.02 | 0.844 | 0.31 |
| ridge_d50_lam100_tf0.1 | 3.10 | 0.02 | 0.842 | 0.84 |
| gp_d50_ls0.5 | 2.45 | 0.01 | 0.790 | 0.55 |
| ridge_d10_lam1 | 2.13 | 0.01 | 0.762 | 0.30 |
| ridge_d10_lam100 | 2.12 | 0.01 | 0.762 | 0.30 |
| gp_d50_ls2 | 1.72 | 0.01 | 0.723 | 0.58 |
| knn_k1 | 1.64 | 0.01 | 0.714 | 1.19 |
| knn_k20_tf0.1 | 1.12 | 0.01 | 0.657 | 0.80 |
| scvi_cf | 0.64 | 0.01 | 0.600 | 1.20 |
| scgen | 0.09 | 0.01 | 0.530 | 1.09 |
| random_shift_s0 | -3.14 | 0.02 | 0.145 | 2.83 |
| random_shift_s1 | -3.20 | 0.02 | 0.141 | 2.73 |
| control_mean | -5.09 | 0.03 | 0.043 | 0.93 |
| target_kd | -13.11 | 0.80 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | 0.010 | 1.6e-02 | 53885 |
| log_n_cells | -0.173 | 0.0e+00 | 53885 |
| dose | -0.236 | 0.0e+00 | 53885 |

## tahoe100m.perturbation

- items: 53972; informative (non-degenerate): 39698; nobody passes: 14274; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-3.43, -1.96, -1.04, -0.12, 1.05]; median SE 0.53
- histogram (bin lower edge: count): -6: 48, -5: 520, -4: 3696, -3: 5599, -2: 10032, -1: 10775, +0: 3849, +1: 5160, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k5 | -1.04 | 0.01 | 0.368 | 0.76 |
| knn_k1 | -1.28 | 0.01 | 0.335 | 0.78 |
| gp_d50_ls0.5 | -1.40 | 0.01 | 0.320 | 0.70 |
| knn_k20 | -1.41 | 0.01 | 0.318 | 0.67 |
| gp_d50_ls2 | -1.52 | 0.01 | 0.304 | 0.68 |
| mlp_h1024_d50 | -1.62 | 0.01 | 0.291 | 0.67 |
| ridge_d50_lam100_tf0.3 | -1.65 | 0.01 | 0.287 | 0.41 |
| ridge_d50_lam100 | -1.70 | 0.01 | 0.281 | 0.38 |
| ridge_d50_lam100_tf0.1 | -1.71 | 0.01 | 0.279 | 0.45 |
| ridge_d50_lam1 | -1.78 | 0.01 | 0.271 | 0.41 |
| mlp_h256_d50 | -1.78 | 0.01 | 0.270 | 0.71 |
| knn_k20_tf0.3 | -1.80 | 0.01 | 0.269 | 0.59 |
| ridge_d10_lam100 | -1.82 | 0.01 | 0.266 | 0.40 |
| ridge_d10_lam1 | -1.87 | 0.01 | 0.260 | 0.42 |
| knn_k20_tf0.1 | -1.97 | 0.01 | 0.248 | 0.63 |
| random_shift_s0 | -3.02 | 0.01 | 0.139 | 1.91 |
| random_shift_s1 | -3.02 | 0.01 | 0.139 | 1.97 |
| lowrank_r5 | -3.41 | 0.02 | 0.108 | 1.74 |
| lowrank_r10 | -3.41 | 0.02 | 0.108 | 1.74 |
| lowrank_r2 | -3.41 | 0.02 | 0.108 | 1.74 |
| control_mean | -4.61 | 0.02 | 0.043 | 1.20 |
| target_kd | -12.31 | 0.82 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.047 | 1.6e-20 | 39698 |
| log_n_cells | -0.087 | 2.7e-68 | 39698 |
| dose | -0.142 | 8.0e-178 | 39698 |

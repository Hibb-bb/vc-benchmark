# Component B summary: pert_idict_v0


## immune_dictionary.context

- items: 963; informative (non-degenerate): 930; nobody passes: 33; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-4.09, -1.46, -0.02, 1.25, 3.51]; median SE 0.68
- histogram (bin lower edge: count): -6: 0, -5: 64, -4: 35, -3: 87, -2: 74, -1: 218, +0: 155, +1: 123, +2: 111, +3: 30, +4: 23, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| ridge_d50_lam100 | 3.36 | 0.12 | 0.869 | 0.23 |
| ridge_d50_lam1 | 3.01 | 0.11 | 0.843 | 0.30 |
| gp_d50_ls0.5 | 2.60 | 0.11 | 0.808 | 0.35 |
| lowrank_r5 | 2.42 | 0.10 | 0.791 | 2.43 |
| gp_d50_ls2 | 2.33 | 0.10 | 0.782 | 0.52 |
| lowrank_r10 | 2.01 | 0.10 | 0.749 | 3.14 |
| lowrank_r2 | 1.80 | 0.09 | 0.725 | 3.22 |
| mlp_h1024_d50 | 1.38 | 0.09 | 0.674 | 0.49 |
| mlp_h256_d50 | 0.80 | 0.09 | 0.597 | 0.51 |
| knn_k20 | -0.03 | 0.09 | 0.483 | 1.17 |
| ridge_d50_lam100_tf0.3 | -0.39 | 0.09 | 0.433 | 1.13 |
| ridge_d10_lam100 | -0.67 | 0.09 | 0.396 | 0.47 |
| ridge_d10_lam1 | -0.69 | 0.09 | 0.393 | 0.50 |
| knn_k20_tf0.3 | -0.80 | 0.09 | 0.379 | 2.12 |
| ridge_d50_lam100_tf0.1 | -2.66 | 0.11 | 0.180 | 1.53 |
| knn_k5 | -2.72 | 0.11 | 0.175 | 0.48 |
| knn_k1 | -3.82 | 0.14 | 0.102 | 0.54 |
| knn_k20_tf0.1 | -3.94 | 0.14 | 0.096 | 1.05 |
| random_shift_s0 | -6.31 | 0.26 | 0.020 | 4.23 |
| random_shift_s1 | -6.38 | 0.26 | 0.019 | 0.98 |
| control_mean | -9.05 | 0.72 | 0.001 | 0.00 |
| target_kd | -9.72 | 0.95 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.164 | 5.2e-07 | 930 |
| log_n_cells | -0.105 | 1.3e-03 | 930 |

## immune_dictionary.perturbation

- items: 963; informative (non-degenerate): 757; nobody passes: 206; everybody passes: 0
- difficulty percentiles 5/25/50/75/95: [-2.66, -1.26, -0.63, 0.24, 0.98]; median SE 0.59
- histogram (bin lower edge: count): -6: 0, -5: 0, -4: 20, -3: 102, -2: 110, -1: 266, +0: 259, +1: 0, +2: 0, +3: 0, +4: 0, +5: 0

### Abilities

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| lowrank_r10 | -0.93 | 0.08 | 0.348 | 0.66 |
| lowrank_r2 | -0.93 | 0.08 | 0.348 | 0.66 |
| lowrank_r5 | -0.93 | 0.08 | 0.348 | 0.66 |
| ridge_d50_lam1 | -1.10 | 0.08 | 0.322 | 0.57 |
| ridge_d50_lam100 | -1.23 | 0.08 | 0.302 | 0.65 |
| knn_k20_tf0.3 | -1.46 | 0.09 | 0.269 | 1.57 |
| gp_d50_ls2 | -1.73 | 0.09 | 0.234 | 0.73 |
| gp_d50_ls0.5 | -1.90 | 0.09 | 0.212 | 2.05 |
| knn_k20 | -2.00 | 0.09 | 0.199 | 0.74 |
| mlp_h1024_d50 | -2.06 | 0.09 | 0.192 | 0.52 |
| ridge_d50_lam100_tf0.3 | -2.11 | 0.10 | 0.187 | 0.97 |
| mlp_h256_d50 | -2.30 | 0.10 | 0.166 | 0.55 |
| knn_k5 | -2.84 | 0.11 | 0.115 | 0.82 |
| ridge_d50_lam100_tf0.1 | -3.01 | 0.12 | 0.102 | 0.73 |
| ridge_d10_lam100 | -3.11 | 0.12 | 0.094 | 0.46 |
| ridge_d10_lam1 | -3.17 | 0.12 | 0.090 | 0.45 |
| knn_k20_tf0.1 | -4.04 | 0.16 | 0.045 | 0.54 |
| knn_k1 | -4.07 | 0.17 | 0.044 | 0.92 |
| random_shift_s1 | -5.12 | 0.25 | 0.017 | 0.86 |
| random_shift_s0 | -5.59 | 0.31 | 0.010 | 1.16 |
| control_mean | -7.39 | 0.72 | 0.001 | 0.13 |
| target_kd | -8.10 | 1.00 | 0.000 | 0.00 |

### Difficulty vs covariates (prediction: difficulty falls with effect size)

| covariate | Spearman rho | p | n |
|---|---|---|---|
| delta_l2 | -0.527 | 2.0e-55 | 757 |
| log_n_cells | 0.069 | 5.7e-02 | 757 |

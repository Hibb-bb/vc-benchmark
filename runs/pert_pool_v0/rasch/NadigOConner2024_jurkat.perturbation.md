# NadigOConner2024_jurkat.perturbation

- items: 1815, respondents: 26, loglik: -16987.1, iters: 394, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.81, -1.87, -0.83, 1.14, 2.58]
- non-degenerate items: 1595; nothing passes: 218; everything passes: 2

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

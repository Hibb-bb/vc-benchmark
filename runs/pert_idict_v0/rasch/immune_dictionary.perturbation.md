# immune_dictionary.perturbation

- items: 963, respondents: 22, loglik: -5895.4, iters: 289, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-2.66, -1.26, -0.63, 0.24, 0.98]
- non-degenerate items: 757; nothing passes: 206; everything passes: 0

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

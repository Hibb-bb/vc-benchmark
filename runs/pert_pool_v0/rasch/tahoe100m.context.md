# tahoe100m.context

- items: 53972, respondents: 24, loglik: -253528.4, iters: 263, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-4.22, -1.63, -0.6, 1.53, 4.27]
- non-degenerate items: 53885; nothing passes: 87; everything passes: 0

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

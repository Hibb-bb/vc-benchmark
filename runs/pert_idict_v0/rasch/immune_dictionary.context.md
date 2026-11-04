# immune_dictionary.context

- items: 963, respondents: 22, loglik: -5410.2, iters: 245, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-4.09, -1.46, -0.02, 1.25, 3.51]
- non-degenerate items: 930; nothing passes: 33; everything passes: 0

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

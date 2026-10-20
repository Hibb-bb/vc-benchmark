# tahoe100m.perturbation

- items: 53972, respondents: 22, loglik: -377530.1, iters: 366, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.43, -1.96, -1.04, -0.12, 1.05]
- non-degenerate items: 39698; nothing passes: 14274; everything passes: 0

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

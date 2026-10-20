# parse_pbmc_cytokines.context

- items: 13967, respondents: 31, loglik: -128704.0, iters: 411, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.71, -2.07, -0.52, 1.97, 3.74]
- non-degenerate items: 13366; nothing passes: 601; everything passes: 0

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

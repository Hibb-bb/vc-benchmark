# parse_pbmc_cytokines.context

- items: 13967, respondents: 27, loglik: -110938.9, iters: 366, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.55, -2.06, -0.54, 2.06, 3.49]
- non-degenerate items: 13248; nothing passes: 719; everything passes: 0

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

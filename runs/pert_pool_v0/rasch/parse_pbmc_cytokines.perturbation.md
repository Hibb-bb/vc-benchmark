# parse_pbmc_cytokines.perturbation

- items: 13967, respondents: 27, loglik: -82253.2, iters: 307, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.24, -1.55, -0.3, 0.49, 0.49]
- non-degenerate items: 10600; nothing passes: 3367; everything passes: 0

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

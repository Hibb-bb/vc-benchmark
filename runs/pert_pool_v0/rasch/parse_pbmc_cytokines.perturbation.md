# parse_pbmc_cytokines.perturbation

- items: 13967, respondents: 29, loglik: -89073.1, iters: 326, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.39, -1.44, -0.23, 0.56, 0.56]
- non-degenerate items: 10744; nothing passes: 3223; everything passes: 0

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

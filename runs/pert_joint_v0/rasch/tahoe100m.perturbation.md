# tahoe100m.perturbation

- items: 53972, respondents: 49, loglik: -637048.0, iters: 500, converged: False
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-4.12, -1.97, -0.68, 0.15, 1.27]
- non-degenerate items: 40506; nothing passes: 13466; everything passes: 0

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k5 | -0.99 | 0.01 | 0.368 | 1.20 |
| knn_k1 | -1.24 | 0.01 | 0.335 | 1.17 |
| gp_d50_ls0.5 | -1.36 | 0.01 | 0.320 | 0.98 |
| knn_k20 | -1.37 | 0.01 | 0.318 | 1.05 |
| gp_d50_ls2 | -1.48 | 0.01 | 0.304 | 0.90 |
| mlp_h1024_d50 | -1.59 | 0.01 | 0.291 | 0.79 |
| ridge_d50_lam100_tf0.3 | -1.63 | 0.01 | 0.287 | 0.48 |
| ridge_d50_lam100 | -1.68 | 0.01 | 0.281 | 0.43 |
| ridge_d50_lam100_tf0.1 | -1.69 | 0.01 | 0.279 | 0.53 |
| ridge_d50_lam1 | -1.76 | 0.01 | 0.271 | 0.44 |
| mlp_h256_d50 | -1.77 | 0.01 | 0.270 | 0.84 |
| knn_k20_tf0.3 | -1.78 | 0.01 | 0.269 | 0.84 |
| ridge_d10_lam100 | -1.81 | 0.01 | 0.266 | 0.43 |
| ridge_d10_lam1 | -1.86 | 0.01 | 0.260 | 0.44 |
| knn_k20_tf0.1 | -1.96 | 0.01 | 0.248 | 0.87 |
| latent_pca_k256 | -2.70 | 0.01 | 0.175 | 0.34 |
| latent_pca_k128 | -2.79 | 0.01 | 0.166 | 0.33 |
| latent_ica_k64 | -3.07 | 0.02 | 0.143 | 0.27 |
| latent_pca_k64 | -3.07 | 0.02 | 0.143 | 0.27 |
| random_shift_s0 | -3.12 | 0.02 | 0.139 | 2.33 |
| random_shift_s1 | -3.13 | 0.02 | 0.139 | 2.40 |
| latent_nystroem_k256_g0.5 | -3.15 | 0.02 | 0.137 | 0.33 |
| latent_nystroem_k256_g2 | -3.16 | 0.02 | 0.136 | 0.43 |
| latent_nystroem_k64_g0.5 | -3.34 | 0.02 | 0.123 | 0.29 |
| latent_nmf_k64 | -3.37 | 0.02 | 0.121 | 0.35 |
| latent_nystroem_k64_g2 | -3.55 | 0.02 | 0.109 | 0.37 |
| latent_pca_k32 | -3.56 | 0.02 | 0.109 | 0.35 |
| lowrank_r2 | -3.58 | 0.02 | 0.108 | 2.65 |
| lowrank_r5 | -3.58 | 0.02 | 0.108 | 2.65 |
| lowrank_r10 | -3.58 | 0.02 | 0.108 | 2.65 |
| latent_gmm_k100 | -3.69 | 0.02 | 0.101 | 0.85 |
| latent_rproj_k128_s1 | -3.73 | 0.02 | 0.098 | 0.24 |
| latent_nmf_k16 | -3.74 | 0.02 | 0.098 | 0.31 |
| latent_rproj_k128_s0 | -3.74 | 0.02 | 0.098 | 0.23 |
| latent_pca_k16 | -3.80 | 0.02 | 0.094 | 0.36 |
| latent_ica_k16 | -3.80 | 0.02 | 0.094 | 0.36 |
| latent_depth2 | -4.17 | 0.02 | 0.075 | 1.79 |
| latent_pca_k8 | -4.23 | 0.02 | 0.072 | 0.46 |
| latent_rproj_k32_s1 | -4.28 | 0.02 | 0.070 | 0.41 |
| latent_pca_k4 | -4.33 | 0.02 | 0.068 | 0.43 |
| latent_rproj_k32_s0 | -4.41 | 0.02 | 0.064 | 0.37 |
| latent_gmm_k30 | -4.43 | 0.02 | 0.063 | 1.11 |
| latent_gmm_k10 | -4.51 | 0.02 | 0.060 | 0.48 |
| latent_rproj_k8_s0 | -4.63 | 0.02 | 0.055 | 0.66 |
| latent_rproj_k8_s1 | -4.70 | 0.02 | 0.053 | 0.66 |
| latent_random_k32_s0 | -4.87 | 0.02 | 0.047 | 1.21 |
| latent_random_k32_s1 | -4.92 | 0.02 | 0.045 | 1.29 |
| control_mean | -4.97 | 0.02 | 0.043 | 1.09 |
| target_kd | -12.88 | 0.81 | 0.000 | 0.00 |

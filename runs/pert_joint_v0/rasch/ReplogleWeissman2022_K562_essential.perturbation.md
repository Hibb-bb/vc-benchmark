# ReplogleWeissman2022_K562_essential.perturbation

- items: 1832, respondents: 53, loglik: -38141.0, iters: 500, converged: False
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-2.83, -1.82, -0.46, 1.4, 3.19]
- non-degenerate items: 1742; nothing passes: 89; everything passes: 1

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| ridge_d10_lam100 | 0.40 | 0.07 | 0.563 | 0.40 |
| pcareg_k5 | 0.40 | 0.07 | 0.563 | 0.51 |
| gp_d50_ls2 | 0.38 | 0.07 | 0.561 | 0.39 |
| ridge_d10_lam1 | 0.38 | 0.07 | 0.560 | 0.37 |
| pcareg_k10 | 0.37 | 0.07 | 0.559 | 0.37 |
| pcareg_k2 | 0.34 | 0.07 | 0.555 | 1.99 |
| pcareg_k20 | 0.26 | 0.07 | 0.545 | 0.35 |
| ridge_d50_lam100 | 0.22 | 0.06 | 0.540 | 0.36 |
| pcareg_k50 | 0.17 | 0.06 | 0.533 | 0.34 |
| ridge_d50_lam1 | 0.15 | 0.06 | 0.531 | 0.34 |
| pcareg_k100 | 0.06 | 0.06 | 0.519 | 0.34 |
| pcareg_k200 | -0.00 | 0.06 | 0.511 | 0.35 |
| gp_d50_ls0.5 | -0.08 | 0.06 | 0.501 | 0.88 |
| ridge_d50_lam100_tf0.3 | -0.42 | 0.06 | 0.455 | 1.11 |
| mlp_h1024_d50 | -0.47 | 0.06 | 0.449 | 0.73 |
| latent_nystroem_k256_g0.5 | -0.60 | 0.06 | 0.431 | 0.39 |
| latent_nystroem_k64_g0.5 | -0.62 | 0.06 | 0.428 | 0.43 |
| latent_pca_k32 | -0.67 | 0.06 | 0.421 | 0.38 |
| latent_pca_k64 | -0.70 | 0.06 | 0.418 | 0.38 |
| latent_nystroem_k256_g2 | -0.70 | 0.06 | 0.418 | 0.66 |
| latent_ica_k64 | -0.70 | 0.06 | 0.418 | 0.38 |
| latent_ica_k16 | -0.71 | 0.06 | 0.415 | 0.41 |
| latent_pca_k8 | -0.71 | 0.06 | 0.415 | 0.58 |
| latent_pca_k16 | -0.72 | 0.06 | 0.415 | 0.41 |
| latent_pca_k128 | -0.72 | 0.06 | 0.415 | 0.36 |
| mlp_h256_d50 | -0.74 | 0.06 | 0.412 | 1.04 |
| latent_pca_k256 | -0.75 | 0.06 | 0.410 | 0.37 |
| latent_nmf_k16 | -0.76 | 0.06 | 0.409 | 0.67 |
| latent_nystroem_k64_g2 | -0.77 | 0.06 | 0.407 | 0.95 |
| latent_gmm_k100 | -0.78 | 0.06 | 0.407 | 0.55 |
| knn_k20 | -0.85 | 0.06 | 0.396 | 1.43 |
| latent_gmm_k30 | -0.87 | 0.06 | 0.394 | 0.79 |
| knn_k20_tf0.3 | -0.95 | 0.06 | 0.383 | 1.66 |
| latent_rproj_k128_s1 | -0.95 | 0.06 | 0.383 | 0.67 |
| latent_rproj_k128_s0 | -1.03 | 0.06 | 0.372 | 0.63 |
| knn_k20_tf0.1 | -1.09 | 0.06 | 0.365 | 2.08 |
| ridge_d50_lam100_tf0.1 | -1.09 | 0.06 | 0.364 | 1.55 |
| latent_gmm_k10 | -1.25 | 0.06 | 0.343 | 2.24 |
| latent_nmf_k64 | -1.30 | 0.06 | 0.336 | 1.70 |
| latent_rproj_k32_s0 | -1.47 | 0.06 | 0.312 | 1.28 |
| latent_rproj_k32_s1 | -1.56 | 0.06 | 0.301 | 1.52 |
| latent_pca_k4 | -1.56 | 0.06 | 0.300 | 3.32 |
| knn_k5 | -1.62 | 0.06 | 0.293 | 1.79 |
| latent_rproj_k8_s1 | -1.96 | 0.07 | 0.248 | 2.98 |
| knn_k1 | -2.08 | 0.07 | 0.234 | 2.07 |
| latent_rproj_k8_s0 | -2.30 | 0.07 | 0.207 | 2.57 |
| random_shift_s1 | -2.60 | 0.07 | 0.175 | 3.86 |
| random_shift_s0 | -2.63 | 0.07 | 0.171 | 4.04 |
| target_kd | -2.79 | 0.07 | 0.155 | 9.50 |
| latent_depth2 | -2.83 | 0.07 | 0.151 | 5.48 |
| latent_random_k32_s0 | -3.11 | 0.08 | 0.125 | 2.01 |
| control_mean | -3.21 | 0.08 | 0.116 | 2.13 |
| latent_random_k32_s1 | -3.21 | 0.08 | 0.116 | 2.48 |

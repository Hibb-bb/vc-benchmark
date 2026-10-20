# ReplogleWeissman2022_K562_gwps.perturbation

- items: 9326, respondents: 53, loglik: -208874.0, iters: 500, converged: False
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.69, -1.44, -0.2, 1.0, 3.1]
- non-degenerate items: 8761; nothing passes: 557; everything passes: 8

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k5 | 0.08 | 0.03 | 0.517 | 0.97 |
| ridge_d10_lam100 | 0.07 | 0.03 | 0.516 | 0.77 |
| pcareg_k10 | 0.06 | 0.03 | 0.515 | 0.76 |
| ridge_d10_lam1 | 0.06 | 0.03 | 0.514 | 0.77 |
| ridge_d50_lam100 | 0.04 | 0.03 | 0.512 | 0.70 |
| pcareg_k20 | 0.04 | 0.03 | 0.511 | 0.74 |
| pcareg_k50 | 0.02 | 0.03 | 0.509 | 0.69 |
| ridge_d50_lam1 | 0.02 | 0.03 | 0.509 | 0.69 |
| pcareg_k100 | 0.02 | 0.03 | 0.508 | 0.68 |
| pcareg_k2 | 0.02 | 0.03 | 0.508 | 1.89 |
| pcareg_k200 | 0.00 | 0.03 | 0.505 | 0.66 |
| gp_d50_ls2 | -0.12 | 0.03 | 0.488 | 1.18 |
| ridge_d50_lam100_tf0.3 | -0.24 | 0.03 | 0.469 | 1.11 |
| gp_d50_ls0.5 | -0.36 | 0.03 | 0.452 | 1.18 |
| mlp_h256_d50 | -0.37 | 0.03 | 0.450 | 1.45 |
| mlp_h1024_d50 | -0.50 | 0.03 | 0.431 | 1.14 |
| ridge_d50_lam100_tf0.1 | -0.61 | 0.03 | 0.415 | 1.19 |
| latent_gmm_k10 | -0.93 | 0.03 | 0.370 | 1.26 |
| latent_gmm_k30 | -0.93 | 0.03 | 0.369 | 1.18 |
| latent_pca_k4 | -0.94 | 0.03 | 0.368 | 1.34 |
| latent_nystroem_k256_g2 | -0.95 | 0.03 | 0.367 | 0.60 |
| latent_nystroem_k64_g2 | -0.95 | 0.03 | 0.367 | 0.68 |
| latent_gmm_k100 | -0.96 | 0.03 | 0.365 | 1.07 |
| latent_nystroem_k64_g0.5 | -0.98 | 0.03 | 0.362 | 0.48 |
| knn_k20 | -1.00 | 0.03 | 0.360 | 0.86 |
| knn_k20_tf0.3 | -1.00 | 0.03 | 0.359 | 0.90 |
| latent_nystroem_k256_g0.5 | -1.00 | 0.03 | 0.359 | 0.46 |
| latent_nmf_k16 | -1.03 | 0.03 | 0.355 | 0.73 |
| latent_pca_k8 | -1.05 | 0.03 | 0.353 | 0.94 |
| latent_ica_k16 | -1.05 | 0.03 | 0.352 | 0.50 |
| latent_pca_k16 | -1.05 | 0.03 | 0.352 | 0.50 |
| latent_pca_k64 | -1.07 | 0.03 | 0.349 | 0.45 |
| latent_ica_k64 | -1.07 | 0.03 | 0.349 | 0.45 |
| latent_depth2 | -1.08 | 0.03 | 0.349 | 0.95 |
| latent_nmf_k64 | -1.08 | 0.03 | 0.348 | 1.40 |
| latent_pca_k32 | -1.08 | 0.03 | 0.348 | 0.47 |
| knn_k20_tf0.1 | -1.10 | 0.03 | 0.346 | 1.05 |
| latent_pca_k128 | -1.10 | 0.03 | 0.345 | 0.44 |
| knn_k5 | -1.10 | 0.03 | 0.345 | 0.81 |
| latent_pca_k256 | -1.17 | 0.03 | 0.336 | 0.42 |
| latent_rproj_k128_s1 | -1.18 | 0.03 | 0.335 | 0.91 |
| latent_rproj_k32_s0 | -1.18 | 0.03 | 0.335 | 1.17 |
| knn_k1 | -1.21 | 0.03 | 0.331 | 0.77 |
| latent_rproj_k128_s0 | -1.23 | 0.03 | 0.327 | 0.70 |
| latent_rproj_k32_s1 | -1.27 | 0.03 | 0.323 | 1.28 |
| latent_rproj_k8_s0 | -1.27 | 0.03 | 0.322 | 1.17 |
| random_shift_s0 | -1.29 | 0.03 | 0.320 | 0.91 |
| random_shift_s1 | -1.29 | 0.03 | 0.320 | 0.89 |
| latent_rproj_k8_s1 | -1.30 | 0.03 | 0.318 | 1.58 |
| latent_random_k32_s1 | -1.32 | 0.03 | 0.315 | 0.75 |
| latent_random_k32_s0 | -1.35 | 0.03 | 0.312 | 0.69 |
| control_mean | -1.40 | 0.03 | 0.305 | 0.59 |
| target_kd | -2.76 | 0.04 | 0.157 | 6.63 |

# NadigOConner2024_hepg2.perturbation

- items: 1061, respondents: 53, loglik: -22374.8, iters: 500, converged: False
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-2.77, -1.85, -0.18, 1.41, 2.97]
- non-degenerate items: 992; nothing passes: 66; everything passes: 3

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| gp_d50_ls2 | 0.25 | 0.08 | 0.532 | 0.60 |
| pcareg_k2 | 0.22 | 0.08 | 0.527 | 1.17 |
| pcareg_k5 | 0.04 | 0.08 | 0.502 | 0.59 |
| ridge_d10_lam100 | -0.00 | 0.08 | 0.497 | 0.45 |
| gp_d50_ls0.5 | -0.03 | 0.08 | 0.493 | 0.87 |
| pcareg_k10 | -0.12 | 0.08 | 0.481 | 0.41 |
| ridge_d10_lam1 | -0.14 | 0.08 | 0.478 | 0.41 |
| ridge_d50_lam100 | -0.20 | 0.08 | 0.470 | 0.37 |
| pcareg_k20 | -0.24 | 0.08 | 0.464 | 0.36 |
| pcareg_k50 | -0.41 | 0.08 | 0.440 | 0.35 |
| ridge_d50_lam1 | -0.43 | 0.08 | 0.438 | 0.35 |
| knn_k20 | -0.48 | 0.08 | 0.432 | 1.63 |
| pcareg_k100 | -0.49 | 0.08 | 0.430 | 0.34 |
| pcareg_k200 | -0.58 | 0.08 | 0.418 | 0.36 |
| mlp_h1024_d50 | -0.65 | 0.08 | 0.408 | 0.83 |
| latent_nystroem_k64_g2 | -0.68 | 0.08 | 0.403 | 0.89 |
| knn_k20_tf0.3 | -0.70 | 0.08 | 0.402 | 1.66 |
| latent_nystroem_k256_g2 | -0.80 | 0.08 | 0.387 | 0.61 |
| ridge_d50_lam100_tf0.3 | -0.82 | 0.08 | 0.385 | 1.27 |
| latent_nystroem_k64_g0.5 | -0.89 | 0.08 | 0.376 | 0.40 |
| mlp_h256_d50 | -0.90 | 0.08 | 0.374 | 0.81 |
| latent_pca_k8 | -0.91 | 0.08 | 0.372 | 0.65 |
| latent_nystroem_k256_g0.5 | -0.96 | 0.08 | 0.367 | 0.34 |
| latent_gmm_k100 | -0.96 | 0.08 | 0.366 | 0.55 |
| latent_gmm_k30 | -0.96 | 0.08 | 0.366 | 0.78 |
| knn_k20_tf0.1 | -0.97 | 0.08 | 0.365 | 2.19 |
| latent_gmm_k10 | -0.98 | 0.08 | 0.363 | 1.35 |
| latent_rproj_k128_s0 | -0.99 | 0.08 | 0.362 | 0.56 |
| latent_pca_k64 | -0.99 | 0.08 | 0.362 | 0.32 |
| latent_ica_k64 | -0.99 | 0.08 | 0.362 | 0.32 |
| latent_pca_k256 | -1.00 | 0.08 | 0.361 | 0.32 |
| latent_ica_k16 | -1.00 | 0.08 | 0.361 | 0.40 |
| latent_nmf_k16 | -1.00 | 0.08 | 0.361 | 0.85 |
| latent_pca_k16 | -1.00 | 0.08 | 0.360 | 0.40 |
| latent_pca_k128 | -1.00 | 0.08 | 0.360 | 0.33 |
| latent_rproj_k128_s1 | -1.04 | 0.08 | 0.355 | 0.61 |
| latent_pca_k32 | -1.04 | 0.08 | 0.355 | 0.35 |
| latent_rproj_k32_s0 | -1.10 | 0.08 | 0.348 | 1.26 |
| knn_k5 | -1.24 | 0.08 | 0.329 | 1.81 |
| latent_nmf_k64 | -1.25 | 0.08 | 0.328 | 1.59 |
| latent_pca_k4 | -1.25 | 0.08 | 0.327 | 1.42 |
| latent_rproj_k32_s1 | -1.33 | 0.09 | 0.318 | 1.54 |
| ridge_d50_lam100_tf0.1 | -1.43 | 0.09 | 0.304 | 1.96 |
| knn_k1 | -1.78 | 0.09 | 0.260 | 1.93 |
| latent_rproj_k8_s1 | -1.82 | 0.09 | 0.255 | 2.02 |
| latent_rproj_k8_s0 | -2.03 | 0.09 | 0.230 | 1.97 |
| random_shift_s0 | -2.29 | 0.09 | 0.201 | 2.73 |
| random_shift_s1 | -2.30 | 0.09 | 0.199 | 2.69 |
| latent_depth2 | -2.34 | 0.09 | 0.195 | 2.40 |
| latent_random_k32_s1 | -2.53 | 0.10 | 0.175 | 1.79 |
| latent_random_k32_s0 | -2.54 | 0.10 | 0.173 | 1.58 |
| control_mean | -2.58 | 0.10 | 0.170 | 1.52 |
| target_kd | -3.00 | 0.10 | 0.131 | 10.57 |

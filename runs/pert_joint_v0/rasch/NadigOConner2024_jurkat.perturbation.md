# NadigOConner2024_jurkat.perturbation

- items: 1815, respondents: 53, loglik: -38307.7, iters: 500, converged: False
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-3.0, -1.79, -0.43, 1.27, 3.05]
- non-degenerate items: 1701; nothing passes: 114; everything passes: 0

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k2 | 0.51 | 0.07 | 0.577 | 1.43 |
| gp_d50_ls2 | 0.22 | 0.06 | 0.538 | 0.43 |
| ridge_d10_lam100 | 0.17 | 0.06 | 0.532 | 0.51 |
| pcareg_k10 | 0.15 | 0.06 | 0.529 | 0.50 |
| ridge_d10_lam1 | 0.14 | 0.06 | 0.528 | 0.51 |
| pcareg_k5 | 0.10 | 0.06 | 0.522 | 0.72 |
| pcareg_k20 | 0.05 | 0.06 | 0.516 | 0.43 |
| ridge_d50_lam100 | 0.02 | 0.06 | 0.512 | 0.37 |
| gp_d50_ls0.5 | -0.01 | 0.06 | 0.509 | 0.96 |
| ridge_d50_lam1 | -0.05 | 0.06 | 0.502 | 0.38 |
| pcareg_k50 | -0.05 | 0.06 | 0.502 | 0.38 |
| pcareg_k100 | -0.15 | 0.06 | 0.489 | 0.37 |
| pcareg_k200 | -0.25 | 0.06 | 0.475 | 0.38 |
| latent_nystroem_k256_g2 | -0.63 | 0.06 | 0.423 | 0.62 |
| mlp_h1024_d50 | -0.64 | 0.06 | 0.421 | 0.73 |
| latent_nystroem_k256_g0.5 | -0.67 | 0.06 | 0.418 | 0.38 |
| latent_nystroem_k64_g0.5 | -0.69 | 0.06 | 0.415 | 0.41 |
| latent_nystroem_k64_g2 | -0.73 | 0.06 | 0.409 | 0.92 |
| latent_gmm_k100 | -0.79 | 0.06 | 0.401 | 0.59 |
| latent_ica_k64 | -0.79 | 0.06 | 0.401 | 0.36 |
| latent_pca_k64 | -0.79 | 0.06 | 0.401 | 0.36 |
| latent_pca_k128 | -0.82 | 0.06 | 0.397 | 0.35 |
| latent_pca_k32 | -0.84 | 0.06 | 0.393 | 0.38 |
| latent_pca_k16 | -0.86 | 0.06 | 0.392 | 0.41 |
| latent_ica_k16 | -0.86 | 0.06 | 0.392 | 0.41 |
| latent_gmm_k30 | -0.88 | 0.06 | 0.388 | 0.78 |
| latent_pca_k256 | -0.88 | 0.06 | 0.388 | 0.36 |
| mlp_h256_d50 | -0.90 | 0.06 | 0.385 | 1.01 |
| ridge_d50_lam100_tf0.3 | -0.91 | 0.06 | 0.384 | 1.07 |
| latent_nmf_k16 | -0.92 | 0.06 | 0.383 | 1.07 |
| latent_pca_k8 | -0.95 | 0.06 | 0.379 | 0.64 |
| knn_k20 | -0.96 | 0.06 | 0.378 | 1.38 |
| latent_gmm_k10 | -1.12 | 0.06 | 0.356 | 2.30 |
| knn_k20_tf0.3 | -1.12 | 0.06 | 0.355 | 1.43 |
| latent_nmf_k64 | -1.25 | 0.06 | 0.337 | 1.46 |
| latent_rproj_k128_s1 | -1.29 | 0.06 | 0.332 | 0.76 |
| knn_k20_tf0.1 | -1.34 | 0.06 | 0.325 | 1.96 |
| latent_rproj_k128_s0 | -1.36 | 0.06 | 0.322 | 0.61 |
| latent_pca_k4 | -1.37 | 0.06 | 0.322 | 2.49 |
| ridge_d50_lam100_tf0.1 | -1.53 | 0.06 | 0.300 | 1.56 |
| latent_rproj_k32_s0 | -1.58 | 0.06 | 0.293 | 1.58 |
| knn_k5 | -1.63 | 0.06 | 0.288 | 1.45 |
| latent_rproj_k32_s1 | -1.77 | 0.07 | 0.269 | 1.55 |
| latent_rproj_k8_s0 | -1.94 | 0.07 | 0.248 | 2.21 |
| latent_depth2 | -2.16 | 0.07 | 0.220 | 4.73 |
| latent_rproj_k8_s1 | -2.21 | 0.07 | 0.214 | 2.25 |
| knn_k1 | -2.22 | 0.07 | 0.213 | 1.77 |
| random_shift_s1 | -2.41 | 0.07 | 0.192 | 2.36 |
| random_shift_s0 | -2.44 | 0.07 | 0.188 | 2.62 |
| latent_random_k32_s1 | -2.85 | 0.08 | 0.147 | 1.81 |
| latent_random_k32_s0 | -2.86 | 0.08 | 0.146 | 2.09 |
| control_mean | -2.87 | 0.08 | 0.145 | 1.62 |
| target_kd | -2.97 | 0.08 | 0.136 | 9.75 |

# pooled_context

- items: 71897, respondents: 58, loglik: -877843.8, iters: 458, converged: True
- 5 datasets pooled on one scale, context scheme (respondent names shared across datasets)

- difficulty percentiles (5/25/50/75/95): [-5.69, -2.37, 0.24, 1.93, 5.27]
- non-degenerate items: 70541; nothing passes: 1354; everything passes: 2

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| pcareg_k200 | 5.81 | 0.03 | 0.795 | 60.72 |
| mlp_h256_d50 | 4.90 | 0.02 | 0.903 | 11.13 |
| mlp_h1024_d50 | 4.75 | 0.02 | 0.896 | 6.86 |
| pcareg_k100 | 4.48 | 0.02 | 0.670 | 22.84 |
| lowrank_r10 | 4.45 | 0.02 | 0.881 | 33.90 |
| lowrank_r5 | 3.59 | 0.01 | 0.832 | 20.34 |
| pcareg_k50 | 3.46 | 0.02 | 0.571 | 8.27 |
| ridge_d50_lam100 | 3.32 | 0.01 | 0.825 | 4.33 |
| ridge_d50_lam1 | 3.31 | 0.01 | 0.824 | 4.61 |
| ridge_d50_lam100_tf0.3 | 3.03 | 0.01 | 0.804 | 7.60 |
| knn_k20 | 3.02 | 0.01 | 0.803 | 36.44 |
| pcareg_k20 | 2.66 | 0.02 | 0.492 | 5.50 |
| lowrank_r2 | 2.46 | 0.01 | 0.744 | 16.82 |
| ridge_d50_lam100_tf0.1 | 2.46 | 0.01 | 0.756 | 8.02 |
| knn_k20_tf0.3 | 2.30 | 0.01 | 0.742 | 19.20 |
| gp_d50_ls0.5 | 2.21 | 0.01 | 0.733 | 4.66 |
| knn_k5 | 2.20 | 0.01 | 0.732 | 16.04 |
| pcareg_k10 | 2.15 | 0.02 | 0.442 | 4.38 |
| ridge_d10_lam100 | 1.77 | 0.01 | 0.690 | 1.58 |
| ridge_d10_lam1 | 1.77 | 0.01 | 0.690 | 1.61 |
| gp_d50_ls2 | 1.67 | 0.01 | 0.680 | 3.48 |
| knn_k20_tf0.1 | 1.16 | 0.01 | 0.626 | 4.20 |
| pcareg_k5 | 1.14 | 0.03 | 0.348 | 4.29 |
| latent_pca_k256 | 0.87 | 0.01 | 0.584 | 0.34 |
| knn_k1 | 0.83 | 0.01 | 0.590 | 9.23 |
| latent_pca_k128 | 0.63 | 0.01 | 0.558 | 0.33 |
| scvi_cf | 0.29 | 0.01 | 0.520 | 2.00 |
| latent_ica_k64 | -0.02 | 0.01 | 0.488 | 0.31 |
| latent_pca_k64 | -0.02 | 0.01 | 0.488 | 0.31 |
| pcareg_k2 | -0.08 | 0.03 | 0.258 | 5.51 |
| scgen | -0.12 | 0.01 | 0.477 | 4.00 |
| latent_nystroem_k256_g0.5 | -0.57 | 0.01 | 0.430 | 0.29 |
| latent_nystroem_k256_g2 | -0.81 | 0.01 | 0.406 | 0.29 |
| latent_nystroem_k64_g0.5 | -0.91 | 0.01 | 0.396 | 0.29 |
| latent_nmf_k64 | -0.94 | 0.01 | 0.393 | 0.50 |
| latent_rproj_k128_s0 | -1.27 | 0.01 | 0.362 | 0.38 |
| latent_rproj_k128_s1 | -1.35 | 0.01 | 0.354 | 0.37 |
| latent_nystroem_k64_g2 | -1.59 | 0.01 | 0.332 | 0.33 |
| latent_pca_k32 | -2.09 | 0.01 | 0.288 | 0.41 |
| latent_nmf_k16 | -2.38 | 0.01 | 0.264 | 0.58 |
| latent_ica_k16 | -2.86 | 0.01 | 0.226 | 0.57 |
| latent_pca_k16 | -2.86 | 0.01 | 0.226 | 0.57 |
| latent_rproj_k32_s0 | -3.02 | 0.01 | 0.215 | 0.80 |
| latent_rproj_k32_s1 | -3.13 | 0.01 | 0.207 | 0.63 |
| latent_gmm_k100 | -3.14 | 0.01 | 0.206 | 0.94 |
| latent_pca_k8 | -3.75 | 0.01 | 0.166 | 1.87 |
| latent_pca_k4 | -4.05 | 0.02 | 0.147 | 5.52 |
| latent_depth2 | -4.35 | 0.02 | 0.130 | 8.34 |
| latent_gmm_k10 | -4.35 | 0.02 | 0.130 | 2.69 |
| random_shift_s0 | -4.37 | 0.02 | 0.129 | 9.25 |
| latent_rproj_k8_s0 | -4.42 | 0.02 | 0.126 | 1.83 |
| random_shift_s1 | -4.43 | 0.02 | 0.126 | 9.75 |
| latent_gmm_k30 | -4.58 | 0.02 | 0.118 | 3.94 |
| latent_rproj_k8_s1 | -4.73 | 0.02 | 0.110 | 2.93 |
| latent_random_k32_s1 | -6.34 | 0.02 | 0.050 | 4.97 |
| latent_random_k32_s0 | -6.35 | 0.02 | 0.050 | 3.72 |
| control_mean | -6.47 | 0.02 | 0.046 | 1.67 |
| target_kd | -11.59 | 0.13 | 0.001 | 15410.99 |

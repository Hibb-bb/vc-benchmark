# tahoe100m.context

- items: 53972, respondents: 51, loglik: -570285.5, iters: 330, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-5.69, -2.25, 0.36, 2.37, 4.97]
- non-degenerate items: 53885; nothing passes: 87; everything passes: 0

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| mlp_h1024_d50 | 8.82 | 0.06 | 0.994 | 0.23 |
| lowrank_r10 | 8.57 | 0.06 | 0.992 | 1.59 |
| mlp_h256_d50 | 8.21 | 0.05 | 0.990 | 3.43 |
| lowrank_r5 | 6.78 | 0.03 | 0.972 | 24.07 |
| knn_k20 | 5.18 | 0.02 | 0.924 | 0.58 |
| ridge_d50_lam100 | 4.58 | 0.02 | 0.895 | 14.31 |
| ridge_d50_lam1 | 4.57 | 0.02 | 0.894 | 15.85 |
| lowrank_r2 | 4.35 | 0.02 | 0.881 | 24.15 |
| ridge_d50_lam100_tf0.3 | 4.32 | 0.02 | 0.880 | 28.74 |
| knn_k5 | 4.23 | 0.02 | 0.874 | 17.41 |
| knn_k20_tf0.3 | 3.78 | 0.02 | 0.844 | 0.83 |
| ridge_d50_lam100_tf0.1 | 3.75 | 0.02 | 0.842 | 24.57 |
| gp_d50_ls0.5 | 3.10 | 0.01 | 0.790 | 10.47 |
| ridge_d10_lam1 | 2.78 | 0.01 | 0.762 | 3.38 |
| ridge_d10_lam100 | 2.78 | 0.01 | 0.762 | 3.19 |
| gp_d50_ls2 | 2.37 | 0.01 | 0.723 | 6.50 |
| knn_k1 | 2.28 | 0.01 | 0.714 | 22.85 |
| latent_pca_k256 | 2.00 | 0.01 | 0.685 | 0.34 |
| knn_k20_tf0.1 | 1.73 | 0.01 | 0.657 | 5.80 |
| latent_pca_k128 | 1.72 | 0.01 | 0.657 | 0.35 |
| scvi_cf | 1.19 | 0.01 | 0.600 | 3.16 |
| latent_pca_k64 | 0.92 | 0.01 | 0.572 | 0.34 |
| latent_ica_k64 | 0.92 | 0.01 | 0.572 | 0.34 |
| scgen | 0.52 | 0.01 | 0.530 | 6.75 |
| latent_nystroem_k256_g0.5 | 0.20 | 0.01 | 0.497 | 0.30 |
| latent_nystroem_k256_g2 | -0.10 | 0.01 | 0.467 | 0.29 |
| latent_nystroem_k64_g0.5 | -0.22 | 0.01 | 0.455 | 0.28 |
| latent_nmf_k64 | -0.33 | 0.01 | 0.444 | 0.42 |
| latent_rproj_k128_s0 | -0.65 | 0.01 | 0.414 | 0.35 |
| latent_rproj_k128_s1 | -0.76 | 0.01 | 0.404 | 0.36 |
| latent_nystroem_k64_g2 | -1.06 | 0.01 | 0.375 | 0.32 |
| latent_pca_k32 | -1.77 | 0.01 | 0.314 | 0.32 |
| latent_nmf_k16 | -2.10 | 0.02 | 0.286 | 0.30 |
| latent_rproj_k32_s0 | -2.70 | 0.02 | 0.240 | 0.39 |
| latent_ica_k16 | -2.71 | 0.02 | 0.239 | 0.27 |
| latent_pca_k16 | -2.71 | 0.02 | 0.239 | 0.27 |
| latent_rproj_k32_s1 | -2.83 | 0.02 | 0.230 | 0.38 |
| latent_gmm_k100 | -3.07 | 0.02 | 0.213 | 0.36 |
| latent_pca_k8 | -3.71 | 0.02 | 0.171 | 0.23 |
| latent_pca_k4 | -3.78 | 0.02 | 0.167 | 0.26 |
| random_shift_s0 | -4.16 | 0.02 | 0.145 | 6.50 |
| latent_gmm_k10 | -4.21 | 0.02 | 0.142 | 0.26 |
| random_shift_s1 | -4.23 | 0.02 | 0.141 | 7.27 |
| latent_depth2 | -4.28 | 0.02 | 0.138 | 1.02 |
| latent_rproj_k8_s0 | -4.32 | 0.02 | 0.136 | 0.36 |
| latent_rproj_k8_s1 | -4.72 | 0.02 | 0.116 | 0.44 |
| latent_gmm_k30 | -4.92 | 0.02 | 0.106 | 0.21 |
| latent_random_k32_s1 | -6.67 | 0.03 | 0.046 | 0.16 |
| latent_random_k32_s0 | -6.67 | 0.03 | 0.046 | 0.14 |
| control_mean | -6.78 | 0.03 | 0.043 | 0.10 |
| target_kd | -15.12 | 0.75 | 0.000 | 0.00 |

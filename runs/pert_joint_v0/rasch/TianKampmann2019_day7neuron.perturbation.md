# TianKampmann2019_day7neuron.perturbation

- items: 35, respondents: 53, loglik: -427.0, iters: 216, converged: True
- rule: pass if pearson_delta@hvg > mean_shift + 0.0

- difficulty percentiles (5/25/50/75/95): [-1.08, 0.94, 1.84, 3.13, 4.05]
- non-degenerate items: 30; nothing passes: 5; everything passes: 0

| respondent | ability | se | p_correct | outfit |
|---|---|---|---|---|
| knn_k20 | 2.70 | 0.44 | 0.571 | 1.30 |
| pcareg_k2 | 2.51 | 0.44 | 0.543 | 0.43 |
| gp_d50_ls2 | 2.13 | 0.43 | 0.486 | 0.80 |
| ridge_d10_lam100 | 1.94 | 0.43 | 0.457 | 0.50 |
| pcareg_k5 | 1.75 | 0.44 | 0.429 | 0.54 |
| pcareg_k10 | 0.96 | 0.46 | 0.314 | 0.46 |
| latent_depth2 | 0.96 | 0.46 | 0.314 | 2.10 |
| ridge_d50_lam100 | 0.75 | 0.47 | 0.286 | 0.49 |
| latent_pca_k8 | 0.52 | 0.48 | 0.257 | 0.58 |
| ridge_d10_lam1 | 0.52 | 0.48 | 0.257 | 0.49 |
| ridge_d50_lam100_tf0.3 | 0.52 | 0.48 | 0.257 | 1.33 |
| latent_nystroem_k64_g0.5 | 0.52 | 0.48 | 0.257 | 0.34 |
| latent_pca_k4 | 0.28 | 0.50 | 0.229 | 0.62 |
| knn_k20_tf0.3 | 0.28 | 0.50 | 0.229 | 2.80 |
| pcareg_k20 | 0.28 | 0.50 | 0.229 | 0.47 |
| latent_nystroem_k256_g0.5 | 0.28 | 0.50 | 0.229 | 0.31 |
| latent_gmm_k30 | 0.02 | 0.52 | 0.200 | 0.25 |
| latent_gmm_k10 | -0.26 | 0.55 | 0.171 | 0.35 |
| latent_nystroem_k256_g2 | -0.26 | 0.55 | 0.171 | 0.29 |
| ridge_d50_lam100_tf0.1 | -0.26 | 0.55 | 0.171 | 1.89 |
| pcareg_k50 | -0.26 | 0.55 | 0.171 | 0.25 |
| pcareg_k100 | -0.26 | 0.55 | 0.171 | 0.25 |
| pcareg_k200 | -0.26 | 0.55 | 0.171 | 0.25 |
| latent_pca_k16 | -0.26 | 0.55 | 0.171 | 0.43 |
| latent_ica_k16 | -0.26 | 0.55 | 0.171 | 0.43 |
| latent_nmf_k16 | -0.58 | 0.58 | 0.143 | 0.44 |
| gp_d50_ls0.5 | -0.58 | 0.58 | 0.143 | 0.37 |
| ridge_d50_lam1 | -0.58 | 0.58 | 0.143 | 0.29 |
| random_shift_s0 | -0.94 | 0.62 | 0.114 | 3.05 |
| knn_k5 | -0.94 | 0.62 | 0.114 | 0.66 |
| latent_nmf_k64 | -0.94 | 0.62 | 0.114 | 0.41 |
| latent_nystroem_k64_g2 | -1.36 | 0.68 | 0.086 | 0.44 |
| latent_pca_k32 | -1.36 | 0.68 | 0.086 | 0.33 |
| knn_k20_tf0.1 | -1.36 | 0.68 | 0.086 | 2.41 |
| latent_gmm_k100 | -1.36 | 0.68 | 0.086 | 0.38 |
| mlp_h1024_d50 | -1.89 | 0.77 | 0.057 | 12.10 |
| latent_pca_k128 | -1.89 | 0.77 | 0.057 | 0.11 |
| latent_rproj_k128_s1 | -1.89 | 0.77 | 0.057 | 0.16 |
| latent_rproj_k32_s0 | -1.89 | 0.77 | 0.057 | 0.18 |
| latent_rproj_k8_s1 | -1.89 | 0.77 | 0.057 | 0.76 |
| latent_ica_k64 | -2.60 | 0.94 | 0.029 | 0.07 |
| latent_pca_k256 | -2.60 | 0.94 | 0.029 | 0.07 |
| latent_pca_k64 | -2.60 | 0.94 | 0.029 | 0.07 |
| latent_rproj_k128_s0 | -2.60 | 0.94 | 0.029 | 0.07 |
| latent_rproj_k32_s1 | -2.60 | 0.94 | 0.029 | 0.63 |
| random_shift_s1 | -2.60 | 0.94 | 0.029 | 0.07 |
| latent_rproj_k8_s0 | -2.60 | 0.94 | 0.029 | 0.27 |
| mlp_h256_d50 | -2.60 | 0.94 | 0.029 | 0.14 |
| knn_k1 | -3.87 | 1.41 | 0.000 | 0.01 |
| control_mean | -3.87 | 1.41 | 0.000 | 0.01 |
| latent_random_k32_s1 | -3.87 | 1.41 | 0.000 | 0.01 |
| latent_random_k32_s0 | -3.87 | 1.41 | 0.000 | 0.01 |
| target_kd | -3.87 | 1.41 | 0.000 | 0.01 |

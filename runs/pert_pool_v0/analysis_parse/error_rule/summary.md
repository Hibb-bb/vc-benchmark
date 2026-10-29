# Parse error analysis under the absolute rule (pass if error <= 1.5 x noise)

Scale fitted on 31 respondents (20 more placed with difficulties held fixed). 13967 items; passed by nobody 20%, by everyone 6%.

## What predicts passing

| descriptor | Spearman r with share of models passing | (published rule) |
|---|---|---|
| within-item reliability | -0.91 | +0.58 |
| signal-to-noise | -0.91 | +0.56 |
| response size | +0.06 | +0.01 |
| donor agreement | -0.56 | +0.72 |
| cells per item | -0.72 | +0.39 |
| receptor expression | -0.16 | +0.23 |
| interferon-gene share | -0.43 | +0.28 |
| error of 'no change' (× noise) | -0.91 | +0.56 |

## By family

| family | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| common gamma chain / IL-4 | 1072 | 23% | 58% | 50% |
| type II interferon | 156 | 29% | 63% | 42% |
| type I interferon | 613 | 36% | 61% | 34% |
| other | 468 | 37% | 53% | 39% |
| IL-1 family | 1091 | 46% | 38% | 25% |
| IL-3 / common beta | 467 | 52% | 35% | 24% |
| complement | 154 | 54% | 42% | 24% |
| IL-12 family | 626 | 58% | 33% | 19% |
| IL-10 family | 931 | 60% | 36% | 18% |
| IL-6 / gp130 | 939 | 62% | 40% | 16% |
| TGF-beta family | 311 | 63% | 47% | 12% |
| hematopoietin | 1243 | 64% | 38% | 14% |
| type III interferon | 466 | 65% | 39% | 14% |
| TNF superfamily | 2642 | 65% | 42% | 14% |
| adipokine | 312 | 65% | 33% | 13% |
| IL-17 family | 927 | 66% | 35% | 12% |
| matrix / other | 311 | 69% | 35% | 12% |
| growth factor | 1083 | 70% | 37% | 11% |
| chemokine | 155 | 72% | 22% | 12% |

## By lineage

| lineage | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| monocyte | 2041 | 29% | 48% | 52% |
| CD4 T | 3107 | 42% | 47% | 32% |
| CD8 T | 2148 | 60% | 46% | 9% |
| B | 2158 | 63% | 40% | 11% |
| dendritic | 791 | 65% | 37% | 16% |
| NK | 2041 | 74% | 33% | 7% |
| innate-like T | 1678 | 82% | 29% | 2% |
| progenitor | 3 | 98% | 77% | 0% |

## By donor

| donor | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| Donor1 | 1259 | 37% | 53% | 33% |
| Donor7 | 933 | 51% | 44% | 19% |
| Donor6 | 1253 | 51% | 47% | 23% |
| Donor5 | 1232 | 54% | 38% | 24% |
| Donor12 | 1235 | 54% | 47% | 26% |
| Donor4 | 983 | 55% | 38% | 19% |
| Donor3 | 1218 | 58% | 26% | 18% |
| Donor8 | 1166 | 62% | 46% | 16% |
| Donor2 | 1234 | 62% | 40% | 18% |
| Donor11 | 1133 | 64% | 39% | 16% |
| Donor10 | 1156 | 65% | 39% | 15% |
| Donor9 | 1165 | 68% | 38% | 14% |

## By within-item reliability

| reliability | items | share passing (new) | (published) | passed by nobody | 'no change' passes | median cells |
|---|---|---|---|---|---|---|
| below 0.1 | 898 | 97% | 7% | 0% | 100% | 90 |
| 0.1-0.3 | 3452 | 92% | 22% | 0% | 99% | 183 |
| 0.3-0.5 | 3214 | 78% | 42% | 0% | 81% | 338 |
| 0.5-0.7 | 2528 | 45% | 52% | 8% | 13% | 532 |
| 0.7 and up | 3875 | 6% | 59% | 67% | 0% | 962 |

## Model abilities

| model | ability (new rule) | pass rate | ability (published rule) |
|---|---|---|---|
| mlp_h256_d50 | +4.22 | 76% | +1.69 |
| mlp_h1024_d50 | +3.81 | 74% | +1.30 |
| lowrank_r10 | +2.95 | 69% | +0.66 |
| pcareg_k200 | +2.32 | 66% | +3.80 |
| pcareg_k100 | +2.11 | 65% | +1.90 |
| ridge_d50_lam100 | +1.92 | 65% | +0.63 |
| ridge_d50_lam1 | +1.90 | 64% | +0.62 |
| pcareg_k50 | +1.90 | 64% | +0.62 |
| gp_d50_ls2 | +1.83 | 64% | +0.17 |
| lowrank_r5 | +1.78 | 64% | -0.91 |
| gp_d50_ls0.5 | +1.76 | 64% | +0.13 |
| ridge_d50_lam100_tf0.3 | +1.66 | 63% | +0.22 |
| pcareg_k20 | +1.57 | 63% | -0.27 |
| mlp_h256_d50_gesm2 | +1.57 | 63% | -0.07 |
| mlp_h256_d50_gscgpt | +1.52 | 63% | -0.15 |
| knn_k20_tf0.1 | +1.40 | 62% | +0.10 |
| ridge_d10_lam100 | +1.33 | 62% | -0.74 |
| pcareg_k10 | +1.32 | 62% | -0.74 |
| ridge_d10_lam1 | +1.32 | 62% | -0.74 |
| mlp_h256_d50_gscfoundation | +1.31 | 62% | -0.29 |
| mlp_h256_d50_gctrlpca | +1.15 | 61% | -0.45 |
| mlp_h256_d50_ggeneformer | +1.15 | 61% | -0.48 |
| pcareg_k5 | +0.87 | 59% | -1.66 |
| ridge_d50_lam100_tf0.1 | +0.84 | 59% | -0.54 |
| pcareg_k2 | +0.59 | 58% | -2.62 |
| lowrank_r2 | +0.54 | 58% | -1.70 |
| target_kd | +0.48 | 57% | -11.85 |
| gp_d50_ls1_gscfoundation | +0.46 | 57% | -1.53 |
| ridge_d50_lam100_gscfoundation | +0.45 | 57% | -1.52 |
| gp_d50_ls1_gscgpt | +0.43 | 57% | -1.59 |
| gp_d50_ls1_ggeneformer | +0.42 | 57% | -1.52 |
| gp_d50_ls1_gctrlpca | +0.40 | 57% | -1.61 |
| ridge_d50_lam100_gscgpt | +0.38 | 57% | -1.66 |
| knn_k20_tf0.3 | +0.36 | 57% | -1.22 |
| gp_d50_ls1_gesm2 | +0.35 | 57% | -1.61 |
| ridge_d50_lam100_ggeneformer | +0.34 | 57% | -1.56 |
| knn_k20 | +0.32 | 57% | -1.33 |
| ridge_d50_lam100_gctrlpca | +0.25 | 56% | -1.71 |
| ridge_d50_lam100_gesm2 | +0.24 | 56% | -1.70 |
| knn_k20_ggeneformer | +0.19 | 56% | -1.12 |
| knn_k20_gesm2 | +0.12 | 55% | -1.52 |
| knn_k20_gctrlpca | +0.12 | 55% | -1.53 |
| knn_k20_gscfoundation | +0.11 | 55% | -1.57 |
| knn_k20_gscgpt | -0.23 | 53% | -2.16 |
| control_mean | -0.42 | 52% | -5.07 |
| scvi_cf | -0.54 | 51% | -1.98 |
| knn_k5 | -1.15 | 47% | -2.67 |
| scgen | -1.59 | 44% | -1.83 |
| knn_k1 | -4.57 | 18% | -3.55 |
| random_shift_s0 | -4.73 | 17% | -4.50 |
| random_shift_s1 | -4.77 | 16% | -4.47 |

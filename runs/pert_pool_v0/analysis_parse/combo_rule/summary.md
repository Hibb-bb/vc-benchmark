# Parse error analysis under the absolute rule (signal-to-noise >= 1.5: pass if R² >= 0.5 x the achievable R²; weaker items: pass if error <= 1.5 x noise)

Scale fitted on 31 respondents (20 more placed with difficulties held fixed). 13967 items; passed by nobody 6%, by everyone 6%.

## What predicts passing

| descriptor | Spearman r with share of models passing | (published rule) |
|---|---|---|
| within-item reliability | -0.81 | +0.58 |
| signal-to-noise | -0.81 | +0.56 |
| response size | +0.15 | +0.01 |
| donor agreement | -0.49 | +0.72 |
| cells per item | -0.65 | +0.39 |
| receptor expression | -0.14 | +0.23 |
| interferon-gene share | -0.36 | +0.28 |
| error of 'no change' (× noise) | -0.81 | +0.56 |

## By family

| family | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| common gamma chain / IL-4 | 1072 | 39% | 58% | 9% |
| other | 468 | 43% | 53% | 9% |
| type II interferon | 156 | 46% | 63% | 8% |
| type I interferon | 613 | 52% | 61% | 2% |
| complement | 154 | 53% | 42% | 18% |
| IL-1 family | 1091 | 54% | 38% | 5% |
| IL-3 / common beta | 467 | 55% | 35% | 7% |
| IL-12 family | 626 | 64% | 33% | 5% |
| IL-6 / gp130 | 939 | 65% | 40% | 4% |
| hematopoietin | 1243 | 65% | 38% | 7% |
| IL-10 family | 931 | 66% | 36% | 6% |
| type III interferon | 466 | 67% | 39% | 5% |
| TNF superfamily | 2642 | 68% | 42% | 6% |
| IL-17 family | 927 | 68% | 35% | 6% |
| TGF-beta family | 311 | 68% | 47% | 3% |
| adipokine | 312 | 70% | 33% | 4% |
| growth factor | 1083 | 70% | 37% | 6% |
| matrix / other | 311 | 70% | 35% | 6% |
| chemokine | 155 | 74% | 22% | 10% |

## By lineage

| lineage | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| monocyte | 2041 | 35% | 48% | 20% |
| CD4 T | 3107 | 53% | 47% | 7% |
| CD8 T | 2148 | 64% | 46% | 2% |
| B | 2158 | 65% | 40% | 3% |
| dendritic | 791 | 66% | 37% | 7% |
| NK | 2041 | 76% | 33% | 2% |
| innate-like T | 1678 | 82% | 29% | 1% |
| progenitor | 3 | 98% | 77% | 0% |

## By donor

| donor | items | share passing (new) | (published) | passed by nobody |
|---|---|---|---|---|
| Donor1 | 1259 | 48% | 53% | 8% |
| Donor7 | 933 | 54% | 44% | 8% |
| Donor4 | 983 | 57% | 38% | 6% |
| Donor12 | 1235 | 58% | 47% | 9% |
| Donor3 | 1218 | 59% | 26% | 6% |
| Donor6 | 1253 | 61% | 47% | 5% |
| Donor2 | 1234 | 65% | 40% | 9% |
| Donor11 | 1133 | 67% | 39% | 5% |
| Donor5 | 1232 | 67% | 38% | 5% |
| Donor8 | 1166 | 67% | 46% | 5% |
| Donor10 | 1156 | 68% | 39% | 3% |
| Donor9 | 1165 | 70% | 38% | 6% |

## By within-item reliability

| reliability | items | share passing (new) | (published) | passed by nobody | 'no change' passes | median cells |
|---|---|---|---|---|---|---|
| below 0.1 | 898 | 97% | 7% | 0% | 100% | 90 |
| 0.1-0.3 | 3452 | 92% | 22% | 0% | 99% | 183 |
| 0.3-0.5 | 3214 | 76% | 42% | 1% | 81% | 338 |
| 0.5-0.7 | 2528 | 37% | 52% | 15% | 13% | 532 |
| 0.7 and up | 3875 | 31% | 59% | 12% | 0% | 962 |

## Model abilities

| model | ability (new rule) | pass rate | ability (published rule) |
|---|---|---|---|
| mlp_h256_d50 | +5.58 | 89% | +1.69 |
| mlp_h1024_d50 | +5.17 | 87% | +1.30 |
| lowrank_r10 | +3.76 | 79% | +0.66 |
| pcareg_k200 | +3.22 | 76% | +3.80 |
| pcareg_k100 | +3.00 | 74% | +1.90 |
| ridge_d50_lam100 | +2.78 | 73% | +0.63 |
| ridge_d50_lam1 | +2.77 | 73% | +0.62 |
| pcareg_k50 | +2.77 | 73% | +0.62 |
| mlp_h256_d50_gscgpt | +2.63 | 72% | -0.15 |
| mlp_h256_d50_gesm2 | +2.62 | 72% | -0.07 |
| lowrank_r5 | +2.56 | 71% | -0.91 |
| ridge_d50_lam100_tf0.3 | +2.45 | 71% | +0.22 |
| gp_d50_ls0.5 | +2.39 | 70% | +0.13 |
| mlp_h256_d50_gscfoundation | +2.39 | 70% | -0.29 |
| pcareg_k20 | +2.37 | 70% | -0.27 |
| mlp_h256_d50_gctrlpca | +2.20 | 69% | -0.45 |
| mlp_h256_d50_ggeneformer | +2.20 | 69% | -0.48 |
| gp_d50_ls2 | +2.18 | 69% | +0.17 |
| pcareg_k10 | +1.96 | 67% | -0.74 |
| ridge_d10_lam1 | +1.96 | 67% | -0.74 |
| ridge_d10_lam100 | +1.96 | 67% | -0.74 |
| ridge_d50_lam100_tf0.1 | +1.59 | 65% | -0.54 |
| lowrank_r2 | +1.48 | 64% | -1.70 |
| knn_k20_tf0.1 | +1.41 | 64% | +0.10 |
| pcareg_k5 | +1.40 | 64% | -1.66 |
| pcareg_k2 | +0.98 | 61% | -2.62 |
| ridge_d50_lam100_gscfoundation | +0.85 | 60% | -1.52 |
| gp_d50_ls1_gscfoundation | +0.82 | 59% | -1.53 |
| ridge_d50_lam100_gscgpt | +0.78 | 59% | -1.66 |
| gp_d50_ls1_gscgpt | +0.77 | 59% | -1.59 |
| gp_d50_ls1_ggeneformer | +0.76 | 59% | -1.52 |
| ridge_d50_lam100_ggeneformer | +0.75 | 59% | -1.56 |
| gp_d50_ls1_gctrlpca | +0.74 | 59% | -1.61 |
| gp_d50_ls1_gesm2 | +0.71 | 59% | -1.61 |
| ridge_d50_lam100_gctrlpca | +0.70 | 59% | -1.71 |
| ridge_d50_lam100_gesm2 | +0.66 | 58% | -1.70 |
| target_kd | +0.60 | 58% | -11.85 |
| knn_k20 | +0.52 | 57% | -1.33 |
| knn_k20_tf0.3 | +0.52 | 57% | -1.22 |
| knn_k20_ggeneformer | +0.51 | 57% | -1.12 |
| knn_k20_gctrlpca | +0.46 | 57% | -1.53 |
| knn_k20_gesm2 | +0.45 | 57% | -1.52 |
| knn_k20_gscfoundation | +0.42 | 56% | -1.57 |
| knn_k20_gscgpt | +0.21 | 55% | -2.16 |
| control_mean | -0.13 | 52% | -5.07 |
| scvi_cf | -0.33 | 50% | -1.98 |
| knn_k5 | -0.64 | 48% | -2.67 |
| scgen | -0.79 | 47% | -1.83 |
| knn_k1 | -3.91 | 19% | -3.55 |
| random_shift_s0 | -4.24 | 16% | -4.50 |
| random_shift_s1 | -4.28 | 16% | -4.47 |

## Weak and null responses (signal-to-noise below 1.5, 7276 items)

A correct answer here is a small change. 'Error ratio' is the median distance from the measured change in units of noise (about 1.0 for a perfect model); a model that invents a response where there is none lands well above it.

| model | passes (error <= k x noise) | median error ratio |
|---|---|---|
| control_mean | 100% | 1.20 |
| mlp_h256_d50 | 99% | 1.09 |
| mlp_h1024_d50 | 99% | 1.11 |
| knn_k20_tf0.1 | 98% | 1.12 |
| gp_d50_ls2 | 98% | 1.12 |
| lowrank_r10 | 97% | 1.11 |
| pcareg_k200 | 96% | 1.08 |
| pcareg_k100 | 96% | 1.11 |
| gp_d50_ls0.5 | 96% | 1.13 |
| ridge_d50_lam100 | 96% | 1.12 |
| scvi_cf | 96% | 1.22 |
| lowrank_r5 | 96% | 1.14 |
| pcareg_k50 | 96% | 1.12 |
| ridge_d50_lam1 | 96% | 1.12 |
| ridge_d10_lam100 | 96% | 1.14 |
| pcareg_k20 | 96% | 1.14 |
| pcareg_k10 | 96% | 1.14 |
| ridge_d10_lam1 | 95% | 1.14 |
| pcareg_k5 | 95% | 1.16 |
| pcareg_k2 | 95% | 1.17 |
| ridge_d50_lam100_tf0.3 | 95% | 1.13 |
| lowrank_r2 | 94% | 1.17 |
| target_kd | 94% | 1.14 |
| mean_shift | 94% | 1.14 |
| mlp_h256_d50_gesm2 | 94% | 1.15 |
| mlp_h256_d50_gscgpt | 94% | 1.15 |
| mlp_h256_d50_gscfoundation | 93% | 1.16 |
| gp_d50_ls1_gscfoundation | 93% | 1.17 |
| mlp_h256_d50_ggeneformer | 93% | 1.16 |
| gp_d50_ls1_gscgpt | 93% | 1.17 |
| gp_d50_ls1_gesm2 | 93% | 1.17 |
| ridge_d50_lam100_gscfoundation | 93% | 1.17 |
| gp_d50_ls1_ggeneformer | 92% | 1.17 |
| gp_d50_ls1_gctrlpca | 92% | 1.17 |
| knn_k20 | 92% | 1.15 |
| knn_k20_tf0.3 | 92% | 1.15 |
| ridge_d50_lam100_gscgpt | 92% | 1.17 |
| mlp_h256_d50_gctrlpca | 92% | 1.17 |
| ridge_d50_lam100_ggeneformer | 92% | 1.18 |
| ridge_d50_lam100_gesm2 | 92% | 1.18 |
| ridge_d50_lam100_gctrlpca | 91% | 1.18 |
| ridge_d50_lam100_tf0.1 | 91% | 1.16 |
| knn_k20_ggeneformer | 91% | 1.15 |
| knn_k20_gctrlpca | 91% | 1.16 |
| knn_k20_gesm2 | 90% | 1.16 |
| knn_k20_gscfoundation | 90% | 1.17 |
| knn_k20_gscgpt | 88% | 1.19 |
| knn_k5 | 80% | 1.26 |
| scgen | 77% | 1.30 |
| knn_k1 | 32% | 1.63 |
| random_shift_s0 | 31% | 1.75 |
| random_shift_s1 | 31% | 1.73 |

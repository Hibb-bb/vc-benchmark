# Type-level link on Parse PBMC: does annotation quality for a type transfer to perturbation prediction in that type?

27 shared encoders x 15 cell types with >= 30 items on both sides. Abilities are anchored to the panel-level (A) and screen-level (B, unseen-combination scheme) item difficulties. `residual` subtracts each encoder's overall ability on each side, leaving the type-specific part.

- overall (one ability per encoder per side) Spearman across encoders: +0.89
- share of the per-type ability variance that is the encoder's overall ability: A 0.75, B 0.93
- within type, Spearman across encoders (raw): median +0.79, range +0.50 to +0.88
- within type, residual (type-specific part): median +0.06, range -0.62 to +0.62, 5 of 15 types with p < 0.05
- within encoder, Spearman across types (raw): median +0.23; residual: median +0.23
- pooled residual over all (encoder, type) cells: +0.16 (p = 0.001, n = 405); without the null encoders +0.28

| cell type | A items | B items | raw rho | raw rho (no null) | residual rho | p |
|---|---|---|---|---|---|---|
| CD4 Naive | 1000 | 1074 | +0.83 | +0.64 | +0.62 | 0.0006 |
| cDC | 1000 | 707 | +0.50 | +0.01 | +0.49 | 0.0087 |
| Treg | 1000 | 953 | +0.86 | +0.67 | +0.48 | 0.012 |
| CD4 Memory | 1000 | 1080 | +0.86 | +0.70 | +0.39 | 0.046 |
| CD8 Naive | 1000 | 1068 | +0.74 | +0.50 | +0.29 | 0.14 |
| pDC | 601 | 84 | +0.63 | +0.20 | +0.28 | 0.15 |
| CD16 Mono | 1000 | 961 | +0.84 | +0.66 | +0.18 | 0.37 |
| MAIT | 1000 | 987 | +0.80 | +0.55 | +0.06 | 0.76 |
| B Naive | 1000 | 1079 | +0.68 | +0.39 | -0.01 | 0.97 |
| B Intermediate-Memory | 1000 | 1079 | +0.78 | +0.50 | -0.02 | 0.93 |
| CD14 Mono | 1000 | 1080 | +0.81 | +0.68 | -0.16 | 0.44 |
| NK | 1000 | 1079 | +0.79 | +0.51 | -0.17 | 0.39 |
| NK CD56bright | 1000 | 962 | +0.88 | +0.80 | -0.25 | 0.21 |
| NKT | 957 | 691 | +0.72 | +0.42 | -0.33 | 0.094 |
| CD8 Memory | 1000 | 1080 | +0.76 | +0.49 | -0.62 | 0.00059 |

| encoder | family | A overall | B overall | raw rho across types | residual rho |
|---|---|---|---|---|---|
| Nyström-256D (kernel width = 0.5) | Kernel features | +3.41 | -2.75 | +0.39 | +0.39 |
| Nyström-64D (kernel width = 0.5) | Kernel features | +3.41 | -2.87 | +0.23 | +0.23 |
| Nyström-256D (kernel width = 2) | Kernel features | +3.37 | -2.86 | +0.02 | +0.02 |
| ICA-64D | ICA | +3.34 | -2.67 | +0.68 | +0.68 |
| PCA-128D | PCA | +3.34 | -2.27 | +0.49 | +0.49 |
| PCA-64D | PCA | +3.34 | -2.67 | +0.68 | +0.68 |
| PCA-32D | PCA | +3.31 | -3.02 | +0.65 | +0.65 |
| Nyström-64D (kernel width = 2) | Kernel features | +3.24 | -3.13 | +0.29 | +0.29 |
| PCA-256D | PCA | +3.23 | -2.03 | -0.29 | -0.29 |
| NMF-64D | NMF | +3.16 | -2.51 | -0.18 | -0.18 |
| PCA-16D | PCA | +2.97 | -3.40 | +0.62 | +0.62 |
| ICA-16D | ICA | +2.96 | -3.40 | +0.59 | +0.59 |
| GMM-100 memberships | GMM | +2.60 | -3.39 | -0.20 | -0.20 |
| NMF-16D | NMF | +2.56 | -3.27 | +0.35 | +0.35 |
| Random projection-128D (seed 0) | Random projection | +2.37 | -3.06 | +0.21 | +0.21 |
| Random projection-128D (seed 1) | Random projection | +2.33 | -3.08 | +0.25 | +0.25 |
| GMM-30 memberships | GMM | +1.93 | -3.95 | -0.02 | -0.02 |
| PCA-8D | PCA | +1.49 | -4.24 | +0.27 | +0.27 |
| Random projection-32D (seed 0) | Random projection | +0.59 | -4.28 | +0.39 | +0.39 |
| Random projection-32D (seed 1) | Random projection | +0.57 | -4.33 | +0.43 | +0.43 |
| PCA-4D | PCA | +0.54 | -5.63 | +0.23 | +0.23 |
| GMM-10 memberships | GMM | -0.38 | -5.31 | +0.17 | +0.17 |
| Random projection-8D (seed 1) | Random projection | -1.30 | -5.25 | +0.03 | +0.03 |
| Random projection-8D (seed 0) | Random projection | -1.50 | -5.18 | -0.12 | -0.12 |
| Depth only (2D) | Floor | -2.63 | -4.99 | -0.06 | -0.06 |
| Random-32D (seed 1) | Floor | -3.80 | -6.16 | -0.31 | -0.31 |
| Random-32D (seed 0) | Floor | -3.82 | -6.18 | -0.06 | -0.06 |

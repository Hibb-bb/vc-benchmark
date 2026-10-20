# Representation -> perturbation link on Parse PBMC

A: `repr_parse_pbmc_celltype` cell-level difficulties (donors held out). B: `parse_pbmc_cytokines` difficulties. Contexts are joined on (donor, cell type); only the five A test donors overlap. Mean difficulty over informative items; `nobody` is the share of items no respondent passes.

| A scale | B scheme | B scale | level | n | Spearman | p | partial (log cells) | Pearson | nobody-share Spearman |
|---|---|---|---|---|---|---|---|---|---|
| panel | context | screen | cell_type | 16 | -0.156 | 0.56 | +0.344 | -0.043 | 0.157 |
| panel | context | screen | donor_type | 69 | -0.029 | 0.81 | +0.233 | -0.117 | -0.062 |
| panel | context | pooled | cell_type | 16 | -0.150 | 0.58 | +0.338 | -0.037 | 0.157 |
| panel | context | pooled | donor_type | 69 | -0.034 | 0.78 | +0.216 | -0.124 | -0.062 |
| panel | perturbation | screen | cell_type | 16 | +0.071 | 0.8 | +0.424 | +0.142 | -0.023 |
| panel | perturbation | screen | donor_type | 67 | +0.116 | 0.35 | +0.279 | +0.103 | -0.019 |
| panel | perturbation | pooled | cell_type | 16 | +0.071 | 0.8 | +0.424 | +0.136 | -0.023 |
| panel | perturbation | pooled | donor_type | 67 | +0.116 | 0.35 | +0.280 | +0.100 | -0.019 |
| pooled | context | screen | cell_type | 16 | -0.100 | 0.71 | +0.326 | -0.071 | 0.157 |
| pooled | context | screen | donor_type | 69 | -0.032 | 0.79 | +0.221 | -0.144 | -0.062 |
| pooled | context | pooled | cell_type | 16 | -0.094 | 0.73 | +0.321 | -0.064 | 0.157 |
| pooled | context | pooled | donor_type | 69 | -0.038 | 0.75 | +0.205 | -0.151 | -0.062 |
| pooled | perturbation | screen | cell_type | 16 | +0.115 | 0.67 | +0.403 | +0.122 | -0.023 |
| pooled | perturbation | screen | donor_type | 67 | +0.122 | 0.32 | +0.276 | +0.089 | -0.019 |
| pooled | perturbation | pooled | cell_type | 16 | +0.115 | 0.67 | +0.403 | +0.117 | -0.023 |
| pooled | perturbation | pooled | donor_type | 67 | +0.122 | 0.32 | +0.277 | +0.086 | -0.019 |

## Cell types (A panel scale, B context-scheme screen scale)

| cell type | A items | A diff | A nobody | B items | B diff | B nobody | B cells/item |
|---|---|---|---|---|---|---|---|
| cDC | 1000 | -2.11 | 0.00 | 707 | +0.08 | 0.03 | 109 |
| HSPC | 889 | -1.84 | 0.00 | 3 | -3.05 | 0.00 | 54 |
| pDC | 601 | -1.31 | 0.00 | 84 | +0.49 | 0.00 | 106 |
| CD14 Mono | 1000 | -0.69 | 0.00 | 1080 | -1.37 | 0.02 | 1232 |
| B Naive | 1000 | -0.68 | 0.00 | 1079 | -0.45 | 0.04 | 417 |
| CD16 Mono | 1000 | -0.50 | 0.00 | 961 | -0.18 | 0.04 | 214 |
| Treg | 1000 | -0.10 | 0.00 | 953 | +0.95 | 0.05 | 141 |
| NK CD56bright | 1000 | +0.01 | 0.00 | 962 | +1.23 | 0.04 | 98 |
| NKT | 957 | +0.02 | 0.00 | 691 | +1.70 | 0.09 | 153 |
| CD8 Naive | 1000 | +0.03 | 0.00 | 1068 | -0.52 | 0.05 | 417 |
| NK | 1000 | +0.21 | 0.01 | 1079 | -0.29 | 0.07 | 391 |
| B Intermediate-Memory | 1000 | +0.24 | 0.00 | 1079 | +0.14 | 0.04 | 236 |
| MAIT | 1000 | +0.64 | 0.01 | 987 | +0.27 | 0.06 | 290 |
| CD4 Naive | 1000 | +1.57 | 0.01 | 1074 | -1.44 | 0.02 | 1261 |
| CD8 Memory | 1000 | +2.14 | 0.07 | 1080 | -0.69 | 0.05 | 603 |
| CD4 Memory | 1000 | +2.39 | 0.06 | 1080 | -1.45 | 0.02 | 1909 |

## Shared encoders

| scale | n | Spearman | p | without random projections |
|---|---|---|---|---|
| pooled_context | 27 | +0.937 | 6.6e-13 | +0.953 (n=21) |
| pooled | 27 | +0.954 | 1.3e-14 | +0.957 (n=21) |

| encoder | family | A ability | B ability | B pass | B outfit | scale |
|---|---|---|---|---|---|---|
| Nyström-256D (kernel width = 0.5) | Kernel features | +0.72 | -0.57 | 0.43 | 0.29 | pooled_context |
| Nyström-256D (kernel width = 0.5) | Kernel features | +0.72 | -2.72 | 0.17 | 0.33 | pooled |
| PCA-128D | PCA | +0.69 | +0.63 | 0.56 | 0.33 | pooled_context |
| PCA-128D | PCA | +0.69 | -2.60 | 0.18 | 0.32 | pooled |
| PCA-256D | PCA | +0.67 | +0.87 | 0.58 | 0.34 | pooled_context |
| PCA-256D | PCA | +0.67 | -2.57 | 0.19 | 0.34 | pooled |
| Nyström-64D (kernel width = 0.5) | Kernel features | +0.67 | -0.91 | 0.40 | 0.29 | pooled_context |
| Nyström-64D (kernel width = 0.5) | Kernel features | +0.67 | -2.83 | 0.16 | 0.31 | pooled |
| ICA-64D | ICA | +0.67 | -0.02 | 0.49 | 0.31 | pooled_context |
| ICA-64D | ICA | +0.67 | -2.73 | 0.17 | 0.29 | pooled |
| PCA-64D | PCA | +0.66 | -0.02 | 0.49 | 0.31 | pooled_context |
| PCA-64D | PCA | +0.66 | -2.73 | 0.17 | 0.29 | pooled |
| Nyström-256D (kernel width = 2) | Kernel features | +0.62 | -0.81 | 0.41 | 0.29 | pooled_context |
| Nyström-256D (kernel width = 2) | Kernel features | +0.62 | -2.72 | 0.17 | 0.42 | pooled |
| PCA-32D | PCA | +0.53 | -2.09 | 0.29 | 0.41 | pooled_context |
| PCA-32D | PCA | +0.53 | -2.98 | 0.15 | 0.32 | pooled |
| Nyström-64D (kernel width = 2) | Kernel features | +0.42 | -1.59 | 0.33 | 0.33 | pooled_context |
| Nyström-64D (kernel width = 2) | Kernel features | +0.42 | -2.94 | 0.15 | 0.45 | pooled |
| NMF-64D | NMF | +0.41 | -0.94 | 0.39 | 0.50 | pooled_context |
| NMF-64D | NMF | +0.41 | -2.99 | 0.15 | 0.57 | pooled |
| PCA-16D | PCA | +0.11 | -2.86 | 0.23 | 0.57 | pooled_context |
| PCA-16D | PCA | +0.11 | -3.11 | 0.14 | 0.33 | pooled |
| ICA-16D | ICA | +0.11 | -2.86 | 0.23 | 0.57 | pooled_context |
| ICA-16D | ICA | +0.11 | -3.11 | 0.14 | 0.33 | pooled |
| Random projection-128D (seed 0) | Random projection | -0.07 | -1.27 | 0.36 | 0.38 | pooled_context |
| Random projection-128D (seed 0) | Random projection | -0.07 | -3.23 | 0.13 | 0.33 | pooled |
| Random projection-128D (seed 1) | Random projection | -0.09 | -1.35 | 0.35 | 0.37 | pooled_context |
| Random projection-128D (seed 1) | Random projection | -0.09 | -3.20 | 0.14 | 0.37 | pooled |
| GMM-100 memberships | GMM | -0.18 | -3.14 | 0.21 | 0.94 | pooled_context |
| GMM-100 memberships | GMM | -0.18 | -2.99 | 0.15 | 0.68 | pooled |
| NMF-16D | NMF | -0.37 | -2.38 | 0.26 | 0.58 | pooled_context |
| NMF-16D | NMF | -0.37 | -3.07 | 0.14 | 0.41 | pooled |
| PCA-8D | PCA | -0.67 | -3.75 | 0.17 | 1.87 | pooled_context |
| PCA-8D | PCA | -0.67 | -3.35 | 0.12 | 0.48 | pooled |
| GMM-30 memberships | GMM | -0.68 | -4.58 | 0.12 | 3.94 | pooled_context |
| GMM-30 memberships | GMM | -0.68 | -3.33 | 0.13 | 0.78 | pooled |
| Random projection-32D (seed 0) | Random projection | -1.29 | -3.02 | 0.21 | 0.80 | pooled_context |
| Random projection-32D (seed 0) | Random projection | -1.29 | -3.57 | 0.11 | 0.62 | pooled |
| Random projection-32D (seed 1) | Random projection | -1.31 | -3.13 | 0.21 | 0.63 | pooled_context |
| Random projection-32D (seed 1) | Random projection | -1.31 | -3.54 | 0.11 | 0.65 | pooled |
| PCA-4D | PCA | -1.50 | -4.05 | 0.15 | 5.52 | pooled_context |
| PCA-4D | PCA | -1.50 | -3.43 | 0.12 | 0.80 | pooled |
| GMM-10 memberships | GMM | -1.88 | -4.35 | 0.13 | 2.69 | pooled_context |
| GMM-10 memberships | GMM | -1.88 | -3.44 | 0.12 | 0.83 | pooled |
| Random projection-8D (seed 0) | Random projection | -2.70 | -4.42 | 0.13 | 1.83 | pooled_context |
| Random projection-8D (seed 0) | Random projection | -2.70 | -3.77 | 0.10 | 0.82 | pooled |
| Random projection-8D (seed 1) | Random projection | -2.70 | -4.73 | 0.11 | 2.93 | pooled_context |
| Random projection-8D (seed 1) | Random projection | -2.70 | -3.77 | 0.10 | 0.94 | pooled |
| Depth only (2D) | Floor | -3.14 | -4.35 | 0.13 | 8.34 | pooled_context |
| Depth only (2D) | Floor | -3.14 | -3.51 | 0.11 | 1.32 | pooled |
| Random-32D (seed 1) | Floor | -3.83 | -6.34 | 0.05 | 4.97 | pooled_context |
| Random-32D (seed 1) | Floor | -3.83 | -4.00 | 0.08 | 0.85 | pooled |
| Random-32D (seed 0) | Floor | -3.83 | -6.35 | 0.05 | 3.72 | pooled_context |
| Random-32D (seed 0) | Floor | -3.83 | -3.99 | 0.08 | 0.81 | pooled |

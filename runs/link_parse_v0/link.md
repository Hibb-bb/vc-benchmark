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

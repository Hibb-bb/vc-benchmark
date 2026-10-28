# What makes a Parse cytokine item hard

13967 items: 90 cytokines x 169 donor-cell-type contexts. Difficulty from the per-screen Rasch fits. Spearman correlations over items that at least one model passed; items passed by nobody are summarised separately.

## Unseen combination

- items passed by nobody: 601 of 13967

| descriptor | Spearman r with difficulty | median, hardest 10% | median, rest | median, passed by nobody |
|---|---|---|---|---|
| response strength (L2) | +0.01 | 3.2 | 2.93 | 2.7 |
| signal-to-noise | -0.56 | 1.13 | 1.62 | 1.2 |
| agreement with other donors | -0.72 | 0.183 | 0.42 | 0.164 |
| receptor expression | -0.22 | 0.00549 | 0.0134 | 0.00363 |
| interferon-gene share | -0.29 | 0.00159 | 0.00444 | 0.00292 |
| cells per item | -0.40 | 166 | 404 | 292 |
| mean-shift reference r | +0.37 | 0.393 | 0.344 | 0.45 |

### By family

| family | items | mean difficulty | share passed by nobody |
|---|---|---|---|
| chemokine | 155 | +1.74 | 9% |
| IL-12 family | 626 | +0.69 | 5% |
| adipokine | 312 | +0.67 | 5% |
| matrix / other | 311 | +0.58 | 5% |
| IL-17 family | 927 | +0.56 | 5% |
| IL-3 / common beta | 467 | +0.53 | 5% |
| IL-10 family | 931 | +0.50 | 8% |
| growth factor | 1083 | +0.39 | 5% |
| IL-1 family | 1091 | +0.33 | 7% |
| hematopoietin | 1243 | +0.32 | 7% |
| type III interferon | 466 | +0.19 | 2% |
| IL-6 / gp130 | 939 | +0.13 | 3% |
| TNF superfamily | 2642 | -0.04 | 3% |
| complement | 154 | -0.10 | 2% |
| TGF-beta family | 311 | -0.54 | 2% |
| other | 468 | -1.08 | 0% |
| common gamma chain / IL-4 | 1072 | -1.42 | 2% |
| type I interferon | 613 | -1.67 | 1% |
| type II interferon | 156 | -1.86 | 3% |

### By lineage

| lineage | items | mean difficulty | share passed by nobody |
|---|---|---|---|
| innate-like T | 1678 | +1.16 | 7% |
| NK | 2041 | +0.71 | 6% |
| dendritic | 791 | +0.28 | 3% |
| B | 2158 | +0.07 | 4% |
| CD8 T | 2148 | -0.32 | 5% |
| CD4 T | 3107 | -0.55 | 3% |
| monocyte | 2041 | -0.64 | 3% |
| progenitor | 3 | -3.05 | 0% |

## Unseen cytokine

- items passed by nobody: 3223 of 13967

| descriptor | Spearman r with difficulty | median, hardest 10% | median, rest | median, passed by nobody |
|---|---|---|---|---|
| response strength (L2) | -0.29 | 2.83 | 3.2 | 2.9 |
| signal-to-noise | -0.54 | 1.3 | 1.83 | 1.21 |
| agreement with other donors | -0.36 | 0.308 | 0.451 | 0.248 |
| receptor expression | -0.18 | 0.00712 | 0.0136 | 0.00927 |
| interferon-gene share | -0.39 | 0.00224 | 0.00595 | 0.00231 |
| cells per item | -0.21 | 286 | 438 | 230 |
| mean-shift reference r | +0.09 | 0.384 | 0.328 | 0.39 |

### By family

| family | items | mean difficulty | share passed by nobody |
|---|---|---|---|
| matrix / other | 311 | +0.86 | 42% |
| type III interferon | 466 | +0.61 | 33% |
| chemokine | 155 | +0.53 | 23% |
| IL-17 family | 927 | +0.51 | 28% |
| adipokine | 312 | +0.47 | 28% |
| complement | 154 | +0.34 | 36% |
| growth factor | 1083 | +0.31 | 25% |
| TNF superfamily | 2642 | +0.23 | 23% |
| IL-3 / common beta | 467 | +0.21 | 32% |
| IL-12 family | 626 | +0.20 | 31% |
| IL-6 / gp130 | 939 | +0.12 | 17% |
| hematopoietin | 1243 | +0.12 | 24% |
| TGF-beta family | 311 | -0.00 | 18% |
| IL-10 family | 931 | -0.05 | 20% |
| other | 468 | -0.21 | 20% |
| IL-1 family | 1091 | -0.35 | 20% |
| type I interferon | 613 | -0.71 | 23% |
| common gamma chain / IL-4 | 1072 | -1.27 | 11% |
| type II interferon | 156 | -1.50 | 9% |

### By lineage

| lineage | items | mean difficulty | share passed by nobody |
|---|---|---|---|
| progenitor | 3 | +1.06 | 67% |
| innate-like T | 1678 | +0.85 | 41% |
| NK | 2041 | +0.40 | 29% |
| dendritic | 791 | +0.17 | 24% |
| CD8 T | 2148 | +0.09 | 23% |
| B | 2158 | +0.06 | 22% |
| CD4 T | 3107 | -0.32 | 18% |
| monocyte | 2041 | -0.74 | 10% |


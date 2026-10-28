# What makes a Parse cytokine item hard

13967 items: 90 cytokines x 169 donor-cell-type contexts. Difficulty from the per-screen Rasch fits. Spearman correlations over items that at least one model passed; items passed by nobody are summarised separately.

## Unseen combination

- items passed by nobody: 601 of 13967

| descriptor | Spearman r with difficulty | median, hardest 10% | median, rest | median, passed by nobody |
|---|---|---|---|---|
| response strength (L2) | +0.01 | 3.2 | 2.93 | 2.7 |
| signal-to-noise | -0.56 | 1.13 | 1.62 | 1.2 |
| agreement with other donors | -0.72 | 0.183 | 0.42 | 0.164 |
| receptor expression | -0.24 | 0.00361 | 0.00867 | 0.00305 |
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
| receptor expression | -0.20 | 0.00449 | 0.00928 | 0.00584 |
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


## Failure modes (2026-10-28)

"Hard" = the hardest 10% of items that someone passed, plus every item nobody passed. "No real response" =
signal-to-noise below 1.5 and agreement with the other donors below 0.3. "Real response" = signal-to-noise
at least 2 and donor agreement at least 0.5.

| split | hard items | hard with no real response | same share among other items | hard with a real response |
|---|---|---|---|---|
| unseen combination | 3,031 | 2,306 (76%) | 15% | 18 (1%) |
| unseen cytokine | 6,417 | 3,131 (49%) | 9% | 341 (5%) |

1. Most hard items have nothing to predict. The cytokine barely moves those cells: the shift is the size of
   sampling noise and does not repeat in the other donors. Raw response size does not track difficulty
   (r = +0.01) because noise inflates it; signal-to-noise (r = -0.56) and donor agreement (r = -0.72) do.
2. Receptor absence explains much of it. Items whose cell type barely expresses the cytokine's receptor
   (control mean below 0.01) average difficulty +0.47; items with clear receptor expression (above 0.2) -1.02.
   The hardest cytokines (IL-26, IL-17E, SCF, IL-35, HGF, LIF, GDNF, FLT3L, 4-1BBL, Megalin) mostly act on
   tissue or progenitor cells, not on circulating blood cells.
3. The easy cytokines are the strong JAK-STAT signals: type I and II interferons and the common-gamma-chain
   cytokines (IL-2, IL-4, IL-7, IL-15), plus IL-1-beta and CD40L. Their responses repeat across donors
   (agreement 0.73 to 0.88).
4. When the response is real but the item is hard in the unseen-combination split, the response looks
   like the cell type's average response (mean-shift reference r 0.80 against 0.37 overall): the pass
   rule asks to beat a reference that is already nearly right.
5. In the unseen-cytokine split, real but missed responses concentrate on cytokines with a distinctive
   programme that other cytokines do not predict: IFN-epsilon, IFN-lambda1 and 3, IFN-alpha1, IL-32-beta,
   TSLP, IL-21, IL-3, IL-4, IL-12, mostly in CD4 memory T cells and CD14 monocytes. These are the genuine
   generalisation failures.
6. Innate-like T cells (MAIT, NKT) and NK cells are the hardest lineages, monocytes the easiest; fewer cells
   per item (r = -0.40) adds noise.

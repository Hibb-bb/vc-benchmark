# Text embeddings as perturbation representations

similarity match = Spearman r between representation similarity and response similarity over all pairs; neighbour r = mean response correlation with the 5 nearest neighbours (all-pairs mean in brackets); class = 5-NN accuracy at a known label (chance in brackets).

## AdamsonWeissman2016_GSM2406681_10X010 (CRISPRi, 87 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.244 | 0.375 (0.215) |  |
| Qwen3-Embedding-4B · card | +0.125 | 0.361 (0.215) |  |
| pubmedbert-base-embeddings · name only | +0.123 | 0.298 (0.215) |  |
| baseline · gene from control cells | +0.066 | 0.269 (0.215) |  |
| Qwen3-Embedding-4B · name only | +0.004 | 0.290 (0.215) |  |
| Qwen3-Embedding-0.6B · name only | +0.001 | 0.280 (0.215) |  |
| random | -0.006 | 0.208 (0.215) |  |
| Qwen3-Embedding-0.6B · card | -0.026 | 0.323 (0.215) |  |

## FrangiehIzar2021_RNA (CRISPR_KO, 229 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · name only | +0.085 | 0.210 (0.203) |  |
| Qwen3-Embedding-4B · card | +0.070 | 0.230 (0.203) |  |
| Qwen3-Embedding-0.6B · card | +0.045 | 0.224 (0.203) |  |
| pubmedbert-base-embeddings · card | +0.040 | 0.226 (0.203) |  |
| baseline · gene from control cells | +0.031 | 0.211 (0.199) |  |
| pubmedbert-base-embeddings · name only | +0.021 | 0.231 (0.203) |  |
| random | +0.010 | 0.208 (0.203) |  |
| Qwen3-Embedding-0.6B · name only | -0.019 | 0.207 (0.203) |  |

## McFarlandTsherniak2020 (drug, 16 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| random | +0.107 | 0.262 (0.198) |  |
| Qwen3-Embedding-0.6B · name only | +0.046 | 0.138 (0.152) |  |
| Qwen3-Embedding-4B · name only | +0.032 | 0.152 (0.152) |  |
| pubmedbert-base-embeddings · name only | +0.031 | 0.128 (0.152) |  |
| Qwen3-Embedding-4B · card | +0.030 | 0.144 (0.152) |  |
| Qwen3-Embedding-0.6B · card | +0.020 | 0.178 (0.152) |  |
| pubmedbert-base-embeddings · card | -0.113 | 0.135 (0.152) |  |

## NadigOConner2024_hepg2 (CRISPRi, 1061 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.170 | 0.275 (0.148) |  |
| Qwen3-Embedding-4B · card | +0.166 | 0.281 (0.148) |  |
| Qwen3-Embedding-0.6B · card | +0.152 | 0.274 (0.148) |  |
| baseline · gene from control cells | +0.091 | 0.235 (0.164) |  |
| Qwen3-Embedding-0.6B · name only | +0.050 | 0.237 (0.148) |  |
| Qwen3-Embedding-4B · name only | +0.020 | 0.244 (0.148) |  |
| pubmedbert-base-embeddings · name only | +0.016 | 0.237 (0.148) |  |
| random | +0.001 | 0.145 (0.148) |  |

## NadigOConner2024_jurkat (CRISPRi, 1815 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.106 | 0.144 (0.052) |  |
| Qwen3-Embedding-4B · card | +0.105 | 0.148 (0.052) |  |
| Qwen3-Embedding-0.6B · card | +0.093 | 0.139 (0.052) |  |
| baseline · gene from control cells | +0.045 | 0.095 (0.060) |  |
| Qwen3-Embedding-0.6B · name only | +0.019 | 0.114 (0.052) |  |
| Qwen3-Embedding-4B · name only | +0.005 | 0.117 (0.052) |  |
| random | +0.000 | 0.048 (0.052) |  |
| pubmedbert-base-embeddings · name only | -0.001 | 0.117 (0.052) |  |

## NormanWeissman2019_filtered (CRISPRa, 236 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · card | +0.207 | 0.546 (0.244) |  |
| pubmedbert-base-embeddings · card | +0.196 | 0.531 (0.244) |  |
| Qwen3-Embedding-0.6B · card | +0.163 | 0.533 (0.244) |  |
| Qwen3-Embedding-4B · name only | +0.085 | 0.509 (0.244) |  |
| baseline · gene from control cells | +0.076 | 0.507 (0.243) |  |
| pubmedbert-base-embeddings · name only | +0.019 | 0.491 (0.244) |  |
| Qwen3-Embedding-0.6B · name only | +0.013 | 0.512 (0.244) |  |
| random | +0.001 | 0.256 (0.244) |  |

## ReplogleWeissman2022_K562_essential (CRISPRi, 1832 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.123 | 0.186 (0.048) |  |
| Qwen3-Embedding-0.6B · card | +0.107 | 0.177 (0.048) |  |
| Qwen3-Embedding-4B · card | +0.101 | 0.186 (0.048) |  |
| Qwen3-Embedding-0.6B · name only | +0.030 | 0.143 (0.048) |  |
| baseline · gene from control cells | +0.030 | 0.104 (0.055) |  |
| pubmedbert-base-embeddings · name only | +0.017 | 0.149 (0.048) |  |
| Qwen3-Embedding-4B · name only | +0.015 | 0.150 (0.048) |  |
| random | +0.001 | 0.047 (0.048) |  |

## ReplogleWeissman2022_K562_gwps (CRISPRi, 2000 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.012 | 0.033 (0.009) |  |
| Qwen3-Embedding-0.6B · name only | +0.010 | 0.022 (0.009) |  |
| baseline · gene from control cells | +0.008 | 0.017 (0.011) |  |
| Qwen3-Embedding-0.6B · card | +0.004 | 0.028 (0.009) |  |
| Qwen3-Embedding-4B · card | +0.003 | 0.030 (0.009) |  |
| Qwen3-Embedding-4B · name only | +0.000 | 0.023 (0.009) |  |
| random | +0.000 | 0.008 (0.009) |  |
| pubmedbert-base-embeddings · name only | -0.010 | 0.023 (0.009) |  |

## ReplogleWeissman2022_rpe1 (CRISPRi, 1611 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| pubmedbert-base-embeddings · card | +0.144 | 0.279 (0.188) |  |
| Qwen3-Embedding-4B · card | +0.114 | 0.277 (0.188) |  |
| Qwen3-Embedding-0.6B · card | +0.094 | 0.270 (0.188) |  |
| Qwen3-Embedding-4B · name only | +0.079 | 0.250 (0.188) |  |
| baseline · gene from control cells | +0.023 | 0.256 (0.218) |  |
| Qwen3-Embedding-0.6B · name only | +0.007 | 0.250 (0.188) |  |
| pubmedbert-base-embeddings · name only | +0.006 | 0.245 (0.188) |  |
| random | -0.000 | 0.188 (0.188) |  |

## SrivatsanTrapnell2020_sciplex3 (drug, 188 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-0.6B · name only | +0.074 | 0.208 (0.166) | 0.14 (0.21) |
| Qwen3-Embedding-4B · name only | +0.056 | 0.246 (0.166) | 0.33 (0.21) |
| Qwen3-Embedding-0.6B · card | +0.045 | 0.269 (0.166) | 0.59 (0.21) |
| pubmedbert-base-embeddings · card | +0.030 | 0.244 (0.166) | 0.64 (0.21) |
| pubmedbert-base-embeddings · name only | +0.018 | 0.192 (0.166) | 0.23 (0.21) |
| Qwen3-Embedding-4B · card | +0.017 | 0.281 (0.166) | 0.67 (0.21) |
| random | -0.002 | 0.171 (0.166) | 0.13 (0.21) |

## TianKampmann2019_day7neuron (CRISPRi, 35 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · card | +0.496 | 0.311 (0.254) |  |
| pubmedbert-base-embeddings · name only | +0.443 | 0.318 (0.254) |  |
| baseline · gene from control cells | +0.421 | 0.330 (0.254) |  |
| pubmedbert-base-embeddings · card | +0.408 | 0.312 (0.254) |  |
| Qwen3-Embedding-0.6B · name only | +0.379 | 0.305 (0.254) |  |
| Qwen3-Embedding-0.6B · card | +0.371 | 0.302 (0.254) |  |
| Qwen3-Embedding-4B · name only | +0.343 | 0.301 (0.254) |  |
| random | +0.013 | 0.273 (0.254) |  |

## TianKampmann2019_iPSC (CRISPRi, 81 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · name only | +0.273 | 0.183 (0.151) |  |
| pubmedbert-base-embeddings · name only | +0.271 | 0.185 (0.151) |  |
| baseline · gene from control cells | +0.269 | 0.175 (0.151) |  |
| Qwen3-Embedding-0.6B · card | +0.258 | 0.183 (0.151) |  |
| Qwen3-Embedding-4B · card | +0.244 | 0.178 (0.151) |  |
| pubmedbert-base-embeddings · card | +0.229 | 0.176 (0.151) |  |
| Qwen3-Embedding-0.6B · name only | +0.190 | 0.176 (0.151) |  |
| random | -0.003 | 0.153 (0.151) |  |

## TianKampmann2021_CRISPRi (CRISPRi, 183 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · name only | +0.012 | 0.286 (0.285) |  |
| baseline · gene from control cells | +0.004 | 0.282 (0.284) |  |
| pubmedbert-base-embeddings · card | +0.003 | 0.286 (0.285) |  |
| random | -0.005 | 0.286 (0.285) |  |
| pubmedbert-base-embeddings · name only | -0.010 | 0.282 (0.285) |  |
| Qwen3-Embedding-0.6B · name only | -0.024 | 0.288 (0.285) |  |
| Qwen3-Embedding-4B · card | -0.033 | 0.280 (0.285) |  |
| Qwen3-Embedding-0.6B · card | -0.045 | 0.283 (0.285) |  |

## parse_pbmc_cytokines (cytokine, 90 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| baseline · esm2 genes | +0.046 | 0.177 (0.139) | 0.50 (0.19) |
| baseline · geneformer genes | +0.043 | 0.186 (0.139) | 0.43 (0.19) |
| baseline · scfoundation genes | +0.032 | 0.185 (0.139) | 0.50 (0.19) |
| baseline · scgpt genes | +0.029 | 0.172 (0.139) | 0.52 (0.19) |
| Qwen3-Embedding-4B · card | +0.024 | 0.214 (0.139) | 0.79 (0.19) |
| random | +0.013 | 0.167 (0.139) | 0.07 (0.19) |
| pubmedbert-base-embeddings · card | -0.002 | 0.199 (0.139) | 0.66 (0.19) |
| Qwen3-Embedding-0.6B · card | -0.008 | 0.167 (0.139) | 0.68 (0.19) |
| pubmedbert-base-embeddings · name only | -0.031 | 0.203 (0.139) | 0.50 (0.19) |
| Qwen3-Embedding-0.6B · name only | -0.063 | 0.145 (0.139) | 0.31 (0.19) |
| Qwen3-Embedding-4B · name only | -0.074 | 0.168 (0.139) | 0.40 (0.19) |

## tahoe100m (drug, 379 perturbations)

| representation | similarity match | neighbour r | class accuracy |
|---|---|---|---|
| Qwen3-Embedding-4B · card | +0.065 | 0.351 (0.269) | 0.88 (0.53) |
| Qwen3-Embedding-0.6B · card | +0.054 | 0.346 (0.269) | 0.75 (0.53) |
| Qwen3-Embedding-4B · name only | +0.052 | 0.344 (0.269) | 0.69 (0.53) |
| Qwen3-Embedding-0.6B · name only | +0.042 | 0.350 (0.269) | 0.61 (0.53) |
| baseline · chemical fingerprint | +0.022 | 0.301 (0.268) | 0.55 (0.52) |
| pubmedbert-base-embeddings · name only | +0.019 | 0.316 (0.269) | 0.50 (0.53) |
| pubmedbert-base-embeddings · card | +0.015 | 0.340 (0.269) | 0.82 (0.53) |
| random | +0.004 | 0.248 (0.269) | 0.44 (0.53) |

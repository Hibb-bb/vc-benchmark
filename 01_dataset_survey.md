# Virtual cell datasets and benchmarks: survey (as of 2026-10-13)

Scope: public data usable for a living IRT benchmark with two components,
(A) representation (cell embeddings; probe tasks such as cell-type annotation,
integration, label transfer) and (B) transition (perturbation response
prediction, genetic and chemical). Sizes are as reported by the sources linked;
anything marked ~ or "verify" I did not confirm against the primary record.

## 0. The landscape in six sentences

1. Data now comes in two tiers: giant atlases (Arc Virtual Cell Atlas with
   Tahoe-100M and scBaseCount, X-Atlas/Orion, CELLxGENE Census, the Virtual
   Cell Challenge releases) and curated benchmark collections with fixed
   splits (scPerturb, scPerturBench, PerturBench, Systema, cz-benchmarks,
   Open Problems).
2. For perturbation prediction, the 2025 to 2026 consensus is that linear and
   mean-shift baselines are competitive with deep models on standard metrics
   (Ahlmann-Eltze et al. Nat Methods 2025; Systema Nat Biotech 2025; PerturBench
   NeurIPS 2025; two 2026 unified benchmarks), with a rebuttal arguing the gap
   reappears under calibrated metrics (Nat Biotech 2026).
3. For representation, zero-shot foundation-model embeddings do not reliably
   beat HVG+PCA, scVI, or Harmony (Kedzierska et al. Genome Biol 2025; three
   2026 preprints; "parameter-free representations" arXiv 2602.16696).
4. Both findings are exactly the regime where difficulty-aware scoring pays
   off: most items are passed by everything, and the ranking is decided by a
   minority of hard items that current metrics average away.
5. The cleanest held-out data this year is the Virtual Cell Challenge 2026
   set (six cell lines, >10k CRISPRi knockdowns per line, zero-shot across
   lines, data rolling out from October 2026).
6. Contamination is the main threat to any ability estimate: Replogle,
   Norman, Adamson, Tahoe, and CELLxGENE are inside the training sets of most
   foundation models, so the benchmark needs a provenance register per item.

## 1. Benchmark suites and curated collections (what to reuse)

| Suite | What it gives you | Datasets | Notes for us |
|---|---|---|---|
| [scPerturb](https://projects.sanderlab.org/scperturb/) (Peidli et al., Nat Methods 2024) | 44 harmonized h5ad perturbation datasets, uniform QC, E-distance | 32 CRISPR RNA, 9 drug RNA, 3 scATAC, 3 CITE-seq. Zenodo [7041849](https://zenodo.org/record/7041849) (RNA), [7058382](https://zenodo.org/record/7058382) (ATAC) | Best single backbone for component B. pertpy loaders read from it. |
| [scPerturBench](https://github.com/bm2-lab/scPerturBench) (bm2-lab, 2025) | 27 methods, 29 datasets, 3 scenarios: unseen cell context (12 datasets), unseen genetic perturbation (14), unseen chemical (3) | Zenodo [14607156](https://zenodo.org/records/14607156) (context), [14638780](https://zenodo.org/records/14638780) (perturbation); figshare mirrors | Metrics: MSE, PCC-delta, E-distance, Wasserstein, KL, common DEGs. Splits are reusable as-is. |
| [PerturBench](https://arxiv.org/abs/2408.10609) (Altos, NeurIPS 2025) | Platform + linear and latent-additive baselines + rank metric for posterior collapse | Norman, Srivatsan (sciPlex3), Frangieh, McFaline-Figueroa, Jiang | Their Linear Additive and Latent Additive are the right floor respondents for us. |
| [Systema](https://www.nature.com/articles/s41587-025-02777-8) (Nat Biotech 2025; [code](https://github.com/mlbio-epfl/systema)) | Shows mean-shift baselines match SOTA on 10 genetic datasets because of systematic variation; proposes perturbed-centroid reference metrics | 10 datasets, 3 technologies, 5 cell lines | Their systematic-variation measure is a natural item covariate: items dominated by the shared shift are the "everyone passes" items. |
| [scArchon](https://link.springer.com/article/10.1186/s13059-026-04104-z) (Genome Biol 2026; [code](https://github.com/hdsu-bioquant/scArchon)) | Snakemake pipeline for non-genetic perturbation models (scGen, CPA, trVAE, scPRAM, scVIDR, CellOT, ...) | 6 datasets | Flags that good aggregate scores can hide lost perturbation signatures; gene-level checks. |
| [PertEval-scFM](https://proceedings.mlr.press/v267/wenteler25a.html) (ICML 2025; [code](https://github.com/aaronwtr/PertEval)) | Zero-shot scFM embeddings + fixed MLP probe for perturbation effect prediction | Norman (105 single, 91 double) | The "fixed probe on frozen embedding" protocol is what keeps model comparisons fair; reuse it. |
| [Ahlmann-Eltze, Huber, Anders](https://www.nature.com/articles/s41592-025-02772-6) (Nat Methods 2025; [Zenodo 16092690](https://zenodo.org/records/16092690)) | PCA + linear model baseline beats 5 scFMs and 2 DL models | Adamson, Norman (via scFoundation), Replogle K562 (via GEARS) | Their baseline is literally the PCA-regression respondent in your plan. Code is public. |
| [Calibrated-metrics rebuttal](https://www.nature.com/articles/s41587-026-03307-w) (Nat Biotech 2026; [preprint](https://www.biorxiv.org/content/10.1101/2025.10.20.683304v1)) | Argues DL models do beat mean, control, and linear baselines on Replogle K562 under calibrated metrics | Norman19, Replogle22 K562 | Metric choice flips the conclusion. For IRT, define item correctness relative to a baseline, not via a raw metric. |
| [In-the-wild VCM benchmark](https://arxiv.org/abs/2604.27646) (arXiv, Apr 2026) | 3 linear + 8 DL methods (incl. STATE), 14 metrics in 3 families, unseen-cell and unseen-perturbation splits incl. scFM-cluster holdouts | 7 scPerturb datasets: McFarland2020, Kang2018, Adamson (2), Norman2019, Replogle K562, sciPlex3 | No model dominates; DEG-level predictions near zero correlation. Splits are documented and reusable. |
| [Empirical Comparison of VCMs](https://www.researchsquare.com/article/rs-10434123/v1) (Research Square, Jul 2026) | 11 methods, 5 families, 6 task families (genetic single, combinatorial, chemical, cross-context, annotation, batch integration), 9 datasets | not extracted (page blocked) | Only suite covering both A and B with one protocol. Headline: on unseen single-gene perturbations State is +26% over cell-mean, linear +19%, GEARS +22%. |
| [cz-benchmarks](https://chanzuckerberg.github.io/cz-benchmarks/) (CZI + NVIDIA, Oct 2025) | Python package, 6 tasks: clustering (ARI, NMI, silhouette), label prediction (macro F1 etc.), cross-species integration, cross-species label prediction, sequential organization, genetic perturbation prediction (in progress) | Tabula Sapiens v2 (>500k), Spermatogenesis (11 species), Replogle K562 essentials (310,385), Sound of Life PBMC (>13M), Human Kidney Disease (304,652), Mouse Kidney (309,666) | Best ready-made component-A task definitions; also a CLI to pull datasets. |
| [Open Problems](https://openproblems.bio/datasets) | Batch integration, label projection, denoising, OP3 perturbation prediction | 6 Census-derived (Diabetic Kidney Disease, GTEx v9, HypoMap, Immune Cell Atlas, Mouse Pancreatic Islet Atlas, Tabula Sapiens), 9 v1 classics (PBMC, pancreas, zebrafish), ~50 spatial | OP3: 146 compounds on human PBMC, (cell type, compound) holdouts; 6 methods + 6 controls on the live leaderboard. |
| [VCBench](https://www.biorxiv.org/content/10.64898/2026.06.18.733146v1.full.pdf) (bioRxiv, Jun 2026) | 7 capability axes (perturbation, cross-species, GRN, modality integration, temporal, multi-scale, in-silico experiments), 5 scFMs | | Useful taxonomy; not a data source. |
| [pertpy](https://pertpy.scverse.org/en/latest/api/datasets_index.html) | 56 one-call loaders | Adamson, Dixit, Norman, Replogle (3), Frangieh, Gasperini, Tian, Datlinger, Papalexi, Kang, McFarland, sciPlex 2/3/4, combosciplex, Schiebinger, Weinreb, Shifrut, Xie, Zhao, ... | Fastest way to assemble the first 20 datasets. |

## 2. Component B: perturbation (transition) datasets

### 2a. Genetic perturbation

| Dataset | Context | Scale | Access / license | Notes |
|---|---|---|---|---|
| Replogle 2022 K562 genome-wide | K562, CRISPRi, day 8 | ~2.0M cells, ~9.9k genes (verify) | scPerturb; pertpy `replogle_2022_k562_gwps`; figshare Plus | In nearly every FM training set. |
| Replogle 2022 K562 essential | K562, CRISPRi, day 7 | 310,385 cells, ~2k genes | pertpy; cz-benchmarks | Standard "unseen perturbation" split source. |
| Replogle 2022 RPE1 essential | RPE1, CRISPRi, day 7 | ~250k cells, ~2.4k genes (verify) | pertpy `replogle_2022_rpe1` | Only non-cancer line among the classics. |
| Norman 2019 | K562, CRISPRa, single + double | ~106k cells; 105 single, ~131 double (filtering varies by paper) | scPerturb; pertpy | The combinatorial benchmark. Perturbation counts differ across papers; fix one filtering and document it. |
| Adamson 2016 | K562, CRISPRi, UPR | ~65k cells, 82 genes (plus 7-gene pilot) | scPerturb; pertpy | Small; good anchor candidate because every method has been run on it. |
| Dixit 2016 | K562 + mouse BMDCs, CRISPR KO | (verify) | pertpy | First Perturb-seq. |
| Frangieh 2021 | Melanoma co-culture, Perturb-CITE-seq | ~218k cells, 750 perturbations, RNA + protein | pertpy (rna / protein / raw) | Multi-modal readout, immune context. |
| Papalexi 2021 | THP-1, ECCITE-seq | 11 gRNAs | pertpy | Small. |
| Tian 2019 / 2021 | iPSC and iPSC-derived neurons, CRISPRi/a | ~20k to ~98k cells, 58 to 374 gRNAs | pertpy | Neuronal context, missing from most suites. |
| Gasperini 2019 | K562, enhancer CRISPRi | ~255k cells, 1,119 candidate enhancers | pertpy | Non-coding perturbations; different item type. |
| [Virtual Cell Challenge 2025](https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up) | H1 hESC, CRISPRi, 10x Flex | ~300k cells, 300 perturbations, >50k UMIs/cell, ~1,000 cells/pert | Arc Virtual Cell Atlas | Purpose-built, distribution-shifted from K562/A375. Metrics: MAE, DES, PDS. Winners did not consistently beat naive baselines. Check whether the held-out test labels are now public. |
| [Virtual Cell Challenge 2026](https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge-2026) ([Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(26)00931-1)) | 6 cell lines (not named on the data page), CRISPRi, 10x Flex, Ultima UG100 | >30M cells, >10k knockdowns per line, 100 NT controls, ~20k UMIs/cell, curated to 400 cells/pert | [virtualcellchallenge.org](https://virtualcellchallenge.org) | Zero-shot: participants see only unperturbed profiles per line. This is the clean held-out set for 2026 and the natural "acquisition" round for a living benchmark. Timeline not on the page; check the site. |
| [X-Atlas/Orion](https://www.biorxiv.org/content/10.1101/2025.06.11.659105.full.pdf) (Xaira, Jun 2025) | HCT116 + HEK293T, genome-wide CRISPRi, FiCS | ~8M cells, all ~20k protein-coding genes, >16k UMIs/cell; sgRNA UMI gives dose | [figshare Plus 29190726](https://doi.org/10.25452/figshare.plus.29190726), ~520 GB; reported non-commercial license (verify on record) | Dose-response items are unique to this set. |
| [Zhu et al. 2025](https://www.biorxiv.org/content/10.64898/2025.12.23.696273.full.pdf) (Marson lab, Dec 2025) | Primary human CD4+ T cells, 4 donors, CRISPRi, 10x Flex | all 12,748 expressed genes; cell count reported inconsistently (verify) | accession not found; check Data Availability | First genome-scale primary-cell Perturb-seq. Donor axis is new. |
| [VIPerturb-seq](https://www.biorxiv.org/content/10.64898/2026.02.12.705613v1.full) (Bradu et al., Feb 2026) | Genome-wide CRISPRi (GuEST-List), two screens | (verify) | preprint; accession not found | Platform paper; 50x throughput claim. |
| KOLF2.1J iPSC CRISPRi atlas | iPSC | (verify) | figshare Plus 27261219, CC BY 4.0; HF mirror | Not verified beyond a search snippet. |

### 2b. Chemical and other perturbation

| Dataset | Context | Scale | Access / license | Notes |
|---|---|---|---|---|
| [Tahoe-100M](https://www.biorxiv.org/content/10.1101/2025.02.20.639398.full.pdf) (Vevo/Tahoe, Feb 2025) | 50 cancer lines x 1,100+ drugs, Mosaic platform | ~100M cells (95.6M curated), ~60k conditions | h5ad via [Arc Virtual Cell Atlas](https://arcinstitute.org/tools/virtualcellatlas) / [Lamin](https://docs.lamin.ai/arc-virtual-cell-atlas); parquet on [HF tahoebio/Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M); CC0 1.0 (verified) | Largest drug set. Known issue: one HF-derived h5ad had an all-zero counts layer; take counts from Arc. Training data for STATE, Tahoe-x1, TranscriptFormer. |
| Tahoe + Arc + Biohub follow-on | drug x patient-derived models | >120M cells, 225k drug-patient interactions | [announced](https://arcinstitute.org/news/tahoe-arc-biohub), not released | Future acquisition round. |
| sciPlex3 (Srivatsan 2020) | A549, K562, MCF7, 188 compounds, doses | ~650k cells | scPerturb; pertpy `srivatsan_2020_sciplex3` | Standard chemical benchmark (scPerturBench, in-the-wild use 10 uM / 24 h). |
| sciPlex2 / sciPlex4 / combosciplex / sciPlex-GxE | A549, MCF7 | smaller | pertpy | Combinatorial drug and gene x drug items. |
| McFarland 2020 (MIX-seq) | 170 cancer lines, drugs + CRISPRi | ~48k cells (scPerturb subset) | scPerturb; pertpy | Many contexts, few perturbations. |
| OP3 (NeurIPS 2023 / 2024 benchmark) | Human PBMC, 146 compounds | | [openproblems.bio](https://openproblems.bio/results/perturbation_prediction/) | Response is a DE signature, not cells. |
| Kang 2018 | PBMC, 8 lupus patients, IFN-beta | ~11k CD4 T (scPerturb subset) to ~29k total | pertpy | Cytokine stimulation; donor axis. |
| Datlinger 2017 / 2021 | Jurkat (CROP-seq), 4 lines (scifi) | ~6k / ~152k | pertpy | |
| Zhao 2021 | Freshly resected tumor slices, drugs | | pertpy | Ex vivo tissue context. |
| Schiebinger 2019, Weinreb 2020 | Reprogramming / hematopoiesis time courses | 66k to 259k | pertpy | Dynamics items; used by the 2026 trajectory benchmark. |

## 3. Component A: representation datasets

| Dataset | Scale | Access / license | Notes |
|---|---|---|---|
| [Tabula Sapiens v2](https://tabula-sapiens.sf.czbiohub.org/) | ~1.1M cells, 28 tissues, 24 donors; `manually_annotated` flag | portal, [figshare](https://figshare.com/articles/dataset/Tabula_Sapiens_v2/27921984), AWS, CELLxGENE (v1 ingested; v2 verify) | The default annotation benchmark (cz-benchmarks, Open Problems, popV). Expert-verified labels make it the best source of representation items. |
| [CELLxGENE Census](https://chanzuckerberg.github.io/cellxgene-census/) LTS 2025-11-08 | 217M+ total, 125M+ unique cells, 1,845 datasets; human, mouse, marmoset, macaque, chimp | TileDB-SOMA API, CC BY 4.0 | Source for everything scGPT-like trained on. Use for items only with a contamination flag. |
| [scBaseCount](https://arcinstitute.org/tools/virtualcellatlas) (Arc) | >230M cells at launch; "2026-01-12 publication release >502M cells, 27 organisms" per Lamin mirror (verify with Arc) | GCS, CC0 | Agent-reprocessed SRA data; labels are not expert-curated, so weak for annotation items, fine for pretraining or batch items. |
| cz-benchmarks set | Spermatogenesis (11 species), Sound of Life PBMC (>13M), Human Kidney Disease (304,652), Mouse Kidney (309,666) | via VCP CLI | Cross-species and disease-state items. |
| Open Problems Census subsets | Diabetic Kidney Disease, GTEx v9, HypoMap, Immune Cell Atlas, Mouse Pancreatic Islet Atlas | openproblems.bio | Pre-split for batch integration and label projection. |
| Classics | Zheng68K PBMC, Segerstolpe / inDrop pancreas, 1k/5k PBMC, zebrafish | Open Problems, scanpy | Near ceiling for modern models; useful only as easy anchors. |
| HCA / Immune Cell Atlas, Allen Brain Cell Atlas | large | CELLxGENE | Not surveyed in depth. |

## 4. Models to evaluate (for the later phases)

Representation: HVG+PCA (several k), scVI, Harmony, Geneformer, scGPT,
scFoundation, UCE ([Nature 2026](https://www.nature.com/articles/s41586-026-10689-z)),
SCimilarity, TranscriptFormer, Tahoe-x1, TEDDY. Evaluate zero-shot with a
fixed probe. Independent findings to expect: scVI strongest on integration;
HVG+PCA strongest on dynamics; UCE and TranscriptFormer self-reported wins on
annotation and cross-species.

Perturbation: no-change, control-mean, perturbation-mean, Linear Additive,
Latent Additive, DecoderOnly (PerturBench), PCA+linear (Ahlmann-Eltze), CPA,
GEARS, scGen, BioLORD, SAMS-VAE, PRnet, scLAMBDA, GenePert, STATE, chemCPA,
scGPT and scFoundation fine-tuned.

## 5. Implications for the IRT benchmark

- Items are not cells for component B. An item is a (perturbation, context,
  dose, time) condition, and its response is a continuous score. Either
  binarize relative to a baseline ("beats Linear Additive by margin m on this
  item") or use a graded or continuous response model. Raw metrics will not
  do: Systema and the calibrated-metrics paper show rankings flip with the
  metric.
- Items can be cells for component A, but cells within a (dataset, cell type,
  donor) stratum are nearly exchangeable. Treat strata as testlets or sample a
  fixed panel of cells per stratum.
- The linear-baseline literature gives a ready-made ability floor and a
  ready-made set of "saturated" items: anything the control-mean passes is a
  retirement candidate on day one.
- Contamination register is mandatory. Every classic dataset is in the
  pretraining corpora of the models we most want to rank. VCC 2026 held-out
  data is the only clean acquisition this year; design the first "round" around
  it.
- Licenses: Tahoe-100M and scBaseCount are CC0; CELLxGENE and Tabula Sapiens
  are CC BY; X-Atlas/Orion is reported non-commercial (verify before
  redistribution of any merged release).

## Sources

Arc: [VCC 2025 wrap-up](https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up), [VCC 2025 launch](https://arcinstitute.org/news/virtual-cell-challenge-2025), [VCC 2025 behind the data](https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge), [VCC 2026 behind the data](https://arcinstitute.org/news/behind-the-data-virtual-cell-challenge-2026), [VCC 2026 Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(26)00931-1), [VCC 2025 Cell paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00675-0), [Virtual Cell Atlas](https://arcinstitute.org/tools/virtualcellatlas), [Atlas launch](https://arcinstitute.org/news/arc-virtual-cell-atlas-launch), [Tahoe/Arc/Biohub](https://arcinstitute.org/news/tahoe-arc-biohub), [Lamin mirror](https://docs.lamin.ai/arc-virtual-cell-atlas).
Tahoe: [Tahoe-100M preprint](https://www.biorxiv.org/content/10.1101/2025.02.20.639398.full.pdf), [HF dataset](https://huggingface.co/datasets/tahoebio/Tahoe-100M), [counts issue](https://huggingface.co/vevotx/Tahoe-100M-SCVI-v1/discussions/1), [Tahoe-x1](https://www.biorxiv.org/content/10.1101/2025.10.23.683759.full.pdf).
Xaira: [X-Atlas/Orion preprint](https://www.biorxiv.org/content/10.1101/2025.06.11.659105.full.pdf), [GEN news](https://www.genengnews.com/topics/artificial-intelligence/xaira-therapeutics-releases-largest-perturb-seq-dataset-to-power-the-virtual-cell/).
CZI: [cz-benchmarks docs](https://chanzuckerberg.github.io/cz-benchmarks/), [assets](https://chanzuckerberg.github.io/cz-benchmarks/assets.html), [VCP benchmarks](https://virtualcellmodels.cziscience.com/benchmarks), [blog](https://chanzuckerberg.com/blog/ai-biology-community-benchmarks/), [workshop report](https://arxiv.org/pdf/2507.10502).
Suites: [scPerturb](https://projects.sanderlab.org/scperturb/), [scPerturb paper](https://pubmed.ncbi.nlm.nih.gov/38279009/), [scPerturBench](https://github.com/bm2-lab/scPerturBench), [PerturBench](https://arxiv.org/abs/2408.10609), [Systema](https://www.nature.com/articles/s41587-025-02777-8), [scArchon](https://link.springer.com/article/10.1186/s13059-026-04104-z), [PertEval-scFM](https://proceedings.mlr.press/v267/wenteler25a.html), [Ahlmann-Eltze 2025](https://www.nature.com/articles/s41592-025-02772-6), [calibrated metrics 2026](https://www.nature.com/articles/s41587-026-03307-w), [in-the-wild 2026](https://arxiv.org/abs/2604.27646), [Empirical Comparison 2026](https://www.researchsquare.com/article/rs-10434123/v1), [Open Problems](https://openproblems.bio/datasets), [OP3](https://proceedings.neurips.cc/paper_files/paper/2024/hash/24c4d51f3ef48dd2dbab78243ecb26a1-Abstract.html), [VCBench](https://www.biorxiv.org/content/10.64898/2026.06.18.733146v1.full.pdf), [pertpy loaders](https://pertpy.scverse.org/en/latest/api/datasets_index.html).
Representation: [Kedzierska 2025](https://link.springer.com/article/10.1186/s13059-025-03574-x), [zero-shot 2026](https://www.biorxiv.org/content/10.64898/2026.08.03.739553v1), [dynamics 2026](https://www.biorxiv.org/content/10.64898/2026.03.10.710748v1.full), [parameter-free 2026](https://arxiv.org/abs/2602.16696), [one PCA rules](https://arxiv.org/pdf/2410.13956), [UCE Nature](https://www.nature.com/articles/s41586-026-10689-z), [TranscriptFormer](https://www.biorxiv.org/content/10.1101/2025.04.25.650731v1.full.pdf), [Tabula Sapiens](https://tabula-sapiens.sf.czbiohub.org/), [TS v2 figshare](https://figshare.com/articles/dataset/Tabula_Sapiens_v2/27921984).
New screens: [Zhu 2025 CD4](https://www.biorxiv.org/content/10.64898/2025.12.23.696273.full.pdf), [VIPerturb-seq](https://www.biorxiv.org/content/10.64898/2026.02.12.705613v1.full), [AssayBench](https://arxiv.org/html/2605.10876v1), [MVCBench](https://www.biorxiv.org/content/10.64898/2026.04.22.720110v1.full.pdf).

# Anatomy of difficulty (v0)

## Component A: what the probe confuses

Ontology coverage of labels by panel: repr_hao_pbmc_l2 0.09, repr_heart_states 0.00, repr_hlca_core_donor 0.06, repr_hlca_core_study 0.06, repr_immune_atlas_donor 0.06, repr_immune_atlas_tissue 0.07, repr_parse_pbmc_celltype 0.19, repr_pool_v0 0.99, repr_scbasecount_human200_blood 1.00, repr_scbasecount_human200_bone_marrow 1.00, repr_scbasecount_human200_liver 1.00, repr_scbasecount_human200_lung 1.00, repr_scbasecount_human200_multitissue 1.00, repr_scbasecount_human200_skin 1.00

Share of wrong predictions within ontology distance 2 of the true label (sibling, parent or child): 0.22

| covariate | Spearman rho | p | n |
|---|---|---|---|
| difficulty_vs_nearest_label_dist | -0.083 | 0.0e+00 | 257995 |
| difficulty_vs_depth | 0.158 | 0.0e+00 | 257995 |
| difficulty_vs_log_train_support | -0.005 | 3.2e-03 | 370341 |

Items passed by nobody: n=52890, median confusion distance 5.0 (others 6.0), median depth 5.0 (others 5.0)

Variance of cell difficulty explained by cell type / stratum, per panel:

| panel | R2 type | R2 stratum | n |
|---|---|---|---|
| repr_hao_pbmc_l2 | 0.50 | 0.52 | 7798 |
| repr_heart_states | 0.31 | 0.48 | 13310 |
| repr_hlca_core_donor | 0.37 | 0.50 | 10827 |
| repr_hlca_core_study | 0.36 | 0.49 | 30839 |
| repr_immune_atlas_donor | 0.38 | 0.48 | 19998 |
| repr_immune_atlas_tissue | 0.49 | 0.56 | 21829 |
| repr_parse_pbmc_celltype | 0.38 | 0.42 | 16637 |
| repr_pool_v0 | 0.50 | 0.66 | 17756 |
| repr_scbasecount_human200_blood | 0.39 | 0.63 | 41284 |
| repr_scbasecount_human200_bone_marrow | 0.08 | 0.51 | 35613 |
| repr_scbasecount_human200_liver | 0.19 | 0.55 | 14890 |
| repr_scbasecount_human200_lung | 0.25 | 0.49 | 60204 |
| repr_scbasecount_human200_multitissue | 0.34 | 0.63 | 53648 |
| repr_scbasecount_human200_skin | 0.34 | 0.53 | 25708 |

Hardest cell types (mean difficulty, pooled scale), with the dominant confusion:

| panel | cell type | n | mean diff | nobody | top confusion | share | CL dist | nearest label dist |
|---|---|---|---|---|---|---|---|---|
| scbasecount_human200_multitissue | pericyte | 204 | +3.06 | 0.93 | endothelial cell | 0.30 | 3.0 | 3.0 |
| hlca_core_donor | SM activated stress response | 100 | +3.02 | 0.91 | Smooth muscle | 0.98 | nan | nan |
| pool_v0 | regular atrial cardiac myocyte | 75 | +3.00 | 0.96 | ventricular cardiac muscle cell | 0.95 | 3.0 | 3.0 |
| pool_v0 | melanocyte | 50 | +2.96 | 0.72 | schwann cell | 0.54 | 5.0 | 2.0 |
| hlca_core_donor | Goblet (bronchial) | 100 | +2.85 | 0.67 | Goblet (nasal) | 0.54 | nan | nan |
| scbasecount_human200_multitissue | monocyte | 4050 | +2.76 | 0.93 | macrophage | 0.67 | 2.0 | 1.0 |
| immune_atlas_tissue | Cycling | 401 | +2.69 | 0.69 | MNP/T doublets | 0.43 | nan | nan |
| scbasecount_human200_skin | mature NK T cell | 47 | +2.64 | 0.83 | CD8-positive, alpha-beta T cell | 1.00 | 2.0 | 2.0 |
| pool_v0 | mural cell | 100 | +2.63 | 0.56 | smooth muscle cell | 0.47 | 3.0 | 1.0 |
| scbasecount_human200_blood | hematopoietic precursor cell | 239 | +2.63 | 0.82 | CD4-positive, alpha-beta T cell | 0.51 | 8.0 | 3.0 |
| hlca_core_study | Goblet (bronchial) | 100 | +2.63 | 0.51 | Goblet (nasal) | 0.89 | nan | nan |
| scbasecount_human200_bone_marrow | classical monocyte | 425 | +2.60 | 0.84 | monocyte | 0.95 | 1.0 | 1.0 |
| scbasecount_human200_bone_marrow | basophil | 302 | +2.57 | 0.87 | monocyte | 0.38 | 3.0 | 2.0 |
| scbasecount_human200_bone_marrow | neutrophil | 100 | +2.57 | 0.96 | monocyte | 0.83 | 3.0 | 2.0 |
| pool_v0 | myeloid dendritic cell | 57 | +2.56 | 0.84 | macrophage | 0.42 | 2.0 | 1.0 |
| pool_v0 | naive thymus-derived cd8-positive, alpha-beta t cell | 84 | +2.53 | 0.71 | cd8-positive, alpha-beta t cell | 0.57 | 1.0 | 1.0 |
| scbasecount_human200_multitissue | regulatory T cell | 241 | +2.48 | 0.64 | CD4-positive, alpha-beta T cell | 0.72 | 2.0 | 2.0 |
| scbasecount_human200_multitissue | T cell | 2740 | +2.47 | 0.71 | CD8-positive, alpha-beta T cell | 0.35 | 3.0 | 2.0 |
| pool_v0 | cd4-positive, alpha-beta thymocyte | 50 | +2.43 | 0.84 | cd4-positive, alpha-beta t cell | 0.80 | 4.0 | 2.0 |
| scbasecount_human200_multitissue | basal cell | 960 | +2.42 | 0.26 | basal cell of prostate epithelium | 0.51 | 6.0 | 3.0 |
| scbasecount_human200_blood | mature NK T cell | 929 | +2.35 | 0.73 | natural killer cell | 0.44 | 7.0 | 2.0 |
| immune_atlas_donor | GC_B (II) | 29 | +2.35 | 0.52 | Naive B cells | 0.59 | nan | nan |
| scbasecount_human200_lung | mature NK T cell | 873 | +2.33 | 0.78 | CD8-positive, alpha-beta T cell | 0.51 | 2.0 | 2.0 |
| pool_v0 | activated cd8-positive, alpha-beta t cell | 100 | +2.33 | 0.40 | cd8-positive, alpha-beta t cell | 0.97 | 1.0 | 1.0 |
| pool_v0 | mesenchymal stem cell of adipose tissue | 100 | +2.29 | 0.55 | fibroblast | 0.82 | 4.0 | 1.0 |
| pool_v0 | colon macrophage | 50 | +2.22 | 0.62 | macrophage | 0.94 | 1.0 | 1.0 |
| scbasecount_human200_bone_marrow | mature NK T cell | 90 | +2.18 | 0.92 | hematopoietic stem cell | 0.38 | 8.0 | 2.0 |
| pool_v0 | muscle cell | 50 | +2.18 | 0.22 | fast muscle cell | 0.84 | 5.0 | 2.0 |
| pool_v0 | intermediate monocyte | 104 | +2.17 | 0.46 | macrophage | 0.54 | 3.0 | 1.0 |
| pool_v0 | innate lymphoid cell | 66 | +2.14 | 0.61 | mature nk t cell | 0.41 | 5.0 | 2.0 |

## Component B: weak perturbation, weak reaction, or generic reaction

Bins: {'no_reaction': 'fewer than 10 genes with |z|>3, or a genetic target measured but not reduced (on-target log1p change > -0.1)', 'generic': 'cosine to the leave-one-out context mean shift >= 0.8', 'specific': 'otherwise'}

### pooled scale (n=88164)

| bin | n | mean difficulty | nobody | pass rate |
|---|---|---|---|---|
| generic | 1331 | -0.44 | 0.26 | 0.181 |
| no_reaction | 3371 | -1.34 | 0.18 | 0.340 |
| specific | 83462 | -0.87 | 0.23 | 0.241 |

| covariate | Spearman rho | p | n |
|---|---|---|---|
| n_resp_genes | -0.057 | 9.5e-50 | 67855 |
| cos_generic | 0.271 | 0.0e+00 | 67855 |
| delta_l2 | -0.0 | 9.4e-01 | 67855 |
| on_target_lfc | 0.005 | 5.5e-01 | 12453 |
| target_ctrl_mean | 0.014 | 1.1e-01 | 12453 |
| n_cells | -0.026 | 9.2e-12 | 67855 |
| dose | -0.158 | 7.4e-234 | 42180 |

Transcription-factor targets vs others (genetic screens): {False: {'size': 13062, 'mean': -1.459}, True: {'size': 1869, 'mean': -2.146}}, Mann-Whitney p=1.4050572872166122e-44
Target in the K562 essential screen vs not: {False: {'size': 8443, 'mean': -1.679}, True: {'size': 6488, 'mean': -1.371}}

### pooled_context scale (n=71897)

| bin | n | mean difficulty | nobody | pass rate |
|---|---|---|---|---|
| generic | 1074 | +2.70 | 0.04 | 0.319 |
| no_reaction | 342 | +4.04 | 0.33 | 0.146 |
| specific | 70481 | -0.20 | 0.02 | 0.634 |

| covariate | Spearman rho | p | n |
|---|---|---|---|
| n_resp_genes | -0.424 | 0.0e+00 | 70511 |
| cos_generic | 0.512 | 0.0e+00 | 70511 |
| delta_l2 | -0.095 | 1.8e-141 | 70511 |
| on_target_lfc | 0.145 | 1.9e-03 | 453 |
| target_ctrl_mean | -0.127 | 6.6e-03 | 453 |
| n_cells | -0.366 | 0.0e+00 | 70511 |
| dose | -0.149 | 2.2e-278 | 56654 |

Transcription-factor targets vs others (genetic screens): {False: {'size': 453, 'mean': 3.47}, True: {'size': 38, 'mean': 3.445}}, Mann-Whitney p=0.3001800221198504
Target in the K562 essential screen vs not: {False: {'size': 442, 'mean': 3.695}, True: {'size': 49, 'mean': 1.42}}


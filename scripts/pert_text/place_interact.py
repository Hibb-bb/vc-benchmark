#!/usr/bin/env python
"""Place the interaction models (interaction_eval.py) on the dataset's unseen-combination scale and compare twins.

  .venv/bin/python scripts/pert_text/place_interact.py --scores runs/pert_text/interact_idict --pub-run pert_idict_v0 \
      --dataset immune_dictionary
  .venv/bin/python scripts/pert_text/place_interact.py --scores runs/pert_text/interact --pub-run pert_pool_v0 \
      --dataset parse_pbmc_cytokines

Anchored placement (item difficulties fixed at runs/<pub-run>/rasch/<dataset>.context.difficulties.csv), as for every
added respondent. Writes <scores>/summary.md and <scores>/abilities.csv: the new models next to the published
respondents of the scale and each text model next to its no-text twin.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_rasch
from vcb.names import plain_name
from vcb.scoring import binarize

ap = argparse.ArgumentParser()
ap.add_argument("--scores", required=True)
ap.add_argument("--pub-run", required=True)
ap.add_argument("--dataset", required=True)
a = ap.parse_args()
S = Path(a.scores)
tag = f"{a.dataset}.context"
sc = pd.read_parquet(S / f"{tag}.scores.parquet")
new_ids = sorted(r for r in sc["respondent_id"].unique() if r != "mean_shift")
b = binarize(sc)
b = b[b["respondent_id"].isin(new_ids)]
diff = pd.read_csv(RUNS / a.pub_run / "rasch" / f"{tag}.difficulties.csv").set_index("item_id")
d = diff.loc[~diff["degenerate"], "difficulty"]
tot = b.groupby("respondent_id")["k"].agg(["sum", "size"])
b = b[b["item_id"].isin(d.index)]
items = pd.Index(sorted(d.index))
rs = pd.Index(sorted(b["respondent_id"].unique()))
K = np.zeros((len(rs), len(items))); N = np.zeros_like(K)
np.add.at(K, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["k"].values)
np.add.at(N, (rs.get_indexer(b["respondent_id"]), items.get_indexer(b["item_id"])), b["n"].values)
theta, se, _, _, info = fit_rasch(K, N, anchors={i: float(d[it]) for i, it in enumerate(items)}, n_iter=300)
new = pd.DataFrame({"respondent_id": rs, "ability": theta, "se": se, "p_correct": (tot["sum"] / tot["size"]).reindex(rs).values,
                    "source": "new"})
pub = pd.read_csv(RUNS / a.pub_run / "rasch" / f"{tag}.abilities.csv")
pub = pub[~pub["respondent_id"].astype(str).str.contains("_txt|_g(?:scgpt|geneformer|scfoundation|esm2|ctrlpca)$", regex=True)]
pub = pub.assign(source="published")[["respondent_id", "ability", "se", "p_correct", "source"]]
allr = pd.concat([pub, new], ignore_index=True).sort_values("ability", ascending=False).reset_index(drop=True)
allr["rank"] = np.arange(1, len(allr) + 1)
allr.to_csv(S / "abilities.csv", index=False)

m = new.set_index("respondent_id")["ability"]
s = new.set_index("respondent_id")["se"]
rows = []
for r in m.index:
    if "txt" in r or "both" in r:
        twin = r.replace("txt", "resp").replace("both", "resp")
        rows.append((r, m[r], s[r], twin, m.get(twin, np.nan)))
best_pub = pub.sort_values("ability", ascending=False).iloc[0]
lines = [f"# Text-enhanced interaction models, {a.dataset}, unseen-combination split", "",
         f"Best published model: {plain_name(best_pub.respondent_id)} ({best_pub.respondent_id}) {best_pub.ability:+.2f}; "
         f"additive two-way model {m.get('additive', np.nan):+.2f}.", "",
         "| text model | ability ± se | no-text twin | twin ability | text − twin |", "|---|---|---|---|---|"]
for r, v, e, tw, tv in rows:
    lines.append(f"| {r} | {v:+.2f} ± {e:.2f} | {tw} | {tv:+.2f} | {v - tv:+.2f} |")
lines += ["", "## Full ranking (published respondents and new models)", "", "| rank | model | source | ability | pass |", "|---|---|---|---|---|"]
for r in allr.itertuples():
    lines.append(f"| {r.rank} | {r.respondent_id} | {r.source} | {r.ability:+.2f} | {r.p_correct:.0%} |")
(S / "summary.md").write_text("\n".join(lines))
print("\n".join(lines[:12 + len(rows)]))

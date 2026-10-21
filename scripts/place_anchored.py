#!/usr/bin/env python
"""Place new respondents on an existing representation scale without refitting it.

Item difficulties are held at the values in `runs/<run>/rasch/<tag>.difficulties.csv` and only the
abilities of the given respondents are estimated (JML with every item anchored, same priors as the
full fit). Rows are added to, or replaced in, `<tag>.abilities.csv` with `placement = anchored`;
rows that came from the full fit are marked `refit`. Published abilities do not move.

  python scripts/place_anchored.py repr --run repr_hao_pbmc_l2 --respondents fm_uce,fm_state
  python scripts/place_anchored.py repr --run repr_hao_pbmc_l2 --respondents auto   # every respondent in responses.parquet not yet in the abilities table
  python scripts/place_anchored.py repr --run repr_pooled_v3 --respondents fm_uce --pool-runs repr_hao_pbmc_l2,repr_ts2   # pooled scale: gather the rows from the panel runs

The next full refit (`fit_rasch.py repr --run ...`) re-estimates everything and advances the version.
"""
import argparse

import numpy as np
import pandas as pd

from vcb import RUNS
from vcb.irt.rasch import fit_rasch

ap = argparse.ArgumentParser()
ap.add_argument("component", choices=["repr"])
ap.add_argument("--run", required=True)
ap.add_argument("--respondents", required=True, help="comma-separated respondent ids, or 'auto'")
ap.add_argument("--pool-runs", default=None, help="for a pooled run: panel runs to gather the respondents' rows from (item ids are namespaced by run)")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()

run = RUNS / a.run
rasch = run / "rasch"


def gather(resps: list[str] | None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """responses (optionally only for resps) and items for this run, namespaced when pooled."""
    if a.pool_runs:
        L, I = [], []
        for r in a.pool_runs.split(","):
            lr = pd.read_parquet(RUNS / r / "responses.parquet")
            if resps is not None:
                lr = lr[lr["respondent_id"].isin(resps)]
            lr["item_id"] = r + "::" + lr["item_id"].astype(str)
            ir = pd.read_parquet(RUNS / r / "items.parquet")[["stratum"]]
            ir.index = r + "::" + ir.index.astype(str); ir["stratum"] = r + "::" + ir["stratum"].astype(str)
            L.append(lr); I.append(ir)
        return pd.concat(L, ignore_index=True), pd.concat(I)
    long = pd.read_parquet(run / "responses.parquet")
    if resps is not None:
        long = long[long["respondent_id"].isin(resps)]
    return long, pd.read_parquet(run / "items.parquet")[["stratum"]]


def place(long: pd.DataFrame, tag: str) -> pd.DataFrame:
    diff = pd.read_csv(rasch / f"{tag}.difficulties.csv").set_index("item_id")
    diff = diff.loc[~diff["degenerate"], "difficulty"]
    tot = long.groupby("respondent_id")[["k", "n"]].sum()   # pass rate over every item, as the full fit reports it
    n_all = long.groupby("respondent_id")["item_id"].nunique()
    long = long[long["item_id"].isin(diff.index)]
    items = pd.Index(sorted(long["item_id"].unique()))
    resps = pd.Index(sorted(long["respondent_id"].unique()))
    K = np.zeros((len(resps), len(items))); N = np.zeros_like(K)
    np.add.at(K, (resps.get_indexer(long["respondent_id"]), items.get_indexer(long["item_id"])), long["k"].values)
    np.add.at(N, (resps.get_indexer(long["respondent_id"]), items.get_indexer(long["item_id"])), long["n"].values)
    theta, se, _, _, info = fit_rasch(K, N, anchors={i: float(diff[it]) for i, it in enumerate(items)}, n_iter=300)
    return pd.DataFrame({"respondent_id": resps, "ability": theta, "se": se, "outfit": info["outfit_resp"], "n_items": n_all.reindex(resps).values,
                         "p_correct": (tot["k"] / tot["n"].clip(lower=1)).reindex(resps).values, "placement": "anchored"})


abil0 = pd.read_csv(rasch / "cell_level.abilities.csv")
if a.respondents == "auto":
    present = gather(None)[0]["respondent_id"].unique() if not a.pool_runs else pd.concat([pd.read_parquet(RUNS / r / "responses.parquet", columns=["respondent_id"]) for r in a.pool_runs.split(",")])["respondent_id"].unique()
    resps = sorted(set(present) - set(abil0["respondent_id"]))
else:
    resps = a.respondents.split(",")
if not resps:
    raise SystemExit("[place] nothing to place")
print(f"[place] {a.run}: anchoring {len(resps)} respondent(s) to the current difficulties: {', '.join(resps)}", flush=True)

long, items = gather(resps)
missing = set(resps) - set(long["respondent_id"])
if missing:
    raise SystemExit(f"[place] no responses for: {sorted(missing)}")
if a.pool_runs and not a.dry_run:
    # keep the pooled response table complete so the next full refit includes these rows
    pooled = pd.read_parquet(run / "responses.parquet")
    pooled = pd.concat([pooled[~pooled["respondent_id"].isin(resps)], long], ignore_index=True)
    pooled.to_parquet(run / "responses.parquet", index=False)

strat = long.merge(items.astype(str), left_on="item_id", right_index=True)
strat = strat.groupby(["stratum", "respondent_id"])[["k", "n"]].sum().reset_index().rename(columns={"stratum": "item_id"})
for tag, df in [("cell_level", long), ("stratum_binomial", strat)]:
    if not (rasch / f"{tag}.difficulties.csv").exists():
        continue
    new = place(df, tag)
    old = pd.read_csv(rasch / f"{tag}.abilities.csv")
    if "placement" not in old.columns:
        old["placement"] = "refit"
    prev = old.set_index("respondent_id")["ability"].reindex(new["respondent_id"])
    for r in new.itertuples():
        was = f" (was {prev[r.respondent_id]:+.2f})" if np.isfinite(prev[r.respondent_id]) else ""
        print(f"  {tag:17s} {r.respondent_id:28s} ability {r.ability:+.3f} ± {r.se:.3f}  pass {r.p_correct:.3f}  outfit {r.outfit:.2f}  items {r.n_items}{was}", flush=True)
    merged = pd.concat([old[~old["respondent_id"].isin(new["respondent_id"])], new], ignore_index=True).sort_values("ability", ascending=False)
    if not a.dry_run:
        merged.to_csv(rasch / f"{tag}.abilities.csv", index=False)
print("[place] dry run, nothing written" if a.dry_run else "[place] abilities tables updated; difficulties unchanged", flush=True)

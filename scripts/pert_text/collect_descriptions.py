#!/usr/bin/env python
"""Step 1-2 of the text perturbation encoder: inventory every perturbation and write a text card for it.

  .venv/bin/python scripts/pert_text/collect_descriptions.py        # needs network (mygene.info, PubChem)

Output (runs/pert_text/):
  perturbations.parquet   one row per (perturbation, type): datasets, targets, contexts, doses, sources
  cards.jsonl             {key, name, type, text_full, text_name}: the text to embed
  gene_info.parquet, drug_info.parquet   raw facts pulled from the databases (cached, re-used on rerun)

Text comes from curated sources, not from a language model: NCBI Gene summaries and GO biological
process terms (via mygene.info) for genes, Tahoe's drug table, sciPlex3's target/pathway labels and
PubChem descriptions for drugs, and the ligand/receptor/family table for cytokines. Cards describe what a
perturbation *is*; they never include how cells responded in our data, so the embedding cannot leak
the benchmark's answers.
"""
import json
import time
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
import urllib.error
import urllib.parse
import urllib.request


def http_json(url, data=None, timeout=60):
    """GET (or form POST when data is given) and parse JSON; None on HTTP errors."""
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers={"User-Agent": "vc-benchmark/0.1 (academic research)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "runs" / "pert_pool_v0"
OUT = ROOT / "runs" / "pert_text"
OUT.mkdir(parents=True, exist_ok=True)
TYPE_TEXT = {"CRISPRi": "CRISPR interference knockdown (gene expression reduced)", "CRISPR_KO": "CRISPR knockout (gene disrupted)",
             "CRISPRa": "CRISPR activation (gene expression increased)", "drug": "small-molecule compound", "cytokine": "recombinant cytokine (extracellular signalling protein)"}

# ---------- inventory ----------
rows = []
for f in sorted(RUN.glob("*.perturbation.items.parquet")):
    it = pd.read_parquet(f)
    ds = str(it["dataset_id"].iloc[0])
    it = it[it["pert_type"].astype(str) != "control"]
    g = it.groupby(["perturbation", "pert_type"], observed=True).agg(targets=("targets", "first"), n_contexts=("context", "nunique"),
                                                                      doses=("dose", lambda x: sorted({float(v) for v in x.dropna()}))).reset_index()
    g["dataset"] = ds
    rows.append(g)
inv = pd.concat(rows, ignore_index=True)
inv["perturbation"] = inv["perturbation"].astype(str)
inv["pert_type"] = inv["pert_type"].astype(str)
per = inv.groupby(["perturbation", "pert_type"]).agg(targets=("targets", "first"), datasets=("dataset", lambda x: sorted(set(x))),
                                                     n_contexts=("n_contexts", "sum"), doses=("doses", lambda x: sorted({d for l in x for d in l}))).reset_index()
per["key"] = per["pert_type"] + "::" + per["perturbation"]
print(f"{len(per)} perturbations; {per.pert_type.value_counts().to_dict()}", flush=True)

# ---------- genes: NCBI summary + GO biological process via mygene.info ----------
def genes_of(r):
    t = str(r.targets or "")
    gs = [g for g in t.replace("_", "|").split("|") if g]
    return gs or [g for g in str(r.perturbation).split("_") if g]


per["genes"] = [genes_of(r) if r.pert_type in ("CRISPRi", "CRISPR_KO", "CRISPRa") else [] for r in per.itertuples()]
cyt = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False).set_index("cytokine")
lig = {c: [g for g in r["ligand_genes"].split(",") if g] for c, r in cyt.iterrows()}
rec = {c: [g for g in r["receptor_genes"].split(",") if g] for c, r in cyt.iterrows()}
all_genes = sorted({g for gs in per["genes"] for g in gs} | {g for v in lig.values() for g in v} | {g for v in rec.values() for g in v})
gcache = OUT / "gene_info.parquet"
ginfo = pd.read_parquet(gcache) if gcache.exists() else pd.DataFrame(columns=["symbol", "name", "summary", "go_bp"]).set_index("symbol")
todo = [g for g in all_genes if g not in ginfo.index]
print(f"genes: {len(all_genes)} needed, {len(todo)} to fetch", flush=True)
new = []
for i in range(0, len(todo), 1000):
    batch = todo[i:i + 1000]
    res = http_json("https://mygene.info/v3/query", data={"q": ",".join(batch), "scopes": "symbol,alias", "species": "human",
                                                          "fields": "symbol,name,summary,go.BP.term", "size": 1}, timeout=180)
    if res is None:
        raise SystemExit("mygene.info query failed")
    seen = set()
    for h in res:
        q = h.get("query")
        if q in seen or h.get("notfound"):
            continue
        seen.add(q)
        bp = h.get("go", {}).get("BP", []) if isinstance(h.get("go"), dict) else []
        bp = [bp] if isinstance(bp, dict) else bp
        terms = list(dict.fromkeys(b.get("term") for b in bp if isinstance(b, dict) and b.get("term")))[:8]
        new.append({"symbol": q, "name": h.get("name", ""), "summary": h.get("summary", ""), "go_bp": "; ".join(terms)})
    print(f"  genes {i + len(batch)}/{len(todo)}", flush=True)
    time.sleep(0.5)
if new:
    ginfo = pd.concat([ginfo, pd.DataFrame(new).set_index("symbol")])
    ginfo = ginfo[~ginfo.index.duplicated()]
    ginfo.to_parquet(gcache)

# ---------- drugs ----------
tahoe = pd.read_parquet(ROOT / "data" / "raw" / "tahoe" / "meta" / "drug_metadata.parquet").set_index("drug")


def obs_table(path, cols):
    with h5py.File(path, "r") as f:
        o = {}
        for c in cols:
            g = f["obs"][c]
            if isinstance(g, h5py.Group):
                cats = np.array([x.decode() if isinstance(x, bytes) else str(x) for x in g["categories"][:]])
                codes = g["codes"][:]
                o[c] = np.where(codes >= 0, cats[np.clip(codes, 0, None)], "")
            else:
                o[c] = np.array([x.decode() if isinstance(x, bytes) else str(x) for x in g[:]])
    return pd.DataFrame(o).drop_duplicates("perturbation").set_index("perturbation")


sci = obs_table(ROOT / "data" / "raw" / "scperturb" / "SrivatsanTrapnell2020_sciplex3.h5ad", ["perturbation", "target", "pathway", "pathway_level_1"])
mcf = obs_table(ROOT / "data" / "raw" / "scperturb" / "McFarlandTsherniak2020.h5ad", ["perturbation", "chembl-ID"])
dcache = OUT / "drug_info.parquet"
dinfo = pd.read_parquet(dcache) if dcache.exists() else pd.DataFrame(columns=["drug", "cid", "description"]).set_index("drug")
drugs = per.loc[per.pert_type == "drug", "perturbation"].tolist()
PUG = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
for d in drugs:
    if d in dinfo.index:
        continue
    cid = tahoe["pubchem_cid"].get(d) if d in tahoe.index else None
    if cid is None or pd.isna(cid):
        name = d.split(" (")[0]
        j = http_json(f"{PUG}/compound/name/{urllib.parse.quote(name)}/cids/JSON", timeout=30)
        cid = (j or {}).get("IdentifierList", {}).get("CID", [None])[0]
    desc = ""
    if cid:
        j = http_json(f"{PUG}/compound/cid/{int(cid)}/description/JSON", timeout=30)
        infos = [x.get("Description") for x in (j or {}).get("InformationList", {}).get("Information", []) if x.get("Description")]
        desc = infos[0] if infos else ""
    dinfo.loc[d] = [cid, desc]
    time.sleep(0.25)
dinfo.to_parquet(dcache)
print(f"drugs: {len(drugs)}; with PubChem text {int((dinfo.reindex(drugs)['description'].fillna('') != '').sum())}", flush=True)

# ---------- cards ----------
def gene_line(g):
    if g not in ginfo.index:
        return f"{g}: no database entry found."
    r = ginfo.loc[g]
    s = f"{g} ({r['name']})." if r["name"] else f"{g}."
    if r["summary"]:
        s += " " + r["summary"]
    if r["go_bp"]:
        s += " Biological processes: " + r["go_bp"] + "."
    return s


def card(r):
    t, n = r.pert_type, r.perturbation
    head = f"Perturbation: {n}. Type: {TYPE_TEXT.get(t, t)}."
    body = []
    if t in ("CRISPRi", "CRISPR_KO", "CRISPRa"):
        body.append(("Target genes: " if len(r.genes) > 1 else "Target gene: ") + ", ".join(r.genes) + ".")
        body += [gene_line(g) for g in r.genes]
    elif t == "drug":
        if n in tahoe.index:
            m = tahoe.loc[n]
            body.append(f"Targets: {m['targets'] or 'unknown'}. Mechanism of action: {m['moa-fine']} ({m['moa-broad']}). Approved for human use: {m['human-approved']}.")
        if n in sci.index:
            body.append(f"Target: {sci.loc[n, 'target']}. Pathway: {sci.loc[n, 'pathway']} ({sci.loc[n, 'pathway_level_1']}).")
        if n in mcf.index and mcf.loc[n, "chembl-ID"]:
            body.append(f"ChEMBL ID: {mcf.loc[n, 'chembl-ID']}.")
        if n in dinfo.index and dinfo.loc[n, "description"]:
            body.append(str(dinfo.loc[n, "description"]))
    elif t == "cytokine" and n in cyt.index:
        body.append(f"Cytokine family: {cyt.loc[n, 'family']}. Encoded by: {', '.join(lig[n]) or 'unknown'}. Receptor genes: {', '.join(rec[n]) or 'none known'}.")
        body += [gene_line(g) for g in lig[n]]
        body += [f"Receptor {gene_line(g)}" for g in rec[n]]
    facts = f"Measured in {len(r.datasets)} dataset(s): {', '.join(r.datasets)}; {int(r.n_contexts)} cell context(s)."
    if r.doses:
        facts += f" Doses: {', '.join(f'{d:g}' for d in r.doses[:6])}."
    return " ".join([head] + body + [facts])


per["text_full"] = [card(r) for r in per.itertuples()]
per["text_name"] = [f"{r.perturbation} ({TYPE_TEXT.get(r.pert_type, r.pert_type)})" for r in per.itertuples()]
per["n_words"] = per["text_full"].str.split().str.len()
per.drop(columns=["doses"]).to_parquet(OUT / "perturbations.parquet")
with open(OUT / "cards.jsonl", "w") as fh:
    for r in per.itertuples():
        fh.write(json.dumps({"key": r.key, "name": r.perturbation, "type": r.pert_type, "text_full": r.text_full, "text_name": r.text_name}) + "\n")
print(per.groupby("pert_type")["n_words"].describe()[["count", "mean", "50%", "max"]].round(0).to_string())
print("example:", per.loc[per.pert_type == "cytokine", "text_full"].iloc[0][:600])

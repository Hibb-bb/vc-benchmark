#!/usr/bin/env python
"""Text cards for the 86 Immune Dictionary cytokines, in the same template as the Parse cytokine cards.

  .venv/bin/python scripts/pert_text/immune_dictionary_cards.py      # needs network for a few new genes (mygene.info)

The dataset's labels (IL-1α, IFN-γ, 41BBL ...) are mapped to the Parse cytokine table where the cytokine is the same
(79 of 86); the other 7 (AdipoQ, C3a, IFN-κ, IL-18, IL-30, IL-Y, neuropoietin) get hand-curated ligand, receptor and
family entries. Genes are described with human NCBI Gene summaries and GO terms, as for Parse (the cards describe the
cytokine, not the species). Writes src/vcb/data/immune_dictionary_cytokines.tsv and runs/pert_text/idict/cards.jsonl.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "runs" / "pert_text" / "idict"
OUT.mkdir(parents=True, exist_ok=True)
LABELS = ['41BBL', 'ADSF (Resistin)', 'APRIL', 'AdipoQ', 'BAFF', 'C3a', 'C5a', 'CD27L', 'CD30L', 'CD40L', 'CT-1', 'Decorin', 'EGF',
          'FGF-β', 'FLT3L', 'FasL', 'G-CSF', 'GDNF', 'GITRL', 'GM-CSF', 'HGF', 'IFN-α1', 'IFN-β', 'IFN-γ', 'IFN-ε', 'IFN-κ', 'IFN-λ2',
          'IGF-I', 'IL-10', 'IL-11', 'IL-12', 'IL-13', 'IL-15', 'IL-17A', 'IL-17B', 'IL-17C', 'IL-17D', 'IL-17E', 'IL-17F', 'IL-18',
          'IL-19', 'IL-1Ra', 'IL-1α', 'IL-1β', 'IL-2', 'IL-20', 'IL-21', 'IL-22', 'IL-23', 'IL-24', 'IL-27', 'IL-3', 'IL-30', 'IL-31',
          'IL-33', 'IL-34', 'IL-36Ra', 'IL-36α', 'IL-4', 'IL-5', 'IL-6', 'IL-7', 'IL-9', 'IL-Y', 'LIF', 'LIGHT', 'LTA1-B2', 'LTA2-B1',
          'Leptin', 'M-CSF', 'NP', 'Noggin', 'OSM', 'OX40L', 'PRL (Prolactin)', 'PSPN (Persephin)', 'RANKL', 'SCF', 'TGF-β1', 'TL1A',
          'TNF-α', 'TPO', 'TRAIL', 'TSLP', 'TWEAK', 'VEGF']
ALIAS = {"41BBL": "4-1BBL", "IGF-I": "IGF-1", "LTA1-B2": "LT-alpha1-beta2", "LTA2-B1": "LT-alpha2-beta1", "TGF-beta1": "LAP-TGF-beta1"}
NEW = {  # card name, ligand genes, receptor genes, family, receptor complexes
    "AdipoQ": ("Adiponectin", "ADIPOQ", "ADIPOR1,ADIPOR2", "adipokine", "ADIPOR1|ADIPOR2"),
    "C3a": ("C3a", "C3", "C3AR1", "complement", "C3AR1"),
    "IFN-kappa": ("IFN-kappa", "IFNK", "IFNAR1,IFNAR2", "type I interferon", "IFNAR1+IFNAR2"),
    "IL-18": ("IL-18", "IL18", "IL18R1,IL18RAP", "IL-1 family", "IL18R1+IL18RAP"),
    "IL-30": ("IL-30 (IL-27 p28 subunit)", "IL27", "IL6R,IL6ST", "IL-12 family", "IL6R+IL6ST"),
    "IL-Y": ("IL-Y (p28 + p40)", "IL27,IL12B", "IL12RB1,IL27RA", "IL-12 family", "IL12RB1+IL27RA"),
    "NP": ("Neuropoietin", "CTF2P", "CNTFR,LIFR,IL6ST", "IL-6 / gp130", "CNTFR+LIFR+IL6ST"),
}


def norm(s):
    s = re.sub(r" \(.*\)", "", s)
    for g, n in (("α", "-alpha"), ("β", "-beta"), ("γ", "-gamma"), ("ε", "-epsilon"), ("κ", "-kappa"), ("λ", "-lambda")):
        s = s.replace(g, n)
    return ALIAS.get(s.replace("--", "-"), s.replace("--", "-"))


parse = pd.read_csv(ROOT / "src" / "vcb" / "data" / "parse_cytokines.tsv", sep="\t", keep_default_na=False).set_index("cytokine")
rows = []
for lab in LABELS:
    n = norm(lab)
    if n in parse.index:
        r = parse.loc[n]
        rows.append({"label": lab, "cytokine": n, "ligand_genes": r["ligand_genes"], "receptor_genes": r["receptor_genes"],
                     "family": r["family"], "receptor_complexes": r["receptor_complexes"], "in_parse": True})
    else:
        name, lg, rg, fam, cx = NEW[n]
        rows.append({"label": lab, "cytokine": name, "ligand_genes": lg, "receptor_genes": rg, "family": fam,
                     "receptor_complexes": cx, "in_parse": False})
tab = pd.DataFrame(rows)
tab.to_csv(ROOT / "src" / "vcb" / "data" / "immune_dictionary_cytokines.tsv", sep="\t", index=False)
print(f"{len(tab)} cytokines, {int(tab['in_parse'].sum())} shared with Parse")

# gene descriptions (shared cache with the main collection)
gcache = ROOT / "runs" / "pert_text" / "gene_info.parquet"
ginfo = pd.read_parquet(gcache)
genes = sorted({g for c in ("ligand_genes", "receptor_genes") for v in tab[c] for g in v.split(",") if g})
todo = [g for g in genes if g not in ginfo.index]
if todo:
    body = urllib.parse.urlencode({"q": ",".join(todo), "scopes": "symbol", "species": "human",
                                   "fields": "symbol,name,summary,go.BP.term", "size": 1}).encode()
    req = urllib.request.Request("https://mygene.info/v3/query", data=body, headers={"User-Agent": "vc-benchmark/0.1 (academic research)"})
    res = json.loads(urllib.request.urlopen(req, timeout=120).read().decode())
    new, seen = [], set()
    for h in res:
        q = h.get("query")
        if q in seen or h.get("notfound") or h.get("symbol") != q:      # exact symbol only (aliases can name other genes)
            continue
        seen.add(q)
        bp = h.get("go", {}).get("BP", []) if isinstance(h.get("go"), dict) else []
        bp = [bp] if isinstance(bp, dict) else bp
        terms = list(dict.fromkeys(b.get("term") for b in bp if isinstance(b, dict) and b.get("term")))[:8]
        new.append({"symbol": q, "name": h.get("name", ""), "summary": h.get("summary", ""), "go_bp": "; ".join(terms)})
    if new:
        ginfo = pd.concat([ginfo, pd.DataFrame(new).set_index("symbol")])
        ginfo.to_parquet(gcache)
    print(f"fetched {len(new)} of {len(todo)} new genes: {todo}")
    time.sleep(0.5)


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


with open(OUT / "cards.jsonl", "w") as fh:
    for r in tab.itertuples():
        lig = [g for g in r.ligand_genes.split(",") if g]
        rec = [g for g in r.receptor_genes.split(",") if g]
        parts = [f"Perturbation: {r.cytokine}. Type: recombinant cytokine (extracellular signalling protein).",
                 f"Cytokine family: {r.family}. Encoded by: {', '.join(lig) or 'unknown'}. Receptor genes: {', '.join(rec) or 'none known'}."]
        parts += [gene_line(g) for g in lig] + [f"Receptor {gene_line(g)}" for g in rec]
        parts.append("Measured in 1 dataset(s): immune_dictionary (mouse lymph node, in vivo).")
        fh.write(json.dumps({"key": f"cytokine::{r.label}", "name": r.label, "type": "cytokine", "text_full": " ".join(parts),
                             "text_name": f"{r.cytokine} (recombinant cytokine (extracellular signalling protein))"}) + "\n")
print(f"wrote {OUT / 'cards.jsonl'}")

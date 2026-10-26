# Virtual Cell Bench website

Static site, no build step: hand-written HTML pages, one stylesheet (`assets/site.css`), one ES module
(`assets/app.js`, chrome and chart toolkit) plus one small module per data page. Every number and chart
comes from the JSON under `data/`, which `scripts/export_site_data.py` regenerates from `runs/`:

    .venv/bin/python scripts/export_site_data.py     # ~40 s; rewrites site/data/*.json
    cd site && python3 -m http.server 8765           # preview at http://localhost:8765/

Deploy: `scripts/publish_site.sh` re-exports the data, mirrors `site/` into a clone of the public repository
`Hibb-bb/virtual-cell-bench` (kept under `cache/site_repo`), commits and pushes; GitHub Pages serves that
repository's `main` branch at the root. This code repository is private, so Pages cannot serve it directly.
The custom domain is virtual-cell-bench.com (the script writes the `CNAME` file).

Adding a panel or screen: extend `PANELS` / `SCREENS` in the export script, re-run it, and the cards,
boards and item browser pick it up. Adding a respondent: nothing to do beyond a refit; names and
families come from `src/vcb/names.py`.

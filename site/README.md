# Virtual Bench website

Static site, no build step: hand-written HTML pages, one stylesheet (`assets/site.css`), one ES module
(`assets/app.js`, chrome and chart toolkit) plus one small module per data page. Every number and chart
comes from the JSON under `data/`, which `scripts/export_site_data.py` regenerates from `runs/`:

    .venv/bin/python scripts/export_site_data.py     # ~40 s; rewrites site/data/*.json
    cd site && python3 -m http.server 8765           # preview at http://localhost:8765/

Deploy: `.github/workflows/site.yml` uploads `site/` to GitHub Pages on every push to `main` that touches
it (enable Pages with source "GitHub Actions" once in the repository settings). The data JSON is committed;
CI never runs the export because `runs/` responses are not in git.

Adding a panel or screen: extend `PANELS` / `SCREENS` in the export script, re-run it, and the cards,
boards and item browser pick it up. Adding a respondent: nothing to do beyond a refit; names and
families come from `src/vcb/names.py`.

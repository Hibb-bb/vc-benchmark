#!/usr/bin/env bash
# Publish site/ to the public GitHub Pages repository (Hibb-bb/virtual-cell-bench).
#
#   scripts/publish_site.sh            # re-export data, sync site/, commit, push
#   EXPORT=0 scripts/publish_site.sh   # skip the data export
#   DOMAIN=bench.example.org scripts/publish_site.sh   # also write the CNAME file
#
# The public repo holds only the static site (HTML, CSS, JS, JSON, the paper PDF); the code and the
# item bank stay in this private repository. A local clone lives under cache/site_repo (git-ignored).
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
SITE_REPO=${SITE_REPO:-Hibb-bb/virtual-cell-bench}
CLONE=${CLONE:-$ROOT/cache/site_repo}
DOMAIN=${DOMAIN:-virtual-cell-bench.com}
EXPORT=${EXPORT:-1}

if [ "$EXPORT" = 1 ]; then
  echo "exporting site data"
  "$ROOT/.venv/bin/python" "$ROOT/scripts/export_site_data.py"
fi

if [ ! -d "$CLONE/.git" ]; then
  mkdir -p "$(dirname "$CLONE")"
  gh repo clone "$SITE_REPO" "$CLONE"
fi
git -C "$CLONE" fetch -q origin
git -C "$CLONE" checkout -q main 2>/dev/null || git -C "$CLONE" checkout -q -b main
git -C "$CLONE" reset -q --hard origin/main 2>/dev/null || true

# Mirror site/ into the clone root; keep the clone's own .git and README.
rsync -a --delete --exclude .git --exclude README.md --exclude CNAME "$ROOT/site/" "$CLONE/"
touch "$CLONE/.nojekyll"                      # serve folders starting with _ and skip Jekyll
[ -n "$DOMAIN" ] && printf '%s\n' "$DOMAIN" > "$CLONE/CNAME"
cat > "$CLONE/README.md" <<'README'
# Virtual Cell Bench website

Static files for the Virtual Cell Bench site, published with GitHub Pages. Generated from the private
`vc-benchmark` repository by `scripts/publish_site.sh`; do not edit here, edits are overwritten on the
next publish.
README

SRC=$(git -C "$ROOT" rev-parse --short HEAD)
git -C "$CLONE" add -A
if git -C "$CLONE" diff --cached --quiet; then
  echo "site unchanged; nothing to publish"
  exit 0
fi
git -C "$CLONE" commit -q -m "Publish site from vc-benchmark $SRC ($(date -u +%Y-%m-%d))"
git -C "$CLONE" push -q origin main
echo "published $(git -C "$CLONE" rev-parse --short HEAD) to https://github.com/$SITE_REPO"

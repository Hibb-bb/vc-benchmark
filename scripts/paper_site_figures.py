#!/usr/bin/env python
"""Turn the website's explanatory SVG diagrams (scripts/site_diagrams.py -> cache/site_svg/) into paper figures.

CSS variables are replaced by the site's light-theme colours and the web font by Helvetica, then MuPDF converts
the SVG to a vector PDF. Four small cards are composed into one 2 x 2 figure.

  python scripts/site_diagrams.py && python scripts/paper_site_figures.py
"""
import re
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SRC, OUT = ROOT / "cache" / "site_svg", ROOT / "paper" / "bench"
LIGHT = {"bg": "#f7f8fa", "bg-2": "#ffffff", "bg-3": "#eef1f5", "fg": "#14181f", "fg-2": "#4a5362", "fg-3": "#7a8494", "line": "#d9dee6", "line-2": "#c3cad5",
         "accent": "#0f5fb5", "accent-2": "#0b4d93", "accent-soft": "#dbe8f8", "s0": "#8a93a2", "s1": "#2a78d6", "s2": "#eb6834", "s3": "#1baf7a",
         "s4": "#eda100", "s5": "#e87ba4", "s6": "#008300", "s7": "#6250d6", "s8": "#e34948", "body": "Helvetica, Arial, sans-serif", "mono": "Courier, monospace"}


def arrowhead(m: re.Match) -> str:
    """MuPDF ignores <marker>; draw the arrowhead as a polygon at the end of the line."""
    import math
    tag = m.group(0)
    g = lambda k: float(re.search(rf'{k}="([-0-9.]+)"', tag).group(1))
    x1, y1, x2, y2 = g("x1"), g("y1"), g("x2"), g("y2")
    col = re.search(r'stroke="([^"]+)"', tag).group(1)
    a = math.atan2(y2 - y1, x2 - x1); L, W = 7.0, 3.2
    bx, by = x2 - L * math.cos(a), y2 - L * math.sin(a)
    px, py = -math.sin(a) * W, math.cos(a) * W
    head = f'<polygon points="{x2:.1f},{y2:.1f} {bx + px:.1f},{by + py:.1f} {bx - px:.1f},{by - py:.1f}" fill="{col}"/>'
    return re.sub(r' marker-end="[^"]*"', "", tag) + head


def plain(svg: str) -> str:
    svg = re.sub(r"var\(--([a-z0-9-]+)\)", lambda m: LIGHT[m.group(1)], svg)
    svg = re.sub(r'<line [^>]*marker-end="[^"]*"[^>]*/>', arrowhead, svg)
    return svg.replace(' style="width:100%;height:auto;display:block"', "")


def to_pdf(name: str) -> pymupdf.Document:
    doc = pymupdf.open("svg", plain((SRC / f"{name}.svg").read_text()).encode())
    return pymupdf.open("pdf", doc.convert_to_pdf())


for name, out in [("pipeline", "fig_pipeline.pdf"), ("scale", "fig_scale.pdf")]:
    to_pdf(name).save(OUT / out, garbage=3, deflate=True)
    print("wrote", OUT / out)

# 2 x 2 of the four "what accuracy cannot do" cards
cards = [to_pdf(n) for n in ("test", "history", "info", "why")]
w, h = cards[0][0].rect.width, cards[0][0].rect.height
gap = 24
fig = pymupdf.open()
page = fig.new_page(width=2 * w + gap, height=2 * h + gap)
for k, c in enumerate(cards):
    x0, y0 = (k % 2) * (w + gap), (k // 2) * (h + gap)
    page.show_pdf_page(pymupdf.Rect(x0, y0, x0 + w, y0 + h), c, 0)
fig.save(OUT / "fig_why.pdf", garbage=3, deflate=True)
print("wrote", OUT / "fig_why.pdf")
for f in ("fig_pipeline.pdf", "fig_scale.pdf", "fig_why.pdf"):
    pymupdf.open(OUT / f)[0].get_pixmap(dpi=90).save(ROOT / "cache" / "shots" / f.replace(".pdf", ".png"))

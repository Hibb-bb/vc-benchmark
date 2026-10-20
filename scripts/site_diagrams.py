"""Generate the explanatory SVG diagrams for the site. Theme via CSS variables; one hue per meaning."""
import math, random
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "cache" / "site_svg"; OUT.mkdir(parents=True, exist_ok=True)
FG, FG2, FG3, LINE, LINE2, BG2, BG3 = "var(--fg)", "var(--fg-2)", "var(--fg-3)", "var(--line)", "var(--line-2)", "var(--bg-2)", "var(--bg-3)"
S1, S2, S3, ACC, ACCS, S0 = "var(--s1)", "var(--s2)", "var(--s3)", "var(--accent)", "var(--accent-soft)", "var(--s0)"

def T(x, y, s, a="start", size=12, fill=FG2, w=None, extra=""):
    wt = f' font-weight="{w}"' if w else ""
    return f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="{size}" fill="{fill}"{wt}{extra}>{s}</text>'
def L(x1, y1, x2, y2, stroke=LINE2, sw=1.2, dash=None, arrow=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{arrow})"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}{extra}/>'
def R(x, y, w, h, fill=BG2, stroke=LINE2, r=8, sw=1.2, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{extra}/>'
def C(x, y, r=4, fill=S1, stroke="none", sw=1.5, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'
def marker(id_, fill=FG3):
    return f'<marker id="{id_}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9 z" fill="{fill}"/></marker>'
def svg(w, h, body, label, cls="", style="width:100%;height:auto;display:block"):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 {w} {h}" role="img" aria-label="{label}" style="{style}" font-family="var(--body)">\n' + "\n".join(body) + "\n</svg>\n"
def box(x, y, w, h, title, lines=(), fill=BG2, stroke=LINE2, tcol=FG, dash=None, size=12.5, r=10, lsize=11.2):
    b = [R(x, y, w, h, fill, stroke, r=r, dash=dash)]
    ty = y + 22
    b.append(T(x + w / 2, ty, title, "middle", size, tcol, 600))
    for i, l in enumerate(lines):
        b.append(T(x + w / 2, ty + 17 + 15 * i, l, "middle", lsize, FG2))
    return b

random.seed(3)

# ---------- 1. the score belongs to the test ----------
def d_test():
    b = [f"<defs>{marker('t1a')}</defs>"]
    # left: accuracy on two panels
    b.append(T(20, 24, "Accuracy", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    b.append(R(20, 36, 92, 24, BG3, LINE, 6)); b.append(T(66, 52, "one model", "middle", 11.5, FG, 600))
    for i, (lab, v, col) in enumerate([("curated atlas", 0.89, S1), ("scBaseCount lung", 0.39, S2)]):
        y = 90 + i * 44
        b.append(T(20, y - 6, lab, "start", 11.5, FG2))
        b.append(R(20, y, 200, 12, BG3, "none", 4)); b.append(R(20, y, 200 * v, 12, col, "none", 4))
        b.append(T(226, y + 10, f"{v:.2f}", "start", 12, FG, 600))
    b.append(T(20, 200, "Two tests, two numbers, one model.", "start", 11.5, FG3))
    # divider
    b.append(L(262, 20, 262, 205, LINE, 1))
    # right: the scale
    x0, x1, ay = 290, 540, 118
    b.append(T(290, 24, "The scale", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    b.append(L(x0, ay, x1, ay, LINE2, 1.2, arrow='t1a'))
    b.append(T(x1, ay + 16, "difficulty →", "end", 11, FG3))
    # item clouds
    for cx, col, lab in [(350, S1, "atlas items"), (480, S2, "lung items")]:
        for k in range(26):
            px = cx + random.gauss(0, 16); py = ay - 10 - abs(random.gauss(0, 14))
            b.append(C(round(px, 1), round(py, 1), 2.6, col, extra=' opacity="0.75"'))
        b.append(T(cx, ay - 58, lab, "middle", 11, col, 600))
    # model
    mx = 415
    b.append(L(mx, ay + 6, mx, ay + 34, FG, 2))
    b.append(C(mx, ay + 38, 5, FG))
    b.append(T(mx, ay + 58, "one ability", "middle", 11.5, FG, 600))
    b.append(T(290, 200, "Items spread out; the model does not move.", "start", 11.5, FG3))
    return svg(560, 210, b, "The same model gets accuracy 0.89 on a curated atlas and 0.39 on a scBaseCount lung panel; on the scale the atlas items sit at low difficulty, the lung items at high difficulty, and the model keeps one ability.")

# ---------- 2. every change resets the history ----------
def d_history():
    b = [f"<defs>{marker('t2a')}</defs>"]
    xs = [70, 200, 330, 460]; labs = ["v0", "v1: +8 panels", "v2: +scBaseCount", "v3: +hard model"]
    # accuracy track
    b.append(T(20, 24, "Accuracy", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    ay0, ah = 44, 56
    vals = [0.80, 0.62, 0.71, 0.55]
    pts = []
    for x, v in zip(xs, vals):
        y = ay0 + ah - ah * v; pts.append((x, y))
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        b.append(L(x1, y1, x2 - 8, y1, S2, 2))
        b.append(L(x2 - 8, y1, x2 - 8, y2, S2, 1.2, "3 3"))
    b.append(L(pts[-1][0], pts[-1][1], 540, pts[-1][1], S2, 2))
    for (x, y), v in zip(pts, vals):
        b.append(C(x, y, 3.5, S2)); b.append(T(x + 4, y - 7, f"{v:.2f}", "start", 10.5, S2, 600))
    b.append(T(540, 34, "moves at every change", "end", 11, S2, 600))
    # ability track
    b.append(T(20, 128, "Ability on anchored scales", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    by = 158
    b.append(L(50, by, 540, by, S1, 2))
    for x in xs:
        se = 7
        b.append(L(x, by - se, x, by + se, S1, 1.4)); b.append(L(x - 4, by - se, x + 4, by - se, S1, 1.4)); b.append(L(x - 4, by + se, x + 4, by + se, S1, 1.4))
        b.append(C(x, by, 3.5, S1))
    b.append(T(540, 148, "stays comparable", "end", 11, S1, 600))
    # version axis
    b.append(L(50, 182, 540, 182, LINE2, 1, arrow='t2a'))
    for x, lab in zip(xs, labs):
        b.append(L(x, 179, x, 185, LINE2, 1)); b.append(T(x, 197, lab, "middle", 10.5, FG3))
    return svg(560, 210, b, "Over four versions, an accuracy score jumps at each added panel or model while an anchored ability keeps its value and its error bar.")

# ---------- 3. which items can tell models apart ----------
def d_info():
    b = [f"<defs>{marker('t3a')}</defs>"]
    x0, x1, ay = 40, 540, 150
    mx = 290
    # information curve
    path = []
    for i in range(0, 501, 5):
        x = x0 + i; z = (x - mx) / 55.0
        y = ay - 92 * math.exp(-z * z / 2)
        path.append(f"{x},{y:.1f}")
    b.append(f'<path d="M{" L".join(path)}" fill="{ACCS}" stroke="{ACC}" stroke-width="1.8" opacity="0.9"/>')
    b.append(L(x0, ay, x1, ay, LINE2, 1.2, arrow='t3a'))
    b.append(T(x1, ay + 16, "item difficulty →", "end", 11, FG3))
    # items along the axis
    for i in range(48):
        x = x0 + 8 + i * 10.4
        near = abs(x - mx) < 85
        b.append(L(round(x, 1), ay - 9 if near else ay - 5, round(x, 1), ay, S1 if near else LINE2, 2 if near else 1.2))
    # the model
    b.append(L(mx, ay + 4, mx, ay + 26, FG, 2)); b.append(C(mx, ay + 30, 5, FG))
    b.append(T(mx + 10, ay + 34, "a model", "start", 11.5, FG, 600))
    b.append(T(mx, 42, "information an item carries", "middle", 11.5, ACC, 600))
    b.append(T(95, 118, "everyone passes:", "middle", 10.5, FG3)); b.append(T(95, 131, "tells nothing", "middle", 10.5, FG3))
    b.append(T(488, 118, "nobody passes:", "middle", 10.5, FG3)); b.append(T(488, 131, "tells nothing", "middle", 10.5, FG3))
    b.append(T(20, 200, "A few hundred items near a model place it; far-off items only add noise.", "start", 11.5, FG3))
    return svg(560, 210, b, "Items near a model's ability carry the most information about it; items far above or below carry none, so error bars come from the informative items and a few hundred of them place a model.")

# ---------- 4. accuracy cannot say why ----------
def d_why():
    b = [f"<defs>{marker('t4a')}</defs>"]
    b.append(T(20, 24, "Accuracy", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    b.append(T(120, 100, "0.61", "middle", 42, FG, 700, ' font-family="var(--mono)"'))
    b.append(T(120, 128, "low. why?", "middle", 12, FG3))
    b.append(L(262, 20, 262, 205, LINE, 1))
    b.append(T(290, 24, "The scale", "start", 12, FG3, 600, ' letter-spacing="0.06em"'))
    # item box
    ix, iy, iw, ih = 360, 82, 120, 46
    b.append(R(ix, iy, iw, ih, BG2, S2, 8, 1.6))
    b.append(T(ix + iw / 2, iy + 19, "one hard item", "middle", 11.5, FG, 600)); b.append(T(ix + iw / 2, iy + 36, "difficulty +2.4", "middle", 11, S2, 600))
    for (tx, ty, anc, lab, ax, ay) in [(292, 54, "start", "shallow cell", 360, 88), (548, 54, "end", "noisy label", 480, 88), (292, 168, "start", "sibling type", 360, 124), (548, 168, "end", "rare in training", 480, 124)]:
        b.append(T(tx, ty, lab, anc, 11, FG2, 500))
        sx = tx + (34 if anc == "start" else -34); sy = ty + (6 if ty < 100 else -12)
        b.append(L(sx, sy, ax, ay, LINE2, 1, arrow='t4a'))
    b.append(T(290, 200, "One number per item, correlated with a reason.", "start", 11.2, FG3))
    return svg(560, 210, b, "An accuracy of 0.61 cannot say why; on the scale each item has a difficulty, and a hard item's difficulty can be correlated with shallow cells, noisy labels, sibling types or rare training support.")

# ---------- 5. what the scale gives: annotated scene ----------
def d_scale():
    W, H = 1320, 440
    b = [f"<defs>{marker('sc-a')}</defs>"]
    x0, x1, ay = 110, 1210, 236
    sx = lambda v: x0 + (v + 4) / 10 * (x1 - x0)   # logits -4..+6
    b.append(L(x0 - 10, ay, x1 + 10, ay, LINE2, 1.4, arrow='sc-a'))
    for v in range(-4, 7, 2):
        b.append(L(sx(v), ay - 4, sx(v), ay + 4, LINE2, 1.2)); b.append(T(sx(v), ay + 20, f"{v:+d}".replace("+0", "0"), "middle", 11, FG3, None, ' font-family="var(--mono)"'))
    b.append(T(x1 + 10, ay + 38, "one logit axis: item difficulty above, model ability below", "end", 11.5, FG3))
    # items above: dot histogram, 1 dot = many items
    random.seed(11)
    counts = {}
    vals = [random.gauss(0.8, 1.6) for _ in range(260)]
    for v in vals:
        k = round(v * 2) / 2
        if k < -4 or k > 6: continue
        counts[k] = counts.get(k, 0) + 1
    for k, n in counts.items():
        n = min(n, 9)
        retired = k <= -3.0 or k >= 5.0
        for j in range(n):
            b.append(C(round(sx(k), 1), ay - 12 - j * 9, 3.4, LINE2 if retired else S1, extra=' opacity="0.55"' if retired else ''))
    # highlighted hard item
    hx = sx(3.0)
    b.append(C(round(hx, 1), ay - 12 - 2 * 9, 4.6, S2, BG2, 1.5))
    b.append(L(hx, ay - 12 - 2 * 9 - 6, hx, 96, S2, 1, "3 3"))
    # callout 2: difficulty with a reason
    b += box(hx - 80, 48, 250, 46, "② one number per item, with a reason", ["difficulty +3.0 · shallow cells, sibling type"], BG2, S2, FG, size=12)
    # callout 4: retired items
    b += box(x0 - 70, 48, 210, 46, "④ retired", ["passed by nobody: no information"], BG2, LINE2, FG2, "4 3", size=12)
    b.append(L(x0 + 35, 94, sx(-3.5), ay - 30, LINE2, 1, "3 3"))
    b += box(x1 - 90, 48, 200, 46, "④ retired", ["passed by everyone: no information"], BG2, LINE2, FG2, "4 3", size=12)
    b.append(L(x1 + 10, 94, sx(5.5), ay - 30, LINE2, 1, "3 3"))
    # callout 1: pooled items
    b += box(sx(-0.3) - 150, 48, 300, 46, "① every panel and screen on one scale", ["items namespaced by source, fit jointly, no averaging"], BG2, S1, FG, size=12)
    # models below
    def model(v, lab, se, col=FG, y=None, dash=None, size=11.5, weight=600):
        y = y or ay + 70
        x = sx(v)
        b.append(L(x, ay + 6, x, y - 8, LINE2, 1, "2 3"))
        b.append(L(sx(v - se), y, sx(v + se), y, col, 1.6)); b.append(L(sx(v - se), y - 4, sx(v - se), y + 4, col, 1.4)); b.append(L(sx(v + se), y - 4, sx(v + se), y + 4, col, 1.4))
        b.append(C(round(x, 1), y, 5, BG2 if dash else col, col, 2, extra=f' stroke-dasharray="{dash}"' if dash else ''))
        b.append(T(x, y + 20, lab, "middle", size, col, weight))
    model(-3.4, "random floor", 0.15, S0); model(-2.4, "depth floor", 0.15, S0)
    model(-0.6, "PCA-16", 0.12, FG, ay + 110); model(0.2, "PCA-64", 0.12, FG, ay + 110); model(0.75, "PCA-256", 0.12, FG, ay + 110)
    b.append(L(sx(-0.6) + 8, ay + 110, sx(0.2) - 8, ay + 110, LINE2, 1, arrow='sc-a')); b.append(L(sx(0.2) + 8, ay + 110, sx(0.75) - 8, ay + 110, LINE2, 1, arrow='sc-a'))
    model(1.9, "scVI", 0.14, S1, ay + 70)
    model(1.3, "misfit ⚑", 0.14, S2, ay + 150); 
    model(3.4, "new model", 0.22, ACC, ay + 70, dash="3 3")
    # callouts below
    b += box(sx(-3.4) - 110, ay + 110, 290, 64, "③ floors and ladders as evidence", ["floors must come last, capacity ladders in order,", "before anything else is read"], BG2, S0, FG2, size=12)
    b += box(sx(1.3) - 125, ay + 186, 250, 0, "", [], "none", "none")  # spacer no-op
    b.append(T(sx(1.3), ay + 190, "⑤ misfit is reported: outfit above 2, passes that do not follow the scale", "middle", 11.5, S2, 500))
    b += box(sx(3.4) - 60, ay + 112, 330, 64, "⑥ anchored placement", ["new models join with difficulties held fixed;", "refits advance the version, every version stays citable"], BG2, ACC, FG, "3 3", size=12)
    b += box(sx(1.9) - 70, ay + 100, 0, 0, "", [], "none", "none")
    b.append(T(sx(1.9) + 14, ay + 64, "ability ± SE", "start", 11, S1, 500))
    return svg(W, H, b, "An annotated scale: items from every panel and screen sit on one logit axis by difficulty, each with a reason; items passed by nobody or everyone are retired; models sit on the same axis with standard errors; floors must be last and ladders in order; misfit is flagged; new models are anchored with difficulties held fixed and every version is kept.", cls="scene-svg")

# ---------- 6. contribute routes ----------
def d_routes():
    W, H = 1240, 300
    b = [f"<defs>{marker('rt-a')}</defs>"]
    rows = [(26, "Route 1 · embeddings", ["cells × dims per panel", ".npy or obsm, panel cell order"], "frozen probe", ["one multinomial read-out,", "fixed settings, run by us"]),
            (116, "Route 2 · predictions", ["held-out conditions × genes", "per screen and split, fold_group"], "pass rule", ["Pearson@HVG beats", "the context's mean shift"]),
            (206, "Route 3 · response table", ["you ran the probe or rule", "yourself"], None, None)]
    for y, t, ls, pt, pl in rows:
        b += box(20, y, 250, 68, t, ls, BG2, S1 if "1" in t else S2 if "2" in t else LINE2, FG, size=14.5, lsize=12.6)
        if pt:
            b.append(L(270, y + 34, 318, y + 34, LINE2, 1.3, arrow='rt-a'))
            b += box(320, y, 190, 68, pt, pl, BG3, LINE2, FG, size=14, lsize=12.6)
            b.append(L(510, y + 34, 560, 150, LINE2, 1.3, arrow='rt-a'))
        else:
            b.append(L(270, y + 34, 560, 150, LINE2, 1.3, arrow='rt-a'))
    b += box(562, 110, 200, 80, "response table", ["item_id · respondent_id · k · n", "k passes out of n trials", "checked against held-out items"], BG2, FG, FG, size=14.5, lsize=12.6)
    b.append(L(762, 150, 812, 150, LINE2, 1.3, arrow='rt-a'))
    b += box(814, 110, 190, 80, "anchored placement", ["difficulties held fixed", "takes seconds", "no published ability moves"], BG2, ACC, FG, "4 3", size=14.5, lsize=12.6)
    b.append(L(1004, 150, 1054, 150, LINE2, 1.3, arrow='rt-a'))
    b += box(1056, 96, 170, 108, "on the board", ["ability ± SE", "outfit, pass rate", "scale version", "contamination register"], ACCS, ACC, FG, size=14.5, lsize=12.6)
    b.append(T(912, 236, "next recalibration: every model refit together, version advances", "middle", 12.2, FG3))
    b.append(L(912, 190, 912, 222, LINE2, 1, "2 3"))
    b.append(T(20, 290, "Three ways in, one response format, one placement step.", "start", 12.5, FG3))
    return svg(W, H, b, "Three submission routes, embeddings scored by the frozen probe, predictions scored by the pass rule, or a ready response table, converge on one response table, are placed with item difficulties held fixed, and appear on the board with ability, standard error, outfit, version and contamination register.", cls="scene-svg")

# ---------- 7. shared-encoder recipe ----------
def d_recipe():
    W, H = 1240, 330
    b = [f"<defs>{marker('rc-a')}</defs>"]
    b += box(20, 128, 130, 70, "cells", ["expression profiles", "of one screen"], BG2, LINE2, FG, size=14.5, lsize=12.6)
    b.append(L(150, 163, 196, 163, LINE2, 1.3, arrow='rc-a'))
    b += box(198, 118, 170, 90, "encoder", ["PCA, ICA, Nyström,", "random projection, …", "the only part that varies"], ACCS, ACC, FG, size=14.5, lsize=12.6)
    b.append(L(368, 163, 414, 163, LINE2, 1.3, arrow='rc-a'))
    b += box(416, 128, 120, 70, "latent z", ["one vector", "per cell"], BG2, LINE2, FG, size=14.5, lsize=12.6)
    # branch A (up)
    b.append(L(536, 150, 600, 70, LINE2, 1.3, arrow='rc-a'))
    b += box(602, 36, 170, 68, "frozen probe", ["names the cell type", "from z"], BG2, S1, FG, size=14, lsize=12.6)
    b.append(L(772, 70, 818, 70, LINE2, 1.3, arrow='rc-a'))
    b += box(820, 36, 190, 68, "representation ability", ["pass = type named right", "all 14 panels"], BG2, S1, S1, size=14, lsize=12.6)
    b.append(T(560, 40, "A", "middle", 16, S1, 700))
    # branch B (down)
    b.append(L(536, 176, 600, 256, LINE2, 1.3, arrow='rc-a'))
    b += box(602, 222, 170, 68, "latent shift", ["mean z of perturbed cells", "minus control, per condition"], BG2, S2, FG, size=14, lsize=12.6)
    b.append(L(772, 256, 818, 256, LINE2, 1.3, arrow='rc-a'))
    b += box(820, 222, 190, 68, "perturbation ability", ["fixed linear decoder to genes;", "pass = beats the mean shift"], BG2, S2, S2, size=14, lsize=12.6)
    b.append(T(560, 300, "B", "middle", 16, S2, 700))
    # join
    b.append(L(1010, 70, 1060, 148, LINE2, 1.3, arrow='rc-a')); b.append(L(1010, 256, 1060, 178, LINE2, 1.3, arrow='rc-a'))
    b += box(1062, 128, 160, 70, "one point", ["same encoder,", "two abilities"], BG2, FG, FG, size=14.5, lsize=12.6)
    b.append(T(20, 318, "Hold everything fixed except the encoder; the random projections at each dimension are the null.", "start", 12.5, FG3))
    return svg(W, H, b, "Cells are embedded by one encoder, the only part that varies; the same latent vectors feed the frozen probe for a representation ability and a latent-shift model with a fixed decoder for a perturbation ability, giving each encoder one point with two abilities.", cls="scene-svg")

for name, fn in [("test", d_test), ("history", d_history), ("info", d_info), ("why", d_why), ("scale", d_scale), ("routes", d_routes), ("recipe", d_recipe)]:
    (OUT / f"{name}.svg").write_text(fn())
    print(name, len(fn()))


# ---------- 8. home page pipeline ----------
def d_pipeline():
    W, H = 1320, 330
    b = [f"<defs>{marker('pp-a')}</defs>"]
    pw, ph, gap, top = 214, 170, 52, 70
    xs = [40 + i * (pw + gap) for i in range(5)]
    titles = [("Items", "every cell and every perturbation is a question"),
              ("The test", "the same read-out for every model"),
              ("Answers", "pass or fail, every model on every item"),
              ("IRT fit", "one model of all the answers"),
              ("One scale", "models and items on the same axis")]
    for (x, (t, sub)) in zip(xs, titles):
        b.append(T(x, 34, t, "start", 15, FG, 700)); b.append(T(x, 52, sub, "start", 11.5, FG3))
        b.append(R(x, top, pw, ph, BG2, LINE2, 12))
    for i in range(4):
        b.append(L(xs[i] + pw + 8, top + ph / 2, xs[i + 1] - 8, top + ph / 2, FG3, 1.6, arrow='pp-a'))
    # panel 1: cells and a perturbation pair
    x = xs[0]; random.seed(5)
    for cx, cy, col in [(x + 60, top + 70, S1), (x + 45, top + 118, S3), (x + 95, top + 110, S2)]:
        for k in range(9):
            b.append(C(round(cx + random.gauss(0, 11), 1), round(cy + random.gauss(0, 9), 1), 3.2, col, extra=' opacity="0.85"'))
    b.append(T(x + 68, top + 150, "cells", "middle", 11.5, FG2))
    b.append(C(x + 150, top + 62, 9, BG3, LINE2, 1.4)); b.append(C(x + 170, top + 120, 9, S2))
    b.append(L(x + 154, top + 72, x + 166, top + 109, FG3, 1.4, arrow='pp-a'))
    b.append(T(x + 160, top + 150, "perturbations", "middle", 11.5, FG2))
    # panel 2: rows of models with ticks and crosses
    x = xs[1]
    rows = [("PCA", S1, "✓✓✗✓"), ("scVI", "var(--s7)", "✓✓✓✗"), ("Nyström", S2, "✓✗✓✓"), ("random", S0, "✗✗✓✗")]
    for i, (n, col, marks) in enumerate(rows):
        y = top + 36 + i * 32
        b.append(C(x + 22, y - 4, 5, col)); b.append(T(x + 34, y, n, "start", 12, FG, 500))
        b.append(T(x + 122, y, "→", "middle", 12, FG3))
        for j, m in enumerate(marks):
            b.append(T(x + 150 + j * 16, y + 1, m, "middle", 12.5, S3 if m == "✓" else S2, 700))
    b.append(T(x + pw / 2, top + 158, "one frozen probe, one pass rule", "middle", 11, FG3))
    # panel 3: pass/fail matrix
    x = xs[2]
    cols_, rws = 12, 7
    cw = 13
    mx0, my0 = x + 32, top + 34
    for r in range(rws):
        for c in range(cols_):
            p = 0.9 - r * 0.11 - c * 0.045
            on = random.random() < p
            b.append(R(mx0 + c * cw, my0 + r * cw, cw - 3, cw - 3, S1 if on else BG3, "none" if on else LINE, 2, 0.8))
    b.append(T(mx0 - 6, my0 + rws * cw / 2, "models", "end", 10.5, FG3, None, f' transform="rotate(-90 {mx0 - 6} {my0 + rws * cw / 2})"'))
    b.append(T(mx0 + cols_ * cw / 2, my0 + rws * cw + 16, "items", "middle", 10.5, FG3))
    b.append(T(x + pw / 2, top + 158, "nothing is averaged", "middle", 11, FG3))
    # panel 4: IRT fit -> two outputs
    x = xs[3]
    b.append(R(x + 22, top + 60, 80, 50, ACCS, ACC, 10, 1.4)); b.append(T(x + 62, top + 81, "IRT", "middle", 15, FG, 700)); b.append(T(x + 62, top + 98, "model", "middle", 11, FG2))
    b.append(L(x + 104, top + 76, x + 124, top + 56, FG3, 1.4, arrow='pp-a')); b.append(L(x + 104, top + 94, x + 124, top + 114, FG3, 1.4, arrow='pp-a'))
    b.append(T(x + 130, top + 52, "ability", "start", 12.5, FG, 600)); b.append(T(x + 130, top + 66, "per model", "start", 11, FG2))
    b.append(T(x + 130, top + 118, "difficulty", "start", 12.5, FG, 600)); b.append(T(x + 130, top + 132, "per item", "start", 11, FG2))
    b.append(T(x + pw / 2, top + 158, "with an error bar on each", "middle", 11, FG3))
    # panel 5: mini Wright map
    x = xs[4]
    ax = x + 110
    b.append(L(ax, top + 26, ax, top + 140, LINE2, 1.4))
    for i, w in enumerate([10, 22, 40, 56, 46, 30, 14]):
        b.append(R(ax - 6 - w, top + 32 + i * 15, w, 11, S1, "none", 2, extra=' opacity="0.75"'))
    for (dy, col, se) in [(40, S2, 9), (58, "var(--s7)", 8), (76, S1, 9), (112, S0, 6)]:
        y = top + dy
        b.append(L(ax + 18 - se, y, ax + 18 + se, y, col, 1.4)); b.append(C(ax + 18, y, 4, col))
    b.append(T(ax - 6, top + 150, "items", "end", 10.5, FG3)); b.append(T(ax + 6, top + 150, "models", "start", 10.5, FG3))
    b.append(T(x + pw / 2, top + 160, "", "middle", 11, FG3))
    # living loop: one return arrow
    ly = top + ph + 42
    b.append(L(xs[4] + pw / 2, top + ph + 8, xs[4] + pw / 2, ly, FG3, 1.3, "4 4"))
    b.append(L(xs[4] + pw / 2, ly, xs[0] + pw / 2, ly, FG3, 1.3, "4 4"))
    b.append(L(xs[0] + pw / 2, ly, xs[0] + pw / 2, top + ph + 10, FG3, 1.3, "4 4", arrow='pp-a'))
    b.append(R(W / 2 - 200, ly - 12, 400, 24, BG2, "none", 6))
    b.append(T(W / 2, ly + 4, "new models and new items join the same scale; every version is kept", "middle", 12, FG2, 500))
    return svg(W, H, b, "The pipeline: cells and perturbations are the items; every model takes the same test; the answers form a pass/fail matrix; an IRT model fits an ability per model and a difficulty per item; both sit on one scale; new models and new items join the same scale and every version is kept.", cls="scene-svg")

if __name__ == "__main__":
    (OUT / "pipeline.svg").write_text(d_pipeline())

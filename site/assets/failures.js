import { $, getJSON, lines, esc, fmt, pct, int, sgn, svgOpen, lin } from './app.js';

const GROUP = (fam) => (/interferon/.test(fam) ? ['Interferons', 'var(--s1)']
  : /gamma chain/.test(fam) ? ['Common gamma chain', 'var(--s3)']
    : /gp130/.test(fam) ? ['IL-6 / gp130', 'var(--s7)']
      : /TNF/.test(fam) ? ['TNF superfamily', 'var(--s4)']
        : /IL-1 |IL-1$/.test(fam) ? ['IL-1 family', 'var(--s2)']
          : /IL-10|IL-12|IL-17/.test(fam) ? ['IL-10, IL-12, IL-17', 'var(--s5)']
            : ['Growth factors and other', 'var(--s0)']);
const GROUP_KEYS = [['Interferons', 'interferon'], ['Common gamma chain', 'gamma chain'], ['IL-6 / gp130', 'gp130'], ['TNF superfamily', 'TNF'],
  ['IL-1 family', 'IL-1 family'], ['IL-10, IL-12, IL-17', 'IL-10'], ['Growth factors and other', 'x']];

const GLOSS = [
  ['Item', 'One cytokine in one donor\'s cell type, for example IFN-β in donor 3\'s CD14 monocytes.'],
  ['Clear response', 'Signal-to-noise of 1.5 or more: the response stands clearly above noise.'],
  ['Weak or null', 'Signal-to-noise below 1.5: little or nothing happened.'],
  ['Pass', 'Clear: the prediction explains at least half the achievable R². Weak or null: the predicted change is within 1.5 × noise.'],
  ['Pass rate', 'Share of items a model passes, or share of models that pass an item.'],
  ['Difficulty, ability', 'Pass rates on one logit scale. Ability above an item\'s difficulty: likely to pass.'],
];

function tiles(D) {
  const h = D.headline, m = D.meta, missed = D.kinds.find((k) => k.key === 'missed');
  const t = [
    [pct(h.hard_clear_share, 1), 'of the hardest items are clear responses'],
    [`${pct(h.clear_pass)} vs ${pct(h.weak_pass)}`, 'of models pass a clear response, against a weak or null one'],
    [int(missed?.n), `clear responses no model captures, of ${int(m.n_clear)}`],
    [sgn(h.best_ability), `best ability: ${h.best_model}`],
  ];
  $('#tiles').innerHTML = t.map(([v, l]) => `<div class="fm-tile"><b>${esc(v)}</b><span>${esc(l)}</span></div>`).join('');
}

function rule(D) {
  // two panels: a clear response (pattern and size must match) and a null response (small change is right)
  const w = 560, h = 300, bw = 18;
  const truthC = [1.6, 1.2, 0.9, -0.5, 0.8, -1.0, 0.3, 1.1, -0.6, 0.2], predC = [1.3, 1.0, 0.7, -0.4, 0.6, -0.8, 0.2, 0.9, -0.5, 0.2];
  const truthN = [0.2, -0.15, 0.1, 0.25, -0.2, 0.05, -0.1, 0.15, -0.25, 0.1], predN = [0.03, -0.02, 0.02, 0.0, -0.03, 0.02, 0.0, 0.02, -0.02, 0.01];
  const panel = (x0, title, sub, truth, pred, verdict) => {
    let s = `<text x="${x0}" y="18" style="font-size:12.5px;font-weight:600">${title}</text><text x="${x0}" y="34" style="font-size:11px;fill:var(--fg-3)">${sub}</text>`;
    [[truth, 'var(--fg-2)', 'measured', 92], [pred, 'var(--s1)', 'predicted', 172]].forEach(([v, c, lab, y0]) => {
      s += `<text x="${x0}" y="${y0 - 34}" style="font-size:10.5px;fill:var(--fg-3)">${lab}</text><line x1="${x0}" x2="${x0 + 10 * (bw + 4)}" y1="${y0}" y2="${y0}" stroke="var(--line-2)"/>`;
      v.forEach((g, j) => { const hh = g * 18; s += `<rect x="${x0 + j * (bw + 4)}" y="${hh > 0 ? y0 - hh : y0}" width="${bw}" height="${Math.max(Math.abs(hh), 0.8)}" fill="${c}" rx="2"/>`; });
    });
    s += `<rect x="${x0}" y="222" width="${10 * (bw + 4) - 4}" height="44" rx="8" fill="var(--s3)" opacity=".12"/><text x="${x0 + 5 * (bw + 4) - 2}" y="240" text-anchor="middle" style="font-size:11.5px;font-weight:600;fill:var(--s3)">${verdict[0]}</text><text x="${x0 + 5 * (bw + 4) - 2}" y="256" text-anchor="middle" style="font-size:10.5px;fill:var(--fg-2)">${verdict[1]}</text>`;
    return s;
  };
  let s = svgOpen(w, h);
  s += panel(0, 'Clear response', `signal-to-noise ≥ ${D.meta.split}`, truthC, predC, ['pass if R² ≥ half the achievable', 'pattern and size must match']);
  s += panel(300, 'Weak or null response', `signal-to-noise < ${D.meta.split}`, truthN, predN, [`pass if error ≤ ${D.meta.k} × noise`, 'a small change is the right answer']);
  $('#rule').innerHTML = s + '</svg>';
  $('#gloss').innerHTML = GLOSS.map(([t, d]) => `<dt>${esc(t)}</dt><dd>${esc(d)}</dd>`).join('');
  if (D.meta.snr_vs_split_half != null) $('#defs-note').textContent = `Check: splitting each item's cells into two halves and correlating them orders items the same way as signal-to-noise (rank correlation ${fmt(D.meta.snr_vs_split_half, 2)}).`;
}

function curves(D) {
  const ser = [['signal-to-noise', 'snr', 'var(--s8)'], ['cells per item', 'cells', 'var(--s1)'], ['raw response size', 'strength', 'var(--s0)']]
    .map(([name, k, color]) => ({ name, color, pts: D.curves[k].map((p, i) => ({ x: i + 1, y: p.y, tip: `${pct(p.y)} pass` })) }));
  $('#curves').innerHTML = lines(ser, { xlabel: 'tenth of items, lowest to highest', ylabel: 'share of models passing', ydom: [0, 1], xdom: [1, 10], xfmt: (t) => String(t), yfmt: (t) => pct(t) });
  $('#curves-leg').innerHTML = ser.map((s) => `<span><i class="sw" style="--c:${s.color}"></i>${esc(s.name)}</span>`).join('');
}

function heat(D) {
  const H = D.heat, nr = H.rows.length, nc = H.cols.length;
  const w = 540, h = 290, m = { l: 82, t: 12, r: 8, b: 56 }, cw = (w - m.l - m.r) / nc, ch = (h - m.t - m.b) / nr;
  let s = svgOpen(w, h);
  H.rows.forEach((rl, i) => H.cols.forEach((cl, j) => {
    const p = H.p[i][j]; if (p == null) return;
    const y = m.t + (nr - 1 - i) * ch, x = m.l + j * cw;
    s += `<g class="mark" data-tip="${esc(cl)} · signal-to-noise ${esc(rl)}<br>${pct(p)} of models pass · ${int(H.n[i][j])} items"><rect x="${x + 1}" y="${y + 1}" width="${cw - 2}" height="${ch - 2}" rx="4" fill="var(--s3)" opacity="${0.08 + 0.92 * p}"/><text x="${x + cw / 2}" y="${y + ch / 2 + 4}" text-anchor="middle" class="mono" style="font-size:11px;fill:${p > 0.55 ? '#fff' : 'var(--fg)'}">${pct(p)}</text></g>`;
  }));
  H.rows.forEach((l, i) => { s += `<text x="${m.l - 8}" y="${m.t + (nr - 1 - i) * ch + ch / 2 + 4}" text-anchor="end" style="font-size:11px">${l}</text>`; });
  H.cols.forEach((l, j) => { s += `<text transform="translate(${m.l + j * cw + cw / 2} ${h - m.b + 14}) rotate(-25)" text-anchor="end" style="font-size:11px">${l}</text>`; });
  s += `<text transform="translate(12 ${m.t + (h - m.t - m.b) / 2}) rotate(-90)" text-anchor="middle">signal-to-noise →</text>`;
  $('#heat').innerHTML = s + '</svg>';
}

function stack(D) {
  const w = 760, h = 50, l = 0, r = 12, bh = 30; let x = l;
  const tot = D.kinds.reduce((a, c) => a + c.n, 0);
  let s = svgOpen(w, h);
  for (const c of D.kinds) {
    const ww = (c.n / tot) * (w - l - r);
    s += `<g class="mark" data-tip="<b>${esc(c.name)}</b><br>${int(c.n)} items (${pct(c.n / tot)})"><rect x="${x}" y="8" width="${Math.max(ww - 1, 0.5)}" height="${bh}" fill="${c.color}"/>${ww > 44 ? `<text x="${x + ww / 2}" y="${8 + bh / 2 + 4}" text-anchor="middle" class="mono" style="font-size:11px;fill:#fff">${pct(c.n / tot)}</text>` : ''}</g>`;
    x += ww;
  }
  $('#stack').innerHTML = s + '</svg>';
  $('#stack-leg').innerHTML = D.kinds.map((c) => `<span><i class="sw" style="--c:${c.color}"></i>${esc(c.name)}</span>`).join('');
}

function cards(D) {
  const it = (e) => !e ? '' : `
    <div class="fm-item"><div class="fm-item-h">${esc(e.cytokine)} <span>→</span> ${esc(e.cell_type)}<em>${esc(e.donor)}</em></div>
    <dl><dt>cells</dt><dd>${int(e.n_cells)}</dd><dt>signal-to-noise</dt><dd>${fmt(e.snr)}</dd>
    ${e.achievable_r2 != null ? `<dt>achievable R²</dt><dd>${fmt(e.achievable_r2)}</dd><dt>best model's share of it</dt><dd>${pct(Math.min(e.best_share, 1))}</dd>` : ''}
    <dt>donor agreement</dt><dd>${fmt(e.repro)}</dd><dt>receptor</dt><dd>${e.receptor == null ? 'none known' : fmt(e.receptor, 3)}</dd>
    <dt>models passing</dt><dd>${e.passed} of ${e.of}</dd></dl></div>`;
  $('#cards').innerHTML = D.kinds.map((c) => `<div class="card fm-card" style="--c:${c.color}">
    <h3><span>${esc(c.name)}</span><span class="mono faint">${pct(c.share)}</span></h3><p class="sub">${esc(c.desc)}</p>
    <div class="fm-meter"><i style="width:${(100 * (c.pass ?? 0)).toFixed(0)}%"></i></div><p class="foot">${pct(c.pass)} of models pass, on average</p>${it(c.example)}</div>`).join('');
}

function hbars(rows, { w = 520, labelW = 150, color = () => 'var(--s1)', tip = () => '', val = (r) => r.pass, fmtV = (v) => pct(v), max = 1, bh = 18 } = {}) {
  const gap = 6, h = rows.length * (bh + gap) + 6, x = lin(0, max, labelW, w - 46);
  let s = svgOpen(w, h);
  rows.forEach((r, i) => {
    const y = 4 + i * (bh + gap), v = val(r);
    s += `<g class="mark" data-tip="${esc(tip(r))}"><text x="${labelW - 8}" y="${y + bh - 5}" text-anchor="end" style="font-size:11.5px">${esc(r.name)}</text><rect x="${labelW}" y="${y}" width="${Math.max(x(v) - labelW, 1)}" height="${bh}" rx="3" fill="${color(r)}"/><text x="${x(v) + 5}" y="${y + bh - 5}" class="mono" style="font-size:11px">${fmtV(v)}</text></g>`;
  });
  return s + '</svg>';
}

function nulls(D) {
  const rows = D.nulls.filter((r) => !/^ridge_d10|^pcareg_k(2|5|10|20)$|_tf0\./.test(r.rid));
  const show = [...rows.slice(0, 6), ...rows.slice(-6)];
  $('#nulls-sub').textContent = `${int(D.meta.n_weak)} items. The six models that most often invent a response, and the six that least often do. Hover for the median error in units of noise (1.0 ≈ a perfect model).`;
  $('#nullbars').innerHTML = hbars(show, { w: 900, labelW: 250, color: (r) => (r.pass < 0.9 ? 'var(--s2)' : 'var(--s3)'), tip: (r) => `${r.name}: ${pct(r.pass)} passed · median error ${fmt(r.ratio)} × noise` });
}

function biology(D) {
  const cy = [...D.cytokines].sort((a, b) => b.pass - a.pass);
  const w = 560, h = 230, m = { l: 40, t: 12, r: 8, b: 26 }, bw = (w - m.l - m.r) / cy.length, y = lin(0, 1, h - m.b, m.t);
  let s = svgOpen(w, h);
  [0, 0.25, 0.5, 0.75, 1].forEach((t) => { s += `<line x1="${m.l}" x2="${w - m.r}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)"/><text x="${m.l - 6}" y="${y(t) + 4}" text-anchor="end" class="mono" style="font-size:10px">${pct(t)}</text>`; });
  cy.forEach((c, i) => {
    const col = GROUP(c.family)[1], x = m.l + i * bw;
    s += `<g class="mark" data-tip="<b>${esc(c.name)}</b> · ${esc(c.family)}<br>${pct(c.pass)} of models pass · median signal-to-noise ${fmt(c.snr)}${c.is_cytokine === false ? '<br>not a cytokine' : ''}"><rect x="${x + 0.5}" y="${y(c.pass)}" width="${Math.max(bw - 1, 1)}" height="${y(0) - y(c.pass)}" fill="${col}" ${c.is_cytokine === false ? 'opacity=".35"' : ''}/></g>`;
  });
  s += `<text x="${m.l + (w - m.l - m.r) / 2}" y="${h - 6}" text-anchor="middle" style="font-size:11px;fill:var(--fg-3)">90 cytokines, easiest to hardest</text>`;
  $('#cyt').innerHTML = s + '</svg>' + `<p class="foot"><b>Easiest:</b> ${cy.slice(0, 5).map((c) => esc(c.name)).join(', ')}. <b>Hardest:</b> ${cy.slice(-5).reverse().map((c) => esc(c.name)).join(', ')}.</p>`;
  $('#cyt-leg').innerHTML = GROUP_KEYS.map(([g, k]) => `<span><i class="sw" style="--c:${GROUP(k)[1]}"></i>${esc(g)}</span>`).join('');
  $('#rec').innerHTML = hbars(D.receptor, { color: () => 'var(--s1)', tip: (r) => `${int(r.n)} items · median signal-to-noise ${fmt(r.snr)}` });
  $('#lin').innerHTML = hbars(D.lineage.filter((r) => r.n > 20), { color: () => 'var(--s3)', tip: (r) => `${int(r.n)} items · median signal-to-noise ${fmt(r.snr)}` });
  $('#don').innerHTML = hbars(D.donors, { labelW: 90, color: (r) => (r.high_isg ? 'var(--s7)' : 'var(--s0)'), tip: (r) => `${int(r.n)} items · median donor agreement ${fmt(r.repro)}` });
}

function rank(D) {
  const col = ['var(--s0)', 'var(--s4)', 'var(--s8)'];
  const xs = D.rank.flatMap((b) => b.pts.map((p) => p.x));
  const w = 1000, h = 320, m = { l: 56, r: 16, t: 14, b: 46 }, x0 = Math.floor(Math.min(...xs)), x1 = Math.ceil(Math.max(...xs));
  const x = lin(x0, x1, m.l, w - m.r), y = lin(0, 1, h - m.b, m.t);
  let s = svgOpen(w, h);
  [0, 0.25, 0.5, 0.75, 1].forEach((t) => { s += `<line x1="${m.l}" x2="${w - m.r}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)"/><text x="${m.l - 8}" y="${y(t) + 4}" text-anchor="end" class="mono" style="font-size:11px">${pct(t)}</text>`; });
  for (let t = x0; t <= x1; t += 1) s += `<text x="${x(t)}" y="${h - m.b + 16}" text-anchor="middle" class="mono" style="font-size:11px">${sgn(t, 0).replace('+0', '0')}</text>`;
  D.rank.forEach((b, i) => b.pts.forEach((p) => {
    s += `<circle class="mark" data-tip="<b>${esc(p.name)}</b><br>${esc(b.band)}: ${pct(p.y)} passed" cx="${x(p.x)}" cy="${y(p.y)}" r="5" fill="${col[i]}" opacity=".85" stroke="var(--bg-2)" stroke-width="1.5"/>`;
  }));
  s += `<text x="${(m.l + w - m.r) / 2}" y="${h - 8}" text-anchor="middle">model ability on this rule (logits) →</text><text transform="translate(14 ${(m.t + h - m.b) / 2}) rotate(-90)" text-anchor="middle">share of items passed</text>`;
  $('#rankchart').innerHTML = s + '</svg>';
  $('#rank-leg').innerHTML = D.rank.map((b, i) => `<span><i class="sw" style="--c:${col[i]}"></i>${esc(b.band)} · ${int(b.n_items)} items · ρ ${fmt(b.rho, 2)}</span>`).join('');
}

function models(D) {
  const keep = D.models.filter((m, i) => i < 12 || /^statetx|scgen|scvi_cf|control_mean|random_shift_s0|mlp_h256_d50_g/.test(m.rid));
  const row = (m) => `<tr${m.placement === 'anchored' ? ' class="faint"' : ''}><td>${esc(m.name)}</td><td class="num">${sgn(m.ability)}</td><td class="num">${pct(m.pass_clear)}</td><td class="num">${pct(m.pass_weak)}</td><td class="num">${m.published == null ? '–' : sgn(m.published)}</td></tr>`;
  $('#mtable').innerHTML = `<thead><tr><th>Model</th><th class="num">Ability</th><th class="num">Clear items passed</th><th class="num">Weak or null passed</th><th class="num">Ability, published rule</th></tr></thead><tbody>${keep.map(row).join('')}</tbody>`;
}

export default async function () {
  const D = await getJSON('data/parse_failures.json');
  tiles(D); rule(D); curves(D); heat(D); stack(D); cards(D); nulls(D); biology(D); rank(D); models(D);
}

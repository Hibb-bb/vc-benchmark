import { $, getJSON, lines, esc, fmt, pct, int, sgn, svgOpen, lin } from './app.js';

const CLS_COLOR = { clear: 'var(--s3)', refright: 'var(--s4)', donor: 'var(--s7)', between: 'var(--s0)', noresp: 'var(--s2)', fewcells: 'var(--s8)' };
const GROUP = (fam) => (/interferon/.test(fam) ? ['Interferons', 'var(--s1)']
  : /gamma chain/.test(fam) ? ['Common gamma chain', 'var(--s3)']
    : /gp130/.test(fam) ? ['IL-6 / gp130', 'var(--s7)']
      : /TNF/.test(fam) ? ['TNF superfamily', 'var(--s4)']
        : /IL-1 |IL-1$/.test(fam) ? ['IL-1 family', 'var(--s2)']
          : /IL-10|IL-12|IL-17/.test(fam) ? ['IL-10, IL-12, IL-17', 'var(--s5)']
            : ['Growth factors and other', 'var(--s0)']);
const GROUP_ORDER = ['Interferons', 'Common gamma chain', 'IL-6 / gp130', 'TNF superfamily', 'IL-1 family', 'IL-10, IL-12, IL-17', 'Growth factors and other'];

const GLOSS = [
  ['Item', 'One cytokine in one donor\'s cell type, for example IFN-β in donor 3\'s CD14 monocytes.'],
  ['Response (shift)', 'Average expression of treated cells minus untreated cells, gene by gene.'],
  ['Average response', 'The mean shift of the other cytokines in the same donor and cell type. The bar to beat.'],
  ['Pass', 'The model\'s predicted shift correlates with the truth better than the average response does.'],
  ['Pass rate', 'Share of items a model passes, or share of models that pass an item.'],
  ['Difficulty, ability', 'Pass rates put on one logit scale. Ability above an item\'s difficulty: likely to pass.'],
  ['Reliability', ''],
  ['Signal-to-noise', 'Size of the shift divided by the size expected from sampling noise alone.'],
  ['Receptor expression', 'Expression of the cytokine\'s receptor in untreated cells of that type.'],
];

function tiles(D) {
  const h = D.headline, m = D.meta;
  const t = [
    [pct(h.hard_unmeasurable), 'of the hardest items have too few cells or no detectable response'],
    [int(h.hard_clear), `hardest items with a clear, reliable response that models miss`],
    [pct(h.share_clear), `of ${int(m.n_items)} items are a clean test of the model`],
    [`${fmt(h.rho_rel, 2)} vs ${fmt(h.rho_strength, 2)}`, 'correlation of pass rate with reliability, and with raw effect size'],
  ];
  $('#tiles').innerHTML = t.map(([v, l]) => `<div class="fm-tile"><b>${v}</b><span>${esc(l)}</span></div>`).join('');
}

function rule(D) {
  // schematic: ten genes, the measured shift, a model's prediction and the average response
  const truth = [1.6, 1.2, 0.9, -0.4, 0.7, -1.0, 0.3, 1.1, -0.6, 0.2];
  const model = [1.3, 1.0, 0.6, -0.2, 0.9, -0.7, 0.1, 0.8, -0.5, 0.4];
  const avg = [1.4, 0.2, 0.8, 0.3, -0.2, -0.2, 0.6, 0.3, 0.2, -0.3];
  const w = 560, h = 250, rowH = 62, x0 = 150, bw = 30;
  const rows = [['Measured shift', truth, 'var(--fg-2)', ''], ['Model prediction', model, 'var(--s1)', 'r = 0.93'], ['Average response', avg, 'var(--s0)', 'r = 0.46']];
  let s = svgOpen(w, h);
  rows.forEach(([lab, v, c, r], i) => {
    const y0 = 34 + i * rowH;
    s += `<text x="0" y="${y0 + 4}" style="font-size:12px;font-weight:600">${lab}</text>`;
    if (r) s += `<text x="0" y="${y0 + 20}" class="mono" style="font-size:11px;fill:${c}">${r}</text>`;
    s += `<line x1="${x0}" x2="${x0 + 10 * (bw + 4)}" y1="${y0}" y2="${y0}" stroke="var(--line-2)"/>`;
    v.forEach((g, j) => { const hh = g * 14; s += `<rect x="${x0 + j * (bw + 4)}" y="${hh > 0 ? y0 - hh : y0}" width="${bw}" height="${Math.abs(hh)}" fill="${c}" rx="2"/>`; });
  });
  s += `<text x="${x0}" y="${34 + 3 * rowH - 6}" style="font-size:11px;fill:var(--fg-3)">one bar per gene</text>`;
  s += `<rect x="${x0 + 220}" y="${34 + 3 * rowH - 22}" width="150" height="26" rx="13" fill="var(--s3)" opacity=".15"/><text x="${x0 + 295}" y="${34 + 3 * rowH - 4}" text-anchor="middle" style="font-size:12px;font-weight:600;fill:var(--s3)">0.93 &gt; 0.46 → pass</text>`;
  $('#rule').innerHTML = s + '</svg>';
  const g = GLOSS.map(([t, d]) => (t === 'Reliability' ? (D.meta.has_reliability ? [t, 'How well two random halves of the item\'s own cells agree. Near 0: the shift is mostly noise.'] : ['Donor agreement', 'How well this donor\'s shift matches the same cytokine and cell type in the other donors. Low: a different response, or noise.']) : [t, d]));
  $('#defs-note').textContent = D.meta.has_reliability ? 'Charts labelled "reliability" use within-item reliability; the item cards show both it and donor agreement.' : 'Within-item reliability is still being computed from the full 9.7-million-cell file; until then, charts labelled "reliability" use donor agreement.';
  $('#gloss').innerHTML = g.map(([t, d]) => `<dt>${esc(t)}</dt><dd>${esc(d)}</dd>`).join('');
}

function heat(D) {
  const H = D.heat, relL = ['below 0.2', '0.2–0.35', '0.35–0.5', '0.5–0.7', '0.7 and up'], refL = relL;
  const w = 520, h = 300, m = { l: 96, t: 24, r: 8, b: 46 }, cw = (w - m.l - m.r) / 5, ch = (h - m.t - m.b) / 5;
  let s = svgOpen(w, h);
  for (let i = 0; i < 5; i++) for (let j = 0; j < 5; j++) {
    const p = H.p[i][j], n = H.n[i][j];
    if (p == null) continue;
    const y = m.t + (4 - i) * ch, x = m.l + j * cw;
    s += `<g class="mark" data-tip="reliability ${relL[i]}, average-response fit ${refL[j]}<br>${pct(p)} of models pass · ${int(n)} items"><rect x="${x + 1}" y="${y + 1}" width="${cw - 2}" height="${ch - 2}" rx="4" fill="var(--s3)" opacity="${0.08 + 0.92 * p}"/><text x="${x + cw / 2}" y="${y + ch / 2 + 4}" text-anchor="middle" class="mono" style="font-size:12px;fill:${p > 0.55 ? '#fff' : 'var(--fg)'}">${pct(p)}</text></g>`;
  }
  relL.forEach((l, i) => { s += `<text x="${m.l - 8}" y="${m.t + (4 - i) * ch + ch / 2 + 4}" text-anchor="end" style="font-size:11px">${l}</text>`; });
  refL.forEach((l, j) => { s += `<text x="${m.l + j * cw + cw / 2}" y="${h - m.b + 16}" text-anchor="middle" style="font-size:11px">${l}</text>`; });
  s += `<text x="${m.l + (w - m.l - m.r) / 2}" y="${h - 8}" text-anchor="middle">how well the average response already fits (r) →</text>`;
  s += `<text transform="translate(12 ${m.t + (h - m.t - m.b) / 2}) rotate(-90)" text-anchor="middle">reliability →</text>`;
  $('#heat').innerHTML = s + '</svg>';
}

function curves(D) {
  const ser = [['reliability', 'rel', 'var(--s3)'], ['signal-to-noise', 'snr', 'var(--s1)'], ['raw effect size', 'strength', 'var(--s2)']]
    .map(([name, k, color]) => ({ name, color, pts: D.curves[k].map((p, i) => ({ x: i + 1, y: p.y, tip: `${pct(p.y)} pass · median ${fmt(p.x, 2)}` })) }));
  $('#curves').innerHTML = lines(ser, { xlabel: 'tenth of items, lowest to highest', ylabel: 'share of models passing', ydom: [0, 0.9], xdom: [1, 10], xfmt: (t) => String(t), yfmt: (t) => pct(t) });
  $('#curves-leg').innerHTML = ser.map((s) => `<span><i class="sw" style="--c:${s.color}"></i>${esc(s.name)}</span>`).join('');
}

function stack(D) {
  D = { ...D, classes: D.classes.filter((c) => c.n > 0) };
  const w = 760, h = 96, l = 150, r = 12, bh = 26;
  const rows = [['All items', (c) => c.n], ['Hardest items', (c) => c.n_hard]];
  let s = svgOpen(w, h);
  rows.forEach(([lab, get], i) => {
    const tot = D.classes.reduce((a, c) => a + get(c), 0); let x = l; const y = 12 + i * (bh + 18);
    s += `<text x="0" y="${y + bh / 2 + 4}" style="font-size:12px;font-weight:600">${lab}</text><text x="${l - 10}" y="${y + bh / 2 + 4}" text-anchor="end" class="mono" style="font-size:11px;fill:var(--fg-3)">${int(tot)}</text>`;
    for (const c of D.classes) {
      const v = get(c); if (!v) continue; const ww = (v / tot) * (w - l - r);
      s += `<g class="mark" data-tip="<b>${esc(c.name)}</b><br>${int(v)} items (${pct(v / tot)})"><rect x="${x}" y="${y}" width="${Math.max(ww - 1, 0.5)}" height="${bh}" fill="${CLS_COLOR[c.key]}"/>${ww > 44 ? `<text x="${x + ww / 2}" y="${y + bh / 2 + 4}" text-anchor="middle" class="mono" style="font-size:11px;fill:#fff">${pct(v / tot)}</text>` : ''}</g>`;
      x += ww;
    }
  });
  $('#stack').innerHTML = s + '</svg>';
  $('#stack-leg').innerHTML = D.classes.map((c) => `<span><i class="sw" style="--c:${CLS_COLOR[c.key]}"></i>${esc(c.name)}</span>`).join('');
}

function cards(D) {
  D = { ...D, classes: D.classes.filter((c) => c.n > 0) };
  const it = (e) => !e ? '<p class="faint">No item in this class.</p>' : `
    <div class="fm-item"><div class="fm-item-h">${esc(e.cytokine)} <span>→</span> ${esc(e.cell_type)}<em>${esc(e.donor)}</em></div>
    <dl><dt>cells</dt><dd>${int(e.n_cells)}</dd><dt>reliability</dt><dd>${fmt(e.rel)}</dd><dt>donor agreement</dt><dd>${fmt(e.repro)}</dd>
    <dt>average-response fit</dt><dd>${fmt(e.ref_r)}</dd><dt>receptor</dt><dd>${e.receptor == null ? 'none known' : fmt(e.receptor, 3)}</dd>
    <dt>models passing</dt><dd>${e.passed} of ${e.of}</dd></dl></div>`;
  $('#cards').innerHTML = D.classes.map((c) => `<div class="card fm-card" style="--c:${CLS_COLOR[c.key]}">
    <h3><span>${esc(c.name)}</span><span class="mono faint">${pct(c.share)}</span></h3><p class="sub">${esc(c.desc)}</p>
    <div class="fm-meter"><i style="width:${(100 * (c.pass ?? 0)).toFixed(0)}%"></i></div><p class="foot">${pct(c.pass)} of models pass, on average</p>${it(c.example)}</div>`).join('');
}

function hbars(rows, { w = 520, labelW = 150, color = () => 'var(--s1)', tip = () => '', val = (r) => r.pass, fmtV = (v) => pct(v), max = 1 } = {}) {
  const bh = 18, gap = 6, h = rows.length * (bh + gap) + 6, x = lin(0, max, labelW, w - 46);
  let s = svgOpen(w, h);
  rows.forEach((r, i) => {
    const y = 4 + i * (bh + gap), v = val(r);
    s += `<g class="mark" data-tip="${esc(tip(r))}"><text x="${labelW - 8}" y="${y + bh - 5}" text-anchor="end" style="font-size:11.5px">${esc(r.name)}</text><rect x="${labelW}" y="${y}" width="${Math.max(x(v) - labelW, 1)}" height="${bh}" rx="3" fill="${color(r)}"/><text x="${x(v) + 5}" y="${y + bh - 5}" class="mono" style="font-size:11px">${fmtV(v)}</text></g>`;
  });
  return s + '</svg>';
}

function biology(D) {
  const cy = [...D.cytokines].sort((a, b) => b.pass - a.pass);
  const w = 560, h = 240, m = { l: 40, t: 12, r: 8, b: 30 }, bw = (w - m.l - m.r) / cy.length, y = lin(0, 1, h - m.b, m.t);
  let s = svgOpen(w, h);
  [0, 0.25, 0.5, 0.75, 1].forEach((t) => { s += `<line x1="${m.l}" x2="${w - m.r}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)"/><text x="${m.l - 6}" y="${y(t) + 4}" text-anchor="end" class="mono" style="font-size:10px">${pct(t)}</text>`; });
  cy.forEach((c, i) => {
    const [g, col] = GROUP(c.family), x = m.l + i * bw;
    s += `<g class="mark" data-tip="<b>${esc(c.name)}</b> · ${esc(c.family)}<br>${pct(c.pass)} of models pass<br>median reliability ${fmt(c.rel)}${c.is_cytokine === false ? '<br>not a cytokine' : ''}"><rect x="${x + 0.5}" y="${y(c.pass)}" width="${Math.max(bw - 1, 1)}" height="${y(0) - y(c.pass)}" fill="${col}" ${c.is_cytokine === false ? 'opacity=".35"' : ''}/></g>`;
  });
  s += `<text x="${m.l + (w - m.l - m.r) / 2}" y="${h - 6}" text-anchor="middle" style="font-size:11px;fill:var(--fg-3)">90 cytokines, easiest to hardest</text>`;
  $('#cyt').innerHTML = s + '</svg>' + `<p class="foot"><b>Easiest:</b> ${cy.slice(0, 5).map((c) => esc(c.name)).join(', ')}. <b>Hardest:</b> ${cy.slice(-5).reverse().map((c) => esc(c.name)).join(', ')}.</p>`;
  $('#cyt-leg').innerHTML = GROUP_ORDER.map((g) => `<span><i class="sw" style="--c:${GROUP(g === 'Interferons' ? 'interferon' : g === 'Common gamma chain' ? 'gamma chain' : g === 'IL-6 / gp130' ? 'gp130' : g === 'TNF superfamily' ? 'TNF' : g === 'IL-1 family' ? 'IL-1 family' : g === 'IL-10, IL-12, IL-17' ? 'IL-10' : 'x')[1]}"></i>${esc(g)}</span>`).join('');
  $('#rec').innerHTML = hbars(D.receptor, { color: () => 'var(--s1)', tip: (r) => `${int(r.n)} items · median reliability ${fmt(r.rel)}` });
  $('#lin').innerHTML = hbars(D.lineage.filter((r) => r.n > 20), { color: () => 'var(--s3)', tip: (r) => `${int(r.n)} items · median reliability ${fmt(r.rel)}` });
  const dn = [...D.donors].sort((a, b) => b.pass - a.pass);
  $('#don').innerHTML = hbars(dn, { labelW: 90, color: (r) => (r.high_isg ? 'var(--s7)' : 'var(--s0)'), tip: (r) => `${int(r.n)} items · median donor agreement ${fmt(r.repro)}` });
}

function rank(D) {
  const col = ['var(--s8)', 'var(--s4)', 'var(--s3)'];
  const w = 1000, h = 320, m = { l: 56, r: 16, t: 14, b: 46 }, x = lin(-5.5, 4.5, m.l, w - m.r), y = lin(0, 1, h - m.b, m.t);
  let s = svgOpen(w, h);
  [0, 0.25, 0.5, 0.75, 1].forEach((t) => { s += `<line x1="${m.l}" x2="${w - m.r}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)"/><text x="${m.l - 8}" y="${y(t) + 4}" text-anchor="end" class="mono" style="font-size:11px">${pct(t)}</text>`; });
  [-4, -2, 0, 2, 4].forEach((t) => { s += `<text x="${x(t)}" y="${h - m.b + 16}" text-anchor="middle" class="mono" style="font-size:11px">${sgn(t, 0).replace('+0', '0')}</text>`; });
  D.rank.forEach((b, i) => b.pts.filter((p) => p.x > -5.5).forEach((p) => {
    s += `<circle class="mark" data-tip="<b>${esc(p.name)}</b><br>${esc(b.band)}: ${pct(p.y)} passed" cx="${x(p.x)}" cy="${y(p.y)}" r="5" fill="${col[i]}" opacity=".85" stroke="var(--bg-2)" stroke-width="1.5"/>`;
  }));
  s += `<text x="${(m.l + w - m.r) / 2}" y="${h - 8}" text-anchor="middle">model ability on Parse (logits) →</text><text transform="translate(14 ${(m.t + h - m.b) / 2}) rotate(-90)" text-anchor="middle">share of items passed</text>`;
  $('#rankchart').innerHTML = s + '</svg>';
  $('#rank-leg').innerHTML = D.rank.map((b, i) => `<span><i class="sw" style="--c:${col[i]}"></i>${esc(b.band)} items · ρ ${fmt(b.rho, 2)}</span>`).join('');
}

function models(D) {
  const ms = D.models.filter((m) => m.pass != null);
  const keep = ms.filter((m, i) => i < 12 || /statetx|scgen|scvi_cf|mean_shift|control_mean|random_shift_s0/.test(m.rid));
  const row = (m) => `<tr${m.placement === 'anchored' ? ' class="faint"' : ''}><td>${esc(m.name)}</td><td class="num">${sgn(m.ability)}</td><td class="num">${pct(m.pass)}</td><td class="num">${fmt(m.r)}</td><td class="num">${fmt(m.r_sys)}</td></tr>`;
  $('#mtable').innerHTML = `<thead><tr><th>Model</th><th class="num">Ability</th><th class="num">Pass rate</th><th class="num">r with truth</th><th class="num">r after removing the average</th></tr></thead><tbody>${keep.map(row).join('')}</tbody>`;
  $('#mfoot').innerHTML = `The average response itself reaches r = ${fmt(D.meta.mean_shift_r)} with the truth, so a high raw r alone says little. The last column removes it: positive means the model adds information beyond the average.`;
}

export default async function () {
  const D = await getJSON('data/parse_failures.json');
  tiles(D); rule(D); heat(D); curves(D); stack(D); cards(D); biology(D); rank(D); models(D);
}

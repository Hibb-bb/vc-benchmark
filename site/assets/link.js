const pv = (p) => (p == null ? '–' : p < 1e-4 ? `< 1e-${Math.min(16, Math.ceil(-Math.log10(p)))}` : p.toFixed(2));
import { $, bench, getJSON, scatter, legend, famColor, famOrder, int, sgn, fmt, pct, esc } from './app.js';

export default async function link() {
  const b = await bench();
  const L = await getJSON('data/link.json');
  const ct = L.cell_type_table, dt = L.donor_type_table;
  const h = L.headline;
  const c1 = h.A_panel__B_context_screen__cell_type, c2 = h.A_panel__B_context_screen__donor_type;
  $('#link-ct').innerHTML = scatter(ct.map((r) => ({ x: r.a_diff, y: r.b_diff, xe: r.a_diff_se, ye: r.b_diff_se, label: r.type_n, tip: `<b>${esc(r.type_n)}</b><br>representation ${sgn(r.a_diff)} ± ${fmt(r.a_diff_se)} (${int(r.a_items)} cells)<br>perturbation ${sgn(r.b_diff)} ± ${fmt(r.b_diff_se)} (${int(r.b_items)} conditions)<br>${int(r.b_n_cells)} cells per condition` })),
    { w: 520, h: 400, xlabel: 'representation difficulty of the type (logits)', ylabel: 'perturbation difficulty in that type (logits)' });
  $('#link-ct-sub').textContent = `Spearman ${sgn(c1.spearman)} (p ${c1.spearman_p < 1e-4 ? '' : '='} ${pv(c1.spearman_p)}) over ${c1.n} types; partial Spearman given log cells per condition ${sgn(c1.spearman_partial_ncells)}.`;
  $('#link-dt').innerHTML = scatter(dt.map((r) => ({ x: r.a_diff, y: r.b_diff, xe: r.a_diff_se, ye: r.b_diff_se, label: '', color: 'var(--s7)', tip: `<b>${esc(r.donor)} · ${esc(r.type_n)}</b><br>representation ${sgn(r.a_diff)} (${int(r.a_items)} cells)<br>perturbation ${sgn(r.b_diff)} (${int(r.b_items)} conditions)<br>${int(r.b_n_cells)} cells per condition` })),
    { w: 520, h: 400, xlabel: 'representation difficulty of the context (logits)', ylabel: 'perturbation difficulty in that context (logits)', labels: false });
  $('#link-dt-sub').textContent = `Spearman ${sgn(c2.spearman)} (p ${c2.spearman_p < 1e-4 ? '' : '='} ${pv(c2.spearman_p)}) over ${c2.n} donor × type contexts; partial given log cells per condition ${sgn(c2.spearman_partial_ncells)}.`;
  $('#link-table').innerHTML = `<thead><tr><th>Cell type</th><th class="num">cells (A)</th><th class="num">A difficulty</th><th class="num">conditions (B)</th><th class="num">B difficulty</th><th class="num">B nobody passes</th><th class="num">cells per condition</th></tr></thead><tbody>${[...ct].sort((p, q) => p.a_diff - q.a_diff).map((r) => `<tr><td>${esc(r.type_n)}</td><td class="num">${int(r.a_items)}</td><td class="num">${sgn(r.a_diff)}</td><td class="num">${int(r.b_items)}</td><td class="num">${sgn(r.b_diff)}</td><td class="num">${pct(r.b_nobody, 0)}</td><td class="num">${int(r.b_n_cells)}</td></tr>`).join('')}</tbody>`;
  $('#link-levels').innerHTML = `<thead><tr><th>A scale</th><th>B split</th><th>B scale</th><th>level</th><th class="num">n</th><th class="num">Spearman</th><th class="num">p</th><th class="num">partial (log cells)</th><th class="num">Pearson</th></tr></thead><tbody>${Object.entries(L.levels).map(([k, c]) => { const [a, bb, lvl] = k.split('__'); const bs = bb.split('_'); return `<tr><td>${a.slice(2)}</td><td>${bs[1]}</td><td>${bs[2]}</td><td>${lvl.replace('_', ' × ')}</td><td class="num">${c.n}</td><td class="num">${sgn(c.spearman)}</td><td class="num">${pv(c.spearman_p)}</td><td class="num">${sgn(c.spearman_partial_ncells)}</td><td class="num">${sgn(c.pearson)}</td></tr>`; }).join('')}</tbody>`;

  const el = $('#enc-body');
  if (!L.encoders || !L.encoders.rows.length) {
    el.innerHTML = `<p class="empty">Shared-encoder runs are in progress on the cluster. This section fills in when the <code>latent_*</code> respondents have been scored on the perturbation screens and refit; it will show one point per encoder, representation ability against perturbation ability, with random projections marked as the null.</p>`;
    return;
  }
  const scaleKey = L.encoders.corr.pooled_context ? 'pooled_context' : 'pooled';
  const rows = L.encoders.rows.filter((r) => r.scale === scaleKey);
  const fams = famOrder('repr').filter((f) => rows.some((r) => r.family === f));
  const corr = L.encoders.corr[scaleKey], corr2 = L.encoders.corr[scaleKey + '_without_rproj'];
  el.innerHTML = `<div class="fig"><h3>Representation ability against perturbation ability of the same encoder</h3><p class="sub">${rows.length} encoders on the ${scaleKey === 'pooled_context' ? 'unseen-combination' : 'unseen-perturbation'} scale. Spearman ${sgn(corr.spearman)} (p ${corr.spearman_p < 1e-4 ? '' : '='} ${pv(corr.spearman_p)}); without random projections ${sgn(corr2.spearman)} (n = ${corr2.n}).</p>
    ${scatter(rows.map((r) => ({ x: r.a_ability, y: r.b_ability, xe: r.a_se, ye: r.b_se, label: r.name, color: famColor('repr', r.family), tip: `<b>${esc(r.name)}</b><br>representation ${sgn(r.a_ability)} ± ${fmt(r.a_se)}<br>perturbation ${sgn(r.b_ability)} ± ${fmt(r.b_se)} · passes ${pct(r.b_pass)} · outfit ${fmt(r.b_outfit)}` })), { w: 640, h: 440, xlabel: 'representation ability (logits)', ylabel: 'perturbation ability of the same encoder (logits)' })}
    ${legend('repr', fams)}</div>
    <div class="tbl-wrap" style="margin-top:1rem"><table><thead><tr><th>Encoder</th><th>Family</th><th class="num">A ability</th><th class="num">B ability</th><th class="num">B pass rate</th><th class="num">B outfit</th></tr></thead><tbody>${[...rows].sort((p, q) => q.a_ability - p.a_ability).map((r) => `<tr><td>${esc(r.name)}</td><td>${esc(r.family)}</td><td class="num">${sgn(r.a_ability)}</td><td class="num">${sgn(r.b_ability)}</td><td class="num">${pct(r.b_pass)}</td><td class="num">${fmt(r.b_outfit)}</td></tr>`).join('')}</tbody></table></div>`;
}

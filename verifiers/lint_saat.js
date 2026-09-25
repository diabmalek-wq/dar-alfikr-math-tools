// Typographic and option-set lint for the SAAT bank — the same checks the GAT
// bank runs, pointed at saat_items_a.js.
const all = [...require('./saat_items_a.js'), ...require('./saat_items_b.js'), ...require('./saat_items_c.js'), ...require('./saat_items_d.js'), ...require('./saat_items_e.js'), ...require('./saat_items_f.js'), ...require('./saat_items_g.js'), ...require('./saat_items_h.js'), ...require('./saat_items_i.js'), ...require('./saat_items_j.js'), ...require('./saat_items_k.js'), ...require('./saat_items_l.js'), ...require('./saat_items_m.js')];
let n = 0;
for (const it of all) {
  const s = it.stem, issues = [];
  if (!/[.?)]\s*$/.test(s)) issues.push('ends without . or ?');
  if (/\s{2,}/.test(s)) issues.push('double space');
  if (/ ,| \?| \./.test(s)) issues.push('space before punctuation');
  if (/[0-9](cm|km|kg|SAR)\b/.test(s)) issues.push('missing space before unit');
  if (/\bthe the\b|\ba a\b|\bof of\b|\bin in\b/.test(s)) issues.push('doubled word');
  if (/[a-z]\.[A-Z]/.test(s)) issues.push('missing space after full stop');
  if (/-\d/.test(s)) issues.push('hyphen used as a minus sign');
  if (issues.length) { n++; console.log(it.sig, '->', issues.join('; ')); console.log('    ' + s.slice(0, 120)); }
}
console.log('---', n, 'stems flagged of', all.length);
let m = 0;
for (const it of all) {
  const o = it.opts.filter(x => typeof x === 'string');
  if (o.length < 4) continue;
  // the unit check only means anything for numeric options
  if (!o.every(x => /\d/.test(x))) continue;
  if (o.some(x => x.includes(','))) continue;   // a coordinate pair is not a unit
  // a single letter pressed straight against a digit is algebra, not a unit:
  // "−7x" is a term and "2i" is a complex number. A real unit is spaced off.
  const unit = x => { const g = x.replace(/(\d)[a-zA-Z]$/, '$1').match(/([a-zA-Z%°²]+)\s*$/); return g ? g[1] : ''; };
  // a quadrant bearing ends in a compass letter — N, S, E or W is a direction,
  // not a unit, and every bearing in a set legitimately ends in a different one
  if (o.every(x => /^[NSEW]\s*\d+(\.\d+)?°\s*[NSEW]$/.test(x.trim()))) continue;
  const us = new Set(o.map(unit));
  if (us.size > 1) { m++; console.log('MIXED UNITS  ' + it.sig + '  ' + JSON.stringify(o)); }
  if (o.some(x => x !== x.trim())) { m++; console.log('PADDED       ' + it.sig); }
  if (new Set(o).size !== o.length) { m++; console.log('DUPLICATE    ' + it.sig); }
}
console.log('---', m, 'option sets flagged');
// every item that mentions a diagram must carry one, and the reverse
let d = 0;
for (const it of all) {
  const saysFig = /\b(below|shown)\b/.test(it.stem) && /\b(graph|diagram|trapezoid below|rhombus below)\b/.test(it.stem);
  if (it.fig && !/\bbelow\b|\bshown\b/.test(it.stem)) { d++; console.log('FIGURE UNREFERENCED ' + it.sig); }
  if (saysFig && !it.fig && !it.stemEq && !it.table) { d++; console.log('PROMISED A PICTURE  ' + it.sig); }
}
console.log('---', d, 'figure references flagged');

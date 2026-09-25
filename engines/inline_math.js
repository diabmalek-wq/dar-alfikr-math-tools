// ---------------------------------------------------------------------------
// INLINE MATHS — one parser, used by lesson_engine.js (slides + speaker notes)
// and docs_engine.js (Word documents).
//
// House rule: mathematics is typeset, never typed as code. Standalone
// expressions are real LaTeX images (make_math_*.py). Mathematics INSIDE a
// sentence is written in config strings as $...$ with a small LaTeX subset and
// rendered here as true typography: italic variables, upright digits and
// function names, a real minus sign, and genuine superscripts / subscripts
// (one level of nesting, e.g. $b^{\log_b x}$).
//
// Supported inside $...$:
//   letters (italic) · digits · ( ) [ ] | . ' · _x _{..} ^x ^{..}
//   \log \ln \sin \cos \tan \exp  (upright)   \text{..} (upright, verbatim)
//   \cdot \times \pm \le \ge \ne \approx \to \infty \Rightarrow \iff \in
//   \pi \Delta \quad \, \; \! \circ \ldots \{ \} \left \right
// Anything else throws, so an unsupported command can never print as code.
//
// lint(cfg) rejects code-style maths OUTSIDE $...$ in any prose string:
// _ ^ superscript digits, f(x), bare variables, relations, coordinates...
// ---------------------------------------------------------------------------

const MATH_FONT = "Cambria";

const UPRIGHT_FN = new Set(["log", "ln", "sin", "cos", "tan", "exp"]);
const REL = { le: "≤", leq: "≤", ge: "≥", geq: "≥", ne: "≠", neq: "≠", approx: "≈",
  to: "→", Rightarrow: "⇒", iff: "⟺", in: "∈" };
const BIN = { cdot: "·", times: "×", pm: "±" };
const SYM = { infty: "∞", pi: "π", Delta: "Δ", circ: "°", ldots: "…" };

// pos: 0 = baseline, "sup", "sub", "supsub" (subscript inside a superscript),
// "subsup" (superscript inside a subscript)
function combine(outer, inner) {
  if (!outer) return inner;
  if (outer === "sup" && inner === "sub") return "supsub";
  if (outer === "sub" && inner === "sup") return "subsup";
  if (outer === inner) return outer;             // x^{2^{n}} — kept one level
  throw new Error("inline maths: scripts nested more than two deep");
}

// Parse the INSIDE of one $...$ span into tokens {t, it, pos}
function parseMath(src) {
  const out = [];
  let i = 0;
  // TeX puts a thin space between an operator name and its argument (log x),
  // but not before a bracket (log(x)).
  const fnGap = {};
  const push = (t, it, pos) => {
    pos = pos || 0;
    if (fnGap[pos] && /^[A-Za-z0-9]/.test(t)) t = "\u2009" + t;
    fnGap[pos] = false;
    out.push({ t, it: !!it, pos });
  };
  // is the previous token something a binary operator can follow?
  const lastOperand = () => {
    const o = out[out.length - 1];
    if (!o) return false;
    const c = o.t.replace(/\s+$/, "").slice(-1);
    return /[A-Za-z0-9)\]|′!∞π°]/.test(c);
  };

  function readGroup(pos) {                       // after ^ or _
    while (src[i] === " ") i++;
    if (src[i] === "{") {
      i++;
      let depth = 1, start = i;
      while (i < src.length && depth) {
        if (src[i] === "{" && src[i - 1] !== "\\") depth++;
        else if (src[i] === "}" && src[i - 1] !== "\\") depth--;
        i++;
      }
      if (depth) throw new Error(`inline maths: unbalanced braces in "${src}"`);
      walk(src.slice(start, i - 1), pos);
    } else if (src[i] === "\\") {
      const m = /^\\([A-Za-z]+)/.exec(src.slice(i));
      if (!m) throw new Error(`inline maths: bad script in "${src}"`);
      i += m[0].length;
      walk("\\" + m[1], pos);
    } else {
      walk(src[i], pos); i++;
    }
  }

  function walk(s, pos) {
    const save = [src, i];
    src = s; i = 0;
    while (i < src.length) {
      const c = src[i];
      if (c === " ") { i++; continue; }
      if (c === "^" || c === "_") {
        i++;
        readGroup(combine(pos, c === "^" ? "sup" : "sub"));
        continue;
      }
      if (c === "{" ) {                           // bare grouping
        let depth = 1, start = ++i;
        while (i < src.length && depth) {
          if (src[i] === "{" && src[i - 1] !== "\\") depth++;
          else if (src[i] === "}" && src[i - 1] !== "\\") depth--;
          i++;
        }
        walk(src.slice(start, i - 1), pos);
        continue;
      }
      if (c === "\\") {
        const m = /^\\([A-Za-z]+|.)/.exec(src.slice(i));
        const cmd = m[1];
        i += m[0].length;
        if (cmd === "text") {
          while (src[i] === " ") i++;
          if (src[i] !== "{") throw new Error(`inline maths: \\text needs braces in "${src}"`);
          const end = src.indexOf("}", i);
          push(src.slice(i + 1, end), false, pos); i = end + 1; continue;
        }
        if (UPRIGHT_FN.has(cmd)) { push(cmd, false, pos); fnGap[pos] = true; continue; }
        if (REL[cmd]) { push(pos ? REL[cmd] : ` ${REL[cmd]} `, false, pos); continue; }
        if (BIN[cmd]) { push(pos || !lastOperand(pos) ? BIN[cmd] : ` ${BIN[cmd]} `, false, pos); continue; }
        if (SYM[cmd]) { push(SYM[cmd], false, pos); continue; }
        if (cmd === "quad") { push(" ", false, pos); continue; }
        if (cmd === ",") { push(" ", false, pos); continue; }
        if (cmd === ";" || cmd === " ") { push(" ", false, pos); continue; }
        if (cmd === "!" || cmd === "left" || cmd === "right") continue;
        if (cmd === "{" || cmd === "}" || cmd === "%" || cmd === "$") { push(cmd, false, pos); continue; }
        throw new Error(`inline maths: unsupported command \\${cmd} in "${src}" — use a LaTeX image`);
      }
      if (c === "-" || c === "+") {
        const g = c === "-" ? "−" : "+";
        push(!pos && lastOperand(pos) ? ` ${g} ` : g, false, pos); i++; continue;
      }
      if (c === "=" || c === "<" || c === ">") { push(pos ? c : ` ${c} `, false, pos); i++; continue; }
      if (c === ",") { push(pos ? "," : ", ", false, pos); i++; continue; }
      if (c === "'") { push("′", false, pos); i++; continue; }
      if (/[A-Za-z]/.test(c)) { push(c, true, pos); i++; continue; }
      push(c, false, pos); i++;                   // digits . ( ) [ ] | / : ; !
    }
    [src, i] = save;
  }

  walk(src, 0);
  // merge neighbours of identical style
  const merged = [];
  for (const o of out) {
    const p = merged[merged.length - 1];
    if (p && p.it === o.it && p.pos === o.pos) p.t += o.t; else merged.push({ ...o });
  }
  return merged;
}

// Split a whole string into plain and maths segments.
// returns [{t, math:false}] and [{t, math:true, it, pos}]
function split(text) {
  if (typeof text !== "string" || text.indexOf("$") < 0) return [{ t: text, math: false }];
  const parts = text.split("$");
  if (parts.length % 2 === 0) throw new Error(`inline maths: unbalanced $ in "${text}"`);
  const out = [];
  parts.forEach((p, k) => {
    if (k % 2 === 0) { if (p) out.push({ t: p, math: false }); }
    else parseMath(p).forEach((tok) => out.push({ ...tok, math: true }));
  });
  return out;
}

// Plain-text rendering (used where only a string can go, e.g. alt text)
function plain(text) {
  return split(text).map((s) => s.t).join("");
}

// ---------------------------------------------------------------- lint
const BAD = [
  [/[_^]/, "code-style _ or ^"],
  [/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀₁₂₃₄₅₆₇₈₉]/, "Unicode superscript/subscript"],
  [/\blog\b|\bln\b/, "log / ln written as text"],
  [/\b[A-Za-z](?:\^?-?1)?\([A-Za-z0-9]/, "function notation f(x)"],
  [/(^|[^A-Za-z’'.\-/])[b-zB-HJ-Z](?=$|[^A-Za-z’'])/, "bare variable letter"],
  [/[=<>≤≥≠≈∈∞√π]/, "relation or maths symbol"],
  [/−/, "minus sign"],
  [/\d\s*[+×÷*/]\s*\d/, "arithmetic"],
  [/\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)/, "coordinate pair"],
];

function lintString(s, where) {
  if (typeof s !== "string" || s.indexOf(" ") < 0) return [];  // asset keys, codes, slugs
  const parts = s.split("$");
  if (parts.length % 2 === 0) return [`${where}: unbalanced $ — "${s}"`];
  const errs = [];
  parts.forEach((p, k) => {
    if (k % 2 === 1) {
      try { parseMath(p); } catch (e) { errs.push(`${where}: ${e.message}`); }
      return;
    }
    // task labels (a) (b) and option letters (A)-(D) are not variables
    const q = p.replace(/\(([a-dA-D])\)/g, "( )").replace(/\b(Q\d|MP\.\d)\b/g, "");
    for (const [re, why] of BAD) {
      const m = re.exec(q);
      if (m) { errs.push(`${where}: ${why} outside $…$ → "${p.trim().slice(0, 90)}"`); break; }
    }
  });
  return errs;
}

function lint(cfg, skip = []) {
  const errs = [];
  const visit = (v, path) => {
    if (skip.some((k) => path.endsWith("." + k))) return;
    if (typeof v === "string") errs.push(...lintString(v, path));
    else if (Array.isArray(v)) v.forEach((x, k) => visit(x, `${path}[${k}]`));
    else if (v && typeof v === "object") Object.entries(v).forEach(([k, x]) => visit(x, `${path}.${k}`));
  };
  visit(cfg, "cfg");
  if (errs.length) {
    throw new Error(`MATHS TYPOGRAPHY LINT — ${errs.length} problem(s):\n  ` + errs.join("\n  "));
  }
}

// ---------------------------------------------------------------- pptx
// baseline values for pptxgenjs (value × 50 = OOXML thousandths of a percent)
const PPT_BASE = { sup: 600, sub: -500, supsub: 280, subsup: -200 };

// Convert one string into pptxgenjs runs. `o` = run options to carry
// (colour, bold, size...). Paragraph options (bullet, breakLine) are placed by
// the caller on the first / last run.
function pptRuns(text, o = {}) {
  return split(text).map((s) => {
    if (!s.math) return { text: s.t, options: { ...o } };
    const opt = { ...o, fontFace: MATH_FONT, italic: s.it };
    if (s.pos) opt.baseline = PPT_BASE[s.pos];
    return { text: s.t, options: opt };
  });
}

// Expand a pptxgenjs text argument (string or run array) into maths runs.
function expandPpt(arg) {
  if (typeof arg === "string") {
    return arg.indexOf("$") < 0 ? arg : pptRuns(arg);
  }
  if (!Array.isArray(arg)) return arg;
  const out = [];
  arg.forEach((item) => {
    const t = item.text;
    if (typeof t !== "string" || t.indexOf("$") < 0) { out.push(item); return; }
    const opts = item.options || {};
    const { bullet, breakLine, ...charOpts } = opts;
    const runs = pptRuns(t, charOpts);
    // pptxgenjs writes one <a:pPr> per run whenever a paragraph mixes runs of
    // different formatting (which every maths run does). Only the LAST such
    // pPr survives in LibreOffice/PowerPoint, so a `bullet:true` placed on the
    // first run of a multi-run paragraph is silently discarded. Rather than
    // fight that, a bulleted paragraph that contains maths gets its bullet
    // drawn as a literal glyph on the first run instead of via the `bullet`
    // paragraph option, which multi-run paragraphs cannot carry reliably.
    if (bullet) runs[0].text = "•   " + runs[0].text;
    runs.forEach((r, k) => {
      if (k === 0) Object.assign(r.options, pick(opts, ["paraSpaceAfter", "paraSpaceBefore", "indentLevel", "align"]));
      if (k === runs.length - 1 && breakLine) r.options.breakLine = true;
      out.push(r);
    });
  });
  return out;
}
const pick = (o, keys) => Object.fromEntries(keys.filter((k) => o[k] !== undefined).map((k) => [k, o[k]]));

// Speaker notes: pptxgenjs writes notes as ONE plain run, so the notes XML is
// rewritten after packing. Returns the <a:r> sequence for one notes string.
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const OOXML_BASE = { sup: 30000, sub: -25000, supsub: 14000, subsup: -10000 };
function notesRunsXml(text) {
  return split(text).map((s) => {
    let a = 'lang="en-US" dirty="0"';
    let latin = "";
    if (s.math) {
      if (s.it) a += ' i="1"';
      if (s.pos) a += ` baseline="${OOXML_BASE[s.pos]}"`;
      latin = `<a:latin typeface="${MATH_FONT}"/>`;
    }
    return `<a:r><a:rPr ${a}>${latin}</a:rPr><a:t>${esc(s.t)}</a:t></a:r>`;
  }).join("");
}

// ---------------------------------------------------------------- docx
// size in half-points (docx TextRun `size`)
function docxRuns(TextRunClass, o) {
  const text = o.text;
  if (typeof text !== "string" || text.indexOf("$") < 0) return [new TextRunClass(o)];
  const size = o.size || 21;
  return split(text).map((s) => {
    if (!s.math) return new TextRunClass({ ...o, text: s.t });
    const r = { ...o, text: s.t, font: MATH_FONT, italics: s.it };
    if (s.pos === "sup") r.superScript = true;
    else if (s.pos === "sub") r.subScript = true;
    else if (s.pos === "supsub") { r.size = Math.round(size * 0.58); r.position = `${(size / 2 * 0.2).toFixed(1)}pt`; }
    else if (s.pos === "subsup") { r.size = Math.round(size * 0.58); r.position = `${(-size / 2 * 0.05).toFixed(1)}pt`; }
    return new TextRunClass(r);
  });
}

module.exports = { split, parseMath, plain, lint, lintString, expandPpt, pptRuns, notesRunsXml, docxRuns, MATH_FONT };

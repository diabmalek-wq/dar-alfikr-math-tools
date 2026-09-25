// ---------------------------------------------------------------------------
// FIKR LESSON DECK ENGINE
//
// One config object per lesson produces a complete, house-rule-compliant deck.
// Everything the house rules demand is enforced here rather than re-typed:
//   · Dept logo top left, School logo top right, every slide
//   · Standards CODES ONLY, bottom-right corner
//   · Objectives and Essential Question quoted verbatim from the curriculum map
//   · Practice / Apply / Investigate — never Support / Core / Extension
//   · "Done when…", never "Success:"
//   · Four pillars: differentiation, adaptive routing, Saudi connection, exam link
//   · FIKR timings that must total 60
//   · Every expression scaled to one common type size (see eq())
//   · Speaker notes on every slide
//
// Adding a lesson = writing a config. No layout code.
// ---------------------------------------------------------------------------
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

const A = (f) => path.join(__dirname, f);
const IM = require("./inline_math");
let JSZip;
try { JSZip = require("jszip"); }
catch (e) { JSZip = require(path.join(path.dirname(require.resolve("pptxgenjs")), "..", "node_modules", "jszip")); }

const TEAL_DEEP = "0E4F4C", TEAL = "1E8F89", TEAL_BRIGHT = "3EB8B2";
const TEAL_TINT = "E7F5F4", TEAL_TINT2 = "CFEBE8", MAROON = "8A1B17";
const CHARCOAL = "222E2D", MUTED = "5C6E6C", WHITE = "FFFFFF", LINE = "D8E6E5";
const HEAD = "Cambria", BODY = "Calibri";

const SW = 13.333, SH = 7.5, MX = 0.45;
const DEPT_W = 1.7, DEPT_H = DEPT_W * (154 / 500), SCH = 0.72, LOGO_Y = 0.32;

const DEPT = A("dept_logo.png"), SCHOOL = A("school_logo.png");
const DEPT_W_LOGO = A("dept_logo_white.png"), SCHOOL_W_LOGO = A("school_logo_white.png");
const BG_LIGHT = A("bg_light.jpg"), BG_DARK = A("bg_dark.jpg");
const COGNIA = A("cognia_badge.png");
// Branding (9 Sep 2026): Cognia badge top-centre on the title slide; the school
// motto centred in the footer of every slide.
const MOTTO = "FAITH,  RIGHTEOUSNESS  AND  WISDOM";

function build(cfg) {
  const MATH = JSON.parse(fs.readFileSync(A(cfg.mathIndex), "utf8"));
  const GRAPH = cfg.graphIndex ? JSON.parse(fs.readFileSync(A(cfg.graphIndex), "utf8")) : {};

  const T = cfg.timings || { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };
  const total = T.t1 + T.t2 + T.t3 + T.t4 + T.t5 + T.t6;
  if (total !== 60 && total !== 40) {
    throw new Error(`FIKR timings total ${total}, must be 40 or 60 — ${cfg.out}`);
  }
  if (!cfg.objectives.length) throw new Error("objectives are required, verbatim from the map");
  if (!cfg.essentialQuestion) throw new Error("essential question is required, verbatim");
  // House rule: maths is typeset, never typed as code. Every prose string must
  // carry its maths inside $...$ — the build stops otherwise.
  IM.lint(cfg);

  const pres = new pptxgen();
  pres.defineLayout({ name: "WIDE", width: SW, height: SH });
  pres.layout = "WIDE";
  pres.author = "Dar Alfikr Schools — Mathematics Department";
  pres.title = cfg.deckTitle;

  // ---------------------------------------------------------------- helpers
  function base(dark, codes) {
    const s = pres.addSlide();
    // every text box on every slide renders $...$ as typeset maths
    const addText = s.addText.bind(s);
    s.addText = (t, o) => addText(IM.expandPpt(t), o);
    s.background = { path: dark ? BG_DARK : BG_LIGHT };
    s.addImage({ path: dark ? DEPT_W_LOGO : DEPT, x: MX, y: LOGO_Y, w: DEPT_W, h: DEPT_H,
      altText: "Mathematics Department logo" });
    s.addImage({ path: dark ? SCHOOL_W_LOGO : SCHOOL, x: SW - MX - SCH, y: LOGO_Y, w: SCH, h: SCH,
      altText: "Dar Alfikr Schools logo" });
    s.addText(cfg.footerLeft, { x: MX, y: SH - 0.4, w: 4.3, h: 0.3, fontFace: BODY, fontSize: 9,
      color: dark ? "BFD9D7" : MUTED, isTextBox: true, margin: 0 });
    s.addText(MOTTO, { x: SW / 2 - 1.75, y: SH - 0.4, w: 3.5, h: 0.3, fontFace: HEAD, fontSize: 8,
      bold: true, charSpacing: 1.2, color: dark ? "BFD9D7" : "1F3864", align: "center",
      isTextBox: true, margin: 0 });
    // house rule 2 — codes only, bottom corner (two lines allowed for the full list)
    const c = codes && codes.length ? codes : null;
    if (c) s.addText(c.join("  ·  "), {
      x: SW - MX - 4.3, y: SH - 0.52, w: 4.3, h: 0.42, fontFace: BODY, fontSize: 8,
      color: dark ? "BFD9D7" : MUTED, align: "right", valign: "bottom", isTextBox: true, margin: 0 });
    return s;
  }

  function title(s, t, sub, dark) {
    // The time pill starts at SW - MX - SCH - 1.78. A fixed 10.2in title box
    // runs underneath it, and a long title prints straight through the pill —
    // "The Method — Five Steps, and the Fifth Is Not Optional" did exactly
    // that. Stop the box short of the pill, then shrink the type until the
    // line fits rather than wrapping into the subtitle.
    const avail = (SW - MX - SCH - 1.78) - MX - 0.28;
    let fs = 30;
    while (fs > 20 && t.length * fs * 0.5 / 72 > avail) fs -= 1;
    s.addText(t, { x: MX, y: 1.28, w: avail, h: 0.68, fontFace: HEAD, fontSize: fs, bold: true,
      color: dark ? WHITE : CHARCOAL, isTextBox: true, margin: 0 });
    if (sub) s.addText(sub, { x: MX, y: 1.92, w: 10.4, h: 0.34, fontFace: BODY, italic: true,
      fontSize: 13, color: dark ? "CFE8E6" : MUTED, isTextBox: true, margin: 0 });
  }

  function phaseTag(s, num, name, time, dark) {
    s.addText(`PHASE ${num} · ${name}`, { x: MX, y: 0.95, w: 6.6, h: 0.26, fontFace: BODY,
      bold: true, fontSize: 10, charSpacing: 2, color: dark ? TEAL_BRIGHT : TEAL,
      isTextBox: true, margin: 0 });
    s.addShape("roundRect", { x: SW - MX - SCH - 1.78, y: 1.3, w: 1.55, h: 0.42, rectRadius: 0.06,
      fill: dark ? { color: WHITE, transparency: 82 } : { color: TEAL_DEEP },
      line: dark ? { color: TEAL_BRIGHT, width: 1 } : { type: "none" } });
    s.addText(time, { x: SW - MX - SCH - 1.78, y: 1.3, w: 1.55, h: 0.42, align: "center",
      valign: "middle", fontFace: BODY, bold: true, fontSize: 11, color: WHITE,
      isTextBox: true, margin: 0 });
  }

  // Scale, never a fixed height: every expression comes from one LaTeX document
  // at one point size, so a common k renders a fraction and a one-line
  // expression at the SAME type size. k = 1.0 is 12 pt.
  function eq(s, key, o) {
    const m = MATH[key];
    if (!m) throw new Error(`missing expression "${key}" in ${cfg.mathIndex}`);
    const k = o.k !== undefined ? o.k : 1.5;
    const w = m.win * k, h = m.hin * k;
    let x = o.x; if (o.cx !== undefined) x = o.cx - w / 2; if (o.rx !== undefined) x = o.rx - w;
    let y = o.y; if (o.cy !== undefined) y = o.cy - h / 2;
    s.addImage({ path: A(m.file), x, y, w, h, altText: o.alt || key });
    return { x, y, w, h };
  }

  function img(s, key, o) {
    const m = GRAPH[key];
    if (!m) throw new Error(`missing graph "${key}" in ${cfg.graphIndex}`);
    const w = o.w, h = w / m.aspect;
    let x = o.x; if (o.cx !== undefined) x = o.cx - w / 2;
    let y = o.y; if (o.cy !== undefined) y = o.cy - h / 2;
    s.addImage({ path: A(m.file), x, y, w, h, altText: o.alt || key });
    return h;
  }

  const bullets = (arr) => arr.map((t, i) => ({
    text: t, options: { bullet: true, breakLine: i < arr.length - 1 },
  }));

  function bar(s, label, text, o = {}) {
    const y = o.y, h = o.h || 0.5;
    s.addShape("roundRect", { x: MX, y, w: 12.43, h, rectRadius: 0.07,
      fill: { color: o.dark ? TEAL_DEEP : TEAL_TINT2 }, line: { type: "none" } });
    s.addText([
      { text: label + "   ", options: { bold: true, color: o.dark ? TEAL_BRIGHT : TEAL_DEEP } },
      { text, options: { color: o.dark ? WHITE : CHARCOAL } },
    ], { x: MX + 0.28, y, w: 11.9, h, valign: "middle", fontFace: BODY,
      fontSize: o.fs || 11.5, isTextBox: true, margin: 0 });
  }

  const ALL = cfg.codes.concat(cfg.mps);

  // ============================================================ 1 TITLE
  {
    const s = base(true);
    s.addImage({ path: COGNIA, x: SW / 2 - 0.55, y: 0.22, w: 1.1, h: 0.825,
      altText: "Cognia School of Distinction 2024" });
    s.addShape("ellipse", { x: 9.6, y: -2.3, w: 6.2, h: 6.2, fill: { color: TEAL, transparency: 62 }, line: { type: "none" } });
    s.addShape("ellipse", { x: -2.1, y: 4.9, w: 5.2, h: 5.2, fill: { color: MAROON, transparency: 76 }, line: { type: "none" } });
    s.addText(cfg.topicLine, { x: MX, y: 2.3, w: 11.0, h: 0.34, fontFace: BODY, fontSize: 12,
      charSpacing: 2.2, color: TEAL_BRIGHT, bold: true, isTextBox: true, margin: 0 });
    s.addText(cfg.lessonTitle, { x: MX, y: 2.62, w: 11.2, h: 1.5, fontFace: HEAD,
      fontSize: cfg.titleSize || 40, bold: true, color: WHITE, isTextBox: true, margin: 0,
      lineSpacingMultiple: 1.05 });
    s.addText(cfg.subtitle, { x: MX, y: 4.16, w: 10.8, h: 0.44, fontFace: BODY, fontSize: 16,
      color: "CFE8E6", isTextBox: true, margin: 0 });
    if (cfg.titleEq) eq(s, cfg.titleEq, { x: MX, y: 4.74, k: cfg.titleEqK || 2.6, alt: cfg.titleEqAlt });
    s.addShape("roundRect", { x: MX, y: 5.86, w: 8.4, h: 0.72, rectRadius: 0.09,
      fill: { color: WHITE, transparency: 92 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "Mr Malek Thiab", options: { bold: true, color: WHITE } },
      { text: `   |   ${cfg.grade}   |   ${cfg.week}   |   ${total} minutes`, options: { color: "CFE8E6" } },
    ], { x: MX + 0.28, y: 5.86, w: 8.0, h: 0.72, fontFace: BODY, fontSize: 12,
      valign: "middle", isTextBox: true, margin: 0 });
    s.addNotes(`FIKR ${total}-minute lesson: $${T.t1}+${T.t2}+${T.t3}+${T.t4}+${T.t5}+${T.t6}=${total}$ minutes including transitions. Standards for this lesson, from the curriculum map: ${ALL.join(", ")}. ${cfg.notes.cover || ""}`);
  }

  // ============================================================ 2 OBJECTIVES
  {
    const s = base(false, ALL);
    title(s, "Lesson Objectives", cfg.objectivesSub || "Quoted verbatim from the curriculum map");
    s.addShape("roundRect", { x: MX, y: 2.34, w: 9.85, h: 0.72, rectRadius: 0.09, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText([
      { text: "ESSENTIAL QUESTION   ", options: { bold: true, color: TEAL_BRIGHT } },
      { text: cfg.essentialQuestion, options: { color: WHITE } },
    ], { x: MX + 0.28, y: 2.34, w: 9.3, h: 0.72, valign: "middle", fontFace: BODY,
      fontSize: 12.5, isTextBox: true, margin: 0 });

    const n = cfg.objectives.length;
    const step = n <= 3 ? 0.82 : (n === 4 ? 0.7 : 0.6);
    let y = 3.3;
    cfg.objectives.forEach((t, i) => {
      s.addShape("ellipse", { x: MX, y, w: 0.44, h: 0.44, fill: { color: TEAL }, line: { type: "none" } });
      s.addText(String(i + 1), { x: MX, y, w: 0.44, h: 0.44, align: "center", valign: "middle",
        fontFace: HEAD, bold: true, fontSize: 15, color: WHITE, isTextBox: true, margin: 0 });
      s.addText(t, { x: MX + 0.66, y: y - 0.06, w: 9.1, h: step - 0.06, valign: "middle",
        fontFace: BODY, fontSize: n > 3 ? 13 : 14, color: CHARCOAL, isTextBox: true, margin: 0 });
      y += step;
    });

    s.addShape("roundRect", { x: MX, y: 6.32, w: 9.85, h: 0.72, rectRadius: 0.09, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
    s.addText([
      { text: "Assessed by:  ", options: { bold: true, color: TEAL_DEEP } },
      { text: `${cfg.assessments[0]} during practice, and ${cfg.assessments[1]} at the Mastery Gate — the two assessments named in the curriculum map for this lesson.`, options: { color: CHARCOAL } },
    ], { x: MX + 0.28, y: 6.32, w: 9.3, h: 0.72, valign: "middle", fontFace: BODY, fontSize: 11.5, isTextBox: true, margin: 0 });

    s.addShape("roundRect", { x: 10.5, y: 2.34, w: 2.4, h: 4.7, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText("FIKR CYCLE", { x: 10.5, y: 2.54, w: 2.4, h: 0.28, align: "center", fontFace: BODY,
      bold: true, fontSize: 10.5, charSpacing: 1.6, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
    [["1 Diagnose", T.t1], ["2 Instruction", T.t2], ["3 Practice", T.t3],
     ["4 Production", T.t4], ["5 Proof", T.t5], ["6 Product", T.t6]].forEach(([a, t], i) => {
      const ry = 3.1 + i * 0.62;
      s.addText(a, { x: 10.66, y: ry, w: 1.6, h: 0.26, fontFace: BODY, fontSize: 10.5, color: WHITE, isTextBox: true, margin: 0 });
      s.addText(`${t} min`, { x: 11.9, y: ry, w: 0.86, h: 0.26, align: "right", fontFace: BODY,
        fontSize: 9.5, color: "9FD6D2", isTextBox: true, margin: 0 });
    });
    s.addNotes(cfg.notes.objectives);
  }

  // ============================================================ 3 VOCABULARY
  {
    const s = base(false, ALL.slice(0, 2));
    title(s, "Key Vocabulary", cfg.vocabSub || `The ${cfg.vocabulary.length} terms the curriculum map lists for this lesson`);
    const v = cfg.vocabulary;
    if (v.length <= 3) {
      const cw = (12.43 - 0.28 * (v.length - 1)) / v.length;
      v.forEach((t, i) => {
        const cx = MX + i * (cw + 0.28);
        s.addShape("roundRect", { x: cx, y: 2.4, w: cw, h: 3.9, rectRadius: 0.1, fill: { color: i % 2 ? TEAL_TINT2 : TEAL_TINT }, line: { color: LINE, width: 1 } });
        s.addShape("roundRect", { x: cx, y: 2.4, w: cw, h: 0.62, rectRadius: 0.1, fill: { color: i % 2 ? TEAL : TEAL_DEEP }, line: { type: "none" } });
        s.addShape("rect", { x: cx, y: 2.82, w: cw, h: 0.2, fill: { color: i % 2 ? TEAL : TEAL_DEEP }, line: { type: "none" } });
        s.addText(t.term, { x: cx, y: 2.4, w: cw, h: 0.62, align: "center", valign: "middle", fontFace: HEAD, bold: true, fontSize: 16, color: WHITE, isTextBox: true, margin: 0 });
        s.addText(t.def, { x: cx + 0.3, y: 3.18, w: cw - 0.6, h: 1.5, fontFace: BODY, fontSize: 13, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
        if (t.eq) {
          s.addShape("roundRect", { x: cx + 0.3, y: 4.8, w: cw - 0.6, h: 0.8, rectRadius: 0.07, fill: { color: WHITE }, line: { type: "none" } });
          eq(s, t.eq, { cx: cx + cw / 2, cy: 5.2, k: t.k || 1.5 });
        }
      });
    } else {
      // Card height adapts to the number of rows so the grid never runs past
      // the bottom bar — 7 terms (three rows) must fit as cleanly as 6.
      const cols = 3, cw = 3.95, gp = 0.28;
      const nrows = Math.ceil(v.length / cols);
      const rh = Math.min(1.86, (4.15 - 0.2 * (nrows - 1)) / nrows);
      const fsT = nrows > 2 ? 13 : 14, fsD = nrows > 2 ? 10 : 11;
      v.forEach((t, i) => {
        const col = i % cols, row = Math.floor(i / cols);
        const cx = MX + col * (cw + gp), cy = 2.4 + row * (rh + 0.2);
        s.addShape("roundRect", { x: cx, y: cy, w: cw, h: rh, rectRadius: 0.1, fill: { color: row % 2 ? TEAL_TINT2 : TEAL_TINT }, line: { color: LINE, width: 1 } });
        s.addText(t.term, { x: cx + 0.26, y: cy + 0.16, w: cw - 0.52, h: 0.34, fontFace: HEAD, bold: true, fontSize: fsT, color: TEAL_DEEP, isTextBox: true, margin: 0 });
        s.addText(t.def, { x: cx + 0.26, y: cy + 0.54, w: cw - 0.52, h: rh - 0.66, fontFace: BODY, fontSize: fsD, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
      });
    }
    s.addNotes(cfg.notes.vocabulary);
  }

  // ============================================================ 4 PRIOR KNOWLEDGE
  {
    const s = base(false, ALL.slice(0, 2));
    title(s, "What You Already Know", cfg.priorSub);
    const cw = 3.95, gp = 0.28;
    cfg.prior.forEach((it, i) => {
      const cx = MX + i * (cw + gp);
      s.addShape("roundRect", { x: cx, y: 2.42, w: cw, h: 2.05, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
      s.addText(it.h, { x: cx + 0.26, y: 2.58, w: cw - 0.52, h: 0.34, fontFace: HEAD, bold: true, fontSize: 15, color: TEAL_DEEP, isTextBox: true, margin: 0 });
      if (it.eq) eq(s, it.eq, { cx: cx + cw / 2, cy: 3.24, k: 1.8 });
      s.addText(it.d, { x: cx + 0.26, y: 3.62, w: cw - 0.52, h: 0.7, fontFace: BODY, fontSize: 12, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
    });
    s.addShape("roundRect", { x: MX, y: 4.68, w: 12.43, h: 1.7, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText("THE ONE IDEA THAT CARRIES OVER", { x: MX + 0.3, y: 4.86, w: 7.9, h: 0.3, fontFace: BODY, bold: true, fontSize: 10.5, charSpacing: 1.5, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
    s.addText(cfg.carryOver, { x: MX + 0.3, y: 5.22, w: cfg.carryOverEq ? 6.5 : 11.8, h: 1.0, fontFace: BODY, fontSize: 13, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
    if (cfg.carryOverEq) eq(s, cfg.carryOverEq, { x: 7.6, cy: 5.6, k: 2.0 });
    s.addNotes(cfg.notes.prior);
  }

  // ============================================================ 5 DIAGNOSE
  {
    const s = base(false, ALL.slice(0, 2));
    phaseTag(s, "1", "INTELLIGENT DIAGNOSE", `${T.t1} min`, false);
    title(s, cfg.diagnose.title, cfg.diagnose.sub);
    cfg.diagnose.questions.forEach((q, i) => {
      const ry = 2.42 + i * 0.79;
      s.addShape("roundRect", { x: MX, y: ry, w: 12.43, h: 0.68, rectRadius: 0.08, fill: { color: i % 2 === 0 ? TEAL_TINT : WHITE }, line: { color: LINE, width: 1 } });
      s.addShape("ellipse", { x: MX + 0.22, y: ry + 0.15, w: 0.38, h: 0.38, fill: { color: TEAL }, line: { type: "none" } });
      s.addText(String(i + 1), { x: MX + 0.22, y: ry + 0.15, w: 0.38, h: 0.38, align: "center", valign: "middle", fontFace: HEAD, bold: true, fontSize: 13, color: WHITE, isTextBox: true, margin: 0 });
      if (q.eq) eq(s, q.eq, { x: MX + 0.86, cy: ry + 0.34, k: 1.5 });
      s.addText(q.t, { x: q.eq ? 6.0 : MX + 0.86, y: ry, w: q.eq ? 6.7 : 11.5, h: 0.68, valign: "middle", fontFace: BODY, fontSize: 13, color: CHARCOAL, isTextBox: true, margin: 0 });
    });
    bar(s, "ADAPTIVE ROUTING", cfg.diagnose.routing, { y: 6.4 });
    s.addNotes(cfg.notes.diagnose);
  }

  // ============================================================ 6..n INSTRUCTION
  cfg.instruction.forEach((sl) => {
    const s = base(sl.dark ? true : false, sl.codes || ALL.slice(0, 3));
    phaseTag(s, "2", sl.tag || "TARGETED INSTRUCTION", `${T.t2} min`, !!sl.dark);
    title(s, sl.title, sl.sub, !!sl.dark);
    if (sl.graph) {
      const gw = sl.graphW || 7.6;
      img(s, sl.graph, { x: sl.graphX !== undefined ? sl.graphX : MX, y: sl.graphY || 2.4, w: gw, alt: sl.graphAlt });
    }
    if (sl.panel) {
      const px = sl.panelX !== undefined ? sl.panelX : 8.3;
      const pw = sl.panelW || 4.58;
      s.addShape("roundRect", { x: px, y: 2.36, w: pw, h: sl.panelH || 4.0, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
      s.addText(sl.panel.h, { x: px + 0.26, y: 2.54, w: pw - 0.52, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
      s.addText(bullets(sl.panel.items), { x: px + 0.26, y: 2.9, w: pw - 0.52, h: (sl.panelH || 4.0) - 0.7, fontFace: BODY, fontSize: sl.panel.fs || 11.5, color: WHITE, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 9 });
    }
    if (sl.rows) {
      const TOP = sl.rowsTop || 2.36, rowH = sl.rowH || 0.62;
      const cw = sl.rowsCw || [6.2, 6.23];
      (sl.rowsHead || ["", ""]).forEach((t, j) => {
        const x0 = MX + cw.slice(0, j).reduce((a, b) => a + b, 0);
        s.addShape("rect", { x: x0, y: TOP, w: cw[j], h: 0.38, fill: { color: TEAL_DEEP }, line: { color: TEAL_DEEP, width: 1 } });
        s.addText(t, { x: x0 + 0.2, y: TOP, w: cw[j] - 0.4, h: 0.38, valign: "middle", fontFace: BODY, bold: true, fontSize: 11.5, color: WHITE, isTextBox: true, margin: 0 });
      });
      sl.rows.forEach((r, i) => {
        const ry = TOP + 0.38 + i * rowH;
        cw.forEach((w, j) => {
          s.addShape("rect", { x: MX + cw.slice(0, j).reduce((a, b) => a + b, 0), y: ry, w, h: rowH,
            fill: { color: i % 2 === 0 ? TEAL_TINT : WHITE }, line: { color: LINE, width: 1 } });
        });
        r.forEach((cell, j) => {
          const x0 = MX + cw.slice(0, j).reduce((a, b) => a + b, 0);
          if (typeof cell === "string") {
            s.addText(cell, { x: x0 + 0.24, y: ry, w: cw[j] - 0.48, h: rowH, valign: "middle", fontFace: BODY, fontSize: 12, color: CHARCOAL, isTextBox: true, margin: 0 });
          } else {
            eq(s, cell.eq, { x: x0 + 0.3, cy: ry + rowH / 2, k: cell.k || 1.25 });
          }
        });
      });
    }
    if (sl.bar) bar(s, sl.bar[0], sl.bar[1], { y: sl.barY || 6.4, dark: !!sl.dark, h: sl.barH });
    if (sl.warn) {
      s.addShape("roundRect", { x: MX, y: sl.warnY || 5.3, w: 12.43, h: 1.1, rectRadius: 0.1, fill: { color: WHITE }, line: { color: MAROON, width: 1.2 } });
      s.addText(sl.warn.h, { x: MX + 0.3, y: (sl.warnY || 5.3) + 0.14, w: 7.0, h: 0.28, fontFace: BODY, bold: true, fontSize: 10.5, charSpacing: 1.4, color: MAROON, isTextBox: true, margin: 0 });
      s.addText(sl.warn.d, { x: MX + 0.3, y: (sl.warnY || 5.3) + 0.48, w: sl.warn.eq ? 7.4 : 11.8, h: 0.5, fontFace: BODY, fontSize: 13, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
      if (sl.warn.eq) eq(s, sl.warn.eq, { rx: MX + 12.13, cy: (sl.warnY || 5.3) + 0.55, k: 1.8 });
    }
    s.addNotes(sl.notes);
  });

  // ============================================================ QUICK CHECK
  {
    const s = base(true, ALL.slice(0, 2));
    phaseTag(s, "2", "QUICK CHECK", "60 sec", true);
    title(s, "Whiteboards Up", "Before we move to practice", true);
    s.addShape("roundRect", { x: MX, y: 2.6, w: 12.43, h: 1.85, rectRadius: 0.12, fill: { color: WHITE }, line: { type: "none" } });
    s.addText(cfg.quickCheck.lead, { x: MX + 0.55, y: 2.6, w: cfg.quickCheck.leadW || 2.6, h: 1.85, valign: "middle", fontFace: HEAD, fontSize: 22, color: CHARCOAL, isTextBox: true, margin: 0 });
    eq(s, cfg.quickCheck.eq, { x: MX + 0.55 + (cfg.quickCheck.leadW || 2.6) + 0.2, cy: 3.52, k: cfg.quickCheck.k || 2.6 });
    s.addShape("roundRect", { x: MX, y: 4.72, w: 6.05, h: 1.62, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText("THINK", { x: MX + 0.3, y: 4.88, w: 5.4, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "9FD6D2", isTextBox: true, margin: 0 });
    s.addText(cfg.quickCheck.think, { x: MX + 0.3, y: 5.2, w: 5.45, h: 1.0, fontFace: BODY, fontSize: 13, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
    s.addShape("roundRect", { x: 6.85, y: 4.72, w: 6.03, h: 1.62, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText("DECISION RULE", { x: 7.15, y: 4.88, w: 5.4, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "9FD6D2", isTextBox: true, margin: 0 });
    s.addText(cfg.quickCheck.rule, { x: 7.15, y: 5.2, w: 5.45, h: 1.0, fontFace: BODY, fontSize: 13, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
    s.addNotes(cfg.notes.quickCheck);
  }

  // ============================================================ GUIDED
  {
    const s = base(false, ALL.slice(0, 3));
    phaseTag(s, "3", "PRACTICE — GUIDED", `${cfg.guided.mins || 4} min`, false);
    title(s, `${cfg.assessments[0]} — Together`, "Two problems, identical for everyone — the routes open up afterwards");
    cfg.guided.items.forEach((it, i) => {
      const ry = 2.42 + i * 2.05;
      s.addShape("roundRect", { x: MX, y: ry, w: 12.43, h: 1.85, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
      s.addShape("ellipse", { x: MX + 0.28, y: ry + 0.24, w: 0.46, h: 0.46, fill: { color: TEAL }, line: { type: "none" } });
      s.addText(String(i + 1), { x: MX + 0.28, y: ry + 0.24, w: 0.46, h: 0.46, align: "center", valign: "middle", fontFace: HEAD, bold: true, fontSize: 15, color: WHITE, isTextBox: true, margin: 0 });
      s.addShape("roundRect", { x: MX + 0.95, y: ry + 0.24, w: 3.3, h: 1.35, rectRadius: 0.08, fill: { color: WHITE }, line: { type: "none" } });
      eq(s, it.eq, { cx: MX + 0.95 + 1.65, cy: ry + 0.915, k: it.k || 2.2 });
      s.addText(it.t, { x: MX + 4.55, y: ry + 0.3, w: 7.4, h: 0.7, fontFace: BODY, fontSize: 14, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
      s.addText(`Hint: ${it.hint}`, { x: MX + 4.55, y: ry + 1.1, w: 7.4, h: 0.4, fontFace: BODY, italic: true, fontSize: 11.5, color: MUTED, isTextBox: true, margin: 0 });
    });
    bar(s, "FEEDBACK", "Worked live on the board, step by step. Self-mark and circle your OWN first error before we move on.", { y: 6.6 });
    s.addNotes(cfg.notes.guided);
  }

  // ============================================================ ROUTES
  {
    const s = base(false, ALL.slice(0, 3));
    phaseTag(s, "3", "PRACTICE — INDEPENDENT", `${cfg.routes.mins || 8} min`, false);
    title(s, "Your Turn — Choose Your Task", "Three routes, same destination. Start anywhere; switch whenever you want to.");
    // House rule 3: task names, never learner labels.
    const meta = [
      { label: "PRACTICE", sub: "Secure the method", head: "BFE0DD", tc: TEAL_DEEP, fill: TEAL_TINT },
      { label: "APPLY", sub: "Use it in context", head: TEAL, tc: WHITE, fill: TEAL_TINT2 },
      { label: "INVESTIGATE", sub: "Find out why", head: TEAL_DEEP, tc: WHITE, fill: TEAL_TINT },
    ];
    const cw = 3.95, gp = 0.28, TOP = 2.5;
    cfg.routes.tiers.forEach((t, i) => {
      const m = meta[i], cx = MX + i * (cw + gp);
      s.addShape("roundRect", { x: cx, y: TOP, w: cw, h: 3.55, rectRadius: 0.1, fill: { color: m.fill }, line: { color: LINE, width: 1 } });
      s.addShape("roundRect", { x: cx, y: TOP, w: cw, h: 0.68, rectRadius: 0.1, fill: { color: m.head }, line: { type: "none" } });
      s.addShape("rect", { x: cx, y: TOP + 0.48, w: cw, h: 0.2, fill: { color: m.head }, line: { type: "none" } });
      s.addText(m.label, { x: cx, y: TOP + 0.04, w: cw, h: 0.3, align: "center", fontFace: BODY, bold: true, fontSize: 12, charSpacing: 2, color: m.tc, isTextBox: true, margin: 0 });
      s.addText(m.sub, { x: cx, y: TOP + 0.33, w: cw, h: 0.28, align: "center", fontFace: HEAD, italic: true, fontSize: 11.5, color: m.tc, isTextBox: true, margin: 0 });
      s.addText(bullets(t.items), { x: cx + 0.24, y: TOP + 0.82, w: cw - 0.48, h: 1.92, fontFace: BODY, fontSize: 10.5, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 6 });
      s.addText(t.help, { x: cx + 0.24, y: TOP + 2.8, w: cw - 0.48, h: 0.4, fontFace: BODY, italic: true, fontSize: 10, color: TEAL_DEEP, isTextBox: true, margin: 0, valign: "top" });
      // house rule 3: "Done when…", never "Success:"
      s.addText(`Done when: ${t.done}`, { x: cx + 0.24, y: TOP + 3.14, w: cw - 0.48, h: 0.36, fontFace: BODY, italic: true, fontSize: 10, color: MUTED, isTextBox: true, margin: 0, valign: "top" });
      if (t.eq) {
        s.addShape("roundRect", { x: cx, y: 6.2, w: cw, h: 0.62, rectRadius: 0.07, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
        eq(s, t.eq, { cx: cx + cw / 2, cy: 6.51, k: 1.35 });
      }
    });
    s.addNotes(cfg.notes.routes);
  }

  // ============================================================ PRODUCTION (Saudi)
  {
    const s = base(true, ALL.slice(0, 3));
    phaseTag(s, "4", "PRODUCTION — FIRST DRAFT", `${T.t4} min`, true);
    title(s, cfg.production.title, cfg.production.sub, true);
    s.addShape("roundRect", { x: MX, y: 2.34, w: 6.6, h: 3.05, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText("THE SITUATION", { x: MX + 0.3, y: 2.5, w: 6.0, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "9FD6D2", isTextBox: true, margin: 0 });
    s.addText(cfg.production.situation, { x: MX + 0.3, y: 2.86, w: 6.0, h: 1.6, fontFace: BODY, fontSize: 12.5, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
    if (cfg.production.eq) {
      // Dark card behind the white expression — a translucent white card left
      // white maths almost unreadable. Card height follows the expression.
      const MATHX = JSON.parse(fs.readFileSync(cfg.mathIndex, "utf8"));
      const mE = MATHX[cfg.production.eq];
      const kE = cfg.production.eqK || 1.8;
      const hE = mE ? mE.hin * kE : 0.5;
      const cardH = Math.max(0.72, hE + 0.26);
      const cardY = 5.28 - cardH;
      s.addShape("roundRect", { x: MX + 0.3, y: cardY, w: 6.0, h: cardH, rectRadius: 0.07, fill: { color: TEAL_DEEP }, line: { color: TEAL_BRIGHT, width: 0.75 } });
      eq(s, cfg.production.eq, { cx: MX + 3.3, cy: cardY + cardH / 2, k: kE });
    }
    s.addShape("roundRect", { x: 7.35, y: 2.34, w: 5.53, h: 3.05, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText("YOUR TASK", { x: 7.63, y: 2.5, w: 5.0, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "9FD6D2", isTextBox: true, margin: 0 });
    s.addText(cfg.production.tasks.map((t, i) => ({ text: t, options: { breakLine: i < cfg.production.tasks.length - 1 } })), { x: 7.63, y: 2.86, w: 5.0, h: 2.4, fontFace: BODY, fontSize: 11.5, color: WHITE, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 8 });
    s.addShape("roundRect", { x: MX, y: 5.55, w: 6.6, h: 0.8, rectRadius: 0.08, fill: { color: WHITE, transparency: 86 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText(cfg.production.note, { x: MX + 0.28, y: 5.55, w: 6.05, h: 0.8, valign: "middle", fontFace: BODY, italic: true, fontSize: 11.5, color: "CFE8E6", isTextBox: true, margin: 0 });
    s.addShape("roundRect", { x: 7.35, y: 5.55, w: 5.53, h: 0.8, rectRadius: 0.08, fill: { color: WHITE, transparency: 86 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "AI IS A CRITIC, NOT A CALCULATOR — ", options: { bold: true, color: "9FD6D2" } },
      { text: cfg.production.aiPrompt, options: { color: WHITE } },
    ], { x: 7.6, y: 5.55, w: 5.05, h: 0.8, valign: "middle", fontFace: BODY, fontSize: 10.5, isTextBox: true, margin: 0 });
    s.addNotes(cfg.notes.production);
  }

  // ============================================================ GEOGEBRA
  {
    const s = base(false, ALL.slice(0, 2));
    phaseTag(s, "4", "PRODUCTION — EXPLORE", `within ${T.t4} min`, false);
    title(s, "Test Your Thinking in GeoGebra", cfg.geogebra.sub);
    // Left panel. Either the lesson's embedded GeoGebra clip (added AFTER
    // animate_deck.py by embed_geogebra.py, which needs this area empty) or a
    // still of the construction students are about to build. Never an
    // "EMBED AREA" placeholder, a fake QR square or a placeholder link — those
    // reached six live decks once (§23/§24).
    const g = cfg.geogebra;
    if (!g.clip) {
      if (!g.graph) throw new Error("geogebra: give either clip (embedded later) or graph (a still)");
      s.addShape("roundRect", { x: MX, y: 2.42, w: 7.5, h: 3.9, rectRadius: 0.1, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
      const gm = GRAPH[g.graph];
      const gh = 3.6, gw = Math.min(7.2, gh * gm.aspect);
      img(s, g.graph, { cx: MX + 3.75, y: 2.57, w: gw, alt: g.graphAlt });
    }
    s.addShape("roundRect", { x: 8.3, y: 2.42, w: 4.58, h: 1.5, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText([
      { text: "ON YOUR OWN DEVICE", options: { bold: true, fontSize: 11, charSpacing: 1.4, color: TEAL_BRIGHT, breakLine: true } },
      { text: "geogebra.org/graphing", options: { bold: true, fontSize: 20, color: WHITE, breakLine: true } },
      { text: "Open it and explore — no account needed.", options: { fontSize: 11, color: "CFE8E6" } },
    ], { x: 8.55, y: 2.42, w: 4.1, h: 1.5, valign: "middle", fontFace: BODY, isTextBox: true, margin: 0, paraSpaceAfter: 3 });
    s.addShape("roundRect", { x: 8.3, y: 4.1, w: 4.58, h: 2.22, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
    s.addText([
      { text: "Explore: ", options: { bold: true, color: MAROON } },
      { text: g.explore, options: { color: CHARCOAL } },
    ], { x: 8.55, y: 4.1, w: 4.1, h: 2.22, valign: "middle", fontFace: BODY, fontSize: 11.5, isTextBox: true, margin: 0 });
    s.addNotes(cfg.notes.geogebra);
  }

  // ============================================================ MASTERY GATE
  {
    const s = base(false, ALL.slice(0, 3));
    phaseTag(s, "5", `PROOF OF LEARNING — ${cfg.assessments[1].toUpperCase()}`, `${T.t5} min`, false);
    title(s, "On Your Own — No Notes, No Partner, No AI", "This one task decides where you go next");
    const gw = cfg.gate.graph ? 5.6 : 0;
    if (cfg.gate.graph) img(s, cfg.gate.graph, { x: MX, y: 2.4, w: gw, alt: cfg.gate.graphAlt });
    const bx = cfg.gate.graph ? MX + gw + 0.35 : MX;
    const bwid = cfg.gate.graph ? 12.88 - bx : 8.1;
    s.addShape("roundRect", { x: bx, y: 2.4, w: bwid, h: 3.55, rectRadius: 0.1, fill: { color: MAROON }, line: { type: "none" } });
    s.addText(cfg.assessments[1].toUpperCase(), { x: bx + 0.32, y: 2.58, w: bwid - 0.64, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "F5CFCD", isTextBox: true, margin: 0 });
    let gy = 2.96;
    cfg.gate.items.forEach((it, i) => {
      s.addText(`${i + 1}.  ${it.t}`, { x: bx + 0.32, y: gy, w: bwid - 0.64, h: 0.4, fontFace: BODY, fontSize: 12.5, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
      gy += 0.42;
      if (it.eq) { eq(s, it.eq, { x: bx + 0.6, y: gy, k: 1.7 }); gy += 0.72; }
      else gy += 0.12;
    });
    s.addText(cfg.gate.footer, { x: bx + 0.32, y: 5.4, w: bwid - 0.64, h: 0.42, fontFace: BODY, italic: true, fontSize: 11.5, color: "F5CFCD", isTextBox: true, margin: 0 });
    bar(s, "ADAPTIVE ROUTING", cfg.gate.routing, { y: 6.15 });
    s.addNotes(cfg.notes.gate);
  }

  // ============================================================ SMART PRODUCTION
  {
    const s = base(true, cfg.mps);
    phaseTag(s, "6", "SMART PRODUCTION — FINAL PRODUCT", `${T.t6} min`, true);
    title(s, "Build Something You're Proud Of", "Graded on clarity and reasoning — not correctness alone", true);
    cfg.smart.steps.forEach((c, i) => {
      const cw = 3.95, cx = MX + i * (cw + 0.28);
      s.addShape("roundRect", { x: cx, y: 2.6, w: cw, h: 2.8, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
      s.addShape("ellipse", { x: cx + 0.28, y: 2.84, w: 0.48, h: 0.48, fill: { color: MAROON }, line: { type: "none" } });
      s.addText(String(i + 1), { x: cx + 0.28, y: 2.84, w: 0.48, h: 0.48, align: "center", valign: "middle", fontFace: HEAD, bold: true, fontSize: 15, color: WHITE, isTextBox: true, margin: 0 });
      s.addText(c.h, { x: cx + 0.28, y: 3.46, w: cw - 0.56, h: 0.34, fontFace: HEAD, bold: true, fontSize: 14.5, color: WHITE, isTextBox: true, margin: 0 });
      s.addText(c.d, { x: cx + 0.28, y: 3.86, w: cw - 0.56, h: 1.35, fontFace: BODY, fontSize: 11.5, color: "CFE8E6", isTextBox: true, margin: 0, valign: "top" });
    });
    s.addShape("roundRect", { x: MX, y: 5.58, w: 12.43, h: 1.22, rectRadius: 0.1, fill: { color: WHITE, transparency: 85 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "Choose your format: ", options: { bold: true, color: "9FD6D2" } },
      { text: "a Canva one-pager, a photographed hand-written solution, or a 45-second voice note — all three are equally acceptable.", options: { color: WHITE, breakLine: true } },
      { text: "Published to: ", options: { bold: true, color: "9FD6D2" } },
      { text: cfg.smart.published, options: { color: WHITE, breakLine: true } },
      { text: "Reflection: ", options: { bold: true, color: "9FD6D2" } },
      { text: cfg.smart.reflection, options: { color: WHITE } },
    ], { x: MX + 0.3, y: 5.58, w: 11.85, h: 1.22, valign: "middle", fontFace: BODY, fontSize: 11.5, isTextBox: true, margin: 0 });
    s.addNotes(cfg.notes.smart);
  }

  // ============================================================ EXAM CONNECTIONS
  {
    const s = base(false, cfg.codes.slice(0, 2));
    title(s, "Where This Shows Up on Your Exams", "The same skill, three different question styles");
    const colours = [TEAL_DEEP, TEAL, MAROON];
    // Card height grows when an item carries e.question (added field, optional
    // and backward-compatible — older decks without it render as before).
    const hasQ = cfg.exams.some((e) => e.question);
    const hasSteps = cfg.exams.some((e) => e.steps && e.steps.length);
    // With worked steps the card must still end above the exam bar and the
    // footer (it used to run to 7.4 in and push the bar off the slide).
    const cardH = hasSteps ? 4.02 : (hasQ ? 4.02 : 3.6);
    const cardBottom = 2.4 + cardH;
    cfg.exams.forEach((e, i) => {
      const cw = 3.95, cx = MX + i * (cw + 0.28);
      s.addShape("roundRect", { x: cx, y: 2.4, w: cw, h: cardH, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
      s.addShape("roundRect", { x: cx, y: 2.4, w: cw, h: 0.9, rectRadius: 0.1, fill: { color: colours[i] }, line: { type: "none" } });
      s.addShape("rect", { x: cx, y: 3.0, w: cw, h: 0.3, fill: { color: colours[i] }, line: { type: "none" } });
      s.addText(e.code, { x: cx, y: 2.46, w: cw, h: 0.42, align: "center", fontFace: HEAD, bold: true, fontSize: 20, color: WHITE, isTextBox: true, margin: 0 });
      s.addText(e.full, { x: cx + 0.14, y: 2.88, w: cw - 0.28, h: 0.3, align: "center", fontFace: BODY, fontSize: 10, color: WHITE, isTextBox: true, margin: 0 });
      const body = [
        { text: "Skill tested", options: { bold: true, color: TEAL_DEEP, breakLine: true } },
        { text: e.skill, options: { breakLine: true } },
        { text: " ", options: { breakLine: true, fontSize: 4 } },
        { text: "Format", options: { bold: true, color: TEAL_DEEP, breakLine: true } },
        { text: e.fmt, options: { breakLine: true } },
        { text: " ", options: { breakLine: true, fontSize: 4 } },
        { text: "Practice tip", options: { bold: true, color: MAROON, breakLine: true } },
        { text: e.tip, options: {} },
      ];
      if (e.question) {
        body.push({ text: "", options: { breakLine: true, fontSize: 4 } });
        body.push({ text: "High-level item", options: { bold: true, color: TEAL_DEEP, breakLine: true } });
        body.push({ text: e.question, options: { italic: true, breakLine: !!(e.steps && e.steps.length) } });
      }
      if (e.steps && e.steps.length) {
        body.push({ text: "", options: { breakLine: true, fontSize: 3 } });
        body.push({ text: "Worked in steps", options: { bold: true, color: MAROON, breakLine: true } });
        e.steps.forEach((st, si) => {
          body.push({ text: `${si + 1}. ${st}`, options: { breakLine: si < e.steps.length - 1, fontSize: 9.5 } });
        });
      }
      s.addText(body, { x: cx + 0.26, y: 3.46, w: cw - 0.52, h: cardH - 1.16, fontFace: BODY, fontSize: hasSteps ? 9.5 : (hasQ ? 10 : 11), color: CHARCOAL, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: hasSteps ? 1.5 : (hasQ ? 2 : 3) });
    });
    if (cfg.examBar) {
      if (hasQ) bar(s, cfg.examBar[0], cfg.examBar[1], { y: cardBottom + 0.14, h: 0.46, fs: 10.5 });
      else bar(s, cfg.examBar[0], cfg.examBar[1], { y: 6.14, h: 0.62 });
    }
    s.addNotes(cfg.notes.exams);
  }

  // ============================================================ SUMMARY
  {
    const s = base(false, ALL);
    title(s, "Summary & Homework", cfg.lessonRef);
    s.addShape("roundRect", { x: MX, y: 2.4, w: 6.0, h: 3.9, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
    s.addText("WHAT YOU CAN NOW DO", { x: MX + 0.3, y: 2.58, w: 5.4, h: 0.28, fontFace: BODY, bold: true, fontSize: 10.5, charSpacing: 1.4, color: TEAL_DEEP, isTextBox: true, margin: 0 });
    s.addText(bullets(cfg.summary), { x: MX + 0.3, y: 2.96, w: 5.4, h: 3.1, fontFace: BODY, fontSize: 12, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 8 });
    s.addShape("roundRect", { x: 6.85, y: 2.4, w: 6.03, h: 3.9, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText("HOMEWORK & NEXT LESSON", { x: 7.15, y: 2.58, w: 5.4, h: 0.28, fontFace: BODY, bold: true, fontSize: 10.5, charSpacing: 1.4, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
    s.addText(cfg.homework.map((t, i) => ({
      text: t, options: { bullet: true, breakLine: i < cfg.homework.length - 1,
        color: i === cfg.homework.length - 1 ? "F5CFCD" : WHITE },
    })), { x: 7.15, y: 2.96, w: 5.4, h: 3.1, fontFace: BODY, fontSize: 12, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 10 });
    s.addNotes(cfg.notes.summary);
  }

  // ============================================================ CLOSING
  {
    const s = base(true);
    s.addShape("ellipse", { x: 4.6, y: 2.3, w: 4.1, h: 4.1, fill: { color: TEAL, transparency: 62 }, line: { type: "none" } });
    s.addText("Questions?", { x: 0, y: 3.0, w: SW, h: 1.0, align: "center", fontFace: HEAD, bold: true, fontSize: 40, color: WHITE, isTextBox: true, margin: 0 });
    s.addText(`Next lesson — ${cfg.nextLesson}`, { x: 0, y: 3.95, w: SW, h: 0.5, align: "center", fontFace: BODY, fontSize: 16, color: "CFE8E6", isTextBox: true, margin: 0 });
    s.addNotes("Close by naming one thing a student said today that changed how someone else was thinking.");
  }

  // pptxgenjs writes each slide's notes as one plain run; rewrite them so the
  // worked answers in the notes are typeset exactly like the slides.
  return pres.write({ outputType: "nodebuffer" })
    .then((buf) => JSZip.loadAsync(buf))
    .then(async (zip) => {
      const names = Object.keys(zip.files).filter((n) => /^ppt\/notesSlides\/notesSlide\d+\.xml$/.test(n));
      for (const n of names) {
        let xml = await zip.file(n).async("string");
        xml = xml.replace(/<a:r><a:rPr lang="en-US" dirty="0"\/><a:t>([\s\S]*?)<\/a:t><\/a:r>/g, (m, t) => {
          const raw = t.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"')
            .replace(/&apos;/g, "'").replace(/&amp;/g, "&");
          return raw.indexOf("$") < 0 ? m : IM.notesRunsXml(raw);
        });
        zip.file(n, xml);
      }
      const out = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
      fs.writeFileSync(A(cfg.out), out);
      console.log("wrote", cfg.out, `(${total} min)`);
    });
}

module.exports = { build };

// Pre-session home task — 4 slides, sent to students BEFORE the lesson.
// Flipped-classroom preparation (FIKR Phase 0): compress the content, then
// gauge readiness so the in-class Diagnose activity starts from evidence.
//   Grade 10 · Topic 1 · Lesson 1 — Key Features of Functions
//   Grade 11 · Topic 5 · Lesson 5-2 — Properties of Exponents and Radical Functions
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

const A = (f) => path.join(__dirname, f);
const M10 = JSON.parse(fs.readFileSync(A("math/_index.json"), "utf8"));
const M11 = JSON.parse(fs.readFileSync(A("math11/_index.json"), "utf8"));

const DEPT = A("dept_logo.png"), SCHOOL = A("school_logo.png");
const DEPT_W_LOGO = A("dept_logo_white.png"), SCHOOL_W_LOGO = A("school_logo_white.png");
const BG_LIGHT = A("bg_light.jpg"), BG_DARK = A("bg_dark.jpg");

const TEAL_DEEP = "0E4F4C", TEAL = "1E8F89", TEAL_BRIGHT = "3EB8B2";
const TEAL_TINT = "E7F5F4", TEAL_TINT2 = "CFEBE8", MAROON = "8A1B17";
const CHARCOAL = "222E2D", MUTED = "5C6E6C", WHITE = "FFFFFF", LINE = "D8E6E5";
const HEAD = "Cambria", BODY = "Calibri";

const SW = 13.333, SH = 7.5, MX = 0.45;
const DEPT_W = 1.7, DEPT_H = DEPT_W * (154 / 500), SCH = 0.72, LOGO_Y = 0.32;

// Grade-10 expressions were rendered at 460 dpi by make_math.py and carry only
// an aspect ratio; Grade-11 expressions were typeset by LaTeX at 500 dpi and
// carry a natural inch size. eq() below handles both.
function sized(MATH, key, o) {
  const m = MATH[key];
  if (!m) throw new Error("missing expression " + key);
  if (m.win !== undefined && o.k !== undefined) return { w: m.win * o.k, h: m.hin * o.k, file: m.file };
  const h = o.h !== undefined ? o.h : (m.hin !== undefined ? m.hin * (o.k || 1.4) : 0.4);
  return { w: h * m.aspect, h, file: m.file };
}

function build(cfg) {
  const MATH = cfg.math;
  const pres = new pptxgen();
  pres.defineLayout({ name: "WIDE", width: SW, height: SH });
  pres.layout = "WIDE";
  pres.author = "Dar Alfikr Schools — Mathematics Department";
  pres.title = cfg.deckTitle;

  function base(dark, standards) {
    const s = pres.addSlide();
    s.background = { path: dark ? BG_DARK : BG_LIGHT };
    s.addImage({ path: dark ? DEPT_W_LOGO : DEPT, x: MX, y: LOGO_Y, w: DEPT_W, h: DEPT_H, altText: "Mathematics Department logo" });
    s.addImage({ path: dark ? SCHOOL_W_LOGO : SCHOOL, x: SW - MX - SCH, y: LOGO_Y, w: SCH, h: SCH, altText: "Dar Alfikr Schools logo" });
    s.addText(cfg.footerLeft, {
      x: MX, y: SH - 0.4, w: 5.6, h: 0.3, fontFace: BODY, fontSize: 9,
      color: dark ? "BFD9D7" : MUTED, isTextBox: true, margin: 0,
    });
    s.addText((standards || cfg.codes).join("  ·  "), {
      x: SW - MX - 5.4, y: SH - 0.4, w: 5.4, h: 0.3, fontFace: BODY, fontSize: 9,
      color: dark ? "BFD9D7" : MUTED, align: "right", isTextBox: true, margin: 0,
    });
    return s;
  }

  function eq(s, key, o) {
    const m = sized(MATH, key, o);
    let x = o.x;
    if (o.cx !== undefined) x = o.cx - m.w / 2;
    let y = o.y;
    if (o.cy !== undefined) y = o.cy - m.h / 2;
    s.addImage({ path: A(m.file), x, y, w: m.w, h: m.h, altText: o.alt || key });
    return { x, y, w: m.w, h: m.h };
  }

  function stepBadge(s, x, y, n, dark) {
    s.addShape("ellipse", { x, y, w: 0.44, h: 0.44, fill: { color: dark ? MAROON : TEAL }, line: { type: "none" } });
    s.addText(String(n), { x, y, w: 0.44, h: 0.44, align: "center", valign: "middle", fontFace: HEAD, bold: true, fontSize: 14, color: WHITE, isTextBox: true, margin: 0 });
  }

  // ---------------------------------------------------- 1 · COVER
  {
    const s = base(true);
    s.addShape("ellipse", { x: 9.6, y: -2.3, w: 6.2, h: 6.2, fill: { color: TEAL, transparency: 62 }, line: { type: "none" } });
    s.addShape("ellipse", { x: -2.1, y: 4.9, w: 5.2, h: 5.2, fill: { color: MAROON, transparency: 76 }, line: { type: "none" } });

    s.addText("BEFORE THE LESSON · HOME TASK · 10 MINUTES", {
      x: MX, y: 2.2, w: 10.5, h: 0.34, fontFace: BODY, fontSize: 12.5, charSpacing: 2.4,
      color: TEAL_BRIGHT, bold: true, isTextBox: true, margin: 0,
    });
    s.addText(cfg.title, {
      x: MX, y: 2.56, w: 11.4, h: 1.5, fontFace: HEAD, fontSize: 38, bold: true,
      color: WHITE, isTextBox: true, margin: 0, lineSpacingMultiple: 1.05,
    });
    s.addText(cfg.coverSub, {
      x: MX, y: 4.1, w: 10.8, h: 0.44, fontFace: BODY, fontSize: 15.5,
      color: "CFE8E6", isTextBox: true, margin: 0,
    });

    s.addShape("roundRect", { x: MX, y: 4.76, w: 12.43, h: 1.0, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "Why you are doing this:  ", options: { bold: true, color: "9FD6D2" } },
      { text: "we start the lesson with a 5-question check. This page tells you exactly what that check will ask, so you can walk in ready instead of guessing.", options: { color: WHITE } },
    ], { x: MX + 0.3, y: 4.76, w: 11.85, h: 1.0, valign: "middle", fontFace: BODY, fontSize: 13, isTextBox: true, margin: 0 });

    s.addShape("roundRect", { x: MX, y: 6.02, w: 8.2, h: 0.7, rectRadius: 0.09, fill: { color: WHITE, transparency: 92 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "Mr Malek Thiab", options: { bold: true, color: WHITE } },
      { text: `   |   ${cfg.grade}   |   ${cfg.week || "Week 2 · Semester 1, 2026–27"}   |   Submit on the LMS before class`, options: { color: "CFE8E6" } },
    ], { x: MX + 0.28, y: 6.02, w: 7.8, h: 0.7, fontFace: BODY, fontSize: 11.5, valign: "middle", isTextBox: true, margin: 0 });
  }

  // ---------------------------------------------------- 2 · THE ONE IDEA
  {
    const s = base(false);
    s.addText("WATCH FIRST · 4 MINUTES", {
      x: MX, y: 0.95, w: 6.4, h: 0.26, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 2, color: TEAL, isTextBox: true, margin: 0 });
    s.addText(cfg.ideaTitle, {
      x: MX, y: 1.28, w: 10.2, h: 0.68, fontFace: HEAD, fontSize: 30, bold: true, color: CHARCOAL, isTextBox: true, margin: 0 });
    s.addText(cfg.ideaSub, {
      x: MX, y: 1.92, w: 10.2, h: 0.34, fontFace: BODY, italic: true, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });

    // video card
    s.addShape("roundRect", { x: MX, y: 2.4, w: 4.5, h: 2.5, rectRadius: 0.1, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText("YOUR VIDEO", { x: MX + 0.3, y: 2.58, w: 3.9, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
    s.addText(cfg.videoTitle, { x: MX + 0.3, y: 2.94, w: 3.9, h: 0.8, fontFace: HEAD, bold: true, fontSize: 16, color: WHITE, isTextBox: true, margin: 0, valign: "top" });
    s.addShape("roundRect", { x: MX + 0.3, y: 3.82, w: 3.9, h: 0.5, rectRadius: 0.07, fill: { color: WHITE, transparency: 84 }, line: { type: "none" } });
    s.addText("LMS  ›  Paste video link here", { x: MX + 0.3, y: 3.82, w: 3.9, h: 0.5, align: "center", valign: "middle", fontFace: BODY, italic: true, fontSize: 11, color: "CFE8E6", isTextBox: true, margin: 0 });
    s.addText("4 minutes · 2 questions inside the video", {
      x: MX + 0.3, y: 4.42, w: 3.9, h: 0.34, fontFace: BODY, fontSize: 11, color: "9FD6D2", isTextBox: true, margin: 0, valign: "top" });

    // the idea
    s.addShape("roundRect", { x: 5.3, y: 2.4, w: 7.58, h: 2.5, rectRadius: 0.1, fill: { color: TEAL_TINT }, line: { color: LINE, width: 1 } });
    s.addText("THE ONE IDEA", { x: 5.6, y: 2.58, w: 7.0, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: TEAL_DEEP, isTextBox: true, margin: 0 });
    s.addText(cfg.ideaText, { x: 5.6, y: 2.94, w: 7.0, h: 0.8, fontFace: BODY, fontSize: 13.5, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
    s.addShape("roundRect", { x: 5.6, y: 3.8, w: 7.0, h: 0.94, rectRadius: 0.07, fill: { color: WHITE }, line: { type: "none" } });
    eq(s, cfg.ideaEq, { cx: 5.6 + 3.5, cy: 4.27, k: cfg.ideaEqK, h: cfg.ideaEqH, alt: cfg.ideaEqAlt });

    // three things to remember
    cfg.recall.forEach((r, i) => {
      const cw = 3.95, cx = MX + i * (cw + 0.28);
      s.addShape("roundRect", { x: cx, y: 5.12, w: cw, h: 1.6, rectRadius: 0.1, fill: { color: i === 1 ? TEAL_TINT2 : TEAL_TINT }, line: { color: LINE, width: 1 } });
      s.addText(r.h, { x: cx + 0.26, y: 5.26, w: cw - 0.52, h: 0.3, fontFace: HEAD, bold: true, fontSize: 13, color: TEAL_DEEP, isTextBox: true, margin: 0 });
      eq(s, r.eq, { cx: cx + cw / 2, cy: 5.88, k: 1.5, h: 0.36 });
      s.addText(r.d, { x: cx + 0.26, y: 6.18, w: cw - 0.52, h: 0.46, fontFace: BODY, fontSize: 10.5, color: CHARCOAL, isTextBox: true, margin: 0, valign: "top" });
    });
  }

  // ---------------------------------------------------- 3 · WORKED EXAMPLE
  {
    const s = base(false);
    s.addText("STUDY THIS · 3 MINUTES", {
      x: MX, y: 0.95, w: 6.4, h: 0.26, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 2, color: TEAL, isTextBox: true, margin: 0 });
    s.addText("One Example, Every Step Shown", {
      x: MX, y: 1.28, w: 10.2, h: 0.68, fontFace: HEAD, fontSize: 30, bold: true, color: CHARCOAL, isTextBox: true, margin: 0 });
    s.addText("Cover the right-hand column, try it yourself, then check.", {
      x: MX, y: 1.92, w: 10.2, h: 0.34, fontFace: BODY, italic: true, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });

    const rowH = 0.86, TOP = 2.42;
    cfg.worked.forEach((w, i) => {
      const y = TOP + i * (rowH + 0.12);
      s.addShape("roundRect", { x: MX, y, w: 12.43, h: rowH, rectRadius: 0.08, fill: { color: i % 2 === 0 ? TEAL_TINT : WHITE }, line: { color: LINE, width: 1 } });
      stepBadge(s, MX + 0.24, y + (rowH - 0.44) / 2, i + 1);
      if (w.eq) eq(s, w.eq, { x: MX + 0.95, cy: y + rowH / 2, k: 1.5, h: 0.42 });
      s.addText(w.say, { x: 6.1, y, w: 6.6, h: rowH, valign: "middle", fontFace: BODY, fontSize: 12.5, color: CHARCOAL, isTextBox: true, margin: 0 });
    });

    const barY = TOP + cfg.worked.length * (rowH + 0.12) + 0.1;
    s.addShape("roundRect", { x: MX, y: barY, w: 12.43, h: 0.62, rectRadius: 0.08, fill: { color: TEAL_DEEP }, line: { type: "none" } });
    s.addText([
      { text: "The mistake most people make:  ", options: { bold: true, color: TEAL_BRIGHT } },
      { text: cfg.misconception, options: { color: WHITE } },
    ], { x: MX + 0.3, y: barY, w: 11.85, h: 0.62, valign: "middle", fontFace: BODY, fontSize: 12, isTextBox: true, margin: 0 });
  }

  // ---------------------------------------------------- 4 · READINESS CHECK
  {
    const s = base(true);
    s.addText("READINESS CHECK · 3 MINUTES", {
      x: MX, y: 0.95, w: 6.4, h: 0.26, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 2, color: TEAL_BRIGHT, isTextBox: true, margin: 0 });
    s.addText("Four Questions — Answer Before Class", {
      x: MX, y: 1.28, w: 10.2, h: 0.68, fontFace: HEAD, fontSize: 30, bold: true, color: WHITE, isTextBox: true, margin: 0 });
    s.addText("This is not graded. It tells me what to teach first — an honest answer helps you more than a lucky one.", {
      x: MX, y: 1.92, w: 11.4, h: 0.34, fontFace: BODY, italic: true, fontSize: 13, color: "CFE8E6", isTextBox: true, margin: 0 });

    cfg.check.forEach((q, i) => {
      const y = 2.46 + i * 0.86;
      s.addShape("roundRect", { x: MX, y, w: 8.6, h: 0.72, rectRadius: 0.08, fill: { color: WHITE }, line: { color: TEAL_BRIGHT, width: 1 } });
      stepBadge(s, MX + 0.22, y + 0.14, i + 1, true);
      // Text starts clear of the expression, however wide the expression is.
      let tx = MX + 0.86;
      if (q.eq) {
        const b = eq(s, q.eq, { x: MX + 0.86, cy: y + 0.36, k: 1.4, h: 0.4 });
        tx = Math.max(4.3, (b && b.x !== undefined ? b.x + b.w : 4.3) + 0.25);
      }
      s.addText(q.t, { x: tx, y, w: MX + 8.6 - 0.2 - tx, h: 0.72, valign: "middle", fontFace: BODY, fontSize: 12, color: CHARCOAL, isTextBox: true, margin: 0 });
    });

    s.addShape("roundRect", { x: 9.4, y: 2.46, w: 3.48, h: 3.44, rectRadius: 0.1, fill: { color: WHITE, transparency: 88 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText("HOW TO SUBMIT", { x: 9.68, y: 2.64, w: 2.95, h: 0.28, fontFace: BODY, bold: true, fontSize: 10, charSpacing: 1.4, color: "9FD6D2", isTextBox: true, margin: 0 });
    s.addText([
      { text: "Type your four answers into the LMS form — one line each.", options: { bullet: true, breakLine: true } },
      { text: "If you are stuck on one, write “not sure yet” and say what confused you. That is a useful answer.", options: { bullet: true, breakLine: true } },
      { text: "Due: before the bell. It takes three minutes.", options: { bullet: true } },
    ], { x: 9.68, y: 3.0, w: 2.95, h: 2.7, fontFace: BODY, fontSize: 11.5, color: WHITE, isTextBox: true, margin: 0, valign: "top", paraSpaceAfter: 9 });

    s.addShape("roundRect", { x: MX, y: 6.06, w: 12.43, h: 0.66, rectRadius: 0.08, fill: { color: WHITE, transparency: 86 }, line: { color: TEAL_BRIGHT, width: 1 } });
    s.addText([
      { text: "In class we start with:  ", options: { bold: true, color: "9FD6D2" } },
      { text: cfg.nextStep, options: { color: WHITE } },
    ], { x: MX + 0.3, y: 6.06, w: 11.85, h: 0.66, valign: "middle", fontFace: BODY, fontSize: 12, isTextBox: true, margin: 0 });
  }

  return pres.writeFile({ fileName: A(cfg.out) }).then(() => console.log("wrote", cfg.out));
}

// =====================================================================
const GR10 = {
  math: M10,
  out: "PreSession_Gr10_T1_L1_Key_Features_of_Functions.pptx",
  deckTitle: "Pre-Session Task — Key Features of Functions (Grade 10)",
  title: "Key Features of Functions",
  grade: "Grade 10",
  footerLeft: "Pre-session task · Grade 10 · Algebra II · Topic 1 · Lesson 1",
  codes: ["HSF.IF.B.4", "HSF.IF.B.6", "HSF.IF.C.7", "MP.4", "MP.5"],
  coverSub: "Everything a graph can tell you — and how fast something is changing",
  ideaTitle: "A Graph Is a Sentence About Change",
  ideaSub: "Read it left to right, the same way you read a line of text",
  ideaText: "Every graph answers three questions: which inputs are allowed (domain), which outputs come back (range), and how fast the output changes as the input moves. That last one has a name: average rate of change.",
  ideaEq: "aroc_def",
  ideaEqH: 0.5,
  ideaEqAlt: "Average rate of change equals f of b minus f of a, over b minus a",
  recall: [
    { h: "A point", eq: "pk_point", d: "Across first, then up or down." },
    { h: "Slope", eq: "pk_slope", d: "Rise for every step across." },
    { h: "Function notation", eq: "pk_sub", d: "Put 3 in, read the answer out." },
  ],
  worked: [
    { eq: "f_lin", say: "Start with the line. Its graph runs from x = −4 to x = 6." },
    { eq: "lin_yint", say: "The y-intercept: where the line crosses the vertical axis." },
    { eq: "lin_zero", say: "The zero: where the line crosses the horizontal axis, so the output is 0." },
    { eq: "lin_domain", say: "The domain in interval notation — square brackets, because both ends are included." },
  ],
  misconception: "reading the zero off the wrong axis. The zero is where the OUTPUT is zero — that is the horizontal axis crossing.",
  check: [
    { t: "What does the y-intercept of a graph tell you?" },
    { t: "Write this domain in interval notation.", eq: "lin_domain" },
    { t: "Does a square bracket include the endpoint, or exclude it?" },
    { t: "In one sentence: what does “average rate of change” measure?" },
  ],
  nextStep: "a 5-question Quizizz on a linear graph — the same four ideas you have just met. Then we go straight into reading key features together.",
};

const GR11 = {
  math: M11,
  out: "PreSession_Gr11_T5_L2_Properties_of_Exponents_and_Radical_Functions.pptx",
  deckTitle: "Pre-Session Task — Properties of Exponents and Radical Functions (Grade 11)",
  title: "Properties of Exponents\nand Radical Functions",
  grade: "Grade 11",
  footerLeft: "Pre-session task · Grade 11 · Algebra II · Topic 5 · Lesson 5-2",
  codes: ["HSA.SSE.A.1", "HSA.SSE.A.2", "HSN.RN.A.1", "HSN.RN.A.2", "MP.2", "MP.7"],
  coverSub: "A radical is an exponent in disguise — once you see that, nothing here is new",
  ideaTitle: "A Radical Is an Exponent in Disguise",
  ideaSub: "The index goes downstairs; the power stays upstairs",
  ideaText: "You already know every exponent rule. Today's lesson does not add a single new one. It only shows you that a radical is a fraction exponent wearing a different costume — so all your old rules still apply.",
  ideaEq: "def_deep",
  ideaEqK: 1.9,
  ideaEqAlt: "a to the m over n equals the nth root of a to the m, equals the nth root of a all to the m",
  recall: [
    { h: "Product rule", eq: "pk_prod", d: "Same base, multiply → add the exponents." },
    { h: "Square roots", eq: "pk_square", d: "The number that squares to the radicand." },
    { h: "nth roots", eq: "pk_root", d: "The index says which root to take." },
  ],
  worked: [
    { eq: "w_start", say: "Start here. The index is 3, so you hunt for perfect CUBES — not squares." },
    { eq: "w_split", say: "Split it: 54 = 27 × 2, and divide each variable exponent by 3." },
    { eq: "w_end", say: "Everything that divided exactly comes out. The remainder stays inside." },
    { eq: "r_warn", say: "And the rule that does NOT exist: a radical of a sum never splits." },
  ],
  misconception: "hunting for perfect squares out of habit, whatever the index says. Read the index first, every single time.",
  check: [
    { t: "Write this using a rational exponent instead of a radical.", eq: "d1" },
    { t: "Evaluate this without a calculator.", eq: "d2" },
    { t: "Simplify this fully.", eq: "d3" },
    { t: "In one sentence: which part of the fraction exponent becomes the index?" },
  ],
  nextStep: "a 5-question Quizizz on exactly these skills. Then the new content — clearing a radical out of a denominator using its conjugate.",
};

module.exports = { build };

if (require.main === module) {
  (async () => {
    await build(GR10);
    await build(GR11);
  })();
}

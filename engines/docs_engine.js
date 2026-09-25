// ---------------------------------------------------------------------------
// LESSON DOCUMENT ENGINE
// From one config: FIKR lesson plan · Lesson plan 2026/27 · classwork ·
// differentiation activity · PBL task sheet.
// Branding, standards codes, name/date block and house rules enforced here.
// ---------------------------------------------------------------------------
const {
  Document, Packer, Paragraph: DocxParagraph, TextRun: DocxTextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType, Header, Footer,
  ImageRun, VerticalAlign, PageOrientation, PageNumber,
} = require("docx");
const fs = require("fs");
const path = require("path");
const IM = require("./inline_math");

// House rule: maths is typeset, never typed as code. Every text run in these
// documents goes through the inline-maths renderer, so "$\log_2(x)+5$" in a
// config prints with a real subscript, italic variables and a true minus.
// TextRun may therefore return SEVERAL runs; Paragraph flattens them.
function TextRun(o) { return typeof o === "object" && !Array.isArray(o) ? IM.docxRuns(DocxTextRun, o) : [new DocxTextRun(o)]; }
function Paragraph(o) {
  if (o && Array.isArray(o.children)) o = { ...o, children: o.children.flat() };
  return new DocxParagraph(o);
}

const A = (f) => path.join(__dirname, f);

const TEAL_DEEP = "0E4F4C", TEAL = "1E8F89", TEAL_TINT = "E7F5F4",
      TEAL_TINT2 = "CFEBE8", MAROON = "8A1B17", CHARCOAL = "222E2D",
      MUTED = "5C6E6C", LINE = "C9DEDC";
const HEAD = "Cambria", BODY = "Calibri";

const deptLogo = fs.readFileSync(A("dept_logo_doc.png"));
const schoolLogo = fs.readFileSync(A("school_logo_doc.png"));
// Cognia accreditation badge, top CENTRE of every page (9 Sep 2026).
const cogniaBadge = fs.readFileSync(A("cognia_badge_doc.png"));

const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const th = (c) => ({ style: BorderStyle.SINGLE, size: 4, color: c });
const cellB = { top: th(LINE), bottom: th(LINE), left: th(LINE), right: th(LINE) };

const W = 9360;    // A4 portrait usable width, DXA
const A3W = 14678; // A3 portrait usable width, DXA — the PBL sheet
const LW = 14678;  // A4 landscape

// Calibration: how many extra ruled lines each project sheet needs so its single
// A3 page is filled to the foot. Written by calibrate_pbl.py, read here.
let PBL_EXTRA = {};
try { PBL_EXTRA = JSON.parse(fs.readFileSync(A("pbl_extra.json"), "utf8")); } catch (e) {}

function makeEngine(cfg) {
  IM.lint(cfg);
  const MATH = JSON.parse(fs.readFileSync(A(cfg.mathDocIndex), "utf8"));
  const GRAPH = cfg.graphIndex ? JSON.parse(fs.readFileSync(A(cfg.graphIndex), "utf8")) : {};
  const CODES = cfg.codes.concat(cfg.mps);

  // docx sizes are PIXELS; natural inches at 96 dpi scaled by k
  const eqRun = (key, k = 1.3) => {
    const m = MATH[key];
    if (!m) throw new Error("missing expression " + key);
    return new ImageRun({ type: "png", data: fs.readFileSync(A(m.file)),
      transformation: { width: Math.round(m.win * 96 * k), height: Math.round(m.hin * 96 * k) } });
  };
  const mathPara = (key, k = 1.4, o = {}) => new Paragraph({
    alignment: o.align || AlignmentType.LEFT,
    spacing: { before: o.before ?? 60, after: o.after ?? 60 },
    children: [eqRun(key, k)],
  });
  const graphPara = (key, widthPx, o = {}) => {
    const m = GRAPH[key];
    return new Paragraph({
      alignment: o.align || AlignmentType.CENTER,
      spacing: { before: o.before ?? 80, after: o.after ?? 120 },
      children: [new ImageRun({ type: "png", data: fs.readFileSync(A(m.file)),
        transformation: { width: widthPx, height: Math.round(widthPx / m.aspect) } })],
    });
  };
  const mix = (parts, o = {}) => new Paragraph({
    alignment: o.align, spacing: { before: o.before ?? 0, after: o.after ?? 70 },
    children: parts.map((p) => (typeof p === "string"
      ? new TextRun({ text: p, font: o.font ?? BODY, size: (o.size ?? 10.5) * 2, bold: o.bold, italics: o.italic, color: o.color ?? CHARCOAL })
      : eqRun(p.eq, p.k ?? 1.15))),
  });
  const P = (text, o = {}) => new Paragraph({
    alignment: o.align, spacing: { before: o.before ?? 0, after: o.after ?? 70 },
    children: [new TextRun({ text, font: o.font ?? BODY, size: (o.size ?? 10.5) * 2,
      bold: o.bold, italics: o.italic, color: o.color ?? CHARCOAL })],
  });
  const cell = (children, o = {}) => new TableCell({
    width: { size: o.w, type: WidthType.DXA }, columnSpan: o.span,
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    borders: o.plain ? noBorders : cellB,
    verticalAlign: o.valign || VerticalAlign.TOP,
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    children,
  });
  const gap = (a = 120) => new Paragraph({ spacing: { after: a }, children: [] });
  const lines = (n, indent = 0) => Array.from({ length: n }, () => new Paragraph({
    spacing: { before: 0, after: 150 }, indent: { left: indent },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "B9CFCD", space: 4 } },
    children: [new TextRun({ text: " ", size: 20 })],
  }));

  function brandHeader(total = W) {
    const side = Math.floor(total * 0.36), mid = total - 2 * side;
    return new Header({ children: [
      new Table({ columnWidths: [side, mid, side], width: { size: total, type: WidthType.DXA },
        borders: noBorders,
        rows: [new TableRow({ children: [
          new TableCell({ width: { size: side, type: WidthType.DXA }, borders: noBorders,
            children: [new Paragraph({ alignment: AlignmentType.LEFT, children: [
              new ImageRun({ type: "png", data: deptLogo, transformation: { width: 152, height: 47 } })] })] }),
          new TableCell({ width: { size: mid, type: WidthType.DXA }, borders: noBorders,
            children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
              new ImageRun({ type: "png", data: cogniaBadge, transformation: { width: 76, height: 57 } })] })] }),
          new TableCell({ width: { size: side, type: WidthType.DXA }, borders: noBorders,
            children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
              new ImageRun({ type: "png", data: schoolLogo, transformation: { width: 54, height: 54 } })] })] }),
        ] })] }),
      new Paragraph({ spacing: { after: 40 }, children: [] }),
    ] });
  }
  // Branding (9 Sep 2026): the document's identifiers on the left, the school
  // motto centred, and "Mr Malek Thiab · Page n of m" on the right.
  const codesFooter = (total = W) => {
    const l = Math.round(total * 0.4), m = Math.round(total * 0.3), r = total - l - m;
    const fcell = (w, children) => new TableCell({ width: { size: w, type: WidthType.DXA }, borders: noBorders,
      verticalAlign: VerticalAlign.BOTTOM, margins: { top: 0, bottom: 0, left: 0, right: 0 }, children });
    return new Footer({ children: [
      new Table({ columnWidths: [l, m, r], width: { size: total, type: WidthType.DXA }, borders: noBorders,
        rows: [new TableRow({ children: [
          fcell(l, [new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 0 },
            children: [new TextRun({ text: CODES.join("  ·  "), font: BODY, size: 14, color: MUTED })] })]),
          fcell(m, [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
            children: [new TextRun({ text: "FAITH,  RIGHTEOUSNESS  AND  WISDOM", font: HEAD,
              size: 15, bold: true, color: "1F3864" })] })]),
          fcell(r, [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 },
            children: [new DocxTextRun({ font: BODY, size: 15, color: MUTED,
              children: ["Mr Malek Thiab  ·  Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES] })] })]),
        ] })] }),
    ] });
  };

  // a3: the project task is printed A3 so a group of four can work on one sheet.
  const makeDoc = (title, children, landscape, a3) => new Document({
    creator: "Dar Alfikr Schools — Mathematics Department", title,
    sections: [{
      properties: { page: {
        size: a3
          ? { width: 16838, height: 23811 }
          : { width: 11906, height: 16838, orientation: landscape ? PageOrientation.LANDSCAPE : undefined },
        margin: { top: 860, bottom: 700, left: 1080, right: 1080 } } },
      headers: { default: brandHeader(a3 ? A3W : landscape ? LW : W) },
      footers: { default: codesFooter(a3 ? A3W : landscape ? LW : W) },
      children,
    }],
  });

  // ---- student sheet furniture ----
  const titleBlock = (activityTitle, subtitle, extra, w = W) => {
    const big = w > W;
    const c1 = Math.round(w * 0.615), c2 = w - c1;
    return [
      new Paragraph({ spacing: { after: 20 }, children: [new TextRun({
        text: cfg.lessonLine, font: BODY, size: big ? 20 : 17, color: TEAL, bold: true })] }),
      new Paragraph({ spacing: { after: 40 }, children: [new TextRun({
        text: activityTitle, font: HEAD, size: big ? 44 : 32, bold: true, color: TEAL_DEEP })] }),
      new Paragraph({ spacing: { after: 150 }, children: [new TextRun({
        text: subtitle, font: BODY, size: big ? 23 : 19, italics: true, color: MUTED })] }),
      new Table({ columnWidths: [c1, c2], width: { size: w, type: WidthType.DXA },
        rows: [new TableRow({ children: [
          cell([P("Student name :  ...............................................................", { size: big ? 12.5 : 11 })], { w: c1, fill: TEAL_TINT }),
          cell([P("Date :  .................................", { size: big ? 12.5 : 11 })], { w: c2, fill: TEAL_TINT }),
        ] })] }),
      ...(extra || []),
      gap(160),
    ];
  };
  const sectionBar = (text, note, w = W) => new Table({
    columnWidths: [w], width: { size: w, type: WidthType.DXA },
    rows: [new TableRow({ children: [cell([new Paragraph({ spacing: { after: 0 }, children: [
      new TextRun({ text, font: HEAD, size: w > W ? 26 : 21, bold: true, color: "FFFFFF" }),
      ...(note ? [new TextRun({ text: `     ${note}`, font: BODY, size: w > W ? 20 : 17, color: "CFE8E6" })] : []),
    ] })], { w, fill: TEAL_DEEP })] })],
  });
  const qRow = (n, key, instruction, k = 1.35) => new Table({
    columnWidths: [620, 3200, W - 3820], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ children: [
      cell([P(n, { size: 11, bold: true, color: TEAL_DEEP, align: AlignmentType.CENTER })], { w: 620, fill: TEAL_TINT }),
      cell([mathPara(key, k, { align: AlignmentType.CENTER })], { w: 3200 }),
      cell([P(instruction, { size: 10.5 })], { w: W - 3820, valign: VerticalAlign.CENTER }),
    ] })],
  });
  const qGrid = (items, k = 1.3) => {
    const cols = 3, cw = Math.floor(W / cols), rows = [];
    // Scale each expression down if it would overflow its column — a wide
    // function pair used to be clipped at the cell edge.
    const maxIn = cw / 1440 - 0.18;
    const fit = (key) => {
      const m = MATH[key];
      if (!m || !m.win) return k;
      return Math.min(k, maxIn / m.win);
    };
    for (let i = 0; i < items.length; i += cols) {
      rows.push(new TableRow({ children: items.slice(i, i + cols).map((it) => cell([
        P(it[0], { size: 9.5, bold: true, color: MAROON, after: 30 }),
        mathPara(it[1], fit(it[1]), { align: AlignmentType.CENTER, before: 20, after: 220 }),
        P(" ", { size: 9 }),
      ], { w: cw })) }));
    }
    return new Table({ columnWidths: Array(cols).fill(cw), width: { size: W, type: WidthType.DXA }, rows });
  };

  // =================================================== FIKR LESSON PLAN
  function fikrPlan() {
    const D = cfg.plan, T = cfg.timings;
    const total = T.t1 + T.t2 + T.t3 + T.t4 + T.t5 + T.t6;
    const phaseBar = (num, label, time) => new Table({
      columnWidths: [620, W - 620], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: [
        cell([P(num, { bold: true, size: 14, color: "FFFFFF", align: AlignmentType.CENTER, font: HEAD })], { w: 620, fill: MAROON }),
        cell([new Paragraph({ spacing: { after: 0 }, children: [
          new TextRun({ text: label, font: HEAD, size: 22, bold: true, color: "FFFFFF" }),
          new TextRun({ text: time ? `      ${time}` : "", font: BODY, size: 18, color: "CFE8E6" }),
        ] })], { w: W - 620, fill: TEAL_DEEP }),
      ] })],
    });
    const field = (prompt, answer) => new Table({
      columnWidths: [W], width: { size: W, type: WidthType.DXA },
      rows: [
        new TableRow({ children: [cell([P(prompt, { bold: true, size: 9.5, color: TEAL_DEEP })], { w: W, fill: TEAL_TINT2 })] }),
        new TableRow({ children: [cell(answer.map((l, i) => {
          const o = { size: 10, after: i === answer.length - 1 ? 0 : 60 };
          if (l instanceof DocxParagraph) return l;
          return Array.isArray(l) ? mix(l, o) : P(l, o);
        }), { w: W })] }),
      ],
    });

    const k = [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: "FIKR Model — Lesson Plan", font: HEAD, size: 30, bold: true, color: TEAL_DEEP })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [new TextRun({ text: "Learning Leading to Production", font: BODY, size: 18, italics: true, color: MUTED })] }),
      new Table({ columnWidths: [1500, 3180, 1500, 3180], width: { size: W, type: WidthType.DXA }, rows: [
        new TableRow({ children: [
          cell([P("Title", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P(cfg.lessonTitle, { size: 10 })], { w: 3180 }),
          cell([P("Subject / Unit", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P(cfg.unit, { size: 10 })], { w: 3180 }),
        ] }),
        new TableRow({ children: [
          cell([P("Grade", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P(cfg.gradeFull, { size: 10 })], { w: 3180 }),
          cell([P("Date", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P(cfg.week, { size: 10 })], { w: 3180 }),
        ] }),
        new TableRow({ children: [
          cell([P("Format", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P("[   ]  40-minute            [ X ]  60-minute", { size: 10 })], { w: 3180 }),
          cell([P("Teacher", { bold: true, size: 9.5, color: TEAL_DEEP })], { w: 1500, fill: TEAL_TINT }),
          cell([P("Mr Malek Thiab", { size: 10 })], { w: 3180 }),
        ] }),
      ] }),
      gap(),
      field("Essential Question (curriculum map)", [cfg.essentialQuestion]), gap(60),
      field("Lesson Objectives (curriculum map — verbatim)", cfg.objectives.map((o, i) => `${i + 1}.  ${o}`)), gap(60),
      field("Vocabulary (curriculum map) · Assessments (curriculum map)", [
        `Vocabulary:  ${cfg.vocabList}.`,
        `Assessments:  ${cfg.assessments[0]} during practice ;  ${cfg.assessments[1]} at the Mastery Gate.`,
      ]), gap(),
    ];

    k.push(phaseBar("0", "Preparation", "Before Class"), gap(60));
    k.push(field("Learning Outcome: What will the student be able to do?", D.outcome), gap(60));
    k.push(field("Pre-Class Preparation — Topic/Link and Evidence of Readiness: What will the student complete before class?", D.preclass), gap());
    k.push(phaseBar("1", "Diagnostic", `${T.t1} min`), gap(60));
    k.push(field("Tool Used: What evidence indicates differences in students' current levels?", D.diagTool), gap(60));
    k.push(field("Where is the learning gap? What will you adjust in your instruction accordingly?", D.diagGap), gap());
    k.push(phaseBar("2", "Targeted Instruction", `${T.t2} min`), gap(60));
    k.push(field("Required Instruction and Modeling: What needs direct explanation? Which example will demonstrate the thinking process and the expected quality standard?", D.instruction), gap(60));
    k.push(field("Quick Check for Understanding: What question or evidence confirms that students are ready to move on to practice?", D.quickCheck), gap());
    k.push(phaseBar("3", "Practice", `${T.t3} min`), gap(60));
    k.push(field("Guided Task: How will the student progress from guided to independent practice? What feedback will the student use?", D.guided), gap(60));
    k.push(field("Independent Task and Feedback Tool: students choose their route and may switch at any time", D.independent), gap());
    k.push(phaseBar("4", "Production — Stage One", `${T.t4} min`), gap(60));
    k.push(field("Production Task: What new task, situation, or product will allow the student to demonstrate learning?", D.production), gap(60));
    k.push(field("Product Quality Criteria and the Role of AI: What is the minimum acceptable standard? What must the student complete independently?", D.criteria), gap());
    k.push(phaseBar("5", "Presentation — Evidence of Learning", `${T.t5} min`), gap(60));
    k.push(field("Evidence of Learning and Success Criterion: What will the student present or explain, and how? What must be clearly demonstrated for learning to be considered achieved?", D.evidence), gap());
    k.push(phaseBar("6", "Final Product — Refinement", `${T.t6} min`), gap(60));
    k.push(field("Refinement and Final Product: What revision will the student make based on feedback? What will the final product look like?", D.refinement), gap(60));
    k.push(field("Presentation/Publication and Reflection: Where will the product be presented or published? What reflection question will close the learning cycle?", D.publication), gap());

    k.push(new Paragraph({ spacing: { after: 160 }, children: [
      new TextRun({ text: "Total minutes across the seven stages:  ", font: BODY, size: 20, bold: true, color: CHARCOAL }),
      new TextRun({ text: `${total}`, font: BODY, size: 20, bold: true, color: MAROON }),
      new TextRun({ text: `   ($${T.t1}+${T.t2}+${T.t3}+${T.t4}+${T.t5}+${T.t6}$) — matches the 60-minute format, including transitions.`, font: BODY, size: 18, color: MUTED }),
    ] }));

    k.push(phaseBar("★", "Required Pillars", "Differentiation · Adaptive Learning · Saudi Connection · Exam Alignment"), gap(60));
    k.push(field("Differentiation — three routes named for the task; students choose, and may switch at any time", D.differentiation), gap(60));
    k.push(field("Adaptive Learning — how the lesson branches on evidence", D.adaptive), gap(60));
    k.push(field("Saudi Culture & Real-World Connection", D.saudi), gap(60));
    k.push(field("SAT / SAAT (Tahsili) / GAT (Qudurat) Connection", D.exams), gap(60));
    k.push(field("Suggestions for Improvement:", ["", ""]));

    return makeDoc(`FIKR Lesson Plan — ${cfg.lessonTitle}`, k, false);
  }

  // =================================================== LESSON PLAN 2026/27
  function lessonPlan2026() {
    const D = cfg.plan2026, T = cfg.timings;
    const hdrCell = (t, w) => cell([P(t, { size: 9.5, bold: true, color: "FFFFFF" })], { w, fill: TEAL_DEEP });
    const val = (t, w) => cell([P(t, { size: 9.5 })], { w });
    const c7 = [2100, 1500, 1500, 3200, 2100, 2200, 2078];
    const children = [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 140 }, children: [new TextRun({ text: "Lesson plan 2026 / 27", font: HEAD, size: 30, bold: true, color: TEAL_DEEP })] }),
      new Table({ columnWidths: c7, width: { size: LW, type: WidthType.DXA }, rows: [
        new TableRow({ children: ["Day & Date", "Week", "Period/s", "Lesson Title", "Subject", "Chapter/Unit", "Grade/ section"].map((t, i) => hdrCell(t, c7[i])) }),
        new TableRow({ children: [val(D.day, c7[0]), val(cfg.weekNum || "2", c7[1]), val("1 period (60 min)", c7[2]),
          val(cfg.lessonTitle, c7[3]), val("Algebra II", c7[4]), val(cfg.unit, c7[5]), val(D.section, c7[6])] }),
      ] }),
      gap(140),
      new Table({ columnWidths: [7339, 7339], width: { size: LW, type: WidthType.DXA }, rows: [
        new TableRow({ children: [hdrCell("Tools To Be Used", 7339), hdrCell("Resources", 7339)] }),
        new TableRow({ children: [cell([P(D.tools, { size: 9.5 })], { w: 7339 }), cell([P(D.resources, { size: 9.5 })], { w: 7339 })] }),
      ] }),
      gap(140),
      new Table({ columnWidths: [4892, 4893, 4893], width: { size: LW, type: WidthType.DXA }, rows: [
        new TableRow({ children: [hdrCell("Competencies", 4892), hdrCell("Technology Embedded", 4893), hdrCell("Connection to student's real life", 4893)] }),
        new TableRow({ children: [
          cell(D.competencies.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4892 }),
          cell(D.technology.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4893 }),
          cell(D.reallife.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4893 }),
        ] }),
      ] }),
      gap(140),
      new Table({ columnWidths: [4892, 4893, 4893], width: { size: LW, type: WidthType.DXA }, rows: [
        new TableRow({ children: [hdrCell("Values", 4892), hdrCell("Soft Skills", 4893), hdrCell("Hard Skills", 4893)] }),
        new TableRow({ children: [
          cell(D.values.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4892 }),
          cell(D.soft.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4893 }),
          cell(D.hard.map((t, i) => P(`${i + 1}-  ${t}`, { size: 9.5, after: 50 })), { w: 4893 }),
        ] }),
      ] }),
      gap(140),
      new Table({ columnWidths: [LW], width: { size: LW, type: WidthType.DXA },
        rows: [new TableRow({ children: [cell([P("Lesson Integral Parts", { size: 12, bold: true, color: "FFFFFF", align: AlignmentType.CENTER })], { w: LW, fill: MAROON })] })] }),
    ];
    const c4 = [3600, 6600, 3078, 1400];
    children.push(new Table({ columnWidths: c4, width: { size: LW, type: WidthType.DXA }, rows: [
      new TableRow({ children: ["Objectives / skills", "Teacher Strategies & Student Activities", "Assessment", "Time"].map((t, i) => hdrCell(t, c4[i])) }),
      new TableRow({ children: [
        cell([
          ...cfg.objectives.map((o, i) => P(`${i + 1}-  ${o}`, { size: 9.5, after: 50 })),
          P(`Essential question: ${cfg.essentialQuestion}`, { size: 9, italic: true, color: MUTED, before: 40, after: 60 }),
          P(`Vocabulary: ${cfg.vocabList}.`, { size: 9, italic: true, color: MUTED }),
        ], { w: c4[0] }),
        cell(D.phases.map((t, i) => P(t, { size: 9.5, after: i === D.phases.length - 1 ? 0 : 60 })), { w: c4[1] }),
        cell(D.assessment.map((t, i) => P(t, { size: 9.5, after: i === D.assessment.length - 1 ? 0 : 60 })), { w: c4[2] }),
        cell([P(`${T.t1} min`, { size: 9.5, after: 60 }), P(`${T.t2} min`, { size: 9.5, after: 60 }),
              P(`${T.t3} min`, { size: 9.5, after: 60 }), P(`${T.t4} min`, { size: 9.5, after: 60 }),
              P(`${T.t5} min`, { size: 9.5, after: 60 }), P(`${T.t6} min`, { size: 9.5, after: 80 }),
              P("Total 60 min", { size: 9.5, bold: true, color: MAROON })], { w: c4[3] }),
      ] }),
    ] }));
    children.push(gap(140));
    const wide = (label, text) => new Table({
      columnWidths: [2600, LW - 2600], width: { size: LW, type: WidthType.DXA },
      rows: [new TableRow({ children: [
        cell([P(label, { size: 10, bold: true, color: "FFFFFF" })], { w: 2600, fill: TEAL_DEEP }),
        cell([P(text, { size: 9.5 })], { w: LW - 2600 }),
      ] })],
    });
    children.push(wide("Lesson Closure:", D.closure)); children.push(gap(90));
    children.push(wide("Reflection for Improvement:", " ")); children.push(gap(90));
    children.push(wide("Homework:", D.homework)); children.push(gap(90));
    children.push(wide("Teacher name:", "Mr Malek Thiab"));
    return makeDoc(`Lesson plan 2026/27 — ${cfg.lessonTitle}`, children, true);
  }

  // =================================================== CLASSWORK
  function classwork() {
    const C = cfg.classwork;
    const k = titleBlock(`Classwork — ${cfg.assessments[0].replace(/[“”]/g, "").replace(" questions", "")}`,
      C.subtitle || "Show all your working. A correct answer with no working is only half an answer.");
    C.sections.forEach((sec, si) => {
      k.push(sectionBar(sec.h, sec.note)); k.push(gap(80));
      if (sec.intro) k.push(P(sec.intro, { size: 10.5, after: 120 }));
      if (sec.graph) k.push(graphPara(sec.graph, sec.graphW || 420));
      (sec.q || []).forEach((q) => k.push(qRow(q.n, q.eq, q.t, q.k)));
      if (sec.text) sec.text.forEach((t) => k.push(Array.isArray(t) ? mix(t, { size: 10.5, after: 140 }) : P(t, { size: 10.5, after: 140 })));
      k.push(...lines(sec.lines || 4));
      k.push(gap(si === C.sections.length - 1 ? 60 : 160));
    });
    return makeDoc(`Classwork — ${cfg.lessonTitle}`, k, false);
  }

  // =================================================== DIFFERENTIATION
  function differentiation() {
    const R = cfg.diffSheet;
    const k = titleBlock("Choose Your Route",
      "Three routes, same destination. Start anywhere — you may switch routes at any time, and you may try more than one.");
    const names = [
      ["PRACTICE — Secure the method", R.routes[0].note],
      ["APPLY — Use it in context", R.routes[1].note],
      ["INVESTIGATE — Find out why", R.routes[2].note],
    ];
    R.routes.forEach((r, i) => {
      k.push(sectionBar(names[i][0], names[i][1])); k.push(gap(80));
      if (r.intro) k.push(P(r.intro, { size: 10.5, after: 120 }));
      if (r.grid) k.push(qGrid(r.grid));
      if (r.graph) k.push(graphPara(r.graph, r.graphW || 400));
      (r.tasks || []).forEach((t) => k.push(Array.isArray(t) ? mix(t, { size: 10.5, after: 140 }) : P(t, { size: 10.5, after: 140 })));
      k.push(...lines(r.lines || 3));
      // house rule 3 — "Done when…", never "Success:"
      k.push(P(`Done when: ${r.done}`, { size: 10, italic: true, color: MUTED, before: 100, after: 160 }));
    });
    k.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: [cell([
        P("Remember", { size: 10.5, bold: true, color: TEAL_DEEP, after: 60 }),
        P("These are names for the tasks, not names for you. Move between them whenever you want to. Everyone answers the same “Time to Check” at the end of the lesson.", { size: 10 }),
      ], { w: W, fill: TEAL_TINT })] })] }));
    return makeDoc(`Choose Your Route — ${cfg.lessonTitle}`, k, false);
  }

  // =================================================== PBL TASK  (A3)
  // Printed A3 so a group of four can work on one sheet on the table between
  // them. Every width below is derived from A3W, and the type is scaled up to
  // match the sheet — A4 sizes look lost on A3.
  function pblTask() {
    const B = cfg.pbl;
    const PW = A3W;
    const k = titleBlock(`Project Task — ${B.title}`, B.subtitle, [
      new Table({ columnWidths: [PW], width: { size: PW, type: WidthType.DXA },
        rows: [new TableRow({ children: [cell([
          P("Group members :   ..................................................    ..................................................    ..................................................    ..................................................",
            { size: 12 }),
        ], { w: PW, fill: TEAL_TINT2 })] })] }),
      new Table({ columnWidths: [PW], width: { size: PW, type: WidthType.DXA },
        rows: [new TableRow({ children: [cell([new Paragraph({ spacing: { after: 0 }, children: [
          new TextRun({ text: "MATERIALS   ", font: BODY, size: 19, bold: true, color: TEAL_DEEP }),
          new TextRun({ text: B.materials.join("   ·   "), font: BODY, size: 21, color: CHARCOAL }),
        ] })], { w: PW, fill: TEAL_TINT })] })] }),
    ], PW);

    // ---- band 1: the brief on the left, the steps on the right
    const lw = 7000, gut1 = 400, rw = PW - lw - gut1;
    const brief = [
      sectionBar("THE DRIVING QUESTION", null, lw), gap(70),
      P(B.driving, { size: 13, bold: true, color: TEAL_DEEP, after: 130 }),
      sectionBar("THE SITUATION", null, lw), gap(70),
      ...B.situation.map((t) => P(t, { size: 11.5, after: 100 })),
    ];
    if (B.eq) {
      // Scale the expression to the column it sits in — at a fixed scale a wide
      // cases block runs straight off the edge of the left column.
      const m = MATH[B.eq];
      const maxIn = lw / 1440 - 0.45;
      const kEq = m && m.win ? Math.min(1.55, maxIn / m.win) : 1.55;
      brief.push(mathPara(B.eq, kEq, { align: AlignmentType.CENTER, before: 90, after: 80 }));
    }
    if (B.data) {
      // The first column carries a label ("t (minutes)"); the rest carry values.
      // Equal columns squeeze the label into two ugly lines.
      const n = B.data[0].length;
      const first = n > 3 ? Math.floor(lw * 0.22) : Math.floor(lw / n);
      const rest = Math.floor((lw - first) / (n - 1));
      const wid = B.data[0].map((_, i) => (i === 0 ? first : rest));
      brief.push(new Table({
        columnWidths: wid, width: { size: lw, type: WidthType.DXA },
        rows: B.data.map((row, r) => new TableRow({ children: row.map((v, i) => cell(
          [P(v, { size: 11.5, bold: r === 0, color: r === 0 ? "FFFFFF" : CHARCOAL, align: AlignmentType.CENTER })],
          { w: wid[i], fill: r === 0 ? TEAL : TEAL_TINT })) })),
      }));
    }

    const badge = 700;
    const steps = [sectionBar("YOUR TASK", `${B.steps.length} steps · ${B.minutes} minutes`, rw), gap(70)];
    B.steps.forEach(([n, h, d]) => {
      steps.push(new Table({ columnWidths: [badge, rw - badge], width: { size: rw, type: WidthType.DXA },
        rows: [new TableRow({ children: [
          cell([P(n, { size: 16, bold: true, color: "FFFFFF", align: AlignmentType.CENTER, font: HEAD })], { w: badge, fill: MAROON }),
          cell([P(h, { size: 12, bold: true, color: TEAL_DEEP, after: 40 }), P(d, { size: 11.5 })], { w: rw - badge, fill: TEAL_TINT }),
        ] })] }));
      steps.push(gap(45));
    });

    k.push(new Table({
      columnWidths: [lw, gut1, rw], width: { size: PW, type: WidthType.DXA },
      rows: [new TableRow({ children: [
        cell(brief, { w: lw, plain: true }),
        cell([P(" ", { size: 8 })], { w: gut1, plain: true }),
        cell(steps, { w: rw, plain: true }),
      ] })],
    }));
    k.push(gap(150));

    // ---- band 2: two writing columns and a reference panel
    k.push(sectionBar("YOUR WORKING", "write on this sheet", PW));
    k.push(gap(90));
    // Each block gets its configured lines plus two, plus a share of the extra
    // the calibrator worked out for this sheet.
    const extra = PBL_EXTRA[cfg.slug] || 0;
    const nb = B.working.length;
    const share = (i) => {
      const base = Math.trunc(extra / nb);
      const rem = extra - base * nb;              // works for negative extra too
      return base + (i < Math.abs(rem) ? Math.sign(rem) : 0);
    };
    const blocks = B.working.map(([label, n], i) => [
      label, Math.max(2, n + 2 + share(i)),       // never fewer than two lines
    ]);
    // Split so the two columns end at roughly the same height — splitting by
    // block count leaves one column short whenever the blocks are uneven.
    const weight = (b) => b[1] + 1.6;              // ruled lines + the label
    const total = blocks.reduce((a, b) => a + weight(b), 0);
    let run = 0, half = blocks.length;
    for (let i = 0; i < blocks.length; i++) {
      run += weight(blocks[i]);
      if (run >= total / 2) { half = i + 1; break; }
    }
    // Level the two columns: pad the shorter one's last block so both sets of
    // ruled lines finish on the same line. A ragged foot is the tell that a
    // sheet was laid out by accident rather than designed.
    const left = blocks.slice(0, half), right = blocks.slice(half);
    const wsum = (arr) => arr.reduce((a, b) => a + weight(b), 0);
    const diff = Math.round(wsum(left) - wsum(right));
    if (diff > 0 && right.length) right[right.length - 1][1] += diff;
    else if (diff < 0 && left.length) left[left.length - 1][1] += -diff;

    const colBlocks = (items) => {
      const out = [];
      items.forEach(([label, n], i) => {
        out.push(P(label, { size: 12.5, bold: true, color: TEAL_DEEP, before: i ? 170 : 0, after: 120 }));
        out.push(...lines(n));   // A3 exists to give them room to work
      });
      return out.length ? out : [P(" ", { size: 10 })];
    };
    const panelBox = (title, items) => {
      const out = [P(title, { size: 10, bold: true, color: TEAL_DEEP, after: 70 })];
      items.forEach((t, i) => out.push(P("·  " + t, { size: 10, after: i === items.length - 1 ? 0 : 50 })));
      return out;
    };
    const panelW = 3600, gut = 300;
    const colW = Math.floor((PW - panelW - 2 * gut) / 2);
    k.push(new Table({
      columnWidths: [colW, gut, PW - panelW - 2 * gut - colW, gut, panelW],
      width: { size: PW, type: WidthType.DXA },
      rows: [new TableRow({ children: [
        cell(colBlocks(left), { w: colW, plain: true }),
        cell([P(" ", { size: 8 })], { w: gut, plain: true }),
        cell(colBlocks(right), { w: PW - panelW - 2 * gut - colW, plain: true }),
        cell([P(" ", { size: 8 })], { w: gut, plain: true }),
        cell([...panelBox("ROLES", B.roles), P(" ", { size: 8 }),
              ...panelBox("DONE WHEN …", B.doneWhen)], { w: panelW, fill: TEAL_TINT }),
      ] })],
    }));
    return makeDoc(`Project Task — ${B.title}`, k, false, true);
  }

  return { fikrPlan, lessonPlan2026, classwork, differentiation, pblTask };
}

async function buildAll(cfg) {
  const e = makeEngine(cfg);
  const outputs = [
    [`FIKR_LessonPlan_${cfg.slug}.docx`, e.fikrPlan()],
    [`LessonPlan2026-27_${cfg.slug}.docx`, e.lessonPlan2026()],
    [`Classwork_${cfg.slug}.docx`, e.classwork()],
    [`Activity_Differentiation_${cfg.slug}.docx`, e.differentiation()],
    [`PBL_Task_${cfg.slug}.docx`, e.pblTask()],
  ];
  for (const [name, doc] of outputs) {
    const buf = await Packer.toBuffer(doc);
    fs.writeFileSync(A(name), buf);
    console.log("  wrote", name, (buf.length / 1024).toFixed(0) + " KB");
  }
}

// Rebuild only the A3 project sheet — used for the two Week 2 tasks that were
// hand-built before this engine existed.
async function buildPbl(cfg) {
  const e = makeEngine(cfg);
  const b = await Packer.toBuffer(e.pblTask());
  const name = `PBL_Task_${cfg.slug}.docx`;
  fs.writeFileSync(A(name), b);
  console.log("  wrote", name, Math.round(b.length / 1024) + " KB");
}

module.exports = { buildAll, buildPbl };

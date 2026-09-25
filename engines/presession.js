// ---------------------------------------------------------------------------
// PRE-SESSION SKILLS SHEET AND PREPARATION NOTES — Week 2, Semester 1 2026-27.
// Two pages exactly, per Mr Thiab: page 1 is the student's skills sheet, page 2
// is the preparation notes they work through before they walk in.
//
// FIKR Phase 0 (flipped): the student arrives already primed, so the in-class
// Diagnose activity starts from evidence rather than from cold.
//
// Every sheet names the CHECKLIST CODES its session will cover, so the coverage
// workbook and the classroom material speak the same language. Nothing here is
// ticked on the checklist — coverage is what he teaches, not what I write.
// ---------------------------------------------------------------------------
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType, VerticalAlign, PageBreak,
  Header, Footer,
} = require("docx");

const A = (f) => path.join(__dirname, f);
const MATH = JSON.parse(fs.readFileSync(A("math_pre/_index.json"), "utf8"));

const TEAL_DEEP = "0E4F4C", TEAL = "17A199", TEAL_TINT = "EAF6F5",
      TEAL_TINT2 = "CFEBE8", MAROON = "AD2A22", CHARCOAL = "222E2D",
      MUTED = "5C6E6C", NAVY = "1B3B6F", LINE = "B9CFCD";
const HEAD = "Cambria", BODY = "Calibri";
const W = 9360;                                   // usable A4 portrait width, DXA

const noBorders = {
  top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
};
const cellB = {
  top: { style: BorderStyle.SINGLE, size: 3, color: LINE },
  bottom: { style: BorderStyle.SINGLE, size: 3, color: LINE },
  left: { style: BorderStyle.SINGLE, size: 3, color: LINE },
  right: { style: BorderStyle.SINGLE, size: 3, color: LINE },
};

const P = (text, o = {}) => new Paragraph({
  alignment: o.align, spacing: { before: o.before ?? 0, after: o.after ?? 60 },
  children: [new TextRun({
    text, font: o.font || BODY, size: (o.size ?? 10) * 2, bold: o.bold,
    italics: o.italic, color: o.color || CHARCOAL })],
});

const cell = (children, o = {}) => new TableCell({
  width: { size: o.w, type: WidthType.DXA }, columnSpan: o.span,
  shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
  borders: o.plain ? noBorders : cellB,
  verticalAlign: o.valign || VerticalAlign.TOP,
  margins: { top: 60, bottom: 60, left: 110, right: 110 },
  children,
});

const eqRun = (key, k = 1.0) => {
  const m = MATH[key];
  if (!m) throw new Error("missing expression " + key);
  return new ImageRun({
    data: fs.readFileSync(A(m.file)),
    transformation: { width: Math.round(m.win * k * 96), height: Math.round(m.hin * k * 96) },
  });
};
const eqP = (key, k = 1.0, align = AlignmentType.CENTER) => new Paragraph({
  alignment: align, spacing: { before: 40, after: 60 }, children: [eqRun(key, k)],
});

const band = (text, note) => new Table({
  columnWidths: [W], width: { size: W, type: WidthType.DXA },
  rows: [new TableRow({ children: [cell([new Paragraph({
    spacing: { after: 0 }, children: [
      new TextRun({ text, font: HEAD, size: 20, bold: true, color: "FFFFFF" }),
      ...(note ? [new TextRun({ text: `     ${note}`, font: BODY, size: 16, color: "CFE8E6" })] : []),
    ] })], { w: W, fill: TEAL_DEEP })] })],
});

const gap = (h = 90) => new Paragraph({ spacing: { after: h }, children: [] });

function header() {
  return new Header({ children: [new Table({
    columnWidths: [4680, 4680], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ children: [
      cell([new Paragraph({ children: [new ImageRun({
        data: fs.readFileSync(A("dept_logo_doc.png")),
        transformation: { width: 150, height: 50 } })] })], { w: 4680, plain: true }),
      cell([new Paragraph({ alignment: AlignmentType.RIGHT, children: [new ImageRun({
        data: fs.readFileSync(A("school_logo_doc.png")),
        transformation: { width: 50, height: 50 } })] })], { w: 4680, plain: true }),
    ] })],
  })] });
}

function footer(cfg) {
  return new Footer({ children: [new Paragraph({
    alignment: AlignmentType.RIGHT, spacing: { before: 60 },
    children: [new TextRun({
      text: `Pre-session · ${cfg.who} · ${cfg.week || "Week 2"} · Semester 1, 2026–27 · Mr Malek Thiab`,
      font: BODY, size: 15, color: MUTED })] })] });
}

// two-column list: term / meaning, or skill / example
const twoCol = (rows, headLeft, headRight, leftW = 3400) => new Table({
  columnWidths: [leftW, W - leftW], width: { size: W, type: WidthType.DXA },
  rows: [
    // A table whose two headings are both empty used to print an empty teal
    // bar under the section band — a stripe of colour saying nothing, and a
    // wasted row on a sheet that has to close on page two. Skip it.
    ...(headLeft || headRight ? [new TableRow({ children: [headLeft, headRight].map((h, i) => cell(
      [P(h, { size: 9.5, bold: true, color: "FFFFFF" })],
      { w: i ? W - leftW : leftW, fill: TEAL })) })] : []),
    ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: [
      cell([P(r[0], { size: 9.5, bold: true, color: NAVY })],
           { w: leftW, fill: ri % 2 ? TEAL_TINT : undefined }),
      cell(Array.isArray(r[1]) ? r[1] : [P(r[1], { size: 9.5 })],
           { w: W - leftW, fill: ri % 2 ? TEAL_TINT : undefined }),
    ] })),
  ],
});

function build(cfg) {
  const kids = [];

  // ---------------------------------------------------------------- page 1
  kids.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({
    text: cfg.headerLine, font: BODY, size: 16, bold: true, color: TEAL })] }));
  kids.push(new Paragraph({ spacing: { after: 30 }, children: [new TextRun({
    text: cfg.title, font: HEAD, size: 30, bold: true, color: TEAL_DEEP })] }));
  kids.push(P(cfg.sub, { size: 9.5, italic: true, color: MUTED, after: 110 }));

  kids.push(band("WHAT THIS SESSION COVERS", "the codes on your teacher's checklist"));
  kids.push(gap(60));
  kids.push(twoCol(cfg.covers, "Code", "Objective", 2500));
  kids.push(gap(110));

  kids.push(band("YOU SHOULD ALREADY BE ABLE TO", "check each one before the session"));
  kids.push(gap(60));
  kids.push(twoCol(cfg.priors.map((p) => [p.skill, p.eq
    ? [eqP(p.eq, p.k || 0.85, AlignmentType.LEFT), P(p.note, { size: 9, color: MUTED, after: 0 })]
    : [P(p.note, { size: 9.5 })]]), "Skill", "Reminder", 3200));
  kids.push(gap(110));

  kids.push(band("WORDS YOU WILL HEAR", ""));
  kids.push(gap(60));
  kids.push(new Table({
    columnWidths: [W / 2, W / 2], width: { size: W, type: WidthType.DXA },
    rows: chunk(cfg.vocab, 2).map((pair, ri) => new TableRow({ cantSplit: true,
      children: pair.map((v) => cell([new Paragraph({ spacing: { after: 0 }, children: [
        new TextRun({ text: v[0] + " — ", font: BODY, size: 19, bold: true, color: NAVY }),
        new TextRun({ text: v[1], font: BODY, size: 19, color: CHARCOAL }),
      ] })], { w: W / 2, fill: ri % 2 ? TEAL_TINT : undefined })) })),
  }));

  kids.push(gap(110));
  kids.push(band(cfg.appearsTitle, cfg.appearsNote || ""));
  kids.push(gap(60));
  kids.push(twoCol(cfg.appears, cfg.appearsHead || "", "", 2900));

  // ---------------------------------------------------------------- page 2
  // A separate page-break PARAGRAPH is fragile: when page 1 fills exactly, the
  // empty paragraph itself lands on page 2 and its break then pushes the notes
  // to page 3, leaving a blank sheet in the middle of a two-page handout.
  // pageBreakBefore on the heading cannot do that.
  kids.push(new Paragraph({ pageBreakBefore: true, spacing: { after: 30 },
    children: [new TextRun({
      text: "Preparation Notes", font: HEAD, size: 28, bold: true, color: TEAL_DEEP })] }));
  kids.push(P(cfg.notesSub, { size: 9.5, italic: true, color: MUTED, after: 110 }));

  kids.push(band("THREE THINGS TO KNOW BEFORE YOU ARRIVE", ""));
  kids.push(gap(60));
  cfg.keys.forEach((k, i) => {
    kids.push(new Table({
      columnWidths: [520, W - 520], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ cantSplit: true, children: [
        cell([P(String(i + 1), { size: 12, bold: true, color: "FFFFFF",
                                 align: AlignmentType.CENTER })],
             { w: 520, fill: TEAL, valign: VerticalAlign.CENTER }),
        cell([
          P(k.head, { size: 10, bold: true, color: MAROON, after: 30 }),
          ...(k.eq ? [eqP(k.eq, k.k || 0.85, AlignmentType.LEFT)] : []),
          P(k.body, { size: 9.5, after: 0 }),
        ], { w: W - 520, fill: TEAL_TINT }),
      ] })],
    }));
    kids.push(gap(50));
  });
  kids.push(gap(50));

  kids.push(band("THE MISTAKE TO AVOID", "your teacher will name this out loud"));
  kids.push(gap(60));
  kids.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ children: [cell([P(cfg.misconception, { size: 10, after: 0 })],
      { w: W, fill: "FBE4E2" })] })] }));
  kids.push(gap(110));

  kids.push(band("READY? TRY THESE SIX", "about ten minutes · answers at the foot of the page"));
  kids.push(gap(60));
  kids.push(new Table({
    columnWidths: [W / 2, W / 2], width: { size: W, type: WidthType.DXA },
    rows: chunk(cfg.warmup, 2).map((pair, ri) => new TableRow({ cantSplit: true,
      children: pair.map((q, ci) => cell([
        new Paragraph({ spacing: { after: q.eq ? 20 : 0 }, children: [
          new TextRun({ text: `${ri * 2 + ci + 1}.  `, font: BODY, size: 19, bold: true, color: MAROON }),
          new TextRun({ text: q.q, font: BODY, size: 19, color: CHARCOAL })] }),
        ...(q.eq ? [eqP(q.eq, q.k || 0.8, AlignmentType.LEFT)] : []),
      ], { w: W / 2, fill: ri % 2 ? TEAL_TINT : undefined })) })),
  }));
  kids.push(gap(70));

  // choose-your-route: the task is named, never the student
  kids.push(new Table({
    columnWidths: [W / 3, W / 3, W / 3], width: { size: W, type: WidthType.DXA },
    rows: [
      new TableRow({ children: ["Practice — secure the method", "Apply — use it in context",
                                "Investigate — find out why"].map((h) =>
        cell([P(h, { size: 9, bold: true, color: "FFFFFF" })], { w: W / 3, fill: TEAL })) }),
      new TableRow({ cantSplit: true, children: cfg.routes.map((r) =>
        cell([P(r, { size: 9, after: 0 })], { w: W / 3, fill: TEAL_TINT2 })) }),
    ],
  }));
  kids.push(gap(70));

  kids.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ children: [cell([
      new Paragraph({ spacing: { after: 0 }, children: [
        new TextRun({ text: "Done when…  ", font: BODY, size: 19, bold: true, color: TEAL_DEEP }),
        new TextRun({ text: cfg.doneWhen, font: BODY, size: 19, color: CHARCOAL })] }),
    ], { w: W, fill: TEAL_TINT })] })] }));
  kids.push(gap(60));

  kids.push(new Paragraph({ spacing: { after: 0 }, children: [
    new TextRun({ text: "Answers:  ", font: BODY, size: 15, bold: true, color: MUTED }),
    new TextRun({ text: cfg.answers, font: BODY, size: 15, color: MUTED }),
  ] }));

  const doc = new Document({
    creator: "Mr Malek Thiab", title: cfg.title,
    sections: [{
      properties: { page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 900, right: 1000, bottom: 800, left: 1000, header: 400, footer: 340 },
      } },
      headers: { default: header() }, footers: { default: footer(cfg) },
      children: kids,
    }],
  });
  Packer.toBuffer(doc).then((b) => {
    fs.writeFileSync(A(cfg.out), b);
    console.log("  wrote", cfg.out, (b.length / 1024).toFixed(0) + " KB");
  });
}

function chunk(a, n) {
  const out = [];
  for (let i = 0; i < a.length; i += n) out.push(a.slice(i, i + n));
  return out;
}

module.exports = { build };

// ---------------------------------------------------------------------------
// EXAM-PREP SET ENGINE  —  GAT / SAAT practice papers
// From one config: a student practice paper and a teacher answer key.
// Branding, strand codes, timing box and the item budget are enforced here.
// Options may be plain strings or { eq: "<key>" } expressions.
// ---------------------------------------------------------------------------
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType, Header, Footer,
  ImageRun, VerticalAlign,
  PageBreak,
} = require("docx");
const fs = require("fs");
const path = require("path");

const A = (f) => path.join(__dirname, f);
// Generator output (math_*/, figs_*/) lives under generators/, one level up
// from this engine — never inside engines/ itself.
const G = (f) => path.join(__dirname, "..", "generators", f);
const LOGOS = (f) => path.join(__dirname, "..", "assets", "logos", f);
const TEAL_DEEP = "0E4F4C", TEAL = "1E8F89", TEAL_TINT = "E7F5F4",
      TEAL_TINT2 = "CFEBE8", MAROON = "8A1B17", CHARCOAL = "222E2D",
      MUTED = "5C6E6C", LINE = "C9DEDC", AMBER = "8A5A17", NAVY = "1F3864";
const HEAD = "Cambria", BODY = "Calibri";
const SZ = (cfg, big, small) => (cfg && cfg.dense ? small : big);
const deptLogo = fs.readFileSync(LOGOS("dept_logo.png"));
const schoolLogo = fs.readFileSync(LOGOS("school_logo.png"));
// Cognia accreditation badge — the top CENTRE of every page (his instruction,
// 9 Sep 2026). It replaced the teacher name that used to sit there; the name now
// lives in the footer beside the school motto.
const cogniaBadge = fs.readFileSync(A("cognia_badge_doc.png"));

const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const th = (c) => ({ style: BorderStyle.SINGLE, size: 4, color: c });
const cellB = { top: th(LINE), bottom: th(LINE), left: th(LINE), right: th(LINE) };
const W = 9360; // A4 portrait usable width, DXA
const LETTER = ["A", "B", "C", "D"];

function makeEngine(cfg) {
  const MATH = JSON.parse(fs.readFileSync(G(cfg.mathIndex), "utf8"));

  const eqRun = (key, k = 1.15) => {
    const m = MATH[key];
    if (!m) throw new Error("missing expression " + key);
    return new ImageRun({ type: "png", data: fs.readFileSync(G(m.file)),
      transformation: { width: Math.round(m.win * 96 * k), height: Math.round(m.hin * 96 * k) } });
  };
  const FIGS = cfg.figIndex
    ? JSON.parse(fs.readFileSync(G(cfg.figIndex), "utf8")) : {};
  const figRun = (key, win) => {
    const f = FIGS[key];
    if (!f) throw new Error("missing figure " + key);
    return new ImageRun({ type: "png", data: fs.readFileSync(G(f.file)),
      transformation: { width: Math.round(win * 96),
        height: Math.round(win * 96 / f.aspect) } });
  };
  const whyRuns = (it) => [
    ...(it.trick ? [new TextRun({ text: "THE TRICK — " + it.trick + "   ",
      font: BODY, size: 18, bold: true, color: MAROON })] : []),
    new TextRun({ text: it.why, font: BODY, size: 19, color: CHARCOAL }),
  ];
  const P = (text, o = {}) => new Paragraph({
    alignment: o.align, spacing: { before: o.before ?? 0, after: o.after ?? 70 },
    children: [new TextRun({ text, font: o.font ?? BODY, size: (o.size ?? 10.5) * 2,
      bold: o.bold, italics: o.italic, color: o.color ?? CHARCOAL })],
  });
  const mathP = (key, k, o = {}) => new Paragraph({
    alignment: o.align ?? AlignmentType.CENTER,
    keepNext: o.keepNext, keepLines: true,
    spacing: { before: o.before ?? 60, after: o.after ?? 60 },
    children: [eqRun(key, k ?? 1.3)],
  });
  const cell = (children, o = {}) => new TableCell({
    width: { size: o.w, type: WidthType.DXA }, columnSpan: o.span,
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    borders: o.plain ? noBorders : cellB,
    verticalAlign: o.valign || VerticalAlign.TOP,
    margins: { top: o.mt ?? (cfg && cfg.dense ? 40 : 70), bottom: o.mb ?? (cfg && cfg.dense ? 40 : 70), left: 110, right: 110 },
    children,
  });
  const gap = (a = 120) => new Paragraph({ spacing: { after: a }, children: [] });

  // One borderless, un-splittable row wrapping a whole block. A cell must end
  // with a paragraph, so one is added if the block ends with a table.
  const keepWhole = (children) => new Table({
    columnWidths: [W], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: W, type: WidthType.DXA },
      borders: noBorders,
      margins: { top: 0, bottom: 0, left: 0, right: 0 },
      children: children[children.length - 1] instanceof Paragraph
        ? children : [...children, new Paragraph({ spacing: { after: 0 }, children: [] })],
    })] })],
  });

  const brandHeader = () => new Header({ children: [
    new Table({ columnWidths: [W * 0.36, W * 0.28, W * 0.36], width: { size: W, type: WidthType.DXA },
      borders: noBorders,
      rows: [new TableRow({ children: [
        new TableCell({ width: { size: W * 0.36, type: WidthType.DXA }, borders: noBorders,
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ alignment: AlignmentType.LEFT, children: [
            new ImageRun({ type: "png", data: deptLogo, transformation: { width: 152, height: 47 } })] })] }),
        new TableCell({ width: { size: W * 0.28, type: WidthType.DXA }, borders: noBorders,
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
            new ImageRun({ type: "png", data: cogniaBadge, transformation: { width: 76, height: 57 } })] })] }),
        new TableCell({ width: { size: W * 0.36, type: WidthType.DXA }, borders: noBorders,
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
            new ImageRun({ type: "png", data: schoolLogo, transformation: { width: 54, height: 54 } })] })] }),
      ] })] }),
    new Paragraph({ spacing: { after: 40 }, children: [] }),
  ] });
  const foot = (t) => new Footer({ children: [
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 60, after: 20 },
      children: [new TextRun({ text: "FAITH,  RIGHTEOUSNESS  AND  WISDOM", font: HEAD,
                               size: 15, bold: true, color: NAVY })] }),
    new Paragraph({
      alignment: AlignmentType.RIGHT, spacing: { after: 0 },
      children: [new TextRun({ text: t, font: BODY, size: 15, color: MUTED })] }),
  ] });

  const makeDoc = (title, children) => new Document({
    creator: "Dar Alfikr Schools — Mathematics Department", title,
    sections: [{
      properties: { page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 860, bottom: 700, left: 1080, right: 1080 } } },
      headers: { default: brandHeader() },
      footers: { default: foot(`${cfg.examName}  ·  ${cfg.weekLine}  ·  Mr Malek Thiab`) },
      children,
    }],
  });

  const sectionBar = (text, note) => new Table({
    columnWidths: [W], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ children: [cell([new Paragraph({ spacing: { after: 0 }, children: [
      new TextRun({ text, font: HEAD, size: 21, bold: true, color: "FFFFFF" }),
      ...(note ? [new TextRun({ text: `     ${note}`, font: BODY, size: 17, color: "CFE8E6" })] : []),
    ] })], { w: W, fill: TEAL_DEEP })] })],
  });

  // A quieter band than sectionBar, for the SUBTOPIC inside a topic. The unit
  // band is a solid rule across the page; this one is a tinted strip with a
  // maroon rule down its left edge, so the eye reads a hierarchy at a glance
  // rather than two competing headings.
  const subBar = (text, note) => new Table({
    columnWidths: [70, W - 70], width: { size: W, type: WidthType.DXA },
    rows: [new TableRow({ cantSplit: true, children: [
      cell([new Paragraph({ spacing: { after: 0 }, children: [] })],
        { w: 70, fill: MAROON, mt: 30, mb: 30 }),
      cell([new Paragraph({ spacing: { after: 0 }, children: [
        new TextRun({ text, font: HEAD, size: 18, bold: true, color: TEAL_DEEP }),
        ...(note ? [new TextRun({ text: `     ${note}`, font: BODY, size: 15, color: MUTED })] : []),
      ] })], { w: W - 70, fill: TEAL_TINT, mt: 30, mb: 30 }),
    ] })],
  });

  // ------------------------------------------------------------ COVER SHEET
  // The brand header stays (dept logo left, Cognia centre, school logo right —
  // the department's rule for every document). Everything below it is the
  // cover: a deep block carrying the title, a row of counted facts, and the
  // strand mix drawn as ONE bar whose segments are sized by their real share,
  // so the shape of the bank is visible before a single question is read.
  const coverPage = (c) => {
    const k = [gap(180)];
    k.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: [cell([
        new Paragraph({ spacing: { after: 60 }, children: [new TextRun({
          text: c.eyebrow, font: BODY, size: 19, bold: true, color: "9FD6D2",
          characterSpacing: 60 })] }),
        new Paragraph({ spacing: { after: 40 }, children: [new TextRun({
          text: c.title, font: HEAD, size: 62, bold: true, color: "FFFFFF" })] }),
        new Paragraph({ spacing: { after: 120 }, children: [new TextRun({
          text: c.subtitle, font: BODY, size: 24, color: "CFE8E6" })] }),
        new Paragraph({ spacing: { after: 0 }, children: [new TextRun({
          text: c.strapline, font: BODY, size: 19, italics: true, color: "9FD6D2" })] }),
      ], { w: W, fill: TEAL_DEEP, mt: 300, mb: 300 })] })] }));
    k.push(gap(220));

    // the counted facts
    const cw = Math.floor(W / c.facts.length);
    k.push(new Table({ columnWidths: Array(c.facts.length).fill(cw),
      width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: c.facts.map((f) => cell([
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 10 },
          children: [new TextRun({ text: f[0], font: HEAD, size: 40, bold: true, color: TEAL_DEEP })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
          children: [new TextRun({ text: f[1], font: BODY, size: 16, color: MUTED })] }),
      ], { w: cw, fill: TEAL_TINT, mt: 150, mb: 150 })) })] }));
    k.push(gap(220));

    // the strand mix, as one proportional bar
    const tot = c.mix.reduce((s, m) => s + m[1], 0);
    const widths = c.mix.map((m) => Math.max(1060, Math.round((m[1] / tot) * W)));
    const scale = W / widths.reduce((a, b) => a + b, 0);
    const wpx = widths.map((w) => Math.round(w * scale));
    k.push(P("WHAT IS IN IT", { size: 10, bold: true, color: TEAL_DEEP, after: 60 }));
    k.push(new Table({ columnWidths: wpx, width: { size: W, type: WidthType.DXA },
      rows: [
        new TableRow({ children: c.mix.map((m, i) => cell([
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
            children: [new TextRun({ text: String(m[1]), font: HEAD, size: 20,
              bold: true, color: "FFFFFF" })] })],
          { w: wpx[i], fill: m[2], mt: 90, mb: 90 })) }),
        new TableRow({ children: c.mix.map((m, i) => cell([
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
            children: [new TextRun({ text: m[0], font: BODY, size: 15, color: MUTED })] })],
          { w: wpx[i], plain: true, mt: 40, mb: 0 })) }),
      ] }));
    k.push(gap(200));

    k.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: [cell(
        c.note.map((t, i) => P(t, { size: 10, after: i === c.note.length - 1 ? 0 : 50,
          color: i === 0 ? TEAL_DEEP : CHARCOAL, bold: i === 0 })),
        { w: W, fill: TEAL_TINT })] })] }));
    k.push(gap(3500));
    // the foot of the cover: who it is for, who wrote it, and the one claim the
    // whole booklet rests on
    k.push(new Table({ columnWidths: [W * 0.5, W * 0.5], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ children: [
        cell([
          P("PREPARED BY", { size: 8.5, bold: true, color: MUTED, after: 30 }),
          P(c.author, { size: 12, bold: true, color: TEAL_DEEP, after: 20 }),
          P(c.authorRole, { size: 9.5, color: MUTED, after: 0 }),
        ], { w: W * 0.5, plain: true }),
        cell([
          P("VERIFIED", { size: 8.5, bold: true, color: MUTED, after: 30,
            align: AlignmentType.RIGHT }),
          P(c.verified, { size: 9.5, color: CHARCOAL, after: 0,
            align: AlignmentType.RIGHT }),
        ], { w: W * 0.5, plain: true }),
      ] })] }));
    k.push(new Paragraph({ children: [new PageBreak()], spacing: { after: 0 } }));
    return k;
  };

  // ------------------------------------------------------------------ INDEX
  // Topic, then subtopic, then the run of question numbers that sits under it.
  // Question numbers rather than page numbers: a page number changes the moment
  // a figure reflows, and the number is what a student is actually told to do.
  const contentsPages = (groups) => {
    const wc = [W - 2500, 1700, 800];
    const rows = [new TableRow({ tableHeader: true, children:
      ["Topic and subtopic", "Questions", "No."].map((h, i) =>
        cell([P(h, { size: 9.5, bold: true, color: "FFFFFF",
          align: i ? AlignmentType.CENTER : undefined })], { w: wc[i], fill: TEAL })) })];
    for (const g of groups) {
      rows.push(new TableRow({ cantSplit: true, children: [
        cell([new Paragraph({ spacing: { after: 0 }, children: [
          new TextRun({ text: g.title, font: HEAD, size: 19, bold: true, color: "FFFFFF" })] })],
          { w: wc[0], fill: TEAL_DEEP, mt: 50, mb: 50 }),
        cell([P(g.range, { size: 9.5, bold: true, color: "FFFFFF", align: AlignmentType.CENTER })],
          { w: wc[1], fill: TEAL_DEEP, mt: 50, mb: 50 }),
        cell([P(String(g.n), { size: 9.5, bold: true, color: "FFFFFF", align: AlignmentType.CENTER })],
          { w: wc[2], fill: TEAL_DEEP, mt: 50, mb: 50 }),
      ] }));
      g.subs.forEach((s, i) => rows.push(new TableRow({ cantSplit: true, children: [
        cell([P(s.title, { size: 9.5, after: 0 })], { w: wc[0], mt: 30, mb: 30,
          fill: i % 2 ? undefined : TEAL_TINT }),
        cell([P(s.range, { size: 9.5, after: 0, align: AlignmentType.CENTER, color: MUTED })],
          { w: wc[1], mt: 30, mb: 30, fill: i % 2 ? undefined : TEAL_TINT }),
        cell([P(String(s.n), { size: 9.5, after: 0, align: AlignmentType.CENTER, color: MUTED })],
          { w: wc[2], mt: 30, mb: 30, fill: i % 2 ? undefined : TEAL_TINT }),
      ] })));
    }
    return [
      sectionBar("INDEX", "topic, subtopic and the questions that sit under it"),
      gap(120),
      new Table({ columnWidths: wc, width: { size: W, type: WidthType.DXA }, rows }),
      new Paragraph({ children: [new PageBreak()], spacing: { after: 0 } }),
    ];
  };

  const titleBlock = (docTitle, subtitle, extra) => [
    new Paragraph({ spacing: { after: 20 }, children: [new TextRun({
      text: cfg.headerLine, font: BODY, size: 17, color: TEAL, bold: true })] }),
    new Paragraph({ spacing: { after: 40 }, children: [new TextRun({
      text: docTitle, font: HEAD, size: 32, bold: true, color: TEAL_DEEP })] }),
    new Paragraph({ spacing: { after: 150 }, children: [new TextRun({
      text: subtitle, font: BODY, size: 19, italics: true, color: MUTED })] }),
    ...(extra || []),
  ];

  // ---- THE WORKED SOLUTION PANEL (solutions edition only)
  //
  // The panel sits exactly where the ruled working space sits in the workbook,
  // so a student can lay the two editions side by side and compare his own
  // working line for line against the printed one. It is built from the four
  // things this bank already holds for every item and has already verified:
  // the METHOD the item is testing, the WORKING itself, the ANSWER as it is
  // typeset in the option list, and what each wrong option means. Nothing in
  // the panel is written fresh here, so nothing in it can drift away from the
  // answers that were re-derived in Python.
  const SOL_FILL = "F4FAF9";
  const hair = { style: BorderStyle.SINGLE, size: 2, color: "DCE9E8" };
  const solRow = (label, kids, o = {}) => new TableRow({
    cantSplit: true,
    children: [
      new TableCell({ width: { size: 1320, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: SOL_FILL, color: "auto" },
        borders: { top: hair, bottom: hair, left: NB, right: NB },
        margins: { top: 45, bottom: 45, left: 110, right: 80 },
        children: [new Paragraph({ spacing: { after: 0 }, children: [new TextRun({
          text: label, font: HEAD, size: 16, bold: true,
          color: o.colour ?? TEAL_DEEP })] })] }),
      new TableCell({ width: { size: W - 1320, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: SOL_FILL, color: "auto" },
        borders: { top: hair, bottom: hair, left: NB, right: NB },
        margins: { top: 45, bottom: 45, left: 0, right: 110 },
        children: kids }),
    ],
  });
  const solText = (text, o = {}) => new Paragraph({
    spacing: { after: o.after ?? 0 },
    children: [new TextRun({ text, font: BODY, size: o.size ?? 18,
      italics: o.italic, color: o.colour ?? CHARCOAL })] });

  function solutionPanel(it) {
    // the trick field is authored as "method — mistake"; a handful have no
    // split, and those simply do not get an AVOID line rather than getting a
    // guessed one.
    const cut = it.trick ? it.trick.indexOf(" — ") : -1;
    const method = cut < 0 ? (it.trick || "") : it.trick.slice(0, cut);
    const mistake = cut < 0 ? "" : it.trick.slice(cut + 3);
    const cap = (s) => (s ? s.trim().charAt(0).toUpperCase() + s.trim().slice(1)
      + (/[.!?]$/.test(s.trim()) ? "" : ".") : "");

    const chosen = it.opts[it.ans];
    const ansKids = [new Paragraph({ spacing: { after: 0 }, children: [
      new TextRun({ text: LETTER[it.ans] + "    ", font: HEAD, size: 20,
        bold: true, color: MAROON }),
      ...(typeof chosen === "string"
        ? [new TextRun({ text: chosen, font: BODY, size: 19, color: CHARCOAL })]
        : [eqRun(chosen.eq, (chosen.k ?? 1.05) * 1.02)]),
    ] })];

    const rows = [
      new TableRow({ cantSplit: true, children: [new TableCell({
        columnSpan: 2, width: { size: W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: TEAL_DEEP, color: "auto" },
        borders: noBorders, margins: { top: 45, bottom: 45, left: 110, right: 110 },
        children: [new Paragraph({ spacing: { after: 0 },
          tabStops: [{ type: "right", position: W - 260 }],
          children: [
            new TextRun({ text: "WORKED SOLUTION", font: HEAD, size: 16,
              bold: true, color: "FFFFFF" }),
            new TextRun({ text: "\tAnswer   " + LETTER[it.ans], font: HEAD,
              size: 16, bold: true, color: "CFEBE8" }),
          ] })] })] }),
      solRow("1 · Set up", [solText(cap(method))]),
      solRow("2 · Working", [solText(it.why, { size: 19 })]),
      solRow("3 · Answer", ansKids),
    ];
    if (it.traps && it.traps.length) {
      rows.push(solRow("The others", it.traps.map((t, i) =>
        solText(t, { size: 17, colour: MUTED, after: i === it.traps.length - 1 ? 0 : 30 }))));
    }
    if (mistake) {
      rows.push(solRow("Avoid", [solText(cap(mistake), { size: 17, colour: MAROON })],
        { colour: MAROON }));
    }
    return new Table({ columnWidths: [1320, W - 1320],
      width: { size: W, type: WidthType.DXA }, rows });
  }

  // ---- one item, student version
  function itemBlock(it, n) {
    const kids = [];
    const stemRuns = [
      new TextRun({ text: `${n}.  `, font: HEAD, size: SZ(cfg, 21, 20), bold: true, color: TEAL_DEEP }),
      new TextRun({ text: it.stem, font: BODY, size: SZ(cfg, 21, 20), color: CHARCOAL }),
      // ONE star is a multi-step item, TWO is the top band. Until now only
      // lvl 3 was starred, which left the 135 hardest questions in the bank
      // looking like routine ones.
      ...(it.lvl >= 4 ? [new TextRun({ text: "  ★★", font: BODY, size: 20, color: MAROON })]
        : it.lvl === 3 ? [new TextRun({ text: "  ★", font: BODY, size: 20, color: MAROON })] : []),
    ];
    // A figured item puts the diagram to the RIGHT of the stem, as the real
    // paper does: stem and any expression on the left, figure on the right.
    if (it.fig) {
      const FW = Math.round((it.figW ?? 1.9) * 1440) + 200;
      const TW = W - FW;
      const left = [new Paragraph({ keepNext: true, keepLines: true,
        spacing: { before: 40, after: it.stemEq ? 20 : 40 }, children: stemRuns })];
      if (it.stemEq) left.push(mathP(it.stemEq, it.k ?? (cfg.dense ? 1.15 : 1.3),
        { align: AlignmentType.LEFT, before: 30, after: it.note ? 10 : 20, keepNext: true }));
      if (it.note) left.push(P(it.note, { size: 10.5, after: 20 }));
      kids.push(new Table({
        columnWidths: [TW, FW], width: { size: W, type: WidthType.DXA },
        rows: [new TableRow({ cantSplit: true, children: [
          cell(left, { w: TW, plain: true, valign: VerticalAlign.CENTER }),
          cell([new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 },
            children: [figRun(it.fig, it.figW ?? 1.9)] })],
            { w: FW, plain: true, valign: VerticalAlign.CENTER }),
        ] })],
      }));
      kids.push(gap(40));
    } else {
      kids.push(new Paragraph({ keepNext: true, keepLines: true, spacing: { before: 40, after: it.stemEq ? 20 : 130 }, children: stemRuns }));
      if (it.stemEq) kids.push(mathP(it.stemEq, it.k ?? (cfg.dense ? 1.2 : 1.35),
        { before: 30, after: it.note ? 10 : 40, keepNext: true }));
      if (it.note) kids.push(new Paragraph({ keepNext: true, spacing: { before: 0, after: 50 },
        indent: { left: 450 },
        children: [new TextRun({ text: it.note, font: BODY, size: 21, color: CHARCOAL })] }));
    }
    if (it.table) {
      const cw = Math.floor((W - 900) / it.table[0].length);
      kids.push(new Table({
        columnWidths: Array(it.table[0].length).fill(cw),
        width: { size: W - 900, type: WidthType.DXA },
        indent: { size: 450, type: WidthType.DXA },
        rows: it.table.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c) => cell(
          [new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { after: 0 },
            children: [new TextRun({ text: c, font: BODY, size: 19, bold: ri === 0,
              color: ri === 0 ? "FFFFFF" : CHARCOAL })] })],
          { w: cw, fill: ri === 0 ? TEAL : (ri % 2 ? TEAL_TINT : undefined) })) })),
      }));
      kids.push(gap(60));
    }
    // A HINT points at the tool without doing the work; a CAUTION names the
    // mistake the distractors are waiting for. Both sit BEFORE the options —
    // after them they would only be read once the choice was already made.
    const aside = (tag, text, colour, fill) => new Table({
      columnWidths: [70, W - 70], width: { size: W, type: WidthType.DXA },
      rows: [new TableRow({ cantSplit: true, children: [
        cell([new Paragraph({ spacing: { after: 0 }, children: [] })],
          { w: 70, fill: colour, mt: 25, mb: 25 }),
        cell([new Paragraph({ spacing: { after: 0 }, children: [
          new TextRun({ text: tag + "  ", font: BODY, size: SZ(cfg, 17, 16),
            bold: true, color: colour }),
          new TextRun({ text, font: BODY, size: SZ(cfg, 17, 16), color: CHARCOAL }),
        ] })], { w: W - 70, fill, mt: 25, mb: 25 }),
      ] })],
    });
    // In the SOLUTIONS edition the full method is printed a few lines below,
    // so a hint above the options is only noise; the CAREFUL line stays,
    // because a named mistake is worth reading before the working, not after.
    if (it.hint && !cfg.noHint) { kids.push(aside("HINT", it.hint, TEAL_DEEP, TEAL_TINT)); kids.push(gap(30)); }
    // and the CAREFUL strip goes the same way in that edition: the panel's own
    // AVOID line is the same warning, so printing both put the identical
    // sentence on the page twice, once above the options and once below them.
    if (it.caution && !cfg.noCaution) { kids.push(aside("CAREFUL", it.caution, MAROON, "FBEDEC")); kids.push(gap(30)); }

    // GRID-IN (Student-Produced Response): no options at all -- a boxed
    // answer cell, the way the real SAT grid works (a single number or
    // simple fraction, not a multiple-choice letter).
    if (it.gridIn) {
      kids.push(new Table({
        columnWidths: [1900, W - 1900], width: { size: W, type: WidthType.DXA },
        rows: [new TableRow({ cantSplit: true, children: [
          cell([new Paragraph({ spacing: { after: 0 }, children: [
            new TextRun({ text: "Answer", font: BODY, size: SZ(cfg, 17, 16), bold: true, color: MAROON }),
          ] })], { w: 1900, mt: 30, mb: 30, valign: VerticalAlign.CENTER }),
          cell([new Paragraph({ spacing: { after: 0 }, children: [
            new TextRun({ text: "(student-produced response — write a single number)",
              font: BODY, size: 15, italics: true, color: MUTED }),
          ] })], { w: W - 1900, plain: true, valign: VerticalAlign.CENTER }),
        ] })],
      }));
    } else {
    // options — one row of four, two rows of two when an item sets
    // `optGrid: 2`, or one option per line when it sets `optGrid: 1`, which is
    // what long prose options need to stay readable. A quarter of the page is about an inch and a half of
    // printable width; an expression wider than that used to be clipped at the
    // cell edge, which is how an option can silently lose its last factor.
    const perRow = it.optGrid === 1 ? 1 : it.optGrid === 2 ? 2 : 4;
    const ow = Math.floor(W / perRow);
    const optCell = (o, i) => {
        const label = new TextRun({ text: `(${LETTER[i]})  `, font: BODY, size: SZ(cfg, 19, 18), bold: true, color: MAROON });
        if (typeof o === "string") {
          return cell([new Paragraph({ spacing: { after: 0 }, children: [
            label, new TextRun({ text: o, font: BODY, size: SZ(cfg, 19, 18), color: CHARCOAL })] })],
            { w: ow, valign: VerticalAlign.CENTER });
        }
        // Letter and expression share ONE line. Two paragraphs cost an extra
        // line of height per option, which across 20 items is a whole page —
        // that is what pushed all four papers to five pages.
        return cell([
          new Paragraph({ spacing: { before: 0, after: 0 }, keepLines: true,
            children: [label, eqRun(o.eq, o.k ?? ((cfg.dense ? 1.05 : 1.2) * (cfg.optScale ?? 1)))] }),
        ], { w: ow, valign: VerticalAlign.CENTER });
    };
    const optRows = [];
    for (let r = 0; r < it.opts.length; r += perRow) {
      optRows.push(new TableRow({ cantSplit: true,
        children: it.opts.slice(r, r + perRow).map((o, j) => optCell(o, r + j)) }));
    }
    kids.push(new Table({
      columnWidths: Array(perRow).fill(ow), width: { size: W, type: WidthType.DXA },
      rows: optRows,
    }));
    }
    // WORKING SPACE. Ruled lines rather than blank paper: a student who has
    // somewhere to put the second line of working is far likelier to write it,
    // and Tahsili is lost in the steps that never got written down. The number
    // of lines is set by the item's level, so a one-step conversion does not
    // get the same half page as an optimisation problem.
    const lines = cfg.workLines ? cfg.workLines(it) : 0;
    if (cfg.solution) {
      kids.push(solutionPanel(it));
    } else if (lines) {
      const rule = { style: BorderStyle.SINGLE, size: 4, color: "DCE9E8" };
      kids.push(new Paragraph({ spacing: { before: 40, after: 20 }, keepNext: true,
        children: [new TextRun({ text: "Working", font: BODY, size: 15, color: MUTED,
          italics: true })] }));
      kids.push(new Table({
        columnWidths: [W], width: { size: W, type: WidthType.DXA },
        rows: Array.from({ length: lines }, () => new TableRow({
          cantSplit: true, height: { value: 300, rule: "atLeast" },
          children: [new TableCell({
            width: { size: W, type: WidthType.DXA },
            borders: { top: NB, left: NB, right: NB, bottom: rule },
            children: [new Paragraph({ spacing: { after: 0 }, children: [] })],
          })] })),
      }));
    }
    kids.push(gap(cfg.itemGap ?? 150));
    return kids;
  }

  // =================================================== STUDENT PAPER
  function paper() {
    const front = [];
    if (cfg.cover) front.push(...coverPage(cfg.cover));
    if (cfg.contents) front.push(...contentsPages(cfg.contents));
    const k = front.concat(titleBlock(cfg.paperTitle, cfg.paperSub, [
      new Table({ columnWidths: [5760, 3600], width: { size: W, type: WidthType.DXA },
        rows: [new TableRow({ children: [
          cell([P("Student name :  ...............................................................", { size: 11 })], { w: 5760, fill: TEAL_TINT }),
          cell([P("Class :  ...................    Date :  ......................", { size: 11 })], { w: 3600, fill: TEAL_TINT }),
        ] })] }),
      gap(cfg.dense ? 80 : 140),
    ]));

    // Mr Thiab's rule: the student paper opens on question 1. Conditions,
    // timing and marking move to the answer key, where the teacher needs them.
    if (!cfg.bare) {
      k.push(sectionBar("EXAM CONDITIONS", "read before you start"));
      k.push(gap(70));
      k.push(new Table({ columnWidths: [2340, 2340, 2340, 2340], width: { size: W, type: WidthType.DXA },
        rows: [
          new TableRow({ children: ["Questions", "Time", "Calculator", "Marking"].map((h) =>
            cell([P(h, { size: 9.5, bold: true, color: "FFFFFF", align: AlignmentType.CENTER })], { w: 2340, fill: TEAL })) }),
          new TableRow({ children: [
            `${cfg.items.length} multiple choice`, cfg.timing,
            // a paper carrying two exams has two calculator rules — say which
            cfg.calculator || "NOT allowed", cfg.marking || "One mark each, no penalty",
          ].map((t) => cell([P(t, { size: 10, align: AlignmentType.CENTER })], { w: 2340, fill: TEAL_TINT })) }),
        ] }));
      k.push(gap(90));
      k.push(P(cfg.conditions, { size: cfg.dense ? 9 : 10, italic: true, color: MUTED, after: cfg.dense ? 40 : 60 }));
      if (cfg.compareNote) {
        k.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
          rows: [new TableRow({ children: [cell([P(cfg.compareNote,
            { size: cfg.dense ? 9.5 : 10, after: 0 })], { w: W, fill: TEAL_TINT2 })] })] }));
        k.push(gap(cfg.dense ? 70 : 110));
      }
      k.push(P(cfg.starNote || "★ marks a multi-step analysis item — the level the examiner uses to separate the top band. Attempt it, but not first.",
        { size: cfg.dense ? 9 : 10, italic: true, color: MAROON, after: cfg.dense ? 110 : 200 }));
    }
    if (!cfg.bare) {
      k.push(sectionBar("QUESTIONS"));
      k.push(gap(cfg.dense ? 70 : 120));
    }
    cfg.items.forEach((it, i) => {
      const block = [];
      // A paper that carries two exams (SAT then GAT) needs a divider mid-run.
      // `sec` on an item opens a titled band before it; `sec.newPage` starts it
      // on a fresh sheet so each exam owns whole pages rather than sharing one.
      if (it.sec) {
        if (it.sec.newPage)
          k.push(new Paragraph({ children: [new PageBreak()], spacing: { after: 0 } }));
        block.push(sectionBar(it.sec.title, it.sec.note));
        block.push(gap(cfg.dense ? 70 : 120));
        if (it.sec.conditions)
          block.push(P(it.sec.conditions, { size: cfg.dense ? 9 : 10, italic: true,
                                            color: MUTED, after: cfg.dense ? 90 : 140 }));
      }
      // `sub` opens a SUBTOPIC strip inside the current band
      if (it.sub) {
        // breathe before a new group — outside the block, so the space collapses
        // at a page top instead of pushing the heading down
        if (!it.sec) k.push(gap(cfg.dense ? 110 : 170));
        block.push(subBar(it.sub.title, it.sub.note));
        block.push(gap(cfg.dense ? 60 : 100));
      }
      block.push(...itemBlock(it, i + 1));
      // KEEP THE QUESTION WHOLE. A question split across a page break is the
      // one layout fault a student actually pays for: the options end up on a
      // sheet away from the stem, or the working space away from both. One
      // un-splittable table row round the whole block — heading included, so a
      // band is never stranded alone at the foot of a page — is what Word
      // honours; keepNext on the paragraphs is not enough once tables are in
      // the mix.
      if (cfg.keepTogether) k.push(keepWhole(block));
      else k.push(...block);
    });

    if (!cfg.bare) {
      k.push(gap(60));
      k.push(new Table({ columnWidths: [W], width: { size: W, type: WidthType.DXA },
        rows: [new TableRow({ children: [cell([
          P("Before you hand this in", { size: 10.5, bold: true, color: TEAL_DEEP, after: 60 }),
          P("Count your blanks. An unanswered question scores nothing and there is no penalty for a wrong answer, so every question gets a letter. Then circle the three you were least sure of — those are the three we work through together.", { size: 10 }),
        ], { w: W, fill: TEAL_TINT })] })] }));
    }
    return makeDoc(cfg.paperTitle, k);
  }

  // =================================================== ANSWER KEY
  function key() {
    const k = titleBlock(cfg.keyTitle, cfg.keySub);

    // strand budget check
    const tally = {};
    cfg.items.forEach((it) => { const s = it.code.split(".")[0]; tally[s] = (tally[s] || 0) + 1; });
    const strands = Object.keys(tally);
    k.push(sectionBar("ITEM BUDGET", cfg.budgetNote || "the set is built to the official weighting — check it before you print"));
    k.push(gap(70));
    const cw = Math.floor(W / strands.length);
    k.push(new Table({ columnWidths: Array(strands.length).fill(cw), width: { size: W, type: WidthType.DXA },
      rows: [
        new TableRow({ children: strands.map((s) => cell([P(s, { size: 9, bold: true, color: "FFFFFF", align: AlignmentType.CENTER })], { w: cw, fill: TEAL })) }),
        new TableRow({ children: strands.map((s) => cell([
          P(`${tally[s]} items`, { size: 10, bold: true, align: AlignmentType.CENTER, color: TEAL_DEEP }),
          P(`${Math.round((tally[s] / cfg.items.length) * 100)}%   (target ${cfg.targets[s] || "—"})`,
            { size: 9, align: AlignmentType.CENTER, color: MUTED }),
        ], { w: cw, fill: TEAL_TINT })) }),
      ] }));
    k.push(gap(160));

    k.push(sectionBar("ANSWERS, REASONING AND THE ERROR BEHIND EACH DISTRACTOR"));
    k.push(gap(80));
    const wq = [760, 1500, 620, W - 2880];   // Q column wide enough for three digits
    k.push(new Table({ columnWidths: wq, width: { size: W, type: WidthType.DXA },
      rows: [
        new TableRow({ tableHeader: true, children: ["Q", "Strand code", "Answer", "Why — and what each wrong option means"]
          .map((h, i) => cell([P(h, { size: 9.5, bold: true, color: "FFFFFF" })], { w: wq[i], fill: TEAL })) }),
        // the key follows the same topic / subtopic order as the paper, and
        // carries the same headings, so a teacher marking one group does not
        // have to count rows to find where it starts
        ...cfg.items.flatMap((it, i) => [
          ...(it.sec ? [new TableRow({ cantSplit: true, children: [cell(
            [new Paragraph({ spacing: { after: 0 }, children: [new TextRun({
              text: it.sec.title, font: HEAD, size: 18, bold: true, color: "FFFFFF" })] })],
            { w: W, span: 4, fill: TEAL_DEEP, mt: 50, mb: 50 })] })] : []),
          ...(it.sub ? [new TableRow({ cantSplit: true, children: [cell(
            [new Paragraph({ spacing: { after: 0 }, children: [
              new TextRun({ text: it.sub.title, font: HEAD, size: 16, bold: true, color: TEAL_DEEP }),
              ...(it.sub.note ? [new TextRun({ text: `     ${it.sub.note}`, font: BODY,
                size: 14, color: MUTED })] : []),
            ] })],
            { w: W, span: 4, fill: TEAL_TINT2, mt: 40, mb: 40 })] })] : []),
          new TableRow({ children: [
          cell([P(String(i + 1) + (it.lvl >= 4 ? " ★★" : it.lvl === 3 ? " ★" : ""), { size: 10, bold: true, color: TEAL_DEEP, align: AlignmentType.CENTER })],
            { w: wq[0], fill: i % 2 ? TEAL_TINT : undefined }),
          cell([P(it.code, { size: 8.5, color: MAROON, bold: true })], { w: wq[1], fill: i % 2 ? TEAL_TINT : undefined }),
          cell([P(it.gridIn ? (it.gridAnswer || "") : LETTER[it.ans], { size: it.gridIn ? 9.5 : 12, bold: true, color: TEAL_DEEP, align: AlignmentType.CENTER })],
            { w: wq[2], fill: i % 2 ? TEAL_TINT : undefined }),
          cell([
            new Paragraph({ spacing: { after: it.traps && it.traps.length ? 40 : 0 },
              children: whyRuns(it) }),
            ...(it.traps || []).map((t) => P(t, { size: 8.5, color: MUTED, italic: true, after: 20 })),
          ], { w: wq[3], fill: i % 2 ? TEAL_TINT : undefined }),
        ] })]),
      ] }));
    k.push(gap(cfg.dense ? 110 : 180));

    k.push(sectionBar("HOW TO USE THE RESULT", "the set is diagnostic — the score is the least interesting part of it"));
    k.push(gap(70));
    k.push(new Table({ columnWidths: [2200, W - 2200], width: { size: W, type: WidthType.DXA },
      rows: cfg.followUp.map((r, i) => new TableRow({ children: [
        cell([P(r[0], { size: 10, bold: true, color: TEAL_DEEP })], { w: 2200, fill: i % 2 ? TEAL_TINT : TEAL_TINT2 }),
        cell([P(r[1], { size: 10 })], { w: W - 2200, fill: i % 2 ? TEAL_TINT : undefined }),
      ] })) }));
    k.push(gap(160));
    k.push(P(cfg.sourceNote, { size: 9.5, italic: true, color: MUTED }));
    return makeDoc(cfg.keyTitle, k);
  }

  return { paper, key };
}

async function buildSet(cfg) {
  const e = makeEngine(cfg);
  const jobs = [[e.paper(), cfg.outPaper], [e.key(), cfg.outKey]];
  for (const [doc, name] of jobs) {
    const b = await Packer.toBuffer(doc);
    fs.writeFileSync(A(name), b);
    console.log("  wrote", name, Math.round(b.length / 1024) + " KB");
  }
}

module.exports = { buildSet };

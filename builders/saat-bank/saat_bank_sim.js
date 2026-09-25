// ---------------------------------------------------------------------------
// SAAT BOOKLET — MATHEMATICS
//
// WHAT THIS IS. The department's Tahsili question booklet for Grades 11 and 12,
// organised by TOPIC. No session number and no week appears anywhere in it: a
// question is found by the skill it tests, not by the day it was taught.
//
// Part A came from the 2021 SAAT set — 37 skills, two items each. Parts B and C
// are number, algebra, equations and quadratics, written out objective by
// objective. Part D is the yield of the Arabic teaching book in the project
// files — 204 worked examples mined for their skills and tricks, never for
// their questions. Part E is reasoning and logic, which the course had no slot
// for, together with the topics the booklet had not yet reached. Part F is the
// yield of the eight official ETEC sample papers: polar coordinates, complex
// numbers in polar form, vectors, matrices, and the questions that hand the
// student a PICTURE — every one of those figures drawn from scratch.
//
// WHY IT IS WRITTEN AND NOT COPIED. Candidates leave the hall and reconstruct
// questions from memory, so recall sheets circulate; ETEC knows this and never
// repeats a question. It repeats IDEAS. A bank of remembered questions is
// therefore worth very little, and a bank of the same ideas rewritten is worth
// a great deal. Nothing below reproduces a source stem, number set, option list
// or figure.
//
// THREE GUARDS RUN AT BUILD TIME.
//   1. No two items may share a `sig`, their skill-and-trick signature.
//   2. Every item carries a named trick and exactly three distractor notes.
//   3. Every figure places its labels through figlabel.py, which measures each
//      label's rendered box and refuses to ship one that sits on the drawing.
//
// Every answer was re-derived independently in Python before release
// (verify_saat.py, 0 failures), and the answer positions were balanced to
// 19/19/18/18 rather than left where the arithmetic happened to put them.
// ---------------------------------------------------------------------------
const { buildSet } = require("./exam_engine");
const MAP = require("./saat_skill_map.js");
const ITEMS = [...require("./saat_items_a.js"), ...require("./saat_items_b.js"), ...require("./saat_items_c.js"), ...require("./saat_items_d.js"), ...require("./saat_items_e.js"), ...require("./saat_items_f.js"), ...require("./saat_items_g.js"), ...require("./saat_items_h.js"), ...require("./saat_items_i.js"), ...require("./saat_items_j.js"), ...require("./saat_items_k.js"), ...require("./saat_items_l.js"), ...require("./saat_items_m.js")];

// PLACEMENT. The booklet is organised by TOPIC, not by the week a session falls
// in, and no session number is printed anywhere in it. The 135-session map is
// still what the earlier parts were written against, so it is used here only to
// look up the unit and the topic title of an item that does not carry its own.
// An item may set `unit` and `topic` directly — reasoning and logic does, since
// the department's course has no session for it — and such an item is placed on
// its own terms.
const SES = new Map();
for (const row of MAP) for (const g of row.sigs) SES.set(g, row.s);
const ROW = new Map(MAP.map((r) => [r.s, r]));
for (const it of ITEMS) {
  if (it.ses === undefined && it.unit === undefined) it.ses = SES.get(it.sig);
  const row = it.ses === undefined ? undefined : ROW.get(it.ses);
  if (it.ses !== undefined && !row)
    throw new Error(`${it.sig} names a session the syllabus has no row for: ${it.ses}`);
  if (it.unit === undefined) {
    if (!row) throw new Error(`${it.sig} carries neither a unit nor a known topic`);
    it.unit = row.u;
  }
  if (it.topic === undefined) {
    if (!row) throw new Error(`${it.sig} carries no topic title`);
    it.topic = row.title;
  }
}

ITEMS.sort((a, b) => a.unit - b.unit || (a.ses ?? 0) - (b.ses ?? 0) || a.lvl - b.lvl);

const seen = new Map();
for (const it of ITEMS) {
  if (!it.sig) throw new Error("item carries no skill signature: " + it.stem.slice(0, 50));
  if (seen.has(it.sig))
    throw new Error(`two items share the skill "${it.sig}" — one of them is a repeat:\n` +
                    `  1) ${seen.get(it.sig).slice(0, 70)}\n  2) ${it.stem.slice(0, 70)}`);
  seen.set(it.sig, it.stem);
  if (!it.trick) throw new Error("no trick recorded for " + it.sig);
  if (!it.traps || it.traps.length !== 3)
    throw new Error("an item needs exactly three distractor notes: " + it.sig);
  if (!/^SAAT-M-(ALG|GEO|TRI|CAL|STA)\.\d+$/.test(it.code))
    throw new Error("bad strand code on " + it.sig + ": " + it.code);
}

const tally = {};
for (const it of ITEMS) {
  const s = it.code.split(".")[0];
  tally[s] = (tally[s] || 0) + 1;
}
const pct = (k) => Math.round((tally[k] / ITEMS.length) * 100);

// A titled band opens each part of the booklet, and every item names its TOPIC.
// Nothing here refers to a session or to a week of the course.
const UNIT_TITLE = {
  0: "REASONING & LOGIC",
  1: "UNIT 1 — NUMBER, ALGEBRA & ALGEBRAIC REASONING",
  2: "UNIT 2 — EQUATIONS, SYSTEMS & QUADRATICS",
  3: "UNIT 3 — FUNCTIONS & MODELING",
  4: "UNIT 4 — GEOMETRY & MEASUREMENT",
  5: "UNIT 5 — COORDINATE GEOMETRY, STATISTICS & PROBABILITY",
  6: "UNIT 6 — EXPONENTIAL & LOGARITHMIC FUNCTIONS",
  7: "UNIT 7 — SEQUENCES, SERIES & COMPLEX NUMBERS",
  8: "UNIT 8 — TRIGONOMETRY I",
  9: "UNIT 9 — TRIGONOMETRY II",
  10: "UNIT 10 — ANALYTIC GEOMETRY & CONIC SECTIONS",
  11: "UNIT 11 — LIMITS & DERIVATIVES",
  12: "UNIT 12 — APPLICATIONS OF DERIVATIVES",
  13: "UNIT 13 — INTEGRATION & ITS APPLICATIONS",
};
// TOPIC AND SUBTOPIC. A solid band opens each TOPIC and a tinted strip opens
// each SUBTOPIC inside it. Still no session number and no week anywhere: the
// subtopic title is the name of the skill group, not the name of a lesson slot.
// Items are grouped so that every question under a strip really belongs to it —
// the sort is unit, then subtopic, then difficulty.
const SUBORDER = new Map();
for (const it of ITEMS) {
  const k = `${it.unit}|${it.topic}`;
  if (!SUBORDER.has(k)) SUBORDER.set(k, SUBORDER.size);
}
ITEMS.sort((a, b) => a.unit - b.unit
  || SUBORDER.get(`${a.unit}|${a.topic}`) - SUBORDER.get(`${b.unit}|${b.topic}`)
  || a.lvl - b.lvl);

const COUNT = {};
for (const it of ITEMS) COUNT[it.unit] = (COUNT[it.unit] || 0) + 1;

// walk the sorted run once, opening bands and strips and recording the question
// ranges the index needs
const CONTENTS = [];
let lastUnit = null, lastTopic = null, unitRow = null, subRow = null;
ITEMS.forEach((it, i) => {
  const n = i + 1;
  if (it.unit !== lastUnit) {
    it.sec = { title: UNIT_TITLE[it.unit], note: `${COUNT[it.unit]} questions` };
    unitRow = { title: UNIT_TITLE[it.unit], from: n, to: n, n: COUNT[it.unit], subs: [] };
    CONTENTS.push(unitRow);
    lastUnit = it.unit;
    lastTopic = null;
  }
  if (it.topic !== lastTopic) {
    it.sub = { title: it.topic };
    subRow = { title: it.topic, from: n, to: n, n: 0 };
    unitRow.subs.push(subRow);
    lastTopic = it.topic;
  }
  subRow.to = n; subRow.n += 1;
  unitRow.to = n;
});
const RANGE = (r) => (r.from === r.to ? `${r.from}` : `${r.from} – ${r.to}`);
for (const u of CONTENTS) {
  u.range = RANGE(u);
  for (const s of u.subs) s.range = RANGE(s);
}
// the subtopic strip carries its own count, so a teacher setting a ten-minute
// drill can see the size of a group without counting down the page
for (const u of CONTENTS)
  for (const s of u.subs) {
    const first = ITEMS[s.from - 1];
    first.sub.note = `Q ${s.range}  ·  ${s.n} question${s.n === 1 ? "" : "s"}`;
  }

// ---------------------------------------------------------------------------
// HINTS AND CAUTIONS. Every item already carries a `trick` — the teacher's
// one-line account of what the question is really testing and what the
// distractors are waiting for. It is written in a fixed shape: the METHOD,
// then an em dash, then the MISTAKE. That split is exactly the two things a
// student needs, so the hint and the caution are taken from it rather than
// written twice and allowed to drift apart.
//
//   hint    — the method pointer, on the top band only (★★). It names the tool
//             and stops; it never does the arithmetic.
//   caution — the mistake to avoid, on every multi-step item (★ and ★★).
//
// A hint that contains the correct answer is refused outright: a nudge that
// hands over the answer is worse than no nudge, because it teaches the student
// to read the hint instead of the question.
// ---------------------------------------------------------------------------
const TIDY = (s) => {
  // the clause after the dash often begins "and …", which reads badly as the
  // opening word of its own sentence
  s = s.trim().replace(/^[,;:]\s*/, "").replace(/^(and|so)\s+/i, "");
  return s.charAt(0).toUpperCase() + s.slice(1) + (/[.!?]$/.test(s) ? "" : ".");
};
// A method clause that ends "…, so <something> = <number>" has stopped being a
// hint and started being the working. Cut it there: naming the step is a nudge,
// carrying it out is the student's job. ("three means make FIVE terms, so
// r⁴ = 625" leaves ±5 with nothing left to do.)
const CUT = (s) => {
  const m = s.match(/,\s+so\s+[^,]*?=\s*-?\d/);
  return m ? s.slice(0, m.index) : s;
};
// REVIEWED BY HAND. The split above gives a good caution for almost every item,
// but a handful of tricks put the WORKING in the second clause rather than the
// mistake, and those cautions were handing the answer over: "so the apex is
// 180 − 2(72)", "the answer is simply √(4 + 25)". Each one below is rewritten to
// name the trap and stop. The build reports any NEW aside that carries worked
// arithmetic, so the next source cannot slip one through unnoticed.
// Two structural items have tricks that state the answer in their METHOD clause
// ("they add to 180° whatever the polygon is"), so the leak guard refused a hint
// for them — correctly. A hand-written nudge points at the structure without
// giving the number away, which is what those items actually need.
const HINT_FIX = {
  "interior-plus-exterior-angle-is-a-straight-angle":
    "Look at how the two marked angles sit against the produced side, not at the pentagon.",
  "angle-sum-without-finding-any-angle":
    "You are not asked for any single angle — look for a figure all three belong to.",
};
const CAUTION_FIX = {
  "pentagon-with-an-attached-triangle":
    "The exterior angle is only the first step; the triangle still has to add to 180°.",
  "distance-between-two-polar-points":
    "The cosine term only vanishes when the two angles differ by 90° — check that difference before dropping it.",
  "limit-by-rationalising":
    "Substituting straight in gives 0/0, which is not an answer; the x only cancels once the conjugate has been used.",
  "permutation-equation-solve":
    "Write both falling products out in full before cancelling; the small numbers inside the symbols are not the answer.",
  "rhombus-diagonal-bisects-the-angle":
    "The angle asked for is the third angle of a right triangle, not the one you were given.",
  "tangent-secant-square":
    "The secant is measured from the external point to the FAR intersection, so the external piece still has to come off.",
  "slope-of-an-implicit-tangent":
    "The tangent is perpendicular to the radius, so the slope is a NEGATIVE reciprocal — a positive answer at a first-quadrant point is wrong on sight.",
  "exact-sine-in-the-third-quadrant":
    "Let the QUADRANT fix the sign; below the axis the sine is negative whatever the reference angle says.",
};
// an aside that carries out arithmetic has stopped warning and started solving
const ARITH = /\d+\s*[−\-+×*÷\/]\s*\d|=\s*-?\d|\d+\s*\(\s*\d/;
let hinted = 0, cautioned = 0, leaks = 0, noSplit = 0, trimmed = 0, fixed = 0;
for (const it of ITEMS) {
  const i = it.trick.indexOf(" — ");
  if (i < 0) { noSplit++; continue; }           // no clean split: say nothing
  const method = it.trick.slice(0, i);
  const mistake = it.trick.slice(i + 3);
  const answer = it.opts[it.ans];

  if (it.lvl >= 4 && HINT_FIX[it.sig]) {
    it.hint = HINT_FIX[it.sig];
    hinted++; fixed++;
  } else if (it.lvl >= 4) {
    const cut = CUT(method);
    if (cut !== method) trimmed++;
    const h = TIDY(cut);
    // the leak guard can only read an answer that is written as text; an
    // answer typeset as an image is checked by eye on the proof
    const bare = typeof answer === "string"
      ? answer.replace(/\s+/g, " ").trim() : null;
    if (bare && bare.length > 2 && h.includes(bare)) { leaks++; }
    else { it.hint = h; hinted++; }
  }
  if (it.lvl >= 3) {
    it.caution = CAUTION_FIX[it.sig] || TIDY(mistake);
    if (CAUTION_FIX[it.sig]) fixed++;
    cautioned++;
  }
}

// ---------------------------------------------------------------------------
// OPTION WIDTH GUARD. A quarter of the text block is 1.47 inches of printable
// width, and the option letter eats a quarter of an inch of that. An expression
// wider than what is left used to be clipped at the cell edge — Word does not
// complain, it just cuts the tail off, and an option missing its last factor is
// worse than no option at all. Anything too wide for four across is laid out
// two across instead; anything too wide for that stops the build.
// ---------------------------------------------------------------------------
const MATH = JSON.parse(require("fs").readFileSync(
  require("path").join(__dirname, "math_saat_doc/_index.json"), "utf8"));
const K = 1.05;                       // the dense option scale the engine uses
const FIT4 = (9360 / 4 - 220) / 1440 - 0.28;
const FIT2 = (9360 / 2 - 220) / 1440 - 0.28;
let widened = 0;
for (const it of ITEMS) {
  const w = it.opts.filter((o) => typeof o === "object")
    .map((o) => MATH[o.eq].win * (o.k ?? K));
  if (!w.length) continue;
  const widest = Math.max(...w);
  if (widest > FIT4) {
    if (widest > FIT2)
      throw new Error(`option too wide even at two across (${widest.toFixed(2)} in): ` + it.sig);
    it.optGrid = 2;
    widened++;
  }
}

// PROSE OPTIONS GO ONE TO A LINE. Four long sentences squeezed across the page
// wrap into ragged three-line cells that are hard to compare; a column of four
// reads down the page like a list, which is what the eye wants.
let stacked = 0;
for (const it of ITEMS) {
  if (it.optGrid) continue;
  const words = it.opts.filter((o) => typeof o === "string");
  if (words.length !== 4) continue;
  if (Math.max(...words.map((w) => w.length)) > 26) {
    it.optGrid = 1;
    stacked++;
  }
}

const SUBCOUNT = CONTENTS.reduce((s, u) => s + u.subs.length, 0);
const FIGCOUNT = ITEMS.filter((it) => it.fig).length;

const CFG = {
  // ---- the cover sheet. The strand mix is drawn as one proportional bar
  // rather than listed as percentages: the shape of the bank is the first
  // thing a reader should see, and algebra being a third of it is the single
  // most useful fact about the Tahsili paper.
  cover: {
    eyebrow: "DAR ALFIKR SCHOOLS  ·  MATHEMATICS DEPARTMENT  ·  2026–27",
    title: "SAAT BOOKLET",
    subtitle: "Tahsili Mathematics  ·  Grades 11 and 12",
    strapline: "Original questions, written skill for skill and trick for trick",
    facts: [
      [String(ITEMS.length), "questions"],
      [String(CONTENTS.length), "topics"],
      [String(SUBCOUNT), "subtopics"],
      [String(FIGCOUNT), "diagrams"],
    ],
    mix: [
      ["Algebra", tally["SAAT-M-ALG"], "0E4F4C"],
      ["Geometry", tally["SAAT-M-GEO"], "1E8F89"],
      ["Calculus", tally["SAAT-M-CAL"], "1F3864"],
      ["Trigonometry", tally["SAAT-M-TRI"], "8A1B17"],
      ["Statistics", tally["SAAT-M-STA"], "8A5A17"],
    ],
    author: "Mr Malek Thiab",
    authorRole: "Mathematics · Diploma Department · Dar Alfikr Schools, Jeddah",
    verified: `All ${ITEMS.length} answers re-derived independently in Python before release — 0 failures. Every diagram places its own labels and asserts its own numbers.`,
    note: [
      "How to use this booklet",
      "Work by SUBTOPIC, not by page. The index opposite gives every subtopic and the run of questions under it, so a ten-minute drill is one strip and a full topic is one band. A starred question is the harder end of its subtopic.",
      "Nothing here is copied. ETEC repeats ideas and never repeats questions, so a bank of remembered questions is worth very little and a bank of the same ideas rewritten is worth a great deal. Every answer was re-derived independently before release, and every diagram was drawn from scratch.",
    ],
  },
  contents: CONTENTS,
  keepTogether: true,        // no question is ever split across a page break
  mathIndex: "math_saat_doc/_index.json",
  figIndex: "figs_saat/_index.json",
  examName: "SAAT (Tahsili) booklet",
  targets: { "SAAT-M-ALG": "~30%", "SAAT-M-GEO": "~20%", "SAAT-M-TRI": "~15%",
             "SAAT-M-CAL": "~20%", "SAAT-M-STA": "~15%" },
  dense: true, itemGap: 55,
  marking: "Two points each",
  budgetNote:
    `${ITEMS.length} questions, covering every topic the Tahsili mathematics paper examines. ` +
    `The mix is ALG ${pct("SAAT-M-ALG")}%, GEO ${pct("SAAT-M-GEO")}%, ` +
    `TRI ${pct("SAAT-M-TRI")}%, CAL ${pct("SAAT-M-CAL")}%, STA ${pct("SAAT-M-STA")}%. ` +
    `The targets beside those figures are the working shares this department uses for ` +
    `Tahsili preparation, not a published ETEC table. The bank is front-loaded on algebra ` +
    `because THE PAPER IS: number, algebra and the quadratic run through everything ` +
    `else. Build a mock by sampling towards the target column, not by taking the ` +
    `first forty questions.`,
  conditions: "No calculator, no phone, no smartwatch. Two points per item. If an item is taking more than about 90 seconds, mark it and move on — Tahsili rewards finishing.",
  sourceNote:
    "These questions are ORIGINAL to this bank. They were written to match, skill for skill and trick for trick, the mathematics section of the 2021 SAAT set, but no wording, number set, option list or figure is reproduced from it. A student who memorised a circulated recall sheet gains nothing here, which is the point: ETEC repeats ideas and never repeats questions. Every answer below was re-derived independently in Python before release, and every figure's labels were placed by a routine that refuses to let a length or an angle sit on the drawing. Answer positions were balanced deliberately across the four letters, so that guessing a letter is worth nothing.",
  weekLine: "Mathematics · 2026–27",
  headerLine: `SAAT (Tahsili) · Mathematics · ${ITEMS.length} questions by topic`,
  paperTitle: "SAAT BOOKLET — Mathematics",
  paperSub: `${ITEMS.length} original questions, grouped by topic and subtopic. Two points each.`,
  starNote: "★ is a multi-step item; ★★ is the top band, and those carry a HINT. Every ★ and ★★ question carries a CAREFUL line naming the mistake its wrong options are built to catch — read it before you choose, not after.",
  keyTitle: "SAAT BOOKLET — Answer Key and Error Analysis",
  keySub: "For Mr Malek Thiab. Every answer re-derived from scratch; each item names the trick it is built on and what each wrong option means.",
  outPaper: "SAAT_Booklet.docx",
  outKey: "SAAT_Booklet_Key.docx",
  timing: "30 minutes for any block of twenty questions",
  followUp: [
    ["66 or more", "Working at the target band across every strand. Move to timed forty-item mocks."],
    ["45 to 65", "Read the strand column, not the total — Tahsili losses are almost always concentrated in one strand."],
    ["Below 45", "Take the algebra band alone, untimed, with the key open. It is a third of this bank and the base of the rest."],
    ["Any pair split", "Where a student answers the plain item of a pair and misses the starred one, the skill is there and the TRICK is not. That is a five-minute correction, not a reteach."],
    ["Whole class", "Any item where more than half the class chose the SAME wrong option is a teaching point, not a marking point."],
  ],
  items: ITEMS,
};

// ---------------------------------------------------------------------------
// TWO BUILDS FROM ONE BANK.
//   the BOOKLET  — compact. The bank itself: hints, cautions, no ruled space,
//                  so a topic still fits in a few sheets and stays printable.
//   the WORKBOOK — the same questions with ruled working space under each one,
//                  sized by level. This is the sit-down-and-solve version, and
//                  it is several times longer, which is the cost of the space.
// Same items, same key: only the layout differs.
// ---------------------------------------------------------------------------
const WORK = {
  ...CFG,
  paperTitle: "SAAT WORKBOOK — Mathematics",
  paperSub: `${ITEMS.length} original questions, grouped by topic and subtopic, with working space under each one.`,
  outPaper: "SAAT_Workbook.docx",
  outKey: "SAAT_Workbook_Key.docx",
  cover: { ...CFG.cover, title: "SAAT WORKBOOK",
    strapline: "Original questions, with room to work and a hint where it counts" },
  // a one-step conversion gets two lines; a multi-step analysis item gets eight
  workLines: (it) => (it.lvl >= 4 ? 8 : it.lvl === 3 ? 5 : it.lvl === 2 ? 3 : 2),
  itemGap: 110,
  keepTogether: true,
};

// ---------------------------------------------------------------------------
// THE SOLUTIONS EDITION. The same questions in the same order with the same
// page numbers' worth of index, but where the workbook rules blank lines this
// one prints the working itself: the method the item is testing, the derivation,
// the answer as it is typeset in the option list, what each wrong option means,
// and the mistake to avoid. A student marks his own workbook page against the
// facing solution; a teacher reads the AVOID lines for the reteach list.
// ---------------------------------------------------------------------------
const SOLN = {
  ...CFG,
  paperTitle: "SAAT WORKBOOK — Worked Solutions",
  paperSub: `${ITEMS.length} original questions, each with the working set out in full under it.`,
  outPaper: "SAAT_Workbook_Solutions.docx",
  outKey: "SAAT_Workbook_Solutions_Key.docx",
  cover: { ...CFG.cover, title: "SAAT SOLUTIONS",
    subtitle: "Tahsili Mathematics  ·  Grades 11 and 12  ·  Worked answers",
    strapline: "Every question with its method, its working and its trap set out in full",
    note: [
      "How to use this edition",
      "This is the WORKBOOK marked. Question for question and number for number it is the same bank, so a student works a page in the workbook and then reads the same numbers here. Do not hand it out before the workbook page has been attempted — a printed method read cold teaches nothing.",
      "Each panel is in one order on purpose. SET UP names the skill the question is testing, WORKING is the derivation, ANSWER is the option exactly as it is printed in the list, THE OTHERS says what each wrong option is made of, and AVOID names the mistake. The last two lines are the teaching: a class that missed an item almost always missed it in the same way, and that way is written there. The booklet's hint and caution strips are not reprinted here — the panel already carries both, in the order the working goes.",
    ] },
  solution: true,        // the panel replaces the ruled working space
  noHint: true,          // the full method is three lines below; a hint is noise
  noCaution: true,       // the panel's AVOID line is the same warning
  itemGap: 150,
  keepTogether: true,
  starNote: "★ is a multi-step item; ★★ is the top band. The hint and the caution that sit beside these questions in the booklet are not repeated here — the panel under each question says the same things in full, in the order the working goes.",
  keyTitle: "SAAT SOLUTIONS — Answer Key and Error Analysis",
};

module.exports = { SAAT: CFG, SAAT_WORK: WORK, SAAT_SOLN: SOLN };

if (require.main === module) {
  (async () => {
    await buildSet(CFG);
    await buildSet(WORK);
    await buildSet(SOLN);
    console.log("  skills:", ITEMS.length, "| strands:", JSON.stringify(tally));
    console.log("  two options across:", widened, "| one option per line:", stacked);
    const carry = ITEMS.filter((it) => [it.hint, it.caution]
      .some((t) => t && ARITH.test(t) && !CAUTION_FIX[it.sig]));
    console.log("  hints:", hinted, "| cautions:", cautioned,
                "| rewritten by hand:", fixed,
                "| still carrying arithmetic (reviewed, kept):", carry.length);
    console.log("  trimmed before the working:", trimmed,
                "| refused as answer-leaking:", leaks,
                "| tricks with no clean split:", noSplit);
  })();
}

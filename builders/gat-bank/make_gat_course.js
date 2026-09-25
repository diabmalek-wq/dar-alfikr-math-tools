// ---------------------------------------------------------------------------
// THE 20-WEEK COURSE ARRANGEMENT OF THE BANK
//
// The department syllabus is written for 60 weeks — and actually runs to Week 64
// and 191 sessions, which is why its own title and its own table disagree. This
// script keeps its SEQUENCE and compresses it into the 20 weeks Mr Thiab has:
// 20 weeks x 3 sessions = 60 sessions, one topic per week.
//
// HOW THIS DIFFERS FROM make_gat_week.js. That builder samples every week to the
// ETEC blueprint, so each worksheet is a small slice of the whole paper — right
// for revision alongside another course. This one is TOPIC-ORDERED: Week 1 is
// nothing but primes and divisibility, Week 11 nothing but angles. It teaches
// the syllabus in the syllabus's own order and is the right shape for a taught
// course. The two arrangements use the SAME 374 items and keep separate ledgers,
// so a class can be taught from one and revised from the other.
//
// EVERY ITEM IS ISSUED EXACTLY ONCE across the twenty weeks, and the build fails
// if that is not true — no item is dropped and none appears in two weeks.
//
//     node make_gat_course.js            -> all twenty weeks
//     node make_gat_course.js 3 4        -> just weeks 3 and 4
//     node make_gat_course.js --plan     -> the coverage table, builds nothing
// ---------------------------------------------------------------------------
const fs = require("fs");
const { buildSet } = require("./exam_engine");

const ITEMS = [...require("./sim_items_a.js"), ...require("./sim_items_b.js"),
               ...require("./sim_items_c.js"), ...require("./sim_items_d.js"),
               ...require("./sim_items_e.js"), ...require("./sim_items_f.js"),
               ...require("./sim_items_g.js"), ...require("./sim_items_h.js"),
               ...require("./sim_items_i.js"), ...require("./sim_items_j.js"),
               ...require("./sim_items_k.js"), ...require("./sim_items_l.js")];

const isPct = (it) => /pct|percent|%/i.test(it.sig + " " + it.stem);

// ---------------------------------------------------------------------------
// THE MAP. Four terms of five weeks, in the syllabus's own order: number sense,
// then algebra, then geometry and data, then advanced reasoning. `take` decides
// which bank items belong to the week; `sessions` names the three teaching
// sessions the week's items are split across.
// ---------------------------------------------------------------------------
const COURSE = [
  // ---------------------------------------- TERM 1 · number sense (syllabus units 1-4)
  { n: 1, term: 1, title: "Integers, Primes and Divisibility",
    sub: "Number sets, order of operations, factors, prime numbers and the divisibility rules",
    take: (it) => it.code === "GAT-Q-ARI.1",
    sessions: ["Integers and the order of operations", "Factors, multiples and prime numbers",
               "Divisibility rules and GAT number reasoning"] },
  { n: 2, term: 1, title: "HCF, LCM and Remainders",
    sub: "Highest common factor, lowest common multiple, remainder problems and counting in a range",
    take: (it) => it.code === "GAT-Q-ARI.2",
    sessions: ["Highest common factor", "Lowest common multiple",
               "Remainders and counting problems"] },
  { n: 3, term: 1, title: "Fractions and Decimals",
    sub: "Equivalent fractions, comparing, operating, decimal work, rounding and estimation",
    take: (it) => it.code === "GAT-Q-ARI.3" && !isPct(it),
    sessions: ["Comparing and ordering fractions", "Operating with fractions and decimals",
               "Estimation, rounding and mental strategies"] },
  { n: 4, term: 1, title: "Percentages",
    sub: "Percent of a quantity, increase and decrease, finding the original amount, successive percentages",
    take: (it) => it.code === "GAT-Q-ARI.3" && isPct(it),
    sessions: ["Percent of a quantity", "Increase, decrease and the original amount",
               "Successive percentages and GAT percentage problems"] },
  { n: 5, term: 1, title: "Rates: Speed, Distance and Work",
    sub: "Unit rates, speed-distance-time, work-rate problems and scale",
    take: (it) => it.code === "GAT-Q-LOG.1" || it.code === "GAT-Q-LOG.2",
    sessions: ["Unit rates and proportion", "Speed, distance and time",
               "Work-rate problems and scale"] },

  // ---------------------------------------- TERM 2 · algebra (syllabus units 5-8)
  { n: 6, term: 2, title: "Algebraic Expressions and Variation",
    sub: "Like terms, the distributive property, evaluating expressions, direct and inverse variation",
    take: (it) => it.code === "GAT-Q-ALG.4" || it.code === "GAT-Q-ALG.5",
    sessions: ["Like terms and simplifying", "Evaluating expressions",
               "Direct and inverse variation"] },
  { n: 7, term: 2, title: "Exponents, Roots and Scientific Notation",
    sub: "Laws of exponents, negative and fractional powers, radicals, standard form",
    take: (it) => it.code === "GAT-Q-ARI.4",
    sessions: ["Laws of exponents", "Roots and radicals",
               "Scientific notation and GAT power problems"] },
  { n: 8, term: 2, title: "Linear Equations and Inequalities",
    sub: "One-step to multi-step equations, fractions in equations, inequalities, absolute value",
    take: (it) => it.code === "GAT-Q-ALG.1",
    sessions: ["Multi-step equations", "Equations with fractions and variables on both sides",
               "Inequalities and absolute value"] },
  { n: 9, term: 2, title: "Systems, Coordinates and Slope",
    sub: "Systems of equations, the coordinate plane, slope, rate of change and functions",
    take: (it) => it.code === "GAT-Q-ALG.2" || it.code === "GAT-Q-GEO.6",
    sessions: ["Systems of equations", "The coordinate plane and slope",
               "Functions and graphs"] },
  { n: 10, term: 2, title: "Sequences and Patterns",
    sub: "Arithmetic and geometric sequences, recursive rules, missing terms, algebraic patterns",
    take: (it) => it.code === "GAT-Q-ARI.5",
    sessions: ["Arithmetic sequences", "Geometric and recursive patterns",
               "Finding missing terms · GAT sequence problems"] },

  // ---------------------------------------- TERM 3 · geometry and data (units 9-12)
  { n: 11, term: 3, title: "Angles and Parallel Lines",
    sub: "Points, lines and angles, angle relationships, parallel lines and transversals",
    take: (it) => it.code === "GAT-Q-GEO.1",
    sessions: ["Angle relationships", "Parallel lines and transversals",
               "Angles round a point and in figures"] },
  { n: 12, term: 3, title: "Triangles",
    sub: "Angle relationships, congruence and similarity, Pythagoras and the special right triangles",
    take: (it) => it.code === "GAT-Q-GEO.2",
    sessions: ["Triangle angle relationships", "Similarity and congruence",
               "Pythagoras and special right triangles"] },
  { n: 13, term: 3, title: "Quadrilaterals, Polygons and Area",
    sub: "Perimeter and area of rectangles, parallelograms and trapezoids, composite figures, regular polygons",
    take: (it) => it.code === "GAT-Q-GEO.4",
    sessions: ["Perimeter and area", "Composite and shaded figures",
               "Polygons and dimensional reasoning"] },
  { n: 14, term: 3, title: "Circles and Solids",
    sub: "Circumference, sector area, circles inside figures, volume and surface area",
    take: (it) => it.code === "GAT-Q-GEO.3" || it.code === "GAT-Q-GEO.5",
    sessions: ["Circumference and sectors", "Circles combined with other figures",
               "Volume, surface area and unit conversion"] },
  { n: 15, term: 3, title: "Reading Charts and Tables",
    sub: "Tables, bar graphs, line graphs, pie charts, histograms and pictograms",
    take: (it) => it.code === "GAT-Q-DAT.1",
    sessions: ["Tables and bar graphs", "Line graphs and pie charts",
               "Histograms, pictograms and GAT data interpretation"] },

  // ---------------------------------------- TERM 4 · advanced reasoning (units 13-16)
  { n: 16, term: 4, title: "Averages, Spread and Data Measures",
    sub: "Mean, median, mode, range, weighted averages and data comparison",
    take: (it) => it.code === "GAT-Q-DAT.5" || it.code === "GAT-Q-DAT.2",
    sessions: ["Mean and the missing value", "Median, mode and range",
               "Weighted averages and data comparison"] },
  { n: 17, term: 4, title: "Probability and Counting",
    sub: "Basic and complementary probability, counting principles, permutations and combinations",
    take: (it) => it.code === "GAT-Q-DAT.3" || it.code === "GAT-Q-DAT.4",
    sessions: ["Basic and complementary probability", "Counting principles",
               "Permutations, combinations and GAT probability problems"] },
  { n: 18, term: 4, title: "Factoring, Identities and Quadratics",
    sub: "Polynomials, common factors, algebraic identities, quadratic expressions and equations",
    take: (it) => it.code === "GAT-Q-ALG.3",
    sessions: ["Common factors and polynomials", "Algebraic identities",
               "Quadratic expressions and equations"] },
  { n: 19, term: 4, title: "Quantitative Word Problems",
    sub: "Ages, ratio shares, arrangement puzzles, working backwards and strategic reasoning",
    take: (it) => it.code === "GAT-Q-LOG.3",
    sessions: ["Ages and ratio shares", "Arrangement and cycle puzzles",
               "Working backwards · logical quantitative reasoning"] },
  { n: 20, term: 4, title: "Money Problems and GAT Mastery",
    sub: "Profit and loss, discounts and VAT, tariffs, currency, and mixed GAT problem solving",
    take: (it) => it.code === "GAT-Q-LOG.4",
    sessions: ["Profit, loss and discount", "Tariffs, billing and currency",
               "Mixed GAT money problems · speed and accuracy"] },
];

const TERM_NAME = {
  1: "Term 1 — Number Sense and Arithmetic",
  2: "Term 2 — Algebra and Quantitative Relationships",
  3: "Term 3 — Geometry and Data Analysis",
  4: "Term 4 — Advanced Quantitative Reasoning and GAT Mastery",
};

// ---- assign every item to exactly one week -------------------------------
const weeks = COURSE.map((w) => ({ ...w, items: ITEMS.filter(w.take) }));
{
  const seen = new Map();
  for (const w of weeks)
    for (const it of w.items) {
      if (seen.has(it.sig))
        throw new Error(`"${it.sig}" falls in week ${seen.get(it.sig)} and week ${w.n}`);
      seen.set(it.sig, w.n);
    }
  const orphans = ITEMS.filter((it) => !seen.has(it.sig));
  if (orphans.length)
    throw new Error(`${orphans.length} item(s) belong to no week — first: ` +
                    `${orphans[0].sig} (${orphans[0].code})`);
}

// ---- order inside a week: stars spread, sessions marked ------------------
/** Deal the week's items so the level-3 ones fall at roughly every fourth slot
 *  rather than at the front, then split into three sessions and title each. */
function arrange(w) {
  const easy = w.items.filter((x) => x.lvl !== 3);
  const hard = w.items.filter((x) => x.lvl === 3);
  const gap = Math.max(2, Math.round(w.items.length / Math.max(1, hard.length)));
  const order = [];
  for (let i = 0; order.length < w.items.length; i++)
    order.push((i % gap === gap - 1 && hard.length) ? hard.shift()
                                                    : (easy.shift() || hard.shift()));
  const per = Math.ceil(order.length / 3);
  return order.map((it, i) => {
    const s = Math.floor(i / per);
    const first = i % per === 0 && s < 3;
    // clone: the item objects are shared with the other builders
    return first
      ? { ...it, sec: { title: `SESSION ${s + 1} — ${w.sessions[s]}`,
                        note: `${Math.min(per, order.length - i)} questions` } }
      : { ...it };
  });
}

// ---- build ---------------------------------------------------------------
function cfg(w, items) {
  const stars = items.filter((x) => x.lvl === 3).length;
  const mins = Math.round(items.length * 1.25 / 5) * 5;
  return {
    mathIndex: "math_sim_doc/_index.json",
    figIndex: "figs_sim/_index.json",
    examName: "GAT (Qudurat) quantitative course",
    // a topic week is deliberately one strand, so the 'target' column says so
    targets: Object.fromEntries([...new Set(items.map((i) => i.code.split(".")[0]))]
                                .map((k) => [k, "topic week"])),
    dense: true, itemGap: 55,
    marking: "One point each, no penalty for a wrong answer",
    budgetNote:
      `Every question in this set is on the week's topic — this is a taught ` +
      `week, not a mixed revision paper. ${items.length} items, ${stars} of them ` +
      `level 3, split across the week's three sessions.`,
    compareNote:
      "COMPARISON QUESTIONS.  Some questions give you two quantities, A and B, and ask which is greater. Answer (A) if A is greater, (B) if B is greater, (C) if the two are exactly equal, and (D) if what you are given is not enough to decide. Both (C) and (D) are real answers on this paper.",
    conditions:
      `No calculator. Work through the sessions in order — each one builds on the ` +
      `one before it. Answer every question: nothing is deducted for a wrong ` +
      `answer, so a guess is always better than a blank.`,
    sourceNote:
      "These questions are ORIGINAL, drawn from the department's 374-item GAT " +
      "bank. Every answer was re-derived independently in Python before release.",
    weekLine: `${TERM_NAME[w.term]} · Week ${w.n} of 20`,
    headerLine: `GAT (Qudurat) · Week ${w.n} · ${w.title} · ${items.length} items · 3 sessions`,
    paperTitle: `Week ${w.n} — ${w.title}`,
    paperSub: w.sub,
    keyTitle: `Week ${w.n} — ${w.title} · Answer Key and Error Analysis`,
    keySub: "For Mr Malek Thiab. Each item names the trick it is built on and what each wrong option means.",
    outPaper: `GAT_Course_W${String(w.n).padStart(2, "0")}_Paper.docx`,
    outKey: `GAT_Course_W${String(w.n).padStart(2, "0")}_Key.docx`,
    timing: `${mins} minutes across 3 sessions`,
    followUp: [
      ["Session 1", "If a student loses more than half of session 1, do not move on — the later sessions assume it."],
      ["Level 3 items", "Marked ★. They are the multi-step items; a student who is secure on the rest but loses these needs pace work, not reteaching."],
      ["Whole class", "Any question where more than half the class chose the SAME wrong option is a teaching point, not a marking point — the key names what that option means."],
      ["After the week", "Record the topic score. The twenty weekly scores are the course profile the mocks are read against."],
    ],
    items,
  };
}

// ---- run -----------------------------------------------------------------
(async () => {
  const args = process.argv.slice(2);
  const planOnly = args.includes("--plan");
  const only = args.filter((a) => /^\d+$/.test(a)).map(Number);

  if (planOnly || !only.length) {
    console.log("\n20-WEEK COURSE ARRANGEMENT · 374 items, each issued once\n");
    let term = 0;
    for (const w of weeks) {
      if (w.term !== term) { term = w.term; console.log(`  ${TERM_NAME[term]}`); }
      const stars = w.items.filter((x) => x.lvl === 3).length;
      console.log(`    W${String(w.n).padStart(2, "0")}  ${w.title.padEnd(42)}` +
                  `${String(w.items.length).padStart(3)} items  ${String(stars).padStart(2)} ★`);
    }
    console.log(`\n    total ${weeks.reduce((s, w) => s + w.items.length, 0)} items · ` +
                `${weeks.reduce((s, w) => s + w.items.filter((x) => x.lvl === 3).length, 0)} level-3\n`);
    if (planOnly) return;
  }

  const ledger = {};
  for (const w of weeks) {
    const items = arrange(w);
    ledger[`Week ${w.n}`] = { title: w.title, term: w.term,
                              sigs: items.map((i) => i.sig) };
    if (only.length && !only.includes(w.n)) continue;
    await buildSet(cfg(w, items));
    console.log(`  Week ${w.n}: ${items.length} items, ` +
                `${items.filter((x) => x.lvl === 3).length} level-3`);
  }
  fs.writeFileSync("gat_course_ledger.json", JSON.stringify(ledger, null, 1));
  console.log("\n  ledger -> gat_course_ledger.json");
})();

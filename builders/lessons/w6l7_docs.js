// Grade 11 · Topic 6 · Lesson 6-7 — Geometric Sequences and Series
// FIKR lesson plan, Lesson plan 2026/27, differentiation activity, PBL task.
// Classwork is NOT requested this round (matching the pattern for
// L6-1/L6-3/L6-4/L6-5/L6-6) — a minimal stub is supplied only so docs_engine's
// buildAll() does not throw; the resulting file is deleted after build and
// never delivered.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread as lessons_w6l7.js — see
// the standing alignment rule noted there (identify/write/derive/sum
// geometric sequences and series, and the community waqf donation-drive
// production task).
const { buildAll } = require("../../engines/docs_engine");
const fs = require("fs");

const MATHDOC = "math_w6l7_doc/_index.json";
const GRAPH = "graphs_w6l7/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I identified $a_1$, $r$ and $n$ correctly before I substituted into the formula, and challenge any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to the series formula, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "This lesson closes Topic 6. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR11 · T6 L6-7 · Geometric Sequences and Series
// =====================================================================
const GR11_L67 = {
  slug: "Gr11_T6_L6-7_Geometric_Sequences_and_Series",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Geometric Sequences and Series",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-7",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 9 · Semester 1, 2026–27",
  weekNum: "9",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-7 — Geometric Sequences and Series",
  codes: ["HSA.SSE.B.4", "HSF.IF.A.3", "HSF.BF.A.2", "HSF.LE.A.2"],
  mps: ["MP.4", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Identify geometric sequences.",
    "Write recursive and explicit formulas for geometric sequences.",
    "Identify geometric series.",
    "Derive the formula for geometric series.",
    "Use the formula for geometric series to find sums.",
  ],
  essentialQuestion: "How can we use geometric sequences to model real-world situations?",
  vocabList: "common ratio ; geometric sequence ; geometric series ; sequence of partial sums ; sigma notation ; index ; starting index ; ending index ; summand",

  plan: {
    outcome: [
      "Students will identify a geometric sequence by testing for a constant ratio, and write it both recursively and explicitly.",
      "Students will identify a geometric series and derive its sum formula by subtracting $rS_n$ from $S_n$.",
      "Students will apply $S_n=a_1(1-r^{\\,n})⁄(1-r)$ to find an exact sum, including in a real-world modeling context written in sigma notation.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “The sequence that lives on a curve” — a geometric sequence as an exponential function sampled at whole numbers. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one exponential-function recall, one growth/decay-factor recall from Lesson 6-1.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz ($\\le 4$ minutes): state the common ratio of $3,6,12,24,\\ldots$; evaluate $f(x)=5(2)^{x}$ at $x=3$; solve $3^{x}=20$ using a logarithm to 2 decimal places; add $2+6+18+54$; classify $5,8,11,14,\\ldots$ as arithmetic, geometric, or neither.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: $r=2$; $f(3)=40$; $x\\approx 2.73$; sum $=80$; arithmetic (common difference 3).",
    ],
    diagGap: [
      "Expected gap 1 — a student who cannot evaluate an exponential function or recall a growth/decay factor from Lesson 6-1; the sequence-as-exponential framing will not land.",
      "Expected gap 2 — a student who cannot solve for an exponent with a logarithm from Lesson 6-6; later term-number problems will stall.",
      "Expected gap 3 — Q5, where students see repeated-looking numbers and guess geometric without actually checking the ratio.",
      "Routing: 0–2 correct → re-teach ratios and factors.  3–4 → straight to the series formula.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): a geometric sequence multiplies by the same ratio $r$ every step — a discrete exponential function, sampled only at whole-number inputs.",
      "Whole class, IF.A.3/BF.A.2 (Objectives 1 & 2): test $3,6,12,24,48,\\ldots$ for a constant ratio ($r=2$), then write it recursively ($a_n=2a_{n-1}$, $a_1=3$) and explicitly ($a_n=3(2)^{n-1}$), checking $a_5=48$ against the sequence.",
      "Whole class, SSE.B.4 (Objectives 3 & 4): define a geometric series as the sum of the sequence's terms, then DERIVE the sum formula live — multiply $S_n$ by $r$, subtract to cancel the middle terms, factor, and arrive at $S_n=a_1(1-r^{\\,n})⁄(1-r)$. Verify on $S_4=3+6+12+24=45$.",
      "Whole class, LE.A.2 (Objective 5): introduce sigma notation on a community waqf's donation drive — $a_1=10\\,000$, $r=1.2$ — written as $Σ_{k=1}^{5}10\\,000(1.2)^{k-1}$, then evaluated with the formula to $S_5=74\\,416$ SAR.",
      "Narration focus — after deriving the formula, verify it on a SMALL case the class can add by hand, so students trust it before applying it to a case too large to add directly.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 90 seconds: find $S_6$ for $a_1=5$, $r=3$, using the formula.",
      "Expected: $S_6=1820$. Watch for sign errors when both the numerator and denominator of the formula are negative.",
      "80% correct → release guided practice. Below 80% → one further modelled example, working the derivation again slowly.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) $4,12,36,108,\\ldots$ — write the explicit formula.  (2) $a_1=2$, $r=4$ — find $S_5$ using the formula.",
      "Answers: (1) $r=3$, so $a_n=4(3)^{n-1}$. (2) $S_5=2(1-4^5)⁄(1-4)=682$.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Two sequences identified and written explicitly, two sums found by formula, one sum verified by direct addition. Done when: explicit formulas pass a check at $n=1$, and sums agree with direct addition.",
      "APPLY — Use it in context. A doubling charity-donation total, a classification-and-sum problem, and the total written in sigma notation. Done when: the total carries units, and sigma notation names all three parts.",
      "INVESTIGATE — Find out why. Explaining the $r=1$ edge case, settling a negative-ratio disagreement, and proving the $r=1$ sum shortcut. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A neighbourhood's charitable waqf (endowment) fund runs an annual donation drive. Year 1 raises 10,000 SAR, and community participation grows the drive by 20% every year after that.",
      "(a) Write the explicit formula for the amount raised in year $n$. (b) Write the 5-year total in sigma notation, naming the start index, end index, and summand. (c) Use the geometric series formula to find the exact 5-year total, in SAR. (d) A committee member says “just multiply year 1's amount by 5 — that's the total.” Explain in one sentence why this underestimates the real total.",
      "Answers: (a) $a_n=10\\,000(1.2)^{\\,n-1}$. (b) $Σ_{k=1}^{5}10\\,000(1.2)^{k-1}$ — start index $k=1$, end index $k=5$, summand $10\\,000(1.2)^{k-1}$. (c) $S_5=10\\,000(1-1.2^{5})⁄(1-1.2)=74\\,416$ SAR. (d) multiplying year 1's amount by 5 assumes NO growth at all, so it ignores that every later year raises MORE than year 1 — it badly underestimates the true total (50,000 SAR versus the actual 74,416 SAR).",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the sigma notation written out fully with start index, end index, and summand each named, and the formula shown with numbers substituted BEFORE the final total is computed.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for part (d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. State the common ratio and write the explicit formula for $5,15,45,135,\\ldots$. 2. Find $S_4$ for $a_1=6$, $r=2$, using the formula. 3. In ONE sentence, explain why checking a RATIO (not a difference) is what identifies a geometric sequence.",
      "Answers: 1. $r=3$, $a_n=5(3)^{n-1}$. 2. $S_4=6(1-2^4)⁄(1-2)=90$. 3. because a difference test identifies an ARITHMETIC sequence instead — applying it to a geometric sequence gives a false negative.",
      "Done when: question 2 shows the formula with numbers substituted before the final answer, and question 3 gives a definition-based reason, not an example alone.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their waqf-fund reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the explicit formula, the 5-year total in full sigma notation, the exact sum from the formula, and ONE worked non-example — multiplying year 1's amount by 5 instead of using the series formula — with a sentence on how a reader would spot the underestimate.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which part is still harder for you — deriving the series formula, or setting up sigma notation correctly from a word problem?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Two sequences identified and written explicitly, two sums found by formula; a partner is allowed. Done when: explicit formulas pass a check at $n=1$ and sums agree with direct addition.",
      "APPLY — Use it in context. The doubling-donation total, a classification-and-sum problem, and sigma notation for the total. Done when: units are stated and sigma notation names all three parts.",
      "INVESTIGATE — Find out why. The $r=1$ edge case, the negative-ratio disagreement, and the $r=1$ sum proof. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a neighbourhood waqf (charitable endowment) fund's donation drive, modeled as a geometric series and solved for an exact 5-year total.",
      "In-class Apply-route item: a charity's donation drive doubling every year, solved for its 4-year total.",
      "Discussion prompt: why a growing total over several years is never just \"this year's amount times the number of years.\"",
    ],
    exams: [
      "GAT (Qudurat) — recognizing a geometric sequence and its common ratio quickly. Practice tip: divide the second term by the first, then check the quotient is the same for every consecutive pair.",
      "SAAT (Tahsili) — applying the geometric series formula directly, a core Grade 11 skill. Practice tip: identify $a_1$, $r$ and $n$ first, then substitute — never add a long sum term by term.",
      "SAT — Advanced Math, a geometric series in a modeling context, a recurring item type. Practice tip: write the sigma notation or the formula before touching a calculator.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 9", section: "Grade 11-B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra / spreadsheet · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Growing a Community Waqf Fund” project task · squared paper",
    competencies: ["Identifying a geometric sequence and writing it recursively and explicitly.", "Deriving and applying the geometric series sum formula, including in sigma notation."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "A spreadsheet or GeoGebra table building a running total to confirm the series formula."],
    reallife: ["A neighbourhood waqf (charitable endowment) fund's growing annual donation drive.", "A charity's donation drive doubling every year, and its cumulative total."],
    values: ["Rigor — deriving a formula rather than accepting it, and verifying it on a case you can check by hand.", "Precision — naming every part of sigma notation before using it."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a running total is not the same as the last term alone."],
    hard: ["Identifying, and writing recursive and explicit formulas for, a geometric sequence.", "Deriving and applying the geometric series formula, including reading and writing sigma notation."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on common ratio, exponential evaluation, solving with a logarithm, direct addition, and sequence classification. Results read as a gap map; students routed to the re-teach table, straight to the series formula, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on evaluating exponentials and growth/decay factors for flagged students. Whole class: identifying and writing a geometric sequence; deriving the series formula; sigma notation and a real total. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The waqf fund's explicit formula, the 5-year total in sigma notation, and the exact sum from the formula. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — a sequence identified and written explicitly, a sum found by formula, and a one-sentence justification. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: [
      "Diagnostic quiz — gap map, not a grade.",
      "Quick check for understanding on whiteboards (80% threshold).",
      "“Give it a go” questions — self-marked, teacher circulates.",
      "Project task sheet against its “Done when…” criteria.",
      "“Time to Check” — Mastery Gate, scored live. PASS → Enrichment & Challenge. NOT YET → Targeted Learning Clinic next lesson.",
      "Final product graded on reasoning and clarity, not correctness alone.",
    ],
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which part is still harder for you — deriving the series formula, or setting up sigma notation correctly from a word problem?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. This closes Topic 6 — the Topic Recap and Unit Assessment follow next session, not a new flipped video.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION 1", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "gs_ws1", t: "Write the explicit formula." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Identify, write, and sum", done: "your explicit formulas both pass a quick check at $n=1$, and your sums agree when checked by direct addition.",
        intro: "For each sequence, state $r$ and write the explicit formula; then find the sums using the formula.",
        grid: [["1.", "gs_ws1"], ["2.", "gs_ws2"], ["3.", "gs_ws3"], ["4.", "gs_ws4"], ["5.", "gs_g1"], ["6.", "gs_qc"]],
        tasks: ["7.  Verify one of your sums by adding the terms directly."],
        lines: 2 },
      { note: "A context, and sigma notation", done: "your total carries units (SAR), and your sigma notation names all three parts — start, end, summand.",
        graph: "g_geo_series", graphW: 380,
        tasks: [
          "1.  A charity's donation drive DOUBLES every year, starting at 500 SAR. Find the TOTAL raised over 4 years.",
          "2.  Determine whether $7,14,28,56,\\ldots$ is geometric; if so, state $r$ and find $S_5$.",
          "3.  Write the 4-year charity total from question 1 in sigma notation, naming the start index, end index, and summand.",
          "4.  Using the graph shown, confirm the waqf fund's 5-year total to the nearest SAR.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          "1.  Explain what happens to $S_n-rS_n=a_1-a_1r^n$ when $r=1$, and why the formula needs $r\\ne 1$ as a result. What formula would you use instead?",
          "2.  Two students disagree about whether $4,-8,16,-32,\\ldots$ is geometric. Settle the disagreement and state $r$.",
          "3.  Prove that the sum of the first $n$ terms of any geometric sequence with $r=1$ is simply $a_1n$, arguing directly from what the series means.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Growing a Community Waqf Fund", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A donation drive doesn't just repeat the same amount — it GROWS every year. How much does that growth actually add up to over five years, and can a quick mental guess be trusted?",
    situation: [
      "A neighbourhood's charitable waqf (endowment) fund runs an annual donation drive. Year 1 raises 10,000 SAR, and community participation grows the drive by 20% every year after that.",
      "A group of Grade 11 students is asked to find the exact 5-year total, and to check a committee member's quick estimate.",
    ],
    eq: "gs_ctx",
    steps: [
      ["1", "WRITE THE FORMULA  (4 min)", "Write the explicit formula for the amount raised in year $n$."],
      ["2", "SET UP SIGMA NOTATION  (4 min)", "Write the 5-year total in sigma notation, naming the start index, end index, and summand."],
      ["3", "APPLY THE FORMULA  (5 min)", "Use the geometric series formula to find the exact 5-year total, in SAR."],
      ["4", "FIND THE TRAP  (4 min)", "A committee member says “just multiply year 1's amount by 5.” Explain in one sentence why this underestimates the total."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: how far off the committee member's estimate really is."],
    ],
    working: [["Step 1 — the explicit formula:", 2], ["Step 2 — sigma notation, in full:", 3],
              ["Step 3 — the 5-year total, from the formula:", 3], ["Step 4 — the committee member's error:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the donation drive", "Calculator — applies the series formula", "Checker — verifies by adding a few terms directly", "Presenter — says the sentence"],
    doneWhen: ["The explicit formula is written and checked at $n=1$.", "Sigma notation names the start index, end index, and summand.", "The 5-year total is exact, shown with the formula before the final number.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR11_L67);
  const cwFile = require("path").join(__dirname, "../../engines", `Classwork_${GR11_L67.slug}.docx`);
  if (fs.existsSync(cwFile)) fs.unlinkSync(cwFile);
})();

module.exports = { GR11_L67 };

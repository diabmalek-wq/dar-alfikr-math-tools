// Grade 11 · Topic 6 · Lesson 6-7 — Geometric Sequences and Series
//
// Follows L6-6 (Exponential and Logarithmic Equations and Inequalities)
// directly, and closes Topic 6 (Exponential and Logarithmic Functions) — the
// curriculum map's next rows are the Unit Recap and Unit Assessment.
// Objectives, essential question, vocabulary, standards and MPs are quoted
// VERBATIM from "Curriculum map A2 OBLAS.docx", Unit 6, Lesson 7.
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6l7_docs.js for the matching plan/activity/PBL.
// The community waqf (charitable endowment) donation-drive context here is
// the SAME context, same numbers, as the PBL task and the docs' production/
// evidence sections.
//
// HOUSE RULE (confirmed by Mr Thiab 26 Sep 2026): every FIKR deck ships
// ANIMATED — run engines/animate_deck.py on the built .pptx before delivery.
//
// Every piece of mathematics inside a sentence (titles, panels, bars, notes)
// is written as $...$ per the inline-maths house rule — see engines/inline_math.js.
// Only self-contained display equations use a LaTeX image key (eq:).
const { build } = require("../../engines/lesson_engine");

const MATH = "math_w6l7/_index.json";
const GRAPH = "graphs_w6l7/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 11 · TOPIC 6 · LESSON 6-7 — Geometric Sequences and Series
// =====================================================================
const GR11_L67 = {
  out: "Gr11_T6_L6-7_Geometric_Sequences_and_Series.pptx",
  deckTitle: "Geometric Sequences and Series — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  weekNum: "9",
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-7",
  lessonTitle: "Geometric Sequences and Series",
  titleSize: 32,
  subtitle: "A geometric sequence is an exponential function that only shows up on whole numbers",
  titleEq: "gs_title_w", titleEqK: 1.9,
  titleEqAlt: "S sub n equals a sub 1 times the quantity 1 minus r to the n, all over 1 minus r",
  grade: "Grade 11", week: "Week 9 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-7",
  lessonRef: "Lesson 6-7 — Geometric Sequences and Series",
  nextLesson: "Topic 6 Recap & Unit Assessment — then Topic 7 begins",

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

  vocabulary: [
    { term: "Common ratio", def: "The fixed number $r$ you multiply by to get from one term of a geometric sequence to the next." },
    { term: "Geometric sequence", def: "A sequence with a constant ratio $r$ between consecutive terms — the discrete cousin of an exponential function." },
    { term: "Geometric series", def: "The sum of the terms of a geometric sequence, written $a_1+a_1r+a_1r^{2}+\\ldots$." },
    { term: "Sequence of partial sums", def: "The list $S_1,S_2,S_3,\\ldots$ where each $S_n$ is the running total of the first $n$ terms — a series is what this sequence is building toward." },
    { term: "Sigma notation", def: "A compact way to write a sum, $Σ_{k=1}^{n}a_k$, naming every term to add without writing them all out." },
    { term: "Index", def: "The counting variable inside sigma notation — usually $k$ or $i$ — that steps through each term of the sum." },
    { term: "Starting index", def: "The value the index begins at, written below the $Σ$ symbol." },
    { term: "Ending index", def: "The value the index stops at, written above the $Σ$ symbol." },
    { term: "Summand", def: "The expression being added for each value of the index — the formula written just after the $Σ$ symbol." },
  ],
  vocabSub: "All nine terms the curriculum map lists for this lesson",

  prior: [
    { h: "Exponential functions (Lesson 6-1)", eq: "gs_prior_exp", d: "$y=a\\cdot b^{x}$ is continuous; a geometric sequence $a_n=a_1r^{\\,n-1}$ is its discrete twin — same multiplicative step, now counted in whole terms." },
    { h: "Growth and decay factors (Lesson 6-1)", eq: "gs_prior_factor", d: "A common ratio $r>1$ means growing, $0<r<1$ means shrinking — exactly the base of an exponential function, wearing a new name." },
    { h: "Solving for an exponent with a logarithm (Lesson 6-6)", eq: "gs_prior_logsolve", d: "Finding which term number reaches a target value uses exactly yesterday's method — set the explicit formula equal to the target and solve." },
  ],
  priorSub: "Three things you already know — today they build a new formula",
  carryOver: "A geometric sequence multiplies by the same ratio $r$ every step — a discrete exponential function. A geometric series is just the running total of those terms, and because each new term is the last one scaled by $r$, that running total collapses into ONE closed-form formula.",
  carryOverEq: "gs_def",

  diagnose: {
    title: "Warm-Up: Ratios, Factors, and Sums",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "gs_d1", t: "State the common ratio." },
      { eq: "gs_d2", t: "Evaluate the exponential function." },
      { eq: "gs_d3", t: "Solve for $x$ using a logarithm, to 2 decimal places." },
      { eq: "gs_d4", t: "Add these four numbers." },
      { eq: "gs_d5", t: "Classify the sequence shown." },
    ],
    routing: "0–2 correct → re-teach ratios and factors with me.      3–4 correct → straight to the series formula.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Identify, Then Write Two Formulas",
      sub: "Objectives 1 & 2 — spot a geometric sequence, then write it recursively and explicitly",
      graph: "g_geo_seq", graphW: 6.3, graphY: 2.5,
      graphAlt: "The points 3, 6, 12, 24, 48 at term numbers 1 through 5, lying exactly on the dashed curve y equals 3 times 2 to the power x minus 1",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "Check the RATIO of consecutive terms, not the difference — constant ratio means geometric.",
          "$6÷3=12÷6=24÷12=2$ — the common ratio is $r=2$.",
          "Recursive form: $a_n=2\\,a_{n-1}$, $a_1=3$ — each term from the one before it.",
          "Explicit form: $a_n=3(2)^{\\,n-1}$ — any term directly, no earlier terms needed.",
          "Check: $a_5=3(2)^{4}=48$ — matches the fifth point on the graph.",
        ],
      },
      panelX: 7.0, panelW: 5.9, panelH: 4.0,
      bar: ["A GEOMETRIC SEQUENCE IS AN EXPONENTIAL FUNCTION, SAMPLED AT WHOLE NUMBERS", "the dashed curve is $y=3(2)^{x-1}$; every term of the sequence is a point sitting exactly on it."],
      barY: 6.32,
      notes: "$3,6,12,24,48$: ratio test $6/3=12/6=24/12=2$, so $r=2$. Recursive: $a_n=2a_{n-1}$, $a_1=3$. Explicit: $a_n=3(2)^{n-1}$; check $a_5=3(16)=48$. Misconception to address aloud: students check the DIFFERENCE between terms (as with arithmetic sequences) instead of the ratio — press them to divide, not subtract, to test for geometric.",
    },
    {
      title: "Deriving the Geometric Series Formula",
      sub: "Objectives 3 & 4 — define a geometric series, then derive its sum from scratch",
      panel: {
        h: "PROVE IT FROM WHAT YOU ALREADY KNOW",
        items: [
          "A geometric SERIES is the sum of the sequence's terms: $S_n=a_1+a_1r+a_1r^{2}+\\ldots+a_1r^{\\,n-1}$.",
          "Multiply the whole sum by $r$: $rS_n=a_1r+a_1r^{2}+\\ldots+a_1r^{\\,n}$.",
          "Subtract — almost everything cancels: $S_n-rS_n=a_1-a_1r^{\\,n}$.",
          "Factor and solve: $S_n=a_1(1-r^{\\,n})⁄(1-r)$, valid whenever $r\\ne 1$.",
          "Verify on the sequence above: $S_4=3(1-2^{4})⁄(1-2)=3(15)=45$ — matches $3+6+12+24$ directly.",
        ],
      },
      panelX: 0.55, panelY: 2.42, panelW: 11.9, panelH: 4.0,
      bar: ["SUBTRACTING $rS_n$ FROM $S_n$ IS THE WHOLE TRICK", "every middle term appears in both sums and cancels, leaving only the first term of $S_n$ and the last (shifted) term of $rS_n$."],
      barY: 6.32,
      notes: "Derivation, say it aloud: $S_n=a_1+a_1r+\\ldots+a_1r^{n-1}$; $rS_n=a_1r+a_1r^2+\\ldots+a_1r^{n}$; subtracting cancels every term except the first of $S_n$ and the last of $rS_n$: $S_n-rS_n=a_1-a_1r^n$; factor both sides: $S_n(1-r)=a_1(1-r^n)$; divide: $S_n=a_1(1-r^n)⁄(1-r)$. Verify: $S_4=3(1-16)⁄(1-2)=3(-15)⁄(-1)=45=3+6+12+24$. Misconception to address aloud: students try to just ADD terms one by one for large $n$ instead of trusting the derived formula — ask them to verify the formula on a small case they CAN add by hand, exactly as done here, so they trust it for large $n$.",
    },
    {
      title: "Sigma Notation and a Real Total",
      sub: "Objective 5 — use the formula to find a sum, written formally in sigma notation",
      graph: "g_geo_series", graphW: 6.1, graphY: 2.5,
      graphAlt: "A bar chart of five yearly donations, 10000, 12000, 14400, 17280 and 20736 SAR, each bar labelled with that year's amount and the running total, ending at 74416 SAR",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "A community waqf's donation drive raises 10,000 SAR in year 1, growing 20% a year: $a_1=10\\,000$, $r=1.2$.",
          "In sigma notation, the 5-year total is $Σ_{k=1}^{5}10\\,000(1.2)^{k-1}$ — start index $k=1$, end index $k=5$, summand $10\\,000(1.2)^{k-1}$.",
          "Apply the formula: $S_5=10\\,000(1-1.2^{5})⁄(1-1.2)$.",
          "$S_5=74\\,416$ SAR — matches the last bar's running total on the graph.",
        ],
      },
      panelX: 7.2, panelW: 5.7, panelH: 4.0,
      bar: ["SIGMA NOTATION NAMES EVERY PIECE OF A SUM", "the index starts and ends where the $Σ$ symbol says, and the summand is the formula for whichever term the index currently names."],
      barY: 6.32,
      notes: "$Σ_{k=1}^{5}10\\,000(1.2)^{k-1}$: start index 1, end index 5, summand $10\\,000(1.2)^{k-1}$. Formula: $S_5=10\\,000(1-1.2^5)⁄(1-1.2)=10\\,000(1-2.48832)⁄(-0.2)=74\\,416$. Misconception to address aloud: students think sigma notation is a NEW kind of maths rather than shorthand for the sum they already know how to compute — write the expanded sum next to the sigma form so they see the two are identical.",
    },
  ],

  quickCheck: {
    lead: "Find the sum, using the formula:", leadW: 5.4,
    eq: "gs_qc", k: 1.9,
    think: "Identify $a_1$ and $r$ first, then substitute directly into the formula — no need to add term by term.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, working the derivation again slowly.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "gs_g1", t: "Write the explicit formula for this sequence.", hint: "Find $r$ by dividing consecutive terms, then use $a_n=a_1r^{n-1}$." },
      { eq: "gs_g2", t: "Find the sum using the formula.", hint: "Substitute $a_1$, $r$ and $n$ directly into $S_n=a_1(1-r^n)/(1-r)$." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["For each sequence, state $r$ and write the explicit formula: (a) $2,\\ 6,\\ 18,\\ 54,\\ldots$   (b) $100,\\ 50,\\ 25,\\ 12.5,\\ldots$", "Find $S_5$ for $a_1=4,\\ r=3$.", "Find $S_6$ for $a_1=1,\\ r=2$.", "Verify one of your sums by adding the terms directly."],
        help: "You may use: the derivation on the board, and a partner.",
        done: "your explicit formulas both pass a quick check at $n=1$, and your sums agree when checked by direct addition.", eq: "gs_ws1" },
      { items: ["A charity's donation drive DOUBLES every year, starting at 500 SAR. Find the TOTAL raised over 4 years.", "Determine whether $7,\\ 14,\\ 28,\\ 56,\\ldots$ is geometric; if so, state $r$ and find $S_5$.", "Write the 4-year charity total from question 1 in sigma notation, naming the start index, end index, and summand."],
        help: "You may use: the worked waqf example, and a calculator.",
        done: "your total carries units (SAR), and your sigma notation names all three parts — start, end, summand.", eq: "gs_ws5" },
      { items: ["Explain what happens to the derivation $S_n-rS_n=a_1-a_1r^n$ when $r=1$, and why the formula needs $r\\ne 1$ as a result. What formula would you use instead?", "Two students disagree about whether $4,\\ -8,\\ 16,\\ -32,\\ldots$ is geometric. Settle the disagreement and state $r$.", "Prove that the sum of the first $n$ terms of ANY geometric sequence with $r=1$ is simply $a_1n$, arguing directly from what the series means."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: null },
    ],
  },

  production: {
    title: "Growing a Community Waqf Fund",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A neighbourhood's charitable waqf (endowment) fund runs an annual donation drive. Year 1 raises 10,000 SAR, and community participation grows the drive by 20% every year after that.",
    eq: "gs_ctx_w", eqK: 1.2,
    tasks: [
      "(a)  Write the explicit formula for the amount raised in year $n$.",
      "(b)  Write the 5-year total in sigma notation, naming the start index, end index, and summand.",
      "(c)  Use the geometric series formula to find the exact 5-year total, in SAR.",
      "(d)  A committee member says “just multiply year 1's amount by 5 — that's the total.” Explain in one sentence why this underestimates the real total.",
    ],
    note: "The sigma notation written out fully in part (b), and the formula shown with numbers substituted BEFORE the final total is computed.",
    aiPrompt: "“Check whether I identified $a_1$, $r$ and $n$ correctly before I substituted into the formula, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Build the sequence as points, and watch the running total climb",
    graph: "g_geo_series",
    graphAlt: "The waqf donation bar chart, each bar labelled with that year's donation and the running total, ending at 74416 SAR after 5 years",
    explore: "In a spreadsheet or at geogebra.org/graphing, list $n=1$ to $5$ and compute $a_n=10\\,000(1.2)^{\\,n-1}$ for each. Add a running-total column and confirm it matches $S_5=74\\,416$ from the formula. Then change the growth rate to $10\\%$ and see how much the 5-year total drops.",
  },

  gate: {
    items: [
      { t: "State the common ratio and write the explicit formula.", eq: "gs_gate1" },
      { t: "Find the sum using the formula.", eq: "gs_gate2" },
      { t: "In ONE sentence, explain why checking a RATIO (not a difference) is what identifies a geometric sequence.", eq: null },
    ],
    footer: "Exact answers for Q1 and Q2, with the formula shown before the final number, and Q3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (deriving the sum formula for a series that starts at a term other than $a_1$).      NOT YET → Targeted Learning Clinic on the ratio test and the series formula, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the waqf fund's explicit formula, the 5-year total in sigma notation, and the exact sum from the formula." },
      { h: "Expose the trap", d: "Add one worked NON-example — multiplying year 1's donation by 5 instead of using the series formula — and a sentence on how a reader would spot the underestimate." },
      { h: "Say why it matters", d: "One caption — why a fund's TOTAL over several years is not just \"this year's amount times the number of years\" — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which part is still harder for you — deriving the series formula, or setting up sigma notation correctly from a word problem?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Recognizing a geometric sequence and finding its common ratio quickly.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Divide the second term by the first — if every consecutive pair gives the same quotient, it's geometric.",
      question: "What is the common ratio of $2,\\ 6,\\ 18,\\ 54,\\ldots$?",
      steps: ["Divide consecutive terms: $6÷2=3$.", "Check again: $18÷6=3$ — confirmed constant.", "Answer: $r=3$."] },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Applying the geometric series formula directly, a core Grade 11 skill.", fmt: "Four-option multiple choice, calculator allowed.", tip: "Identify $a_1$, $r$ and $n$ first, then substitute — never add long sums term by term under time pressure.",
      question: "Find $S_5$ for a geometric sequence with $a_1=3$, $r=2$.",
      steps: ["Substitute into $S_n=a_1(1-r^n)/(1-r)$: $S_5=3(1-2^5)/(1-2)$.", "Simplify inside: $3(1-32)/(-1)=3(-31)/(-1)$.", "Answer: $S_5=93$."] },
    { code: "SAT", full: "College Board", skill: "Advanced Math — geometric series in a modeling context, a recurring item type.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Write the sigma notation or the formula BEFORE touching a calculator — it prevents substituting the wrong value for $n$.",
      question: "A geometric series has $a_1=4$ and $r=3$. What is the sum of the first 4 terms?",
      steps: ["Substitute: $S_4=4(1-3^4)/(1-3)$.", "Simplify inside: $4(1-81)/(-2)=4(-80)/(-2)$.", "Answer: $S_4=160$."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "identify $a_1$, $r$ and $n$ first, then substitute directly into $S_n=a_1(1-r^{\\,n})/(1-r)$ — never add a long geometric sum term by term."],

  summary: [
    "Identify a geometric sequence by testing for a CONSTANT RATIO between consecutive terms.",
    "Write a geometric sequence recursively ($a_n=r\\,a_{n-1}$) and explicitly ($a_n=a_1r^{\\,n-1}$).",
    "Identify a geometric series as the sum of a geometric sequence's terms, and read sigma notation naming its index and summand.",
    "Derive the geometric series formula by subtracting $rS_n$ from $S_n$.",
    "Apply $S_n=a_1(1-r^{\\,n})/(1-r)$ to find an exact sum, including in a real-world modeling context.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "This closes Topic 6 — the next session is the Topic Recap and Unit Assessment, not a new flipped video.",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on the ratio test and the series formula.",
  ],

  notes: {
    cover: "Week 9 lesson for Grade 11-B, closing Topic 6 (Exponential and Logarithmic Functions) directly from Lesson 6-6. The Topic Recap and Unit Assessment follow next session, not a new lesson.",
    objectives: "All five objectives are verbatim from the curriculum map. The map lists HSA.SSE.B.4, HSF.IF.A.3, HSF.BF.A.2 and HSF.LE.A.2 for this lesson, and only MP.4 and MP.7 — do not add others. HSA.SSE.B.4 (deriving the series formula) is the spine of instruction slide 2; the other three standards (sequences as functions, recursive/explicit forms, constructing from given information) run across all three slides.",
    vocabulary: "All nine terms are the map's list — the most of any lesson this topic. Group them in three families as you go: RATIO/SEQUENCE words (common ratio, geometric sequence), SERIES words (geometric series, sequence of partial sums), and SIGMA words (sigma notation, index, starting index, ending index, summand).",
    prior: "If a student cannot evaluate an exponential function or recall a growth/decay factor from Lesson 6-1, the sequence-as-exponential framing will not land. Watch for it in the diagnostic, questions 1 and 2.",
    diagnose: "Answers: $r=2$; $f(3)=5(2)^{3}=40$; $x=(\\log 20)/(\\log 3)\\approx 2.73$; $2+6+18+54=80$; arithmetic (common difference 3, not a common ratio). Expected gap: Q5, where students see repeated multiplication-looking numbers and guess geometric without checking.",
    quickCheck: "Answer: $a_1=5,\\ r=3$ gives $S_6=5(1-3^6)/(1-3)=5(1-729)/(-2)=5(-728)/(-2)=1820$. Watch for sign errors when both the numerator and denominator are negative.",
    guided: "Answers — 1: $4,12,36,108,\\ldots$ has $r=3$, so $a_n=4(3)^{n-1}$. 2: $a_1=2,\\ r=4$: $S_5=2(1-4^5)/(1-4)=2(1-1024)/(-3)=2(-1023)/(-3)=682$. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference. Apply-route answers: charity doubling total $S_4=500(1-2^4)/(1-2)=500(15)=7500$ SAR; $7,14,28,56,\\ldots$ is geometric with $r=2$, $S_5=7(1-2^5)/(1-2)=7(31)=217$.",
    production: "Answers — (a) $a_n=10\\,000(1.2)^{\\,n-1}$. (b) $Σ_{k=1}^{5}10\\,000(1.2)^{k-1}$ — start index $k=1$, end index $k=5$, summand $10\\,000(1.2)^{k-1}$. (c) $S_5=10\\,000(1-1.2^{5})⁄(1-1.2)=74\\,416$ SAR. (d) multiplying year 1's amount by 5 assumes NO growth at all — it ignores that every later year raises MORE than year 1, so it badly underestimates the true total (50,000 SAR versus the actual 74,416 SAR).",
    geogebra: "The running-total column is the whole point — watching it accumulate row by row toward 74,416 makes the abstract formula concrete before students trust it for a case too large to add by hand.",
    gate: "Answers: $5,15,45,135,\\ldots$ has $r=3$, so $a_n=5(3)^{n-1}$. $a_1=6,\\ r=2$: $S_4=6(1-2^4)/(1-2)=6(-15)/(-1)=90$. Q3: because only a ratio test survives being applied to EVERY pair of consecutive terms consistently for a geometric sequence — a difference test is what identifies an ARITHMETIC sequence instead, and applying the wrong test gives a false negative. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — treating a growing series as a flat repeated amount is exactly the shortcut a real committee member might take, and it is worth showing the size of the underestimate as a percentage.",
    exams: "Show this before homework so the practice set has an obvious purpose. Walk through at least one worked card aloud before moving on.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L67);
})();

module.exports = { GR11_L67 };

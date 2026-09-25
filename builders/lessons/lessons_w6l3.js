// Grade 11 · Topic 6 · Lesson 6-3 — Logarithms
//
// L6-2 (Exponential Models) is NOT taught per the department's own
// Curriculum Distribution (Topic 6, Weeks 5-8 lists 6-1 -> 6-3 -> 6-4 -> 6-5
// -> 6-6 -> 6-7, skipping 6-2) — confirmed with Mr Thiab 24 Sep 2026. This
// lesson follows L6-1 Key Features of Exponential Functions directly.
//
// Objectives, vocabulary and standards are quoted VERBATIM from the
// curriculum map (Scope and sequence_OA2W_Global.docx, Unit 6, Lesson 3).
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6l3_docs.js for the matching plan/activity/PBL.
const { build } = require("./lesson_engine");

const MATH = "math_w6l3/_index.json";
const GRAPH = "graphs_w6l3/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

const GR11_L63 = {
  out: "Gr11_T6_L6-3_Logarithms.pptx",
  deckTitle: "Logarithms — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-3",
  lessonTitle: "Logarithms",
  titleSize: 34,
  subtitle: "The question exponentials couldn't answer: what power gets me there?",
  titleEq: "l_title_w", titleEqK: 2.6,
  titleEqAlt: "log base b of x equals y if and only if b to the y equals x",
  grade: "Grade 11", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-3",
  lessonRef: "Lesson 6-3 — Logarithms",
  nextLesson: "Topic 6 · Lesson 6-4 — Logarithmic Functions",

  codes: ["HSF.BF.B.4.A", "HSF.BF.B.5", "HSF.LE.A.4"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Understand and evaluate logarithms.",
    "Analyze common logarithms and natural logarithms.",
    "Convert between exponential and logarithmic forms.",
    "Use logarithms to solve problems involving exponential models.",
    "Evaluate logarithms using technology.",
  ],
  essentialQuestion: "What is a logarithm, and how does it let us solve for an exponent we cannot find by inspection?",

  vocabulary: [
    { term: "Logarithm", def: "The exponent to which a base b must be raised to produce x: log_b x = y means b^y = x. A logarithm IS an exponent." },
    { term: "Common logarithm", def: "A logarithm with base 10, written log x (no base shown). log x means log_10 x." },
    { term: "Natural logarithm", def: "A logarithm with base e (≈ 2.71828), written ln x. ln x means log_e x." },
    { term: "Logarithmic function", def: "A function of the form f(x) = log_b x — the inverse of the exponential function f(x) = b^x." },
    { term: "Order of magnitude", def: "The power of 10 closest to a number's size, found by taking its common logarithm and rounding — a quick way to compare sizes that differ by factors of ten." },
  ],
  vocabSub: "All five terms the curriculum map lists for this lesson",

  prior: [
    { h: "Lesson 6-1: exponential functions", eq: "l_exp1", d: "You can graph and evaluate b^x. Today asks the opposite question — given the OUTPUT, find the exponent." },
    { h: "Solving 2^x = 8 by inspection", eq: "l_d4", d: "Worked when the answer was a whole number. Today's tool works even when it isn't." },
    { h: "Inverse functions", eq: null, d: "From Topic 5, Lesson 5-6. A logarithm is nothing new here — it is exactly the inverse of an exponential function." },
  ],
  priorSub: "Three things you already know — today gives the missing operation a name",
  carryOver: "A logarithm is just an exponent wearing a different name. log_b x = y answers the question “b to WHAT power gives x?” — the exact question you could only answer by guessing until now.",
  carryOverEq: "l_def",

  diagnose: {
    title: "Warm-Up: The Question You Can't Yet Answer",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "l_d1", t: "Evaluate directly." },
      { eq: "l_d2", t: "Evaluate directly." },
      { eq: "l_d3", t: "Evaluate the exponential function at 0." },
      { eq: "l_d4", t: "Solve for x by inspection — what power of 2 gives 16?" },
      { eq: "l_d5", t: "No inspection will give an exact whole number here — estimate between which two integers." },
    ],
    routing: "0–2 correct → re-teach exponent basics with me.      3–4 correct → straight to the definition.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Understanding and Evaluating Logarithms",
      sub: "Objectives 1 and 3 — what a logarithm means, and converting between forms",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "log_b x = y is ALWAYS asking: b to what power gives x?",
          "The two forms say the exact same thing — swap between them freely.",
          "log_2 8 = 3, because 2³ = 8 — check the exponential form to verify any logarithm.",
          "log_5 1 = 0 for every base, because any base to the power 0 is 1.",
          "A logarithm is undefined for x ≤ 0 — no real power of a positive base gives zero or a negative number.",
        ],
      },
      panelX: 0.45, panelY: 2.5, panelW: 6.5, panelH: 4.0,
      rowsHead: ["FORM", "EXAMPLE"],
      rowsTop: 2.5, rowH: 0.78, rowsX: 7.3, rowsW: 5.6,
      rows: [
        ["Exponential → log", { eq: "l_ex_conv1", k: 1.8 }],
        ["Log → exponential", { eq: "l_ex_conv2", k: 1.8 }],
        ["Evaluate", { eq: "l_ex_eval1", k: 1.8 }],
        ["Evaluate", { eq: "l_ex_eval2", k: 1.8 }],
      ],
      bar: ["THE CONVERSION RULE", "b^y = x  ⟺  log_b x = y — the base stays the base, the exponent and the answer just swap sides."],
      barY: 6.32,
      notes: "log_2 8 = 3 because 2^3 = 8. log_5 1 = 0 because 5^0 = 1 for every base. 3^4 = 81 -> log_3 81 = 4. log_7 49 = 2 -> 7^2 = 49. Misconception to address aloud: students try to 'cancel' the base and the log like factors, instead of reading the whole expression as one exponent statement.",
    },
    {
      title: "Common and Natural Logarithms",
      sub: "Objectives 2 and 5 — the two logarithms your calculator knows, and order of magnitude",
      graph: "g_log_basic", graphW: 6.0, graphY: 2.55,
      graphAlt: "The curve f of x equals log base 2 of x, through 1 comma 0 and 2 comma 1, approaching the vertical asymptote x equals 0",
      panel: {
        h: "ON YOUR CALCULATOR",
        items: [
          "log x with no base written means log_10 x — the COMMON logarithm.",
          "ln x means log_e x — the NATURAL logarithm, base e ≈ 2.71828.",
          "Every calculator has a LOG key and an LN key — no other base has its own key.",
          "Order of magnitude: round log(N) to estimate how many digits N has — log(6.3×10⁸) ≈ 8.8, so N is order of magnitude 9.",
        ],
      },
      panelX: 7.1, panelW: 5.8, panelH: 4.0,
      bar: ["WHY e MATTERS HERE", "e is the natural base for continuous growth — the same e from compound-interest and population models in Topic 6’s exponential work. ln undoes e^x exactly as log undoes 10^x."],
      barY: 6.32,
      notes: "log 50 = log_10 50 approx 1.699. ln 50 = log_e 50 approx 3.912. Order of magnitude of 6.3x10^8 is 9 (log approx 8.8, rounds up to the next power of ten it is closest to reaching). Misconception to address aloud: students think 'log' with no base is base e (confusing it with ln) -- log with no base is ALWAYS base 10 in this course; ln is the only one that means base e.",
    },
    {
      title: "Logarithms and Exponential Models",
      sub: "Objective 4 — solving for time or rate inside a growth/decay model",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "An exponential model A = A₀·b^t asks for A given t — easy, just substitute.",
          "But 'how long until A reaches a target?' asks for t given A — t is trapped in the exponent.",
          "Isolate the power first: b^t = A/A₀.",
          "Take log_b of both sides: t = log_b(A/A₀) — this is exactly what a logarithm is FOR.",
          "This is the same growth-factor idea from Lesson 6-1, now solved in the other direction.",
        ],
      },
      panelX: 0.45, panelY: 2.5, panelW: 6.6, panelH: 4.0,
      rowsHead: ["STEP", "RESULT"],
      rowsTop: 2.5, rowH: 0.9, rowsX: 7.35, rowsW: 5.55,
      rows: [
        ["Model", { eq: "l_model1", k: 1.6 }],
        ["Isolate the power, then take the log", { eq: "l_model2", k: 3.0 }],
      ],
      bar: ["THE PATTERN TO MEMORIZE", "whenever the unknown sits in the EXPONENT, isolate the exponential term, then apply a logarithm with the same base to both sides."],
      barY: 6.32,
      notes: "A = A0 b^t solved for t: b^t = A/A0, so t = log_b(A/A0). This directly extends Lesson 6-1's growth/decay factors -- same b, now solving for time instead of amount. Misconception to address aloud: students try to divide by b or subtract b from both sides instead of taking a logarithm -- remind them b^t is multiplicative in t, not additive, so only a logarithm undoes it.",
    },
  ],

  quickCheck: {
    lead: "Evaluate", leadW: 2.0,
    eq: "l_qc", k: 2.0,
    think: "Ask: 3 to what power gives 27? Check your answer by rewriting it in exponential form.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time a common logarithm.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "l_g1", t: "Evaluate, then check by rewriting in exponential form.", hint: "2 to what power gives 32?" },
      { eq: "l_g2", t: "Evaluate — this is a common logarithm.", hint: "10 to what power gives 10,000? Count the zeros." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Evaluate four logarithms by converting each to exponential form first: log_2 16, log_10 1000, log_5 25, log_3 1.", "State whether each is a common logarithm, a natural logarithm, or neither.", "Use a calculator to evaluate log 50 and ln 50 — round to three decimal places.", "Check each answer against the exponential form before moving on."],
        help: "You may use: the conversion rule on the board, a calculator, and a partner.",
        done: "every logarithm you evaluated checks out in exponential form.", eq: "l_ws1" },
      { items: ["Solve 6^x = 216 by converting to a logarithm.", "Solve log_4 x = 3 by converting to exponential form.", "A tank starts with 6,000 liters and grows 18% a year, modelling desalination-plant storage capacity under Vision 2030. Set up the equation for the number of years to reach 50,000 liters — do not solve yet.", "Now solve it with a calculator, to one decimal place."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your equation is set up BEFORE you touch a calculator, and your final answer carries units (years).", eq: "l_ws3" },
      { items: ["Explain why log_b x is undefined for x ≤ 0 — argue from what a logarithm MEANS (an exponent on a positive base), not just “the calculator gives an error”.", "A classmate says log(50) and ln(50) should give the same number because they are “both logarithms of 50.” Explain what's wrong with this, using the two different bases.", "Show algebraically that log_b(b^k) = k for any base b and any exponent k — explain why this must always be true."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument grounded in the definition, not just a computed answer.", eq: null },
    ],
  },

  production: {
    title: "How Long Until the Reservoir Runs Low?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A Jeddah desalination reservoir holds 500,000 m³ and usage is DRAINING it by 4% a week (a decay factor of 0.96), part of monitoring under the Kingdom's water-security planning.",
    eq: "l_model_w", eqK: 2.2,
    tasks: [
      "(a)  Write the volume function V(t) in terms of weeks t.",
      "(b)  Set up an equation for the number of weeks until the reservoir reaches 300,000 m³ — do not solve yet.",
      "(c)  Solve for t using logarithms, to one decimal place, and state the units.",
      "(d)  A colleague says “just divide 500,000 by 300,000 and use that as the answer.” Explain in one sentence why this skips the step that actually answers the question.",
    ],
    note: "Exact expressions shown before any decimal is computed, units named (m³, weeks), and the equation set up BEFORE it is solved.",
    aiPrompt: "“Check whether I isolated the exponential term correctly before taking the logarithm, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide the base and watch the exponential curve fold into its logarithm",
    explore: "graph f(x) = b^x and g(x) = log_b(x) together with a slider for b (b > 1). Trace a point on f(x), reflect it across y = x, and watch it land exactly on g(x). Then set b = 1.18 and check your production-task numbers against where the curve crosses your target value.",
  },

  gate: {
    eq: "l_gate_w",
    items: [
      { t: "Evaluate the logarithm shown.", eq: null },
      { t: "Rewrite it in exponential form.", eq: null },
      { t: "In ONE sentence, explain what a logarithm IS, in terms of exponents.", eq: null },
    ],
    footer: "Exact answers only. Question 2 shown as a full exponential equation, not just restated in words, and question 3 a definition, not an example.",
    routing: "PASS → Enrichment & Challenge (solving an exponential model for time, both directions).      NOT YET → Targeted Learning Clinic on the exponential–logarithm conversion, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the reservoir decay function, the equation set up for the target volume, and the solved number of weeks." },
      { h: "Expose the trap", d: "Add one worked NON-example — dividing the two volumes and stopping there instead of taking a logarithm — and a sentence saying what that shortcut actually computes instead." },
      { h: "Say why it matters", d: "One caption — “why a water utility needs to know WHEN, not just by how much” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which direction is still harder for you — evaluating a logarithm you're given, or setting one up from a word problem yourself?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Logarithms sit in the Grade 11 band, evaluated as straightforward base-exponent conversions — no calculator, so the base is always a clean power.", fmt: "Four-option multiple choice, no calculator.", tip: "Convert to exponential form FIRST, every time — log_b x = y becomes b^y = x, and the answer is usually then obvious by inspection.",
      question: "Evaluate log_4 64.",
      steps: ["Rewrite as exponential form: 4^y = 64.", "Test powers of 4: 4¹=4, 4²=16, 4³=64.", "So y = 3, meaning log_4 64 = 3."] },
    { code: "SAT", full: "College Board", skill: "Advanced Math — exponential equations solved using logarithms is a recurring Advanced Math item type, often embedded in a modelling context.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Isolate the exponential term completely before applying a logarithm — divide out any leading coefficient first, or the logarithm applies to the wrong expression.",
      question: "500(1.06)^t = 1000. Solve for t to the nearest tenth.",
      steps: ["Divide both sides by 500: 1.06^t = 2.", "Take log (or ln) of both sides: t·log(1.06) = log(2).", "Divide: t = log(2) / log(1.06) ≈ 11.9."] },
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Exponent-and-root reasoning under time pressure, including recognizing a power of a familiar base without a calculator.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Recognize common powers of 2 (2, 4, 8, 16, 32, ...512) on sight — GAT logarithm items almost always use a base with a clean, memorizable power chain.",
      question: "log_2 512 = ? (A) 7  (B) 8  (C) 9  (D) 10",
      steps: ["Rewrite as 2^y = 512.", "Double from 2: 2,4,8,16,32,64,128,256,512 — that's 9 doublings from 2⁰=1.", "So y = 9 — answer (C)."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "log_b x = y and b^y = x say the same thing — when the unknown is an exponent, convert to a logarithm and it stops being hidden."],

  summary: [
    "Define a logarithm as the exponent that produces a given value from a given base.",
    "Convert freely between exponential form and logarithmic form.",
    "Identify and evaluate common logarithms (base 10) and natural logarithms (base e).",
    "Use a logarithm's value to estimate a number's order of magnitude.",
    "Solve an exponential model for an unknown exponent (time or rate) using logarithms.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 6 · Lesson 6-4 — Logarithmic Functions (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on exponential-to-log conversion.",
  ],

  notes: {
    cover: "Week 6 lesson for 11B, continuing Topic 6 (Exponential and Logarithmic Functions) directly from Lesson 6-1. Per the department's own Curriculum Distribution, Lesson 6-2 (Exponential Models) is not taught in this sequence -- do not reference it as a prerequisite. Three teaching days this week, so the Smart Production step may run into the next session -- protect the Mastery Gate instead.",
    objectives: "All five objectives are verbatim from the curriculum map. The map lists HSF.BF.B.4.A, HSF.BF.B.5 and HSF.LE.A.4 for this lesson, and only MP.2 and MP.7 -- do not add others.",
    vocabulary: "All five terms are the map's list. Make students say the difference aloud: COMMON log has no base written and means base 10; NATURAL log is written ln and means base e -- there is no such thing as 'log' meaning base e in this course.",
    prior: "If a student cannot evaluate b^x directly (from Lesson 6-1), the whole lesson stalls -- they need that skill to CHECK every logarithm they compute. Watch for it in the diagnostic, questions 1-3.",
    diagnose: "Answers: 2^5=32, 10^3=1000, f(0)=2(3)^0=2, 2^x=16 -> x=4, log_2 20 is between 4 and 5 (since 2^4=16 and 2^5=32). Expected gap: Q5, where students want an exact integer and don't yet have language for 'between two values' -- this IS the motivation for the whole lesson.",
    quickCheck: "Answer: log_3 27 = 3, since 3^3=27. Watch for students who answer 9 (computing 3x3 instead of finding the exponent) or 24 (subtracting instead of asking 'to what power').",
    guided: "Answers -- 1: log_2 32 = 5 (2^5=32). 2: log_10 10,000 = 4 (10^4=10,000, four zeros). Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers -- (a) V(t) = 500,000(0.96)^t. (b) 500,000(0.96)^t = 300,000. (c) 0.96^t = 0.6 -> t = log(0.6)/log(0.96) ≈ 12.5 weeks. (d) dividing 500,000 by 300,000 only finds the RATIO (1.67), not how many weeks of 4% shrinkage produce that ratio -- the logarithm is the step that actually counts the weeks.",
    geogebra: "The reflection across y=x is the whole point -- every point on f(x)=b^x reflects to a point on g(x)=log_b(x), because they are inverse functions. This is the visual proof that a logarithm 'undoes' an exponential.",
    gate: "Answers: for log_5 125, 5^3=125 so the value is 3; exponential form 5^3=125; a logarithm is the exponent you need on a given base to produce a given number. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part -- stopping at the ratio (500,000/300,000 = 1.67) and calling it the answer is exactly the kind of shortcut a real report might present incorrectly; the correction is showing what a logarithm adds that division alone does not.",
    exams: "Show this before homework so the practice set has an obvious purpose. Each card now works a full item in steps, not just a bare question -- walk through at least one aloud before moving on.",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L63);
})();

module.exports = { GR11_L63 };

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
  mps: ["MP.2", "MP.5"],
  assessments: ASSESS,

  objectives: [
    "Understand and evaluate logarithms.",
    "Analyze common logarithms and natural logarithms.",
    "Convert between exponential and logarithmic forms.",
    "Use logarithms to solve problems involving exponential models.",
    "Evaluate logarithms using technology.",
  ],
  essentialQuestion: "How can we use logarithms and relate them to exponents?",

  vocabulary: [
    { term: "Logarithm", def: "The exponent to which a base b must be raised to produce x: log_{b} x = y means b^{y} = x. A logarithm IS an exponent." },
    { term: "Common logarithm", def: "A logarithm with base 10, written log x (no base shown). log x means log_{10} x." },
    { term: "Natural logarithm", def: "A logarithm with base e (≈ 2.71828), written ln x. ln x means log_{e} x." },
    { term: "Logarithmic function", def: "A function of the form f(x) = log_{b} x — the inverse of the exponential function f(x) = b^{x}." },
    { term: "Order of magnitude", def: "The power of 10 nearest a number's size, found by rounding its common logarithm — a quick way to compare sizes that differ by factors of ten." },
  ],
  vocabSub: "All five terms the curriculum map lists for this lesson",

  prior: [
    { h: "Lesson 6-1: exponential functions", eq: "l_exp1", d: "You can graph and evaluate b^{x}. Today asks the opposite question — given the OUTPUT, find the exponent." },
    { h: "Solving 2^{x} = 8 by inspection", eq: "l_d4", d: "Worked when the answer was a whole number. Today's tool works even when it isn't." },
    { h: "Inverse functions", eq: null, d: "From Algebra II. A logarithm is nothing new here — it is exactly the inverse of an exponential function." },
  ],
  priorSub: "Three things you already know — today gives the missing operation a name",
  carryOver: "A logarithm is just an exponent wearing a different name. log_{b} x = y answers the question “b to WHAT power gives x?” — the exact question you could only answer by guessing until now.",
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
          "log_{b} x = y is ALWAYS asking: b to what power gives x?",
          "The base is positive and not 1 (b > 0, b ≠ 1).",
          "log_{2} 8 = 3, because 2^{3} = 8 — check the exponential form to verify any logarithm.",
          "log_{b} 1 = 0 for every valid base, because b^{0} = 1.",
          "log_{b} x is undefined for x ≤ 0 — no power of a positive base gives zero or a negative number.",
        ],
      },
      panelX: 0.45, panelY: 2.5, panelW: 6.5, panelH: 4.0,
      rowsHead: ["FORM", "EXAMPLE"],
      rowsTop: 2.5, rowH: 0.78, rowsX: 7.3, rowsW: 5.6,
      rows: [
        ["Exponential → log", { eq: "l_ex_conv1", k: 1.35 }],
        ["Log → exponential", { eq: "l_ex_conv2", k: 1.35 }],
        ["Evaluate", { eq: "l_ex_eval1", k: 1.35 }],
        ["Evaluate", { eq: "l_ex_eval2", k: 1.35 }],
      ],
      bar: ["THE CONVERSION RULE", "b^{y} = x  ⟺  log_{b} x = y — the base stays the base; the exponent and the answer swap sides."],
      barY: 6.32,
      notes: "log_2 8 = 3 because 2^3 = 8. log_5 1 = 0 because 5^0 = 1 (any valid base). 3^4 = 81 -> log_3 81 = 4. log_7 49 = 2 -> 7^2 = 49. Domain: x > 0 only. Misconception to address aloud: students try to 'cancel' the base and the log like factors, instead of reading the whole expression as one exponent statement.",
    },
    {
      title: "Common and Natural Logarithms",
      sub: "Objectives 2 and 5 — the two logarithms your calculator knows, and order of magnitude",
      graph: "g_log_basic", graphW: 6.0, graphY: 2.55,
      graphAlt: "The curve f of x equals log base 2 of x, through 1 comma 0 and 2 comma 1, approaching the vertical asymptote x equals 0",
      panel: {
        h: "ON YOUR CALCULATOR",
        items: [
          "log x with no base written means log_{10} x — the COMMON logarithm.",
          "ln x means log_{e} x — the NATURAL logarithm, base e ≈ 2.71828.",
          "Calculators have dedicated LOG and LN keys.",
          "Order of magnitude: round log N to the nearest integer — log(6.3×10^{8}) ≈ 8.8 → 9, so N is about 10^{9}.",
          "The graph shows the shape of every log with b > 1: through (1, 0), asymptote x = 0, domain x > 0.",
        ],
      },
      panelX: 7.1, panelW: 5.8, panelH: 4.0,
      bar: ["WHY e MATTERS HERE", "e is the natural base for continuous growth. ln undoes e^{x} exactly as log undoes 10^{x}."],
      barY: 6.32,
      notes: "log 50 = log_10 50 approx 1.699. ln 50 = log_e 50 approx 3.912. Order of magnitude of 6.3x10^8 is 9 (log approx 8.8, which rounds to 9; the number has 9 digits). Misconception to address aloud: students think 'log' with no base is base e (confusing it with ln) -- log with no base is ALWAYS base 10 in this course; ln is the only one that means base e.",
    },
    {
      title: "Logarithms and Exponential Models",
      sub: "Objective 4 — solving for time or rate inside a growth/decay model",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Worked example: a culture starts at 5 and doubles each hour. When does it reach 40?",
          "The model is A = 5·2^{t}, so 5·2^{t} = 40.",
          "Divide by 5 to isolate the power: 2^{t} = 8.",
          "Convert: t = log_{2} 8 = 3 hours. Check: 5·2^{3} = 40 ✓",
          "General pattern: A = A_{0}·b^{t} gives t = log_{b}(A/A_{0}).",
        ],
      },
      panelX: 0.45, panelY: 2.5, panelW: 6.6, panelH: 4.0,
      rowsHead: ["STEP", "RESULT"],
      rowsTop: 2.5, rowH: 0.78, rowsX: 7.35, rowsW: 5.55,
      rows: [
        ["Model and target", { eq: "l_mod_a", k: 1.8 }],
        ["Isolate the power", { eq: "l_mod_b", k: 1.8 }],
        ["Convert to a log", { eq: "l_mod_c", k: 1.8 }],
        ["General pattern", { eq: "l_model2", k: 1.25 }],
      ],
      bar: ["THE PATTERN TO MEMORIZE", "when the unknown is in the EXPONENT, isolate the power first, then convert: b^{t} = k  ⟹  t = log_{b} k."],
      barY: 6.32,
      notes: "Worked: 5(2)^t = 40 -> 2^t = 8 -> t = log_2 8 = 3. General: A = A0 b^t -> t = log_b(A/A0). This directly extends Lesson 6-1's growth/decay factors -- same b, now solving for time instead of amount. Misconception to address aloud: students try to divide by b or subtract b from both sides instead of taking a logarithm -- remind them b^t is multiplicative in t, not additive, so only a logarithm undoes it.",
    },
  ],

  quickCheck: {
    lead: "Evaluate", leadW: 2.0,
    eq: "l_qc", k: 2.0,
    think: "Ask: 3 to what power gives 27? Check by rewriting in exponential form.",
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
      { items: ["Evaluate by converting each to exponential form first: log_{2} 16, log_{10} 1000, log_{5} 25, log_{3} 1.", "State whether each is a common logarithm, a natural logarithm, or neither.", "Use a calculator to evaluate log 50 and ln 50 — round to three decimal places.", "Check each answer against the exponential form before moving on."],
        help: "You may use: the conversion rule on the board, a calculator, and a partner.",
        done: "every logarithm you evaluated checks out in exponential form.", eq: "l_ws1" },
      { items: ["Solve 6^{x} = 216 by converting to a logarithm.", "Solve log_{4} x = 3 by converting to exponential form.", "A tank starts with 6,000 liters and grows 18% a year, modelling desalination-plant storage capacity under Vision 2030. Set up the equation for the years to reach 50,000 liters — do not solve yet.", "Now solve it with a calculator, to one decimal place."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your equation is set up BEFORE you touch a calculator, and your final answer carries units (years).", eq: "l_ws3" },
      { items: ["Explain why log_{b} x is undefined for x ≤ 0 — argue from what a logarithm MEANS, not just “the calculator gives an error”.", "A classmate says log(50) and ln(50) should give the same number because they are “both logarithms of 50.” Explain what's wrong with this, using the two different bases.", "Show that log_{b}(b^{k}) = k for any valid base b and any k, and explain why it must always be true."],
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
    preview: "g_exp_log_inverse",
    previewAlt: "Graphs of 2 to the x, log base 2 of x and the line y equals x; the first two are mirror images across the line",
    url: "https://www.geogebra.org/graphing",
    steps: [
      "Open the link (any browser, no sign-in needed).",
      "Type b = 2 and click the slider button that appears.",
      "Type f(x) = b^(x), then g(x) = log(b, x), then y = x.",
      "Type A = (1, b) and B = (b, 1). Right-click A: Trace on. Drag the slider.",
    ],
    explore: "A and B always mirror across y = x, and B sits on g. Where does g cross the x-axis for every b? Why is there no graph for x ≤ 0?",
  },

  gate: {
    eq: "l_gate_w",
    items: [
      { t: "Evaluate the logarithm shown.", eq: "l_gate_w" },
      { t: "Rewrite it in exponential form.", eq: null },
      { t: "In ONE sentence, explain what a logarithm IS, in terms of exponents.", eq: null },
    ],
    footer: "Exact answers only. Write question 2 as a full equation; question 3 is a definition, not an example.",
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
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Convert between forms, twice, with no calculator.",
      question: "If log_{4} x = 3, what is log_{2} x?   (A) 3   (B) 6   (C) 12   (D) 1.5",
      steps: ["log_{4} x = 3 ⟹ x = 4^{3} = 64.", "log_{2} 64 = 6, since 2^{6} = 64.", "Answer (B). Strategy: find x first."],
      trap: "(A) assumes the base does not matter; (C) multiplies 4 × 3; (D) halves 3." },
    { code: "SAT", full: "College Board — Advanced Math", skill: "Isolate the exponential, then write the unknown exponent as a logarithm.",
      question: "V = 500(1.06)^{t} riyals. Which gives the years to reach 1000?   (A) log_{1.06} 1000   (B) log_{1.06} 2   (C) log_{2} 1.06   (D) 2/1.06",
      steps: ["Divide by 500: 1.06^{t} = 2.", "Convert: t = log_{1.06} 2 ≈ 11.9 years.", "Answer (B). Strategy: divide before converting."],
      trap: "(A) skips the division by 500; (C) swaps base and argument; (D) treats t as a factor." },
    { code: "GAT", full: "Qudurat — Quantitative Comparison", skill: "Compare two logarithms by evaluating each from its exponent form, no calculator.",
      question: "A = log_{2} 64 and B = log_{3} 243.   (A) A greater   (B) B greater   (C) equal   (D) cannot tell",
      steps: ["2^{6} = 64, so A = 6.", "3^{5} = 243, so B = 5.", "6 > 5: answer (A) in about 45 seconds."],
      trap: "Choosing (B) because 243 > 64; the base decides the exponent, not the size of the number." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "log_{b} x = y and b^{y} = x say the same thing — when the unknown is an exponent, convert and it stops being hidden."],

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
    objectives: "All five objectives are verbatim from the curriculum map. The map lists HSF.BF.B.4.A, HSF.BF.B.5 and HSF.LE.A.4 for this lesson, and only MP.2 and MP.5 -- do not add others.",
    vocabulary: "All five terms are the map's list. Make students say the difference aloud: COMMON log has no base written and means base 10; NATURAL log is written ln and means base e -- there is no such thing as 'log' meaning base e in this course.",
    prior: "If a student cannot evaluate b^x directly (from Lesson 6-1), the whole lesson stalls -- they need that skill to CHECK every logarithm they compute. Watch for it in the diagnostic, questions 1-3.",
    diagnose: "Answers: 2^5=32, 10^3=1000, f(0)=2(3)^0=2, 2^x=16 -> x=4, log_2 20 is between 4 and 5 (since 2^4=16 and 2^5=32). Expected gap: Q5, where students want an exact integer and don't yet have language for 'between two values' -- this IS the motivation for the whole lesson.",
    quickCheck: "Answer: log_3 27 = 3, since 3^3=27. Watch for students who answer 9 (computing 3x3 instead of finding the exponent) or 24 (subtracting instead of asking 'to what power').",
    guided: "Answers -- 1: log_2 32 = 5 (2^5=32). 2: log_10 10,000 = 4 (10^4=10,000, four zeros). Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers -- (a) V(t) = 500,000(0.96)^t. (b) 500,000(0.96)^t = 300,000. (c) 0.96^t = 0.6 -> t = log(0.6)/log(0.96) ≈ 12.5 weeks. (d) dividing 500,000 by 300,000 only finds the RATIO (1.67), not how many weeks of 4% shrinkage produce that ratio -- the logarithm is the step that actually counts the weeks.",
    geogebra: "The reflection across y=x is the whole point -- every point on f(x)=b^x reflects to a point on g(x)=log_b(x), because they are inverse functions. This is the visual proof that a logarithm 'undoes' an exponential.",
    gate: "Answers: log_5 125 = 3 because 5^3=125; exponential form 5^3=125; a logarithm is the exponent you need on a given base to produce a given number. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part -- stopping at the ratio (500,000/300,000 = 1.67) and calling it the answer is exactly the kind of shortcut a real report might present incorrectly; the correction is showing what a logarithm adds that division alone does not.",
    exams: "Show before homework. Format reminders: SAAT four-option, no calculator; SAT two 35-min adaptive modules, calculator allowed; GAT about 75 s per item, no calculator. Walk one item aloud, and name the trap before revealing it.",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L63);
})();

module.exports = { GR11_L63 };

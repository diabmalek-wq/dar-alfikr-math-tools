// Grade 11 · Topic 6 · Lesson 6-4 — Logarithmic Functions
//
// Follows L6-3 (Logarithms) directly. Objectives, vocabulary and standards
// are quoted VERBATIM from the curriculum map (Scope and sequence_OA2W_Global.docx,
// Unit 6, Lesson 4).
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6l4_docs.js for the matching plan/activity/PBL.
const { build } = require("./lesson_engine");

const MATH = "math_w6l4/_index.json";
const GRAPH = "graphs_w6l4/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

const GR11_L64 = {
  out: "Gr11_T6_L6-4_Logarithmic_Functions.pptx",
  deckTitle: "Logarithmic Functions — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-4",
  lessonTitle: "Logarithmic Functions",
  titleSize: 34,
  subtitle: "Every logarithmic function is an exponential function turned inside out",
  titleEq: "m_title_w", titleEqK: 2.4,
  titleEqAlt: "f of x equals log base b of x, if and only if its inverse f inverse of x equals b to the x",
  grade: "Grade 11", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-4",
  lessonRef: "Lesson 6-4 — Logarithmic Functions",
  nextLesson: "Topic 6 · Lesson 6-5 — Properties of Logarithms",

  codes: ["HSF.IF.B.5", "HSF.IF.B.6", "HSF.IF.C.7.E", "HSF.IF.C.9", "HSF.BF.B.3", "HSF.BF.B.4", "(+)HSF.BF.B.4.C"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Identify key features of logarithmic functions.",
    "Use inverse properties to analyze logarithmic and exponential functions.",
    "Graph logarithmic functions and interpret their key features.",
    "Write and interpret the inverses of exponential and logarithmic functions.",
  ],
  essentialQuestion: "How are the key features of a logarithmic function connected to its exponential inverse, and what do they tell us about the function's graph?",

  vocabulary: [
    { term: "Inverse relationship", def: "Two functions f and g are inverses when g undoes exactly what f does: if f takes a to b, g takes b back to a. Their graphs are reflections of each other across the line y = x." },
    { term: "Logarithmic function", def: "A function of the form f(x) = log_b x (b > 0, b ≠ 1) — the inverse of the exponential function f(x) = b^x." },
  ],
  vocabSub: "Both terms the curriculum map lists for this lesson",

  prior: [
    { h: "Lesson 6-3: what a logarithm is", eq: "m_prior_log", d: "log_b x = y means b^y = x — a logarithm IS an exponent. You already convert freely between the two forms." },
    { h: "Lesson 6-1: exponential key features", eq: "m_prior_exp", d: "Domain, range, intercept, and asymptote of b^x. Today asks what happens to each of these once the function is inverted." },
    { h: "Inverse functions (Topic 5)", eq: "m_prior_inv", d: "Swap x and y, solve for y, and the new graph is the old one reflected across y = x. A logarithm is not a new idea here — it is the inverse of an exponential, full stop." },
  ],
  priorSub: "Three things you already know — today puts them together",
  carryOver: "A logarithmic function is what you get when you reflect an exponential function across y = x. Every key feature — domain, range, intercept, asymptote — swaps sides in exactly the way inverses always swap.",
  carryOverEq: "m_def",

  diagnose: {
    title: "Warm-Up: What Survives the Swap?",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "m_d1", t: "Evaluate directly." },
      { eq: "m_d2", t: "State the domain and range." },
      { eq: "m_d3", t: "Find the inverse function." },
      { eq: "m_d4", t: "True or false? Be ready to justify." },
      { eq: "m_d5", t: "State the horizontal asymptote." },
    ],
    routing: "0–2 correct → re-teach inverses with me.      3–4 correct → straight to key features.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Key Features of Logarithmic Functions",
      sub: "Objective 1 — domain, range, intercept, asymptote, and end behavior",
      graph: "gm_key_features", graphW: 5.9, graphY: 2.55,
      graphAlt: "The curve f of x equals log base 3 of x, through 1 comma 0 and 3 comma 1, approaching the vertical asymptote x equals 0",
      panel: {
        h: "READ IT OFF THE GRAPH",
        items: [
          "Domain: x > 0 — a logarithm is undefined for zero or a negative input.",
          "Range: all real numbers — the curve climbs and falls without bound.",
          "x-intercept always (1, 0), because log_b 1 = 0 for every base.",
          "No y-intercept — the vertical asymptote at x = 0 blocks it.",
          "For b > 1: as x→0⁺, f(x)→−∞; as x→∞, f(x)→∞ — a slow, never-ending climb.",
        ],
      },
      panelX: 7.05, panelW: 5.85, panelH: 4.0,
      bar: ["THE FIVE FEATURES TO NAME EVERY TIME", "domain · range · intercept · asymptote · end behavior — always in that order, so nothing gets skipped."],
      barY: 6.32,
      notes: "f(x) = log_3 x: domain x>0, range all reals, x-intercept (1,0), vertical asymptote x=0, end behavior f to -infinity as x to 0+ and f to infinity as x to infinity. Misconception to address aloud: students look for a y-intercept out of habit -- a logarithmic function never has one, because x=0 is excluded from the domain, not just a point where f happens to be undefined.",
    },
    {
      title: "Inverse Properties",
      sub: "Objective 2 — the two identities that prove log and exponential undo each other",
      rowsHead: ["PROPERTY", "WORKED CHECK"],
      rowsTop: 2.55, rowH: 1.1, rowsCw: [2.95, 3.35],
      rows: [
        ["log_b(b^x) = x", { eq: "m_ip_check1", k: 1.55 }],
        ["b^(log_b x) = x", { eq: "m_ip_check2", k: 1.55 }],
      ],
      panel: {
        h: "WHY THIS MATTERS",
        items: [
          "log_b(b^x) = x for every real x — take the log of an exponential, base and exponent vanish, leaving x.",
          "b^(log_b x) = x for every x > 0 — raise the base to a logarithm, and it undoes back to x.",
          "These two identities ARE the proof that f(x) = b^x and g(x) = log_b x are genuine inverses.",
          "Domain of log_b x = range of b^x (all positive reals). Range of log_b x = domain of b^x (all reals) — domain and range always swap under inversion.",
        ],
      },
      panelX: 7.05, panelW: 5.85, panelH: 4.0,
      bar: ["THE TWO IDENTITIES TO MEMORIZE", "log_b(b^x) = x for every real x.   b^(log_b x) = x for every x > 0."],
      barY: 6.32,
      notes: "log_2(2^5) = 5, because the log and the exponential cancel. 3^(log_3 7) = 7, same idea in the other order. Domain of log_b x is x>0, which is exactly the RANGE of b^x; range of log_b x is all reals, which is exactly the DOMAIN of b^x. Misconception to address aloud: students think log_b(b^x)=x only works for 'nice' exponents -- it holds for every real x, because it is an identity, not a computation.",
    },
    {
      title: "Graphing Transformations and Writing Inverses",
      sub: "Objectives 3 and 4 — shifting the asymptote, and solving for the inverse algebraically",
      graph: "gm_shift", graphW: 5.6, graphY: 2.55,
      graphAlt: "The curve g of x equals log base 2 of x minus 3 shown beside its parent f of x equals log base 2 of x, with the vertical asymptote shifted from x equals 0 to x equals 3",
      panel: {
        h: "FIND THE INVERSE, STEP BY STEP",
        items: [
          "Start: y = log_3(x − 1).",
          "Swap x and y: x = log_3(y − 1).",
          "Convert to exponential form: 3^x = y − 1.",
          "Solve for y: y = 3^x + 1, so f⁻¹(x) = 3^x + 1.",
        ],
      },
      panelX: 7.0, panelW: 5.9, panelH: 4.0,
      bar: ["SHIFT RULE", "log_b(x) + k shifts vertically, asymptote stays x = 0.   log_b(x − h) shifts the asymptote itself, to x = h."],
      barY: 6.32,
      notes: "g(x) = log_2(x-3) has its asymptote moved from x=0 to x=3 -- the whole graph slides right 3, exactly like any other horizontal shift. Inverse steps: y = log_3(x-1) -> swap -> x = log_3(y-1) -> exponential form 3^x = y-1 -> y = 3^x + 1. Misconception to address aloud: students shift the WRONG direction (log_b(x-h) shifts the asymptote to x=+h, not x=-h) -- test it by substituting x=h+1 and checking the asymptote sits where the argument of the log hits zero.",
    },
  ],

  quickCheck: {
    lead: "State the vertical asymptote and x-intercept of", leadW: 4.6,
    eq: "m_qc", k: 1.5,
    think: "Ask: for f(x) = log_5 x, where does the input hit zero? That is the asymptote. Where does the output hit zero? That is the x-intercept.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time with a horizontal shift.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "m_g1", t: "State all four key features.", hint: "Domain, range, asymptote, x-intercept — in that order." },
      { eq: "m_g2", t: "Find the inverse function.", hint: "Swap x and y first, then convert to exponential form." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["State the domain, range, vertical asymptote, and x-intercept of four logarithmic functions: log_4 x, log_2(x−3), log_5(x)+2, log_3(x+1)−1.", "Sketch one of the four, labelling its asymptote and x-intercept.", "Verify one inverse property numerically: show log_2(2^5) = 5.", "Check each answer against the general rule before moving on."],
        help: "You may use: the five-feature checklist on the board, a calculator, and a partner.",
        done: "every key feature you stated matches the general rule for its function's shift.", eq: "m_ws1" },
      { items: ["Find the inverse of two logarithmic functions: f(x) = log_2 x, then g(x) = log_5(x) − 3.", "A water-treatment lab at a Red Sea desalination plant reports pH values and needs a way to recover hydrogen-ion concentration from a pH reading, part of Vision 2030 water-security monitoring. Starting from pH = −log₁₀[H⁺], find the inverse relationship [H⁺] in terms of pH.", "Use your inverse to find [H⁺] when pH = 8.1 (slightly basic, typical of treated seawater)."],
        help: "You may use: the worked inverse-steps example, and a calculator.",
        done: "your inverse is solved algebraically (not guessed), and your final concentration answer carries units (mol/L).", eq: "m_inv_ws1" },
      { items: ["Prove that log_b(b^x) = x for any base b and any real x — argue from what a logarithm MEANS, not just by example.", "Explain why a logarithmic function never has a y-intercept, using the definition of its domain.", "A classmate says “log_b(x−h) and log_b(x)−h are the same shift.” Explain what's wrong, using the asymptote of each."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument grounded in the definition, not just a computed answer.", eq: null },
    ],
  },

  production: {
    title: "Reading the Water: pH at a Red Sea Desalination Plant",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A desalination plant on the Red Sea coast measures the hydrogen-ion concentration [H⁺] of its treated water and reports it as pH, using pH = −log₁₀[H⁺], where [H⁺] is measured in mol/L. This monitoring supports Vision 2030 water-security targets.",
    eq: "m_ctx_w", eqK: 2.0,
    tasks: [
      "(a)  State the domain of the pH function in terms of [H⁺], and explain what that domain restriction means physically (can [H⁺] be zero or negative?).",
      "(b)  A sample has [H⁺] = 4 × 10⁻⁸ mol/L. Find its pH, to two decimal places.",
      "(c)  Find the inverse function — write [H⁺] in terms of pH.",
      "(d)  A technician says “the inverse function is pointless — we always measure [H⁺] directly anyway.” Explain in one sentence a situation where the inverse function is actually the useful direction.",
    ],
    note: "Exact expressions shown before any decimal is computed, units named (mol/L), and the domain restriction stated as an inequality, not just described in words.",
    aiPrompt: "“Check whether I applied the inverse steps in the right order before I converted to exponential form, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide the base and watch the exponential curve fold into its logarithm",
    explore: "graph f(x) = b^x and g(x) = log_b(x) together with a slider for b (b > 1). Trace a point on f(x), reflect it across y = x, and watch it land exactly on g(x). Then shift g(x) horizontally and watch the asymptote move with it.",
  },

  gate: {
    eq: "m_gate1_w",
    items: [
      { t: "State all four key features: domain, range, vertical asymptote, x-intercept.", eq: null },
      { t: "Find the inverse of f(x) = log_4(x) − 1.", eq: "m_gate2" },
      { t: "In ONE sentence, explain why a logarithmic function's graph never crosses its vertical asymptote.", eq: null },
    ],
    footer: "Exact answers only. Question 2 shown as a fully simplified inverse function, not left half-solved, and question 3 a definition-based reason, not an example.",
    routing: "PASS → Enrichment & Challenge (graphing a logarithmic function from its inverse alone).      NOT YET → Targeted Learning Clinic on the inverse-steps method, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the pH function, the domain restriction, the pH calculation, and the inverse function solved for [H⁺]." },
      { h: "Expose the trap", d: "Add one worked NON-example — dropping the negative sign when converting pH back to [H⁺] — and a sentence saying what error that produces (a concentration greater than 1 mol/L, which is never realistic for treated water)." },
      { h: "Say why it matters", d: "One caption — “why an inverse function lets an engineer work backward from a report to a raw measurement” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which direction is still harder for you — reading key features straight off a graph, or solving algebraically for an inverse function?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Domain and asymptote of a shifted logarithmic function sit in the Grade 11 band, usually asked as reading a restriction directly off the function rule.", fmt: "Four-option multiple choice, no calculator.", tip: "Set the argument of the log greater than zero and solve — that inequality IS the domain, every time.",
      question: "State the vertical asymptote of f(x) = log_3(x − 4).",
      steps: ["The asymptote sits where the argument of the log equals zero: x − 4 = 0.", "Solve: x = 4.", "So the vertical asymptote is x = 4."] },
    { code: "SAT", full: "College Board", skill: "Advanced Math — writing the inverse of a logarithmic or exponential function algebraically is a recurring item type.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Swap x and y FIRST, before doing any algebra — solving for the wrong variable is the most common error on this item type.",
      question: "Find the inverse of f(x) = log_2(x) + 5.",
      steps: ["Write y = log_2(x) + 5, then swap: x = log_2(y) + 5.", "Isolate the log: x − 5 = log_2(y).", "Convert to exponential form: y = 2^(x−5), so f⁻¹(x) = 2^(x−5)."] },
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Domain restrictions on a logarithmic expression under time pressure, usually a quick single-step inequality.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Don't solve the whole function — just set the inside of the log greater than zero and solve that one inequality.",
      question: "Domain of f(x) = log_5(x − 9) is? (A) x > 0  (B) x > 5  (C) x > 9  (D) x ≥ 9",
      steps: ["The argument must be strictly positive: x − 9 > 0.", "Solve: x > 9.", "Answer (C) — note it is strict, not ≥, so (D) is a trap."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "set the argument of the log greater than zero to find the domain, and swap x and y before you touch the algebra to find the inverse."],

  summary: [
    "Identify the domain, range, x-intercept, vertical asymptote, and end behavior of a logarithmic function.",
    "Use the two inverse properties — log_b(b^x) = x and b^(log_b x) = x — to analyze logarithmic and exponential functions together.",
    "Graph a logarithmic function, including a horizontal or vertical shift, and interpret its key features.",
    "Write the inverse of an exponential or logarithmic function algebraically, and interpret what it means in context.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 6 · Lesson 6-5 — Properties of Logarithms (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on the inverse-steps method.",
  ],

  notes: {
    cover: "Week 6 lesson for 11B, continuing Topic 6 (Exponential and Logarithmic Functions) directly from Lesson 6-3. Three teaching days this week, so the Smart Production step may run into the next session -- protect the Mastery Gate instead.",
    objectives: "All four objectives are verbatim from the curriculum map. The map lists HSF.IF.B.5, HSF.IF.B.6, HSF.IF.C.7.E, HSF.IF.C.9, HSF.BF.B.3, HSF.BF.B.4 and the plus-standard HSF.BF.B.4.C for this lesson -- do not add others.",
    vocabulary: "Both terms are the map's list. Make students say the inverse-relationship definition aloud in their own words before showing the logarithmic-function definition -- the second is a special case of the first.",
    prior: "If a student cannot state the key features of an exponential function (from Lesson 6-1), the whole lesson stalls -- they need that skill to predict what a logarithm's features will be BEFORE checking. Watch for it in the diagnostic, question 2.",
    diagnose: "Answers: log_2 8 = 3; g(x)=2^x has domain all reals, range y>0; f(x)=x+5 has inverse f^-1(x)=x-5; TRUE, the graph of f^-1 is the reflection of f across y=x; horizontal asymptote of 3^x - 2 is y = -2. Expected gap: Q4, where students confuse 'reflection across y=x' with 'reflection across the x-axis' -- this IS the motivation for today's graph-pair demonstration.",
    quickCheck: "Answer: vertical asymptote x=0, x-intercept (1,0), for f(x)=log_5 x. Watch for students who report a y-intercept (there isn't one) or confuse the asymptote with the intercept.",
    guided: "Answers -- 1: f(x)=log_3 x has domain x>0, range all reals, asymptote x=0, x-intercept (1,0). 2: f(x)=log_2(x)+4 -> swap -> x=log_2(y)+4 -> x-4=log_2(y) -> y=2^(x-4), so f^-1(x)=2^(x-4). Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers -- (a) domain [H+]>0, since a hydrogen-ion concentration of zero or negative is not physically possible -- there is always SOME concentration, however small. (b) pH = -log10(4x10^-8) = -(log10(4) + log10(10^-8)) = -(0.602 - 8) = 7.398, rounds to 7.40. (c) pH = -log10[H+] -> -pH = log10[H+] -> [H+] = 10^(-pH). (d) the inverse direction is useful whenever an engineer is given a target pH (a regulatory limit, say) and needs to know what concentration to dose FOR, rather than measuring an existing sample.",
    geogebra: "The reflection across y=x is the whole point -- every point on f(x)=b^x reflects to a point on g(x)=log_b(x), because they are inverse functions. Shifting g(x) horizontally after the reflection shows students the asymptote moves WITH the shift, not independently of it.",
    gate: "Answers: for g(x)=log_2(x+5), domain x>-5, range all reals, vertical asymptote x=-5, x-intercept where x+5=1 so x=-4, giving (-4,0); f(x)=log_4(x)-1 has inverse f^-1(x)=4^(x+1) (swap: x=log_4(y)-1 -> x+1=log_4(y) -> y=4^(x+1)); a logarithmic graph never crosses its vertical asymptote because the function is undefined AT and beyond that value -- the curve approaches but the domain never reaches it. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part -- dropping the negative sign when inverting pH = -log[H+] gives [H+] = 10^(pH) instead of 10^(-pH), producing a concentration far too large to be physically real; the correction is checking the sign BEFORE trusting the number.",
    exams: "Show this before homework so the practice set has an obvious purpose. Each card now works a full item in steps, not just a bare question -- walk through at least one aloud before moving on.",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L64);
})();

module.exports = { GR11_L64 };

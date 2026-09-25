// Grade 11 · Topic 6 · Lesson 6-4 — Logarithmic Functions
// FIKR lesson plan, Lesson plan 2026/27, differentiation activity, PBL task.
// Classwork is NOT requested this round (matching the pattern for L6-1/L6-3)
// — a minimal stub is supplied only so docs_engine's buildAll() does not
// throw; the resulting file is deleted after build and never delivered.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread as lessons_w6l4.js — see
// the standing alignment rule noted there.
const { buildAll } = require("./docs_engine");
const fs = require("fs");

const MATHDOC = "math_w6l4_doc/_index.json";
const GRAPH = "graphs_w6l4/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I applied the inverse steps in the right order before I converted to exponential form, and challenge any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to key features, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "Three teaching days this week. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR11 · T6 L6-4 · Logarithmic Functions
// =====================================================================
const GR11_L64 = {
  slug: "Gr11_T6_L6-4_Logarithmic_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Logarithmic Functions",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-4",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27",
  weekNum: "6",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-4 — Logarithmic Functions",
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
  vocabList: "inverse relationship ; logarithmic function",

  plan: {
    outcome: [
      "Students will state the domain, range, x-intercept, vertical asymptote, and end behavior of a logarithmic function.",
      "Students will use the two inverse properties — log_b(b^x) = x and b^(log_b x) = x — to analyze logarithmic and exponential functions together.",
      "Students will graph a logarithmic function including a horizontal or vertical shift, and write the inverse of an exponential or logarithmic function algebraically.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “The reflection that undoes it” — what an inverse function is, and why a logarithm is the exponential's reflection across y = x. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one exponential key-feature recall, one simple linear inverse.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): evaluate log_2 8; state the domain and range of g(x) = 2^x; find the inverse of f(x) = x + 5; decide true or false whether f⁻¹ is the reflection of f across y = x; state the horizontal asymptote of g(x) = 3^x − 2.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: log_2 8 = 3 ; domain all reals, range y > 0 ; f⁻¹(x) = x − 5 ; TRUE ; horizontal asymptote y = −2.",
    ],
    diagGap: [
      "Expected gap 1 — confusing “reflection across y = x” with “reflection across the x-axis” when asked about an inverse's graph.",
      "Expected gap 2 — swapping x and y correctly but then solving for the wrong variable, leaving the inverse half-finished.",
      "Expected gap 3 — Q5, which decides whether students can carry an exponential key feature (asymptote) into today's inverted version without being told it changes.",
      "Routing: 0–2 correct → re-teach inverses table.  3–4 → straight to key features.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): a logarithmic function is not a new shape to memorise from scratch — it is the exponential function's graph reflected across y = x, so every key feature can be PREDICTED from the exponential's, not re-derived.",
      "Whole class, IF.B.5 / IF.B.6 / IF.C.7.E: read f(x) = log_3 x's key features off its graph — domain x > 0, range all reals, x-intercept (1, 0), vertical asymptote x = 0, end behavior f→−∞ as x→0⁺ and f→∞ as x→∞.",
      "Whole class, BF.B.4 / (+)BF.B.4.C: the two inverse properties, log_b(b^x) = x and b^(log_b x) = x, checked numerically (log_2(2^5) = 5, 3^(log_3 7) = 7) and then used to explain WHY domain and range swap between a function and its inverse.",
      "Whole class, IF.C.9 / BF.B.3: graphing g(x) = log_2(x − 3) as a horizontal shift of the asymptote to x = 3, then finding the inverse of f(x) = log_3(x − 1) algebraically step by step — swap x and y, convert to exponential form, solve for y.",
      "Narration focus — swap x and y FIRST, before any other algebra, every single time; solving for the wrong variable is the single most common error on this skill.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: state the vertical asymptote and x-intercept of f(x) = log_5 x.",
      "Expected: vertical asymptote x = 0, x-intercept (1, 0). Watch for students who report a y-intercept (there is not one).",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time with a horizontal shift.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) f(x) = log_3 x — state the domain, range, vertical asymptote, and x-intercept.  (2) f(x) = log_2(x) + 4 — find the inverse function.",
      "Answers: (1) domain x > 0, range all reals, asymptote x = 0, x-intercept (1, 0). (2) swap: x = log_2(y) + 4 → x − 4 = log_2(y) → y = 2^(x−4), so f⁻¹(x) = 2^(x−4).",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four logarithmic functions with key features stated, one sketched with asymptote and x-intercept labelled, one inverse property verified numerically. Done when: every key feature stated matches the general rule for its function's shift.",
      "APPLY — Use it in context. Two inverse functions found algebraically, and a Red Sea desalination-plant pH context solved for the inverse relationship [H⁺] in terms of pH. Done when: every inverse is solved algebraically, and the real-world answer carries units (mol/L).",
      "INVESTIGATE — Find out why. Proving log_b(b^x) = x from the definition, explaining why a logarithmic function never has a y-intercept, and spotting the error in “log_b(x−h) and log_b(x)−h are the same shift.” Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A desalination plant on the Red Sea coast measures the hydrogen-ion concentration [H⁺] of its treated water and reports it as pH, using pH = −log₁₀[H⁺], where [H⁺] is measured in mol/L. This monitoring supports Vision 2030 water-security targets.",
      "(a) State the domain of the pH function in terms of [H⁺], and explain what that domain restriction means physically. (b) A sample has [H⁺] = 4 × 10⁻⁸ mol/L. Find its pH, to two decimal places. (c) Find the inverse function — write [H⁺] in terms of pH. (d) A technician says “the inverse function is pointless — we always measure [H⁺] directly anyway.” Explain in one sentence a situation where the inverse function is actually the useful direction.",
      "Answers: (a) [H⁺] > 0 — a hydrogen-ion concentration of zero or negative is not physically possible. (b) pH = −log₁₀(4×10⁻⁸) = −(log₁₀4 + log₁₀10⁻⁸) = −(0.602 − 8) ≈ 7.40. (c) pH = −log₁₀[H⁺] → −pH = log₁₀[H⁺] → [H⁺] = 10^(−pH). (d) the inverse direction is useful whenever an engineer is given a TARGET pH and needs to know what concentration to dose for, rather than measuring an existing sample.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the domain restriction stated as an inequality (not just described in words), the pH calculation shown with exact expressions before rounding, and the inverse solved algebraically with the correct sign.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. State the domain, range, vertical asymptote, and x-intercept of g(x) = log_2(x + 5). 2. Find the inverse of f(x) = log_4(x) − 1. 3. In ONE sentence, explain why a logarithmic function's graph never crosses its vertical asymptote.",
      "Answers: 1. domain x > −5, range all reals, vertical asymptote x = −5, x-intercept (−4, 0). 2. swap: x = log_4(y) − 1 → x + 1 = log_4(y) → y = 4^(x+1), so f⁻¹(x) = 4^(x+1). 3. the function is undefined at and beyond the asymptote's x-value — the domain never reaches it, so the curve can only approach, never cross.",
      "Done when: question 2 is a fully simplified inverse function, not left half-solved, and question 3 gives a definition-based reason, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their desalination-plant reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the domain restriction, the pH calculation, and the inverse function solved for [H⁺]; ONE worked non-example — dropping the negative sign when inverting pH — with a sentence on how a reader would spot it (a concentration greater than 1 mol/L, never realistic for treated water); and a caption on why an inverse function lets an engineer work backward from a report to a raw measurement.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which direction is still harder for you — reading key features straight off a graph, or solving algebraically for an inverse function?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four logarithmic functions with key features stated, one sketched with asymptote and x-intercept labelled; the five-feature checklist stays on the board and a partner is allowed. Done when: every key feature matches the general rule for its function's shift.",
      "APPLY — Use it in context. Two inverse functions found algebraically, and the Red Sea desalination pH context. Done when: every inverse is solved algebraically and the real-world answer carries units.",
      "INVESTIGATE — Find out why. The log_b(b^x)=x proof, the no-y-intercept argument, and the shift-versus-shift trap. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Red Sea desalination plant's pH monitoring, modelled with a logarithmic function and its inverse, supporting Vision 2030 water-security targets.",
      "In-class Apply-route item: the same pH context, solved for the inverse relationship and evaluated at a specific reading.",
      "Discussion prompt: why an engineer sometimes needs the inverse direction of a model — working backward from a target reading to the raw measurement that would produce it.",
    ],
    exams: [
      "SAAT (Tahsili) — domain and asymptote of a shifted logarithmic function, usually asked as reading a restriction directly off the function rule. Practice tip: set the argument of the log greater than zero and solve — that inequality IS the domain, every time.",
      "SAT — Advanced Math, writing the inverse of a logarithmic or exponential function algebraically is a recurring item type. Practice tip: swap x and y FIRST, before doing any algebra.",
      "GAT (Qudurat) — domain restrictions on a logarithmic expression under time pressure, usually a quick single-step inequality. Practice tip: don't solve the whole function — just set the inside of the log greater than zero.",
    ],
  },

  plan2026: {
    day: "Tuesday, Week 6", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Reading the Water” project task · squared paper",
    competencies: ["Reading domain, range, intercept, asymptote and end behavior off a logarithmic graph.", "Solving algebraically for the inverse of an exponential or logarithmic function."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders showing the exponential–logarithm reflection across y = x."],
    reallife: ["A Red Sea desalination plant's pH monitoring, part of Vision 2030 water-security targets.", "Converting a reported pH value back into a hydrogen-ion concentration for dosing calculations."],
    values: ["Precision — stating a domain restriction as an inequality, not a description.", "Working backward — recognising when the inverse direction of a model is the useful one."],
    soft: ["Collaboration in assigned group roles.", "Explaining why domain and range swap between a function and its inverse."],
    hard: ["Identifying and graphing the key features of a logarithmic function.", "Writing the inverse of an exponential or logarithmic function algebraically."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on evaluating a logarithm, exponential key features, a simple linear inverse, and the reflection property. Results read as a gap map; students routed to the re-teach table, straight to key features, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on the reflection-across-y=x idea for flagged students. Whole class: key features of a logarithmic function; the two inverse properties; graphing a shift and finding an inverse algebraically. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The Red Sea desalination plant's pH function: the domain restriction, the pH calculation, and the inverse function solved for [H⁺]. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — key features of a shifted logarithmic function, an inverse solved algebraically, and a one-sentence justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which direction is still harder for you — reading key features straight off a graph, or solving algebraically for an inverse function?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 6 · Lesson 6-5 — Properties of Logarithms. Clinic group: bring your Time to Check paper.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION A", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "m_ws1", t: "Evaluate." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Key features, and one property check", done: "every key feature you stated matches the general rule for its function's shift.",
        intro: "For each function, state the domain, range, vertical asymptote, and x-intercept.",
        grid: [["1.", "m_ws1"], ["2.", "m_ws2"], ["3.", "m_ws3"], ["4.", "m_ws4"], ["5.", "m_qc"], ["6.", "m_g1"]],
        tasks: ["7.  Sketch any one of the functions above, labelling its asymptote and x-intercept clearly."],
        lines: 2 },
      { note: "Inverses, and one Saudi context", done: "your inverse is solved algebraically (not guessed), and your final concentration answer carries units (mol/L).",
        graph: "gm_exp_log_inverse", graphW: 380,
        tasks: [
          "1.  Find the inverse of f(x) = log_2 x.",
          "2.  Find the inverse of g(x) = log_5(x) − 3.",
          "3.  A Red Sea desalination plant models water pH as pH = −log₁₀[H⁺]. Find the inverse relationship, writing [H⁺] in terms of pH.",
          "4.  Use your answer to Q3 to find [H⁺] when pH = 8.1, in mol/L.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument grounded in the definition, not just a computed answer.",
        tasks: [
          ["1.  Prove that ", { eq: "m_ip1_bare", k: 0.95 }, " for any base b and any real x — argue from what a logarithm means, not just by example."],
          "2.  Explain why a logarithmic function never has a y-intercept, using the definition of its domain.",
          "3.  A classmate says “log_b(x−h) and log_b(x)−h are the same shift.” Explain what's wrong, using the asymptote of each.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Reading the Water", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A desalination plant reports its water quality as a pH value. If an engineer is only given a TARGET pH, how do they work out what hydrogen-ion concentration that actually means?",
    situation: [
      "A Red Sea desalination plant models water pH as pH = −log₁₀[H⁺], where [H⁺] is the hydrogen-ion concentration in mol/L.",
      "This monitoring supports Vision 2030 water-security targets.",
      "A group of Grade 11 students is asked to build a quick-reference tool that goes both ways — concentration to pH, and pH back to concentration.",
    ],
    eq: "m_ctx1",
    steps: [
      ["1", "WRITE THE MODEL  (3 min)", "State the domain of the pH function in terms of [H⁺], and explain what that restriction means physically."],
      ["2", "CONVERT FORWARD  (4 min)", "A sample has [H⁺] = 4 × 10⁻⁸ mol/L. Find its pH, to two decimal places."],
      ["3", "FIND THE INVERSE  (5 min)", "Solve pH = −log₁₀[H⁺] for [H⁺] — show every algebra step."],
      ["4", "CONVERT BACKWARD  (4 min)", "Use your inverse to find [H⁺] when pH = 8.1 (slightly basic, typical of treated seawater)."],
      ["5", "PRESENT  (4 min)", "One sentence: when would an engineer actually need the backward (inverse) direction?"],
    ],
    working: [["Step 1 — the domain and what it means:", 2], ["Step 2 — the forward pH calculation:", 3],
              ["Step 3 — the inverse, worked out:", 4], ["Step 4 — the backward calculation:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the pH model", "Calculator — runs the forward and backward conversions", "Checker — verifies the inverse algebraically", "Presenter — says the sentence"],
    doneWhen: ["The domain restriction is written as an inequality, not just described.", "The inverse is solved algebraically, with the sign checked.", "Both conversions carry the correct units (mol/L or no units for pH).", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR11_L64);
  const cwFile = `Classwork_${GR11_L64.slug}.docx`;
  if (fs.existsSync(cwFile)) fs.unlinkSync(cwFile);
})();

module.exports = { GR11_L64 };

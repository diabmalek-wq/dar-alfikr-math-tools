// Week 6 · Gr11 · T6 L6-4 Logarithmic Functions — derived from lessons_w6l4.js (the deck).
const { ASSESS, T, AI_CRITIC, PILLAR_ADAPTIVE, WEEK_NOTE, PHASE_STD, STUB } = require("./wk6_common");

const GR11_L64 = {
  slug: "Wk6_Gr11_T6_L6-4_Logarithmic_Functions",
  mathDocIndex: "math_wk6_doc/_index.json", graphIndex: "graphs_wk6/_index.json", timings: T,
  lessonTitle: "Logarithmic Functions",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-4",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27", weekNum: "6",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-4 — Logarithmic Functions",
  codes: ["HSF.IF.B.5", "HSF.IF.B.6", "HSF.IF.C.7.E", "HSF.IF.C.9", "HSF.BF.B.3", "HSF.BF.B.4", "HSF.BF.B.4.C"], mps: ["MP.4", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Identify key features of logarithmic functions.",
    "Use inverse properties to analyze logarithmic and exponential functions.",
    "Graph logarithmic functions and interpret their key features.",
    "Write and interpret the inverses of exponential and logarithmic functions.",
  ],
  essentialQuestion: "How is the relationship between logarithmic and exponential functions revealed in the features of their graphs?",
  vocabList: "inverse relationship ; logarithmic function",

  plan: {
    outcome: [
      "Students will state the domain, range, x-intercept, asymptote and end behaviour of a logarithmic function, and compare its average rate of change over different intervals (objective 1; HSF.IF.B.6).",
      "Students will write the inverse of an exponential function and of a logarithmic function by swapping inputs and outputs, and read inverse values from a table or graph (objectives 2 and 4; HSF.BF.B.4.C).",
      "Students will graph y = log_b(x − h) + k, moving the asymptote and key points with the shift (objective 3).",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Every exponential has a mirror image” — swapping the columns of a table of 3ˣ. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one evaluation of a logarithm, one reading of an inverse value from a table.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes) — the slide-5 warm-up: log₃ 81 ; log₂(1/8) ; f(x) = 3ˣ, find f(3) ; which input gives an output of 9 ; try to solve 3ˣ = 0 and say what happens.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: 4 ; −3 ; 27 ; x = 2 ; no solution, because 3ˣ is always positive — which is why the graph of 3ˣ has asymptote y = 0 and why a logarithm has domain x > 0.",
    ],
    diagGap: [
      "Expected gap 1 — evaluating or converting a logarithm (Lesson 6-3); if questions 1–3 fail, the lesson stalls.",
      "Expected gap 2 — Q5: students expect “3ˣ = 0” to have an answer. The “no solution” discussion is the entry to the domain of the logarithm.",
      "Routing: 0–2 correct → re-teach converting between forms with the teacher.  3–4 → straight to the graphs.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Slide 6 — Exponential and logarithmic functions are inverses (objectives 2 and 4). Swap x and y, then solve. Table of f(x) = 3ˣ: x = −1, 0, 1, 2 gives 1/3, 1, 3, 9; swap the columns for f⁻¹. Reading f⁻¹(9): find 9 in the OUTPUT column of f and read the input, 2. The pairs (0, 1) ↔ (1, 0), (1, 3) ↔ (3, 1), (2, 9) ↔ (9, 2) mirror across y = x. Say aloud: f⁻¹(x) is not 1/f(x).",
      "Slide 7 — Key features of f(x) = log₃ x (objectives 1 and 3; IF.B.6). Domain x > 0; range all reals; x-intercept (1, 0), no y-intercept; vertical asymptote x = 0; f → −∞ as x → 0⁺ and f → ∞ slowly as x → ∞. Average rate of change: [1, 3] is 1/2, [3, 9] is 1/6, [9, 27] is 1/18 — each interval triples, the output rises by exactly 1, so the rate falls.",
      "Slide 8 — Graphing transformations (objective 3). g(x) = log₃(x − 2) + 1: right 2, up 1; asymptote moves x = 0 → x = 2; domain x > 2; key points (1, 0) → (3, 1), (3, 1) → (5, 2), (9, 2) → (11, 3). Check g(5) = log₃ 3 + 1 = 2.",
      "Narration focus — the argument of a logarithm must stay positive: solve it > 0 first, then the asymptote is where the argument equals 0.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: write the inverse of f(x) = 3ˣ.",
      "Expected: f⁻¹(x) = log₃ x. Watch for 1/3ˣ (treating −1 as a reciprocal) and for swapped base and argument.",
      "80% correct → release guided practice. Below 80% → one more modelled example with a different base.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) Find the inverse of f(x) = 2ˣ, then check with f(3) = 8.  (2) Use the table of f (x = 0, 1, 2, 3 gives 1, 5, 25, 125) to find f⁻¹(25) and f⁻¹(125).",
      "Answers: (1) f⁻¹(x) = log₂ x; f(3) = 8 so log₂ 8 = 3.  (2) f⁻¹(25) = 2 and f⁻¹(125) = 3 — find the output in the table and read the input.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Inverses of 4ˣ and log₅ x; features of y = log₂ x; reading f⁻¹(16) and f⁻¹(32) from a table; a sketch with asymptote and three labelled points. Done when: each inverse composes back to x, and your sketch shows the asymptote and three labelled points.",
      "APPLY — Use it in context. Sketch log₂(x + 3) with asymptote, domain and key points; average rate of change of log₂ x on [1, 4] and [4, 16]; a Vision 2030 solar-farm model inverted. Done when: the asymptote is written as an equation, and the answer to the context question carries units (years).",
      "INVESTIGATE — Find out why. Why log₃ x never touches the y-axis; comparing function B (a table) with A(x) = log₃ x (objective 3, HSF.IF.C.9); why the average rate of change falls. Done when: each argument uses the inverse relationship, not just a calculation.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice (slide 14).",
      "A classroom model for a Vision 2030 solar farm says its output triples every 5 years from 10 MW: P = 10·3^(t/5), t in years. The model is invented for practice, not a forecast.",
      "(a) Complete the table for t = 0, 5, 10, 15 and read when P = 270 MW. (b) Write the inverse t(P) and state its domain. (c) Find t when P = 50 MW, to one decimal place. (d) Find the average rate of change of t on [10, 30] and on [90, 270] (years per MW) and say what it means for planners.",
      "Answers: (a) P = 10, 30, 90, 270, so P = 270 at t = 15. (b) t = 5 log₃(P/10), domain P > 0. (c) t = 5 log₃ 5 ≈ 7.3 years. (d) 1/4 year per MW on [10, 30]; 1/36 year per MW on [90, 270] — each extra MW takes less time as the farm grows; the inverse flattens.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the table read before the inverse is used, exact expressions before decimals, and units (MW, years) in every answer.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Write the inverse of the function shown (f(x) = 5ˣ). 2. State the domain and the asymptote of y = log₅ x. 3. Use f(2) = 25 to find f⁻¹(25), and say what the point (25, 2) tells you about the graph of f⁻¹.",
      "Answers: 1. f⁻¹(x) = log₅ x. 2. domain x > 0; asymptote x = 0. 3. f⁻¹(25) = 2; (25, 2) lies on f⁻¹ — it is the mirror image of (2, 25) on f.",
      "Done when: answers are exact and question 3 gives the value AND the meaning of the point.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their solar-farm reasoning using the AI critique and the teacher’s micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the table, the inverse t(P), and the time for one new target output; ONE worked non-example — reading f⁻¹(9) as the reciprocal of f(9) — with a sentence on what that wrong answer actually computes; and a caption on why planners need time as a function of output.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which is harder for you — reading an inverse value from a table, or writing the inverse as a formula?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Inverses of 4ˣ and log₅ x, features of log₂ x, inverse values from a table, and a sketch. Done when: each inverse composes back to x.",
      "APPLY — Use it in context. log₂(x + 3) sketched, two average rates of change, and the solar-farm inverse. Done when: the asymptote is an equation and the answer carries years.",
      "INVESTIGATE — Find out why. The asymptote argument, function A against function B, and why the rate of change falls. Done when: each argument uses the inverse relationship.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production and project context: a Vision 2030 solar farm (an invented classroom model) whose output triples every 5 years — time as a function of output.",
      "Discussion prompt: why planners need time as a function of output, not just output as a function of time.",
    ],
    exams: [
      "SAAT (Tahsili) — domain of f(x) = log₃(x − 1) + 2 is x > 1: the argument must be positive and the +2 does not change the domain. No calculator.",
      "SAT — Advanced Math: f(x) = 2·3ˣ, find f⁻¹(18). Divide by 2, 3ˣ = 9, so 2. Name the trap: stopping at 9.",
      "GAT (Qudurat) — compare log₃ 50 and log₅ 50 by bracketing: 3 to 4 against 2 to 3. A bigger base does not give a bigger logarithm of the same number.",
    ],
  },

  plan2026: {
    day: "Week 6 · day per timetable", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Time as a Function of Output” project task (A3) · squared paper",
    competencies: ["Writing and interpreting the inverse of an exponential or logarithmic function.", "Reading domain, range, intercept and asymptote of a logarithmic function and its transformations."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders on b, h and k: watch the asymptote and key points move, and A and B mirror across y = x."],
    reallife: ["A solar farm whose output triples every 5 years: when does it reach a target?", "Planners who need time as a function of output."],
    values: ["Precision — keeping the argument of a logarithm positive.", "Long-term planning — using inverses to plan for national targets."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a graph and its inverse mirror, in words."],
    hard: ["Writing inverses; graphing and transforming logarithmic functions.", "Computing and interpreting an average rate of change."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on logarithms, evaluating 3ˣ and the 3ˣ = 0 question. Results read as a gap map; students routed to the re-teach table, straight to the graphs, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Re-teach converting forms for flagged students. Whole class: inverses and tables; key features and average rate of change; transformations. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The solar-farm model: table, inverse, new target, two average rates of change. AI used as critic only. Extended in the A3 project task.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — inverse, domain and asymptote, and the meaning of a point on f⁻¹. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: PHASE_STD.assessment,
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is harder for you — reading an inverse value from a table, or writing the inverse as a formula?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 6 · Lesson 6-5 — Properties of Logarithms. Clinic group: bring your Time to Check paper.",
  },

  classwork: STUB("k_l4a"),

  diffSheet: {
    routes: [
      { note: "Swap it, read it, sketch it", done: "each inverse composes back to x, and your sketch shows the asymptote and three labelled points.",
        intro: "Items 1–3: write the inverse function, then check one value. Items 4–6 below.",
        grid: [["1.", "k_l4a"], ["2.", "k_l4b"], ["3.", "k_l4c"]],
        tasks: [
          "4.  For y = log₂ x state the domain, the range, the x-intercept and the asymptote.",
          "5.  Table of f(x) = 2ˣ. Use it to read f⁻¹(16) and f⁻¹(32).",
          { table: [["x", "0", "1", "2", "3", "4", "5"], ["f(x)", "1", "2", "4", "8", "16", "32"]] },
          "6.  Sketch y = log₂ x through (1, 0), (2, 1) and (4, 2). Draw its asymptote as a dashed line and label it.",
          { graph: "k_grid", w: 270 },
        ], lines: 2 },
      { note: "Shift it, rate it, and one real context", done: "the asymptote is written as an equation, and the answer to the context question carries units (years).",
        tasks: [
          "1.  Sketch g(x) = log₂(x + 3). Give the asymptote as an equation, the domain, and two key points.",
          { graph: "k_grid", w: 235 },
          "2.  Find the average rate of change of y = log₂ x on [1, 4] and on [4, 16]. Say why they differ.",
          ["3.  A Vision 2030 solar-farm model (invented for practice) says output is ", { eq: "k_l4p", k: 1.0 }, " MW after t years. Write t as a function of P, then find t when P = 90."],
        ], lines: 3 },
      { note: "Arguments, not answers", done: "each argument uses the inverse relationship, not just a calculation.",
        tasks: [
          "1.  Explain why the graph of y = log₃ x can never touch the y-axis, using the graph of 3ˣ.",
          ["2.  Function B is given by the table x = 3, 5, 11 and B(x) = 1, 2, 3. Compare it with ", { eq: "k_a3", k: 1.0 }, ": which is larger at x = 11, and which transformation of A gives B?"],
          "3.  Explain why the average rate of change of log₃ x falls from [1, 3] to [3, 9], using what you know about 3ˣ.",
        ], lines: 3 },
    ],
  },

  pbl: {
    title: "Time as a Function of Output", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "Planners know the solar farm’s output grows by the same factor every 5 years. How long until it reaches a target — and why does each extra MW take less time as the farm grows?",
    situation: [
      "A classroom model (invented for practice, not a forecast): a solar farm starts at 10 MW and triples every 5 years.",
      "Planners want time as a function of output — the inverse of the model.",
      "Each group answers for two new targets: 50 MW and 100 MW.",
    ],
    eq: "k_l4p",
    data: [["t (years)", "0", "5", "10", "15"], ["P (MW)", "", "", "", ""]],
    steps: [
      ["1", "FILL THE TABLE  (4 min)", "Complete P for t = 0, 5, 10 and 15 using the model, with one calculation shown."],
      ["2", "SWAP IT  (4 min)", "Write the inverse t(P) and state its domain. Read t when P = 90 from the table, then confirm with your formula."],
      ["3", "NEW TARGETS  (5 min)", "Use t(P) to find the time to reach 50 MW and 100 MW, to one decimal place, with units. Show the exact expression first."],
      ["4", "READ THE RATES  (4 min)", "Find the average rate of change of t on [10, 30] and on [90, 270] in years per MW. What does the fall mean for planners?"],
      ["5", "PRESENT  (3 min)", "One sentence for the planners: why does each extra MW take less time to add as the farm grows, in terms of the inverse?"],
    ],
    working: [["Step 1 — the table, one calculation:", 3], ["Step 2 — the inverse and the check at P = 90:", 3],
              ["Step 3 — exact expressions, then decimals:", 4], ["Step 4 — the two average rates of change:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the model and the targets", "Calculator — fills the table and the decimals", "Checker — swaps back to confirm each inverse value", "Presenter — says the sentence"],
    doneWhen: ["Every inverse value is checked by substituting it into P(t).", "The exact expression is written before the decimal.", "Units (MW, years, years per MW) appear in every answer.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};
module.exports = { GR11_L64 };

// Week 6 · Gr10 · T2 L2-3 Factored Form — derived from lessons_g10q3.js.
const { ASSESS, T, AI_CRITIC, PILLAR_ADAPTIVE, WEEK_NOTE, PHASE_STD, STUB } = require("./wk6_common");

const GR10_L23 = {
  slug: "Wk6_Gr10_T2_L2-3_Factored_Form",
  mathDocIndex: "math_wk6_doc/_index.json", graphIndex: "graphs_wk6/_index.json", timings: T,
  lessonTitle: "Factored Form of a Quadratic Function",
  unit: "Topic 2 — Quadratic Functions and Equations · Lesson 2-3",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27", weekNum: "6",
  lessonLine: "Grade 10 · Algebra II · Topic 2: Quadratic Functions and Equations · Lesson 2-3 — Factored Form of a Quadratic Function",
  codes: ["HSA.SSE.A.1.B", "HSA.SSE.B.3.A", "HSA.APR.B.3", "HSF.IF.C.7", "HSF.IF.C.7.A", "HSA.SSE.A.2", "HSF.IF.C.8.A"], mps: [],
  assessments: ASSESS,
  objectives: [
    "Solve quadratic equations by factoring.",
    "Find the zeros of a quadratic function by factoring.",
    "Determine the intervals where a quadratic function is positive or negative.",
  ],
  essentialQuestion: null,
  vocabList: "factored form ; negative interval ; positive interval ; x-intercepts ; zeros (of a quadratic function) ; zero-product property",

  plan: {
    outcome: [
      "Students will solve a quadratic equation by factoring and the zero-product property (objective 1).",
      "Students will find the zeros of a quadratic function from factored form and write them as x-intercepts, then read the axis, vertex and y-intercept (objective 2).",
      "Students will state where a quadratic function is positive or negative as intervals (objective 3).",
      "The curriculum map’s Essential Question and Math Practices columns for Topic 2 were not in the project text; they are left open, not invented.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Multiply, then reverse” — (x + 2)(x + 3) expanded and factored back. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one expansion, one factor-pair question.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes) — the slide-5 warm-up: expand (x + 2)(x − 5) ; evaluate (x − 2)(x + 4) at x = 2 ; what must be true if a·b = 0 ; factor x² + 5x + 6 ; the axis of x² − 2x − 3 using −b/(2a).",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: x² − 3x − 10 ; 0, so x = 2 is a zero and (2, 0) is on the graph ; a = 0 or b = 0 ; (x + 2)(x + 3) ; x = 1.",
    ],
    diagGap: [
      "Expected gap 1 — expanding two binomials and factoring a trinomial (questions 1 and 4); slow down on the prior-knowledge slide if these fail.",
      "Expected gap 2 — Q3: stating the zero-product property in words; students often say “a and b are zero”.",
      "Routing: 0–2 correct → re-teach multiplying and factoring with the teacher.  3–4 → straight to factored form.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Slide 7 — Factored form: read the zeros (objective 2). f(x) = (x + 1)(x − 3): zeros −1 and 3, axis x = (p + q)/2 = 1, vertex f(1) = −4, y-intercept f(0) = −3. Say aloud: the zero of (x + 1) is −1, not 1.",
      "Slide 8 — Solve by factoring: the zero-product property (objectives 1 and 2). x² − 2x − 3 = 0 → (x + 1)(x − 3) = 0 → x = −1 or x = 3. Factor pair: product −3, sum −2. Say aloud: the equation must equal ZERO before factoring.",
      "Slide 9 — Positive and negative intervals (objective 3). Zeros −1 and 3 cut the axis into three intervals. Test points: f(−2) = 5, f(0) = −3, f(4) = 5. Positive: x < −1 or x > 3; negative: −1 < x < 3. The zeros themselves are neither.",
      "Narration focus — set each bracket to zero and mind the sign inside the bracket; use “or” for the two outside intervals, never “and”.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: state the zeros of f(x) = (x − 4)(x + 2).",
      "Expected: 4 and −2. Watch for 4 and 2.",
      "80% correct → release guided practice. Below 80% → one more modelled example with a plus sign inside a bracket.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) Solve x² + 5x + 6 = 0 by factoring and check one solution by substitution.  (2) f(x) = (x − 1)(x − 5): state the zeros, then the interval where f(x) is negative.",
      "Answers: (1) (x + 2)(x + 3) = 0, x = −2 or x = −3; check (−2)² + 5(−2) + 6 = 0.  (2) zeros 1 and 5; negative for 1 < x < 5.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Zeros and x-intercepts from factored form; equations solved by factoring and checked; axis, vertex and y-intercept of (x + 3)(x − 2); where it is positive and negative. Done when: each solution is checked by substitution, and each interval is written with the right inequality signs.",
      "APPLY — Use it in context. Function from zeros −2 and 4 through (0, −16); 2x² − 2x − 12 = 0 and where it is negative; a ball thrown from 0 m landing at 6 m, 9 m high at 3 m. Done when: your function is checked by substituting a point, and every answer carries a sentence in context.",
      "INVESTIGATE — Find out why. Why the axis is (p + q)/2; the error in solving (x − 2)(x − 3) = 6; why zeros lie in neither interval. Done when: you have an argument grounded in the zero-product property or in the graph, not just a computed answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice (slide 14).",
      "A footbridge arch on the Jeddah Corniche touches the ground at two points 8 m apart and is 4 m high in the middle; x is measured along the ground from the left foot (an invented classroom model).",
      "(a) Write h(x) in factored form using the zeros 0 and 8 and the top point (4, 4). (b) State the interval where h(x) > 0 and what it means. (c) Find the height 2 m from the left foot. (d) Find where the arch is 3 m high.",
      "Answers: (a) a·x(x − 8), with h(4) = 4: −16a = 4, a = −1/4, so h(x) = −(1/4)x(x − 8). (b) 0 < x < 8: the arch is above the ground between its feet. (c) h(2) = −(1/4)(2)(−6) = 3 m. (d) −(1/4)x(x − 8) = 3 gives x² − 8x + 12 = 0, so x = 2 or x = 6.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the zeros used before a is found, exact fractions before decimals, and units (metres) in every answer.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Write the function with zeros −3 and 1 through (0, 6) in factored form. 2. Solve x² − x − 12 = 0 by factoring. 3. In ONE sentence, say where f(x) = (x + 2)(x − 5) is negative and how you know.",
      "Answers: 1. a(3)(−1) = 6 gives a = −2: f(x) = −2(x + 3)(x − 1). 2. (x − 4)(x + 3) = 0, so x = 4 or x = −3. 3. Negative for −2 < x < 5, because a > 0 and the graph lies below the axis between its zeros.",
      "Done when: answers are exact and question 3 is a sentence with an interval, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their arch reasoning using the AI critique and the teacher’s micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the arch in factored form and expanded form, the interval above the ground, and the 3 m points; ONE worked non-example — solving (x − 2)(x − 3) = 6 as x = 8 or x = 9 — and what goes wrong (it is not a product equal to zero: the true solutions are 0 and 5); and a caption on why an engineer needs to know where an arch meets the ground.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 2 modelling set.",
      "Reflection question: “Which is easier for you — reading the zeros from factored form, or finding them from standard form?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Zeros, solutions by factoring, the axis, vertex and y-intercept, and the intervals for (x + 3)(x − 2). Done when: each solution is checked by substitution.",
      "APPLY — Use it in context. A function from zeros and a point, 2x² − 2x − 12 = 0, and the ball. Done when: the function is checked by substituting a point.",
      "INVESTIGATE — Find out why. The axis formula, the (x − 2)(x − 3) = 6 error, and why zeros lie in neither interval. Done when: the argument rests on the zero-product property or the graph.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production and project context: a footbridge arch on the Jeddah Corniche (invented model), then two arches compared for headroom in the A3 task.",
      "Apply-route item: a ball’s flight modelled from its zeros and top point.",
      "Discussion prompt: why an engineer needs to know where an arch meets the ground and how much of it has enough headroom.",
    ],
    exams: [
      "SAAT (Tahsili) — sum of the solutions of x² − 5x + 6 = 0 is 5. No calculator. Name the trap: the product, 6.",
      "SAT — Advanced Math: x-intercepts (−3, 0), (5, 0) through (1, −32) gives y = 2(x + 3)(x − 5). Name the trap: forgetting a.",
      "GAT (Qudurat) — larger solution of x² − x − 6 = 0 against 3: the solutions are 3 and −2, so they are equal. About 75 seconds, no calculator.",
    ],
  },

  plan2026: {
    day: "Week 6 · day per timetable", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Two Arches, One Walkway” project task (A3) · squared paper",
    competencies: ["Reading zeros, axis, vertex and y-intercept from factored form.", "Solving a quadratic equation by factoring and stating where the function is positive or negative."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders on a, p and q, and f(x) > 0 to shade the positive intervals."],
    reallife: ["A footbridge arch on the Jeddah Corniche, modelled as a parabola.", "Headroom along a walkway under an arch."],
    values: ["Precision — setting each bracket to zero and reading the sign.", "Safety by design — checking clearance before building."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a solution must come from a product equal to zero."],
    hard: ["Factoring a quadratic and applying the zero-product property.", "Writing intervals of positive and negative values."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz: expand, evaluate at a zero, the zero-product idea, factor a trinomial, the axis. Results read as a gap map; students routed to the re-teach table, straight to factored form, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Re-teach multiplying and factoring for flagged students. Whole class: factored form and zeros; solving by factoring; positive and negative intervals. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The footbridge arch: factored form, interval, height at 2 m, and the 3 m points. AI used as critic only. Extended in the A3 project task.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — factored form from zeros and a point, solve by factoring, and a sentence with an interval. No notes, no partner, no AI.",
      "FIKR Phase 6 — Smart Production. Students refine their reasoning into a final product including one worked non-example, and publish to the LMS portfolio.",
    ],
    assessment: PHASE_STD.assessment,
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is easier for you — reading the zeros from factored form, or finding them from standard form?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 2 · Lesson 2-4 — Overview of Complex Numbers. Clinic group: bring your Time to Check paper.",
  },

  classwork: STUB("k_r1"),

  diffSheet: {
    routes: [
      { note: "Factor it, solve it, check it", done: "each solution is checked by substitution, and each interval is written with the right inequality signs.",
        intro: "Items 1, 4, 6: state the zeros and the x-intercepts. Items 2, 3, 5: solve by factoring and check one solution by substitution.",
        grid: [["1.", "k_r1"], ["2.", "k_r2"], ["3.", "k_r3"], ["4.", "k_r4"], ["5.", "k_r5"], ["6.", "k_r6"]],
        tasks: [
          "7.  For f(x) = (x + 3)(x − 2) find the axis of symmetry, the vertex and the y-intercept.",
          "8.  Where is f(x) = (x + 3)(x − 2) positive? Where is it negative? Write each as an interval, using “or” where needed.",
        ], lines: 3 },
      { note: "Build it, solve it, test it", done: "your function is checked by substituting a point, and every answer carries a sentence in context.",
        tasks: [
          "1.  Write the function with zeros −2 and 4 that passes through (0, −16).",
          "2.  Factor and solve 2x² − 2x − 12 = 0, then say where f(x) = 2x² − 2x − 12 is negative.",
          "3.  A ball is on the ground at 0 m and at 6 m horizontally and is 9 m high at 3 m. Write its height function in factored form and check it with a fourth point of your own.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument grounded in the zero-product property or in the graph, not just a computed answer.",
        tasks: [
          ["1.  Show that for ", { eq: "k_rdef", k: 0.95 }, " the axis is x = (p + q)/2, by the symmetry of the zeros."],
          ["2.  A student solves ", { eq: "k_rtrap", k: 0.95 }, " by writing x − 2 = 6 or x − 3 = 6. Explain the error, then solve it correctly."],
          "3.  Explain why the zeros are never in the positive or the negative interval, using a graph.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Two Arches, One Walkway", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "Two arches could carry a Corniche walkway. A walkway needs at least 3 m of headroom — which arch gives the wider clear walkway, and how can factored form tell you exactly?",
    situation: [
      "Arch A touches the ground at two points 8 m apart and is 4 m high at its middle: zeros 0 and 8, top (4, 4).",
      "Arch B touches the ground at two points 12 m apart and is 5.4 m high at its middle: zeros 0 and 12, top (6, 5.4).",
      "Measure x along the ground from the left foot. This is an invented classroom model; heights and distances are in metres.",
    ],
    eq: "k_ra",
    steps: [
      ["1", "WRITE BOTH ARCHES  (4 min)", "Arch A is given above. Write Arch B in factored form using its zeros and top point. Find a and check by substitution."],
      ["2", "ZEROS AND INTERVALS  (4 min)", "State each arch’s zeros, axis and the interval where its height is positive. What does that interval mean for the walkway?"],
      ["3", "FIND THE HEADROOM  (6 min)", "Set each height equal to 3 and solve by factoring. For each arch give the x-values where the height is 3 m, and the clear width where it is at least 3 m."],
      ["4", "TEST A SHORTCUT  (3 min)", "A student solves −(1/4)x(x − 8) = 3 by writing x = 3 or x − 8 = 3. Explain why this is wrong."],
      ["5", "PRESENT  (3 min)", "One sentence: a market stall is 6 m wide and needs 3 m of headroom. Which arch lets it through, and how do you know?"],
    ],
    working: [["Step 1 — Arch B in factored form:", 3], ["Step 2 — zeros, axes and intervals:", 3],
              ["Step 3 — both equations factored and solved:", 5], ["Step 4 — why the shortcut fails:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two arches", "Calculator — finds a and the heights", "Checker — substitutes each solution back", "Presenter — says the sentence"],
    doneWhen: ["Each function is checked by substituting a known point.", "Each equation is set equal to zero before factoring.", "Units (metres) appear in every answer.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};
module.exports = { GR10_L23 };

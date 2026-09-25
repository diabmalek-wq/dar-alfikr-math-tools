// Week 5 core lesson documents — FIKR plan, Lesson plan 2026/27,
// differentiation activity, PBL task. Classwork is NOT requested this round
// (per the Weekly Work Order for this build) — a minimal stub is supplied
// only so docs_engine's buildAll() does not throw; the resulting file is
// deleted after build and never delivered.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum map.
const { buildAll } = require("./docs_engine");
const fs = require("fs");

const MATHDOC = "math_w5core_doc/_index.json";
const GRAPH = "graphs_w5core/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Challenge my reasoning and point out any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to modelling, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "Three teaching days this week. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR10 · T1 L5 · Solving Equations and Inequalities by Graphing
// =====================================================================
const GR10_L5 = {
  slug: "Gr10_T1_L5_Solving_Equations_and_Inequalities_by_Graphing",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Solving Equations and Inequalities by Graphing",
  unit: "Topic 1 — Linear Functions · Lesson 5",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 5 · Semester 1, 2026–27",
  weekNum: "5",
  lessonLine: "Grade 10 · Algebra II · Topic 1: Linear Functions · Lesson 5 — Solving Equations and Inequalities by Graphing",
  codes: ["HSA.CED.A.1", "HSA.REI.D.11"],
  mps: ["MP.2", "MP.5"],
  assessments: ASSESS,
  objectives: [
    "Solve equations graphically.",
    "Solve inequalities graphically.",
    "Use tables to approximate solutions of equations.",
  ],
  essentialQuestion: "How can graphing be used to find solutions to equations and inequalities?",
  vocabList: "graphical solution ; solution set",

  plan: {
    outcome: [
      "Students will solve an equation by graphing both sides and reading the x-coordinate of the intersection.",
      "Students will solve a strict or non-strict inequality graphically and write the solution set properly.",
      "Students will use a table to trap and narrow an approximate solution that is not a whole number.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Where two graphs agree” — solving a linear equation by graphing both sides. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one intersection read off a graph, one function evaluation.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): where 2x − 3 = −x + 9 meets; evaluating f(x) = 3x − 1 at x = 2; testing x = 3 in 2x − 1 > x + 2; bracketing a root of g(x) = x² − 5 between two integers; reading a solution off two short tables.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: x = 4 ; f(2) = 5 ; no (both sides equal 5 at x = 3, so the STRICT inequality fails) ; root between 2 and 3 ; f(x) = g(x) at x = 2.",
    ],
    diagGap: [
      "Expected gap 1 — reporting the y-coordinate of an intersection point as if it were the solution, instead of the x-coordinate.",
      "Expected gap 2 — testing a boundary point in a STRICT inequality and calling it a solution because the two sides are merely close, not checking they are actually unequal.",
      "Expected gap 3 — Q4 and Q5, which decide whether the bracket-and-narrow table method lands later in the lesson.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to graphing systems.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): the equation asks for the SHARED INPUT (x), not the shared output (y) — say it, write it, and point at both coordinates of a worked intersection point.",
      "Whole class, CED.A.1: graph y = 3x − 2 and y = −x + 6 together; they cross at (2, 4), so x = 2. Check by substitution in both sides.",
      "Whole class, REI.D.11: the same two lines, this time asked as an inequality — 3x − 2 > −x + 6 has solution x > 2, because the teal line sits above the maroon line exactly when x > 2. The solution SET is written {x : x > 2}, not just the number 2.",
      "Whole class, REI.D.11 (tables): x² = 2x + 1 has no whole-number solution. Build a table of x² − (2x + 1) near x = 2 and x = 3; the sign changes, so a root is trapped between them; narrowing to x = 2.4 and x = 2.5 gives x ≈ 2.4.",
      "Narration focus — do the sign-change bracketing with the actual numbers BEFORE naming it as a method. A table narrows a bracket; it does not guess.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: find where 4x − 1 = −2x + 11 meet — solve for x.",
      "Expected: x = 2 (and y = 7, though only x was asked for). Watch for students who solve for y and report that as the answer.",
      "80% correct → release guided practice. Below 80% → one further modelled example, graphed slowly, line by line.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) 3x − 2 = −2x + 8 — solve by graphing or algebra, then check in both sides.  (2) x² − 4x + 1 = 0 — use a table to approximate the positive solution to one decimal place.",
      "Answers: (1) x = 2, checked: 3(2)−2=4, −2(2)+8=4. (2) exact value 2+√3 ≈ 3.732; table shows h(3.7) = −0.11, h(3.8) = +0.24, so x ≈ 3.7 to one decimal place.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four equations solved by graphing, each pair graphed and its intersection marked, one answer verified by substitution. Done when: your x-value makes both sides equal when you substitute it back in.",
      "APPLY — Use it in context. A strict inequality solved and written as a set, two ride-hailing apps compared graphically to find their crossover distance in SAR and km, and a table-approximated quadratic root. Done when: your inequality answer is a set, not a point, and your Saudi-context answer carries both SAR and km.",
      "INVESTIGATE — Find out why. Why the x-coordinate answers the equation and the y-coordinate does not; what parallel lines mean for the number of solutions; what a quadratic-and-line system with two crossings means for a table approximation. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "Two ride-hailing apps price a trip around Jeddah differently. App A charges a 5 SAR flag fall plus 2 SAR per kilometre. App B charges a 15 SAR flag fall plus 1 SAR per kilometre.",
      "(a) Write both cost functions, C_A(d) and C_B(d). (b) Graph both and find the exact crossover distance and price. (c) Which app is cheaper for a 6 km trip, and for a 14 km trip? Use the graph. (d) A friend says “just pick the lower flag fall — it'll always be cheaper.” Explain in one sentence why the friend is wrong.",
      "Answers: (a) C_A(d) = 5 + 2d, C_B(d) = 15 + d. (b) crossover at d = 10 km, price 25 SAR. (c) at 6 km App A is cheaper (17 vs 21 SAR); at 14 km App B is cheaper (33 vs 29 SAR). (d) the friend ignored the per-kilometre RATE, which decides which app wins past the crossover distance.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: both cost functions written correctly, the crossover found exactly (not just estimated from the picture), and every real-world answer in SAR and km.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Find the solution shown by a graph of two lines. 2. Use a table to approximate, to one decimal place, the positive solution of x² − 3x − 1 = 0. 3. In ONE sentence, explain why the x-coordinate of an intersection point solves the equation, but the y-coordinate does not.",
      "Answers: 1. the two lines meet at x = 2. 2. exact value (3+√13)/2 ≈ 3.303; table shows h(3.3) = −0.01, h(3.31) = +0.03, so x ≈ 3.3. 3. the x-value is the shared input where both functions agree, which is what f(x) = g(x) asks for; the y-value is just the common output.",
      "Done when: the answer to Q1 is exact, the table for Q2 is shown, and Q3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their ride-app reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: both cost functions, the exact crossover distance and price, and the 6 km / 14 km comparison; ONE worked non-example — “always pick the lower flag fall” — with a sentence on how a reader would spot the error; and a caption on why the cheaper app depends on distance.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 1 modelling set.",
      "Reflection question: “Which still catches you out — reading x instead of y off the graph, or trusting a table to be exact?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four equations solved by graphing, intersections marked, one verified by substitution; the worked example stays on the board and a partner is allowed. Done when: the x-value makes both sides equal when substituted back in.",
      "APPLY — Use it in context. A strict inequality written as a set, the ride-app crossover in SAR and km, and a table-approximated quadratic root. Done when: the inequality answer is a set and the Saudi-context answer carries units.",
      "INVESTIGATE — Find out why. The x-versus-y argument, the parallel-lines argument, and the two-crossing quadratic case. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: two Jeddah ride-hailing apps priced against distance, compared graphically to find the SAR and km crossover.",
      "In-class Apply-route item: two grocery delivery apps with different flat fees and per-kilometre rates, compared the same way.",
      "Discussion prompt: why the cheaper option in a fixed-plus-rate pricing model depends on how far you are going, not on the flat fee alone.",
    ],
    exams: [
      "GAT (Qudurat) — algebra strand, reading where two linear relationships meet inside a quantitative-reasoning item, no graphing tool provided. Practice tip: set the two expressions equal and solve directly rather than sketching under time pressure.",
      "SAAT (Tahsili) — solving linear systems by graphing sits in the Grade 10 band; items ask “the lines cross at x = ?” or give a small table. Practice tip: rewrite both lines as y = mx + b first.",
      "SAT — Algebra, systems of two linear equations in two variables, one of the most heavily tested Algebra sub-skills. Practice tip: graph both lines in Desmos and read the Intersection point directly.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 5", section: "Grade 10 — 10A and 10C",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Two Rides, One Fair Price” project task · squared paper",
    competencies: ["Reading the correct coordinate off a graphed intersection point.", "Choosing between graphing, algebra and a table depending on the answer's form."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra Intersect tool to confirm a graphed or table-approximated solution."],
    reallife: ["Two ride-hailing apps priced by a flag fall plus a per-kilometre rate.", "A grocery delivery app comparison with the same pricing structure."],
    values: ["Precision — reporting the coordinate the question actually asked for.", "Informed consumer choice — comparing real pricing plans before assuming one is always cheaper."],
    soft: ["Collaboration in assigned group roles.", "Explaining which method — graph, algebra, or table — fits a given answer, and why."],
    hard: ["Solving an equation or inequality by graphing both sides.", "Using a table to trap and narrow an approximate solution."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on reading intersections, evaluating, testing inequalities and bracketing roots. Results read as a gap map; students routed to the re-teach table, straight to graphing systems, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on x-versus-y for flagged students. Whole class: graphing an equation; graphing the same system as an inequality; using a table to approximate an irrational solution. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. Two Jeddah ride-hailing apps: both cost functions, the exact crossover, and a comparison at two distances. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — read a graphed solution, approximate a root by table, and justify which coordinate solves the equation. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which still catches you out — reading x instead of y off the graph, or trusting a table to be exact?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 1 · Lesson 6. Clinic group: bring your Time to Check paper.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION A", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "s_ws1", t: "Solve." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Graph it, solve it", done: "your x-value makes both sides equal when you substitute it back in.",
        intro: "Solve each equation by graphing (or algebra). Check each answer by substitution.",
        grid: [["1.", "s_ws1"], ["2.", "s_ws2"], ["3.", "s_ws3"], ["4.", "s_ws4"], ["5.", "s_g1"], ["6.", "s_qc"]],
        tasks: ["7.  Choose any two of the equations above and solve them a SECOND way — using a table instead of a graph. Do your two methods agree?"],
        lines: 2 },
      { note: "Inequalities, and one Saudi context", done: "your inequality answer is a set, not a point, and your Saudi-context answer carries both SAR and km.",
        graph: "g_lines_ineq", graphW: 380,
        tasks: [
          "1.  Solve graphically: 2x − 1 ≥ −x + 8. Shade the correct region and write the solution set.",
          "2.  A grocery app charges 8 SAR flat plus 1.5 SAR/km; a rival charges 3 SAR flat plus 2.5 SAR/km. Find, graphically, the distance where the costs are equal, in SAR and km.",
          "3.  Use a table to approximate, to one decimal place, the positive solution of x² − 3x − 1 = 0.",
          "4.  For the class ride-hailing example (App A: 5 + 2d, App B: 15 + d), which app is cheaper for a 7 km trip? Justify using the graph.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Explain why the x-coordinate of an intersection point solves ", { eq: "s_def", k: 0.95 }, ", but the y-coordinate does not answer the question being asked."],
          "2.  Two lines are parallel and never meet. What does that say about the number of solutions to f(x) = g(x)? Argue from slope.",
          "3.  A quadratic and a line cross twice. Explain what this means for the equation f(x) = g(x), and whether a table can approximate both solutions at once.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Two Rides, One Fair Price", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "Two ride apps price a trip differently — one has a higher starting fee but a lower per-kilometre rate. At what distance does it stop mattering which app you choose?",
    situation: [
      "App A charges a 5 SAR flag fall plus 2 SAR per kilometre.",
      "App B charges a 15 SAR flag fall plus 1 SAR per kilometre.",
      "A group of Grade 10 students wants to know which app to recommend for trips of different lengths around Jeddah.",
    ],
    eq: "s_ctx",
    steps: [
      ["1", "WRITE THE MODEL  (4 min)", "Write both cost functions, C_A(d) and C_B(d)."],
      ["2", "GRAPH AND MEET  (5 min)", "Graph both on the same axes; find the exact intersection point (show working, not just reading the picture)."],
      ["3", "PRICE THREE TRIPS  (4 min)", "Find and compare the cost of each app for trips of 4 km, 10 km, and 16 km."],
      ["4", "EXPLAIN THE SWITCH  (4 min)", "Explain in writing why the cheaper app changes at the intersection distance."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: which app you'd advise for an 8 km trip to the mall, and why."],
    ],
    working: [["Step 1 — both cost functions:", 2], ["Step 2 — the intersection, worked out:", 3],
              ["Step 3 — three trips priced for both apps:", 4], ["Step 4 — why the cheaper app switches:", 4],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two pricing plans", "Calculator — prices all three trips", "Checker — verifies the intersection by substitution", "Presenter — says the sentence"],
    doneWhen: ["The intersection distance and price are exact, not estimated.", "The cost function used is named for every calculation.", "Step 4 explains the switch using the rates, not just the numbers.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

// =====================================================================
// GR11 · T6 L6-1 · Key Features of Exponential Functions
// =====================================================================
const GR11_L61 = {
  slug: "Gr11_T6_L6-1_Key_Features_of_Exponential_Functions",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Key Features of Exponential Functions",
  unit: "Topic 6 — Exponential and Logarithmic Functions · Lesson 6-1",
  gradeFull: "Grade 11 — Algebra II",
  week: "Week 5 · Semester 1, 2026–27",
  weekNum: "5",
  lessonLine: "Grade 11 · Algebra II · Topic 6: Exponential and Logarithmic Functions · Lesson 6-1 — Key Features of Exponential Functions",
  codes: ["HSF.IF.C.7.E", "HSF.LE.A.2", "HSF.LE.B.5", "HSF.LE.A.1.C"],
  mps: ["MP.4", "MP.7"],
  assessments: ASSESS,
  objectives: [
    "Identify key features of exponential functions, including intercepts, domain, range, and end behavior, using graphs and tables.",
    "Graph exponential function transformations, including vertical shifts and reflections, and label key points.",
    "Model exponential growth and decay using functions with growth and decay factors to represent changes by a constant percentage over time.",
  ],
  essentialQuestion: "How can we identify and interpret the key features of exponential functions in graphs and equations?",
  vocabList: "decay factor ; exponential functions ; growth factor",

  plan: {
    outcome: [
      "⚠ STANDARDS NOTE. HSF.IF.C.7.E also covers logarithmic and trigonometric graphing; this lesson teaches only its EXPONENTIAL-function clause. Logarithmic and trigonometric graphing are separate lessons later in Topic 6 — flagged here per the map-mismatch convention used elsewhere in this pipeline.",
      "Students will read the y-intercept, asymptote, domain, range and end behavior straight off an exponential graph or table.",
      "Students will graph a vertical shift or a reflection of an exponential function and relabel its asymptote and y-intercept.",
      "Students will convert a percent change into a growth or decay factor and model a real percentage-based change over time.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “Multiply, don't add” — the y-intercept and growth factor of a simple exponential function. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one function evaluation, one percent-to-factor conversion.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz (≤ 4 minutes): evaluate f(x) = 2ˣ at x = 0 and x = 3; compare adding 3 five times against multiplying by 1.5 five times, starting at 2; convert an 8% increase to a growth factor; convert a 15% decrease to a decay factor; decide whether a given table is linear or exponential.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: f(0) = 1, f(3) = 8 ; the two are close after 5 steps but multiplying eventually overtakes adding — build the actual table with the class rather than asserting it ; 8% increase → 1.08 ; 15% decrease → 0.85 ; the table is exponential because the ratio between consecutive y-values is constant.",
    ],
    diagGap: [
      "Expected gap 1 — assuming multiplicative growth always wins immediately; it wins in the long run, not necessarily on the first few steps.",
      "Expected gap 2 — converting a percent change to a factor with the wrong sign of operation (adding instead of subtracting for a decrease, or vice versa).",
      "Expected gap 3 — Q5, which decides whether students can tell growth/decay data from linear data by ratio rather than by eye.",
      "Routing: 0–2 correct → re-teach table.  3–4 → straight to reading the graph.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): f(0) = 1 for every function of the form bˣ — substitute x = 0 first, always, before anything else.",
      "Whole class, IF.C.7.E: read f(x) = 2ˣ's key features off its graph — y-intercept (0,1), horizontal asymptote y = 0, domain all reals, range y > 0, end behavior x→∞ f→∞ and x→−∞ f→0⁺.",
      "Whole class, transformations: g(x) = 2ˣ − 3 shifts the asymptote to y = −3 and the y-intercept to −2; h(x) = −2ˣ reflects the range to y < 0 and the y-intercept to −1. The asymptote moves with a SHIFT; the range flips with a REFLECTION.",
      "Whole class, LE.A.2 / LE.B.5 / LE.A.1.C: an 8% increase is new = old + 0.08·old = 1.08·old, so the growth factor is 1.08; a 15% decrease gives decay factor 0.85. General forms y = a(1+r)ᵗ (growth) and y = a(1−r)ᵗ (decay).",
      "Narration focus — show the actual increasing yearly increments in a growth table (not just assert them) so students see WHY a percentage change is not a fixed amount.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: state the y-intercept and growth factor of f(x) = 5(3)ˣ.",
      "Expected: y-intercept 5, growth factor 3. Watch for students who swap the coefficient and the base.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time a decay function.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) f(x) = 3(2)ˣ — state the y-intercept, growth factor, domain, range and end behavior.  (2) g(x) = 100(0.8)ˣ — state the decay factor and percent decrease, then evaluate at x = 5.",
      "Answers: (1) y-intercept 3, growth factor 2, domain all reals, range y > 0, end behavior x→∞ f→∞, x→−∞ f→0⁺. (2) decay factor 0.8, percent decrease 20%, g(5) = 32.768.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four functions classified as growth or decay with percent change and y-intercept, two sketched with asymptote and intercept labelled. Done when: the y-intercept, growth/decay factor and percent change all agree with each other.",
      "APPLY — Use it in context. A vertical shift and a reflection each relabelled, and two Saudi-context growth/decay models (a farming project, a reservoir). Done when: every transformation comes with its new asymptote, and every real-world answer carries its units.",
      "INVESTIGATE — Find out why. Why y = a·bˣ can never equal zero, how two functions with the same intercept but different bases diverge in end behavior, and an algebraic proof that a 1.08 growth factor means an 8% increase. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A new eco-tourism destination near AlUla opened with 40,000 visitors and is growing by 25% every year, as part of a Vision 2030 tourism target.",
      "(a) Identify the growth factor and percent increase, and write V(t). (b) Find the number of visitors after 3 years. (c) State V(0) and what it means in context; state a sensible domain and range. (d) A colleague says “it grew by 10,000 in the first year, so it's growing by 10,000 a year — that's linear.” Explain in one sentence why this is wrong.",
      "Answers: (a) growth factor 1.25, 25% increase, V(t) = 40 000(1.25)ᵗ. (b) V(3) = 78 125 visitors. (c) V(0) = 40 000, the opening-year count; domain t ≥ 0, range V ≥ 40 000. (d) the growth is a PERCENTAGE of an ever-larger total, so the yearly increase itself grows (10 000, then 12 500, then 15 625, ...) — a fixed 10 000-a-year model underestimates every year after the first.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the growth factor identified correctly before the function is written, and every real-world answer carries its units (visitors, years).",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a)–(d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "For f(x) = 4(0.6)ˣ: 1. state the decay factor and percent decrease. 2. state the domain, range and horizontal asymptote. 3. in ONE sentence explain why the graph never reaches y = 0.",
      "Answers: 1. decay factor 0.6, percent decrease 40%. 2. domain all reals, range y > 0, asymptote y = 0. 3. 0.6 raised to any real power is always strictly positive, so 4(0.6)ˣ can get arbitrarily close to zero but never equal it.",
      "Done when: the percent decrease is shown as a calculation, not just stated, and question 3 gives a reason rather than a restatement.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their eco-tourism reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the growth function, the 3-year visitor count, and V(0) in context; ONE worked non-example — treating the first year's 10,000-visitor increase as a fixed yearly amount — with a sentence on how a reader would spot it; and a caption on why percentage growth eventually outpaces fixed growth.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 6 modelling set.",
      "Reflection question: “Which is still harder for you — reading the key features off a graph, or telling growth and decay apart from an equation alone?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four functions classified growth/decay with percent change and y-intercept; the two general forms stay on the board and a partner is allowed. Done when: the y-intercept, factor and percent change all agree.",
      "APPLY — Use it in context. A shift and a reflection relabelled, and two Saudi-context growth/decay models. Done when: every transformation carries its new asymptote and every answer carries units.",
      "INVESTIGATE — Find out why. Why y = a·bˣ is never zero, how end behavior diverges for different bases, and the 1.08-means-8% proof. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a Vision 2030 eco-tourism destination near AlUla, growing 25% a year, modelled and projected forward.",
      "In-class Apply-route items: a Vision 2030 smart-farming project in Al-Kharj (growth) and a reservoir's summer evaporation (decay).",
      "Discussion prompt: why a project that grows by a fixed PERCENTAGE eventually outpaces one that grows by a fixed NUMBER, even if the fixed number looks bigger in year one.",
    ],
    exams: [
      "SAAT (Tahsili) — exponential functions in the Grade 11 band, 30% of the mathematics section; asked as reading a y-intercept from a rule or matching a table to growth vs. decay. Practice tip: substitute x = 0 first, always.",
      "SAT — Advanced Math, exponential models and interpreting parameters in context. Practice tip: the base is always (1 ± rate) — subtract it from or add it to 1 to recover the percent change directly.",
      "GAT (Qudurat) — percentage growth over repeated periods inside quantitative reasoning, usually two or three periods. Practice tip: multiply by the growth factor once per period rather than adding the percentage each time.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 5", section: "Grade 11 — 11B",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Tracking a New Destination” project task · squared paper",
    competencies: ["Reading intercepts, asymptote, domain, range and end behavior off an exponential graph.", "Converting a percent change to a growth or decay factor and back again."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders on a and b in y = a·bˣ, to watch growth turn into decay at b = 1."],
    reallife: ["A Vision 2030 eco-tourism destination growing by a fixed percentage each year.", "A smart-farming project and a reservoir's evaporation, one growth and one decay."],
    values: ["Precision — telling a percentage change apart from a fixed amount.", "Long-term thinking — recognising that percentage growth compounds over time."],
    soft: ["Collaboration in assigned group roles.", "Explaining why growth and decay factors sit on either side of 1, not just stating which is which."],
    hard: ["Reading key features of an exponential function from a graph, table or rule.", "Modelling a real percentage-based change with a growth or decay factor."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on evaluating, comparing addition to multiplication, converting percentages, and reading a table. Results read as a gap map; students routed to the re-teach table, straight to reading the graph, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on f(0) = 1 for flagged students. Whole class: reading key features off a graph; vertical shifts and reflections; growth and decay factors from percentages. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The AlUla eco-tourism destination: the growth function, the 3-year visitor count, and the domain/range in context. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — decay factor, percent decrease, domain/range/asymptote and a one-sentence justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — reading the key features off a graph, or telling growth and decay apart from an equation alone?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for the next lesson, Topic 6 · Lesson 6-2 — Compound Interest. Clinic group: bring your Time to Check paper.",
  },

  // Minimal stub — classwork is NOT requested this round; this file is
  // deleted immediately after build and never delivered.
  classwork: {
    subtitle: "Not delivered this round.",
    sections: [
      { h: "SECTION A", note: "placeholder — not delivered", lines: 2,
        q: [{ n: "Q1", eq: "x_ws1", t: "Evaluate." }] },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Growth, decay, and the y-intercept", done: "your y-intercept, growth/decay factor and percent change all agree with each other.",
        intro: "For each function, state whether it's growth or decay, its percent change, and its y-intercept.",
        grid: [["1.", "x_ws1"], ["2.", "x_ws2"], ["3.", "x_ws3"], ["4.", "x_ws4"], ["5.", "x_g1"], ["6.", "x_g2"]],
        tasks: ["7.  Choose any two of the functions above and sketch both on the same axes, labelling the asymptote and y-intercept on each."],
        lines: 2 },
      { note: "Transformations, and one Saudi context", done: "every transformation comes with its new asymptote, and every real-world answer carries its units.",
        graph: "g_exp_transform", graphW: 380,
        tasks: [
          "1.  Graph g(x) = 2ˣ − 4. State its new asymptote, y-intercept, domain and range.",
          "2.  Graph h(x) = −3ˣ. State its range, and explain in one sentence why the y-intercept is negative.",
          "3.  A Vision 2030 smart-farming project in Al-Kharj starts with 1,200 hectares and expands by 12% each year. Find the area after 4 years, in hectares.",
          "4.  A reservoir holds 50,000 m³ and loses 6% of its volume to evaporation each week. Find the volume after 6 weeks, in m³.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Explain why ", { eq: "x_def", k: 0.95 }, " can never equal zero, no matter how large or small x gets — argue from what bˣ means."],
          "2.  Two functions share a y-intercept but have different bases, one bigger than 1 and one between 0 and 1. Sketch both and explain how their end behavior differs.",
          "3.  A quantity's growth factor is 1.08. Show algebraically that this is the same as saying it grows by 8% each period.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Tracking the New Destination", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A new eco-tourism site grows by a fixed percentage every year. When does it first pass 100,000 visitors, and is a flat 10,000-a-year forecast on track?",
    situation: [
      "The site opened in year 0 with 40,000 visitors.",
      "Visitor numbers grow by 25% every year — a fixed PERCENTAGE, not a fixed number.",
      "A planning report assumed a flat 10,000 more visitors every year.",
    ],
    eq: "x_ctx",
    steps: [
      ["1", "WRITE THE MODEL  (3 min)", "Write V(t), and identify the growth factor and percent increase."],
      ["2", "BUILD THE TABLE  (5 min)", "Find V(0) through V(4), and record each year's actual increase."],
      ["3", "TEST THE REPORT  (4 min)", "Compare the actual increases to the flat 10,000-a-year forecast. Which year is closest? Which is furthest off?"],
      ["4", "FIND THE MILESTONE  (5 min)", "Find, to the nearest year, when visitors first exceed 100,000."],
      ["5", "PRESENT  (3 min)", "One sentence: why does percentage growth eventually outpace fixed growth?"],
    ],
    working: [["Step 1 — the model, factor and percent:", 2], ["Step 2 — the table V(0) to V(4):", 3],
              ["Step 3 — comparison to the flat forecast:", 3], ["Step 4 — the milestone year:", 2],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the growth rule", "Calculator — builds the table", "Checker — verifies the milestone year", "Presenter — says the sentence"],
    doneWhen: ["The table is built from V(t) = 40 000(1.25)ᵗ.", "The milestone year is found by checking, not guessed.", "The forecast comparison uses actual numbers.", "Your sentence suits a non-mathematician."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  for (const cfg of [GR10_L5, GR11_L61]) {
    await buildAll(cfg);
    const cwFile = `Classwork_${cfg.slug}.docx`;
    if (fs.existsSync(cwFile)) fs.unlinkSync(cwFile);
  }
})();

module.exports = { GR10_L5, GR11_L61 };

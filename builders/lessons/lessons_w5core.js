// Week 5 core lessons — the lessons immediately following Week 4's, per each
// lesson's own nextLesson field in lessons_w4.js.
//   Gr10  Lesson 1-5  Solving Equations and Inequalities by Graphing
//   Gr11  Lesson 6-1  Key Features of Exponential Functions
//
// Objectives, essential questions, vocabulary, standards, MPs and assessment
// names are quoted VERBATIM from the curriculum map (cmap.docx), extracted
// earlier this session.
const { build } = require("./lesson_engine");

const MATH = "math_w5core/_index.json";
const GRAPH = "graphs_w5core/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 1 · LESSON 5 — Solving Equations and Inequalities by Graphing
// =====================================================================
const GR10_L5 = {
  out: "Gr10_T1_L5_Solving_Equations_and_Inequalities_by_Graphing.pptx",
  deckTitle: "Solving Equations and Inequalities by Graphing — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 1 · LINEAR FUNCTIONS · LESSON 5",
  lessonTitle: "Solving Equations and Inequalities by Graphing",
  titleSize: 32,
  subtitle: "A solution is just a place where two graphs agree",
  titleEq: "s_title_w", titleEqK: 2.4,
  titleEqAlt: "f of x equals g of x",
  grade: "Grade 10", week: "Week 5 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 1 · Lesson 5",
  lessonRef: "Lesson 1-5 — Solving Equations and Inequalities by Graphing",
  nextLesson: "Topic 1 · Lesson 6",

  codes: ["HSA.CED.A.1", "HSA.REI.D.11"],
  mps: ["MP.2", "MP.5"],
  assessments: ASSESS,

  objectives: [
    "Solve equations graphically.",
    "Solve inequalities graphically.",
    "Use tables to approximate solutions of equations.",
  ],
  essentialQuestion: "How can graphing be used to find solutions to equations and inequalities?",

  vocabulary: [
    { term: "Graphical solution", def: "The x-value (or values) where the graphs of the two sides of an equation cross — read directly from the picture rather than computed by algebra alone." },
    { term: "Solution set", def: "The complete collection of values that make an equation or inequality true. For an inequality solved graphically, this is usually an interval of x-values, not a single point." },
  ],
  vocabSub: "The two terms the curriculum map lists for this lesson",

  prior: [
    { h: "Graphing a line from its equation", eq: "s_lin", d: "From Topic 1. Slope and y-intercept, plotted point by point." },
    { h: "Evaluating a function at a value", eq: "s_eval", d: "Substitute the input, read off the output." },
    { h: "Reading a table of values", eq: "s_tbl", d: "You built one for every sequence in Lesson 1-4 — today the table finds a solution instead." },
  ],
  priorSub: "Three things from Topic 1 — today they answer one new question",
  carryOver: "A solution to an equation is simply a place where two graphs agree — an x-value where both give the same y. Whether you find it by staring at a graph, scanning a table, or solving algebraically, it is the same question asked three different ways.",
  carryOverEq: "s_def",

  diagnose: {
    title: "Warm-Up: Where Do They Meet?",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "s_d1", t: "Where do these two lines meet? Find x." },
      { eq: "s_d2", t: "Evaluate the function." },
      { eq: "s_d3", t: "Is it TRUE at x = 3? Yes or no?" },
      { eq: "s_d4", t: "Between which two integers does g(x) = 0?" },
      { t: "From the table, f(1) = 0, f(2) = 1, f(3) = 2 and g(1) = 3, g(2) = 1, g(3) = −1. At which x does f(x) = g(x)?", eq: null },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to graphing systems.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Where Two Lines Agree",
      sub: "Objective 1 — solve an equation by graphing both sides",
      graph: "g_lines_eq", graphW: 6.6, graphY: 2.5,
      graphAlt: "The lines y equals 3x minus 2 and y equals negative x plus 6, crossing at the point 2 comma 4, which is marked and labelled",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "Graph y = LEFT side and y = RIGHT side, on the same axes.",
          "Wherever the two graphs cross, both give the SAME y — that is what the equation demands.",
          "The x-coordinate of that point is the solution.",
          "The y-coordinate is just the shared output — not what you were asked to find.",
          "Check by substitution: does the x-value make both sides equal?",
        ],
      },
      panelX: 7.5, panelW: 5.4, panelH: 4.0,
      bar: ["CHECK IT", "substitute x = 2 into BOTH sides: 3(2) − 2 = 4 and −(2) + 6 = 4 — they agree, so x = 2 is confirmed, not just read off a picture."],
      barY: 6.32,
      notes: "Graph y = 3x − 2 and y = −x + 6 together; they cross at (2, 4), so x = 2. Misconception to address aloud: students report the WHOLE point (2, 4) as \"the solution\" when the question only asks for x. Ask explicitly: what does the equation 3x − 2 = −x + 6 actually ask you to find?",
    },
    {
      title: "Equation or Inequality — Same Picture, Different Question",
      sub: "Objective 2 — solve an inequality by graphing",
      rowsHead: ["WHAT YOU'RE ASKING", "HOW THE GRAPH ANSWERS IT"],
      rowsTop: 2.42, rowH: 0.82,
      rows: [
        ["Equation — where are the two graphs EQUAL?", { eq: "s_row_eq", k: 1.35 }],
        ["Strict inequality (>) — where is line A ABOVE line B?", { eq: "s_row_ineq", k: 1.35 }],
        ["The solution set, written properly", { eq: "s_row_set", k: 1.4 }],
        ["Non-strict (≥) includes the meeting point itself", { eq: "s_row_ge", k: 1.35 }],
      ],
      bar: ["THE MEETING POINT IS THE BOUNDARY", "for a strict inequality it is NOT included in the solution set; for ≥ or ≤ it is. Shade the region that is above (or below) the line, then read the boundary off the x-axis."],
      barY: 6.32,
      notes: "Same two lines as slide 1: 3x − 2 > −x + 6 has solution x > 2, because for x > 2 the teal line sits above the maroon line. Misconception to address aloud: students shade the wrong side, or forget that a STRICT inequality excludes x = 2 itself. Ask them to test a point, like x = 0, in the original inequality to confirm which side is shaded.",
    },
    {
      title: "When the Answer Isn't a Whole Number — Use a Table",
      sub: "Objective 3 — approximate a solution with a table of values",
      graph: "g_table_approx", graphW: 6.6, graphY: 2.5,
      graphAlt: "The curve y equals x squared and the line y equals 2x plus 1, crossing near x approximately 2.41 and x approximately negative 0.41, both points marked",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "x² = 2x + 1 has no nice whole-number solution.",
          "Build a table of x² − (2x + 1) near where the graphs look close.",
          "At x = 2 it's −1; at x = 3 it's +2 — a sign change means a root is trapped between them.",
          "Narrow the interval: at x = 2.4 it's −0.04; at x = 2.5 it's +0.25.",
          "So the positive solution is x ≈ 2.4, to one decimal place.",
        ],
      },
      panelX: 7.5, panelW: 5.4, panelH: 4.0,
      bar: ["A TABLE NARROWS A BRACKET, IT DOESN'T GUESS", "find one x where the difference is negative and one where it's positive, then test the midpoint — that's the same idea an algebra student will later call bisection."],
      barY: 6.32,
      notes: "The exact solutions are x = 1 ± √2 ≈ 2.414 and −0.414 — irrational, so no exact table entry lands on them; a table only APPROXIMATES. Misconception to address aloud: students think a table gives an exact answer if you make it fine enough. It never does for an irrational root — only a bracket that narrows.",
    },
  ],

  quickCheck: {
    lead: "Find where these two lines meet — solve for x:", leadW: 5.9,
    eq: "s_qc", k: 2.2,
    think: "Set up both lines as y = ..., decide which method you'll use (graph or algebra), and check your x-value in both.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, graphed slowly, line by line.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "s_g1", t: "Solve by graphing (or algebra) — find x, then check it in both sides.", hint: "Rearrange so both sides are of the form y = ..., then find where they meet." },
      { eq: "s_g2", t: "Use a table to approximate the positive solution to one decimal place.", hint: "Try x = 3 and x = 4 first to trap the root, then narrow." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Solve four equations by graphing: (a) x + 3 = 2x − 1  (b) 5 − x = 2x − 4  (c) −3x + 7 = x − 1  (d) 2x + 1 = x + 6.", "Graph each pair on the same axes and mark the intersection point.", "Verify one of your four answers by substitution.", "State which method — graph or algebra — you would trust more for a non-whole-number answer, and why."],
        help: "You may use: squared paper, the worked example on the board, and a partner.",
        done: "your x-value makes both sides equal when you substitute it back in.", eq: "s_ws1" },
      { items: ["Solve graphically: 2x − 1 ≥ −x + 8. Write the solution set.", "Two delivery apps: 8 + 1.5/km vs. 3 + 2.5/km. Find where the costs are equal, in SAR and km.", "By table, approximate the positive root of x² − 3x − 1 = 0 to one decimal place.", "For a 7 km ride, which class app is cheaper? Justify from the graph."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your inequality answer is a set, not a point, and your Saudi-context answer carries both SAR and km.", eq: "s_ws5" },
      { items: ["Explain why the x-coordinate of an intersection point solves f(x) = g(x), but the y-coordinate does not answer the question being asked.", "Two lines are parallel and never meet. What does that say about the number of solutions to f(x) = g(x)? Argue from slope.", "A quadratic and a line cross twice. What does that mean for the equation f(x) = g(x), and can a table approximate both solutions at once?"],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "s_def" },
    ],
  },

  production: {
    title: "Two Rides, One Fair Price",
    sub: "A context you have not seen before — this tests transfer",
    situation: "Two ride-hailing apps price a trip around Jeddah differently. App A charges a 5 SAR flag fall plus 2 SAR per kilometre. App B charges a 15 SAR flag fall plus 1 SAR per kilometre — a higher starting fee but a lower rate per kilometre.",
    eq: "s_ctx_w", eqK: 1.25,
    tasks: [
      "(a)  Write both cost functions, C_A(d) and C_B(d).",
      "(b)  Graph both on the same axes and find the exact distance where the two apps cost the same, and the price at that distance.",
      "(c)  Which app is cheaper for a 6 km trip to a mall, and for a 14 km trip to the airport? Use the graph to decide.",
      "(d)  A friend says “just pick the app with the lower flag fall — it'll always be cheaper.” Explain in one sentence why the friend is wrong.",
    ],
    note: "Exact values, in SAR and km, and the graph named as the method for part (c).",
    aiPrompt: "“Check whether I've read the crossover point correctly, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Graph both sides and drag to see the crossing point move",
    explore: "enter f(x) = 3x − 2 and g(x) = −x + 6, then find their Intersect point. Change the −2 to +2 and watch where the solution moves. Then try f(x) = x² and g(x) = 2x + 1, and say aloud why GeoGebra's two intersection points match the table method's estimates.",
  },

  gate: {
    eq: "s_gate_w",
    graph: "g_gate_lines",
    graphAlt: "The lines y equals negative 2x plus 9 and y equals 3x minus 1, crossing at the point 2 comma 5",
    items: [
      { t: "Find the solution shown by the graph — the x-value where the two lines meet.", eq: null },
      { t: "Use a table to approximate, to one decimal place, the positive solution of x² − 3x − 1 = 0.", eq: null },
      { t: "In ONE sentence, explain why the x-coordinate of an intersection point solves the equation, but the y-coordinate does not.", eq: null },
    ],
    footer: "Exact answer for Q1, the table shown for Q2, and Q3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (a quadratic-and-line system with two solutions, both approximated by table).      NOT YET → Targeted Learning Clinic on reading the CORRECT coordinate off an intersection point, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present both ride-app cost functions, the exact crossover distance and price, and your answer for the 6 km and 14 km trips." },
      { h: "Expose the trap", d: "Add one worked NON-example — \"always pick the lower flag fall\" — and a sentence saying how a reader would spot the error using the graph." },
      { h: "Say why it matters", d: "One caption — “why the cheaper app depends on how far you're going” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 1 modelling set.",
    reflection: "which still catches you out — reading x instead of y off the graph, or trusting a table to be exact?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Algebra strand — reading where two linear relationships meet, inside a quantitative-reasoning item. No graphing tool is provided; the picture (or the algebra) has to be done in your head or on paper.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Set the two expressions equal and solve directly — it's faster than sketching under time pressure. Use the graph only to sanity-check your answer.",
      question: "The lines y = 3x − 2 and y = −x + 6 are graphed on the same axes. At what x-value do they intersect?" },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Solving linear systems by graphing sits in the Grade 10 band; items are phrased as \"the lines cross at x = ?\" or give a small table and ask which x makes two rules agree.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Rewrite both lines as y = mx + b first — a common wrong option comes from mixing up which line has which slope.",
      question: "Line f has equation y = x + 1 and line g has equation y = −2x + 10. Graphed together, the two lines cross at x = ?" },
    { code: "SAT", full: "College Board", skill: "Algebra — systems of two linear equations in two variables, one of the most heavily tested Algebra sub-skills. Often given as a graph with the intersection point to be read, or as two equations to solve.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Graph both lines in Desmos and use the Intersection point directly — on the calculator-allowed modules this is faster than elimination.",
      question: "The graphs of y = x + 2 and y = 3x − 6 intersect at the point (x, y). What is the value of x?" },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the SOLUTION is the x-coordinate of the intersection — not the y-coordinate, and not the whole ordered pair unless the question asks for it."],

  summary: [
    "Solve an equation by graphing both sides and reading the x-coordinate where they meet.",
    "Solve a strict or non-strict inequality by shading the correct side of the boundary line.",
    "Write a solution set properly, as an inequality or interval — not just a single number.",
    "Use a table to trap and narrow an approximate solution when it isn't a whole number.",
    "Model two real pricing plans graphically and find where they cost the same.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 1 · Lesson 6 (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on reading the correct coordinate off a graph.",
  ],

  notes: {
    cover: "Week 5 lesson for 10A and 10C, following Arithmetic Sequences and Series. Three teaching days this week, so the Smart Production step may run into the next session — protect the Mastery Gate instead.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSA.CED.A.1 and HSA.REI.D.11 for this lesson, and only MP.2 and MP.5 — do not add others.",
    vocabulary: "Both terms are the map's list. Make students say the difference aloud: a graphical SOLUTION is usually one number (or a short list); a SOLUTION SET can be an entire interval, which is the case for every inequality in this lesson.",
    prior: "If a student cannot read a value off a table cold, the third objective will not land. Watch for it in the diagnostic, question 5.",
    diagnose: "Answers: x = 4; f(2) = 5; no (both sides equal 5, so x = 3 is NOT a strict solution); the root is between x = 2 and x = 3; f(x) = g(x) at x = 2. Expected gap: Q3, where students answer 'yes' because they only check that the point lies near the lines, not that it makes the STRICT inequality false when the sides are equal.",
    quickCheck: "Answer: x = 2, y = 7 (from 4x − 1 = −2x + 11). Watch for students who solve for y first and report y as if it were the requested solution.",
    guided: "Answers — 1: 3x − 2 = −2x + 8 gives x = 2 (check: 3(2)−2=4, −2(2)+8=4, confirmed). 2: x² − 4x + 1 = 0 has positive root x ≈ 3.7 to one decimal place (exact value 2+√3 ≈ 3.732; h(3.7) = −0.11, h(3.8) = +0.24, so 3.7 is closer). Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) C_A(d) = 5 + 2d, C_B(d) = 15 + d. (b) 5 + 2d = 15 + d gives d = 10 km, and the shared price is C = 25 SAR. (c) at 6 km: App A = 17 SAR, App B = 21 SAR — App A cheaper; at 14 km: App A = 33 SAR, App B = 29 SAR — App B cheaper. (d) the friend has ignored the per-kilometre RATE — a lower flag fall only wins for short trips; past the crossover distance the higher-rate app becomes more expensive.",
    geogebra: "The x² and 2x + 1 pair is the one that matters: GeoGebra's Intersect tool will report x ≈ 2.41 and x ≈ −0.41, matching the table method's bracket from the lesson — the two methods are the same idea, one visual and one numerical.",
    gate: "Answers: Q1 −2x + 9 = 3x − 1 gives x = 2 (check: −2(2)+9=5, 3(2)−1=5). Q2 x² − 3x − 1 = 0 has positive root x ≈ 3.3 to one decimal place (exact value (3+√13)/2 ≈ 3.303; h(3.3) = −0.01, h(3.31) = +0.03, root sits at 3.3). Q3: because the x-value is the shared INPUT where both functions agree — that is what the equation f(x) = g(x) asks for — while the y-value is just the common output, which the equation never asked you to find. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — 'always pick the lower flag fall' is exactly the shortcut a real customer would take, and it is wrong for any trip past 10 km.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

// =====================================================================
// GRADE 11 · TOPIC 6 · LESSON 6-1 — Key Features of Exponential Functions
// =====================================================================
const GR11_L61 = {
  out: "Gr11_T6_L6-1_Key_Features_of_Exponential_Functions.pptx",
  deckTitle: "Key Features of Exponential Functions — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-1",
  lessonTitle: "Key Features of Exponential Functions",
  titleSize: 30,
  subtitle: "A new topic, and one new habit: multiply by the same factor, not add the same amount",
  titleEq: "x_title_w", titleEqK: 2.2,
  titleEqAlt: "y equals a times b to the power x",
  grade: "Grade 11", week: "Week 5 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-1",
  lessonRef: "Lesson 6-1 — Key Features of Exponential Functions",
  nextLesson: "Topic 6 · Lesson 6-2 — Compound Interest",

  codes: ["HSF.IF.C.7.E", "HSF.LE.A.2", "HSF.LE.B.5", "HSF.LE.A.1.C"],
  mps: ["MP.4", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Identify key features of exponential functions, including intercepts, domain, range, and end behavior, using graphs and tables.",
    "Graph exponential function transformations, including vertical shifts and reflections, and label key points.",
    "Model exponential growth and decay using functions with growth and decay factors to represent changes by a constant percentage over time.",
  ],
  essentialQuestion: "How can we identify and interpret the key features of exponential functions in graphs and equations?",

  vocabulary: [
    { term: "Exponential functions", def: "Functions of the form y = a·bˣ (a ≠ 0, b > 0, b ≠ 1) in which the input sits in the EXPONENT, so the output changes by a constant multiplicative factor per unit step, not a constant amount." },
    { term: "Growth factor", def: "The base b of y = a·bˣ when b > 1. Each unit increase in x MULTIPLIES the value by b, growing it by a constant percentage." },
    { term: "Decay factor", def: "The base b of y = a·bˣ when 0 < b < 1. Each unit increase in x MULTIPLIES the value by b, shrinking it by a constant percentage." },
  ],
  vocabSub: "The three terms the curriculum map lists for this lesson",

  prior: [
    { h: "Exponent rules", eq: "x_exprules", d: "From earlier this course. Today the exponent is a variable, not just a fixed power." },
    { h: "Linear functions add", eq: "x_lincontrast", d: "A straight line changes by the same AMOUNT every step. Today's functions change by the same FACTOR instead." },
    { h: "Percent as a multiplier", eq: "x_pct", d: "Convert the percent to a decimal, then add or subtract it from 1 — that number becomes the base." },
  ],
  priorSub: "Three things you already know — today's topic is new, but the tools are not",
  carryOver: "Every exponential function is built from ONE idea: multiply by the same factor every time x increases by 1. A growth factor is that number when it is bigger than 1; a decay factor is that number when it is between 0 and 1. The graph shape, the asymptote, and the modelling all fall out of that one multiplicative step.",
  carryOverEq: "x_def",

  diagnose: {
    title: "Warm-Up: Adding vs. Multiplying",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "x_d1", t: "Evaluate the function at both inputs." },
      { eq: "x_d2", t: "After 5 steps, which is bigger — and by how much?" },
      { eq: "x_d3", t: "Convert the percent change to a growth factor." },
      { eq: "x_d4", t: "Convert the percent change to a decay factor." },
      { eq: "x_d5", t: "Is this table linear or exponential? How do you know?" },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to reading the graph.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Reading the Graph of an Exponential Function",
      sub: "Objective 1 — intercepts, domain, range and end behavior",
      graph: "g_exp_growth", graphW: 6.5, graphY: 2.5,
      graphAlt: "The curve f of x equals 2 to the power x, passing through 0 comma 1, approaching the horizontal asymptote y equals 0 on the left and rising steeply on the right, with end behavior arrows and labels",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "y-intercept: f(0) = 1 for every function of the form bˣ — check it before anything else.",
          "Horizontal asymptote: y = 0. The curve gets closer and closer but never touches it.",
          "Domain: all real numbers — you can raise 2 to ANY power.",
          "Range: y > 0 only. An exponential function is never zero and never negative.",
          "End behavior: as x → ∞, f → ∞; as x → −∞, f → 0⁺.",
        ],
      },
      panelX: 7.4, panelW: 5.5, panelH: 4.0,
      bar: ["WHY IT NEVER TOUCHES ZERO", "2 raised to any power — however negative — is still positive, just very small. There is no power of 2 that gives exactly 0."],
      barY: 6.32,
      notes: "f(x) = 2ˣ: f(0) = 1, asymptote y = 0, domain all reals, range y > 0. Misconception to address aloud: students think the graph eventually crosses the x-axis if you zoom out far enough. It never does — 2 to any real power stays strictly positive, which is exactly why the range excludes zero.",
    },
    {
      title: "Vertical Shifts and Reflections",
      sub: "Objective 2 — transform the graph and relabel its key features",
      rowsHead: ["THE TRANSFORMATION", "WHAT CHANGES"],
      rowsTop: 2.42, rowH: 0.86,
      rows: [
        ["Vertical shift down 3: f(x) = 2ˣ becomes...", { eq: "x_row_shift", k: 1.6 }],
        ["...which moves the asymptote to", { eq: "x_row_asym1", k: 1.5 }],
        ["Reflect over the x-axis: f(x) = 2ˣ becomes", { eq: "x_row_reflect", k: 1.6 }],
        ["...which flips the range to", { eq: "x_row_range2", k: 1.5 }],
      ],
      bar: ["THE ASYMPTOTE MOVES WITH A VERTICAL SHIFT — THE RANGE FLIPS WITH A REFLECTION", "a shift up or down k units moves the asymptote to y = k; a reflection over the x-axis turns range y > 0 into range y < 0. The y-intercept moves too — recompute it, don't guess."],
      barY: 6.32,
      notes: "g(x) = 2ˣ − 3 has new y-intercept g(0) = 1 − 3 = −2 and asymptote y = −3. h(x) = −2ˣ has new y-intercept h(0) = −1 and range y < 0, asymptote still y = 0. Misconception to address aloud: students shift the ASYMPTOTE but forget to recompute the y-intercept, or assume a reflection changes the asymptote (it does not — only a vertical shift moves it).",
    },
    {
      title: "Growth and Decay Factors — the Same Picture, Two Directions",
      sub: "Objective 3 — model a constant percentage change over time",
      graph: "g_exp_growth_decay", graphW: 6.5, graphY: 2.5,
      graphAlt: "Two curves through the point 0 comma 1: f of x equals 2 to the x rising to the right, and g of x equals 0.5 to the x falling to the right, each labelled growth or decay",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "An 8% increase means: new = old + 0.08·old = 1.08·old.",
          "So the growth FACTOR is 1.08 — one number that does the whole calculation.",
          "A 15% decrease means: new = old − 0.15·old = 0.85·old — decay factor 0.85.",
          "General forms: growth y = a(1+r)ᵗ with b = 1+r > 1; decay y = a(1−r)ᵗ with 0 < b = 1−r < 1.",
          "a is the STARTING value, at t = 0 — check it's the y-intercept before you use it.",
        ],
      },
      panelX: 7.4, panelW: 5.5, panelH: 4.0,
      bar: ["A FIXED PERCENTAGE IS NOT A FIXED AMOUNT", "growing by 25% a year adds a DIFFERENT number of units every year, because 25% of a bigger total is itself bigger — that is exactly why this is exponential, not linear."],
      barY: 6.32,
      notes: "Growth factor b = 1 + r (b > 1); decay factor b = 1 − r (0 < b < 1). Misconception to address aloud: students treat the first year's increase (a fixed NUMBER) as if it will repeat every year, effectively modelling a percentage-growth situation as linear. Show the table: the yearly increase itself grows.",
    },
  ],

  quickCheck: {
    lead: "State the y-intercept and the growth factor for", leadW: 5.6,
    eq: "x_qc", k: 2.4,
    think: "The y-intercept is f(0) — substitute 0 for x. The growth (or decay) factor is just the base, read straight off the rule.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time a decay function.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "x_g1", t: "State the y-intercept, growth factor, domain, range and end behavior.", hint: "Growth or decay first — is the base bigger or smaller than 1? Everything else follows from that." },
      { eq: "x_g2", t: "State the decay factor and the percent decrease, then evaluate at x = 5.", hint: "The decay factor is the base. Percent decrease = (1 − base) × 100%." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["For four functions — f(x)=5(1.2)ˣ, f(x)=2(0.9)ˣ, f(x)=4(3)ˣ, f(x)=10(0.5)ˣ — state whether each is growth or decay, its percent change, and its y-intercept.", "Sketch any two of the four on the same axes, labelling the asymptote and the y-intercept on each.", "For one function of your choice, state its domain, range and end behavior.", "Test each rule at x = 0 first, and say what that always tells you."],
        help: "You may use: the two general forms on the board, and a partner.",
        done: "your y-intercept, growth/decay factor and percent change all agree with each other.", eq: "x_ws1" },
      { items: ["Graph g(x) = 2ˣ − 4. State its asymptote, y-intercept, domain and range.", "Graph h(x) = −3ˣ. State its range and y-intercept.", "Al-Kharj farming project: 1,200 ha, growing 12% a year. Find the area after 4 years, in hectares.", "A 50,000 m³ reservoir loses 6% a week. Find the volume after 6 weeks, in m³."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "every transformation comes with its new asymptote, and every real-world answer carries its units.", eq: "x_ws3" },
      { items: ["Explain why y = a·bˣ can never equal zero, no matter how large or small x gets — argue from what bˣ means, not just \"that's the graph shape\".", "Two functions share a y-intercept but have different bases, one bigger than 1 and one between 0 and 1. Sketch both and explain how their end behavior differs.", "A quantity's growth factor is 1.08. Show algebraically that this is the same as saying it grows by 8% each period."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "x_pctcheck" },
    ],
  },

  production: {
    title: "Tracking a New Destination",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A new eco-tourism destination near AlUla opened with 40,000 visitors and is growing by 25% every year, as part of a Vision 2030 tourism target — not by a fixed number of visitors, but by a fixed PERCENTAGE.",
    eq: "x_ctx_w", eqK: 1.4,
    tasks: [
      "(a)  Identify the growth factor and the percent increase, and write the function V(t).",
      "(b)  Find the number of visitors after 3 years.",
      "(c)  State V(0) and say what it means in context. State a sensible domain and range for this model.",
      "(d)  A colleague says “it grew by 10,000 visitors in the first year, so it's growing by 10,000 a year — that's a linear model.” Explain in one sentence why this is wrong.",
    ],
    note: "Exact values, units named (visitors, years), and the growth factor stated before anything else.",
    aiPrompt: "“Check whether I've used the growth factor correctly, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide the base and watch growth turn into decay",
    explore: "enter f(x) = a*b^x with sliders for a and b. Set a = 1, then drag b from 0.2 up through 1 to 3, and watch the curve flip from decay to growth exactly at b = 1. Then set b = 1.25 and a = 40000, and check your production-task numbers against the graph.",
  },

  gate: {
    eq: "x_gate_w",
    items: [
      { t: "State the decay factor and the percent decrease for the function shown.", eq: null },
      { t: "State the domain, range and horizontal asymptote.", eq: null },
      { t: "In ONE sentence, explain why the graph never reaches y = 0.", eq: null },
    ],
    footer: "Exact answers only. The percent decrease shown as a calculation, not just stated, and question 3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (a transformed exponential with both a shift and a reflection, key features fully relabelled).      NOT YET → Targeted Learning Clinic on growth vs. decay factors, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the eco-tourism growth function, the visitor count after 3 years, and the y-intercept in context." },
      { h: "Expose the trap", d: "Add one worked NON-example — treating the first year's 10,000-visitor increase as a fixed yearly amount — and a sentence saying how a reader would spot the error from a table." },
      { h: "Say why it matters", d: "One caption — “why growing by a percentage eventually outpaces growing by a fixed number” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which is still harder for you — reading the key features off a graph, or telling growth and decay apart from an equation alone?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Exponential functions sit in the Grade 11 band, 30% of the mathematics section — asked as reading a y-intercept from a rule, or matching a table to growth vs. decay.", fmt: "Four-option multiple choice, no calculator.", tip: "Substitute x = 0 first, always — the y-intercept is the fastest fact you can pull from any exponential rule.",
      question: "The function f(x) = 3(2)ˣ is graphed. What is the y-intercept?" },
    { code: "SAT", full: "College Board", skill: "Advanced Math — exponential models and interpreting parameters in context, a core Advanced Math sub-skill worth close attention.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "The base is always (1 ± rate) — subtract it from 1, or subtract 1 from it, to recover the percent change directly.",
      question: "The function g(t) = 500(0.75)ᵗ models the value, in dollars, of equipment t years after purchase. By what percent does the value decrease each year?" },
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Percentage growth over repeated periods, inside quantitative reasoning — usually two or three periods, meant to be estimated quickly rather than computed exactly.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Multiply by the growth factor once per period rather than adding the percentage each time — repeated addition of a percent gives the wrong (smaller) answer.",
      question: "A quantity starts at 200 and increases by 10% each period. After 2 periods, the quantity is closest to which value? (A) 220  (B) 240  (C) 242  (D) 260" },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the base b IS the growth or decay factor — read it straight off the rule, and it converts to a percent change as (b − 1) × 100%."],

  summary: [
    "Read the y-intercept, asymptote, domain, range and end behavior straight off an exponential graph or rule.",
    "Graph a vertical shift or a reflection, and relabel the asymptote and y-intercept correctly.",
    "Tell growth from decay by comparing the base to 1.",
    "Convert a percent increase or decrease into a growth or decay factor, and back again.",
    "Model a real percentage-based change over time, and explain why it isn't linear.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 6 · Lesson 6-2 — Compound Interest (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on growth vs. decay factors.",
  ],

  notes: {
    cover: "Week 5 lesson for 11B, opening Topic 6 (Exponential and Logarithmic Functions) after Topic 5 (Radical Functions) closed with Inverse Relations and Functions. This is a NEW topic — do not lean on radical-function content. Three teaching days this week, so the Smart Production step may run into the next session — protect the Mastery Gate instead.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSF.IF.C.7.E, HSF.LE.A.2, HSF.LE.B.5 and HSF.LE.A.1.C for this lesson, and only MP.4 and MP.7 — do not add others. NOTE: HSF.IF.C.7.E also covers logarithmic and trigonometric graphing; only its exponential-function clause is taught in this lesson — logarithmic and trigonometric graphing are separate lessons later in the topic. Flagged here per the map-mismatch convention used elsewhere in this pipeline.",
    vocabulary: "All three terms are the map's list. Make students say which is which: GROWTH factor is always bigger than 1; DECAY factor is always between 0 and 1 — there is no such thing as a decay factor above 1 or a growth factor below 1.",
    prior: "If a student cannot convert a percent to a decimal multiplier cleanly, the whole third objective collapses. Watch for it in the diagnostic, questions 3 and 4.",
    diagnose: "Answers: f(0) = 1, f(3) = 8; multiplying by 1.5 five times overtakes adding 3 five times (2×1.5⁵ ≈ 15.2 vs. 2+5×3 = 17 — check this WITH the class, the crossover is close and worth showing on a table, not asserting); 8% increase → 1.08; 15% decrease → 0.85; the table is exponential, because the ratio between consecutive y-values is constant (×2 each step), not the difference. Expected gap: Q2, where students assume 'multiplying always wins immediately' — it does not, early on; it wins in the LONG run.",
    quickCheck: "Answer: y-intercept 5, growth factor 3. Watch for students who report the coefficient (5) as the growth factor, or the base (3) as the y-intercept — the two roles are easy to swap.",
    guided: "Answers — 1: f(x) = 3(2)ˣ: y-intercept 3, growth factor 2, domain all reals, range y > 0, end behavior x→∞ f→∞, x→−∞ f→0⁺. 2: g(x) = 100(0.8)ˣ: decay factor 0.8, percent decrease 20%, g(5) = 100(0.8)⁵ = 32.768. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) growth factor 1.25, 25% increase, V(t) = 40 000(1.25)ᵗ. (b) V(3) = 40 000(1.25)³ = 78 125 visitors. (c) V(0) = 40 000 — the opening-year visitor count; sensible domain t ≥ 0 (years since opening), range V ≥ 40 000. (d) the colleague has mistaken one year's increase for a fixed yearly amount — because the growth is a PERCENTAGE of an ever-larger total, the actual yearly increase itself grows (10 000, then 12 500, then 15 625, ...), so a linear model with a constant 10 000-a-year addition will underestimate every year after the first.",
    geogebra: "The crossover at b = 1 is the whole point of the slider — b = 1 gives the constant function y = a, which is neither growth nor decay; the moment b passes 1 the curve tips into growth, and the moment it drops below 1 it tips into decay.",
    gate: "Answers: for f(x) = 4(0.6)ˣ, decay factor 0.6, percent decrease (1 − 0.6) × 100% = 40%. Domain all real numbers, range y > 0, horizontal asymptote y = 0. Q3: because 0.6 raised to any real power is always strictly positive (never zero or negative), so 4(0.6)ˣ can get arbitrarily close to zero but can never equal it. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — treating a percentage-growth situation as a fixed yearly amount is exactly the mistake a real planning report would make, and it is worth showing the actual increasing increments (10 000, 12 500, 15 625, ...) as the correction.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  for (const cfg of [GR10_L5, GR11_L61]) await build(cfg);
})();

module.exports = { GR10_L5, GR11_L61 };

// Grade 10 · Topic 1 · Lesson 6 — Linear Systems
//
// Follows L1-5 (Solving Equations and Inequalities by Graphing) directly,
// and closes Topic 1 (Linear Functions) — the curriculum map's next rows
// are the Unit Recap and Unit Assessment, then Topic 2 · Lesson 1 (Vertex
// Form of a Quadratic Function). Objectives, essential question, vocabulary,
// standards and MPs are quoted VERBATIM from "Curriculum map A2 OBLAS.docx",
// Unit 1, Lesson 6.
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6_docs.js for the matching plan/activity/PBL.
// The Al-Ahsa farm context here is the SAME context, same numbers, as the
// PBL task and the docs' production/evidence sections.
//
// Every piece of mathematics inside a sentence (titles, panels, bars, notes)
// is written as $...$ per the inline-maths house rule — see engines/inline_math.js.
// Only self-contained display equations use a LaTeX image key (eq:).
const { build } = require("../../engines/lesson_engine");

const MATH = "math_w6/_index.json";
const GRAPH = "graphs_w6/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 1 · LESSON 6 — Linear Systems
// =====================================================================
const GR10_L6 = {
  out: "Gr10_T1_L6_Linear_Systems.pptx",
  deckTitle: "Linear Systems — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  weekNum: "6",
  topicLine: "TOPIC 1 · LINEAR FUNCTIONS · LESSON 6",
  lessonTitle: "Linear Systems",
  titleSize: 34,
  subtitle: "One point that makes two equations true at once",
  titleEq: "sy_title_w", titleEqK: 2.2,
  titleEqAlt: "A system of two linear equations, a one x plus b one y equals c one, and a two x plus b two y equals c two, grouped by a brace",
  grade: "Grade 10", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 1 · Lesson 6",
  lessonRef: "Lesson 1-6 — Linear Systems",
  nextLesson: "Topic 1 Recap & Unit Assessment — then Topic 2 · Lesson 1, Vertex Form of a Quadratic Function",

  codes: ["HSA.REI.C.6", "HSA.CED.A.3"],
  mps: ["MP.4", "MP.3"],
  assessments: ASSESS,

  objectives: [
    "Visualize and interpret solutions of systems of linear equations in two variables.",
    "Solve systems of linear equations both algebraically and graphically.",
    "Identify and describe graphically the regions that satisfy systems of inequalities.",
  ],
  essentialQuestion: "How can the concepts of linear systems be used to solve real-world problems?",

  vocabulary: [
    { term: "System of linear equations", def: "Two or more linear equations considered together, in the same variables — a solution must satisfy every equation at once." },
    { term: "Solution (of a system of linear equations)", def: "An ordered pair $(x,y)$ that makes every equation in the system true at the same time — the point where the lines meet." },
    { term: "Solution set", def: "The complete collection of ordered pairs that satisfy a system — a single point, no points at all, or every point on a shared line." },
    { term: "Substitution", def: "Solve one equation for a variable, then substitute that expression into the other equation to solve for the remaining variable." },
    { term: "Elimination", def: "Add or subtract multiples of the equations so one variable cancels, leaving a single equation in the other variable." },
    { term: "Linear inequality", def: "A statement comparing a linear expression to a value with $<$, $\\le$, $>$, or $\\ge$ — its graph is a half-plane, not a line." },
    { term: "Boundary line", def: "The line that separates the half-plane where an inequality is true from the half-plane where it is false — solid for $\\le$ or $\\ge$, dashed for $<$ or $>$." },
    { term: "System of linear inequalities", def: "Two or more linear inequalities considered together — a solution must satisfy every inequality at once." },
    { term: "Feasible region", def: "The overlap of every shaded half-plane in a system of inequalities — every point inside it is a viable solution to the whole system." },
  ],
  vocabSub: "All nine terms the curriculum map lists for this lesson",

  prior: [
    { h: "Solving equations by graphing (Lesson 1-5)", eq: "sy_prior_l5", d: "Two graphs crossing gave the $x$-value where they agreed. Today that same crossing point becomes the FULL answer — an ordered pair $(x,y)$." },
    { h: "Graphing a line from slope-intercept form", eq: "sy_prior_line", d: "Plot the $y$-intercept, then use the slope for a second point — today you graph two lines at once, on the same axes." },
    { h: "Solving a one-variable linear equation", eq: "sy_prior_solve", d: "Isolate the variable with inverse operations — substitution and elimination both finish with exactly this kind of equation." },
  ],
  priorSub: "Three things you already know — today they combine into one new method",
  carryOver: "A system of linear equations asks: where do these lines agree, in BOTH coordinates at once? A system of linear inequalities asks the same question about regions instead of lines — where do the shaded half-planes overlap?",
  carryOverEq: "sy_def",

  diagnose: {
    title: "Warm-Up: One Line, Two Lines",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "sy_d1", t: "Solve for $x$." },
      { eq: "sy_d2", t: "State the slope and the $y$-intercept." },
      { eq: "sy_d3", t: "Do these two lines have the same slope? Will they ever meet?" },
      { eq: "sy_d4", t: "Is the point shown a solution to the inequality?" },
      { eq: "sy_d5", t: "From the table, at which input do lines $f$ and $g$ meet?" },
    ],
    routing: "0–2 correct → re-teach isolating a variable.      3–4 correct → straight to solving systems.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "One Point, Two Equations",
      sub: "Objective 1 — what a solution to a system actually means",
      graph: "g_sys_one", graphW: 6.6, graphY: 2.5,
      graphAlt: "Two lines, y equals 2x minus 1 and y equals negative x plus 5, crossing at the point 2 comma 3, which is marked and labelled",
      panel: {
        h: "READ IT THIS WAY",
        items: [
          "A solution to a system is an ordered pair $(x,y)$ — it must satisfy BOTH equations, not just one.",
          "Graph both lines: wherever they cross is the ONLY point that works for both — that is the solution.",
          "One crossing point → exactly ONE solution — the usual case.",
          "Same slope, different $y$-intercept → the lines are parallel and NEVER meet — NO solution.",
          "Same slope AND same $y$-intercept → the lines ARE the same line — INFINITELY many solutions.",
        ],
      },
      panelX: 7.5, panelW: 5.4, panelH: 4.0,
      bar: ["A SYSTEM'S SOLUTION IS A POINT, NOT JUST A NUMBER", "in Lesson 1-5 you found one $x$-value where two rules agreed; today's solution is the FULL point $(x,y)$ where two whole equations agree."],
      barY: 6.32,
      notes: "$y=2x-1$ and $y=-x+5$ meet at $(2,3)$: check $2(2)-1=3$ and $-(2)+5=3$. Misconception to address aloud: students report only the $x$-value, as they did for a single equation in Lesson 1-5 — press them to say the FULL ordered pair, and to check it in BOTH original equations, not one.",
    },
    {
      title: "Three Roads, Same Destination",
      sub: "Objective 2 — solve one system by substitution, elimination, and graphing",
      rowsHead: ["METHOD", "SOLVING $x+y=7$ AND $x-y=1$"],
      rowsTop: 2.42, rowH: 0.86,
      rows: [
        ["Substitution — solve one equation for a variable, then plug it into the other", { eq: "sy_row_sub", k: 1.5 }],
        ["Elimination — add the equations so $y$ cancels", { eq: "sy_row_elim", k: 1.5 }],
        ["Graphing — plot both lines and read the crossing point", { eq: "sy_row_graph", k: 1.7 }],
        ["All three methods must AGREE", { eq: "sy_row_agree", k: 1.7 }],
      ],
      bar: ["PICK THE METHOD THE NUMBERS SUGGEST", "substitution is fastest when a variable is already isolated; elimination is fastest when coefficients match or cancel easily; graphing checks either one, but is not exact unless the solution lands on whole numbers."],
      barY: 6.32,
      notes: "All three methods solve $x+y=7$, $x-y=1$ and land on $x=4,\\ y=3$. Misconception to address aloud: students trust ONE method and never check it against another — insist that the algebraic answer and the graphed crossing point are the SAME point, every time.",
    },
    {
      title: "Where Two Shaded Regions Overlap",
      sub: "Objective 3 — graph a system of inequalities and find the feasible region",
      graph: "g_sys_ineq", graphW: 6.6, graphY: 2.5,
      graphAlt: "The boundary lines y less than or equal to negative x plus 6, solid, and y greater than 2x minus 1, dashed, with the overlapping region shaded and the points 0 comma 3 and 4 comma 4 marked",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Graph each boundary line — solid for $\\le$ or $\\ge$, dashed for $<$ or $>$.",
          "Shade the half-plane each inequality allows — test a point if you are unsure which side.",
          "The FEASIBLE REGION is where BOTH shaded areas overlap — every point inside satisfies BOTH inequalities.",
          "A point outside the overlap fails at least one inequality — it is NOT a solution to the system.",
          "Always confirm with a test point: substitute into both inequalities and check both come out true.",
        ],
      },
      panelX: 7.5, panelW: 5.4, panelH: 4.0,
      bar: ["THE OVERLAP IS THE ANSWER, NOT EITHER SHADING ALONE", "a point can satisfy one inequality and fail the other — only the region inside BOTH shadings solves the system."],
      barY: 6.32,
      notes: "$(0,3)$: $3\\le 6$ true and $3>-1$ true — feasible. $(4,4)$: $4\\le 2$ is false — not feasible, even though it looks close to the boundary. Misconception to address aloud: students shade based on the FIRST inequality only and forget to intersect it with the second; walk them through testing $(4,4)$ in both inequalities separately.",
    },
  ],

  quickCheck: {
    lead: "Solve this system by elimination — find $x$ and $y$:", leadW: 6.6,
    eq: "sy_qc", k: 2.2,
    think: "Look for a variable whose coefficients are already matched or opposite — add or subtract the equations to eliminate it first.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time by substitution.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "sy_g1", t: "Solve by substitution — find $x$ and $y$.", hint: "Solve the simpler-looking equation for one variable first, then substitute." },
      { eq: "sy_g2", t: "Graph this system of inequalities and shade the feasible region.", hint: "Graph each boundary line, decide solid or dashed, then test a point to choose the correct side." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Solve four systems, by substitution or elimination — your choice: (a) $x+y=10$, $x-y=2$   (b) $2x+y=7$, $x-y=-1$   (c) $3x-2y=5$, $x+2y=7$   (d) $y=2x-3$, $y=-x+9$.", "Graph any TWO of the four systems above, and mark the crossing point on each graph.", "Verify one of your four answers by substituting it into BOTH original equations.", "State which method you used most, and why it suited those particular numbers."],
        help: "You may use: the worked example on the board, and a partner.",
        done: "your $x$- and $y$-values satisfy BOTH original equations when you substitute them back in.", eq: "sy_ws1" },
      { items: ["Solve graphically: $y=-2x+8$ and $y=x-1$ — state the crossing point.", "Two internet plans: Plan $A$ costs $50+2g$ SAR, Plan $B$ costs $20+5g$ SAR, for $g$ GB of data. Find, algebraically, where the two plans cost the same, in SAR and GB.", "Graph the system $y\\le -x+7$ and $y> x-1$, and shade the feasible region.", "Test whether the point $(2,2)$ lies inside the feasible region you shaded."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your inequality answer is a shaded region, not a single point, and your Saudi-context answer carries both SAR and GB.", eq: "sy_ws5" },
      { items: ["Explain, using slope, why two lines with the same slope but different $y$-intercepts can never be a system's solution.", "A system of two linear equations has infinitely many solutions. What must be true about the two equations? Give your own example.", "A system of two inequalities has NO feasible region at all. Sketch an example and explain, using the boundary lines, why no point can satisfy both."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "sy_def" },
    ],
  },

  production: {
    title: "Planning a Farm Plot in Al-Ahsa",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A farm in the Al-Ahsa Oasis is planning this season's planting of dates and alfalfa, as part of the Kingdom's push for local food security. The farm has 40 hectares of land available, and its irrigation system can deliver at most 150 water units this season. Each hectare of dates needs 3 water units; each hectare of alfalfa needs 5 water units.",
    eq: "sy_farm_w", eqK: 1.3,
    tasks: [
      "(a)  Write both constraints as inequalities, using $x$ for hectares of dates and $y$ for hectares of alfalfa.",
      "(b)  Graph the system and shade the feasible region — the combinations of $x$ and $y$ the farm can actually plant.",
      "(c)  Is a plan of 25 hectares of dates and 10 hectares of alfalfa feasible? Justify using BOTH constraints.",
      "(d)  A worker says “just use up all 40 hectares, plant however you like.” Explain in one sentence why that is not always possible.",
    ],
    note: "Both inequalities checked separately, and a written reason — not just yes or no — for parts (c) and (d).",
    aiPrompt: "“Check whether I've shaded the correct side of each boundary line, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Drag a line and watch the intersection — and the shaded region — move",
    graph: "g_sys_one",
    graphAlt: "The lines y equals 2x minus 1 and y equals negative x plus 5, crossing at the point 2 comma 3, the construction to rebuild in GeoGebra",
    explore: "enter $f(x)=2x-1$ and $g(x)=-x+5$, then find their Intersect point and check it matches $(2,3)$. Drag a slider on the second line's slope until it matches the first, and watch the lines become parallel with no intersection at all. Then switch to inequality mode, shade $y\\le f(x)$ and $y> g(x)$, and check that the feasible region matches your hand-drawn graph from the farm task.",
  },

  gate: {
    graph: "g_gate_sys",
    graphAlt: "The lines x plus y equals 7 and 2x minus y equals 2, crossing at the point 3 comma 4",
    items: [
      { t: "Solve the system shown — find $x$ and $y$.", eq: null },
      { t: "The SAME two lines now form a system of inequalities: $y\\le 7-x$ and $y> 2x-2$. Name ONE point in the feasible region.", eq: null },
      { t: "In ONE sentence, explain why the boundary lines having exactly ONE crossing point does not mean the system of inequalities has only one solution.", eq: null },
    ],
    footer: "Exact answers for Q1 and a checked point for Q2, and Q3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (a system of inequalities with three boundary lines and a triangular feasible region).      NOT YET → Targeted Learning Clinic on reading a system's solution as a point, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present both farm constraints, the feasible-region graph, and your yes/no answer — with reasoning — for the 25-and-10 hectare plan." },
      { h: "Expose the trap", d: "Add one worked NON-example — a plan that fits the land limit but breaks the water limit — and a sentence saying how a reader would spot the error from the graph." },
      { h: "Say why it matters", d: "One caption — “why two limits can rule out a plan that only checks one of them” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 1 modelling set.",
    reflection: "which is still harder for you — solving a system algebraically, or reading a feasible region correctly off a graph?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Algebra strand — solving a small system of two linear equations quickly, inside a quantitative-reasoning item. No graphing tool is provided.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Add or subtract the two equations directly if a variable's coefficients already match or are opposite — it is faster than isolating a variable first.",
      question: "The system $x+y=8$ and $x-y=2$ has solution $(x,y)$. What is the value of $x$?" },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Systems of linear equations sit squarely in the Grade 10 band — usually asked as \"at what $x$-value do these two lines meet?\" or as a short algebraic solve.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Set the two expressions for $y$ equal to each other first — it collapses the system into the one-variable equation you already know how to solve.",
      question: "Line $f$ has equation $y=x+3$ and line $g$ has equation $y=-2x+9$. Graphed together, the two lines cross at $x=$ ?" },
    { code: "SAT", full: "College Board", skill: "Systems of two linear equations in two variables — one of the most heavily tested Algebra sub-skills, often asking for a combination like $x+y$ rather than each variable separately.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "If the question asks for a COMBINATION of the variables, check whether adding or subtracting the equations gets you there directly, without solving for $x$ and $y$ individually.",
      question: "If $2x+3y=12$ and $x-y=1$, what is the value of $x+y$?" },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the solution to a system is the ONE point — or region — that makes EVERY equation or inequality true at once; check it by substituting back into ALL of them, not just one."],

  summary: [
    "State that a system's solution is an ordered pair $(x,y)$ satisfying every equation at once — one solution, no solution, or infinitely many.",
    "Solve a system of two linear equations by substitution, by elimination, and by graphing, and confirm all three agree.",
    "Graph a linear inequality as a shaded half-plane, with a solid or dashed boundary line.",
    "Graph a system of inequalities and identify its feasible region as the overlap of every shading.",
    "Model a real two-constraint situation as a system of inequalities and judge whether a proposed plan is feasible.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "This closes Topic 1 — the next session is the Unit Recap and Performance Task, not a new flipped video.",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on reading a system's solution as a point.",
  ],

  notes: {
    cover: "Week 6 lesson for both Grade 10 sections, closing Topic 1 (Linear Functions) after Solving Equations and Inequalities by Graphing. The Unit Recap and Unit Assessment follow next session, not a new lesson.",
    objectives: "All three objectives are verbatim from the curriculum map. The map lists HSA.REI.C.6 and HSA.CED.A.3 for this lesson, and only MP.4 and MP.3 — do not add others.",
    vocabulary: "All nine terms are the map's list. Group them aloud into three families as you go: SOLUTION words (solution, solution set), METHOD words (substitution, elimination), and INEQUALITY words (linear inequality, boundary line, system of linear inequalities, feasible region) — the grouping is the fastest way into a nine-term list.",
    prior: "If a student cannot isolate a variable in a one-step equation cold, both substitution and elimination will stall. Watch for it in the diagnostic, question 1.",
    diagnose: "Answers: $x=4$; slope $-3$, $y$-intercept $4$; yes, same slope $2$, so the lines are parallel and never meet; $(0,0)$ is NOT a solution to $y>x+1$ since $0>1$ is false; lines $f$ and $g$ meet at $x=2$ (both give $y=3$). Expected gap: Q3, where students confuse \"same slope\" with \"they meet somewhere far away\" rather than \"they never meet.\"",
    quickCheck: "Answer: $x=4,\\ y=1$ (from $2x+y=9$ and $x-y=3$, adding gives $3x=12$). Watch for students who add instead of subtract, or subtract instead of add, without checking which operation actually cancels a variable.",
    guided: "Answers — 1: $y=x+2$, $3x+y=18$ substitutes to $3x+(x+2)=18 \\to x=4,\\ y=6$. 2: $y<x+3$ (dashed) and $y\\ge -2x+1$ (solid) — feasible region is the wedge above the solid line and below the dashed line. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) $x+y\\le 40$ (land), $3x+5y\\le 150$ (water). (b) the feasible region is the polygon bounded by both lines and the axes, in the first quadrant. (c) $x=25,\\ y=10$: land $35\\le 40$ true, water $3(25)+5(10)=125\\le 150$ true — FEASIBLE. (d) the worker has ignored the water constraint — for instance all 40 hectares in alfalfa needs $5(40)=200$ water units, which exceeds the 150-unit supply, so not every land-only plan is actually deliverable.",
    geogebra: "The moment the slider makes both slopes equal, GeoGebra's Intersect tool fails to return a point — that failure IS the parallel-lines case, made concrete instead of just described.",
    gate: "Answers: Q1 $x+y=7$, $2x-y=2$ gives $x=3,\\ y=4$ (check: $3+4=7$, $2(3)-4=2$). Q2 many points work — for instance $(0,0)$: $0\\le 7$ true, $0>-2$ true. Q3: because a system of INEQUALITIES accepts every point in a whole shaded region, not just the single point where the two BOUNDARY lines happen to cross — the crossing point is only one corner of that region. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — a plan that respects land but not water is exactly the kind of single-constraint thinking a real farm planner has to avoid.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  await build(GR10_L6);
})();

module.exports = { GR10_L6 };

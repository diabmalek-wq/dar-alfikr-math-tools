// Grade 10 · Topic 1 · Lesson 6 — Linear Systems
// FIKR lesson plan, Lesson plan 2026/27, classwork, differentiation activity,
// PBL task.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread — and the SAME Al-Ahsa
// farm context and numbers — as lessons_w6.js. See the standing alignment
// rule noted there.
const { buildAll } = require("../../engines/docs_engine");

const MATHDOC = "math_w6_doc/_index.json";
const GRAPH = "graphs_w6/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I've shaded the correct side of each boundary line, and challenge any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to solving systems, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "This lesson closes Topic 1. If time runs short, cut Smart Production and carry it into the next session — never the Mastery Gate, which is the evidence.";

// =====================================================================
// GR10 · T1 L6 · Linear Systems
// =====================================================================
const GR10_L6 = {
  slug: "Gr10_T1_L6_Linear_Systems",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Linear Systems",
  unit: "Topic 1 — Linear Functions · Lesson 6",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 6 · Semester 1, 2026–27",
  weekNum: "6",
  lessonLine: "Grade 10 · Algebra II · Topic 1: Linear Functions · Lesson 6 — Linear Systems",
  codes: ["HSA.REI.C.6", "HSA.CED.A.3"],
  mps: ["MP.4", "MP.3"],
  assessments: ASSESS,
  objectives: [
    "Visualize and interpret solutions of systems of linear equations in two variables.",
    "Solve systems of linear equations both algebraically and graphically.",
    "Identify and describe graphically the regions that satisfy systems of inequalities.",
  ],
  essentialQuestion: "How can the concepts of linear systems be used to solve real-world problems?",
  vocabList: "system of linear equations ; solution (of a system of linear equations) ; solution set ; substitution ; elimination ; linear inequality ; boundary line ; system of linear inequalities ; feasible region",

  plan: {
    outcome: [
      "Students will state that a system's solution is an ordered pair $(x,y)$ satisfying every equation at once — one solution, no solution, or infinitely many.",
      "Students will solve a system of two linear equations by substitution, by elimination, and by graphing, and confirm all three agree.",
      "Students will graph a system of linear inequalities and identify its feasible region as the overlap of every shading.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “One point, two lines” — what it means for an ordered pair to satisfy two equations at once, building directly on Lesson 1-5's single-equation graphing. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one slope-intercept recall, one one-variable equation solve.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz ($\\le 4$ minutes): solve $2x+3=11$ for $x$; state the slope and $y$-intercept of $y=-3x+4$; decide whether $y=2x-1$ and $y=2x+5$ share a slope and will ever meet; decide whether $(0,0)$ solves $y>x+1$; read from a small table at which input two lines $f$ and $g$ meet.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: $x=4$; slope $-3$, $y$-intercept $4$; same slope $2$, so they never meet; $(0,0)$ is NOT a solution since $0>1$ is false; $f$ and $g$ meet at input $2$.",
    ],
    diagGap: [
      "Expected gap 1 — a student who cannot isolate a variable in a one-step equation cold; both substitution and elimination stall immediately without this.",
      "Expected gap 2 — confusing \"same slope\" with \"they meet somewhere far away\" instead of \"they never meet\".",
      "Expected gap 3 — Q4, which decides whether a student can test a point against an inequality rather than just estimating from a picture.",
      "Routing: 0–2 correct → re-teach isolating a variable.  3–4 → straight to solving systems.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): a system's solution is not a new idea from scratch — it is Lesson 1-5's crossing point, except the FULL ordered pair is now the answer, not just $x$.",
      "Whole class, REI.C.6 (Objective 1): read a system's solution as the ordered pair $(x,y)$ where two lines cross, and classify the three cases — one crossing point (one solution), same slope with different $y$-intercepts (parallel, no solution), same slope and same $y$-intercept (coincident, infinitely many solutions).",
      "Whole class, REI.C.6 (Objective 2): solve ONE system — $x+y=7$ and $x-y=1$ — three ways: substitution ($y=7-x$, then $x-(7-x)=1$), elimination (add the equations so $y$ cancels), and graphing (plot both lines). All three land on $x=4,\\ y=3$.",
      "Whole class, CED.A.3 (Objective 3): graph the system $y\\le -x+6$ and $y> 2x-1$ — solid boundary for $\\le$, dashed for $>$ — and shade the feasible region where both hold. Test $(0,3)$ (feasible) against $(4,4)$ (not feasible, since $4\\le 2$ is false).",
      "Narration focus — after ANY algebraic solve, say the check out loud: substitute both values into BOTH original equations, not just one.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: solve $2x+y=9$ and $x-y=3$ by elimination.",
      "Expected: $x=4,\\ y=1$. Watch for students who add when they should subtract, or vice versa, without checking which operation actually cancels a variable.",
      "80% correct → release guided practice. Below 80% → one further modelled example, this time by substitution.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) $y=x+2$ and $3x+y=18$ — solve by substitution.  (2) $y<x+3$ and $y\\ge -2x+1$ — graph and shade the feasible region.",
      "Answers: (1) $3x+(x+2)=18 \\to x=4,\\ y=6$. (2) dashed line $y=x+3$, solid line $y=-2x+1$, feasible region is the wedge above the solid line and below the dashed line.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Four systems solved by substitution or elimination, two graphed with the crossing point marked, one answer verified by substitution. Done when: your $x$- and $y$-values satisfy BOTH original equations.",
      "APPLY — Use it in context. A two-plan cost comparison solved algebraically, and a system of inequalities graphed with a test point checked. Done when: your inequality answer is a shaded region, not a point, and the context answer carries the right units.",
      "INVESTIGATE — Find out why. Arguing from slope why parallel lines share no solution, constructing an example with infinitely many solutions, and sketching a system of inequalities with no feasible region at all. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A farm in the Al-Ahsa Oasis is planning this season's planting of dates and alfalfa, as part of the Kingdom's push for local food security. The farm has 40 hectares of land available, and its irrigation system can deliver at most 150 water units this season. Each hectare of dates needs 3 water units; each hectare of alfalfa needs 5 water units.",
      "(a) Write both constraints as inequalities, using $x$ for hectares of dates and $y$ for hectares of alfalfa. (b) Graph the system and shade the feasible region. (c) Is a plan of 25 hectares of dates and 10 hectares of alfalfa feasible? Justify using BOTH constraints. (d) A worker says “just use up all 40 hectares, plant however you like.” Explain in one sentence why that is not always possible.",
      "Answers: (a) $x+y\\le 40$ (land), $3x+5y\\le 150$ (water). (b) the feasible region is the polygon bounded by both lines and the axes in the first quadrant. (c) $x=25,\\ y=10$: land $35\\le 40$ true, water $3(25)+5(10)=125\\le 150$ true — FEASIBLE. (d) the worker has ignored the water constraint — all 40 hectares in alfalfa alone needs $5(40)=200$ water units, more than the 150-unit supply, so not every land-only plan is actually deliverable.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: both constraints written as inequalities (not described in words only), the feasible region shaded on a correctly scaled graph, and a written reason — not just yes or no — for parts (c) and (d).",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (c) and (d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. Solve the system $x+y=7$ and $2x-y=2$ — find $x$ and $y$. 2. The same two lines now form the system of inequalities $y\\le 7-x$ and $y> 2x-2$ — name ONE point in the feasible region. 3. In ONE sentence, explain why the boundary lines having exactly one crossing point does not mean the system of inequalities has only one solution.",
      "Answers: 1. $x=3,\\ y=4$ (check: $3+4=7$, $2(3)-4=2$). 2. many points work, for instance $(0,0)$: $0\\le 7$ true, $0>-2$ true. 3. a system of inequalities accepts every point in a whole shaded region, not just the single point where the two boundary lines cross — that crossing point is only one corner of the region.",
      "Done when: question 1 is checked in both original equations, not left unchecked, and question 3 gives a definition-based reason, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their farm-plot reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: both constraints as inequalities, the shaded feasible region, and the feasibility judgment for parts (c) and (d); ONE worked non-example — a plan that satisfies the land limit but breaks the water limit — with a sentence on how a reader would spot it; and a caption on why a plan needs to be checked against EVERY constraint, not just one.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 1 modelling set.",
      "Reflection question: “Which is still harder for you — solving a system algebraically, or reading a feasible region correctly off a graph?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Four systems solved by substitution or elimination, two graphed with the crossing point marked; a partner is allowed. Done when: every $x$- and $y$-value satisfies BOTH original equations.",
      "APPLY — Use it in context. The two-plan cost comparison and a system of inequalities graphed with a test point checked. Done when: the inequality answer is a shaded region and the context answer carries the right units.",
      "INVESTIGATE — Find out why. The parallel-lines argument, the infinitely-many-solutions example, and the no-feasible-region sketch. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: an Al-Ahsa Oasis farm's dates-and-alfalfa planting plan, modelled with a system of linear inequalities, supporting local food-security goals.",
      "In-class Apply-route item: a two-provider internet-plan cost comparison solved as a system of linear equations, in SAR and GB.",
      "Discussion prompt: why a real plan must be checked against EVERY constraint at once, not just the one that happens to be easiest to compute.",
    ],
    exams: [
      "GAT (Qudurat) — solving a small system of two linear equations quickly, under time pressure and without a graphing tool. Practice tip: add or subtract the two equations directly when a variable's coefficients already match or are opposite.",
      "SAAT (Tahsili) — systems of linear equations sit squarely in the Grade 10 band, usually asked as \"at what $x$-value do these two lines meet?\" Practice tip: set both expressions for $y$ equal to each other first.",
      "SAT — Advanced Math, systems of two linear equations, one of the most heavily tested Algebra sub-skills, often asking for a combination like $x+y$ rather than each variable separately. Practice tip: check whether adding or subtracting the equations reaches the requested combination directly.",
    ],
  },

  plan2026: {
    day: "Wednesday, Week 6", section: "Grade 10-A",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Planning a Farm Plot” project task · squared paper",
    competencies: ["Solving a system of two linear equations by substitution, elimination, and graphing.", "Graphing a system of linear inequalities and identifying its feasible region."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders showing lines becoming parallel, and the equivalent inequality shading."],
    reallife: ["An Al-Ahsa Oasis farm's dates-and-alfalfa planting plan under land and water constraints, part of local food-security goals.", "Comparing two internet data plans to find the usage level where costs match."],
    values: ["Precision — checking a solution in BOTH original equations, not one.", "Diligence — testing a plan against EVERY constraint, not just the first one checked."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a feasible region, not a single point, answers a system of inequalities."],
    hard: ["Solving a system of two linear equations by three methods and confirming they agree.", "Graphing a system of linear inequalities and identifying the feasible region."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on isolating a variable, reading slope and intercept, comparing slopes, and testing a point against an inequality. Results read as a gap map; students routed to the re-teach table, straight to solving systems, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on isolating a variable for flagged students. Whole class: reading a system's solution as a point; solving one system three ways; graphing a system of inequalities and finding the feasible region. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The Al-Ahsa farm plot: both constraints as inequalities, the feasible region, and a feasibility judgment with reasoning. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — a system solved algebraically, a feasible point named for the matching inequality system, and a one-sentence justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which is still harder for you — solving a system algebraically, or reading a feasible region correctly off a graph?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. This closes Topic 1 — the Unit Recap and Performance Task follow next session, not a new flipped video.",
  },

  classwork: {
    subtitle: "Show every step. Substitution and elimination both end with a one-variable equation — write it before you solve it.",
    sections: [
      { h: "SECTION 1 — Solving by substitution", note: "Objective 2", lines: 4,
        q: [
          { n: "Q1", eq: "sy_cw1", t: "Solve by substitution.", k: 0.85 },
          { n: "Q2", eq: "sy_cw2", t: "Solve by substitution.", k: 0.85 },
        ] },
      { h: "SECTION 2 — Solving by elimination", note: "Objective 2", lines: 4,
        intro: "Look for a variable whose coefficients already match or are opposite before you add or subtract.",
        q: [
          { n: "Q3", eq: "sy_cw3", t: "Solve by elimination.", k: 0.85 },
          { n: "Q4", eq: "sy_cw4", t: "Solve by elimination.", k: 0.85 },
        ] },
      { h: "SECTION 3 — Reading and classifying systems", note: "Objective 1", lines: 4,
        graph: "g_cw_sys", graphW: 340,
        q: [
          { n: "Q5", eq: "sy_cw5", t: "How many solutions does this system have? Justify from the slopes.", k: 0.85 },
          { n: "Q6", eq: "sy_cw6", t: "How many solutions does this system have? Justify — write both equations in slope-intercept form first.", k: 0.85 },
        ],
        text: [
          "Q7.  From the graph above, state the solution to the system shown.",
        ] },
      { h: "SECTION 4 — A charity fair in SAR", note: "MP.4 · the real-world objective", lines: 5,
        intro: "A school club sells posters for 7 SAR and bookmarks for 3 SAR at a charity fair. The club needs total sales of at least 210 SAR, and the display table can hold at most 40 items at once.",
        text: [
          "Q8.  Write both constraints as inequalities, using $p$ for posters and $b$ for bookmarks.",
          "Q9.  Graph the system and shade the feasible region.",
          "Q10.  Is a display of 20 posters and 15 bookmarks a feasible plan? Justify using both constraints.",
          "Q11.  Give ONE combination of posters and bookmarks that IS feasible, and check both constraints.",
        ],
        graph: "g_cw_poster", graphW: 420 },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Four systems, your method", done: "your $x$- and $y$-values satisfy BOTH original equations when you substitute them back in.",
        intro: "Solve each system by substitution or elimination — your choice. Check each answer in both original equations.",
        grid: [["1.", "sy_ws1"], ["2.", "sy_ws2"], ["3.", "sy_ws3"], ["4.", "sy_ws4"], ["5.", "sy_qc"], ["6.", "sy_g1"]],
        tasks: ["7.  Graph any TWO of the systems above on the same axes as their algebraic solution, and mark the crossing point."],
        lines: 2 },
      { note: "A context, and a feasible region", done: "your inequality answer is a shaded region, not a single point, and your context answer carries both SAR and GB.",
        graph: "g_sys_ineq", graphW: 380,
        tasks: [
          "1.  Two internet plans: Plan $A$ costs $50+2g$ SAR, Plan $B$ costs $20+5g$ SAR, for $g$ GB of data. Find, algebraically, where the two plans cost the same, in SAR and GB.",
          "2.  Solve graphically: $y=-2x+8$ and $y=x-1$ — state the crossing point.",
          "3.  Graph the system $y\\le -x+7$ and $y> x-1$, and shade the feasible region.",
          "4.  Test whether the point $(2,2)$ lies inside the feasible region you shaded in Q3.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          ["1.  Explain, using slope, why two lines with the same slope but different $y$-intercepts, such as ", { eq: "sy_parallel_pair", k: 0.9 }, ", can never be a system's solution."],
          "2.  A system of two linear equations has infinitely many solutions. What must be true about the two equations? Give your own example.",
          "3.  A system of two inequalities has NO feasible region at all. Sketch an example and explain, using the boundary lines, why no point can satisfy both.",
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Planning a Farm Plot in Al-Ahsa", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A farm has a land limit AND a water limit. If a plan fits inside one limit, does that automatically mean it is deliverable?",
    situation: [
      "A farm in the Al-Ahsa Oasis is planning this season's planting of dates and alfalfa, as part of the Kingdom's push for local food security.",
      "The farm has 40 hectares of land available, and its irrigation system can deliver at most 150 water units this season. Each hectare of dates needs 3 water units; each hectare of alfalfa needs 5 water units.",
      "A group of Grade 10 students is asked to check candidate planting plans and recommend one that is actually deliverable.",
    ],
    eq: "sy_farm",
    steps: [
      ["1", "WRITE THE MODEL  (4 min)", "Write both constraints as inequalities, using $x$ for hectares of dates and $y$ for hectares of alfalfa."],
      ["2", "GRAPH THE REGION  (5 min)", "Graph the system and shade the feasible region — the combinations of $x$ and $y$ the farm can actually plant."],
      ["3", "TEST A PLAN  (4 min)", "Check whether 25 hectares of dates and 10 hectares of alfalfa is feasible, showing both constraints."],
      ["4", "FIND THE TRAP  (4 min)", "Find one combination that respects the land limit but breaks the water limit, and explain why it fails."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: why a plan has to be checked against BOTH limits, not just one."],
    ],
    working: [["Step 1 — both constraints:", 2], ["Step 2 — the feasible region, described:", 3],
              ["Step 3 — the 25-and-10 plan, checked:", 3], ["Step 4 — the trap combination:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the two constraints", "Grapher — sketches the feasible region", "Checker — tests both candidate plans", "Presenter — says the sentence"],
    doneWhen: ["Both constraints are written as inequalities, not just described.", "The feasible region is shaded, not just outlined.", "Both the 25-and-10 plan and the trap combination are checked against BOTH constraints.", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR10_L6);
})();

module.exports = { GR10_L6 };

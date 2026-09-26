// Grade 10 · Topic 2 · Lesson 1 — Vertex Form of a Quadratic Function
// FIKR lesson plan, Lesson plan 2026/27, classwork, differentiation activity,
// PBL task.
//
// Objectives / EQ / vocabulary / assessments verbatim from the curriculum
// map. This suite shares the same objective thread — and the SAME park
// fountain context and numbers — as lessons_w7.js. See the standing
// alignment rule noted there.
const { buildAll } = require("../../engines/docs_engine");

const MATHDOC = "math_w7_doc/_index.json";
const GRAPH = "graphs_w7/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];
const T = { t1: 6, t2: 18, t3: 12, t4: 12, t5: 6, t6: 6 };

const AI_CRITIC = "Role of AI: critic only. Briefed prompt — “Check whether I used the correct point to solve for a, and challenge any step I have not justified.” Never “solve this”.";
const PILLAR_ADAPTIVE = [
  "Entry branch — the Quizizz result routes each student to the re-teach table, straight to vertex form, or the Investigate prompt.",
  "Mid-lesson branch — Pear Deck flags error patterns during independent practice; flagged students get a 2-minute micro-conference while others continue.",
  "Exit branch — the Mastery Gate routes each student: PASS → Enrichment & Challenge; NOT YET → Targeted Learning Clinic at the start of the next lesson.",
  "Routing is communicated privately through the LMS, never read aloud.",
];
const WEEK_NOTE = "This lesson opens Topic 2. Take extra care with the sign-of-h misconception in Phase 2 — it recurs all topic.";

// =====================================================================
// GR10 · T2 L1 · Vertex Form of a Quadratic Function
// =====================================================================
const GR10_L21 = {
  slug: "Gr10_T2_L1_Vertex_Form_of_a_Quadratic_Function",
  mathDocIndex: MATHDOC, graphIndex: GRAPH, timings: T,
  lessonTitle: "Vertex Form of a Quadratic Function",
  unit: "Topic 2 — Quadratic Functions and Equations · Lesson 1",
  gradeFull: "Grade 10 — Algebra II",
  week: "Week 7 · Semester 1, 2026–27",
  weekNum: "7",
  lessonLine: "Grade 10 · Algebra II · Topic 2: Quadratic Functions and Equations · Lesson 1 — Vertex Form of a Quadratic Function",
  codes: ["HSA.REI.B.4", "HSA.REI.B.4.A", "HSF.IF.C.7.A", "HSA.CED.A.2", "HSF.IF.B.4", "HSF.BF.B.3"],
  mps: ["MP.4", "MP.5"],
  assessments: ASSESS,
  objectives: [
    "Graph quadratic functions given in vertex form.",
    "Write a quadratic function in vertex form given its key features.",
  ],
  essentialQuestion: "What are the key features of a transformation of the parent quadratic function?",
  vocabList: "parabola ; parent quadratic function ; quadratic function ; vertex ; vertex form ; axis of symmetry ; minimum point ; minimum value ; maximum point ; maximum value",

  plan: {
    outcome: [
      "Students will read the vertex, axis of symmetry, and max/min directly off a quadratic function's vertex form.",
      "Students will graph a quadratic function given in vertex form as a transformation of the parent function $y=x^{2}$.",
      "Students will write a quadratic function in vertex form given its vertex and one other point.",
      WEEK_NOTE,
    ],
    preclass: [
      "Flipped video (4 min): “The $x^{2}$ in disguise” — every parabola is the parent function transformed, using exactly the same shift/stretch language as Lesson 1-2. Posted on the LMS 48 hours ahead.",
      "Two embedded EdPuzzle questions: one transformation-description recall, one function-evaluation recall.",
      "Evidence of readiness: EdPuzzle completion report plus both embedded answers submitted before the bell.",
    ],
    diagTool: [
      "5-question Quizizz ($\\le 4$ minutes): describe the transformation in $y=f(x)+3$; describe the transformation in $y=f(x-2)$; evaluate $f(x)=x^2$ at $x=-3$; state the vertex of $y=(x-1)^2+4$ by inspection; decide whether $y=-3(x+2)^2-1$ opens up or down.",
      "Cross-referenced against overnight EdPuzzle watch analytics — who watched, who skipped, who missed the embedded items.",
      "Answers: shift up 3; shift right 2; $f(-3)=9$; vertex $(1,4)$; opens down.",
    ],
    diagGap: [
      "Expected gap 1 — a student who cannot describe $f(x-h)+k$ as a shift from Lesson 1-2; vertex form will look like an entirely new idea instead of familiar transformations renamed.",
      "Expected gap 2 — Q4, where students read the vertex correctly here but will need the SAME sign-flip skill applied consistently to different examples later in the lesson.",
      "Expected gap 3 — a student unsure how the sign of $a$ alone decides opening direction, independent of $h$ and $k$.",
      "Routing: 0–2 correct → re-teach transformations.  3–4 → straight to vertex form.  5 → begin the Investigate prompt immediately.",
    ],
    instruction: [
      "Direct explanation (3–5 min, flagged students only): vertex form is not a new shape to memorise — it is the parent function $y=x^2$, transformed, with the transformation parameters visible right in the equation.",
      "Whole class, IF.C.7.A/IF.B.4 (Objective 1, part 1): read the vertex, axis of symmetry, and max/min straight off three vertex-form functions — $f(x)=2(x-3)^2+4$, $g(x)=-(x+1)^2+5$, $h(x)=(1⁄2)x^2-2$ — naming the sign-of-$h$ trap explicitly.",
      "Whole class, BF.B.3 (Objective 1, part 2): graph $f(x)=2(x-3)^2+4$ as three moves from the parent function — shift right 3, shift up 4, stretch by a factor of 2 — using the same transformation language as Lesson 1-2.",
      "Whole class, CED.A.2/REI.B.4.A (Objective 2): write vertex form from a vertex and one other point — vertex $(2,-3)$, point $(4,5)$ — placing the vertex first, then solving for $a$ from the other point.",
      "Narration focus — say the sign flip for $h$ out loud EVERY time: $(x+1)^2=(x-(-1))^2$ has $h=-1$, not $h=1$.",
      "This is a NEW example — it does not repeat the flipped video.",
    ],
    quickCheck: [
      "On whiteboards, 60 seconds: state the vertex of $f(x)=-2(x+5)^2+7$, and whether it's a max or min.",
      "Expected: vertex $(-5,7)$, maximum (since $a=-2<0$). Watch for students who find the vertex correctly but forget to check the sign of $a$ before naming max or min.",
      "80% correct → release guided practice. Below 80% → one further modelled example, reading $a$, $h$, $k$ slowly together.",
    ],
    guided: [
      "Two “Give it a go” problems, identical for every student, worked together with the teacher:",
      "(1) $f(x)=(x-2)^2-3$ — graph using transformations.  (2) vertex $(-1,4)$, point $(1,-4)$ — write vertex form.",
      "Answers: (1) parent shifted right 2, down 3, no stretch. (2) $-4=a(1-(-1))^2+4=4a+4 \\to a=-2$, so $f(x)=-2(x+1)^2+4$.",
      "Feedback: worked live on the board step by step; students self-mark and circle their OWN first error.",
    ],
    independent: [
      "Delivered through the “Choose Your Route” sheet with live feedback in Pear Deck. Routes are named for the task, not for the student.",
      "PRACTICE — Secure the method. Three functions read for key features, one graphed by transformation, one vertex form written from a vertex and a point. Done when: every vertex matches the sign convention, and the written equation passes through both given points.",
      "APPLY — Use it in context. A basketball's path read for its maximum, and a fountain's height function written and evaluated at two distances. Done when: height answers carry units, and the equation is checked at the nozzle point.",
      "INVESTIGATE — Find out why. Comparing two parabolas with the same vertex and different $a$, arguing why a negative $a$ forces a maximum, and proving the vertex of $f(x)=a(x-h)^2+k$ is $(h,k)$ by evaluating $f(h)$. Done when: you have an argument, not just an answer.",
      "Every student sits the same Mastery Gate. The gate is not differentiated, because it is the evidence.",
    ],
    production: [
      "Non-routine transfer task — this context has not appeared in practice.",
      "A decorative fountain in a neighbourhood park shoots a jet of water in a parabolic arc. The water reaches a maximum height of 4 metres at a horizontal distance of 2 metres from the nozzle, and lands back at ground level 4 metres from the nozzle. The nozzle itself sits at ground level.",
      "(a) State the vertex of the height function, and explain how you know it is a maximum. (b) Use the nozzle point $(0,0)$ to solve for $a$, and write the vertex form of the height function. (c) Find the water's height at 1 metre and at 3 metres from the nozzle. (d) A designer says “the water is always highest exactly halfway between where it leaves and lands.” Explain in one sentence why this is true, using the axis of symmetry.",
      "Answers: (a) vertex $(2,4)$; maximum, since the water rises then falls back to ground level. (b) $0=a(0-2)^2+4 \\to a=-1$, so $h(x)=-(x-2)^2+4$. (c) $h(1)=3$ metres; $h(3)=3$ metres — symmetric about the axis. (d) the axis of symmetry $x=2$ sits exactly halfway between the two ground points by definition, so the vertex (the peak) always falls exactly there.",
      "Students then hand their reasoning to the AI critic and ask it to challenge any step they have not justified.",
    ],
    criteria: [
      "Minimum acceptable standard: the value of $a$ shown as solved algebraically (not guessed or estimated from the graph), and part (d) answered by naming the axis of symmetry, not just restating the observation.",
      AI_CRITIC,
      "Completed independently by the student: the written justification for parts (a) and (d). AI may challenge it; it may not write it.",
    ],
    evidence: [
      "“Time to Check” — one individual task. No notes, no partner, no AI.",
      "1. State the vertex, axis of symmetry, and max/min for $f(x)=3(x-1)^2-2$. 2. Write the vertex form of a parabola with vertex $(2,5)$ passing through $(0,1)$. 3. In ONE sentence, explain how you can tell from vertex form alone whether a parabola opens up or down.",
      "Answers: 1. vertex $(1,-2)$, axis $x=1$, minimum (since $a=3>0$). 2. $1=a(0-2)^2+5=4a+5 \\to a=-1$, so $f(x)=-(x-2)^2+5$. 3. the sign of $a$ tells you directly — positive opens up, negative opens down.",
      "Done when: question 2 is checked against the given point, not left unverified, and question 3 gives a definition-based reason, not an example.",
      "Scored live in Pear Deck as submissions arrive; result logged in the Impact Dashboard Mastery Rate.",
    ],
    refinement: [
      "Students revise their fountain reasoning using the AI critique and the teacher's micro-conference note.",
      "Final product, three equally acceptable formats: a Canva one-pager, a photographed hand-written solution, or a 45-second voice note.",
      "Required content: the vertex identified as a maximum with reasoning, the value of $a$ solved algebraically, both requested heights, and ONE worked non-example — misreading the vertex of $(x+2)^2+4$ as $(2,4)$ instead of $(-2,4)$ — with a sentence on how a reader would spot the sign error.",
      "Graded on originality and clarity of reasoning, not correctness alone.",
    ],
    publication: [
      "Published to the class LMS portfolio; the strongest go on the Mathematics Department wall as the Topic 2 opening modelling set.",
      "Reflection question: “Which part is still harder for you — reading key features off vertex form, or writing the equation from a vertex and a point?”",
    ],
    differentiation: [
      "PRACTICE — Secure the method. Three functions read for key features, one graphed by transformation, one vertex form written from a vertex and a point; a partner is allowed. Done when: every vertex matches the sign convention and the written equation checks against its point.",
      "APPLY — Use it in context. The basketball's maximum height, and the fountain's equation written and evaluated. Done when: heights carry units and the equation is checked at a known point.",
      "INVESTIGATE — Find out why. The same-vertex comparison, the negative-$a$ argument, and the $f(h)=k$ proof. Done when: there is an argument, not just an answer.",
      "No student is labelled. The routes describe tasks; every student sits the same Mastery Gate.",
    ],
    adaptive: PILLAR_ADAPTIVE,
    saudi: [
      "Production context: a neighbourhood park's decorative fountain, its water arc modelled and solved in vertex form.",
      "In-class Apply-route item: a basketball's flight path read for its maximum height and location.",
      "Discussion prompt: why a parabola's symmetry means its peak always falls exactly halfway between two equal-height points, such as where a fountain's water leaves and lands.",
    ],
    exams: [
      "GAT (Qudurat) — reading the vertex directly off vertex form, meant to be answered in seconds. Practice tip: flip the sign inside the parentheses for $h$ — that single step is where most errors happen under time pressure.",
      "SAAT (Tahsili) — finding a maximum or minimum value from vertex form, a core Grade 10 skill. Practice tip: check the sign of $a$ first, before looking at $k$.",
      "SAT — Advanced Math, writing a quadratic's equation from its vertex and one other point, a recurring item type. Practice tip: put the vertex into $a(x-h)^2+k$ first, then substitute the other point.",
    ],
  },

  plan2026: {
    day: "Sunday, Week 7", section: "Grade 10-A",
    tools: "Quizizz (diagnostic) · Pear Deck (live practice feedback) · GeoGebra Graphing Calculator · Canva (final product) · Whiteboards",
    resources: "Lesson presentation (18 slides) · “Choose Your Route” differentiation sheet · “Designing a Park Fountain's Arc” project task · squared paper",
    competencies: ["Reading the vertex, axis of symmetry, and max/min directly off vertex form.", "Graphing a quadratic in vertex form as a transformation of the parent function, and writing vertex form from a vertex and a point."],
    technology: ["Quizizz live diagnostic with instant gap analysis.", "GeoGebra sliders showing the vertex move with $h$ and $k$, and the parabola flip as $a$ crosses zero."],
    reallife: ["A neighbourhood park's decorative fountain, modelled and solved in vertex form.", "A basketball's flight path, read for its maximum height and location."],
    values: ["Precision — checking the sign flip on $h$ every time, not just when it's convenient.", "Rigor — solving for $a$ algebraically rather than estimating it from a sketch."],
    soft: ["Collaboration in assigned group roles.", "Explaining why a parabola's peak falls exactly at its axis of symmetry."],
    hard: ["Reading key features directly off vertex form.", "Graphing a transformation of the parent quadratic function, and writing vertex form from given key features."],
    phases: [
      "FIKR Phase 1 — Diagnose. 5-question Quizizz on describing transformations, evaluating a function, and reading a vertex by inspection. Results read as a gap map; students routed to the re-teach table, straight to vertex form, or the Investigate prompt.",
      "FIKR Phase 2 — Targeted Instruction. Focused re-teach on transformation language for flagged students. Whole class: reading key features off vertex form; graphing as a transformation of the parent function; writing vertex form from a vertex and a point. Quick check on whiteboards.",
      "FIKR Phase 3 — Practice. Two identical “Give it a go” problems worked together. Students then choose a route and may switch at any time. Live feedback via Pear Deck; 2-minute micro-conferences.",
      "FIKR Phase 4 — Production. The park fountain's vertex, the value of $a$ solved algebraically, and the height at two distances. AI used as critic only.",
      "FIKR Phase 5 — Proof of Learning. “Time to Check” — key features read from vertex form, an equation written from a vertex and a point, and a one-sentence justification. No notes, no partner, no AI.",
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
    closure: "Two minutes of peer show-and-tell on the final products, then the reflection question: “Which part is still harder for you — reading key features off vertex form, or writing the equation from a vertex and a point?”",
    homework: "Finish the final product and upload to the LMS portfolio (any of the three formats). Practice set on Pear Deck — 12 questions, choose your route. Watch the flipped video for our next lesson, Topic 2 · Lesson 2 — Standard Form of a Quadratic Function.",
  },

  classwork: {
    subtitle: "Show every step. State the vertex first, before anything else — every other feature follows from it.",
    sections: [
      { h: "SECTION 1 — Reading key features", note: "Objective 1", lines: 4,
        q: [
          { n: "Q1", eq: "vf_cw1", t: "State the vertex, axis of symmetry, and max or min.", k: 1.1 },
          { n: "Q2", eq: "vf_cw2", t: "State the vertex, axis of symmetry, and max or min.", k: 1.1 },
        ] },
      { h: "SECTION 2 — Graphing by transformation", note: "Objective 1", lines: 5,
        intro: "Describe the transformation from the parent function in words, then sketch the graph on the grid provided.",
        q: [
          { n: "Q3", eq: "vf_cw3", t: "Graph using transformations from the parent function.", k: 1.1 },
          { n: "Q4", eq: "vf_cw4", t: "Graph using transformations from the parent function.", k: 1.1 },
        ] },
      { h: "SECTION 3 — Writing vertex form", note: "Objective 2", lines: 4,
        intro: "Place the vertex in the equation first, then substitute the other point to solve for $a$.",
        q: [
          { n: "Q5", eq: "vf_cw5", t: "Write the vertex form of the parabola with this vertex and point.", k: 0.85 },
          { n: "Q6", eq: "vf_cw6", t: "Write the vertex form of the parabola with this vertex and point.", k: 0.85 },
        ] },
      { h: "SECTION 4 — A fountain in Riyadh", note: "MP.4 · the real-world objective", lines: 5,
        intro: "A different park fountain reaches a maximum height of 5 metres at a horizontal distance of 3 metres from its nozzle, which sits at ground level.",
        text: [
          "Q7.  State the vertex of the height function.",
          "Q8.  Use the nozzle point $(0,0)$ to solve for $a$, and write the vertex form of the height function.",
          "Q9.  Find the water's height at a horizontal distance of 1 metre from the nozzle.",
          "Q10.  At what horizontal distance does the water land back at ground level? Use the axis of symmetry to answer without solving an equation.",
        ],
        graph: "g_fountain", graphW: 340 },
    ],
  },

  diffSheet: {
    routes: [
      { note: "Read, graph, and write", done: "every vertex you state matches the sign convention exactly, and your written equation passes through both given points.",
        intro: "For each function, state the vertex, axis of symmetry, and whether it's a max or min.",
        grid: [["1.", "vf_ws1"], ["2.", "vf_ws2"], ["3.", "vf_ws3"], ["4.", "vf_ws4"], ["5.", "vf_qc"], ["6.", "vf_g2"]],
        tasks: ["7.  Graph any ONE of the functions above using transformations from the parent function."],
        lines: 2 },
      { note: "Contexts, and a fountain", done: "your height answers carry units (metres), and your equation is checked at the nozzle point.",
        graph: "g_fountain", graphW: 380,
        tasks: [
          "1.  A basketball's path is modeled by $h(x)=-0.5(x-3)^{2}+5$ (where $x$ is the horizontal distance in metres and $h$ is the height in metres). State the maximum height and where it occurs.",
          "2.  A decorative fountain's water jet has vertex $(2,4)$ and passes through $(0,0)$ at the nozzle. Write the vertex form of the height function.",
          "3.  Use your equation from Q2 to find the water's height at a horizontal distance of 1 metre.",
          "4.  Using the graph shown, confirm where the water lands back at ground level.",
        ], lines: 4 },
      { note: "Arguments, not answers", done: "you have an argument, not just an answer.",
        tasks: [
          "1.  Two parabolas share the same vertex but have different values of $a$. Explain how their graphs differ, and what stays exactly the same.",
          "2.  A parabola opens downward and has vertex $(3,-2)$. Explain, using the meaning of $a<0$, why $(3,-2)$ MUST be a maximum.",
          ["3.  Prove that ", { eq: "vf_def", k: 0.9 }, " always has vertex $(h,k)$, by evaluating $f(h)$ directly."],
        ], lines: 5 },
    ],
  },

  pbl: {
    title: "Designing a Park Fountain's Arc", minutes: 20,
    subtitle: "A 20-minute group project. Work in fours. Every member signs the sheet.",
    driving: "A fountain's water traces a perfect parabola. If you know only where it's highest and where it starts, can you find the whole arc — and predict its height anywhere along the way?",
    situation: [
      "A decorative fountain in a neighbourhood park shoots a jet of water in a parabolic arc.",
      "The water reaches a maximum height of 4 metres at a horizontal distance of 2 metres from the nozzle, and lands back at ground level 4 metres from the nozzle. The nozzle itself sits at ground level.",
      "A group of Grade 10 students is asked to model the arc completely and predict heights the fountain's designer has not measured directly.",
    ],
    eq: "vf_fountain",
    steps: [
      ["1", "STATE THE VERTEX  (3 min)", "State the vertex of the height function, and explain how you know it is a maximum."],
      ["2", "SOLVE FOR $a$  (5 min)", "Use the nozzle point $(0,0)$ to solve for $a$, and write the vertex form of the height function."],
      ["3", "PREDICT TWO HEIGHTS  (5 min)", "Find the water's height at 1 metre and at 3 metres from the nozzle."],
      ["4", "EXPLAIN THE SYMMETRY  (4 min)", "A designer says the water is always highest exactly halfway between where it leaves and lands. Explain why, using the axis of symmetry."],
      ["5", "PRESENT  (3 min)", "Prepare one sentence your presenter will say: how the vertex and one point are enough to model the WHOLE arc."],
    ],
    working: [["Step 1 — the vertex, justified:", 2], ["Step 2 — solving for a:", 3],
              ["Step 3 — both heights:", 3], ["Step 4 — the symmetry argument:", 3],
              ["Step 5 — our sentence:", 2]],
    roles: ["Reader — states the fountain's measurements", "Solver — finds the value of $a$", "Checker — verifies both predicted heights", "Presenter — says the sentence"],
    doneWhen: ["The vertex is stated and justified as a maximum.", "The value of $a$ is solved algebraically, not guessed.", "Both predicted heights carry units (metres).", "Your sentence makes sense to someone who does not study maths."],
    materials: ["This sheet", "Squared paper", "A pencil and ruler", "A calculator"],
  },
};

(async () => {
  await buildAll(GR10_L21);
})();

module.exports = { GR10_L21 };

// Grade 10 · Topic 2 · Lesson 1 — Vertex Form of a Quadratic Function
//
// Opens Topic 2 (Quadratic Functions and Equations), after Topic 1 (Linear
// Functions) closed with Linear Systems and its Unit Recap/Assessment.
// Objectives, essential question, vocabulary, standards and MPs are quoted
// VERBATIM from "Curriculum map A2 OBLAS.docx", Unit 2, Lesson 1.
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w7_docs.js for the matching plan/activity/PBL.
// The decorative-fountain context here is the SAME context, same numbers,
// as the PBL task and the docs' production/evidence sections.
//
// HOUSE RULE (confirmed by Mr Thiab 26 Sep 2026): every FIKR deck ships
// ANIMATED — run engines/animate_deck.py on the built .pptx before delivery.
//
// Every piece of mathematics inside a sentence (titles, panels, bars, notes)
// is written as $...$ per the inline-maths house rule — see engines/inline_math.js.
// Only self-contained display equations use a LaTeX image key (eq:).
// Large numbers inside inline $...$ use "\," for thousands grouping (never a
// literal comma, which the parser reads as a list separator and pads with a
// space) — see the Sep 2026 fix in lessons_w6l6.js / lessons_w6l7.js.
const { build } = require("../../engines/lesson_engine");

const MATH = "math_w7/_index.json";
const GRAPH = "graphs_w7/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 2 · LESSON 1 — Vertex Form of a Quadratic Function
// =====================================================================
const GR10_L21 = {
  out: "Gr10_T2_L1_Vertex_Form_of_a_Quadratic_Function.pptx",
  deckTitle: "Vertex Form of a Quadratic Function — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  weekNum: "7",
  topicLine: "TOPIC 2 · QUADRATIC FUNCTIONS AND EQUATIONS · LESSON 1",
  lessonTitle: "Vertex Form of a Quadratic Function",
  titleSize: 30,
  subtitle: "Every parabola is the parent function $y=x^{2}$ in disguise — vertex form shows exactly which disguise",
  titleEq: "vf_title_w", titleEqK: 2.2,
  titleEqAlt: "f of x equals a times the quantity x minus h, squared, plus k",
  grade: "Grade 10", week: "Week 7 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 2 · Lesson 1",
  lessonRef: "Lesson 2-1 — Vertex Form of a Quadratic Function",
  nextLesson: "Topic 2 · Lesson 2 — Standard Form of a Quadratic Function",

  codes: ["HSA.REI.B.4", "HSA.REI.B.4.A", "HSF.IF.C.7.A", "HSA.CED.A.2", "HSF.IF.B.4", "HSF.BF.B.3"],
  mps: ["MP.4", "MP.5"],
  assessments: ASSESS,

  objectives: [
    "Graph quadratic functions given in vertex form.",
    "Write a quadratic function in vertex form given its key features.",
  ],
  essentialQuestion: "What are the key features of a transformation of the parent quadratic function?",

  vocabulary: [
    { term: "Parabola", def: "The rounded, symmetric curve that is the graph of any quadratic function." },
    { term: "Parent quadratic function", def: "The simplest quadratic, $f(x)=x^{2}$ — every other parabola is a transformation of this one graph." },
    { term: "Quadratic function", def: "A function that can be written with $x^{2}$ as its highest power of $x$." },
    { term: "Vertex", def: "The turning point of a parabola — its lowest point if the parabola opens up, or its highest point if it opens down." },
    { term: "Vertex form", def: "A quadratic function written as $f(x)=a(x-h)^{2}+k$, with vertex $(h,k)$ read directly off the equation." },
    { term: "Axis of symmetry", def: "The vertical line $x=h$ through the vertex — the parabola is a mirror image of itself across this line." },
    { term: "Minimum point / value", def: "The vertex and its $y$-value when the parabola opens up ($a>0$) — the smallest output the function reaches." },
    { term: "Maximum point / value", def: "The vertex and its $y$-value when the parabola opens down ($a<0$) — the largest output the function reaches." },
  ],
  vocabSub: "All ten terms the curriculum map lists for this lesson, grouped in pairs",

  prior: [
    { h: "Transformations of functions (Lesson 1-2)", eq: "vf_prior_transform", d: "$f(x-h)$ shifts horizontally, $+k$ shifts vertically, and a coefficient stretches or reflects — vertex form bundles all three onto one parent function." },
    { h: "The parent function $y=x^{2}$", eq: "vf_prior_parent", d: "Vertex $(0,0)$, opens up, symmetric about $x=0$ — every transformation today starts from this one shape." },
    { h: "Evaluating a function at a value", eq: "vf_prior_eval", d: "Substitute the input, read off the output — exactly how you will check a vertex or a point on any parabola today." },
  ],
  priorSub: "Three things you already know — today they describe a parabola",
  carryOver: "Every quadratic function in vertex form, $f(x)=a(x-h)^{2}+k$, is the parent function $y=x^{2}$ shifted, stretched, and possibly flipped — the vertex $(h,k)$ and the sign of $a$ tell you exactly how.",
  carryOverEq: "vf_def",

  diagnose: {
    title: "Warm-Up: Transformations, One More Time",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "vf_d1", t: "Describe the transformation from $y=f(x)$." },
      { eq: "vf_d2", t: "Describe the transformation from $y=f(x)$." },
      { eq: "vf_d3", t: "Evaluate." },
      { eq: "vf_d4", t: "State the vertex by inspection." },
      { eq: "vf_d5", t: "Does this parabola open up or down?" },
    ],
    routing: "0–2 correct → re-teach transformations with me.      3–4 correct → straight to vertex form.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Reading Key Features Straight Off Vertex Form",
      sub: "Objective 1, part 1 — the vertex, axis of symmetry, and max/min, without graphing anything",
      rowsHead: ["FUNCTION", "KEY FEATURES"],
      rowsTop: 2.42, rowH: 1.05, rowsCw: [3.55, 3.9],
      rows: [
        [{ eq: "vf_ex1", k: 1.5 }, { eq: "vf_feat1", k: 1.15 }],
        [{ eq: "vf_ex2", k: 1.5 }, { eq: "vf_feat2", k: 1.15 }],
        [{ eq: "vf_ex3", k: 1.5 }, { eq: "vf_feat3", k: 1.15 }],
      ],
      panel: {
        h: "READ $a$, $h$, AND $k$",
        items: [
          "In $f(x)=a(x-h)^{2}+k$, the vertex is $(h,k)$ — watch the SIGN inside the parentheses flips $h$.",
          "If $a>0$, the parabola opens UP and the vertex is a MINIMUM.",
          "If $a<0$, the parabola opens DOWN and the vertex is a MAXIMUM.",
          "The axis of symmetry is always the vertical line $x=h$.",
          "$|a|>1$ makes the parabola NARROWER than the parent; $|a|<1$ makes it WIDER.",
        ],
      },
      panelX: 8.15, panelW: 4.7, panelH: 4.05,
      bar: ["THE SIGN OF $h$ INSIDE THE PARENTHESES IS THE TRAP", "$f(x)=2(x-3)^{2}+4$ has vertex $(3,4)$, NOT $(-3,4)$ — subtracting a negative $h$ looks like addition — for instance $(x+1)^{2}=(x-(-1))^{2}$ has $h=-1$."],
      barY: 6.32,
      notes: "Row 1: $f(x)=2(x-3)^{2}+4$, vertex $(3,4)$, $a=2>0$ opens up, minimum value 4. Row 2: $g(x)=-(x+1)^{2}+5$, vertex $(-1,5)$, $a=-1<0$ opens down, maximum value 5. Row 3: $h(x)=(1⁄2)x^{2}-2$, vertex $(0,-2)$, $a=1⁄2$, opens up and WIDER than the parent since $|a|<1$. Misconception to address aloud: students read $(x+1)^{2}$ as vertex $x=1$ instead of $x=-1$ — rewrite it as $(x-(-1))^{2}$ on the board every time until it's automatic.",
    },
    {
      title: "Graphing Vertex Form as a Transformation",
      sub: "Objective 1, part 2 — build the graph from the parent function, one move at a time",
      graph: "g_vertex_transform", graphW: 6.5, graphY: 2.5,
      graphAlt: "The parent parabola y equals x squared, dashed, and the transformed parabola f of x equals 2 times the quantity x minus 3, squared, plus 4, solid, with vertex marked at 3 comma 4 and the axis of symmetry x equals 3 shown dashed",
      panel: {
        h: "BUILD IT IN THREE MOVES",
        items: [
          "Start from $y=x^{2}$, vertex $(0,0)$.",
          "Shift RIGHT 3 (from $h=3$): vertex moves to $(3,0)$.",
          "Shift UP 4 (from $k=4$): vertex moves to $(3,4)$.",
          "Stretch by a factor of 2 (from $a=2$): the parabola gets NARROWER, but the vertex does not move.",
          "Draw the axis of symmetry $x=3$ last, as a dashed guide line through the vertex.",
        ],
      },
      panelX: 7.4, panelW: 5.5, panelH: 4.0,
      bar: ["THE VERTEX MOVES FIRST, THE SHAPE CHANGES LAST", "translate $(h,k)$ to place the vertex, then apply $a$ to stretch, compress, or flip around that new vertex — never the other way round."],
      barY: 6.32,
      notes: "$f(x)=2(x-3)^{2}+4$: parent vertex $(0,0)$ moves to $(3,4)$ (right 3, up 4), then the factor of 2 narrows the curve around the NEW vertex. Check a second point: parent has $(1,1)$; after the shift $(4,1)$ would be on $y=(x-3)^2+4$, and after stretching by 2 it becomes $(4,6)$ on $f$. Misconception to address aloud: students apply the stretch factor around the ORIGINAL origin instead of the new vertex, distorting the shift they just made — narrate stretching as happening 'around the vertex you just placed'.",
    },
    {
      title: "Writing Vertex Form From Key Features",
      sub: "Objective 2 — given a vertex and one more point, find the missing $a$",
      panel: {
        h: "WORK BACKWARD FROM THE VERTEX",
        items: [
          "Given: $\\text{vertex }(2,-3)$, and the parabola passes through $(4,5)$.",
          "Start the equation with the vertex already in place: $f(x)=a(x-2)^{2}-3$.",
          "Substitute the OTHER point to solve for $a$: $5=a(4-2)^{2}-3$.",
          "Simplify and isolate $a$: $5=4a-3 \\Rightarrow a=2$.",
          "Final answer: $f(x)=2(x-2)^{2}-3$ — check it passes through both given points.",
        ],
      },
      panelX: 0.55, panelY: 2.42, panelW: 11.9, panelH: 4.0,
      bar: ["THE VERTEX GOES IN FIRST, $a$ COMES FROM THE OTHER POINT", "you only ever need ONE more point besides the vertex — substitute it and solve for the single unknown, $a$."],
      barY: 6.32,
      notes: "Vertex $(2,-3)$, point $(4,5)$: $f(x)=a(x-2)^2-3$; substitute $(4,5)$: $5=a(2)^2-3=4a-3$; solve: $a=2$; final $f(x)=2(x-2)^2-3$. Check: $f(2)=-3$ ✓, $f(4)=2(4)-3=5$ ✓. Misconception to address aloud: students substitute the VERTEX itself into the equation to solve for $a$, which always gives $0=0$ (no information) — press them to use the OTHER given point instead.",
    },
  ],

  quickCheck: {
    lead: "State the vertex, and whether it's a max or a min:", leadW: 6.6,
    eq: "vf_qc", k: 2.0,
    think: "Read $h$ and $k$ straight off the equation — remember the sign inside the parentheses flips for $h$. Then check the sign of $a$.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, reading $a$, $h$ and $k$ slowly together.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "vf_g1", t: "Graph this function using transformations from the parent function.", hint: "Place the vertex first (shift), then apply the stretch or reflection around it." },
      { eq: "vf_g2", t: "Write the vertex form of the parabola with this vertex and point.", hint: "Put the vertex in the equation first, then substitute the other point to solve for $a$." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["For each function, state the vertex, axis of symmetry, and whether it's a max or min: (a) $f(x)=(x-4)^{2}+1$   (b) $f(x)=-2(x+3)^{2}+6$   (c) $f(x)=(1⁄3)x^{2}-5$.", "Graph function (a) using transformations from the parent function.", "Write the vertex form of a parabola with vertex $(3,-1)$ passing through $(5,7)$.", "Check your equation from the previous question by substituting BOTH given points."],
        help: "You may use: the worked examples on the board, and a partner.",
        done: "every vertex you state matches the sign convention exactly, and your written equation passes through both given points.", eq: "vf_ws1" },
      { items: ["A basketball's path is modeled by $h(x)=-0.5(x-3)^{2}+5$ (where $x$ is the horizontal distance in metres and $h$ is the height in metres). State the maximum height and where it occurs.", "A decorative fountain's water jet has vertex $(2,4)$ and passes through $(0,0)$ at the nozzle. Write the vertex form of the height function.", "Use your equation to find the water's height at a horizontal distance of 1 metre."],
        help: "You may use: the worked fountain example, and a calculator.",
        done: "your height answers carry units (metres), and your equation is checked at the nozzle point.", eq: "vf_ws5" },
      { items: ["Two parabolas share the same vertex but have different values of $a$. Explain how their graphs differ, and what stays exactly the same.", "A parabola opens downward and has vertex $(3,-2)$. Explain, using the meaning of $a<0$, why $(3,-2)$ MUST be a maximum, not a minimum.", "Prove that the vertex form $f(x)=a(x-h)^{2}+k$ always has vertex $(h,k)$, by evaluating $f(h)$ directly."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: null },
    ],
  },

  production: {
    title: "Designing a Park Fountain's Arc",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A decorative fountain in a neighbourhood park shoots a jet of water in a parabolic arc. The water reaches a maximum height of 4 metres at a horizontal distance of 2 metres from the nozzle, and lands back at ground level 4 metres from the nozzle. The nozzle itself sits at ground level.",
    eq: "vf_fountain_w", eqK: 1.4,
    tasks: [
      "(a)  State the vertex of the height function, and explain how you know it is a MAXIMUM.",
      "(b)  Use the nozzle point $(0,0)$ to solve for $a$, and write the vertex form of the height function.",
      "(c)  Find the water's height at a horizontal distance of 1 metre and at 3 metres from the nozzle.",
      "(d)  A designer says “the water is always highest exactly halfway between where it leaves and lands.” Explain in one sentence why this is true, using the axis of symmetry.",
    ],
    note: "The value of $a$ shown as solved algebraically (not guessed), and part (d) answered using the axis of symmetry by name.",
    aiPrompt: "“Check whether I used the correct point to solve for $a$, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Drag the vertex and watch the whole parabola follow",
    graph: "g_vertex_transform",
    graphAlt: "The parent parabola and the transformed parabola f of x equals 2 times the quantity x minus 3, squared, plus 4, with vertex marked at 3 comma 4",
    explore: "Graph $y=x^{2}$ at geogebra.org/graphing, then create $f(x)=a(x-h)^{2}+k$ with sliders for $a$, $h$ and $k$. Drag $h$ and $k$ and watch the vertex move; then drag $a$ through 0 and watch the parabola flip from opening up to opening down. Finally set $h=2$, $k=4$, and find the value of $a$ that makes the curve pass through $(0,0)$ — check it matches the fountain task.",
  },

  gate: {
    items: [
      { t: "State the vertex, axis of symmetry, and whether it's a max or min.", eq: "vf_gate1" },
      { t: "Write the vertex form of the parabola with this vertex and point.", eq: "vf_gate2" },
      { t: "In ONE sentence, explain how you can tell from vertex form alone whether a parabola opens up or down.", eq: null },
    ],
    footer: "Exact answers for Q1 and Q2, with Q2 checked against the given point, and Q3 a reason rather than a restatement.",
    routing: "PASS → Enrichment & Challenge (writing vertex form from a vertex and an $x$-intercept instead of an arbitrary point).      NOT YET → Targeted Learning Clinic on reading $a$, $h$, $k$ from vertex form, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the fountain's vertex, the value of $a$ solved algebraically, and the height at 1 metre and 3 metres from the nozzle." },
      { h: "Expose the trap", d: "Add one worked NON-example — reading the vertex of $(x+2)^{2}+4$ as $(2,4)$ instead of $(-2,4)$ — and a sentence on how a reader would spot the sign error." },
      { h: "Say why it matters", d: "One caption — why a designer needs the EXACT maximum height and its location, not just a rough sketch — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 2 opening modelling set.",
    reflection: "which part is still harder for you — reading key features off vertex form, or writing the equation from a vertex and a point?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Reading the vertex directly off vertex form, meant to be answered in seconds.", fmt: "Multiple choice, about 75 seconds per item, no calculator.", tip: "Flip the sign inside the parentheses for $h$ — that single step is where most errors happen under time pressure.",
      question: "What is the vertex of $f(x)=4(x-1)^{2}+6$?",
      steps: ["Compare to $f(x)=a(x-h)^{2}+k$: $h=1$, $k=6$.", "Answer: vertex $(1,6)$."] },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Finding a maximum or minimum value from vertex form, a core Grade 10 skill.", fmt: "Four-option multiple choice, no calculator.", tip: "Check the sign of $a$ FIRST to know whether you're finding a maximum or a minimum before you even look at $k$.",
      question: "What is the maximum value of $f(x)=-2(x+3)^{2}+9$?",
      steps: ["$a=-2<0$, so the vertex is a MAXIMUM.", "Vertex is $(-3,9)$.", "Answer: maximum value $9$."] },
    { code: "SAT", full: "College Board", skill: "Writing a quadratic's equation from its vertex and one other point — a recurring Advanced Math item type.", fmt: "Two 35-minute adaptive modules; calculator allowed throughout.", tip: "Put the vertex into $a(x-h)^2+k$ first, then substitute the other point — never expand before solving for $a$.",
      question: "A parabola has vertex $(3,-4)$ and passes through $(5,4)$. Write its equation in vertex form.",
      steps: ["Start with $f(x)=a(x-3)^{2}-4$.", "Substitute $(5,4)$: $4=a(2)^{2}-4=4a-4$.", "Solve: $a=2$. Answer: $f(x)=2(x-3)^{2}-4$."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "the vertex is $(h,k)$ with the sign of $h$ FLIPPED from what's written inside the parentheses — check that flip before reading anything else off vertex form."],

  summary: [
    "Read the vertex, axis of symmetry, and whether it's a max or min, directly off vertex form.",
    "Graph a quadratic function as a transformation of the parent function $y=x^{2}$: shift the vertex first, then stretch or reflect around it.",
    "Write a quadratic's vertex form by placing the vertex, then solving for $a$ using one other point.",
    "Watch the sign of $h$ inside the parentheses — it is the single most common source of error in this topic.",
    "Model a real parabolic path (like a fountain's arc) using vertex form, including finding heights at other horizontal distances.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 2 · Lesson 2 — Standard Form of a Quadratic Function (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on reading $a$, $h$, $k$ from vertex form.",
  ],

  notes: {
    cover: "Week 7 lesson for both Grade 10 sections, opening Topic 2 (Quadratic Functions and Equations) after Topic 1's Unit Recap and Assessment. This is a NEW topic — do not assume prior quadratic-specific vocabulary beyond what Topic 1's function work already covered.",
    objectives: "Both objectives are verbatim from the curriculum map. The map lists HSA.REI.B.4, HSA.REI.B.4.A, HSF.IF.C.7.A, HSA.CED.A.2, HSF.IF.B.4 and HSF.BF.B.3 for this lesson, and only MP.4 and MP.5 — do not add others. HSA.REI.B.4.A's completing-the-square language connects directly to vertex form, since vertex form IS the completed-square form of a quadratic.",
    vocabulary: "All ten terms are the map's list, grouped here into five pairs for teaching efficiency: shape words (parabola, parent quadratic function), the function itself (quadratic function, vertex form), the turning point (vertex, axis of symmetry), and its two possible roles (minimum point/value, maximum point/value).",
    prior: "If a student cannot describe $f(x-h)+k$ as a shift from Lesson 1-2, vertex form will look like a brand-new idea instead of familiar transformations with new names. Watch for it in the diagnostic, questions 1 and 2.",
    diagnose: "Answers: shift up 3; shift right 2; $f(-3)=9$; vertex $(1,4)$; opens down (since $a=-3<0$). Expected gap: Q4, where students read $(x-1)^2$ correctly but then mis-transfer the SAME sign rule incorrectly to a form like $(x+2)^2$ later in the lesson.",
    quickCheck: "Answer: vertex $(-5,7)$, and since $a=-2<0$, it's a MAXIMUM. Watch for students who correctly find the vertex but forget to check the sign of $a$ before naming it max or min.",
    guided: "Answers — 1: $f(x)=(x-2)^{2}-3$ shifts the parent right 2, down 3, no stretch. 2: vertex $(-1,4)$, point $(1,-4)$: $-4=a(1-(-1))^2+4=4a+4 \\to a=-2$, so $f(x)=-2(x+1)^{2}+4$. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference. Apply-route answers: basketball max height 5 metres at $x=3$; fountain equation from vertex $(2,4)$ and point $(0,0)$ is $h(x)=-(x-2)^2+4$; height at $x=1$ is 3 metres.",
    production: "Answers — (a) vertex $(2,4)$; maximum, since the water rises then falls back to ground level, and $(2,4)$ is the highest point reached. (b) $0=a(0-2)^2+4 \\to 0=4a+4 \\to a=-1$, so $h(x)=-(x-2)^2+4$. (c) $h(1)=-(1-2)^2+4=3$ metres; $h(3)=-(3-2)^2+4=3$ metres — symmetric about the axis, as expected. (d) the axis of symmetry $x=2$ sits exactly halfway between the two ground points $x=0$ and $x=4$ by definition — a parabola is symmetric about this line, so the peak (vertex) always falls exactly there.",
    geogebra: "The moment $a$ crosses 0, the parabola visibly flips — connecting the ABSTRACT sign rule to something students watch happen in real time, before they try to state it from memory.",
    gate: "Answers: $f(x)=3(x-1)^2-2$ has vertex $(1,-2)$, axis $x=1$, minimum (since $a=3>0$). Vertex $(2,5)$, point $(0,1)$: $1=a(0-2)^2+5=4a+5 \\to a=-1$, so $f(x)=-(x-2)^2+5$. Q3: because the sign of $a$ tells you directly — positive $a$ means the parabola opens up, negative $a$ means it opens down, with no need to graph anything. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — misreading the sign inside the parentheses is THE most common error in this entire topic, and naming it explicitly here helps students catch it in their own work later.",
    exams: "Show this before homework so the practice set has an obvious purpose. Walk through at least one worked card aloud before moving on.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  await build(GR10_L21);
})();

module.exports = { GR10_L21 };

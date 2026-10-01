// Grade 10 · Topic 2 · Lesson 2-3 — Factored Form of a Quadratic Function.
// Objectives, standards and vocabulary are quoted from the curriculum map. The map's Essential Question and
// Math Practices columns for Topic 2 were not available in the project text, so they are NOT shown and NOT invented.
const { build } = require("./lesson_engine");

const CFG = {
  out: "Gr10_T2_L2-3_Factored_Form.pptx",
  deckTitle: "Factored Form of a Quadratic Function — Grade 10 Algebra II",
  mathIndex: "math_g10q3/_index.json", graphIndex: "graphs_g10q3/_index.json",
  topicLine: "TOPIC 2 · QUADRATIC FUNCTIONS AND EQUATIONS · LESSON 2-3",
  lessonTitle: "Factored Form of a Quadratic Function", titleSize: 34,
  subtitle: "Where does the parabola cross the x-axis — and where is it positive or negative?",
  titleEq: "c_title_w", titleEqK: 2.4,
  titleEqAlt: "f of x equals a times x minus p times x minus q: the factored form of a quadratic function",
  grade: "Grade 10", week: "Week 6 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 2 · Lesson 2-3",
  lessonRef: "Lesson 2-3 — Factored Form of a Quadratic Function",
  nextLesson: "Topic 2 · Lesson 2-4 — Overview of Complex Numbers",
  codes: ["HSA.SSE.A.1.B", "HSA.SSE.B.3.A", "HSA.APR.B.3", "HSF.IF.C.7", "HSF.IF.C.7.A", "HSA.SSE.A.2", "HSF.IF.C.8.A"],
  mps: [],
  assessments: ["“Give it a go” questions", "“Time to Check”"],

  objectives: [
    "Solve quadratic equations by factoring.",
    "Find the zeros of a quadratic function by factoring.",
    "Determine the intervals where a quadratic function is positive or negative.",
  ],
  essentialQuestion: null,
  objectivesSub: "Quoted from the curriculum map",

  vocabulary: [
    { term: "factored form", def: "f(x) = a(x − p)(x − q). The zeros are p and q, so the x-intercepts can be read straight off." },
    { term: "negative interval", def: "An interval of x-values on which the function is below the x-axis: f(x) < 0." },
    { term: "positive interval", def: "An interval of x-values on which the function is above the x-axis: f(x) > 0." },
    { term: "x-intercepts", def: "The points where the graph crosses the x-axis, written (p, 0) and (q, 0)." },
    { term: "zeros (of a quadratic function)", def: "The x-values where f(x) = 0. They are the x-coordinates of the x-intercepts." },
    { term: "zero-product property", def: "If a · b = 0, then a = 0 or b = 0. It is why we can solve an equation once it is factored and set equal to 0." },
  ],
  vocabSub: "All six terms the curriculum map lists for Lesson 2-3",

  prior: [
    { h: "Lesson 2-2: standard form", eq: "c_p1", d: "Read a, b and c; the y-intercept is c and the axis is −b over 2a." },
    { h: "Lesson 2-1: vertex form", eq: "c_p2", d: "The vertex is (h, k) and the axis is x = h." },
    { h: "Multiplying binomials", eq: "c_p3", d: "Today we run this in reverse: from the trinomial back to two factors." },
  ],
  priorSub: "Three things you already know — today adds a third view of the same parabola",
  carryOver: "Standard form shows where the parabola starts, vertex form shows where it turns, and factored form shows where it crosses the x-axis. Same function, three views.",
  carryOverEq: "c_co_w",

  diagnose: {
    title: "Warm-Up: Multiply, Evaluate, Reverse",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "c_d1", t: "Expand the brackets." },
      { eq: "c_d2", t: "Evaluate at x = 2. What does the result tell you about the graph?" },
      { eq: "c_d3", t: "What must be true about a or b?" },
      { eq: "c_d4", t: "Factor the trinomial into two brackets." },
      { eq: "c_d5", t: "Use −b over 2a." },
    ],
    routing: "0–2 correct → re-teach multiplying and factoring with me.      3–4 correct → straight to factored form.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Factored Form: Read the Zeros",
      sub: "Lesson 2-3, objective 2 — f(x) = a(x − p)(x − q) shows the x-intercepts at once",
      graph: "g_fac", graphW: 5.6, graphX: 0.45, graphY: 2.45,
      graphAlt: "Parabola f of x equals x plus 1 times x minus 3, crossing the x-axis at minus 1 and 3, with vertex 1 comma minus 4 and y-intercept 0 comma minus 3",
      panel: {
        h: "READ IT THIS WAY: f(x) = a(x − p)(x − q)",
        items: [
          "The zeros are p and q: set each bracket equal to 0. The x-intercepts are (p, 0) and (q, 0).",
          "Read the sign of the bracket the other way: (x + 1) gives the zero x = −1.",
          "The axis of symmetry is halfway between the zeros: x = (p + q) over 2.",
          "Substitute the axis value to get the vertex: f(1) = (2)(−2) = −4.",
          "The y-intercept is f(0) = a · p · q: here (1)(−3) = −3.",
        ],
        fs: 12,
      },
      panelX: 6.3, panelY: 2.5, panelW: 6.6, panelH: 3.75,
      bar: ["SIGN WATCH", "(x + 1) means the zero is x = −1, and (x − 3) means the zero is x = 3 — the zero is the value that makes the bracket 0."],
      barY: 6.32,
      notes: "f(x)=(x+1)(x-3): zeros -1 and 3; axis x=(−1+3)/2=1; vertex f(1)=(2)(-2)=-4 -> (1,-4); y-intercept f(0)=(1)(-3)=-3; expanded it is x^2-2x-3 (this is the same parabola as the standard-form view). Misconceptions to say aloud: (1) the zero of (x+1) is -1, not 1; (2) the zeros are x-values -- the points are (-1,0) and (3,0); (3) a does not move the zeros, only the stretch and direction. Link: HSA.SSE.B.3.A -- factoring reveals the zeros.",
    },
    {
      title: "Solve by Factoring: the Zero-Product Property",
      sub: "Lesson 2-3, objectives 1 and 2 — factor, set each bracket to 0, solve",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Get 0 on one side first. The property only works on a product that equals 0.",
          "Factor: I need two numbers that multiply to −3 and add to −2. They are 1 and −3.",
          "Zero-product property: if the product is 0, one of the brackets is 0.",
          "Solve each bracket. Check by substituting back: (−1)² − 2(−1) − 3 = 0 ✓ and 9 − 6 − 3 = 0 ✓.",
        ],
        fs: 12,
      },
      panelX: 0.45, panelY: 2.5, panelW: 5.8, panelH: 3.75,
      rowsHead: ["STEP", "WORK"],
      rowsTop: 2.5, rowH: 0.8, rowsX: 6.5, rowsW: 6.4,
      rows: [
        ["Equation equal to 0", { eq: "c_z1", k: 1.5 }],
        ["Factor", { eq: "c_z2", k: 1.5 }],
        ["Zero-product property", { eq: "c_z3", k: 1.5 }],
        ["Solutions = zeros", { eq: "c_z4", k: 1.5 }],
      ],
      bar: ["THE PATTERN", "solving x² − 2x − 3 = 0 and finding the zeros of f(x) = x² − 2x − 3 are the same job: the solutions of the equation are the zeros of the function."],
      barY: 6.32,
      notes: "x^2-2x-3=0 -> (x+1)(x-3)=0 -> x=-1 or x=3. The factor pair: product -3, sum -2 -> 1 and -3. These are the zeros of f(x)=x^2-2x-3 and the x-intercepts (-1,0),(3,0): connect to slide 7. Misconceptions to say aloud: (1) the equation must equal ZERO before factoring -- (x-2)(x-3)=6 does NOT give x-2=6; (2) do not drop a solution -- two brackets, two zeros; (3) when a is not 1 factor out the common factor first (next slide set / practice).",
    },
    {
      title: "Positive and Negative Intervals",
      sub: "Lesson 2-3, objective 3 — the zeros cut the x-axis into intervals",
      graph: "g_pos", graphW: 5.2, graphX: 0.45, graphY: 2.5,
      graphAlt: "Parabola f of x equals x plus 1 times x minus 3. Teal parts are above the x-axis for x less than minus 1 and x greater than 3; the orange part is below the x-axis between minus 1 and 3",
      rowsHead: ["WHERE THE GRAPH IS", "INTERVAL"],
      rowsTop: 2.42, rowH: 0.8, rowsX: 5.9, rowsW: 7.0, rowsCw: [2.4, 4.6],
      rows: [
        ["Above the x-axis (positive)", { eq: "c_i1", k: 1.1 }],
        ["Below the x-axis (negative)", { eq: "c_i2", k: 1.1 }],
        ["Method", "mark the zeros, test one x-value in each interval"],
        ["Test x = 0", "f(0) = −3 < 0, so the middle interval is negative"],
      ],
      bar: ["READ THE SHAPE", "a > 0 opens up, so the graph is negative between the zeros and positive outside them. If a < 0 it flips."],
      barY: 6.32,
      notes: "f(x)=(x+1)(x-3). Zeros -1 and 3 give three intervals: x<-1, -1<x<3, x>3. Test points: f(-2)=(-1)(-5)=5>0; f(0)=-3<0; f(4)=(5)(1)=5>0. Positive: x<-1 or x>3. Negative: -1<x<3. Misconceptions: (1) the zeros themselves are neither positive nor negative -- open intervals; (2) positive/negative refers to the OUTPUT f(x), not to x; (3) use 'or' for the two outside intervals, never 'and'. Colour code on the graph: teal = positive, orange = negative.",
    },
  ],

  quickCheck: {
    lead: "State the zeros", leadW: 2.9,
    eq: "c_qc", k: 2.0,
    think: "Set each bracket to 0: x − 4 = 0 gives 4, and x + 2 = 0 gives −2. Mind the sign of the second bracket.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example with a plus sign inside a bracket.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "c_g1", t: "Solve by factoring. Check one solution by substitution.", hint: "Two numbers that multiply to 6 and add to 5." },
      { eq: "c_g2", t: "State the zeros, then the interval where f(x) is negative.", hint: "a = 1 > 0, so the graph is below the axis between the zeros." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["State the zeros and the x-intercepts of f(x) = (x + 3)(x − 2).", "Solve by factoring: x² − 7x + 12 = 0 and x² + 2x = 0.", "For f(x) = (x + 3)(x − 2) find the axis (x = −1/2), the vertex and the y-intercept.", "Where is f(x) = (x + 3)(x − 2) positive? Where is it negative?"],
        help: "You may use: the key-features table on the board, and a partner.",
        done: "each solution is checked by substitution, and each interval is written with the right inequality signs.", eq: "c_ws1" },
      { items: ["Write the function with zeros −2 and 4 that passes through (0, −16).", "Factor and solve 2x² − 2x − 12 = 0, then say where f(x) = 2x² − 2x − 12 is negative.", "Data: a ball is on the ground at 0 m and 6 m horizontally and 9 m high at 3 m. Write its height function and check it with a fourth point."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your function is checked by substituting a point, and every answer carries a sentence in context.", eq: "c_ws3" },
      { items: ["Show that for f(x) = a(x − p)(x − q) the axis is x = (p + q) over 2, by symmetry of the zeros.", "A student solves (x − 2)(x − 3) = 6 by writing x − 2 = 6 or x − 3 = 6. Explain the error, then solve it correctly.", "Explain why the zeros are never in the positive or negative interval, using a graph."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument grounded in the zero-product property or in the graph, not just a computed answer.", eq: null },
    ],
  },

  production: {
    title: "How Wide Is the Arch?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A footbridge arch on the Jeddah Corniche touches the ground at two points 8 m apart and is 4 m high at its middle. Measure x along the ground from the left foot. This is an invented classroom model.",
    eq: "c_model_w", eqK: 2.2,
    tasks: [
      "(a)  Write the arch height h(x) in factored form using the zeros 0 and 8 and the top point (4, 4).",
      "(b)  State the interval where h(x) > 0 and say what it means for the walkway.",
      "(c)  Find the height 2 m from the left foot.",
      "(d)  Using technology, find where the arch is 3 m high.",
    ],
    note: "Exact fractions before any decimal; units named (metres); the factored form checked against the top point.",
    aiPrompt: "“Check whether my factored form and my expanded form describe the same parabola, and challenge any step I have not justified.”",
  },

  geogebra: {
    sub: "Slide p and q — watch the zeros and the intervals move",
    preview: "g_fac",
    previewAlt: "Parabola f of x equals x plus 1 times x minus 3 with its zeros, vertex and axis of symmetry",
    url: "https://www.geogebra.org/graphing",
    steps: [
      "Open the link (any browser, no sign-in needed).",
      "Type a = 1, p = −1 and q = 3 and click each slider button.",
      "Type f(x) = a(x − p)(x − q), then the points A = (p, 0) and B = (q, 0).",
      "Type f(x) > 0 to shade where the function is positive, and compare.",
    ],
    explore: "Which slider moves the zeros? What happens when p = q? Make f pass through (0, −16) with zeros −2 and 4.",
  },

  gate: {
    eq: "c_gate_w",
    items: [
      { t: "Write the function in factored form.", eq: "c_gate_w" },
      { t: "Solve x² − x − 12 = 0 by factoring.", eq: null },
      { t: "In ONE sentence, say where f(x) = (x + 2)(x − 5) is negative and how you know.", eq: null },
    ],
    footer: "Exact answers only. Question 3 is a sentence with an interval, not an example.",
    routing: "PASS → Enrichment & Challenge (find the zeros from a graph and write the function in all three forms).      NOT YET → Targeted Learning Clinic on factoring trinomials, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the arch in factored form and expanded form, the interval where it is above the ground, and the 3 m points." },
      { h: "Expose the trap", d: "Add one worked NON-example — solving (x − 2)(x − 3) = 6 as x = 8 or x = 9 — and show what goes wrong." },
      { h: "Say why it matters", d: "One caption — “why an engineer needs to know where the arch meets the ground” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 2 modelling set.",
    reflection: "which is easier for you — reading the zeros from factored form, or finding them from standard form?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Sum of the solutions of a quadratic equation, no calculator.",
      question: "Sum of the solutions of x² − 5x + 6 = 0?   (A) 5   (B) 6   (C) −5   (D) 1",
      steps: ["(x − 2)(x − 3) = 0.", "x = 2 or x = 3.", "Sum = 5: answer (A)."],
      trap: "(B) is the product; (C) takes the sign of b; (D) is the difference." },
    { code: "SAT", full: "College Board — Advanced Math", skill: "Write a parabola's equation from its x-intercepts and a point.",
      question: "x-intercepts (−3, 0) and (5, 0), through (1, −32). Which equation?   (A) y = 2(x − 3)(x + 5)   (B) y = 2(x + 3)(x − 5)   (C) y = −2(x + 3)(x − 5)   (D) y = (x + 3)(x − 5)",
      steps: ["y = a(x + 3)(x − 5).", "−32 = a(4)(−4), so a = 2.", "Answer (B)."],
      trap: "(A) flips both signs; (C) gets the sign of a wrong; (D) forgets a." },
    { code: "GAT", full: "Qudurat — Quantitative Comparison", skill: "Solve a quadratic by factoring and compare the larger solution.",
      question: "A = larger solution of x² − x − 6 = 0 and B = 3.   (A) A greater   (B) B greater   (C) equal   (D) cannot tell",
      steps: ["(x − 3)(x + 2) = 0.", "x = 3 or x = −2; the larger is 3.", "A = B: answer (C)."],
      trap: "Choosing −2 as the larger, or taking x = 6 from the constant term." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "set the factored expression equal to 0 and read the zeros — then watch the sign inside each bracket."],

  summary: [
    "Solve a quadratic equation by factoring and the zero-product property.",
    "Find the zeros of a quadratic function and write them as x-intercepts.",
    "Read the zeros, axis, vertex and y-intercept from factored form.",
    "Say where a quadratic function is positive or negative using intervals.",
    "Move between standard, vertex and factored form, knowing they describe the same parabola.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 2 · Lesson 2-4 — Overview of Complex Numbers (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on factoring trinomials.",
  ],

  notes: {
    cover: "Week 6 lesson for 10A and 10C. If time runs short, cut Smart Production and carry it over, never the Mastery Gate. Objectives, vocabulary and standards are quoted from the curriculum map (HSA.SSE.A.1.B and SSE.B.3.A, APR.B.3, IF.C.7 and IF.C.7.A, SSE.A.2, IF.C.8.A). The map's Essential Question and Math Practices columns for Topic 2 were not in the project text; they are left off rather than invented.",
    objectives: "The three objectives are quoted from the map. Solve by factoring, find the zeros, and the sign intervals.",
    vocabulary: "Six terms. Ask students to restate the zero-product property in their own words.",
    prior: "If students cannot expand (x+2)(x-5) or factor x^2+5x+6, slow down here. Watch diagnostic questions 1 and 4.",
    diagnose: "Answers: x^2-3x-10; f(2)=0, so x=2 is a zero and (2,0) is on the graph; a=0 or b=0; (x+2)(x+3); axis x=-(-2)/2=1.",
    quickCheck: "Answer: zeros 4 and -2. Watch for 4 and 2.",
    guided: "Answers: (1) (x+2)(x+3)=0 gives x=-2 or x=-3; check (-2)^2+5(-2)+6=0. (2) zeros 1 and 5; negative for 1<x<5. Do not release independent work until about 80% have both.",
    routes: "Answers. Practice: zeros -3 and 2; x=3,4; x=0,-2; axis x=-1/2, vertex f(-1/2)=(5/2)(-5/2)=-25/4, y-int -6; positive for x<-3 or x>2, negative for -3<x<2. Apply: a(0+2)(0-4)=-16 gives a=2, f=2(x+2)(x-4). 2x^2-2x-12=2(x-3)(x+2): zeros 3,-2; negative for -2<x<3. Ball: zeros 0 and 6, vertex (3,9): a(3)(-3)=9 gives a=-1, h=-x(x-6). Check h(1)=5. Investigate: zeros p,q are symmetric about the axis so axis=(p+q)/2; (x-2)(x-3)=6 -> x^2-5x=0 -> x=0 or x=5; zeros are where f=0, which is neither >0 nor <0.",
    production: "Answers: (a) h(x)=a x(x-8) with h(4)=4: -16a=4, a=-1/4, so h(x)=-(1/4)x(x-8). (b) 0<x<8: the arch is above the ground between its feet. (c) h(2)=-(1/4)(2)(-6)=3 m. (d) -(1/4)x(x-8)=3 gives x^2-8x+12=0, so x=2 or x=6.",
    geogebra: "p and q move the zeros; a changes the opening. f(x)>0 shades the positive intervals. With a=2, p=-2, q=4 the graph passes through (0,-16).",
    gate: "Answers: (1) a(3)(-1)=6 gives a=-2: f=-2(x+3)(x-1). (2) (x-4)(x+3)=0: x=4 or -3. (3) Negative for -2<x<5 because a>0 and the graph is below the axis between the zeros. Score live and route privately.",
    smart: "The non-example: (x-2)(x-3)=6 is not a product equal to 0. Expanding gives x^2-5x=0, so x=0 or x=5, not 8 or 9. Check: (0-2)(0-3)=6 and (5-2)(5-3)=6.",
    exams: "Show before homework. Format reminders: SAAT four-option, no calculator; SAT two 35-minute adaptive modules with a calculator; GAT about 75 seconds per item with no calculator. Answers: SAAT (A); SAT (B); GAT (C).",
    summary: "Route the clinic group privately through the LMS -- never announce the list to the class.",
  },
};

(async () => { await build(CFG); })();
module.exports = { CFG };

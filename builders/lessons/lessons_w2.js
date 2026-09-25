// Week 2 — two lessons per grade, per the Curriculum Distribution.
//   Gr10  Lesson 1-1  Key Features of Functions            (already built)
//   Gr10  Lesson 1-2  Transformations of Functions          ← this file
//   Gr11  Lesson 5-3  Graphing Radical Functions            ← this file
//   Gr11  Lesson 5-4  Solving Radical Equations             ← this file
//
// Objectives, essential questions, vocabulary, standards, MPs and assessment
// names are quoted VERBATIM from "Curriculum map A2 OBLAS.docx".
const { build } = require("./lesson_engine");

const MATH = "math_w2/_index.json";
const GRAPH = "graphs_w2/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

// =====================================================================
// GRADE 10 · TOPIC 1 · LESSON 2 — Transformations of Functions
// =====================================================================
const GR10_L2 = {
  out: "Gr10_T1_L2_Transformations_of_Functions.pptx",
  deckTitle: "Transformations of Functions — Grade 10 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 1 · LINEAR FUNCTIONS · LESSON 2",
  lessonTitle: "Transformations of Functions",
  titleSize: 40,
  subtitle: "Move it, flip it, stretch it — and predict the graph before you draw it",
  titleEq: "t_general_w", titleEqK: 2.4,
  titleEqAlt: "g of x equals a times f of b times x minus h, plus k",
  grade: "Grade 10", week: "Week 2 · Semester 1, 2026–27",
  footerLeft: "Grade 10 · Algebra II · Topic 1 · Lesson 2",
  lessonRef: "Lesson 1-2 — Transformations of Functions",
  nextLesson: "Piecewise-Defined Functions",

  codes: ["HSF.BF.B.3", "HSF.IF.B.5"],
  mps: ["MP.5", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Identify the different types of transformations (translations, reflections, stretches, and compressions) applied to functions and their graphical representations.",
    "Apply transformations to various functions and predict the changes in their graphs, enhancing their ability to visualize and manipulate mathematical functions.",
  ],
  essentialQuestion: "How do transformations affect the shape and position of a function’s graph?",

  vocabulary: [
    { term: "Transformation", def: "Any change to a function that moves, flips or resizes its graph. The shape family stays the same." },
    { term: "Translation", def: "A slide. The graph moves left, right, up or down without changing shape or orientation." },
    { term: "Reflection", def: "A flip across an axis. Across the x-axis is −f(x); across the y-axis is f(−x)." },
    { term: "Stretch", def: "The graph is pulled away from an axis, making it taller or wider than the parent." },
    { term: "Compression", def: "The graph is squashed towards an axis, making it shorter or narrower than the parent." },
    { term: "Scaling", def: "The general name for stretching and compressing — multiplying by a factor rather than adding." },
  ],
  vocabSub: "The six terms the curriculum map lists for this lesson",

  prior: [
    { h: "The parent function", eq: "t_parent", d: "Every family has a simplest member. We transform that one." },
    { h: "Reading a graph", eq: "t_up", d: "Adding to the output moves the whole graph up." },
    { h: "Function notation", eq: "t_right", d: "Changing the input moves it sideways — the surprising one." },
  ],
  priorSub: "Three things from Lesson 1 — today we move the graph around",
  carryOver: "A transformation never changes what family a function belongs to. A parabola stays a parabola however far you slide, flip or stretch it — which is why you can predict the new graph without plotting a single point.",
  carryOverEq: "t_general_w",

  diagnose: {
    title: "Warm-Up: Predict the Move",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "t_d1", t: "Describe what this does to the graph of f." },
      { eq: "t_d2", t: "Describe what this does to the graph of f." },
      { eq: "t_d3", t: "Which axis is the graph reflected in?" },
      { eq: "t_d4", t: "Stretch or compression? By what factor?" },
      { eq: "t_d5", t: "Which axis is the graph reflected in this time?" },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to modelling.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "The Four Families of Transformation",
      sub: "Objective 1 — one parent function, four things you can do to it",
      graph: "g_transform_panel", graphW: 12.43, graphY: 2.5,
      graphAlt: "Four panels showing a parabola translated up, translated right, reflected in the x-axis, and stretched and compressed vertically",
      bar: ["THE PATTERN", "Changes OUTSIDE the function move it vertically and behave as you expect. Changes INSIDE the brackets move it horizontally — and do the opposite of what the sign suggests."],
      barY: 6.32,
      notes: "Work left to right. The horizontal translation is the one that catches everyone: f(x−2) moves the graph RIGHT by 2, not left. Ask why: the input has to be 2 bigger to give the same output.",
    },
    {
      title: "Reading the General Form",
      sub: "Objective 2 — every number in the form tells you one thing",
      rows: [
        [{ eq: "t_up" }, "k moves the graph UP by k. Outside the function, so it behaves as you expect."],
        [{ eq: "t_right" }, "h moves the graph RIGHT by h. Inside the brackets, so the sign is reversed."],
        [{ eq: "t_reflx" }, "Reflection in the x-axis. Every output changes sign."],
        [{ eq: "t_refly" }, "Reflection in the y-axis. Every input changes sign."],
        [{ eq: "t_stretch" }, "Vertical stretch by a factor of a — the graph gets taller."],
        [{ eq: "t_compress" }, "Vertical compression — the graph gets flatter."],
        [{ eq: "t_horiz" }, "Horizontal scaling by a factor of 1/b — again, the opposite of what you expect."],
      ],
      rowsHead: ["The transformation", "What it does to the graph"],
      rowsCw: [3.6, 8.83], rowH: 0.56, rowsTop: 2.32,
      notes: "Do not reteach the algebra — this is a reading exercise. Ask a different student to read each row aloud in words. Misconception to name: students think a>1 always means 'bigger'. For a horizontal scaling it means narrower.",
    },
    {
      title: "Modelled Example — I Think Aloud",
      sub: "Objective 2 — three transformations at once, predicted before plotting",
      graph: "g_transform_worked", graphW: 6.2, graphY: 2.42,
      graphAlt: "The parabola f of x equals x squared shown dashed, with g of x equals negative 2 times x minus 3 squared plus 5 reflected, stretched and translated, vertex marked at 3 comma 5",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Read the form first: a = −2, h = 3, k = 5.",
          "The minus sign flips it — this parabola opens downwards.",
          "The 2 stretches it vertically, so it is narrower than the parent.",
          "h = 3 moves it RIGHT 3, not left. Inside the bracket.",
          "k = 5 moves it UP 5.",
          "The vertex lands at (3, 5). I knew that before plotting anything.",
        ],
      },
      panelX: 6.95, panelW: 5.93, panelH: 4.1,
      notes: "Narrate the ORDER: reflect and stretch first, then translate. Ask what happens if you translate before stretching — the answer is a different graph, and that is worth two minutes.",
    },
  ],

  quickCheck: {
    lead: "Describe every transformation in", leadW: 4.6,
    eq: "t_qc", k: 2.4,
    think: "There are three things happening here. Name each one, and say whether it is inside or outside the function.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time built up one step at a time.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "t_g1", t: "Describe the transformation and state the new vertex.", hint: "Inside the bracket moves it sideways — and reverses the sign." },
      { eq: "t_g2", t: "Describe every transformation applied to the parent function.", hint: "Two things are happening, not one." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Describe the transformation in six given equations.", "Match four equations to four sketched graphs.", "State the new vertex for each of three translations.", "Sketch two translations of the parent parabola on the grid provided."],
        help: "You may use: the general-form table on the board, and a partner.",
        done: "you can name each transformation from the equation alone.", eq: "t_ws1" },
      { items: ["Write the equation for a graph shown, from its vertex and shape.", "Apply three transformations in the correct order and sketch the result.", "Explain what happens when the order of two transformations is swapped.", "One context question: a parabolic arch relocated along a span."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your sketch matches the equation, and your vertex is exact.", eq: "t_ws2" },
      { items: ["Prove that f(x−h)+k and f(x)+k−h are not the same transformation.", "Find a single transformation with the same effect as two given ones combined.", "Explain why a horizontal stretch by factor b uses 1/b in the equation."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "t_ws4" },
    ],
  },

  production: {
    title: "The Arch of a Vision 2030 Pedestrian Bridge",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A pedestrian bridge over a highway in Riyadh is designed with a parabolic arch. Measuring from the left support, the height of the arch in metres is given by the function below, where x is the distance across the span.",
    eq: "ctx_arch_w", eqK: 1.5,
    tasks: [
      "(a)  State the vertex, and say what it means for the bridge in one sentence with units.",
      "(b)  The design is revised: the arch must be 4 m taller. Write the new equation and name the transformation.",
      "(c)  A second, identical arch begins 80 m further along. Write its equation.",
      "(d)  Explain why changing the 0.02 would be a poor way to make the arch taller.",
    ],
    note: "Exact values, and every transformation named.",
    aiPrompt: "“Check whether I have named each transformation correctly, and challenge any step I cannot justify.”",
  },

  geogebra: {
    sub: "Drag the sliders and watch the parabola move",
    explore: "build g(x) = a·f(b(x−h))+k with four sliders. Change one at a time and say aloud what it does. Then set a negative and b negative together — what happens, and why?",
  },

  gate: {
    graph: "g_transform_gate",
    graphAlt: "A downward parabola with vertex at minus 2 comma 7",
    items: [
      { t: "Write the equation of the graph shown, in the form g(x) = a(x−h)² + k.", eq: null },
      { t: "Name every transformation applied to the parent function f(x) = x².", eq: null },
      { t: "In ONE sentence, explain why the horizontal shift uses the opposite sign to the one you might expect.", eq: null },
    ],
    footer: "Exact answers only. Show how you read each number from the graph.",
    routing: "PASS → Enrichment & Challenge (composing three transformations).      NOT YET → Targeted Learning Clinic on horizontal shifts, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the chain", d: "Take the parent function and apply your transformations one at a time, sketching each stage, so the reader sees the graph move." },
      { h: "Expose the trap", d: "Add one worked NON-example: a horizontal shift with the sign the wrong way round, and a sentence saying how you would spot it." },
      { h: "Say why it matters", d: "One caption — “why an engineer transforms a function rather than starting again” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 1 anchor set.",
    reflection: "which is still harder for you — the vertical moves, or the horizontal ones?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Recognising a shifted or reflected graph at a glance, usually inside a data-interpretation item.", fmt: "Multiple choice, about 75 seconds per item.", tip: "Look at the vertex first. It gives you h and k immediately." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Transformations of functions sit in the Grade 11 band, which is 30% of the mathematics questions.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Read the sign inside the bracket twice. It is the single most common error." },
    { code: "SAT", full: "College Board", skill: "Advanced Math — nonlinear functions, and identifying an equivalent transformed form.", fmt: "Roughly 35% of the Mathematics section; some items are typed responses.", tip: "Graph it in Desmos and compare. The calculator is allowed for the whole section." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "inside the bracket moves the graph horizontally and reverses the sign; outside moves it vertically and does not."],

  summary: [
    "Name all four families: translation, reflection, stretch and compression.",
    "Read a, b, h and k straight from the general form.",
    "Predict where a graph will land before plotting a single point.",
    "Write the equation of a transformed graph from its picture.",
    "Explain why horizontal changes behave in the opposite direction.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 1-3: Piecewise-Defined Functions (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on horizontal shifts.",
  ],

  notes: {
    cover: "Second lesson of Week 2 for 10A and 10C, following Key Features of Functions.",
    objectives: "Both objectives are verbatim from the curriculum map. Note the map lists only HSF.BF.B.3 and HSF.IF.B.5 for this lesson, and only MP.5 and MP.7 — do not add others.",
    vocabulary: "All six terms are the map's list for this lesson. 'Scaling' is the umbrella term for stretch and compression — students often think it is a third, separate thing.",
    prior: "If a student cannot say what f(x−2) does, they will not survive the modelled example. Watch for it in the diagnostic.",
    diagnose: "Answers: up 3; right 2; reflection in the x-axis; vertical stretch by 4; reflection in the y-axis. Expected gap: Q2 — students say 'left 2'. If more than half do, reteach before modelling.",
    quickCheck: "Answer: vertical compression by a factor of one half; translation 4 left; translation 1 down. Watch for students who say 'right 4'.",
    guided: "Answers — 1: translation 5 right and 2 up, vertex (5, 2). 2: reflection in the x-axis and a vertical stretch by 3. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference.",
    production: "Answers — (a) vertex (30, 18): the arch is highest 30 m across the span, at 18 m. (b) h(x) = −0.02(x−30)² + 22, a translation 4 up. (c) h(x) = −0.02(x−110)² + 18, a translation 80 right. (d) changing 0.02 changes the width and the whole shape, not just the height — the supports would no longer be 60 m apart.",
    geogebra: "Setting a and b both negative is the interesting case: the graph is reflected twice and students expect it to return to the parent. It does not, unless h and k are zero.",
    gate: "Answer: g(x) = −(x+2)² + 7; reflection in the x-axis, translation 2 left and 7 up; the horizontal shift uses the opposite sign because the input must change to compensate. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — students who can articulate the sign trap rarely fall into it.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

// =====================================================================
// GRADE 11 · TOPIC 5 · LESSON 3 — Graphing Radical Functions
// =====================================================================
const GR11_L3 = {
  out: "Gr11_T5_L3_Graphing_Radical_Functions.pptx",
  deckTitle: "Graphing Radical Functions — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 5 · RATIONAL EXPONENTS AND RADICAL FUNCTIONS · LESSON 3",
  lessonTitle: "Graphing Radical Functions",
  titleSize: 40,
  subtitle: "Two parent curves, and everything you already know about transformations",
  titleEq: "r_parent_w", titleEqK: 2.1,
  titleEqAlt: "f of x equals the square root of x, and f of x equals the cube root of x",
  grade: "Grade 11", week: "Week 2 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 5 · Lesson 5-3",
  lessonRef: "Lesson 5-3 — Graphing Radical Functions",
  nextLesson: "Solving Radical Equations",

  codes: ["HSA.REI.A.2", "HSF.IF.C.7.B", "HSF.BF.B.3", "HSF.BF.B.4"],
  mps: ["MP.4", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Graph radical functions and transformations of radical functions.",
    "Write an equation for the transformation of a radical function given a graph.",
  ],
  essentialQuestion: "How does the graph of f(x) = nth root of x change depending on whether n is even or odd?",

  vocabulary: [
    { term: "Radical function", def: "A function whose variable sits underneath a radical sign." },
    { term: "Parent radical function", def: "The simplest member of the family — no stretch, no shift, no reflection." },
    { term: "Square root function", def: "Index 2. Defined only where the radicand is not negative, so it is half a curve." },
    { term: "Cube root function", def: "Index 3. Defined for every real number, so it runs across the whole plane." },
    { term: "nth root function", def: "The general case. The index n decides the domain, and nothing else does." },
    { term: "Transformations", def: "The same four families as any function: translate, reflect, stretch, compress." },
  ],
  vocabSub: "The six terms the curriculum map lists for this lesson",

  prior: [
    { h: "Rational exponents", eq: "r_nth", d: "A radical is an exponent in disguise — Lesson 5-2." },
    { h: "Domain in interval form", eq: "r_dom_even", d: "Square brackets include the endpoint." },
    { h: "The general form", eq: "r_general", d: "The same a, b, h and k you met in Grade 10." },
  ],
  priorSub: "Three things you already have — this lesson only combines them",
  carryOver: "You are not learning new transformations today. You are applying the ones you already know to two new parent curves. The only genuinely new idea is that the index decides whether the domain is half the line or all of it.",
  carryOverEq: "r_general_w",

  diagnose: {
    title: "Warm-Up: Domain First",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "r_ws2", t: "State the domain in interval notation." },
      { eq: "r_ws4", t: "State the domain in interval notation." },
      { eq: "r_ws3", t: "Describe the transformation of the parent function." },
      { eq: "r_ws1", t: "Describe the transformation of the parent function." },
      { eq: "r_ws6", t: "State the domain. Careful — this one is not what it looks like." },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to modelling.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "Two Parents, One Question: Is the Index Even or Odd?",
      sub: "Objective 1 — and this is the essential question, answered",
      graph: "g_radical_parents", graphW: 12.43, graphY: 2.5,
      graphAlt: "Two graphs side by side: the square root of x starting at the origin and running right only, and the cube root of x running through every quadrant",
      bar: ["THE WHOLE ANSWER IN ONE LINE", "An EVEN index cannot accept a negative radicand, so the graph is half a curve starting at one point. An ODD index accepts anything, so the graph runs across the entire plane."],
      barY: 6.34,
      notes: "This slide answers the essential question directly — put it on the board and leave it there. Ask why an even root of a negative is not real, and let a student explain rather than telling them.",
    },
    {
      title: "Modelled Example — I Think Aloud",
      sub: "Objective 1 — three transformations applied to a square root",
      graph: "g_radical_worked", graphW: 6.4, graphY: 2.42,
      graphAlt: "The square root of x shown dashed, and g of x equals 2 root x minus 3 plus 1 stretched and translated, with its start point marked at 3 comma 1",
      panel: {
        h: "WATCH MY THINKING",
        items: [
          "Read the form: a = 2, h = 3, k = 1.",
          "Find the start point first — it is at (h, k), so (3, 1).",
          "The domain begins where the radicand is zero: x ≥ 3.",
          "a = 2 stretches it vertically — it rises twice as fast.",
          "Then I plot two easy points: x = 4 gives 3, x = 7 gives 5.",
          "Three points and the shape I already know is enough.",
        ],
      },
      panelX: 6.95, panelW: 5.93, panelH: 4.1,
      notes: "The start point is the whole technique. Students who plot a table of values from x = 0 waste four minutes and get a wrong domain. Model finding (h, k) FIRST, every time.",
    },
    {
      title: "Reading a Graph Backwards",
      sub: "Objective 2 — writing the equation when you are given the picture",
      rows: [
        ["Find the start point.", "That gives you h and k straight away — the graph starts at (h, k)."],
        ["Decide the index.", "Half a curve means an even index. A full S-shape through the plane means an odd one."],
        ["Check the direction.", "Rising left to right means a is positive; falling means a is negative."],
        ["Find one more point.", "Substitute it in and solve for a. One point is all you need."],
        ["Write it and test it.", "Put a second point through your equation. If it fails, the sign of h is the usual culprit."],
      ],
      rowsHead: ["Step", "What to do"],
      rowsCw: [4.2, 8.23], rowH: 0.66, rowsTop: 2.4,
      bar: ["THE ORDER MATTERS", "Start point, then index, then direction, then scale. Doing it in this order means you never have to guess — each step narrows what is left."],
      barY: 6.28,
      notes: "This is a procedure, and it is worth writing on the board as five numbered steps. Students who try to find a first almost always get h and k wrong.",
    },
  ],

  quickCheck: {
    lead: "Sketch and state the domain of", leadW: 4.6,
    eq: "r_qc", k: 2.4,
    think: "Where is the start point? Which way does it open, and how far has it moved?",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example with a negative value of a.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "r_g1", t: "State the start point and the domain, then sketch it.", hint: "The radicand cannot be negative. Where does it equal zero?" },
      { eq: "r_g2", t: "Describe every transformation, and state the domain.", hint: "Odd index — so the domain is not restricted at all." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["State the domain of four square root functions.", "Match four equations to four sketched graphs.", "Sketch two translations of the parent square root function.", "Name the start point for each of three given equations."],
        help: "You may use: the five-step table on the board, and a partner.",
        done: "every domain is in correct interval notation.", eq: "r_ws2" },
      { items: ["Sketch three transformed radical graphs, including one cube root.", "Write the equation for two graphs given only their pictures.", "Compare the domains of an even-index and an odd-index function.", "One context question: stopping distance as a radical function."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "your equation reproduces the graph you were given.", eq: "r_ws7" },
      { items: ["Explain why the graph of the square root of −x is a reflection, not an error.", "Show that a cube root graph has rotational symmetry about the origin.", "Find a transformation of the square root that has domain (−∞, 4]."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "r_ws8" },
    ],
  },

  production: {
    title: "The Speed of a Falling Object",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A maintenance crew works on a tower in the King Abdullah Financial District. For safety planning they need the speed at which a dropped object reaches the ground. Ignoring air resistance, speed in metres per second relates to drop height h in metres by the function below, with g = 9.8 m/s².",
    eq: "ctx_speed_w", eqK: 1.9,
    tasks: [
      "(a)  What kind of function is this? Name the parent and state its domain in this context.",
      "(b)  Sketch v against h for heights from 0 to 50 m. Label two exact points.",
      "(c)  Doubling the drop height does NOT double the speed. Use the graph to explain why, in one sentence.",
      "(d)  By what factor must the height increase for the speed to double? Justify it algebraically.",
    ],
    note: "Exact values where you can; two decimal places only when the question asks.",
    aiPrompt: "“Check whether my domain is right for this context, and challenge any step I cannot justify.”",
  },

  geogebra: {
    sub: "Drag the index and watch the domain change",
    explore: "plot the nth root of x with a slider on n. Step n through 2, 3, 4, 5, 6. Watch what happens to the left half of the plane each time n changes parity — then explain it.",
  },

  gate: {
    graph: "g_radical_gate",
    graphAlt: "A square root curve starting at minus 1 comma minus 4 and rising to the right",
    items: [
      { t: "Write the equation of the graph shown.", eq: null },
      { t: "State its domain and range in interval notation.", eq: null },
      { t: "In ONE sentence, say how you knew the index was even.", eq: null },
    ],
    footer: "Exact answers only. No decimals, no calculator.",
    routing: "PASS → Enrichment & Challenge (radical functions with a horizontal stretch).      NOT YET → Targeted Learning Clinic on start points and domain, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the route", d: "Lay out your falling-object solution as a clean chain: parent, domain, transformation, sketch — each step justified." },
      { h: "Expose the trap", d: "Add one worked NON-example: a domain taken from the equation without checking the radicand, and a sentence saying why it fails." },
      { h: "Say why it matters", d: "One caption — “why the speed does not double when the height does” — in language a non-maths student would understand." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 5 anchor set.",
    reflection: "which is still harder for you — finding the start point, or getting the domain right?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Recognising a root relationship in a data or graph item, and estimating from it quickly.", fmt: "Multiple choice, about 75 seconds per item.", tip: "If doubling the input does not double the output, suspect a root." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Radical and rational expressions sit in the Grade 11 band — 30% of the mathematics questions.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Check the domain before you check the answer. Wrong-domain options are always offered." },
    { code: "SAT", full: "College Board", skill: "Advanced Math — nonlinear functions, and equivalent forms of a radical expression.", fmt: "Roughly 35% of the Mathematics section.", tip: "Desmos is allowed for the whole section. Graph it and read the start point off." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "an even index restricts the domain; an odd index does not. Everything else on this slide follows from that one fact."],

  summary: [
    "Sketch both parent radical functions from memory.",
    "Say why an even index halves the plane and an odd index does not.",
    "Find the start point of a transformed radical function from its equation.",
    "State domain and range in interval notation, every time.",
    "Write the equation of a radical graph you are shown, in five steps.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for Lesson 5-4: Solving Radical Equations (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on start points.",
  ],

  notes: {
    cover: "First lesson of Week 2 for 11B, following Properties of Exponents and Radical Functions.",
    objectives: "Both objectives verbatim from the map. NOTE: the curriculum map titles this lesson 'Graphing Rational Functions', but every objective, the essential question and all six vocabulary terms are about RADICAL functions — and the syllabus calls it Graphing Radical Functions. The map's title is a typo; we follow the objectives.",
    vocabulary: "All six terms are the map's list. Draw the link back to Lesson 5-2: parent radical function is just the a = 1, h = k = 0 case.",
    prior: "Students who did not secure rational exponents in 5-2 will struggle to see why the index controls the domain. Check in the diagnostic.",
    diagnose: "Answers: [2, ∞); (−∞, ∞); reflection in the x-axis; translation 5 up; (−∞, 0]. Q5 is the interesting one — the radicand is −x, so the domain is x ≤ 0, not x ≥ 0.",
    quickCheck: "Answer: start point (−5, −2), domain [−5, ∞). Watch for students who write [5, ∞).",
    guided: "Answers — 1: start (4, 0), domain [4, ∞). 2: reflection in the x-axis and translation 2 up, domain (−∞, ∞). Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. The Mastery Gate is never differentiated, because it is the evidence.",
    production: "Answers — (a) square root parent, domain h ≥ 0 (physically, 0 to the tower height). (b) points (0,0) and (5, 9.9). (c) the graph flattens: equal increases in height give smaller increases in speed. (d) height must increase by a factor of 4, since v is proportional to the square root of h.",
    geogebra: "The parity pattern is the point. Even n gives half a curve, odd n gives a full one — and students discover it rather than being told.",
    gate: "Answer: g(x) = 3√(x+1) − 4; domain [−1, ∞), range [−4, ∞); the index is even because the graph is half a curve with a definite start point. Score live and route privately.",
    smart: "The non-example is the highest-value part. A student who can articulate the domain trap rarely falls into it.",
    exams: "11C sit both SAAT and SAT — this lesson feeds both directly.",
    summary: "Lesson 5-4 needs today's domain fluency, so the flipped video is not optional for anyone.",
  },
};

// =====================================================================
// GRADE 11 · TOPIC 5 · LESSON 4 — Solving Radical Equations
// =====================================================================
const GR11_L4 = {
  out: "Gr11_T5_L4_Solving_Radical_Equations.pptx",
  deckTitle: "Solving Radical Equations — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  topicLine: "TOPIC 5 · RATIONAL EXPONENTS AND RADICAL FUNCTIONS · LESSON 4",
  lessonTitle: "Solving Radical Equations",
  titleSize: 42,
  subtitle: "Square both sides — then find out which of your answers was never really there",
  titleEq: "s_head_w", titleEqK: 2.4,
  titleEqAlt: "the square root of x plus 5 equals x minus 1",
  grade: "Grade 11", week: "Week 2 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 5 · Lesson 5-4",
  lessonRef: "Lesson 5-4 — Solving Radical Equations",
  nextLesson: "Function Operations and Composition",

  codes: ["HSA.REI.A.1", "HSA.REI.A.2", "HSA.CED.A.4"],
  mps: ["MP.2", "MP.3"],
  assessments: ASSESS,

  objectives: [
    "Solve an equation involving radicals.",
    "Determine if a solution to an equation involving radicals is valid or extraneous.",
    "Solve an inequality involving radicals.",
  ],
  essentialQuestion: "What strategy can be used to solve equations involving radicals?",

  vocabulary: [
    { term: "Extraneous solution", def: "A value that appears when you solve an equation, satisfies the squared version, but does NOT satisfy the original. It is not a mistake in your algebra — it is created by the squaring step itself, which is why checking is compulsory rather than optional.", eq: "s_check_no", k: 1.4 },
  ],
  vocabSub: "One term — and it is the whole point of this lesson",

  prior: [
    { h: "Inverse operations", eq: "s_g1", d: "Squaring undoes a square root. That is the strategy." },
    { h: "Solving quadratics", eq: "s_step5", d: "Squaring usually produces one." },
    { h: "Domain of a radical", eq: "r_dom_even", d: "An even root cannot be negative — remember 5-3." },
  ],
  priorSub: "Three things from earlier lessons — today they combine into one method",
  carryOver: "Squaring both sides is a legal move, but it is not reversible. It can turn a false statement into a true one — which means it can hand you a solution that never satisfied the original equation. The check at the end is not tidying up; it is part of the method.",

  diagnose: {
    title: "Warm-Up: Undo the Radical",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "s_ws1", t: "Solve." },
      { eq: "s_ws2", t: "Solve." },
      { eq: "s_ws3", t: "Solve. Careful — the index is 3." },
      { eq: "s_ws4", t: "Solve." },
      { eq: "s_step2", t: "Expand the right-hand side fully." },
    ],
    routing: "0–2 correct → re-teach table with me.      3–4 correct → straight to modelling.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "The Method — Five Steps, and the Fifth Is Not Optional",
      sub: "Objective 1 — one worked example, every step justified",
      rows: [
        [{ eq: "s_step1" }, "Isolate the radical. Here it already is."],
        [{ eq: "s_step2" }, "Square both sides. This is the step that can create a false solution."],
        [{ eq: "s_step3" }, "Expand carefully. (x−1)² is NOT x²−1."],
        [{ eq: "s_step4" }, "Collect everything on one side."],
        [{ eq: "s_step5" }, "Factorise and solve."],
        [{ eq: "s_step6" }, "Two candidates. Now check BOTH in the ORIGINAL equation."],
      ],
      rowsHead: ["Step", "What is happening, and why"],
      rowsCw: [4.6, 7.83], rowH: 0.6, rowsTop: 2.36,
      bar: ["STEP 5 IS THE LESSON", "Every radical equation you solve by squaring produces candidates, not answers. They become answers only after they survive the check."],
      barY: 6.24,
      notes: "Write the five steps on the board and leave them there all lesson. Name the misconception aloud: (x−1)² is not x²−1. Have a student expand it on the board before you continue.",
    },
    {
      title: "Why an Extraneous Solution Appears",
      sub: "Objective 2 — the graph makes it obvious",
      graph: "g_extraneous", graphW: 6.4, graphY: 2.42,
      graphAlt: "The curve y equals root x plus 5 and the line y equals x minus 1 crossing once at x equals 4, with open circles at x equals minus 1 showing the curve at 2 and the line at minus 2",
      panel: {
        h: "READ THE PICTURE",
        items: [
          "The curve and the line meet ONCE, at x = 4. That is the only solution.",
          "At x = −1 the curve is at 2 and the line is at −2.",
          "They are 4 apart — not equal.",
          "But squaring makes 2 and −2 the same number.",
          "That is exactly how the false solution gets in.",
          "The check throws it back out again.",
        ],
      },
      panelX: 7.05, panelW: 5.83, panelH: 4.1,
      notes: "This slide is the conceptual heart of the lesson. Do not rush it. Ask: what does squaring do to a negative number? Then ask why that matters here. Let them say it before you do.",
    },
    {
      title: "Radical Inequalities",
      sub: "Objective 3 — two conditions, not one",
      graph: "g_inequality", graphW: 5.9, graphY: 2.46,
      graphAlt: "The curve y equals root x minus 2 with the horizontal line y equals 3, meeting at x equals 11, and the solution interval from 2 to 11 marked on the axis",
      panel: {
        h: "TWO CONDITIONS",
        items: [
          "First: the radicand must not be negative — so x ≥ 2.",
          "Second: solve the inequality itself — so x < 11.",
          "The answer is where BOTH hold at once.",
          "Written together: 2 ≤ x < 11.",
          "Forgetting the domain gives x < 11, which wrongly includes x = 0.",
        ],
        fs: 12,
      },
      panelX: 6.55, panelW: 6.33, panelH: 3.2,
      warn: { h: "THE MOST COMMON ERROR", d: "Solving the inequality and forgetting the domain. The radicand condition is half the answer, every single time.", eq: "s_ineq_ans" },
      warnY: 5.82,
      notes: "Ask what √(x−2) would mean at x = 0. The answer 'it is not a real number' is the justification for the first condition. Answer: 2 ≤ x < 11.",
    },
  ],

  quickCheck: {
    lead: "Solve, and check every candidate:", leadW: 4.8,
    eq: "s_qc", k: 2.4,
    think: "Square it, solve the quadratic, then test BOTH answers in the original equation.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time with two extraneous candidates.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "s_g1", t: "Solve, and verify your answer in the original equation.", hint: "Square both sides. Only one candidate here." },
      { eq: "s_ws6", t: "Solve, then check both candidates. One of them will not survive.", hint: "Expand (x−3)² carefully before collecting terms." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Solve four radical equations with a single candidate each.", "Verify each answer in the original equation, showing the substitution.", "Solve two cube root equations — no extraneous solutions arise.", "Say in one sentence why checking still matters."],
        help: "You may use: the five-step method on the board, and a partner.",
        done: "every answer is substituted back and shown to work.", eq: "s_ws2" },
      { items: ["Solve three equations that produce two candidates each.", "Identify and reject every extraneous solution, with the substitution shown.", "Solve two radical inequalities, stating both conditions.", "One context question: a pendulum period."],
        help: "You may use: the worked example, and the sentence frames.",
        done: "every rejected candidate has a reason written beside it.", eq: "s_ws6" },
      { items: ["Explain why squaring can create solutions but never loses them.", "Construct a radical equation whose only candidate is extraneous.", "Explain why cube root equations do not produce extraneous solutions."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument, not just an answer.", eq: "s_ws7" },
    ],
  },

  production: {
    title: "Timing the Swing of a Pendulum",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A science museum in Riyadh is installing a Foucault pendulum in its atrium. The period T, in seconds, of a pendulum of length L metres is given by the formula below, with g = 9.8 m/s². The designers need a period of exactly 6 seconds.",
    eq: "ctx_pend_w", eqK: 1.8,
    tasks: [
      "(a)  Rearrange the formula to make L the subject. Show every step.",
      "(b)  Find the exact length needed for a period of 6 seconds, then give it to two decimal places.",
      "(c)  The atrium can only take a 12 m cable. What is the longest period achievable? Justify it.",
      "(d)  Explain why doubling the length does not double the period, referring to the formula.",
    ],
    note: "Rearranging is objective 3 in disguise — HSA.CED.A.4.",
    aiPrompt: "“Check my rearrangement, and challenge any step where I have not said why it is allowed.”",
  },

  geogebra: {
    sub: "See the extraneous solution appear and disappear",
    explore: "plot y = √(x+5) and y = x−1 together. Then plot y = x+5 and y = (x−1)² — the squared versions. Count the intersections in each picture. Where did the extra one come from?",
  },

  gate: {
    items: [
      { t: "Solve this equation, showing every step.", eq: "s_gate" },
      { t: "Check BOTH candidates in the original equation and state which is extraneous.", eq: null },
      { t: "In ONE sentence, explain why squaring both sides can create a solution that was never there.", eq: null },
    ],
    footer: "Exact answers only. A correct value with no check does not pass question 2.",
    routing: "PASS → Enrichment & Challenge (equations with two separate radicals).      NOT YET → Targeted Learning Clinic on checking candidates, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the chain", d: "Lay out your pendulum solution as a clean chain of equivalent equations, each step justified by a named property." },
      { h: "Expose the trap", d: "Add one worked NON-example: a radical equation solved without checking, with the extraneous answer left in — and a sentence on how to catch it." },
      { h: "Say why it matters", d: "One caption — “why an engineer checks an answer against the original problem” — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 5 anchor set.",
    reflection: "which is still harder for you — the algebra of squaring, or remembering that the check is part of the method?",
  },

  exams: [
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Quick solution of simple root equations inside a word problem.", fmt: "Multiple choice, about 75 seconds per item.", tip: "Substitute the options back. With four choices it is often faster than solving." },
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Radical equations and rearranging formulae — Grade 11 band, 30% of the mathematics questions.", fmt: "Four-option multiple choice, mixed with the other subjects.", tip: "Extraneous roots are deliberately offered as distractors. Always check." },
    { code: "SAT", full: "College Board", skill: "Advanced Math — nonlinear equations in one variable, and rearranging a formula.", fmt: "Roughly 35% of the Mathematics section; some are typed responses.", tip: "On typed responses there are no options to check against, so verify your own answer." },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "an extraneous root is not a mistake you made — it is produced by squaring, and the only defence is substituting back into the original."],

  summary: [
    "Solve a radical equation by isolating and squaring.",
    "Expand a squared bracket correctly, every time.",
    "Check every candidate in the ORIGINAL equation, not the squared one.",
    "Explain what an extraneous solution is and where it comes from.",
    "Solve a radical inequality using both the domain and the inequality.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 14 questions, choose your route.",
    "Watch the flipped video for Lesson 5-5: Function Operations and Composition (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on checking candidates.",
  ],

  notes: {
    cover: "Second lesson of Week 2 for 11B, following Graphing Radical Functions.",
    objectives: "All three objectives verbatim from the map. Objective 3 — inequalities — is often skipped under time pressure; it is on the slide because the map lists it and HSA.CED.A.4 covers the rearranging.",
    vocabulary: "The map lists exactly one term for this lesson: extraneous solution. Give it a whole slide — it deserves one.",
    prior: "A student who cannot expand (x−1)² will fail every question in this lesson. Check it in the diagnostic, item 5.",
    diagnose: "Answers: 49; 21; 32; 1; x²−2x+1. Item 5 is the predictor — if they cannot expand it, the whole method collapses at step 3.",
    quickCheck: "Answer: candidates x = 3 and x = −1; only x = 3 survives, since √(2(−1)+3) = 1 ≠ −1. Watch for students who accept both.",
    guided: "Answers — 1: x = 6. 2: candidates x = 8 and x = 1; only x = 8 survives. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Every student sits the same Mastery Gate.",
    production: "Answers — (a) L = gT²/(4π²). (b) exact 9.8·36/(4π²) = 88.2/π² m ≈ 8.94 m. (c) T = 2π√(12/9.8) ≈ 6.95 s. (d) T is proportional to the square root of L, so quadrupling L doubles T.",
    geogebra: "The two-picture comparison is the point: the squared versions meet twice, the originals once. That extra intersection IS the extraneous root, made visible.",
    gate: "Answers — squaring gives x²−11x+18 = 0, so candidates x = 9 and x = 2. Only x = 9 survives: √(2+7) = 3 ≠ 2−5 = −3. Score live and route privately.",
    smart: "The non-example is the highest-value part — a student who can articulate the trap rarely falls into it.",
    exams: "Show this before homework so the practice set has an obvious purpose.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  for (const cfg of [GR10_L2, GR11_L3, GR11_L4]) await build(cfg);
})();

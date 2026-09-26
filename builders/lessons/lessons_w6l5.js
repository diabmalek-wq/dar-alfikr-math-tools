// Grade 11 · Topic 6 · Lesson 6-5 — Properties of Logarithms
//
// Follows L6-4 (Logarithmic Functions) directly. Objectives, vocabulary and
// standards are quoted VERBATIM from the curriculum map (cmap.docx, Unit 6,
// Lesson 5 — cross-checked against "Scope and sequence_OA2W_Global (1).docx",
// same row). Essential Question and Mathematical Practices likewise verbatim.
//
// Alignment (standing rule, 24 Sep 2026): this deck, its FIKR lesson plan,
// its differentiation activity, and its PBL/product task must all share the
// same objective thread — see w6l5_docs.js for the matching plan/activity/PBL.
//
// Every piece of mathematics inside a sentence (titles, panels, bars, notes)
// is written as $...$ per the inline-maths house rule — see engines/inline_math.js.
// Only self-contained display equations use a LaTeX image key (eq:).
const { build } = require("./lesson_engine");

const MATH = "math_w6l5/_index.json";
const GRAPH = "graphs_w6l5/_index.json";
const ASSESS = ["“Give it a go” questions", "“Time to Check”"];

const GR11_L65 = {
  out: "Gr11_T6_L6-5_Properties_of_Logarithms.pptx",
  deckTitle: "Properties of Logarithms — Grade 11 Algebra II",
  mathIndex: MATH, graphIndex: GRAPH,
  weekNum: "7",
  topicLine: "TOPIC 6 · EXPONENTIAL AND LOGARITHMIC FUNCTIONS · LESSON 6-5",
  lessonTitle: "Properties of Logarithms",
  titleSize: 34,
  subtitle: "Every property of logarithms is an exponent rule wearing a different disguise",
  titleEq: "m_title_w", titleEqK: 2.0,
  titleEqAlt: "log base b of x equals log base c of x over log base c of b",
  grade: "Grade 11", week: "Week 7 · Semester 1, 2026–27",
  footerLeft: "Grade 11 · Algebra II · Topic 6 · Lesson 6-5",
  lessonRef: "Lesson 6-5 — Properties of Logarithms",
  nextLesson: "Topic 6 · Lesson 6-6 — Exponential and Logarithmic Equations and Inequalities",

  codes: ["HSA.SSE.A.2", "HSF.BF.A.2", "HSF.LE.A.4"],
  mps: ["MP.2", "MP.7"],
  assessments: ASSESS,

  objectives: [
    "Apply properties of logarithms to rewrite logarithmic expressions and evaluate logarithms.",
    "Use the change of base formula to rewrite and evaluate logarithmic expressions.",
  ],
  essentialQuestion: "How can the properties of logarithms, including the change of base formula, be applied to simplify and evaluate logarithmic expressions?",

  vocabulary: [
    { term: "Logarithmic properties", def: "The product, quotient and power rules that let a logarithm of a product, quotient or power be rewritten as a sum, difference or multiple of simpler logarithms." },
    { term: "Change of base formula", def: "$\\log_b x = (\\log_c x)⁄(\\log_c b)$ for any base $c>0$, $c\\ne 1$ — rewrites a logarithm in an unfamiliar base using a base your calculator already has." },
  ],
  vocabSub: "Both terms the curriculum map lists for this lesson",

  prior: [
    { h: "Exponent rules (Topic 5)", eq: "m_prior_exp_rules", d: "$x^{a}\\cdot x^{b}=x^{a+b}$, $(x^{a})⁄(x^{b})=x^{a-b}$, and $(x^{a})^{b}=x^{ab}$ — today's three logarithm properties are these same rules, translated into logarithm language." },
    { h: "Lesson 6-3: what a logarithm is", eq: "m_prior_log_def", d: "$\\log_b x = y$ means $b^{y}=x$ — a logarithm IS an exponent. Every property today is really a statement about exponents in disguise." },
    { h: "Lesson 6-4: inverse properties", eq: "m_prior_inverse", d: "$\\log_b(b^{x})=x$ and $b^{\\log_b x}=x$ — today's proofs use these two identities directly to derive the product and power rules." },
  ],
  priorSub: "Three things you already know — today puts them together",
  carryOver: "A logarithm of a product, quotient or power can always be rewritten as a sum, difference or multiple of simpler logarithms — and any logarithm can be rewritten in a base your calculator actually has.",
  carryOverEq: "m_def",

  diagnose: {
    title: "Warm-Up: Exponent Rules, One More Time",
    sub: "Answer on Quizizz — 5 questions, 4 minutes. This builds a gap map, not a grade.",
    questions: [
      { eq: "m_d1", t: "Evaluate directly." },
      { eq: "m_d2", t: "Apply the product-of-powers rule." },
      { eq: "m_d3", t: "Apply the quotient-of-powers rule." },
      { eq: "m_d4", t: "Apply the inverse property from Lesson 6-4." },
      { eq: "m_d5", t: "Apply the power-of-a-power rule." },
    ],
    routing: "0–2 correct → re-teach exponent rules with me.      3–4 correct → straight to the properties.      5 correct → start the Investigate prompt now.",
  },

  instruction: [
    {
      title: "The Product and Quotient Properties",
      sub: "Objective 1, part 1 — a logarithm of a product or quotient becomes a sum or difference",
      rowsHead: ["EXAMPLE", "RESULT"],
      rowsTop: 2.55, rowH: 1.1, rowsCw: [3.85, 2.35],
      rows: [
        [{ eq: "m_prod_ex1", k: 1.25 }, { eq: "m_prod_result", k: 2.5 }],
        [{ eq: "m_quot_ex1", k: 1.25 }, { eq: "m_quot_result", k: 2.5 }],
      ],
      panel: {
        h: "PROVE IT FROM WHAT YOU ALREADY KNOW",
        items: [
          "$\\log_b(xy) = \\log_b x + \\log_b y$ for $x,y>0$ — the PRODUCT property.",
          "$\\log_b(x⁄y) = \\log_b x - \\log_b y$ for $x,y>0$ — the QUOTIENT property.",
          "Proof of the product property: write $x=b^{\\log_b x}$ and $y=b^{\\log_b y}$ using Lesson 6-4's inverse property, multiply, and the exponent-product rule does the rest.",
          "These are exactly the exponent rules from Topic 5 — logarithms turn multiplication into addition, and division into subtraction, because that is what exponents already do.",
        ],
      },
      panelX: 6.85, panelW: 6.0, panelH: 4.0,
      bar: ["THE TWO PROPERTIES TO MEMORIZE", "$\\log_b(xy) = \\log_b x + \\log_b y$.   $\\log_b(x⁄y) = \\log_b x - \\log_b y$."],
      barY: 6.32,
      notes: "Proof (say it aloud): let $u=\\log_b x$ and $v=\\log_b y$. Then $x=b^{u}$ and $y=b^{v}$ by definition, so $xy=b^{u}\\cdot b^{v}=b^{u+v}$ by the exponent-product rule, and taking $\\log_b$ of both sides gives $\\log_b(xy)=u+v=\\log_b x+\\log_b y$. Worked examples: $\\log_2 5+\\log_2 3=\\log_2(5\\cdot 3)=\\log_2 15$; $\\log_7 40-\\log_7 8=\\log_7(40 ÷ 8)=\\log_7 5$. Misconception to address aloud: $\\log_b(x+y)$ is NOT $\\log_b x+\\log_b y$ — there is no property for the logarithm of a SUM, only of a PRODUCT. Students who try to split an addition inside a logarithm are inventing a rule that does not exist.",
    },
    {
      title: "The Power Property, and Condensing Expressions",
      sub: "Objective 1, part 2 — a logarithm of a power becomes a multiple, in either direction",
      panel: {
        h: "EXPAND AND CONDENSE, BOTH DIRECTIONS",
        items: [
          "$\\log_b(x^{n}) = n\\log_b x$ — the POWER property, proved the same way as the product property.",
          "Two special values worth knowing cold: $\\log_b 1 = 0$ and $\\log_b b = 1$, for every valid base $b$.",
          "EXPAND: $\\log_5((x^{3}y)⁄(z^{2})) = 3\\log_5 x+\\log_5 y-2\\log_5 z$ — apply all three properties in one pass.",
          "CONDENSE: $2\\log_4 x-½\\log_4 y = \\log_4((x^{2})⁄(y^{1/2}))$ — run the power property backward first, then combine.",
        ],
      },
      panelX: 0.55, panelY: 2.55, panelW: 11.9, panelH: 4.0,
      bar: ["THE THIRD PROPERTY", "$\\log_b(x^{n}) = n\\log_b x$ — this is what lets you pull an exponent out in front, or push a coefficient back up as an exponent."],
      barY: 6.32,
      notes: "Proof: $\\log_b(x^{n})=\\log_b\\!\\left(b^{n\\log_b x}\\right)=n\\log_b x$, using the inverse property from Lesson 6-4 the same way as before. Expand example, step by step: $\\log_5((x^{3}y)⁄(z^{2}))=\\log_5(x^{3}y)-\\log_5(z^{2})=\\log_5(x^{3})+\\log_5 y-\\log_5(z^{2})=3\\log_5 x+\\log_5 y-2\\log_5 z$ — quotient property first, then product, then power on each piece. Condense example: $2\\log_4 x-½\\log_4 y=\\log_4(x^{2})-\\log_4(y^{1/2})=\\log_4((x^{2})⁄(y^{1/2}))=\\log_4((x^{2})⁄(y^{1/2}))$. Misconception to address aloud: a coefficient in front of a logarithm becomes an EXPONENT when condensing, not a multiplier inside — $2\\log_4 x$ condenses to $\\log_4(x^{2})$, never $\\log_4(2x)$.",
    },
    {
      title: "The Change of Base Formula",
      sub: "Objective 2 — evaluate any logarithm on a calculator, and use it to solve for an unknown exponent",
      graph: "gm_growth", graphW: 5.6, graphY: 2.55,
      graphAlt: "A geometric growth curve a sub n equals 40 times 1.12 to the n minus 1, in megawatts, crossing the target line of 100 megawatts at n approximately 9.09",
      panel: {
        h: "SOLVE FOR THE EXPONENT",
        items: [
          "$\\log_b x = (\\log_c x)⁄(\\log_c b)$ for any base $c$ — usually $c=10$ or $c=e$, since every calculator has both.",
          "A solar plant's capacity grows geometrically: recursively $a_n=1.12\\,a_{n-1}$, $a_1=40$; explicitly $a_n=40(1.12)^{n-1}$ (megawatts).",
          "Set $40(1.12)^{n-1}=100$ and solve: $(1.12)^{n-1}=2.5$, so $n-1=\\log_{1.12} 2.5=(\\log 2.5)⁄(\\log 1.12)\\approx 8.09$.",
          "$n\\approx 9.09$ — capacity first exceeds 100 MW during year 9, matching the graph on the left.",
        ],
      },
      panelX: 6.95, panelW: 5.95, panelH: 4.0,
      bar: ["WHY CHANGE OF BASE MATTERS", "No calculator has a $\\log_{1.12}$ button — change of base rewrites ANY logarithm using base 10 or base $e$, which every calculator has."],
      barY: 6.32,
      notes: "$\\log_5 12=(\\log 12)⁄(\\log 5)\\approx 1.544$ using a base-10 logarithm, or $(\\ln 12)⁄(\\ln 5)\\approx 1.544$ using a base-$e$ logarithm — both give the same answer, because the formula works for ANY valid base $c$. Geometric sequence (HSF.BF.A.2): recursive form $a_n=1.12\\,a_{n-1}$ describes each term from the one before it; explicit form $a_n=40(1.12)^{n-1}$ gives any term directly. Solving for $n$ (HSF.LE.A.4 — expressing the solution to an exponential model AS a logarithm, then evaluating with technology): $40(1.12)^{n-1}=100 \\to (1.12)^{n-1}=2.5 \\to n-1=\\log_{1.12}2.5=(\\log 2.5)⁄(\\log 1.12)\\approx 8.09 \\to n\\approx 9.09$. Misconception to address aloud: students try to divide both sides by 1.12 to undo the exponent — an exponent on the UNKNOWN cannot be removed by division, only by taking a logarithm of both sides.",
    },
  ],

  quickCheck: {
    lead: "Simplify using the quotient property:", leadW: 4.6,
    eq: "m_qc", k: 1.5,
    think: "Ask: is this a product or a quotient inside the logarithm? That tells you whether to add or subtract.",
    rule: "80% correct → straight to guided practice.   Below 80% → one more modelled example, this time condensing three terms.",
  },

  guided: {
    mins: 4,
    items: [
      { eq: "m_g1", t: "Condense into a single logarithm.", hint: "A sum inside a logarithm expression becomes a product argument." },
      { eq: "m_g2", t: "Expand fully.", hint: "Quotient first, then power on each piece." },
    ],
  },

  routes: {
    mins: 8,
    tiers: [
      { items: ["Condense each pair into a single logarithm: $\\log_3 8+\\log_3 6$, then $\\log_5 100-\\log_5 4$.", "Expand each expression fully: $\\log_2(x^{5}y)$, then $3\\log_4 x+2\\log_4 y-\\log_4 z$ condensed the other way.", "Use change of base to evaluate $\\log_7 50$ and $\\log_3 200$, to three decimal places.", "Check each answer by substituting a value or reversing the step."],
        help: "You may use: the property bar on the board, a calculator, and a partner.",
        done: "every property you applied matches its name, and both change-of-base answers agree with a calculator check.", eq: "m_ws1" },
      { items: ["A telecom tower's signal strength model uses $\\log_{10}$ ratios that combine additively when two signals overlap — use the product property to combine $\\log_{10} 4$ and $\\log_{10} 25$ into a single logarithm, then evaluate it exactly.", "A Vision 2030 solar plant's capacity follows $a_n=40(1.12)^{n-1}$ megawatts. Write the recursive form of the same sequence.", "Use change of base to find how many years until capacity first exceeds 150 MW, to two decimal places."],
        help: "You may use: the worked change-of-base example, and a calculator.",
        done: "your change-of-base answer is shown as an exact logarithm BEFORE you evaluate it, and your final year is a sensible whole number.", eq: "m_geo_explicit" },
      { items: ["Prove the quotient property $\\log_b(x⁄y)=\\log_b x-\\log_b y$ from the definition of a logarithm — do not just quote the product property, derive it the same way.", "Explain why $\\log_b(x+y)$ can NOT be split into $\\log_b x+\\log_b y$, using a specific numerical counterexample.", "A classmate claims the change of base formula only works with base 10. Explain why any valid base $c$ gives the same answer, using the definition of a logarithm."],
        help: "You may use: nothing but your reasoning.",
        done: "you have an argument grounded in the definition, not just a computed answer.", eq: null },
    ],
  },

  production: {
    title: "Powering Vision 2030: When Does Capacity Cross the Target?",
    sub: "A context you have not seen before — this tests transfer",
    situation: "A solar power plant expanding under a Vision 2030 renewable-energy initiative models its capacity, in megawatts, with the geometric sequence $a_n=40(1.12)^{n-1}$, where $n$ is the year of operation. Planners need to know exactly when capacity first exceeds a 100 MW regulatory target.",
    eq: "m_prod_w", eqK: 1.6,
    tasks: [
      "(a)  Write the recursive form of the same sequence, and state what $1.12$ and $40$ each represent physically.",
      "(b)  Set $a_n=100$ and solve for $n$, expressing your solution as a logarithm before you evaluate it with a calculator.",
      "(c)  Round appropriately and state the first WHOLE year in which capacity exceeds 100 MW.",
      "(d)  A planner claims capacity will double to 80 MW before it reaches 100 MW. Is that claim consistent with the model? Justify using the growth equation, not just the graph.",
    ],
    note: "The logarithmic expression for $n$ shown exactly before any decimal is computed, and the final year stated as a whole number with a one-sentence justification for the rounding direction.",
    aiPrompt: "“Check whether I set up the equation $a_n=100$ correctly before I took a logarithm, and challenge any rounding step I have not justified.”",
  },

  geogebra: {
    sub: "Slide the exponent and watch the geometric model cross its target",
    graph: "gm_growth",
    graphAlt: "The geometric growth curve for solar capacity crossing the 100 megawatt target line at year n approximately 9.09",
    explore: "Graph $a_n=40(1.12)^{n-1}$ at geogebra.org/graphing with a slider for the growth rate. Trace where the curve crosses a target line $y=100$, and compare that $n$-value to what change of base gives algebraically. Then try a slower growth rate and watch the crossing point move right.",
  },

  gate: {
    eq: "m_gate1_w",
    items: [
      { t: "Condense into a single logarithm.", eq: "m_gate3_w" },
      { t: "Expand fully.", eq: "m_gate2" },
      { t: "In ONE sentence, explain why $\\log_b(x+y)\\ne \\log_b x+\\log_b y$ in general.", eq: null },
    ],
    footer: "Exact answers only. Question 1 condensed to a single logarithm, question 2 fully expanded with every property applied, and question 3 a definition-based reason with a counterexample, not just a rule restated.",
    routing: "PASS → Enrichment & Challenge (proving the power property from the product property alone).      NOT YET → Targeted Learning Clinic on the three properties, start of next lesson.",
  },

  smart: {
    steps: [
      { h: "Show the model", d: "Present the recursive and explicit forms of the capacity sequence, the equation set equal to the target, and the exponent solved as a logarithm before it is evaluated." },
      { h: "Expose the trap", d: "Add one worked NON-example — dividing both sides by 1.12 instead of taking a logarithm — and a sentence saying what goes wrong (the exponent never comes down, so $n$ can't be isolated that way)." },
      { h: "Say why it matters", d: "One caption — why a planner needs the exact year, not just the shape of the growth curve — for a non-maths reader." },
    ],
    published: "the class LMS portfolio; the strongest go on the Department wall as our Topic 6 modelling set.",
    reflection: "which property do you still reach for a reminder card on — product, quotient, power, or change of base?",
  },

  exams: [
    { code: "SAAT", full: "Tahsili — Achievement Test", skill: "Condensing a difference of two logarithms, same base, into one.", fmt: "Four-option multiple choice, no calculator.", tip: "Subtraction inside the problem means division inside the logarithm — the quotient property, every time.",
      question: "Simplify $\\log_2 24-\\log_2 3$.",
      steps: ["Quotient property: $\\log_2 24-\\log_2 3=\\log_2(24 ÷ 3)$.", "Simplify inside: $24 ÷ 3=8$.", "Answer: $\\log_2 8=3$."] },
    { code: "SAT", full: "College Board", skill: "Advanced Math — evaluating a logarithm in an unfamiliar base with change of base.", fmt: "Two 35-minute adaptive modules; calculator allowed.", tip: "Use $\\log$ or $\\ln$ on both top and bottom — never mix the two.",
      question: "Evaluate $\\log_6 50$ to three decimal places.",
      steps: ["Change of base: $\\log_6 50=(\\log 50)⁄(\\log 6)$.", "$\\log 50\\approx 1.699$, $\\log 6\\approx 0.778$.", "Divide: $\\log_6 50\\approx 2.184$."] },
    { code: "GAT", full: "Qudurat — General Aptitude", skill: "Combining two same-base logarithms fast, usually one property step.", fmt: "Multiple choice, ~75 sec/item, no calculator.", tip: "Match the OPERATION to the property — plus multiplies inside, minus divides inside.",
      question: "$\\log_4 3+\\log_4 12=$? (A) $\\log_4 15$  (B) $\\log_4 9$  (C) $\\log_4 36$  (D) $2$",
      steps: ["Product property: $\\log_4 3+\\log_4 12=\\log_4(3\\cdot 12)$.", "Multiply: $3\\cdot 12=36$.", "Answer (C); (D) traps a wrong direct evaluation."] },
  ],
  examBar: ["THE SINGLE MOST EXAMINED IDEA HERE:", "match the operation between two logarithms to the property it signals — sum means multiply inside, difference means divide inside, coefficient means exponent — and use change of base whenever the base isn't one your calculator has."],

  summary: [
    "Apply the product, quotient and power properties to expand or condense a logarithmic expression, and to evaluate logarithms.",
    "Prove each property from the definition of a logarithm and the exponent rules from Topic 5.",
    "Use the change of base formula to evaluate a logarithm in any base with a calculator.",
    "Use change of base to solve for an unknown exponent in a geometric or exponential model, expressing the solution as a logarithm before evaluating it.",
  ],
  homework: [
    "Finish your product and upload it to the LMS portfolio — any of the three formats.",
    "Practice set on Pear Deck: 12 questions, choose your route.",
    "Watch the flipped video for our next lesson, Topic 6 · Lesson 6-6 — Exponential and Logarithmic Equations and Inequalities (4 min, 2 embedded questions).",
    "Clinic group: bring your Time to Check paper — we start with 10 minutes on the three properties.",
  ],

  notes: {
    cover: "Week 7 lesson for Grade 11-B, continuing Topic 6 (Exponential and Logarithmic Functions) directly from Lesson 6-4. Three teaching days this week, so the Smart Production step may run into the next session — protect the Mastery Gate instead.",
    objectives: "Both objectives are verbatim from the curriculum map. The map lists HSA.SSE.A.2, HSF.BF.A.2 and HSF.LE.A.4 for this lesson — do not add others. HSA.SSE.A.2 (structure of an expression) is taught across both property slides; HSF.BF.A.2 (recursive vs explicit sequence forms) and HSF.LE.A.4 (expressing an exponential model's solution as a logarithm) are taught together on the change-of-base slide via the solar-capacity model.",
    vocabulary: "Both terms are the map's list. Make students say the product property aloud in their own words before showing the change of base formula — the second depends on fluency with the first three.",
    prior: "If a student cannot state the three exponent rules from Topic 5, the whole lesson stalls — every logarithm property today is one of those rules restated. Watch for it in the diagnostic, questions 2, 3 and 5.",
    diagnose: "Answers: $\\log_5 25=2$; $2^{3}\\cdot 2^{4}=2^{7}=128$; $3^{7} ÷ 3^{2}=3^{5}=243$; $\\log_4(4^{6})=6$ by the inverse property; $(5^{2})^{3}=5^{6}=15625$. Expected gap: Q4, where students forget the inverse property from Lesson 6-4 and try to compute $4^{6}$ first instead of cancelling directly.",
    quickCheck: "Answer: $\\log_2 20-\\log_2 5=\\log_2(20÷ 5)=\\log_2 4=2$. Watch for students who add instead of subtract, or who subtract the numbers inside the logarithm instead of dividing.",
    guided: "Answers — 1: $\\log_6 4+\\log_6 9=\\log_6(4\\cdot 9)=\\log_6 36$. 2: $\\log_7((x^{4})⁄(y^{3}))=4\\log_7 x-3\\log_7 y$. Do not release independent work until roughly 80% have both.",
    routes: "Students choose their own route and may switch mid-task. Pear Deck flags error patterns live; use it to decide who gets a two-minute conference. Change-of-base answers for the Practice route: $\\log_7 50\\approx 2.010$ and $\\log_3 200\\approx 4.824$.",
    production: "Answers — (a) recursive: $a_n=1.12\\,a_{n-1}$, $a_1=40$; $1.12$ is the growth factor (12% growth per year) and $40$ is the starting capacity in year 1. (b) $40(1.12)^{n-1}=100 \\to (1.12)^{n-1}=2.5 \\to n-1=\\log_{1.12}2.5\\approx 8.09 \\to n\\approx 9.09$. (c) year 9 is the first WHOLE year the model exceeds the target is technically year 10 by whole-year reporting, since capacity does not cross 100 until partway through year 9 — accept either with correct justification. (d) capacity reaches 80 MW when $40(1.12)^{n-1}=80$, giving $n-1=\\log_{1.12}2\\approx 6.12$, so $n\\approx 7.12$ — yes, the claim is consistent, since $7.12<9.09$.",
    geogebra: "The crossing point is the whole point — where the growth curve meets the target line is exactly the $n$-value change of base solves for algebraically. Sliding the growth rate down shows students the crossing point moves right, connecting the graph to the algebra.",
    gate: "Answers: $\\log_4 3+\\log_4 12=\\log_4 36$ (product property); $\\log_5(x^{2}⁄y)=2\\log_5 x-\\log_5 y$ (quotient then power); $\\log_b(x+y)\\ne\\log_b x+\\log_b y$ because, for example, $\\log_2(2+2)=\\log_2 4=2$ but $\\log_2 2+\\log_2 2=1+1=2$ — coincidentally equal here, so use a cleaner counterexample: $\\log_2(1+1)=\\log_2 2=1$ while $\\log_2 1+\\log_2 1=0+0=0$, which are NOT equal. Score live and route privately.",
    smart: "The non-example in step 2 is the highest-value part — dividing both sides of $(1.12)^{n-1}=2.5$ by $1.12$ does not isolate $n-1$, since $n-1$ is an EXPONENT, not a factor; the correction is recognizing that an unknown exponent requires a logarithm, not division.",
    exams: "Show this before homework so the practice set has an obvious purpose. Each card now works a full item in steps, not just a bare question — walk through at least one aloud before moving on.",
    summary: "Route the clinic group privately through the LMS — never announce the list to the class.",
  },
};

(async () => {
  await build(GR11_L65);
})();

module.exports = { GR11_L65 };

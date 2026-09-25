// Pre-session home tasks (FIKR Phase 0) for the Week 3 lessons.
// Four slides: cover · the one idea + video slot · one worked example ·
// readiness check that feeds the in-class Diagnose.
const { build } = require("./build_presession");
const fs = require("fs");
const path = require("path");

const M = JSON.parse(fs.readFileSync(path.join(__dirname, "math_w3/_index.json"), "utf8"));
const common = { math: M };

// ------------------------------------------------- Gr10 1-3
const GR10_L3 = {
  ...common,
  out: "PreSession_Gr10_T1_L3_Piecewise_Defined_Functions.pptx",
  deckTitle: "Pre-Session Task — Piecewise-Defined Functions (Grade 10)",
  title: "Piecewise-Defined Functions",
  grade: "Grade 10", week: "Week 3 · Semester 1, 2026–27",
  footerLeft: "Pre-session task · Grade 10 · Algebra II · Topic 1 · Lesson 3",
  codes: ["HSF.IF.B.5", "HSF.IF.C.7.B", "HSF.LE.A.2", "HSS.ID.B.6.A", "MP.4", "MP.5"],
  coverSub: "One function, more than one rule — and the boundary decides which one you use",
  ideaTitle: "Choose The Rule Before You Substitute",
  ideaSub: "Every input belongs to exactly one piece of the domain",
  ideaText: "A piecewise-defined function carries two or more rules, each one used on its own part of the domain. The parts are disjoint — they share no point — so no input can obey two rules at once. Decide which piece your input lives in FIRST. Then substitute.",
  ideaEq: "p_general", ideaEqK: 1.5,
  ideaEqAlt: "f of x equals rule one for x less than a, and rule two for x greater than or equal to a",
  videoTitle: "One function, more than one rule",
  recall: [
    { h: "Absolute value", eq: "p_abs", d: "A piecewise function you already know." },
    { h: "Round DOWN", eq: "p_floor_ex", d: "The floor function. Watch the negatives." },
    { h: "Round UP", eq: "p_ceil_ex", d: "The ceiling function. Also watch the negatives." },
  ],
  worked: [
    { eq: "p_ex", say: "Two rules. The boundary is at x = 1, and ≥ tells you the second rule owns it." },
    { eq: "p_ex_a", say: "x = −2 is less than 1, so the FIRST rule applies. f(−2) = −3." },
    { eq: "p_ex_b", say: "x = 1 sits on the boundary, and the second rule has ≥. So f(1) = 4." },
    { eq: "p_ex_c", say: "x = 4 is greater than 1, so the second rule again. f(4) = 1." },
  ],
  misconception: "substituting into whichever rule you read first. Check the subinterval before you touch the algebra — that is the whole skill.",
  check: [
    { eq: "p_d1", t: "Find f(−2) and f(0). Say which rule you used each time." },
    { eq: "p_d3", t: "Evaluate the floor." },
    { eq: "p_d4", t: "Evaluate the ceiling." },
    { t: "In one sentence: why must the two pieces of the domain share no point?" },
  ],
  nextStep: "a 5-question Quizizz on choosing the rule, floors and ceilings. Then we graph these functions and get the circles right.",
  notesCover: "Pre-session for Gr10 1-3. Send with the flipped video 48 hours before the lesson.",
};

// ------------------------------------------------- Gr11 5-5
const GR11_L5 = {
  ...common,
  out: "PreSession_Gr11_T5_L5_Operations_on_Functions.pptx",
  deckTitle: "Pre-Session Task — Operations on Functions (Grade 11)",
  title: "Operations on Functions",
  grade: "Grade 11", week: "Week 3 · Semester 1, 2026–27",
  footerLeft: "Pre-session task · Grade 11 · Algebra II · Topic 5 · Lesson 5-5",
  codes: ["HSF.BF.A.1.B", "(+)HSF.BF.A.1", "MP.4", "MP.7"],
  coverSub: "Add them, multiply them — or feed one straight into the other",
  ideaTitle: "Inside First",
  ideaSub: "The symbol order and the working order are opposites",
  ideaText: "You can combine two functions by adding, subtracting, multiplying or dividing their outputs. You can also feed one into the other — that is composition. In (f ∘ g)(x), the INSIDE function g acts on x first, and f acts on whatever g produced.",
  ideaEq: "o_comp", ideaEqK: 1.7,
  ideaEqAlt: "f composed with g of x equals f of g of x",
  videoTitle: "Inside first",
  recall: [
    { h: "Add the outputs", eq: "o_sum", d: "The domain is where both are defined." },
    { h: "Divide the outputs", eq: "o_quot", d: "Exclude every zero of the bottom function." },
    { h: "Compose them", eq: "o_comp2", d: "Here f runs first. Order changes everything." },
  ],
  worked: [
    { eq: "o_fg", say: "One pair of functions. We will combine them four ways and compose them twice." },
    { eq: "o_ex_sum", say: "The sum: add the two outputs and collect like terms." },
    { eq: "o_ex_comp1", say: "f of g: replace every x in f with the WHOLE of g, bracket and all." },
    { eq: "o_ex_comp2", say: "g of f: now f runs first. A different function — this is the point of the lesson." },
  ],
  misconception: "reading (f ∘ g)(x) left to right and applying f first. It is the inside function that meets x, so g runs first.",
  check: [
    { eq: "o_g1", t: "Write (f + g)(x) as a single expression." },
    { eq: "o_pk1", t: "Evaluate, for f(x) = x² and g(x) = x + 1. Inside out." },
    { eq: "o_pk2", t: "Expand fully. This is the step that gets dropped in composition." },
    { t: "In one sentence: why is (f ∘ g)(x) usually different from (g ∘ f)(x)?" },
  ],
  nextStep: "a 5-question Quizizz on combining and composing. Then both compositions of one pair, and a Saudi pricing problem.",
  notesCover: "Pre-session for Gr11 5-5. Send with the flipped video 48 hours before the lesson.",
};

const NOTES = {
  notesWhy: "", notesMap: "", notesStd: "", notesFmt: "", notesExpect: "",
  notesTools: "", notesRules: "", notesStart: "The readiness check feeds straight into the in-class Diagnose — collect it before the bell.",
};

(async () => {
  for (const cfg of [GR10_L3, GR11_L5]) await build({ ...NOTES, ...cfg });
})();

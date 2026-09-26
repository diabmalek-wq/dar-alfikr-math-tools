// Week 7 pre-session sheet — Grade 10, Topic 2 · Lesson 1, Vertex Form of a
// Quadratic Function.
//
// Objectives and standards quoted VERBATIM from lessons_w7.js, itself quoted
// verbatim from "Curriculum map A2 OBLAS.docx", Unit 2, Lesson 1 — see that
// file's header note.
//
// The three priors below are exactly the "prior" block lessons_w7.js already
// teaches from (transformations, the parent function, evaluating a function)
// — the same equations, freshly rendered under p7_ keys so the presession
// sheet does not depend on the lesson's own math_w7 index.
const { build } = require("../../engines/presession");

build({
  who: "Grade 10",
  week: "Week 7",
  out: "PreSession_Gr10_T2_L1_Vertex_Form.docx",
  headerLine: "Grade 10 · Algebra II · Week 7 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Getting Ready for Vertex Form",
  sub: "Classes 10A and 10B · this week opens Topic 2 with Lesson 2-1, Vertex Form of a "
     + "Quadratic Function — every parabola you meet from here on is the parent function "
     + "y = x² wearing a disguise.",
  covers: [
    ["HSF.IF.C.7.A", "Graph quadratic functions given in vertex form."],
    ["HSF.BF.B.3", "Write a quadratic function in vertex form given its key features."],
  ],
  priors: [
    { skill: "Describe a transformation of a function", eq: "p7_transform",
      note: "Inside the parentheses moves the graph sideways (and flips the sign); outside moves it up or down." },
    { skill: "Picture the parent function", eq: "p7_parent",
      note: "y = x² — vertex (0, 0), opens up. Every parabola this topic starts from this one shape." },
    { skill: "Evaluate a function at a value", eq: "p7_eval",
      note: "Substitute the input, read off the output. You will use this to check a vertex or a point on any parabola." },
  ],
  vocab: [
    ["Parabola", "the rounded, symmetric curve that is the graph of any quadratic function"],
    ["Parent quadratic function", "the simplest quadratic, f(x) = x²"],
    ["Vertex", "the turning point of a parabola — its lowest or highest point"],
    ["Vertex form", "f(x) = a(x − h)² + k, with vertex (h, k) read directly off the equation"],
    ["Axis of symmetry", "the vertical line x = h through the vertex"],
    ["Minimum / maximum value", "the vertex's y-value — smallest output if a > 0, largest if a < 0"],
  ],
  appearsTitle: "WHERE THIS SHOWS UP LATER",
  appearsNote: "vertex form is not the end of the topic — it is the beginning",
  appears: [
    ["Standard form — next lesson", "Topic 2 Lesson 2 turns f(x) = ax² + bx + c back into vertex form by "
     + "completing the square. Today's skill runs in reverse there."],
    ["Modelling real motion", "A fountain's arc, a basketball's path, a bridge cable — all are solved "
     + "fastest in vertex form, because the vertex answers 'where is the highest or lowest point?' directly."],
    ["GAT and SAT alike", "Both papers ask for a parabola's maximum or minimum without a graph. Vertex "
     + "form gives it in one line — no completing the square needed in the exam room."],
  ],
  notesSub: "Three ideas. The second is the one most people get backwards the first time.",
  keys: [
    { head: "Vertex form bundles three moves onto one parent function", eq: "p7_vf",
      body: "a stretches or reflects, h shifts sideways, k shifts up or down — and the vertex is "
          + "read straight off as (h, k)." },
    { head: "The sign inside the parentheses flips", eq: "p7_signflip",
      body: "(x − 3)² has vertex at x = 3, not x = −3 — the minus sign inside is undone to find h. "
          + "This single sign-flip is the most common slip in the whole topic." },
    { head: "The sign of a tells you up or down before you graph anything", eq: "p7_signa",
      body: "No plotting needed: check the sign of a first, and you already know whether you are "
          + "hunting for a minimum or a maximum." },
  ],
  misconception:
    "Reading the vertex straight off the numbers without flipping the sign inside the parentheses — "
    + "writing the vertex of f(x) = (x − 3)² + 5 as (−3, 5) instead of (3, 5). The k outside keeps its "
    + "sign; the h inside does not.",
  warmup: [
    { q: "Evaluate.", eq: "q7_g10a" },
    { q: "Describe the shift in words.", eq: "q7_g10b" },
    { q: "Describe the shift in words.", eq: "q7_g10c" },
    { q: "Describe both shifts in words.", eq: "q7_g10d" },
    { q: "Evaluate.", eq: "q7_g10e" },
    { q: "Shifting left 3 and down 2 moves the vertex of y = x² away from (0, 0) — to where?" },
  ],
  routes: [
    "Questions 1 and 5 — evaluating a function. Substitute first, then simplify.",
    "Questions 2, 3 and 4 — naming a shift in words. Say which way AND how far for each one.",
    "Question 6: use the sign rule from question 2–4 to place the new vertex, then check it makes sense.",
  ],
  doneWhen: "you can evaluate a function at a value, describe a horizontal or vertical shift in words, "
    + "and place a shifted vertex without graphing it.",
  answers: "1) 16   2) up 7   3) right 5   4) left 2, down 3   5) 25   6) (−3,−2)",
});

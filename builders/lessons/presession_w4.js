// Week 4 pre-session sheets — Grade 10 SAT & GAT, Grade 11 SAAT & SAT, Grade 9
// Mawhiba. Grade 12 GAT is NOT here: its Week 4 sheet already exists as
// PreSession_W4_Percentages.pdf in the 20-week course series, and Mr Thiab
// confirmed on 16 Sep 2026 that the course order is the authoritative one.
//
// Week 4 anchors, taken from the distributions rather than chosen:
//   Grade 10  T1 · L4 Arithmetic Sequences and Series
//   Grade 11  T5 · L5-6 Inverse Functions
//   Grade 9   Unit 1 Linear equations · Activity 3 Number Pyramids
//
// Every warm-up answer below was recomputed in Python before this file was
// written, and no warm-up reuses a page-1 reminder's numbers.
const { build } = require("./presession");

// =====================================================================
// GRADE 10 · SAT & GAT · Week 4 — arithmetic sequences and series.
// The lesson is the bridge: a sequence with a constant difference IS a
// linear function, which is why one week's work pays into both papers.
// =====================================================================
build({
  who: "Grade 10 SAT & GAT",
  week: "Week 4",
  out: "PreSession_Gr10_SATGAT_W4.docx",
  headerLine: "Grade 10 · SAT & GAT · Week 4 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Sequences that Grow by a Fixed Step",
  sub: "Classes 10A and 10B · this week's Algebra II lesson is T1 · L4 Arithmetic Sequences "
     + "and Series — and the same idea is a GAT pattern item and an SAT linear-function item.",
  covers: [
    ["GAT-Q-ARI.5", "Numerical series and pattern recognition"],
    ["SAT-ALG.2", "Linear functions"],
    ["SAT-ALG.3", "Linear equations in two variables"],
  ],
  priors: [
    { skill: "Find the step between consecutive terms", eq: "p4_seq",
      note: "Subtract in one direction and keep it: later term minus earlier term." },
    { skill: "Reach any term without listing them all", eq: "p4_nth",
      note: "The first term is already there, so the step is applied n − 1 times, not n." },
    { skill: "Add a run of terms", eq: "p4_sum",
      note: "The average of the first and last term, times how many terms there are." },
    { skill: "Find the slope of a line through two points", eq: "p4_slope",
      note: "Same subtraction, same direction rule. This is why the two topics are one topic." },
  ],
  vocab: [
    ["Term", "one number in the sequence, counted from the first"],
    ["Common difference", "the fixed step added each time"],
    ["Arithmetic sequence", "a list where that step never changes"],
    ["Series", "the sum of the terms, not the list of them"],
    ["nth term", "a rule that gives any term straight from its position"],
    ["Partial sum", "the total of the first n terms only"],
  ],
  appearsTitle: "WHERE THIS APPEARS IN THE PAPER",
  appearsNote: "so you know what you are preparing for",
  appears: [
    ["GAT — pattern items", "A row of numbers with the next one missing. Arithmetic is about "
     + "36% of the quantitative half, and the step is found in one subtraction."],
    ["GAT — the hidden ones", "Seats in a theatre row by row, a salary rising by a fixed "
     + "amount each year. The words change; the step does not."],
    ["SAT — linear functions", "A table with a constant difference is a linear function in "
     + "disguise, and the step is the slope. The SAT asks for the rule, not the next term."],
    ["Why it is worth the time", "No calculator in GAT — one subtraction and one "
     + "multiplication is twenty seconds, not ninety."],
  ],
  notesSub: "Three ideas. The first is the one that turns this from a memory exercise into "
          + "something you can work out if you forget the formula.",
  keys: [
    { head: "An arithmetic sequence is a straight line with the positions as the x-values",
      eq: "p4_lin",
      body: "The nth term is dn plus a constant — slope d, intercept a₁ − d. The SAT calls it "
          + "a linear function and the GAT calls it a pattern: one object, two languages." },
    { head: "The sum is the average term times how many terms", eq: "p4_sum",
      body: "Pair the first with the last, the second with the second-last: every pair has the "
          + "same total. That is the whole proof, and it means you can rebuild the formula in "
          + "the exam room if it slips." },
    { head: "Count the terms — never estimate them", eq: "p4_count",
      body: "From 9 to 79 in steps of 5 there are fifteen terms, not fourteen. Divide the gap "
          + "by the step and ADD ONE — the first term was there before any step was taken." },
  ],
  misconception:
    "Two errors, and they are neighbours. Using n instead of n − 1 in the nth term gives an "
    + "answer exactly one step too big; subtracting the wrong way round for the step turns a "
    + "rising sequence into a falling one. Both are caught by the same habit — after you write "
    + "the rule, test it on a term you already know.",
  warmup: [
    { q: "Find the common difference.", eq: "q4_g10a" },
    { q: "Find the twelfth term.", eq: "q4_g10b" },
    { q: "How many terms are there?", eq: "q4_g10c" },
    { q: "Find the sum of the first twenty terms.", eq: "q4_g10d" },
    { q: "Read the common difference straight off the rule.", eq: "q4_g10e" },
    { q: "Write the nth term of 6, 13, 20, 27, …" },
  ],
  routes: [
    "Questions 1, 2 and 5 — the step and the nth term. Do them, then check each answer "
      + "against a term you can count to by hand.",
    "Questions 3 and 4 — counting the terms and summing them. Write the first and last term "
      + "down before you touch a formula.",
    "Question 6: turn the list into a rule, then explain why the rule's number in front of n "
      + "is the same as the step.",
  ],
  doneWhen: "you can find the step, write the nth term, count how many terms a sequence has, "
    + "and say why the step is the slope of a line.",
  answers: "1) 7   2) 71   3) 15   4) 610   5) 4   6) aₙ = 7n − 1",
});

// =====================================================================
// GRADE 11 · SAAT & SAT · Week 4 — inverse functions. SAAT-led, by his
// instruction on 16 Sep 2026: 11C sits Tahsili as well as the SAT, and
// the Tahsili Grade 11 row is this term's syllabus almost line for line.
// =====================================================================
build({
  who: "Grade 11 SAAT & SAT",
  week: "Week 4",
  out: "PreSession_Gr11_SAATSAT_W4.docx",
  headerLine: "Grade 11 · SAAT (Tahsili) & SAT · Week 4 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Undoing a Function",
  sub: "Class 11C · this week's lesson is T5 · L5-6 Inverse Functions, and Grade 11 content "
     + "is 30% of the Tahsili mathematics section.",
  covers: [
    ["SAAT-M-11.2", "Radical and rational expressions"],
    ["SAAT-M-11.1", "Exponents and logarithms"],
    ["SAT-ADV.1", "Equivalent expressions"],
    ["SAT-ADV.4", "Nonlinear functions"],
  ],
  priors: [
    { skill: "Substitute one function into another", eq: "p4_comp", k: 0.72,
      note: "The inner function is worked out first. Read it from the inside out." },
    { skill: "Swap and solve — the method itself", eq: "p4_inv", k: 0.72,
      note: "Swap x and y, then make y the subject again. Two steps, in that order." },
    { skill: "Move between a rational exponent and a radical", eq: "p4_rex", k: 0.72,
      note: "The bottom of the fraction is the root; the top is the power." },
    { skill: "Simplify a square root of a square", eq: "p4_sqrt", k: 0.72,
      note: "The root sign returns the non-negative value, which is why domains get restricted." },
  ],
  vocab: [
    ["Inverse function", "the function that undoes what the original did"],
    ["One-to-one", "no two inputs share an output — the horizontal line test"],
    ["Composition", "one function applied to the output of another"],
    ["Domain", "the inputs a function is allowed to take"],
    ["Range", "the outputs it actually produces"],
    ["Restricted domain", "a cut-down input set, chosen so an inverse exists"],
  ],
  appearsTitle: "WHERE THIS APPEARS IN THE TWO PAPERS",
  appearsNote: "so you know what you are preparing for",
  appears: [
    ["SAAT — how it is asked", "As 'find f⁻¹', as 'which graph is the inverse', and as a "
     + "composition that quietly cancels."],
    ["SAAT — the cancelling trick", "Heavy-looking algebra collapses to x because the two "
     + "functions are inverses. Spot it and the item takes ten seconds."],
    ["SAT — Advanced Math", "About 35% of the paper: equivalent expressions and nonlinear "
     + "functions, usually with a domain restriction attached."],
    ["Both — the domain", "The inverse's domain is the original's RANGE, and that swap is "
     + "what most of the wrong options are built from."],
  ],
  notesSub: "Three ideas. The third is the one that decides most of the marks, and it is not "
          + "about algebra at all.",
  keys: [
    { head: "The check is composition, not the graph", eq: "p4_check",
      body: "Unsure whether you have the inverse? Put one into the other. If the answer is x "
          + "— both ways round — you are right. No graph needed." },
    { head: "Swapping x and y swaps domain and range", eq: "p4_dom",
      body: "Whatever the original could take in, the inverse gives out. So the moment you "
          + "have the rule, write the two intervals down; the question usually wants them." },
    { head: "An inverse exists only if nothing repeats an output",
      body: "y = x² sends 3 and −3 to the same place, so it has no inverse until the domain "
          + "is cut to x ≥ 0 — which is why the square root is defined the way it is." },
  ],
  misconception:
    "f⁻¹(x) is NOT 1/f(x). The −1 is not an exponent here; it names the undoing function, and "
    + "the reciprocal is the commonest error in this topic on both papers. Two slips travel "
    + "with it: solving for y before swapping rather than after, and inverting a square "
    + "without restricting the domain.",
  warmup: [
    { q: "Find the inverse.", eq: "q4_g11a" },
    { q: "Find the inverse.", eq: "q4_g11b" },
    { q: "Find the value.", eq: "q4_g11c" },
    { q: "State the domain of the inverse.", eq: "q4_g11d" },
    { q: "Evaluate.", eq: "q4_g11e" },
    { q: "Without any algebra, what is f⁻¹(f(7))?" },
  ],
  routes: [
    "Questions 1 and 2 — swap and solve. Then check each answer by composing, both ways round.",
    "Questions 3 and 5 — a value rather than a rule. Decide what is being undone before you "
      + "write anything.",
    "Questions 4 and 6: say why the answer to 6 needs no working at all, and what that tells "
      + "you about question 4.",
  ],
  doneWhen: "you can find an inverse by swapping and solving, check it by composing, and state "
    + "the inverse's domain without being asked twice.",
  answers: "1) (x − 2)/5   2) 4x + 7   3) 1   4) x ≥ 0   5) 9   6) 7",
});

// =====================================================================
// GRADE 9 · MAWHIBA · Week 4 — Unit 1 Linear equations, Activity 3
// Number Pyramids. Not an exam class: the sheet names the unit and the
// six Mawhiba values instead of exam codes, per the Student Book.
// =====================================================================
build({
  who: "Grade 9 Mawhiba",
  week: "Week 4",
  out: "PreSession_Gr9_Mawhiba_W4.docx",
  headerLine: "Grade 9 · Mawhiba · Week 4 · read this BEFORE the session",
  title: "Pre-Session Skills Sheet — Number Pyramids",
  sub: "Classes 9A and 9B · Unit 1 Linear equations, Activity 3. Bring a pencil you are "
     + "willing to rub out — this activity is built to be got wrong first.",
  covers: [
    ["Unit 1 · Activity 3", "Number Pyramids — building and solving linear expressions"],
    ["Inquiry", "you will be asked what happens IF, before you are told what does"],
    ["Perseverance", "the first pyramid you try to fill from the top will not work"],
  ],
  priors: [
    { skill: "Add two expressions and collect like terms", eq: "p4_like",
      note: "Only terms with the same letter combine. The numbers stay separate." },
    { skill: "Solve a one-unknown linear equation", eq: "p4_solve",
      note: "Undo in the reverse order: the addition first, then the multiplication." },
    { skill: "Read a pyramid — each brick is the sum of the two below it", eq: "p4_pyr", k: 0.58,
      note: "Work upward and every brick is forced. There is nothing to choose." },
    { skill: "Do the same with letters instead of numbers", eq: "p4_pyralg", k: 0.58,
      note: "The middle letter appears twice at the top. Notice it; the whole activity turns "
          + "on that." },
  ],
  vocab: [
    ["Expression", "letters and numbers with no equals sign"],
    ["Equation", "two expressions set equal — it can be solved"],
    ["Like terms", "terms with exactly the same letter part"],
    ["Coefficient", "the number multiplying a letter"],
    ["Substitute", "put a number in place of a letter"],
    ["Generalise", "say what is true for every case, not just yours"],
  ],
  appearsTitle: "WHY THIS ACTIVITY IS IN THE COURSE",
  appearsNote: "Mawhiba is not extra homework — it is a different way of working",
  appears: [
    ["It goes both ways", "Upward is arithmetic. Downward from a known top is algebra, "
     + "because you have to name the unknown and solve."],
    ["The pattern is the point", "a + 2b + c is not a fact to memorise — you will find it, "
     + "then be asked why the middle one is doubled."],
    ["It scales", "Four bricks give 1, 3, 3, 1; five give 1, 4, 6, 4, 1. Those numbers "
     + "return in Unit 6."],
    ["You will be asked to justify", "Assessed against inquiry, risk taking, creativity, "
     + "perseverance, collaboration and concern for society."],
  ],
  notesSub: "Three ideas. Read them, then try the six — but try them before you decide whether "
          + "you understood the ideas.",
  keys: [
    { head: "Upward is forced; downward is a choice you have to justify", eq: "p4_pyr", k: 0.46,
      body: "Given the bottom row there is exactly one pyramid. Given the top there are many, "
          + "so the question must tell you something else — finding it is half the task." },
    { head: "The middle brick counts twice", eq: "p4_pyralg", k: 0.46,
      body: "The middle brick feeds both bricks above it, so the top is a + 2b + c. Change "
          + "the middle by one and the top changes by two — test it before you believe it." },
    { head: "Name the unknown, then write what the pyramid says",
      body: "If the top is known and a bottom brick is missing, call it x, build the top in "
          + "terms of x, and set it equal to the number given. The pyramid writes the "
          + "equation; you only solve it." },
  ],
  misconception:
    "Filling a pyramid downward by splitting each brick in half. It works for the first row "
    + "then fails, because the middle brick serves two bricks above it at once. Getting stuck "
    + "there is not a mistake — it is why the activity needs algebra.",
  warmup: [
    { q: "Fill it in, working upward.", eq: "q4_g9a", k: 0.58 },
    { q: "Fill in the three missing bricks.", eq: "q4_g9b", k: 0.58 },
    { q: "What is the top brick?", eq: "q4_g9c" },
    { q: "What is the top brick?", eq: "q4_g9d" },
    { q: "Find x.", eq: "q4_g9e" },
    { q: "Can two different bottom rows give the same top brick? Show one pair, or say why not." },
  ],
  routes: [
    "Questions 1 and 2 — build upward, then use the top to fill what is missing. Check by "
      + "rebuilding the pyramid from your answer.",
    "Questions 3 and 5 — one letter only. Write the top in terms of the letter before you "
      + "put any number in.",
    "Questions 4 and 6: prove the a + 2b + c rule with a pyramid of your own, then answer 6 "
      + "with an example, not an opinion.",
  ],
  doneWhen: "you can build a pyramid upward, write the top brick in letters, and use it to "
    + "find a missing number at the bottom.",
  answers: "1) 8, 12 → 20   2) middle 13, 17; bottom 4, 9, 8   3) 4n   4) a + 2b + c   "
    + "5) x = 9   6) yes — 1, 5, 1 and 3, 3, 3 both give 12",
});

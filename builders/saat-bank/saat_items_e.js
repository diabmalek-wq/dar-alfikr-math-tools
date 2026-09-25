// PART E of the SAAT booklet.
//
// Two things live here that could not live anywhere else.
//
// 1. REASONING AND LOGIC. Tahsili examines truth values, negation, the
//    conditional and its converse, inverse and contrapositive, the
//    biconditional, the syllogism and the counterexample. The department's
//    45-week course has no session with that name, so under the old plan-only
//    rule the bank refused the topic outright. The booklet no longer prints
//    sessions, so the topic is written here where it belongs — at the front.
//
// 2. THE SKILLS THE BANK HAD NOT REACHED. Twenty-three topic areas of the
//    syllabus held no item: solids, exponential and logarithmic applications,
//    complex roots, special triangles, trigonometric graphs, proving
//    identities, identifying and applying conics, the chain rule, the
//    derivatives of the transcendental functions, implicit differentiation,
//    curve sketching, optimisation, related rates, motion, antiderivatives,
//    the integration rules, substitution, the properties of the definite
//    integral and area between curves. Two items each, written against the
//    objectives as the syllabus states them.
//
// Every answer is re-derived independently in verify_saat_e.py.

module.exports = [
  // ================================================= REASONING AND LOGIC
  {
    sig: "truth-value-of-a-conjunction",
    code: "SAAT-M-ALG.98", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "p is the statement \"a rectangle is a quadrilateral\" and q is the statement \"a rectangle has four right angles\". What is the truth value of p ∧ q, and of ~p ∨ q?",
    opts: [
      "p ∧ q is true, and ~p ∨ q is true",
      "p ∧ q is true, and ~p ∨ q is false",
      "p ∧ q is false, and ~p ∨ q is true",
      "Both are false"
    ],
    ans: 0,
    trick: "AND needs every part true, OR needs only one — and ~p is FALSE here, so the second statement is carried entirely by q; a false first half never sinks an OR",
    why: "p is true and q is true, so p ∧ q is true; ~p is false but q is true, so ~p ∨ q is true.",
    traps: [
      "B: ~p taken to decide the disjunction on its own.",
      "C: the conjunction read as needing only one true part.",
      "D: p judged false because not every quadrilateral is a rectangle.",
    ],
  },
  {
    sig: "negation-of-a-statement",
    code: "SAAT-M-ALG.99", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "The statement \"every prime number is odd\" is false. What is its negation, and what is the negation's truth value?",
    opts: [
      "\"Some prime number is odd\", which is true",
      "\"Some prime number is not odd\", which is true",
      "\"Every prime number is even\", which is false",
      "\"No prime number is odd\", which is false"
    ],
    ans: 1,
    trick: "the negation of EVERY is SOME … NOT, never EVERY … NOT — and the negation of a false statement is always true, which is the check that catches three of these at once",
    why: "The negation of a universal claim is an existential denial; 2 is prime and not odd, so it is true.",
    traps: [
      "A: a statement that is true but does not contradict the original.",
      "C: every replaced by every, which is a different claim, not a negation.",
      "D: the negation over-stated as a universal denial.",
    ],
  },
  {
    sig: "when-a-conditional-is-false",
    code: "SAAT-M-ALG.100", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "In which case only is the conditional p → q false?",
    opts: [
      "p false and q false",
      "Whenever p and q differ",
      "p true and q false",
      "p false and q true"
    ],
    ans: 2,
    trick: "a conditional promises nothing when the hypothesis fails, so a FALSE p makes the whole statement true — the single false row is true hypothesis, false conclusion, and no other",
    why: "p → q is false exactly when the hypothesis holds and the conclusion does not.",
    traps: [
      "A: also vacuously true.",
      "B: two of the three differing cases are true.",
      "D: a false hypothesis makes the conditional vacuously true.",
    ],
  },
  {
    sig: "converse-of-a-conditional",
    code: "SAAT-M-ALG.101", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "What is the converse of \"if a figure is a square, then it is a rectangle\"?",
    opts: [
      "If a figure is not a square, then it is not a rectangle",
      "If a figure is not a rectangle, then it is not a square",
      "A figure is a square if and only if it is a rectangle",
      "If a figure is a rectangle, then it is a square"
    ],
    ans: 3,
    trick: "the CONVERSE swaps the two parts and negates neither — the inverse negates both without swapping, and the contrapositive does both, so all three are on this page",
    why: "The converse of p → q is q → p.",
    traps: [
      "A: the inverse, which negates both parts in place.",
      "B: the contrapositive, which swaps and negates.",
      "C: the biconditional, which claims both directions at once.",
    ],
  },
  {
    sig: "contrapositive-and-equivalence",
    code: "SAAT-M-ALG.102", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "Which pair of statements always have the same truth value?",
    opts: [
      "A conditional and its contrapositive",
      "A conditional and its converse",
      "A conditional and its inverse",
      "A converse and a contrapositive"
    ],
    ans: 0,
    trick: "only the CONTRAPOSITIVE is logically equivalent to the conditional — the converse and the inverse are equivalent to EACH OTHER, and to neither of the first two",
    why: "p → q and ~q → ~p have identical truth tables.",
    traps: [
      "B: \"squares are rectangles\" is true, its converse is not.",
      "C: the inverse matches the converse, not the conditional.",
      "D: these are the two that are not equivalent to the original.",
    ],
  },
  {
    sig: "biconditional-truth-value",
    code: "SAAT-M-ALG.103", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "When is the biconditional p ↔ q true?",
    opts: [
      "Whenever at least one of them is true",
      "Exactly when p and q have the same truth value",
      "Only when both are true",
      "Only when both are false"
    ],
    ans: 1,
    trick: "a biconditional is an AND of the two conditionals, so it survives BOTH true and BOTH false — reading it as an ordinary conjunction loses the second of those rows",
    why: "p ↔ q is true when p and q are both true and when they are both false.",
    traps: [
      "A: that is the disjunction, not the biconditional.",
      "C: the both-false row also makes it true.",
      "D: the both-true row also makes it true.",
    ],
  },
  {
    sig: "law-of-syllogism",
    code: "SAAT-M-ALG.104", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "Given that \"if I find work, I will earn money\" and \"if I earn money, I can buy a car\" are both true, what follows?",
    opts: [
      "If I do not find work, I cannot buy a car",
      "Nothing follows without a third statement",
      "If I find work, I can buy a car",
      "If I can buy a car, I found work"
    ],
    ans: 2,
    trick: "the syllogism chains p → q with q → r to give p → r, and only in that direction — reading the chain backwards gives the converse, which does not follow",
    why: "p → q and q → r together give p → r.",
    traps: [
      "A: the inverse of the conclusion.",
      "B: the two conditionals are enough.",
      "D: the converse of the conclusion.",
    ],
  },
  {
    sig: "inductive-conjecture-next-term",
    code: "SAAT-M-ALG.105", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "Write the conjecture that describes the pattern 10, 4, −2, −8, … and give the next term.",
    opts: [
      "Each term is 6 less than the one before it; the next term is −2",
      "Each term is half the one before it; the next term is −4",
      "Each term is 6 more than the one before it; the next term is −2",
      "Each term is 6 less than the one before it; the next term is −14"
    ],
    ans: 3,
    trick: "state the rule and APPLY it — a conjecture that describes the pattern correctly but is then applied to the wrong term is the option sitting beside the answer",
    why: "The difference is −6 throughout, so the next term is −8 − 6 = −14.",
    traps: [
      "A: the rule right, the subtraction applied to the wrong term.",
      "B: the pattern read as a ratio.",
      "C: the direction of the change reversed.",
    ],
  },
  {
    sig: "counterexample-to-a-prime-claim",
    code: "SAAT-M-ALG.106", unit: 0, topic: "Statements, truth values & reasoning", lvl: 3,
    stem: "A student claims that n² + n + 11 is prime for every whole number n. Which value of n disproves the claim?",
    opts: [
      "11",
      "3",
      "5",
      "7"
    ],
    ans: 0,
    trick: "one counterexample kills a general claim, and the small cases here all WORK — the value that breaks it is the one that makes every term share a factor",
    why: "At n = 11: 121 + 11 + 11 = 143 = 11 × 13, which is not prime.",
    traps: [
      "B: 9 + 3 + 11 = 23, prime.",
      "C: 25 + 5 + 11 = 41, prime.",
      "D: 49 + 7 + 11 = 67, prime.",
    ],
  },
  {
    sig: "counterexample-is-enough",
    code: "SAAT-M-ALG.107", unit: 0, topic: "Statements, truth values & reasoning", lvl: 2,
    stem: "How many counterexamples are needed to prove that a general statement is false?",
    opts: [
      "A counterexample cannot disprove a statement",
      "One",
      "At least three",
      "As many as there are cases"
    ],
    ans: 1,
    trick: "a general claim says EVERY case works, so a single failure is a complete refutation — but the reverse is not true, and no number of successful cases ever proves one",
    why: "A universal claim is false as soon as one instance fails.",
    traps: [
      "A: that is exactly what a counterexample does.",
      "C: no threshold applies; one is a proof of falsity.",
      "D: checking every case is a proof of truth, not of falsity.",
    ],
  },

  // ================================================= UNIT 4 · solids
  {
    sig: "volume-of-a-cone",
    code: "SAAT-M-GEO.63", ses: 35, lvl: 3,
    stem: "A cone has radius 6 cm and height 8 cm. Taking π ≈ 3.14, what are its volume and its slant height?",
    opts: [
      "Volume 301.44 cm³, slant height 14 cm",
      "Volume 150.72 cm³, slant height 10 cm",
      "Volume 301.44 cm³, slant height 10 cm",
      "Volume 904.32 cm³, slant height 10 cm"
    ],
    ans: 2,
    trick: "a cone is ONE THIRD of the cylinder around it, and the slant height comes from Pythagoras on the radius and the height — adding the two lengths instead is the other half of the error",
    why: "V = (1/3)(3.14)(36)(8) = 301.44; slant = √(36 + 64) = 10.",
    traps: [
      "A: the radius and the height added for the slant height.",
      "B: a sixth taken instead of a third.",
      "D: the cylinder's volume given, with no third taken.",
    ],
  },
  {
    sig: "effect-of-scaling-on-volume",
    code: "SAAT-M-GEO.64", ses: 35, lvl: 3,
    stem: "Every length of a solid is multiplied by 3. By what factor is its volume multiplied?",
    opts: [
      "3",
      "9",
      "6",
      "27"
    ],
    ans: 3,
    trick: "lengths scale by k, areas by k SQUARED and volumes by k CUBED — the square is the answer to a different question and is always offered here",
    why: "3³ = 27.",
    traps: [
      "A: the length factor repeated.",
      "B: the area factor given.",
      "C: the factor multiplied by the number of dimensions.",
    ],
  },

  // ================================================= UNIT 6 · exp and log
  {
    sig: "inverse-of-a-logarithmic-function",
    code: "SAAT-M-ALG.108", ses: 52, lvl: 3,
    stem: "What is the inverse of f(x) = log₅ x?",
    opts: [
      { eq: "e_ilog1" },
      { eq: "e_ilog2" },
      { eq: "e_ilog3" },
      { eq: "e_ilog4" }
    ],
    ans: 0,
    trick: "the exponential and the logarithm to the SAME base undo each other — the inverse is not the reciprocal of the logarithm and not a logarithm to the reciprocal base",
    why: "y = log₅ x gives x = log₅ y, so y = 5ˣ.",
    traps: [
      "B: the reciprocal taken instead of the inverse.",
      "C: the base inverted.",
      "D: the base and the argument interchanged.",
    ],
  },
  {
    sig: "composition-of-exponential-and-log",
    code: "SAAT-M-ALG.109", ses: 52, lvl: 3,
    stem: "Simplify the expression below, given that x > 0.",
    stemEq: "e_comp",
    opts: [
      { eq: "e_comp4" },
      { eq: "e_comp1" },
      { eq: "e_comp2" },
      { eq: "e_comp3" }
    ],
    ans: 1,
    trick: "a base raised to a logarithm of the SAME base returns the argument untouched — the 4 in the exponent multiplies the logarithm, so it becomes a POWER of x, not a multiple of it",
    why: "2^(4 log₂ x) = 2^(log₂ x⁴) = x⁴.",
    traps: [
      "A: the 4 taken as a base.",
      "C: the 4 read as a multiplier of x.",
      "D: the composition read as cancelling to x alone.",
    ],
  },
  {
    sig: "compound-interest-in-sar",
    code: "SAAT-M-ALG.110", ses: 53, lvl: 4,
    stem: "A deposit of 20 000 SAR earns 5% a year, compounded annually. Which expression gives its value after t years?",
    opts: [
      { eq: "e_ci3" },
      { eq: "e_ci4" },
      { eq: "e_ci1" },
      { eq: "e_ci2" }
    ],
    ans: 2,
    trick: "the growth factor is 1 PLUS the rate, not the rate alone — a factor of 0.05 would destroy the deposit rather than grow it, and a factor of 5 would multiply it fivefold each year",
    why: "A = 20000(1.05)ᵗ.",
    traps: [
      "A: the interest added once rather than compounded.",
      "B: the percentage read as a whole number.",
      "D: the rate used as the factor, which shrinks the deposit.",
    ],
  },
  {
    sig: "half-life-remaining-amount",
    code: "SAAT-M-ALG.111", ses: 53, lvl: 3,
    stem: "A substance has a half-life of 6 years. What fraction of a sample remains after 24 years?",
    opts: [
      "1/4",
      "1/8",
      "1/24",
      "1/16"
    ],
    ans: 3,
    trick: "count the HALVINGS, not the years — 24 years is four half-lives, so the fraction is one half to the fourth power, and dividing 24 by 6 gives the exponent, never the answer",
    why: "24 ÷ 6 = 4 half-lives, so (1/2)⁴ = 1/16.",
    traps: [
      "A: the number of half-lives read as the denominator.",
      "B: three halvings counted.",
      "C: the years used directly in the denominator.",
    ],
  },

  // ================================================= UNIT 7 · complex roots
  {
    sig: "least-degree-from-complex-zeros",
    code: "SAAT-M-ALG.112", ses: 62, lvl: 4,
    stem: "A polynomial with real coefficients has zeros 2, 3 + i and 1 − 4i. What is its least possible degree?",
    opts: [
      "5",
      "3",
      "6",
      "4"
    ],
    ans: 0,
    trick: "with REAL coefficients every complex zero drags its conjugate along, so two complex zeros are really four — counting the zeros as listed is the error the second option rewards",
    why: "The conjugates 3 − i and 1 + 4i must also be zeros, giving five in all.",
    traps: [
      "B: the three zeros counted as given.",
      "C: a conjugate counted for the real zero as well.",
      "D: one conjugate added, not both.",
    ],
  },
  {
    sig: "imaginary-roots-of-a-quartic",
    code: "SAAT-M-ALG.113", ses: 62, lvl: 4,
    stem: "How many of the four roots of x⁴ − 16 = 0 are imaginary?",
    opts: [
      "1",
      "2",
      "4",
      "0"
    ],
    ans: 1,
    trick: "factor as a difference of squares TWICE — the first factor gives two real roots and the second, a sum of squares, gives the conjugate imaginary pair",
    why: "x⁴ − 16 = (x² − 4)(x² + 4) gives x = ±2 and x = ±2i.",
    traps: [
      "A: only one member of the conjugate pair counted.",
      "C: every root assumed imaginary because the degree is even.",
      "D: the sum-of-squares factor overlooked.",
    ],
  },

  // ================================================= UNIT 8 · trigonometry I
  {
    sig: "side-in-a-30-60-90-triangle",
    code: "SAAT-M-TRI.24", ses: 66, lvl: 2,
    stem: "In a triangle with angles 30°, 60° and 90° the shortest side measures 5. What are the other two sides?",
    opts: [
      { eq: "e_sp3" },
      { eq: "e_sp4" },
      { eq: "e_sp1" },
      { eq: "e_sp2" }
    ],
    ans: 2,
    trick: "the sides run 1 : √3 : 2 with the SHORTEST opposite the 30° angle — the √3 belongs to the middle side, and putting it on the hypotenuse is the standard slip",
    why: "The sides are 5, 5√3 and 10.",
    traps: [
      "A: the shortest side taken to be opposite the 60° angle.",
      "B: the hypotenuse taken as three times the short side.",
      "D: the ratios of the 45-45-90 triangle used.",
    ],
  },
  {
    sig: "exact-value-from-special-angles",
    code: "SAAT-M-TRI.25", ses: 66, lvl: 3,
    stem: "Find the exact value of the expression below.",
    stemEq: "e_exv",
    opts: [
      { eq: "e_exv2" },
      { eq: "e_exv3" },
      { eq: "e_exv4" },
      { eq: "e_exv1" }
    ],
    ans: 3,
    trick: "sin 30° is one half and cos 60° is also one half — the two are equal, so the difference of their squares is zero, and any option that is not zero has confused one of them with a √3 value",
    why: "sin²30° − cos²60° = 1/4 − 1/4 = 0.",
    traps: [
      "A: cos 60° read as √3 ÷ 2.",
      "B: sin 30° read as √3 ÷ 2.",
      "C: only the first term evaluated.",
    ],
  },
  {
    sig: "range-of-the-tangent-graph",
    code: "SAAT-M-TRI.26", ses: 70, lvl: 2,
    stem: "Which statement about the graph of y = tan x is correct?",
    opts: [
      "Its range is all real numbers and it has vertical asymptotes",
      "Its range is from −1 to 1 and it has no asymptotes",
      "Its range is all real numbers and it has a horizontal asymptote",
      "Its range is from −1 to 1 and it has vertical asymptotes"
    ],
    ans: 0,
    trick: "the tangent is a QUOTIENT, so it runs to infinity wherever its denominator vanishes — the range −1 to 1 belongs to the sine and cosine, which have no asymptotes at all",
    why: "tan x = sin x ÷ cos x is unbounded, with vertical asymptotes where cos x = 0.",
    traps: [
      "B: the sine and cosine range attached to the tangent.",
      "C: a horizontal asymptote would bound the function.",
      "D: the right asymptotes with the wrong range.",
    ],
  },
  {
    sig: "zeros-of-the-cosine-graph",
    code: "SAAT-M-TRI.27", ses: 70, lvl: 2,
    stem: "Where does the graph of y = cos x meet the x-axis between 0° and 360°?",
    opts: [
      "At 180° only",
      "At 90° and 270°",
      "At 0° and 180°",
      "At 0°, 180° and 360°"
    ],
    ans: 1,
    trick: "the cosine is ZERO where the sine is at its extremes, and the other way round — reading the cosine's zeros off the sine's graph is exactly the confusion the second option is built from",
    why: "cos 90° = 0 and cos 270° = 0, and the cosine is non-zero elsewhere in the interval.",
    traps: [
      "A: the cosine at 180° is −1, not 0.",
      "C: the sine's zeros given.",
      "D: the sine's zeros with the endpoint added.",
    ],
  },
  {
    sig: "amplitude-and-period-of-a-sine",
    code: "SAAT-M-TRI.28", ses: 71, lvl: 3,
    stem: "For the function y = 4 sin(3x), what are the amplitude and the period in degrees?",
    opts: [
      "Amplitude 4, period 1080°",
      "Amplitude 4, period 360°",
      "Amplitude 4, period 120°",
      "Amplitude 3, period 120°"
    ],
    ans: 2,
    trick: "the number OUTSIDE sets the amplitude and the number INSIDE divides the period — multiplying by the inside number instead of dividing turns a squeezed graph into a stretched one",
    why: "Amplitude |4| = 4 and period 360 ÷ 3 = 120.",
    traps: [
      "A: the period multiplied by 3.",
      "B: the inside coefficient ignored.",
      "D: the two coefficients interchanged.",
    ],
  },
  {
    sig: "b-from-a-stated-period",
    code: "SAAT-M-TRI.29", ses: 71, lvl: 3,
    stem: "A cosine function has period 90°. What is the value of b in y = cos(bx)?",
    opts: [
      "90",
      "0.25",
      "270",
      "4"
    ],
    ans: 3,
    trick: "b = 360 ÷ period, so a SHORT period means a LARGE b — dividing the other way round gives a fraction, and the fraction is on the page",
    why: "360 ÷ 90 = 4.",
    traps: [
      "A: the period copied as b.",
      "B: the division taken the other way round.",
      "C: 360 − 90 taken.",
    ],
  },

  // ================================================= UNIT 9 · identities
  {
    sig: "which-identity-clears-the-mixed-terms",
    code: "SAAT-M-TRI.30", ses: 75, lvl: 3,
    stem: "To prove that sin⁴θ − cos⁴θ = sin²θ − cos²θ, what is the first useful step?",
    opts: [
      "Factor the left side as a difference of squares, then use sin²θ + cos²θ = 1",
      "Replace sin²θ by 1 + cos²θ",
      "Divide both sides by cos²θ",
      "Square both sides"
    ],
    ans: 0,
    trick: "work ONE side into the other and look for structure before reaching for an identity — the fourth powers here are a difference of squares, and the Pythagorean identity then removes the second factor entirely",
    why: "sin⁴θ − cos⁴θ = (sin²θ − cos²θ)(sin²θ + cos²θ) = sin²θ − cos²θ.",
    traps: [
      "B: the Pythagorean identity misquoted; it is 1 − cos²θ.",
      "C: dividing introduces a restriction and does not simplify.",
      "D: squaring an identity is never a proof of it.",
    ],
  },
  {
    sig: "not-an-identity-by-counterexample",
    code: "SAAT-M-TRI.31", ses: 75, lvl: 3,
    stem: "Which equation below is NOT an identity?",
    opts: [
      { eq: "e_ni4" },
      { eq: "e_ni1" },
      { eq: "e_ni2" },
      { eq: "e_ni3" }
    ],
    ans: 1,
    trick: "an identity must hold for EVERY admissible angle, so one substitution is enough to reject one — try 30° or 45°, where the sine and cosine are known exactly and are not equal",
    why: "At θ = 30°, sin θ + cos θ ≈ 1.366, not 1.",
    traps: [
      "A: the reciprocal identity for the secant.",
      "C: the Pythagorean identity, true for every θ.",
      "D: the definition of the tangent.",
    ],
  },

  // ================================================= UNIT 10 · conics
  {
    sig: "classify-a-conic-from-its-coefficients",
    code: "SAAT-M-GEO.65", ses: 86, lvl: 3,
    stem: "The equation 4x² − 9y² + 8x + 36y − 68 = 0 describes which conic?",
    opts: [
      "A parabola",
      "A circle",
      "A hyperbola",
      "An ellipse"
    ],
    ans: 2,
    trick: "read the two squared coefficients: OPPOSITE signs give a hyperbola, the same sign but unequal an ellipse, equal a circle, and one missing a parabola",
    why: "The coefficients of x² and y² are 4 and −9 — opposite in sign.",
    traps: [
      "A: a parabola has only one squared term.",
      "B: a circle needs the two coefficients equal.",
      "D: an ellipse needs both coefficients of the same sign.",
    ],
  },
  {
    sig: "ellipse-that-is-a-circle",
    code: "SAAT-M-GEO.66", ses: 86, lvl: 2,
    stem: "Under what condition does an ellipse become a circle?",
    opts: [
      "When a = 2b",
      "When c = a",
      "When the centre is at the origin",
      "When a = b, so the two foci coincide at the centre"
    ],
    ans: 3,
    trick: "a circle is the ellipse whose two axes are EQUAL — the foci then collapse onto the centre and the eccentricity falls to zero; where the centre sits has nothing to do with it",
    why: "If a = b then c² = a² − b² = 0, so both foci sit at the centre.",
    traps: [
      "A: that is an ordinary ellipse, twice as long as it is wide.",
      "B: c = a would flatten the ellipse to a segment.",
      "C: an ellipse anywhere may or may not be a circle.",
    ],
  },
  {
    sig: "focus-of-a-parabolic-dish",
    code: "SAAT-M-GEO.67", ses: 87, lvl: 4,
    stem: "A satellite dish in cross-section is the parabola x² = 16y, measured in centimetres from its vertex. How far from the vertex is the receiver placed?",
    opts: [
      "4 cm",
      "16 cm",
      "8 cm",
      "2 cm"
    ],
    ans: 0,
    trick: "the receiver sits at the FOCUS, and the standard form x² = 4cy makes 4c the number you can read off — the answer is a quarter of it, never the number itself",
    why: "4c = 16 gives c = 4.",
    traps: [
      "B: the coefficient read as the distance.",
      "C: the coefficient halved.",
      "D: the coefficient divided by 8.",
    ],
  },
  {
    sig: "width-of-an-elliptical-hall",
    code: "SAAT-M-GEO.68", ses: 87, lvl: 4,
    stem: "An elliptical hall is 40 m long and 24 m wide. How far from the centre is each focus?",
    opts: [
      "20 m",
      "16 m",
      "32 m",
      "8 m"
    ],
    ans: 1,
    trick: "the length and the width are the WHOLE axes, so a and b are their halves — using 40 and 24 as a and b makes the hall four times too big and gives an answer larger than the hall itself",
    why: "a = 20 and b = 12, so c = √(400 − 144) = 16.",
    traps: [
      "A: the semi-major axis given as the focal distance.",
      "C: the whole axes used as a and b.",
      "D: the difference of the semi-axes taken.",
    ],
  },
  {
    sig: "multi-step-slope-distance-midpoint",
    code: "SAAT-M-GEO.69", ses: 88, lvl: 4,
    stem: "A is (−6, 8) and B is (12, 0). M is the midpoint of AB. What is the distance from M to the origin?",
    opts: [
      "12",
      "6",
      "5",
      "10"
    ],
    ans: 2,
    trick: "two steps, and the first must finish before the second starts — find M, THEN measure; measuring from A or from B instead gives the two large options",
    why: "M = (3, 4), and √(9 + 16) = 5.",
    traps: [
      "A: the distance from the origin to B given.",
      "B: half the distance from the origin to B given.",
      "D: the distance from the origin to A given.",
    ],
  },
  {
    sig: "vertex-from-side-conditions",
    code: "SAAT-M-GEO.70", ses: 88, lvl: 4,
    stem: "Three vertices of a parallelogram are P(1, 2), Q(5, 2) and R(7, 6). What is the fourth vertex S, taken so that PQRS is the parallelogram in that order?",
    opts: [
      { eq: "e_vsc2" },
      { eq: "e_vsc3" },
      { eq: "e_vsc4" },
      { eq: "e_vsc1" }
    ],
    ans: 3,
    trick: "in PQRS the diagonals PR and QS bisect each other, so S = P + R − Q — writing the letters in a different order gives a different, and equally real, parallelogram, so the ORDER in the name is the whole question",
    why: "S = (1 + 7 − 5, 2 + 6 − 2) = (3, 6).",
    traps: [
      "A: S = Q + R − P used, which names a different vertex.",
      "B: the coordinates simply added.",
      "C: the translation applied from the wrong vertex.",
    ],
  },

  // ================================================= UNIT 11 · derivatives
  {
    sig: "derivative-of-a-power-of-a-function",
    code: "SAAT-M-CAL.19", ses: 96, lvl: 3,
    stem: "Differentiate the function below.",
    stemEq: "e_ch1",
    opts: [
      { eq: "e_ch1a" },
      { eq: "e_ch1b" },
      { eq: "e_ch1c" },
      { eq: "e_ch1d" }
    ],
    ans: 0,
    trick: "bring the power down, drop it by one, and then MULTIPLY BY THE DERIVATIVE OF THE INSIDE — leaving that last factor off is the single most common error in the whole of differentiation",
    why: "y = (3x² + 5)⁴ gives y′ = 4(3x² + 5)³ · 6x = 24x(3x² + 5)³.",
    traps: [
      "B: the inside derivative left off.",
      "C: the power not reduced.",
      "D: the inside differentiated and the outside left alone.",
    ],
  },
  {
    sig: "derivative-of-a-radical-of-a-function",
    code: "SAAT-M-CAL.20", ses: 96, lvl: 4,
    stem: "Differentiate the function below.",
    stemEq: "e_ch2",
    opts: [
      { eq: "e_ch2d" },
      { eq: "e_ch2a" },
      { eq: "e_ch2b" },
      { eq: "e_ch2c" }
    ],
    ans: 1,
    trick: "rewrite the root as a power of one half FIRST — the derivative of √u is u′ over 2√u, and the 2 in that denominator is what the careless answer is missing",
    why: "y = √(x² + 9) gives y′ = 2x ÷ (2√(x² + 9)) = x ÷ √(x² + 9).",
    traps: [
      "A: the root differentiated as if the inside were x.",
      "C: the 2 in the denominator lost.",
      "D: the inside derivative left off.",
    ],
  },
  {
    sig: "derivative-of-sine-with-the-chain-rule",
    code: "SAAT-M-CAL.21", ses: 97, lvl: 3,
    stem: "Differentiate the function below.",
    stemEq: "e_tr1",
    opts: [
      { eq: "e_tr1c" },
      { eq: "e_tr1d" },
      { eq: "e_tr1a" },
      { eq: "e_tr1b" }
    ],
    ans: 2,
    trick: "the derivative of sine is cosine, with NO sign change — the minus belongs to the derivative of the cosine, and the inside coefficient still has to come out in front",
    why: "y = sin(5x) gives y′ = 5 cos(5x).",
    traps: [
      "A: the inside coefficient left off.",
      "B: the sine kept instead of the cosine.",
      "D: the sign of the cosine's derivative borrowed.",
    ],
  },
  {
    sig: "derivative-of-a-natural-logarithm",
    code: "SAAT-M-CAL.22", ses: 97, lvl: 3,
    stem: "Differentiate the function below.",
    stemEq: "e_tr2",
    opts: [
      { eq: "e_tr2b" },
      { eq: "e_tr2c" },
      { eq: "e_tr2d" },
      { eq: "e_tr2a" }
    ],
    ans: 3,
    trick: "the derivative of ln u is u′ OVER u — the inside function goes underneath, and its derivative goes on top; writing 1 over the inside alone forgets the chain rule",
    why: "y = ln(x³ + 2) gives y′ = 3x² ÷ (x³ + 2).",
    traps: [
      "A: the inside derivative left off the numerator.",
      "B: the logarithm differentiated as a power.",
      "C: the numerator and the denominator interchanged.",
    ],
  },
  {
    sig: "implicit-differentiation-dy-dx",
    code: "SAAT-M-CAL.23", ses: 98, lvl: 4,
    stem: "For the circle x² + y² = 25, what is dy/dx?",
    opts: [
      { eq: "e_im1" },
      { eq: "e_im2" },
      { eq: "e_im3" },
      { eq: "e_im4" }
    ],
    ans: 0,
    trick: "every y differentiated brings a dy/dx with it — collecting those terms and dividing is the whole method, and treating y as a constant is what leaves the answer with no y in it",
    why: "2x + 2y·y′ = 0 gives y′ = −x ÷ y.",
    traps: [
      "B: the sign lost when the x term was moved across.",
      "C: y treated as a constant.",
      "D: the reciprocal taken.",
    ],
  },
  {
    sig: "slope-of-an-implicit-tangent",
    code: "SAAT-M-CAL.24", ses: 98, lvl: 4,
    stem: "What is the slope of the tangent to x² + y² = 25 at the point (3, 4)?",
    opts: [
      "1.33",
      "−0.75",
      "0.75",
      "−1.33"
    ],
    ans: 1,
    trick: "differentiate first and substitute AFTERWARDS — the tangent to a circle is perpendicular to the radius, so its slope is the negative reciprocal of 4/3, and a positive answer at a point in the first quadrant is wrong on sight",
    why: "y′ = −x/y = −3/4 = −0.75.",
    traps: [
      "A: both errors together.",
      "C: the sign dropped.",
      "D: the fraction inverted.",
    ],
  },

  // ================================================= UNIT 12 · applications
  {
    sig: "match-a-function-to-its-graph",
    code: "SAAT-M-CAL.25", ses: 104, lvl: 4,
    stem: "A function has f′(x) > 0 and f″(x) < 0 on an interval. What does its graph do there?",
    opts: [
      "It falls while bending downwards",
      "It falls while bending upwards",
      "It rises while bending downwards",
      "It rises while bending upwards"
    ],
    ans: 2,
    trick: "the FIRST derivative gives the direction and the SECOND gives the bend — they are independent, so a rising curve may bend either way, and reading a negative second derivative as \"falling\" is the error",
    why: "A positive first derivative means increasing; a negative second derivative means concave down.",
    traps: [
      "A: the second derivative read as the direction.",
      "B: both signs read as the direction.",
      "D: the sign of the second derivative read as positive.",
    ],
  },
  {
    sig: "curve-from-stated-conditions",
    code: "SAAT-M-CAL.26", ses: 104, lvl: 4,
    stem: "A curve has f′(2) = 0 and f″(2) > 0. What happens at x = 2?",
    opts: [
      "A local maximum",
      "A point of inflection",
      "Nothing can be decided",
      "A local minimum"
    ],
    ans: 3,
    trick: "a POSITIVE second derivative is the bowl, so a stationary point inside it is a minimum — the mnemonic that a positive number means a maximum is the trap the paper is built on",
    why: "The second derivative test: f′ = 0 with f″ > 0 marks a local minimum.",
    traps: [
      "A: the sign of the test reversed.",
      "B: an inflection needs the second derivative to change sign.",
      "C: the test decides it.",
    ],
  },
  {
    sig: "maximum-area-for-a-fixed-perimeter",
    code: "SAAT-M-CAL.27", ses: 105, lvl: 4,
    stem: "A rectangular plot is to be fenced with 80 m of fencing. What is the largest area it can enclose?",
    opts: [
      "400 m²",
      "1600 m²",
      "375 m²",
      "800 m²"
    ],
    ans: 0,
    trick: "80 m is the PERIMETER, so the two dimensions add to 40, not to 80 — the square that maximises the area is 20 by 20, and using 40 by 40 doubles both sides at once",
    why: "x + y = 40 and A = x(40 − x) is greatest at x = 20, giving 400.",
    traps: [
      "B: the perimeter used as the semi-perimeter.",
      "C: a 15 by 25 plot, close but not the maximum.",
      "D: the perimeter multiplied by the side.",
    ],
  },
  {
    sig: "maximum-volume-of-an-open-box",
    code: "SAAT-M-CAL.28", ses: 105, lvl: 4,
    stem: "Squares of side x are cut from the corners of a 12 cm by 12 cm sheet and the sides folded up. Which value of x gives the largest volume?",
    opts: [
      "4 cm",
      "2 cm",
      "3 cm",
      "6 cm"
    ],
    ans: 1,
    trick: "the base loses TWO x from each dimension, so the volume is x(12 − 2x)² — using (12 − x)² instead moves the maximum and gives an answer the box cannot even be folded into",
    why: "V′ = (12 − 2x)(12 − 6x) = 0 gives x = 2 inside the interval, and V(2) = 128.",
    traps: [
      "A: a third of the side taken.",
      "C: only one x subtracted from each dimension.",
      "D: half the side taken, which leaves no base at all.",
    ],
  },
  {
    sig: "related-rate-expanding-circle",
    code: "SAAT-M-CAL.29", ses: 106, lvl: 4,
    stem: "The radius of a circular oil slick grows at 3 cm per second. How fast is its area growing when the radius is 10 cm?",
    opts: [
      "100π cm²/s",
      "20π cm²/s",
      "60π cm²/s",
      "30π cm²/s"
    ],
    ans: 2,
    trick: "differentiate A = πr² with respect to TIME, which gives 2πr times dr/dt — substituting the radius into the area formula and calling that a rate skips the differentiation entirely",
    why: "dA/dt = 2π(10)(3) = 60π.",
    traps: [
      "A: the area itself given rather than its rate.",
      "B: the rate of change of the circumference given.",
      "D: the factor 2 left out.",
    ],
  },
  {
    sig: "related-rate-sliding-ladder",
    code: "SAAT-M-CAL.30", ses: 106, lvl: 4,
    stem: "A 13 m ladder leans against a wall. Its foot slides away at 2 m/s. How fast is the top sliding down when the foot is 5 m from the wall?",
    opts: [
      "2 m/s downwards",
      "6/5 m/s downwards",
      "24/5 m/s downwards",
      "5/6 m/s downwards"
    ],
    ans: 3,
    trick: "the LADDER is constant, so x² + y² = 169 differentiates to x·dx/dt + y·dy/dt = 0 — the height must be found from Pythagoras first, and here it is 12, not 13",
    why: "y = 12, so 5(2) + 12(dy/dt) = 0 and dy/dt = −10/12 = −5/6.",
    traps: [
      "A: the two rates assumed equal.",
      "B: the fraction inverted.",
      "C: the ladder length used in place of the height.",
    ],
  },
  {
    sig: "velocity-and-the-time-at-rest",
    code: "SAAT-M-CAL.31", ses: 107, lvl: 3,
    stem: "A particle's displacement is s(t) = t³ − 6t² + 9t metres, with t in seconds. At what times, in seconds, is it at rest?",
    opts: [
      "t = 1 and t = 3",
      "t = 0 and t = 3",
      "Only t = 2",
      "Only t = 3"
    ],
    ans: 0,
    trick: "at rest means the VELOCITY is zero, not the displacement — solving s(t) = 0 answers a different question, and its answers are on the page",
    why: "v = 3t² − 12t + 9 = 3(t − 1)(t − 3), zero at t = 1 and t = 3.",
    traps: [
      "B: s(t) = 0 solved instead of v(t) = 0.",
      "C: the acceleration set to zero.",
      "D: only one of the two roots kept.",
    ],
  },
  {
    sig: "maximum-height-of-a-projectile",
    code: "SAAT-M-CAL.32", ses: 107, lvl: 4,
    stem: "A ball is thrown so that its height is h(t) = −5t² + 20t + 1 metres. What is its greatest height?",
    opts: [
      "41 m",
      "21 m",
      "20 m",
      "2 m"
    ],
    ans: 1,
    trick: "the maximum is reached where the VELOCITY is zero, and the answer wanted is the HEIGHT at that moment, not the time — the time is 2 s and it is offered as an option",
    why: "h′ = −10t + 20 = 0 at t = 2, and h(2) = −20 + 40 + 1 = 21.",
    traps: [
      "A: the height doubled.",
      "C: the initial constant left out of h(2).",
      "D: the time of the maximum given instead of the height.",
    ],
  },

  // ================================================= UNIT 13 · integration
  {
    sig: "antiderivative-of-a-power",
    code: "SAAT-M-CAL.33", ses: 109, lvl: 2,
    stem: "Find the indefinite integral below.",
    stemEq: "e_ap",
    opts: [
      { eq: "e_ap3" },
      { eq: "e_ap4" },
      { eq: "e_ap1" },
      { eq: "e_ap2" }
    ],
    ans: 2,
    trick: "RAISE the power by one and divide by the NEW power, then add the constant — an antiderivative written without + C is not the general answer, and one of the options is exactly that",
    why: "∫6x² dx = 6x³/3 + C = 2x³ + C.",
    traps: [
      "A: the power rule for differentiation applied instead.",
      "B: divided by the old power.",
      "D: the constant of integration left off.",
    ],
  },
  {
    sig: "particular-antiderivative-through-a-point",
    code: "SAAT-M-CAL.34", ses: 109, lvl: 4,
    stem: "F′(x) = 4x − 3 and F(2) = 5. What is F(x)?",
    opts: [
      { eq: "e_pa2" },
      { eq: "e_pa3" },
      { eq: "e_pa4" },
      { eq: "e_pa1" }
    ],
    ans: 3,
    trick: "integrate first, THEN use the point to pin the constant — reading the 5 straight into the constant without substituting is what the wrong options are for",
    why: "F(x) = 2x² − 3x + C; F(2) = 8 − 6 + C = 5 gives C = 3.",
    traps: [
      "A: the 5 written in as the constant.",
      "B: the constant taken as zero.",
      "C: the sign of the constant reversed.",
    ],
  },
  {
    sig: "integral-of-a-sum",
    code: "SAAT-M-CAL.35", ses: 110, lvl: 2,
    stem: "Find the indefinite integral below.",
    stemEq: "e_is",
    opts: [
      { eq: "e_is1" },
      { eq: "e_is2" },
      { eq: "e_is3" },
      { eq: "e_is4" }
    ],
    ans: 0,
    trick: "integrate TERM BY TERM, and remember that the integral of a constant is that constant times x — a constant that survives unchanged into the answer has not been integrated at all",
    why: "∫(3x² − 4x + 7) dx = x³ − 2x² + 7x + C.",
    traps: [
      "B: the constant term carried through unintegrated.",
      "C: the middle term not halved.",
      "D: the terms differentiated instead.",
    ],
  },
  {
    sig: "integral-of-a-negative-power",
    code: "SAAT-M-CAL.36", ses: 110, lvl: 3,
    stem: "Find the indefinite integral below.",
    stemEq: "e_in",
    opts: [
      { eq: "e_in4" },
      { eq: "e_in1" },
      { eq: "e_in2" },
      { eq: "e_in3" }
    ],
    ans: 1,
    trick: "the power rule still applies to a NEGATIVE power — raising −3 by one gives −2, and dividing by −2 flips the sign; the rule fails only at the power −1, which is not this case",
    why: "∫x⁻³ dx = x⁻²/(−2) + C = −1/(2x²) + C.",
    traps: [
      "A: the power lowered instead of raised.",
      "C: the sign of the new power mishandled.",
      "D: the logarithm rule used, which belongs to x⁻¹.",
    ],
  },
  {
    sig: "choose-u-and-du",
    code: "SAAT-M-CAL.37", ses: 111, lvl: 3,
    stem: "For the integral of 2x(x² + 1)⁵ dx, what should u be, and what is du?",
    opts: [
      "u = (x² + 1)⁵ and du = 5(x² + 1)⁴ dx",
      "u = x and du = dx",
      "u = x² + 1 and du = 2x dx",
      "u = 2x and du = 2 dx"
    ],
    ans: 2,
    trick: "u is the INSIDE of the composition, and the rest of the integrand should turn out to be du — choosing the whole power as u leaves an integral harder than the one you started with",
    why: "With u = x² + 1, du = 2x dx and the integral becomes ∫u⁵ du.",
    traps: [
      "A: the whole power chosen as u.",
      "B: no substitution made at all.",
      "D: the outside factor chosen, leaving the bracket untouched.",
    ],
  },
  {
    sig: "integrate-a-power-times-its-derivative",
    code: "SAAT-M-CAL.38", ses: 111, lvl: 4,
    stem: "Find the indefinite integral below.",
    stemEq: "e_sub",
    opts: [
      { eq: "e_sub2" },
      { eq: "e_sub3" },
      { eq: "e_sub4" },
      { eq: "e_sub1" }
    ],
    ans: 3,
    trick: "after the substitution the integral is just u⁵, so the answer carries a SIXTH, not a fifth — and the 2x has been used up by du and must not reappear in the answer",
    why: "∫2x(x² + 1)⁵ dx = (x² + 1)⁶/6 + C.",
    traps: [
      "A: divided by 5 rather than by 6.",
      "B: the 2x left in the answer.",
      "C: the power not raised.",
    ],
  },
  {
    sig: "reverse-the-limits-of-an-integral",
    code: "SAAT-M-CAL.39", ses: 114, lvl: 3,
    stem: "The integral of f from 1 to 6 equals 14. What is the integral of f from 6 to 1, and the integral of f from 6 to 6?",
    opts: [
      "−14 and 0",
      "14 and 0",
      "−14 and 14",
      "0 and 0"
    ],
    ans: 0,
    trick: "reversing the limits reverses the SIGN, and an integral whose two limits are the same is zero whatever the function does — neither depends on knowing f",
    why: "Swapping the limits negates the integral; an integral over a single point is zero.",
    traps: [
      "B: the sign not reversed.",
      "C: the zero-width integral taken as the original value.",
      "D: both integrals taken as zero.",
    ],
  },
  {
    sig: "split-an-integral-at-an-interior-point",
    code: "SAAT-M-CAL.40", ses: 114, lvl: 3,
    stem: "The integral of f from 0 to 4 is 9, and from 0 to 7 is 20. What is the integral of f from 4 to 7?",
    opts: [
      "9",
      "11",
      "29",
      "−11"
    ],
    ans: 1,
    trick: "the whole is the sum of the parts, so the missing piece is the LARGE interval minus the small one — adding them instead is the error, and the sum is the option beside the answer",
    why: "20 − 9 = 11.",
    traps: [
      "A: the first integral copied.",
      "C: the two integrals added.",
      "D: the subtraction taken the wrong way round.",
    ],
  },
  {
    sig: "limits-from-the-intersections",
    code: "SAAT-M-CAL.41", ses: 116, lvl: 3,
    stem: "What are the limits of integration for the area between y = x² and y = x + 2?",
    opts: [
      "From −2 to 1",
      "From 0 to 4",
      "From −1 to 2",
      "From 0 to 2"
    ],
    ans: 2,
    trick: "the limits are the x values where the two curves MEET, found by setting them equal — the y values of the intersections, and the intercepts of either curve alone, are all offered here",
    why: "x² = x + 2 gives x² − x − 2 = 0, so x = −1 and x = 2.",
    traps: [
      "A: the signs of both roots reversed.",
      "B: the y values of the intersections used.",
      "D: only the positive root kept, with 0 assumed.",
    ],
  },
  {
    sig: "area-between-a-curve-and-a-line",
    code: "SAAT-M-CAL.42", ses: 116, lvl: 4,
    stem: "Find the area of the region enclosed between y = x² and y = x + 2.",
    opts: [
      "9",
      "2.25",
      "3",
      "4.5"
    ],
    ans: 3,
    trick: "integrate UPPER minus LOWER, and between the intersections the LINE is above the parabola — taking the parabola first gives the same number with a minus sign, and an area is never negative",
    why: "∫ from −1 to 2 of (x + 2 − x²) dx = 4.5.",
    traps: [
      "A: the area doubled.",
      "B: the area halved.",
      "C: the two curves integrated separately and subtracted at the endpoints only.",
    ],
  },
];

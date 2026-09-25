// PART L of the SAAT booklet — three items from the 17 September practice set.
//
// That source held 110 questions of which 96 were skills the bank already had.
// Of the twelve genuinely new candidates, Mr Thiab took the three that are real
// Tahsili traps rather than recall gaps:
//
//   · a logarithm whose BASE is a radical — the bank had radicals in the
//     ARGUMENT only, and the base case inverts the arithmetic
//   · a quotient whose divisor is PURE imaginary — the bank had the two-term
//     conjugate only, and multiplying by the conjugate here is wasted work
//   · the binomial mean and standard deviation — the bank had the normal
//     distribution but never np and the root of npq
//
// Same rule as every other part: skill and trick only. No stem, number set,
// option list or figure is reproduced. Every answer is re-derived independently
// in verify_saat_l.py.
module.exports = [
  {
    sig: "log-with-a-radical-base",
    code: "SAAT-M-ALG.3", unit: 6, topic: "Laws of logarithms", ses: 50, lvl: 3,
    stem: "Evaluate the expression below.",
    stemEq: "lx_log",
    opts: [{ eq: "lx_l1" }, { eq: "lx_l2" }, { eq: "lx_l3" }, { eq: "lx_l4" }],
    ans: 0,
    trick: "a radical BASE is a half power, so the exponent you want is DIVIDED by one half rather than multiplied by it — reading the base as 3 instead of √3 halves the answer, and it is the option the paper puts first",
    why: "√3 = 3^(1/2) and 9 = 3², so the exponent is 2 ÷ (1/2) = 4.",
    traps: [
      "B: the base read as 3 rather than √3.",
      "C: the exponent multiplied by the half instead of divided by it.",
      "D: the base's own exponent reported as the answer.",
    ],
  },
  {
    sig: "quotient-by-a-pure-imaginary",
    code: "SAAT-M-ALG.7", unit: 7, topic: "Complex numbers & operations", ses: 61, lvl: 3,
    stem: "Write the quotient below in the form a + bi.",
    stemEq: "lx_div",
    opts: [{ eq: "lx_d1" }, { eq: "lx_d2" }, { eq: "lx_d3" }, { eq: "lx_d4" }],
    ans: 0,
    optGrid: 2,
    trick: "when the divisor is PURE imaginary there is no two-term conjugate to form — multiplying top and bottom by i alone clears it, and the i² in the denominator turns the sign over one more time than students expect",
    why: "Multiplying above and below by i gives (5i + 2i²)/(3i²) = (5i − 2)/(−3) = 2/3 − (5/3)i.",
    traps: [
      "B: every sign reversed, from multiplying by −i instead of i.",
      "C: the real and imaginary parts divided by 3 separately, leaving the i where it was.",
      "D: the i² in the denominator taken as +1, so the imaginary sign never turns.",
    ],
  },
  {
    sig: "binomial-mean-and-standard-deviation",
    code: "SAAT-M-STA.2", unit: 5, topic: "Measures of dispersion & standard deviation",
    ses: 42, lvl: 3,
    stem: "A binomial experiment has the parameters below. What are its mean and standard deviation?",
    stemEq: "lx_bin",
    opts: [{ eq: "lx_b1" }, { eq: "lx_b2" }, { eq: "lx_b3" }, { eq: "lx_b4" }],
    ans: 0,
    optGrid: 2,
    trick: "npq is the VARIANCE, not the standard deviation — the square root is the step that gets dropped, and 16 sits in the options waiting for anyone who forgets it",
    why: "μ = np = 100(0.2) = 20, and σ = √(npq) = √(100 × 0.2 × 0.8) = √16 = 4.",
    traps: [
      "B: the variance npq reported as the standard deviation.",
      "C: the root taken of the mean rather than of npq.",
      "D: p itself reported as the mean.",
    ],
  },
];

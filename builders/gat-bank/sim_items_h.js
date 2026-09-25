// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part H: skills mined from Mr Tamer Elsawy's Part 1 set.
//
// The recording carried 25 distinct skills. EIGHTEEN of them the bank already
// had — clock angles, pictograms, bar-chart percentage change, pie sectors,
// primes, counting a range, people-and-days work rate, the 45° triangle, the
// parallel-line angle pair. Adding those again would have made the bank longer
// without making it better, and would have broken the one-item-per-skill rule
// the build enforces.
//
// The seven below are the ones that were genuinely missing. Three are algebra,
// which is exactly where the bank was thinnest — and two of those three are the
// same underlying move (equal fractions with 1 on top mean equal bottoms),
// asked at two difficulties, because that move appears on the real paper far
// more often than one item's worth.
//
// Nothing is transcribed. The skills are Mr Elsawy's to have collected; the
// wording, numbers and figures here are new, so this part stays part of the
// bank Mr Thiab may set and share freely.
// ---------------------------------------------------------------------------
module.exports = [

// ================================================================ GEOMETRY
{ sig: "rectilinear-perimeter", code: "GAT-Q-GEO.4", lvl: 3,
  stem: "The shape below is made of horizontal and vertical sides only. Find its perimeter, in centimetres.",
  fig: "h_stairs", figW: 1.85,
  opts: ["12", "18", "24", "36"], ans: 2,
  trick: "slide every step out to the enclosing rectangle — the horizontal pieces add to the full width and the vertical pieces to the full height, so no missing side ever needs to be found",
  why: "The horizontal sides total 2 × 7 = 14 cm and the vertical sides total 2 × 5 = 10 cm. The perimeter is 24 cm — the same as the 7 by 5 rectangle that encloses it.",
  traps: ["A: one width and one height added, 7 + 5.",
          "B: the three visible steps counted instead of the full width.",
          "D: the area of the enclosing rectangle given."] },

{ sig: "triangle-angles-from-ratio", code: "GAT-Q-GEO.1", lvl: 2,
  stem: "The three angles of a triangle are in the ratio 3 : 4 : 5. Find the largest angle.",
  opts: ["45°", "60°", "75°", "90°"], ans: 2,
  trick: "the parts share 180°, not 100° — divide 180 by the TOTAL number of parts before touching any option",
  why: "3 + 4 + 5 = 12 parts, so one part is 180 ÷ 12 = 15°. The largest angle is 5 × 15 = 75°.",
  traps: ["A: the smallest angle given.",
          "B: the middle angle given.",
          "D: a right angle assumed because 3 : 4 : 5 names a right triangle's SIDES — the trap this item exists for."] },

{ sig: "circle-area-to-square-area", code: "GAT-Q-GEO.4", lvl: 3,
  stem: "A circle of the area shown is drawn inside a square so that it touches all four sides. Find the area of the square, in square centimetres.",
  stemEq: "h_circ36",
  opts: ["36", "72", "144", "155"], ans: 2,
  trick: "run the chain the whole way — area to radius to DIAMETER to side. The side of the square is twice the radius, and stopping at the radius is where the mark goes",
  why: "πr² = 36π gives r = 6 cm. The circle touches all four sides, so the side of the square is the diameter, 12 cm, and the area is 12² = 144 cm².",
  traps: ["A: the circle's area copied as the square's.",
          "B: the area doubled instead of the radius.",
          "D: the side taken as the radius, 6, and then π left in by mistake."] },

{ sig: "right-triangle-in-circle-circumference", code: "GAT-Q-GEO.3", lvl: 3,
  stem: "The triangle drawn in the circle below is right-angled, and its two shorter sides are 6 cm and 8 cm. Find the circumference of the circle. (Take π = 3.14.)",
  fig: "h_tri_circle", figW: 2.05,
  opts: ["15.7", "31.4", "62.8", "78.5"], ans: 1,
  trick: "a right angle drawn on a circle always stands on a DIAMETER — so the hypotenuse is the diameter, and Pythagoras hands you the whole circle",
  why: "6² + 8² = 100, so the hypotenuse is 10 cm. That hypotenuse is the diameter, so the circumference is 3.14 × 10 = 31.4 cm.",
  traps: ["A: the radius used where the diameter belongs.",
          "C: 2πd used instead of πd.",
          "D: the AREA of the circle given, 3.14 × 5²."] },

// ================================================================= ALGEBRA
{ sig: "sum-of-squares-zero", code: "GAT-Q-ALG.1", lvl: 3,
  stem: "Use the statement below to find the value asked for.",
  stemEq: "h_sumsq",
  opts: ["−5", "−4", "−3", "0"], ans: 3,
  trick: "a square is never negative, so two squares can only add to zero if BOTH are zero — there is nothing to solve once you see that",
  why: "x² ≥ 0 and y² ≥ 0 for all real numbers, so x² + y² = 0 forces x = 0 and y = 0. Then x² − y² = 0.",
  traps: ["A: a guess from the pattern of the other options.",
          "B: the difference of squares expanded and a value invented for it.",
          "C: x and y treated as opposites with non-zero values."] },

{ sig: "equate-fourth-powers", code: "GAT-Q-ALG.2", lvl: 3,
  stem: "Solve for x, given that x is positive.", stemEq: "h_fourth",
  opts: ["−4", "2", "3", "6"], ans: 1,
  trick: "equal fractions with 1 on top mean equal bottoms — then write the number as a POWER that matches, and the exponents come off. An EVEN power allows a negative root too, which is why the question fixes the sign",
  why: "(x + 8)⁴ = 10 000 = 10⁴, so x + 8 = ±10. The positive case gives x = 2. (The other case, x + 8 = −10, gives x = −18, which the condition rules out — an even power always carries that second root.)",
  traps: ["A: the 8 added instead of subtracted.",
          "C: 10 000 read as 10³.",
          "D: x + 8 taken as 14."] },

{ sig: "equal-reciprocals-denominators", code: "GAT-Q-ALG.2", lvl: 2,
  stem: "Solve for x.", stemEq: "h_recip",
  opts: ["−1", "1", "3", "4"], ans: 1,
  trick: "if two fractions with 1 on top are equal then their bottoms are equal — cross-multiplying works but costs you twenty seconds you do not have",
  why: "2x + 1 = x + 2, so x = 1.",
  traps: ["A: both constants moved with the wrong sign.",
          "C: 2x − x read as 3x.",
          "D: the right-hand side doubled while cross-multiplying."] },

];

// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part L: from the unified practice sheet (Manus AI).
//
// That sheet held 104 questions, but far fewer than 104 skills: the triangle-area
// item appears four times, the circle-angle item four times, the shadow item
// four times, and the 2, 3, 5, 8, 12 sequence three times. Strip the repeats and
// remove everything the bank already had — two-tier tariffs, similar shadows,
// wheel revolutions, handshakes, LCM, unit conversion, probability from counts —
// and TWENTY-TWO skills were left. Those are below.
//
// The weighting is again driven by the ledger rather than by the source. Before
// this part the bank could build one more worksheet and was stopped by WORD
// LOGIC, which had two items left. Ten of the twenty-two are word logic and all
// of those are level 1 or 2, which is what a worksheet needs and what the strand
// was short of.
//
// One item in the source is worth naming because it is NOT here: "what condition
// makes {-s^2} positive?", whose four options are all wrong — a square is never
// negative, so {-s^2} is never positive. It was left out rather than repaired
// into something the source did not ask.
//
// Nothing is transcribed. Numbers, contexts and the one figure are new, and
// every answer is re-derived in verify_sim.py.
// ---------------------------------------------------------------------------
module.exports = [

// ================================================================ WORD LOGIC
{ sig: "salary-plus-commission-target", code: "GAT-Q-LOG.4", lvl: 2,
  stem: "A salesman is paid 7 000 SAR a month plus 500 SAR for every car he sells. How many cars must he sell in a month to be paid 12 000 SAR?",
  opts: ["8", "10", "12", "16"], ans: 1,
  trick: "take the fixed part off FIRST — only the difference is earned by selling, and dividing 12 000 by 500 is the fast wrong answer",
  why: "12 000 − 7 000 = 5 000 SAR must come from commission, and 5 000 ÷ 500 = 10 cars.",
  traps: ["A: 4 000 divided by 500.",
          "C: 6 000 divided by 500.",
          "D: 8 000 divided by 500, the fixed salary taken as 4 000."] },

{ sig: "linear-depreciation", code: "GAT-Q-LOG.4", lvl: 1,
  stem: "A machine is bought for 1 800 SAR and loses 200 SAR of its value every year. What is it worth after 7 years?",
  opts: ["100", "400", "500", "1 200"], ans: 1,
  trick: "a FIXED loss each year is multiplied, not compounded — 200 × 7 comes off the start value in one step",
  why: "200 × 7 = 1 400 SAR of value lost, so 1 800 − 1 400 = 400 SAR remain.",
  traps: ["A: 200 × 8 subtracted, an extra year counted.",
          "C: 200 taken off six times and then halved.",
          "D: 200 × 3 subtracted."] },

{ sig: "months-to-reach-savings-target", code: "GAT-Q-LOG.3", lvl: 1,
  stem: "A man has 17 000 SAR and saves 2 000 SAR a month towards a car costing 45 000 SAR. How many months must he save?",
  opts: ["11", "14", "22", "31"], ans: 1,
  trick: "he does not start from zero — subtract what he already has BEFORE dividing, which is the whole item",
  why: "He still needs 45 000 − 17 000 = 28 000 SAR, and 28 000 ÷ 2 000 = 14 months.",
  traps: ["A: 22 000 divided by 2 000.",
          "C: 45 000 divided by 2 000 and then halved.",
          "D: 62 000 divided by 2 000, the 17 000 added instead of subtracted."] },

{ sig: "count-from-total-and-unit-price", code: "GAT-Q-LOG.4", lvl: 1,
  stem: "Entry to an exhibition costs 20 SAR a person. One day's takings were 4 000 SAR. How many people entered?",
  opts: ["150", "200", "300", "800"], ans: 1,
  trick: "divide the total by the price of ONE — the answer is a count of people, so the riyals must cancel out",
  why: "4 000 ÷ 20 = 200 people.",
  traps: ["A: 3 000 divided by 20.",
          "C: 6 000 divided by 20.",
          "D: 4 000 divided by 5."] },

{ sig: "time-span-across-midnight-split", code: "GAT-Q-LOG.1", lvl: 2,
  stem: "A night shift runs from 8:00 p.m. until 3:30 a.m., and the time is shared equally among 6 workers. How many minutes does each work?",
  opts: ["65", "75", "85", "95"], ans: 1,
  trick: "count to midnight and then onwards — 4 hours plus 3½ hours — rather than subtracting the clock readings, which crosses midnight and gives nonsense",
  why: "8:00 p.m. to midnight is 4 hours and midnight to 3:30 a.m. is 3½ hours: 7½ hours, or 450 minutes. 450 ÷ 6 = 75 minutes each.",
  traps: ["A: 390 minutes divided by 6, half an hour lost.",
          "C: 510 minutes used.",
          "D: the clock readings subtracted as 8 − 3.5."] },

{ sig: "minimum-rooms-largest-capacity", code: "GAT-Q-LOG.3", lvl: 2,
  stem: "A hotel has rooms taking 2, 3 or 4 guests. What is the least number of rooms needed for 58 guests?",
  opts: ["14", "15", "16", "20"], ans: 1,
  trick: "to use the FEWEST rooms, fill the largest ones — 4 at a time — and then take one more room for whatever is left over",
  why: "14 rooms of 4 hold 56 guests, and the last 2 need one more room: 15 rooms.",
  traps: ["A: 58 ÷ 4 rounded down, leaving two guests without a room.",
          "C: rooms of 4 used but the remainder given a room of 4 and another counted.",
          "D: rooms of 3 used throughout."] },

{ sig: "fraction-difference-to-whole", code: "GAT-Q-LOG.3", lvl: 2,
  stem: "A tank is one sixth full. After 6 litres are poured in it is half full. What is the tank's capacity, in litres?",
  opts: ["12", "18", "24", "36"], ans: 1,
  trick: "the 6 litres are the DIFFERENCE between the two fractions, not a fraction of the tank on their own — find that difference first",
  why: "½ − ⅙ = ⅓ of the tank is 6 litres, so the capacity is 18 litres.",
  traps: ["A: the 6 litres taken as half the tank.",
          "C: ½ + ⅙ used instead of the difference.",
          "D: the 6 litres taken as one sixth."] },

{ sig: "rate-difference-over-time", code: "GAT-Q-LOG.3", lvl: 1,
  stem: "Badr reads 6 pages a day and his brother reads 8. How many more pages has his brother read after 16 days?",
  opts: ["2", "16", "32", "128"], ans: 2,
  trick: "find the daily DIFFERENCE first and multiply once — working out both totals and subtracting is two multiplications where one will do",
  why: "The brother reads 2 more pages a day, and 2 × 16 = 32 pages.",
  traps: ["A: the daily difference given.",
          "B: the number of days given.",
          "D: 8 × 16 given, the other reader ignored."] },

{ sig: "floor-division-full-containers", code: "GAT-Q-LOG.4", lvl: 1,
  stem: "A drum holds 900 cm³ of oil. How many bottles of 72 cm³ can be filled completely from it?",
  opts: ["11", "12", "13", "15"], ans: 1,
  trick: "'filled completely' means round DOWN — the opposite of a question asking how many buses or boxes are needed, where the leftover still takes one more",
  why: "900 ÷ 72 = 12.5, so 12 bottles can be filled and 36 cm³ are left over.",
  traps: ["A: 900 ÷ 80 taken.",
          "C: rounded up, as if the leftover filled a bottle — the trap this item exists for.",
          "D: 900 ÷ 60 taken."] },

{ sig: "chained-money-comparisons", code: "GAT-Q-LOG.3", lvl: 1,
  stem: "Yusuf has 300 SAR more than Mansour. Mansour has 500 SAR less than Saud, and Saud has 2 100 SAR. How many riyals does Yusuf have?",
  opts: ["1 300", "1 900", "2 300", "2 900"], ans: 1,
  trick: "start from the person whose amount you KNOW and work backwards along the chain — starting at Yusuf leaves two unknowns at once",
  why: "Saud has 2 100, so Mansour has 1 600 and Yusuf has 1 600 + 300 = 1 900 SAR.",
  traps: ["A: 300 subtracted from Mansour instead of added.",
          "C: 500 added to Saud rather than subtracted.",
          "D: both steps added to Saud."] },

// ================================================================= ALGEBRA
{ sig: "solve-equation-unlike-denominators", code: "GAT-Q-ALG.1", lvl: 2,
  stem: "Solve the equation below for x.", stemEq: "u_frac_eq",
  opts: ["12", "15", "18", "24"], ans: 2,
  trick: "add the two fractions FIRST — a third and a sixth make a half, so the equation is x/2 = 9 and there is nothing left to clear",
  why: "x/3 + x/6 = 2x/6 + x/6 = x/2, so x/2 = 9 and x = 18.",
  traps: ["A: the denominators added, giving x/9 = 9.",
          "B: 9 multiplied by 3 minus 6.",
          "D: both denominators multiplied out, giving x/18 wrongly inverted."] },

{ sig: "product-of-pair-products", code: "GAT-Q-ALG.3", lvl: 3,
  stem: "Three positive numbers satisfy the conditions below. Find the value of abc.",
  stemEq: "u_prod3",
  opts: ["2", "4", "8", "16"], ans: 1,
  trick: "multiply all three conditions together — each letter then appears TWICE, so the product is (abc)², and one square root finishes it",
  why: "(ab)(bc)(ac) = a²b²c² = 1 × 2 × 8 = 16, so (abc)² = 16 and abc = 4 for positive numbers.",
  traps: ["A: the three conditions added instead of multiplied.",
          "C: one of the three pairs used on its own.",
          "D: the square root not taken — the trap this item exists for."] },

{ sig: "square-equals-cube", code: "GAT-Q-ALG.3", lvl: 1,
  stem: "Find the positive number that satisfies the condition below.", stemEq: "u_sqcube",
  opts: ["1", "2", "3", "4"], ans: 0,
  trick: "divide both sides by s² — allowed here because s is positive — and the condition collapses to s = 1",
  why: "s² = s³ gives s³ − s² = 0, so s²(s − 1) = 0. With s positive, s = 1.",
  traps: ["B: 2² and 2³ assumed equal.",
          "C: 3 chosen from the exponents.",
          "D: 2² = 4 read as the value of s."] },

{ sig: "self-referential-linear", code: "GAT-Q-ALG.1", lvl: 2,
  stem: "A minaret's height is 30 metres more than a quarter of its own height. Find its height, in metres.",
  stemEq: "u_selfref",
  opts: ["30", "37.5", "40", "47.5"], ans: 2,
  trick: "collect the h terms on one side — three quarters of the height is 30, so the height is 40, not 30 plus a quarter of 30",
  why: "h − h/4 = 30 gives (3/4)h = 30, so h = 40 m.",
  traps: ["A: the 30 read as the height itself.",
          "B: a quarter of 30 added to 30.",
          "D: 30 increased by a quarter twice."] },

{ sig: "quadratic-from-rectangle-area", code: "GAT-Q-ALG.3", lvl: 2,
  stem: "A rectangle is 4 cm longer than it is wide and its area is 45 cm². Find its width, in centimetres.",
  stemEq: "u_rect",
  opts: ["3", "5", "9", "15"], ans: 1,
  trick: "look for two numbers 4 apart whose product is 45 before expanding anything — 5 and 9 are found faster than the quadratic is solved",
  why: "x(x + 4) = 45 gives x² + 4x − 45 = 0, so (x + 9)(x − 5) = 0 and the positive width is 5 cm.",
  traps: ["A: 3 × 7 = 21 tried and accepted.",
          "C: the LENGTH given instead of the width.",
          "D: 45 divided by 3."] },

// ============================================================== ARITHMETIC
{ sig: "double-plus-one-sequence", code: "GAT-Q-ARI.5", lvl: 2,
  stem: "Find the next term in the sequence below.", stemEq: "u_seq",
  opts: ["35", "41", "47", "51"], ans: 2,
  trick: "when the gaps double, the rule is not a difference but an operation — test 'double and add 1' on two terms before trusting it",
  why: "Each term is twice the one before it plus 1: 2, 5, 11, 23, and 2 × 23 + 1 = 47.",
  traps: ["A: 12 added, the growing gap ignored.",
          "B: the gap 18 repeated.",
          "D: 23 doubled and 5 added."] },

{ sig: "remainders-one-less-than-lcm", code: "GAT-Q-ARI.2", lvl: 3,
  stem: "Find the smallest whole number greater than 1 that leaves remainder 1 when divided by 2, remainder 2 when divided by 3, and remainder 3 when divided by 4.",
  opts: ["8", "9", "11", "13"], ans: 2,
  trick: "each remainder is ONE LESS than its divisor, so the number is one less than a common multiple — take the LCM and subtract 1",
  why: "The LCM of 2, 3 and 4 is 12, and 12 − 1 = 11 leaves remainders 1, 2 and 3 as required.",
  traps: ["A: 8 leaves remainder 0, 2 and 0.",
          "B: 9 leaves remainder 1, 0 and 1.",
          "D: 13 leaves remainder 1, 1 and 1."] },

{ sig: "consecutive-average-to-smallest", code: "GAT-Q-ARI.5", lvl: 2,
  stem: "Seven consecutive whole numbers have an average of 7. What is the smallest of them?",
  opts: ["1", "4", "5", "7"], ans: 1,
  trick: "for an odd run of consecutive numbers the average IS the middle one — so count back three places rather than solving anything",
  why: "The middle number is 7, so the seven numbers are 4, 5, 6, 7, 8, 9, 10 and the smallest is 4.",
  traps: ["A: seven subtracted from the average.",
          "C: only two places counted back.",
          "D: the average given as the smallest."] },

{ sig: "halala-riyal-compare", code: "GAT-Q-ARI.3", lvl: 1,
  stem: "Which quantity is greater: (A) 2 500 halalas, or (B) 25 riyals?",
  opts: ["A is greater", "B is greater", "they are equal", "not enough information"], ans: 2,
  trick: "convert to ONE unit before comparing — 100 halalas make a riyal, so 2 500 halalas is exactly 25 riyals",
  why: "2 500 ÷ 100 = 25 riyals, so the two are equal.",
  traps: ["A: the larger number read as the larger amount.",
          "B: 1 000 halalas taken as a riyal.",
          "D: both are exact amounts, so a comparison is always possible."] },

{ sig: "percent-commutes-compare", code: "GAT-Q-ARI.3", lvl: 1,
  stem: "Which quantity is greater: (A) 40% of 60, or (B) 60% of 40?",
  opts: ["A is greater", "B is greater", "they are equal", "not enough information"], ans: 2,
  trick: "both are 0.4 × 0.6 × 100 — swapping the percentage and the number it is taken of never changes the answer, so this one costs no working at all",
  why: "40% of 60 = 24 and 60% of 40 = 24. They are equal.",
  traps: ["A: 60 read as the larger starting number.",
          "B: 60% read as the larger percentage.",
          "D: both quantities are fully determined."] },

{ sig: "sum-of-squares-vs-square-compare", code: "GAT-Q-ARI.4", lvl: 2,
  stem: "Which quantity is greater?", stemEq: "u_cmp_sq",
  opts: ["A is greater", "B is greater", "they are equal", "not enough information"], ans: 0,
  trick: "606 + 505 is only a little more than 707, but SQUARING spreads them apart — two squares added always beat the square of a smaller-looking sum here, so estimate to the nearest hundred rather than multiplying in full",
  why: "606² + 505² ≈ 367 000 + 255 000 = 622 000, while 707² ≈ 500 000. A is greater.",
  traps: ["B: 707 read as the largest number and its square assumed largest.",
          "C: an identity assumed of the form a² + b² = c².",
          "D: all three numbers are given, so the comparison can be made."] },

// ===================================================================== DATA
{ sig: "median-from-table-grid", code: "GAT-Q-DAT.5", lvl: 2,
  stem: "Find the median of the sixteen numbers in the table below.",
  fig: "u_median_grid", figW: 2.2,
  opts: ["6", "6.5", "6.875", "7"], ans: 1,
  trick: "the table's rows mean nothing — write all sixteen values in ORDER, then average the eighth and ninth, because an even count has no single middle value",
  why: "Sorted, the values are 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13. The eighth and ninth are 6 and 7, so the median is 6.5.",
  traps: ["A: only the eighth value taken.",
          "C: the mean given.",
          "D: only the ninth value taken."] },

];

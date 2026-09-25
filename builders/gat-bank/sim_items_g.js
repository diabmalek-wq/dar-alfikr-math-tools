// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part G: the data strand, brought up to blueprint weight.
//
// WHY THIS FILE EXISTS. After part F the bank held 226 skills but only 21 of
// them were data — 10% against an ETEC blueprint of about 18%. Data was the one
// strand with no surplus, which meant a blueprint-accurate mock could not be
// SAMPLED from the bank: every data item in the bank would have had to go into
// every mock, and the class would have met each one before the real sitting.
//
// The twenty items below fix that. They are not more of the same: the sixteen
// data items already in the bank were nearly all "read one value off a chart".
// These add the four things the computerised sitting actually leans on and the
// department sets never covered —
//   · statistics that must be worked backwards (a missing value, a weighted
//     mean, the effect of an outlier),
//   · probability beyond one-step counting (complement, "or", without
//     replacement, expected numbers, area probability),
//   · counting where order does or does not matter,
//   · and chart reading where the obvious bar is the WRONG bar (largest
//     percentage rise on the smallest numbers, the modal class against the
//     median class, symbols against what the symbols stand for).
//
// Same rule as parts E and F: methods only, every item written fresh.
// ---------------------------------------------------------------------------
const CMP = ["A is greater", "B is greater", "they are equal",
             "not enough information"];

module.exports = [

// ==================================================== AVERAGES, WORKED BACK
{ sig: "weighted-mean-two-groups", code: "GAT-Q-DAT.5", lvl: 3,
  stem: "Section A has 20 students with a mean mark of 78. Section B has 30 students with a mean mark of 68. What is the mean mark of all 50 students?",
  opts: ["70", "72", "73", "74"], ans: 1,
  trick: "the two means cannot simply be averaged — the bigger group pulls harder, so add the TOTAL marks and divide by the total number of students",
  why: "Total marks = 20 × 78 + 30 × 68 = 1560 + 2040 = 3600, and 3600 ÷ 50 = 72.",
  traps: ["A: leaned too far towards the larger, weaker group.",
          "C: averaged 78 and 68 — the trap this item exists for.",
          "D: weighted the sections the wrong way round."] },

{ sig: "mean-missing-value", code: "GAT-Q-DAT.5", lvl: 2,
  stem: "A student's first four test marks are 82, 76, 90 and 68. What must the fifth mark be for the mean of all five to be exactly 80?",
  opts: ["79", "82", "84", "88"], ans: 2,
  trick: "the mean tells you the TOTAL — five marks averaging 80 must add to 400, so the missing mark is what is left",
  why: "The five marks must total 5 × 80 = 400. The first four total 316, so the fifth is 400 − 316 = 84.",
  traps: ["A: averaged the four marks given, 79, and stopped there.",
          "B: adjusted the mean of the four by two marks.",
          "D: made the total 404."] },

{ sig: "mean-from-frequency", code: "GAT-Q-DAT.5", lvl: 2,
  stem: "In a class of 20 students, 6 scored 5 marks, 9 scored 7 marks, 4 scored 8 marks and 1 scored 10 marks. What is the mean mark?",
  opts: ["6.5", "6.75", "7", "7.5"], ans: 1,
  trick: "each mark must be counted as many times as it OCCURS — divide by the number of students, never by the number of different marks",
  why: "Total = 6×5 + 9×7 + 4×8 + 1×10 = 30 + 63 + 32 + 10 = 135, and 135 ÷ 20 = 6.75.",
  traps: ["A: rounded the total down before dividing.",
          "C: gave the most common mark instead of the mean.",
          "D: averaged the four different marks, (5+7+8+10)÷4 — the trap this item exists for."] },

{ sig: "outlier-mean-vs-median", code: "GAT-Q-DAT.5", lvl: 3,
  stem: "The seven values 3, 5, 6, 8, 9, 11, 14 are recorded, and then the 14 is corrected to 70. Which is greater?   A: the increase in the mean   B: the increase in the median",
  opts: CMP, ans: 0,
  trick: "one extreme value drags the MEAN and leaves the median where it is — the median only counts positions, not sizes",
  why: "The mean rises from 56⁄7 = 8 to 112⁄7 = 16, an increase of 8. The median is the fourth value, 8, both before and after, so it does not move at all.",
  traps: ["B: assumed a bigger value must pull every average up.",
          "C: assumed the two averages always move together.",
          "D: every value is given, so both averages are fixed."] },

// ============================================================== PROBABILITY
{ sig: "probability-complement", code: "GAT-Q-DAT.3", lvl: 1,
  stem: "A bag holds 24 marbles, of which 9 are green. One marble is taken at random. What is the probability that it is NOT green?",
  opts: ["3⁄8", "5⁄8", "5⁄9", "2⁄3"], ans: 1,
  trick: "subtract from the WHOLE first — 24 − 9 = 15 favourable outcomes, and the denominator stays at 24",
  why: "There are 24 − 9 = 15 marbles that are not green, so the probability is 15⁄24 = 5⁄8.",
  traps: ["A: gave the probability that it IS green.",
          "C: divided the greens by the non-greens.",
          "D: rounded 15⁄24 to 2⁄3."] },

{ sig: "probability-or-multiples", code: "GAT-Q-DAT.3", lvl: 3,
  stem: "One of the numbers from 1 to 30 is chosen at random. What is the probability that it is a multiple of 3 or a multiple of 5?",
  opts: ["7⁄15", "8⁄15", "1⁄2", "3⁄5"], ans: 0,
  trick: "the numbers counted TWICE must come off once — 15 and 30 are multiples of both, so subtract them",
  why: "Multiples of 3: 10. Multiples of 5: 6. Multiples of 15: 2, counted in both lists. So 10 + 6 − 2 = 14 numbers, and 14⁄30 = 7⁄15.",
  traps: ["B: added 10 and 6 without removing the overlap — the trap this item exists for.",
          "C: counted 15 numbers.",
          "D: counted 18 numbers."] },

{ sig: "probability-without-replacement", code: "GAT-Q-DAT.3", lvl: 3,
  stem: "A box holds 5 red pens and 3 blue pens. Two pens are taken out one after the other, and the first is not put back. What is the probability that both are red?",
  opts: ["5⁄14", "5⁄16", "25⁄64", "5⁄28"], ans: 0,
  trick: "the second draw happens on a SMALLER box — both the top and the bottom of the second fraction go down by one",
  why: "P = 5⁄8 × 4⁄7 = 20⁄56 = 5⁄14.",
  traps: ["B: reduced the total but not the reds.",
          "C: multiplied 5⁄8 by 5⁄8, as if the pen were put back — the trap this item exists for.",
          "D: halved the correct answer."] },

{ sig: "expected-count-from-probability", code: "GAT-Q-DAT.3", lvl: 2,
  stem: "At an exhibition in Jeddah the probability that a visitor buys a ticket for the evening show is 0.15. Out of 2400 visitors, how many would you expect to buy one?",
  opts: ["240", "300", "360", "400"], ans: 2,
  trick: "an expected number is just the probability TIMES the total — 0.15 is 15 per hundred, not 15 per thousand",
  why: "0.15 × 2400 = 360 visitors.",
  traps: ["A: used 0.10.",
          "B: used 1⁄8 of the visitors.",
          "D: rounded 0.15 up to one sixth."] },

{ sig: "probability-from-area", code: "GAT-Q-DAT.3", lvl: 3,
  stem: "A square board of side 14 cm carries a circular target of radius 7 cm that touches all four sides. A dart lands at a random point on the board. What is the probability that it lands on the target? (Take π = 22⁄7.)",
  opts: ["3⁄14", "1⁄4", "11⁄14", "7⁄8"], ans: 2,
  trick: "when the outcome is a position rather than a count, probability is an AREA over an area",
  why: "Target 22⁄7 × 7² = 154 cm²; board 14² = 196 cm². So 154⁄196 = 11⁄14.",
  traps: ["A: gave the probability of missing the target.",
          "B: compared the radius with the side instead of the areas.",
          "D: compared 7 with 8."] },

// ================================================================ COUNTING
{ sig: "counting-code-choices", code: "GAT-Q-DAT.4", lvl: 2,
  stem: "A locker code is made of 2 letters chosen from A, B, C, D, E followed by 3 digits chosen from 0 to 9. Letters and digits may be repeated. How many different codes are possible?",
  opts: ["5000", "25 000", "30 000", "50 000"], ans: 1,
  trick: "when repeats are allowed every position has the FULL set to choose from, and the positions multiply",
  why: "5 × 5 × 10 × 10 × 10 = 25 000 codes.",
  traps: ["A: used only one letter position.",
          "C: added the letter choices instead of multiplying them.",
          "D: used 5 × 10 000."] },

{ sig: "counting-with-constraint", code: "GAT-Q-DAT.4", lvl: 3,
  stem: "A committee of 3 is chosen from 5 boys and 4 girls, and it must contain exactly 2 boys and 1 girl. In how many ways can it be formed?",
  opts: ["20", "40", "60", "84"], ans: 1,
  trick: "choose within each group SEPARATELY and then multiply — order does not matter on a committee",
  why: "Boys: 5 × 4 ÷ 2 = 10 ways. Girls: 4 ways. Together 10 × 4 = 40.",
  traps: ["A: chose the boys in order and then halved twice.",
          "C: counted the boys as ordered pairs, 20 × 4 ÷ 2 slipped.",
          "D: ignored the condition and chose any 3 from 9 — the trap this item exists for."] },

// ==================================================== SPREAD AND POSITION
{ sig: "median-even-count", code: "GAT-Q-DAT.2", lvl: 2,
  stem: "Find the median of 6, 13, 9, 20, 18, 11, 15 and 24.",
  opts: ["13", "14", "14.5", "15"], ans: 1,
  trick: "order the list first, and with an EVEN count the median is the average of the two middle values, not either one of them",
  why: "In order: 6, 9, 11, 13, 15, 18, 20, 24. The two middle values are 13 and 15, so the median is (13 + 15) ÷ 2 = 14.",
  traps: ["A: took the fourth value on its own.",
          "C: averaged the wrong pair.",
          "D: took the fifth value on its own."] },

{ sig: "range-after-adding-value", code: "GAT-Q-DAT.2", lvl: 2,
  stem: "The values 12, 19, 25, 31 and 47 are recorded, and then a sixth value of 8 is added. Which is greater?   A: the range of the first five values   B: the range of all six values",
  opts: CMP, ans: 1,
  trick: "the range depends only on the LARGEST and the SMALLEST — a new value changes it only if it falls outside both",
  why: "First five: 47 − 12 = 35. All six: 47 − 8 = 39. So B is greater.",
  traps: ["A: assumed extra data cannot widen the range.",
          "C: assumed a value inside the old maximum leaves the range alone — 8 is below the old minimum.",
          "D: all six values are given."] },

// ============================================================= CHART SKILLS
{ sig: "pie-percent-to-amount", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The pie chart below shows how a monthly household budget of 7200 SAR is divided. How much is spent on the part marked with a question mark, in SAR?",
  fig: "sim_pie_missing", figW: 2.05,
  opts: ["2160", "2880", "3600", "4320"], ans: 1,
  trick: "two steps, and the first is the one that gets skipped — find the missing PERCENTAGE from 100 before touching the money",
  why: "The three sectors given are 20 + 15 + 25 = 60%, so the missing one is 40%. Then 40% of 7200 = 2880 SAR.",
  traps: ["A: used 30% for the missing sector.",
          "C: split what was left equally between two sectors and took half.",
          "D: spent the 60% that IS labelled instead of the 40% that is not."] },

{ sig: "line-largest-gap", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The graph shows monthly sales at two branches. In which month is the difference between the branches greatest?",
  fig: "sim_line_gap", figW: 2.75,
  opts: ["February", "March", "April", "May"], ans: 2,
  trick: "the widest gap is not where either line PEAKS — read the vertical distance between the lines, month by month",
  why: "The gaps are 8, 16, 4, 24 and 6. The largest, 24, is in April.",
  traps: ["A: read the month where the lower line first rises sharply.",
          "B: read the month where the lines come closest.",
          "D: read the month where the upper line ends, not where the gap is widest."] },

{ sig: "bar-percent-increase", code: "GAT-Q-DAT.1", lvl: 2,
  stem: "The bar chart below shows quarterly sales, in thousands of SAR. By what percentage did sales rise from the third quarter to the fourth?",
  fig: "sim_bar_pct_change", figW: 2.73,
  opts: ["18%", "28%", "40%", "45%"], ans: 2,
  trick: "a percentage rise is measured against the STARTING bar, so divide the rise by the third quarter, not by the fourth",
  why: "The rise is 63 − 45 = 18, and 18 ÷ 45 = 0.40, so 40%.",
  traps: ["A: read the rise of 18 as 18% — the trap this item exists for.",
          "B: divided the rise by the fourth quarter, 18 ÷ 63.",
          "D: compared the fourth quarter with the first."] },

{ sig: "histogram-median-class", code: "GAT-Q-DAT.2", lvl: 3,
  stem: "The chart shows the times taken by 48 competitors, in minutes. Which interval contains the median time?",
  fig: "sim_hist_class", figW: 2.81,
  opts: ["10 – 20", "20 – 30", "30 – 40", "40 – 50"], ans: 1,
  trick: "the median sits at the MIDDLE POSITION, so add the bars up from the left until you pass half the total — the tallest bar is a different question",
  why: "Half of 48 is 24. The running totals are 9, 21, 29, 43, 48, so the 24th and 25th values both fall in 20 – 30.",
  traps: ["A: stopped one interval early, at a running total of 21.",
          "C: picked the tallest bar — the trap this item exists for.",
          "D: picked the last interval."] },

{ sig: "table-largest-percent-rise", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The table shows applicant numbers at four campuses. Which campus had the largest percentage increase from 1446 to 1447?",
  fig: "sim_table_growth", figW: 2.30,
  opts: ["Jeddah", "Makkah", "Madinah", "Dammam"], ans: 3,
  trick: "the largest RISE and the largest percentage rise are rarely the same campus — always divide by the starting figure",
  why: "Jeddah 48⁄240 = 20%, Makkah 54⁄180 = 30%, Madinah 12⁄120 = 10%, Dammam 21⁄60 = 35%. Dammam is largest.",
  traps: ["A: picked the campus with the largest numbers.",
          "B: picked the largest rise in applicants, +54 — the trap this item exists for.",
          "C: divided by the later figure instead of the earlier one."] },

{ sig: "stacked-bar-majority", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The chart shows the number of boys and girls at three schools. At which school or schools do girls make up more than half the students?",
  fig: "sim_stacked_schools", figW: 2.55,
  opts: ["School A only", "School B only", "Schools B and C", "School C only"], ans: 1,
  trick: "compare each part with the WHOLE bar, not with the bar beside it — and 'more than half' does not include exactly half",
  why: "A: 80 girls of 200, B: 110 of 200, C: 150 of 300. Only School B is above half; School C is exactly half.",
  traps: ["A: compared the girls' blocks with each other and picked the shortest bar.",
          "C: counted School C, where the two parts are equal — the trap this item exists for.",
          "D: picked the tallest bar."] },

{ sig: "pictogram-key-scale", code: "GAT-Q-DAT.1", lvl: 2,
  stem: "The pictogram below shows how many books were borrowed each week. How many more books were borrowed in week 2 than in week 3?",
  fig: "sim_pictogram", figW: 2.70,
  opts: ["3", "16", "24", "32"], ans: 2,
  trick: "count the symbols, then multiply by what ONE symbol is worth — the difference in symbols is not the difference in books",
  why: "Week 2 has 7 symbols and week 3 has 4, a difference of 3 symbols. Each symbol is 8 books, so 3 × 8 = 24 books.",
  traps: ["A: gave the difference in symbols — the trap this item exists for.",
          "B: used 2 books per symbol.",
          "D: used the week 2 total, 7 × 8 ÷ 1.75."] },

];

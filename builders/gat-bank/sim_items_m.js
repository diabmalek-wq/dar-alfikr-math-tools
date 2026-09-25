// ---------------------------------------------------------------------------
// SIMULATED GAT BANK — part M: level-3 arithmetic and data (20 items)
//
// Written to close the single highest-value gap flagged in the Coverage
// Audit: the unissued pool had run down to 2 arithmetic items and 1 data
// item, blocking the next weekly worksheet, while the unused level-3 pool
// bank-wide had fallen to 5. This part adds 12 level-3 arithmetic items
// (multi-step: two or three operations, not one) and 8 level-3 data items
// (charts with a calculation on top, weighted averages, a grouped-mean
// estimate, permutations, and a mean-vs-median comparison), all ORIGINAL —
// no wording, number set, or figure reproduced from any source. Every
// answer was re-derived independently in Python (verify_sim.py) before this
// part was wired into the build. Answer letters were chosen to favour A and
// D, the two most under-used positions bank-wide, wherever a natural
// distractor set allowed it without forcing an artificial option.
// ---------------------------------------------------------------------------
const CMP = ["A is greater", "B is greater", "they are equal",
             "not enough information"];

module.exports = [

// ============================================================== ARITHMETIC
{ sig: "lcm-three-buses", code: "GAT-Q-ARI.1", lvl: 3,
  stem: "Three tour buses leave the same terminal in Jeddah together at 8:00 a.m. Bus A returns to the terminal every 18 minutes, Bus B every 24 minutes, and Bus C every 30 minutes. How many minutes pass before all three are at the terminal together again?",
  opts: ["72", "90", "120", "360"], ans: 3,
  trick: "the buses meet again at the LCM of all THREE intervals, not the LCM of just two of them — leaving a bus out of the calculation is the trap",
  why: "LCM(18, 24, 30) = 360. All three are back at the terminal together after 360 minutes.",
  traps: ["A: the LCM of only Bus A and Bus B, 18 and 24.",
          "B: the LCM of only Bus A and Bus C, 18 and 30.",
          "C: the LCM of only Bus B and Bus C, 24 and 30."] },

{ sig: "remainder-common-divisor", code: "GAT-Q-ARI.1", lvl: 3,
  stem: "N is a whole number between 200 and 300. When N is divided by 9 the remainder is 4, and when N is divided by 12 the remainder is also 4. What is N?",
  opts: ["229", "244", "250", "256"], ans: 3,
  trick: "both remainders are the SAME, so N − 4 is divisible by both divisors at once — find the LCM of 9 and 12 first, then add the remainder back",
  why: "N − 4 must be a multiple of lcm(9, 12) = 36. In the range 200–300 the only such N is 256, since 256 − 4 = 252 = 36 × 7.",
  traps: ["A: satisfies the divide-by-9 condition alone (229 − 4 = 225 = 9 × 25) but not the divide-by-12 condition.",
          "B: satisfies the divide-by-12 condition alone (244 − 4 = 240 = 12 × 20) but not the divide-by-9 condition.",
          "C: falls in the range but satisfies neither condition."] },

{ sig: "ratio-mix-paint", code: "GAT-Q-ARI.2", lvl: 3,
  stem: "A can of mixed paint weighs 9.6 kg in total. The blue and white paints inside it are mixed in the ratio 5 : 3. How many kilograms of white paint does the can contain?",
  opts: ["3.6", "4.8", "6", "230.4"], ans: 0,
  trick: "share the TOTAL weight into 5 + 3 = 8 parts first — the white paint is 3 of those 8 parts, not half the can",
  why: "9.6 kg ÷ 8 parts = 1.2 kg per part. White is 3 parts: 3 × 1.2 = 3.6 kg.",
  traps: ["B: half the total weight, the ratio ignored entirely.",
          "C: the BLUE paint's weight, the ratio's two parts swapped.",
          "D: the total multiplied by the 8 parts instead of divided by them."] },

{ sig: "defect-rate-scaled", code: "GAT-Q-ARI.2", lvl: 3,
  stem: "A factory inspects its output and finds 3 faulty items in every batch of 250 produced. At this same rate, how many faulty items would be expected in a production run of 12 500?",
  opts: ["50", "75", "125", "150"], ans: 3,
  trick: "scale the RATE up to the full run in two steps — first find how many 250-batches fit into the run, then multiply that count by 3, since one of the two steps is easy to skip",
  why: "12 500 ÷ 250 = 50 batches, and 50 × 3 = 150 faulty items.",
  traps: ["A: the 50 batches found correctly, but the final ×3 step forgotten.",
          "B: the run halved before the rate was scaled up.",
          "C: the rate treated as 3 faulty per 300, not per 250."] },

{ sig: "map-scale-area", code: "GAT-Q-ARI.2", lvl: 3,
  stem: "A map is drawn to a scale of 1 : 40 000. A rectangular plot of land measures 3 cm by 2 cm on the map. Find the actual area of the plot, in square kilometres.",
  opts: ["0.48", "0.96", "1.92", "2.4"], ans: 1,
  trick: "a LINEAR scale of 1 : 40 000 becomes an AREA scale of 1 : 40 000² — square the scale factor before it ever touches the area, never after",
  why: "The real dimensions are 3 × 40 000 = 120 000 cm = 1.2 km and 2 × 40 000 = 80 000 cm = 0.8 km. The real area is 1.2 × 0.8 = 0.96 km².",
  traps: ["A: the correct area halved.",
          "C: the correct area doubled.",
          "D: the map's area, 6 cm², multiplied by the scale factor only ONCE and converted with the linear cm-to-km factor — 6 × 40 000 ÷ 100 000."] },

{ sig: "successive-discounts", code: "GAT-Q-ARI.3", lvl: 3,
  stem: "A laptop costs 800 SAR. It is discounted 25%, and the reduced price is then discounted a further 10%. Find the final price, in SAR.",
  opts: ["520", "540", "600", "660"], ans: 1,
  trick: "apply the two discounts ONE AFTER ANOTHER, each to the price left after the one before it — adding 25% and 10% into a single 35% off is not the same calculation",
  why: "800 × 0.75 = 600 SAR after the first discount, then 600 × 0.90 = 540 SAR after the second.",
  traps: ["A: a single 35% discount (25 + 10) applied directly to 800.",
          "C: only the first discount applied, the second forgotten.",
          "D: the two discounts averaged into a single 17.5% off, 800 × 0.825, instead of applied in sequence."] },

{ sig: "percent-inc-then-dec", code: "GAT-Q-ARI.3", lvl: 3,
  stem: "A shop increases a price by 20%, and then decreases the new price by 20%. Compared with the ORIGINAL price, what is the net change?",
  opts: ["decreased by 20%", "increased by 4%", "no net change", "decreased by 4%"], ans: 3,
  trick: "a rise and a fall of the SAME percentage never cancel out, because the fall is taken from a larger number than the rise was — track the actual price through both steps instead of assuming they undo each other",
  why: "Start at 100. After the rise: 100 × 1.20 = 120. After the fall: 120 × 0.80 = 96. That is a net decrease of 4% from the original 100.",
  traps: ["A: only the second step's 20% applied to the ORIGINAL price, the first step ignored.",
          "B: the direction of the net change reversed.",
          "C: the rise and fall assumed to cancel because they share the same percentage — the trap this item exists for."] },

{ sig: "vat-reverse", code: "GAT-Q-ARI.3", lvl: 3,
  stem: "A washing machine's price, including 15% VAT, is 690 SAR. What was its price before VAT, in SAR?",
  opts: ["90", "510", "586.5", "600"], ans: 3,
  trick: "690 SAR already INCLUDES the tax, so divide by 1.15 to undo it — subtracting 15% of 690 is not the reverse of adding 15% in the first place",
  why: "690 ÷ 1.15 = 600 SAR.",
  traps: ["A: the VAT amount itself given as the answer, not the price.",
          "B: 15% of the correct pre-VAT price deducted a second time, from 600.",
          "C: 15% of the inclusive price, 690, subtracted directly from 690."] },

{ sig: "age-ratio-future", code: "GAT-Q-ARI.4", lvl: 3,
  stem: "A father's age and his son's age are currently in the ratio 7 : 2. In 10 years, the ratio of their ages will be 9 : 4. What is the father's CURRENT age?",
  opts: ["35", "45", "55", "63"], ans: 0,
  trick: "let the current ages be 7k and 2k, add 10 to EACH one, and set the new ratio equal to 9 : 4 — the '+10' applies to both ages, not just to the ratio numbers",
  why: "(7k + 10) / (2k + 10) = 9/4, so 4(7k + 10) = 9(2k + 10), giving 28k + 40 = 18k + 90, so 10k = 50 and k = 5. The father's current age is 7 × 5 = 35.",
  traps: ["B: the father's age IN 10 YEARS given, not his current age.",
          "C: the 10-year shift added twice by mistake.",
          "D: 7 multiplied by the new ratio's 9 directly, the equation skipped entirely."] },

{ sig: "combined-tank-rate-not-enough-info", code: "GAT-Q-ARI.4", lvl: 3,
  stem: "Pipe A alone can fill a tank in 6 hours. Which is greater?   A: the fraction of the tank Pipe A fills in one hour.   B: the fraction of the tank Pipe B fills in one hour.",
  opts: CMP, ans: 3,
  trick: "a comparison needs BOTH sides pinned down — nothing at all is stated about Pipe B, so no comparison can be decided, no matter how confident A's value looks",
  why: "Pipe A fills 1/6 of the tank per hour. Pipe B's rate is never given, so B cannot be evaluated, and the comparison cannot be decided.",
  traps: ["A: Pipe B assumed slower simply because nothing is said about it.",
          "B: Pipe B assumed faster simply because it is asked about second.",
          "C: the two pipes assumed to work at the same rate merely because none is stated for B."] },

{ sig: "geometric-8th-term", code: "GAT-Q-ARI.5", lvl: 3,
  stem: "In the sequence 3, 6, 12, 24, …, each term after the first is double the one before it. Find the 8th term.",
  opts: ["24", "192", "384", "768"], ans: 2,
  trick: "the nth term of a doubling sequence is (first term) × 2^(n − 1) — the exponent is one LESS than the term's position, a slip that is easy to make when counting terms by hand",
  why: "The 8th term is 3 × 2⁷ = 3 × 128 = 384.",
  traps: ["A: the sequence treated as arithmetic, adding a constant difference of 3 instead of doubling.",
          "B: the 7th term given, one short of the 8th.",
          "D: the exponent taken as 8 instead of 7, giving 3 × 2⁸."] },

{ sig: "arith-series-sum", code: "GAT-Q-ARI.5", lvl: 3,
  stem: "An arithmetic sequence begins at 7 and has a common difference of 5. Find the sum of its first 20 terms.",
  opts: ["107", "891", "988", "1090"], ans: 3,
  trick: "use the sum formula S = n/2 × [2a + (n − 1)d] with the actual term COUNT, 20 — not a shortcut that skips straight from the first term to a guess at the last one",
  why: "S = 20/2 × [2(7) + 19(5)] = 10 × [14 + 95] = 10 × 109 = 1090.",
  traps: ["A: the formula S = n·d + a used instead of the real sum formula.",
          "B: the term count taken as 18 instead of 20.",
          "C: the term count taken as 19 instead of 20."] },

// ===================================================================== DATA
{ sig: "weighted-avg-exam-components", code: "GAT-Q-DAT.5", lvl: 3,
  stem: "A student's course grade is built from three components: a quiz worth 20% of the grade, a midterm worth 30%, and a final exam worth 50%. The student scored 70 on the quiz, 80 on the midterm, and 90 on the final. Find the student's overall course grade.",
  opts: ["75", "77", "80", "83"], ans: 3,
  trick: "multiply EACH score by its OWN weight and add the results — averaging the three scores as if they counted equally throws away the weighting entirely",
  why: "0.20 × 70 + 0.30 × 80 + 0.50 × 90 = 14 + 24 + 45 = 83.",
  traps: ["A: only the quiz and midterm averaged, the final left out entirely.",
          "B: the weights applied in reverse order — 50% to the quiz, 20% to the final.",
          "C: a plain unweighted average of the three scores, (70 + 80 + 90) ÷ 3."] },

{ sig: "grouped-mean-estimate", code: "GAT-Q-DAT.5", lvl: 3,
  stem: "The chart below shows the times, in minutes, taken by 50 runners to finish a race, grouped into five classes. Estimate the mean finishing time.",
  fig: "sim_hist_grouped_freq", figW: 2.81,
  opts: ["24.6", "25", "29.6", "246"], ans: 0,
  trick: "estimate the mean using each class's MIDPOINT, not its upper boundary — the midpoints here are 5, 15, 25, 35 and 45, one for every class",
  why: "(5×5 + 15×12 + 25×18 + 35×10 + 45×5) ÷ 50 = 1230 ÷ 50 = 24.6 minutes.",
  traps: ["B: the modal class's midpoint given as the mean.",
          "C: each class's UPPER boundary used instead of its midpoint.",
          "D: the total divided by the number of classes, 5, instead of the total number of runners, 50."] },

{ sig: "bar-chart-revenue-target", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The chart below shows units sold each quarter, in thousands. Each unit sells for 25 SAR. In which quarter did revenue first exceed 1 500 000 SAR?",
  fig: "sim_bar_revenue_quarters", figW: 2.73,
  opts: ["Q1", "Q2", "Q3", "Q4"], ans: 3,
  trick: "convert EACH bar to revenue, units × 1000 × 25 SAR, before comparing it to the target — the tallest-looking bar is not automatically the one that clears it",
  why: "Revenues are Q1 = 1 000 000, Q2 = 1 375 000, Q3 = 875 000, Q4 = 1 750 000 SAR. Only Q4 exceeds 1 500 000.",
  traps: ["A: the revenue computed correctly, but compared against a target read as 1 000 000, not 1 500 000.",
          "B: the closest quarter to the target picked without checking it actually clears it — 1 375 000 is still short of 1 500 000, the trap this item exists for.",
          "C: the units read directly as the revenue, without multiplying by the price at all."] },

{ sig: "line-chart-steepest-rise", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "The graph below shows a greenhouse's temperature, in °C, recorded every two hours. Between which two consecutive readings did the temperature rise the MOST?",
  fig: "sim_line_temp_rise", figW: 2.6,
  opts: ["0 to 2 hours", "2 to 4 hours", "4 to 6 hours", "6 to 8 hours"], ans: 1,
  trick: "compare the RISE across each two-hour gap, not the height the line eventually reaches — the steepest gap is not always the one ending at the highest point",
  why: "The rises are 4, 7, 2 and 2 degrees across the four gaps. The largest, 7 degrees, is between hours 2 and 4.",
  traps: ["A: the first interval picked without comparing it to the others.",
          "C: the point where the line is highest confused with where it rises fastest.",
          "D: the last interval picked, where the line is still rising but only slightly."] },

{ sig: "probability-at-least-one-red", code: "GAT-Q-DAT.3", lvl: 3,
  stem: "A box holds 4 red pens and 6 blue pens. Two pens are drawn out one after another, without putting the first one back. What is the probability that AT LEAST ONE of the two pens is red?",
  opts: ["2/15", "2/5", "16/25", "2/3"], ans: 3,
  trick: "'at least one' is fastest through the COMPLEMENT — find the probability that NEITHER pen is red, and subtract that from 1, rather than adding up every red-pen case separately",
  why: "P(no red) = 6/10 × 5/9 = 1/3. So P(at least one red) = 1 − 1/3 = 2/3.",
  traps: ["A: the probability that BOTH pens are red computed and given for 'at least one' instead.",
          "B: only the first draw's probability of red used, the second draw ignored.",
          "C: the pens treated as replaced after the first draw, using 6/10 × 6/10 for 'no red'."] },

{ sig: "permutation-vowels-not-adjacent", code: "GAT-Q-DAT.4", lvl: 3,
  stem: "The word RIYADH has six different letters, two of which (I and A) are vowels. In how many ways can all six letters be arranged so that the two vowels are NEVER next to each other?",
  opts: ["240", "360", "480", "720"], ans: 2,
  trick: "count the arrangements where the vowels ARE together — glue them into one block — and subtract that from the total, since counting the 'never together' arrangements directly is far harder",
  why: "All 6 letters arrange in 6! = 720 ways. Gluing I and A into one block gives 5! × 2! = 240 arrangements where they ARE adjacent, so 720 − 240 = 480 arrangements keep them apart.",
  traps: ["A: the adjacent count given as the answer to the 'never adjacent' question — the trap this item exists for.",
          "B: the total divided by 2 instead of the adjacent count subtracted.",
          "D: no restriction applied at all."] },

{ sig: "median-vs-mean-outlier", code: "GAT-Q-DAT.2", lvl: 3,
  stem: "A small data set is 12, 15, 15, 18, 90. Which is greater?   A: the median of the data set.   B: the mean of the data set.",
  opts: CMP, ans: 1,
  trick: "a single extreme value pulls the MEAN a long way but barely touches the MEDIAN — find both rather than assuming a 'typical' data set behaves the same way",
  why: "Sorted, the median (the middle value) is 15. The mean is (12 + 15 + 15 + 18 + 90) ÷ 5 = 150 ÷ 5 = 30. The mean is greater.",
  traps: ["A: assumed the median is always at least as large as the mean.",
          "C: assumed the outlier affects both measures equally.",
          "D: both quantities are fully computable from the five values given."] },

{ sig: "two-group-percent-total", code: "GAT-Q-DAT.1", lvl: 3,
  stem: "Of the 200 students in a school, 120 study Science and the remaining 80 study Arts. Among the Science students, 45% also take Robotics as an elective; among the Arts students, 20% take Robotics. How many students in total take Robotics?",
  opts: ["60", "70", "90", "130"], ans: 1,
  trick: "apply EACH percentage to its OWN group and add the two counts — applying one group's percentage to the whole school, or swapping the two percentages, both throw the answer off",
  why: "Science: 45% of 120 = 54. Arts: 20% of 80 = 16. Total = 54 + 16 = 70 students.",
  traps: ["A: the two percentages swapped between the groups — 20% of Science, 45% of Arts.",
          "C: the Science percentage, 45%, applied to the whole school of 200.",
          "D: the two percentages simply added, 45% + 20% = 65%, and applied to the whole school."] },

];

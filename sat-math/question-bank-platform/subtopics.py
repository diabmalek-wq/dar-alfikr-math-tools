import re
R=lambda s:re.compile(s,re.I)
TAX={
'Equivalent expressions':[
 ('Exponents and radicals',R(r'sqrt\[|\\sqrt|exponent|\^\{?\\?(?:dfrac|frac)|radical|\^\{-|rational exponent|\d\^\{x|\d\^x|power')),
 ('Rational expressions',R(r'\\d?frac\{[^}]*x[^}]*\}\{[^}]*x|rational expression|equivalent to \$\\d?frac')),
 ('Polynomial division and remainder',R(r'remainder|divided by|divisible|factor theorem|polynomial division|quotient')),
 ('Factoring and expanding',R(r'factor|expand|product|\(x[+-]\d+\)\(|difference of squares|perfect square|equivalent')),
],
'Nonlinear equations and systems':[
 ('Linear-nonlinear and nonlinear systems',R(r'system|intersect|solutions? \(x|ordered pair|point.*(?:line|parabola|circle)')),
 ('Quadratic equations and discriminant',R(r'discriminant|exactly one (?:real )?solution|no real solution|two distinct|solutions? of .*x\^\{?2|quadratic|roots?|sum of the (?:squares|solutions)|product of the solutions|x\^2|x\^\{2\}')),
 ('Radical and rational equations',R(r'sqrt|\\d?frac\{[^}]*\}\{[^}]*x|extraneous|denominator')),
 ('Exponential and other equations',R(r'\d\^x|\d\^\{x|exponential|log|abs|\|')),
],
'Nonlinear functions':[
 ('Exponential growth and decay',R(r'exponential|growth|decay|doubl|half-life|depreciat|compound|percent (?:per|each)|%.*(?:each|per) (?:year|month|day|hour)|\d\^\{?[tx]|\^\{?t/')),
 ('Quadratic functions and vertex form',R(r'parabola|vertex|axis of symmetry|maximum|minimum|zeros?|x-intercept|quadratic|x\^\{?2|x\^2|projectile|height.*seconds')),
 ('Function transformations and notation',R(r'transform|shift|reflect|translat|f\(x\s*[+-]|g\(x\)\s*=\s*f|composite|f\(g|g\(f|f\(\d|g\(\d|h\(\d|domain|range|even|odd|inverse')),
 ('Polynomial and rational function graphs',R(r'polynomial|degree|asymptote|end behavior|cubic|rational function|x\^3|x\^\{3\}|x\^4|hole|zeros? of|factor')),
],
'Linear equations in one variable':[
 ('Number of solutions (none or infinite)',R(r'no solution|infinitely many|exactly one solution|number of solutions|how many solutions')),
 ('Equations with constants and parameters',R(r'constant|for what value of \$?[a-z]|value of \$?k')),
 ('Word problems and writing equations',R(r'SAR|cost|each|per |total|ticket|price|rate|hour|bought|sold|fee|week|month|team|students')),
 ('Solving and rearranging',R(r'.*')),
],
'Linear equations in two variables':[
 ('Parallel and perpendicular lines',R(r'parallel|perpendicular')),
 ('Intercepts and slope from an equation',R(r'intercept|slope|x-intercept|y-intercept')),
 ('Writing and interpreting models',R(r'SAR|cost|each|per |total|ticket|price|rate|hour|represent|meaning|interpret|mix|combination')),
 ('Graphs and points on lines',R(r'.*')),
],
'Linear functions':[
 ('Interpreting slope and intercept in context',R(r'interpret|represents?|meaning|each (?:additional|extra)|per |rate|SAR|cost|every')),
 ('Writing a linear function',R(r'which of the following (?:equations|functions)|defines|function .* models|table|two points|passes through')),
 ('Evaluating and transforming linear functions',R(r'f\(|g\(|h\(|shift|translat|reflect|transform')),
 ('Slope and graph features',R(r'.*')),
],
'Linear inequalities':[
 ('Systems of inequalities',R(r'system|graph|region|shaded|ordered pair|\(x,\s*y\)')),
 ('Compound and absolute value inequalities',R(r'compound|abs|\||between|less than .* and greater')),
 ('Inequality word problems',R(r'at least|at most|no more than|no less than|minimum|maximum|budget|SAR|cost|each|per ')),
 ('Solving and solution sets',R(r'.*')),
],
'Systems of linear equations':[
 ('No solution or infinitely many solutions',R(r'no solution|infinitely many|exactly one|number of solutions|parallel')),
 ('Word problems with systems',R(r'SAR|cost|each|per |total|ticket|price|tickets|adult|child|coins?|mix|bought|sold|hour|team|students|boxes')),
 ('Finding a value from the solution',R(r'value of|what is|sum|product|difference|\(x,\s*y\)|ordered pair')),
 ('Solving by substitution or elimination',R(r'.*')),
],
'Area and volume':[
 ('Volume of solids',R(r'volume|cylinder|cone|sphere|prism|pyramid|cube|tank|capacity|litre|liter|cm\^3|m\^3|\^\{3\}')),
 ('Surface area and scaling',R(r'surface area|scale|similar|ratio of the (?:areas|volumes)|dilat|enlarg')),
 ('Area of plane figures',R(r'area|perimeter|rectangle|triangle|trapezoid|parallelogram|polygon|region|hexagon|square|rhombus|circle')),
 ('Composite figures and unit conversion',R(r'.*')),
],
'Circles':[
 ('Tangent lines',R(r'tangent')),
 ('Equation of a circle',R(r'x\^\{?2\}?\s*\+\s*y\^\{?2|\(x\s*[-+]\s*\d+\)\^\{?2\}?\s*\+|center|equation of (?:a|the) circle|xy-plane')),
 ('Arc length and sector area',R(r'arc|sector|radian|central angle|segment|\\pi\}?\s*\\?(?:text)?\{?\s*(?:cm|m)')),
 ('Inscribed angles and chords',R(r'inscribed|chord|diameter|angle|secant|intersect|cyclic|quadrilateral')),
 ('Circle measurements',R(r'.*')),
],
'Lines, angles, and triangles':[
 ('Similar triangles',R(r'similar|\\sim|scale factor|ratio of|proportion|parallel to')),
 ('Congruence and special triangles',R(r'congruent|isosceles|equilateral|midsegment|median|centroid|altitude|angle bisector|pythag|right triangle')),
 ('Parallel lines and angle relationships',R(r'parallel|transversal|supplementary|complementary|vertical angle|exterior angle|interior angle|sum of the angles|polygon')),
 ('Triangle inequality and sides',R(r'.*')),
],
'Right triangles and trigonometry':[
 ('Special right triangles',R(r'30|45|60|special|isosceles right|equilateral')),
 ('Sine, cosine, tangent ratios',R(r'sin|cos|tan\b|\\tan|ratio|cosine|sine|complementary')),
 ('Pythagorean theorem applications',R(r'pythag|hypotenuse|legs?|diagonal|distance|ladder|ramp|height|shadow|cable|slant')),
 ('Radians and unit circle',R(r'.*')),
],
'Percentages':[
 ('Percent change and growth',R(r'increase|decrease|change|discount|markup|sale|growth|decay|depreciat|original|new price|tax|tip')),
 ('Percent of a quantity and parts',R(r'of the|percent of|\\%|%')),
 ('Percent in tables and context',R(r'.*')),
],
'Ratios, rates and units':[
 ('Unit conversion',R(r'convert|per hour|per minute|per second|km|mile|meter|metre|feet|gallon|liter|litre|kilogram|pound|units?')),
 ('Rates and proportional relationships',R(r'rate|speed|per |constant|proportion|inverse|vary')),
 ('Ratios and scale',R(r'ratio|scale|map|model|mixture|parts')),
 ('Density and composite rates',R(r'.*')),
],
'One-variable data':[
 ('Mean, median and mode',R(r'mean|median|mode|average')),
 ('Spread: range and standard deviation',R(r'standard deviation|range|spread|interquartile|variab|iqr')),
 ('Data displays and distributions',R(r'.*')),
],
'Two-variable data and scatterplots':[
 ('Line of best fit and prediction',R(r'best fit|regression|predict|trend|line of best')),
 ('Scatterplot and model choice',R(r'scatter|exponential|quadratic|linear model|model')),
 ('Tables and two-way data',R(r'.*')),
],
'Probability':[
 ('Conditional probability and two-way tables',R(r'given|conditional|table|two-way|survey|participants')),
 ('Basic and compound probability',R(r'.*')),
],
'Inference and margin of error':[
 ('Margin of error and confidence',R(r'margin|confidence|interval|plausible')),
 ('Sample estimates and populations',R(r'.*')),
],
'Statistical claims and studies':[
 ('Study design and causation',R(r'random assign|random sample|experiment|observational|cause|causal|conclusion')),
 ('Generalizing from samples',R(r'.*')),
],
}
def sub(skill,text):
    for name,rx in TAX[skill]:
        if rx.search(text): return name
    return TAX[skill][-1][0]

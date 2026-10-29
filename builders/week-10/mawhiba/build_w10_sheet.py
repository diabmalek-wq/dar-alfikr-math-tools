"""Mawhiba Unit 3 Activity 2 student worksheet, exactly 3 pages. Nothing pre-answered."""
from w9common import *
def inl(k, s=0.78): return eq(k, s, inline=True)
def img(path, w_mm, extra=""): return f'<img class="fig" src="{path}" style="width:{w_mm}mm;{extra}">'
HEAD = lambda small, h1, idb=False: HEADER + title(small, h1) + (IDBAR if idb else "")
FT = "Mawhiba Grade 9 · Unit 3 · Activity 2"
def R(n, h=None): return ('<div class="rule"' + (f' style="height:{h}mm"' if h else '') + '></div>') * n
CARDS = ["Number of people in a lift","Total weight of passengers","Temperature","Seedling growth","Time in months","Children’s heights","Mileage","Petrol consumption","Number of TVs","Life span","Time in hours","Virus multiplication","Time in years","Radioactive decay","Pressure","Wind speed","Amount of fertiliser applied to a crop whilst growing","The crop yield produced"]
ORDER = [2,13,0,9,6,17,4,3,10,15,8,1,14,5,12,11,16,7]
def p1():
    bank = "".join(f'<span style="border:1px solid var(--line);border-radius:1mm;padding:.5mm 1.6mm;background:#fff">{CARDS[i]}</span>' for i in ORDER)
    rows = "".join(f'<tr class="tt"><td class="l" style="width:7mm;text-align:center;height:9.2mm">{i}</td><td style="width:50mm;height:9.2mm"></td><td style="width:50mm"></td><td></td></tr>' for i in range(1, 10))
    return f"""{HEAD("Mawhiba Grade 9 · Unit 3 Linear Functions and Relations · Activity 2", "Paired Variables", True)}
<div class="grid g2" style="margin-bottom:2mm">
  <div class="card tint"><h2 class="p">Unit 3 learning objectives</h2>
    <ul style="font-size:7.6pt"><li>Apply prior knowledge of linear equations to construct and interpret lines of best fit to contextual data</li>
    <li>Use and evaluate inferences about the relationship between paired variables based on modelling data using linear relationships</li>
    <li>Compare mathematical linear relationships between variables to relationships between variables in the real world</li></ul></div>
  <div class="card tint"><h2 class="t">Advanced performance characteristics</h2>
    <ul style="font-size:7.6pt"><li>Tolerate ambiguity and be able to work with inexact relationships</li>
    <li>Show insight into the nature of different types of linear relationships in mathematics and science</li></ul></div>
</div>
<div class="need"><b>You will need</b> &nbsp; This sheet, a clear ruler, a sharp pencil, and a spreadsheet or GeoGebra if allowed. All data are model values.</div>
<div class="card" style="margin-bottom:2mm">
  <h2 class="p">Task 1 · Practice · Match the paired variables</h2>
  <p class="quote" style="margin-bottom:1mm"><b>Independent</b> variables answer the question “What do I change?” <b>Dependent</b> variables answer the question “What do I observe?” Match the cards into nine pairs, with one card as the independent variable and one as the dependent variable. There is more than one way of pairing the cards.</p>
  <div style="display:flex;flex-wrap:wrap;gap:1.4mm;font-size:7.6pt;margin-bottom:1.6mm">{bank}</div>
  <table class="cj"><tr><th></th><th>Independent variable<br><span style="text-transform:none">(what I change)</span></th><th>Dependent variable<br><span style="text-transform:none">(what I observe)</span></th><th>The context I chose and why</th></tr>{rows}</table>
  <p style="margin:1.4mm 0 .2mm"><b>Compare with another pair.</b> Which pairing was different from yours, and what context did they choose?</p>{R(1, 5.4)}
  <p style="margin:1.2mm 0 .2mm"><b>What if...?</b> A card could go with more than one partner. Which card, and what are the two contexts?</p>{R(1, 5.4)}
  <p class="footnote" style="margin-top:1mm"><b>Done when</b> all nine pairs say which variable you change and which you observe, and you can explain a context for each.</p>
</div>
{foot(FT, 1, 3)}"""
def p2():
    def pane(f, t, ctx):
        return (f'<div class="fc"><div class="top"><span class="n">{t}</span></div><div style="font-size:7pt;min-height:11mm;margin-bottom:.6mm">{ctx}</div>{img(f"fig/th_{f}_doc.png", 53)}</div>')
    vocab = "".join(f"<span>&#9744; {v}</span>" for v in ["exact linear relationship", "inexact linear relationship", "experimental errors", "limited assumptions", "complex assumptions"])
    rows = "".join(f'<tr class="tr2"><td class="l" style="width:8mm;text-align:center">{k}</td><td style="width:44mm"></td><td style="width:44mm"></td><td></td></tr>' for k in "ABC")
    return f"""{HEAD("Task 2 · Apply", "Exact or Inexact?")}
<div class="card" style="margin-bottom:2mm">
  <h2 class="t">Task 2 · Apply · Three graphs, three kinds of relationship</h2>
  <p class="quote" style="margin-bottom:1.2mm">Consider the 3 graphs and accompanying explanations. Talk to your partner and together make comments about the relationship you see in each diagram and the context described. Try to use this vocabulary:</p>
  <div class="val" style="margin-bottom:1.6mm">{vocab}</div>
  <div class="grid g3" style="gap:2mm">{pane("car","Graph A · Hiring a car in Jeddah","A car costs SAR 280 a day, the first 100 km is included, then SAR 0.80 for each extra km. The graph shows the cost for distances over 100 km.")}{pane("spr","Graph B · Stretching a spring","Masses are added to a spring and its length is measured with a ruler each time.")}{pane("fer","Graph C · Fertiliser on date palms","A farm in Al-Ahsa records the fertiliser used on each palm and the dates harvested from it.")}</div>
  <table class="cj" style="margin-top:2mm"><tr><th></th><th style="text-transform:none">Exact or inexact? Why?</th><th style="text-transform:none">Errors or assumptions</th><th style="text-transform:none">What the relationship tells me</th></tr>{rows}</table>
</div>
<div class="card" style="margin-bottom:1mm">
  <h2 class="p">Look closer at graph B</h2>
  <p style="margin:0 0 .4mm">Use a ruler to draw a line of best fit. Choose two points ON your line (they need not be dots).</p>
  <table class="cj"><tr><td class="l" style="width:36mm">{inl("lab_pt1", .7)}</td><td></td><td class="l" style="width:36mm">{inl("lab_pt2", .7)}</td><td></td></tr>
  <tr class="tr2"><td class="l">{inl("lab_m2", .7)}</td><td></td><td class="l">{inl("lab_c2", .7)}</td><td></td></tr>
  <tr class="tr2"><td class="l">{inl("lab_eqn", .7)}</td><td colspan="3"></td></tr></table>
  <p style="margin:1.4mm 0 .2mm"><b>Interpret.</b> What does the gradient mean in the context of the spring? What does the intercept mean?</p>{R(2, 5.4)}
  <p style="margin:1.2mm 0 .2mm"><b>What if...?</b> You hang 5 kg (5000 g) on the spring. What does your line predict, and should you trust it? Why?</p>{R(2, 5.4)}
  <p class="footnote" style="margin-top:1mm"><b>Done when</b> every graph is named exact or inexact with a reason, and you can interpret the gradient and intercept in context.</p>
</div>
{foot(FT, 2, 3)}"""
def p3():
    claims = [("A", "If the dots do not lie exactly on a line, there is no linear relationship.", "Does a model need to touch every dot to be useful?"),
              ("B", "Only one way of pairing the cards is correct.", "Did I say which context I chose?"),
              ("C", "The line for the spring is reliable for any mass.", "Does the spring still behave the same far beyond the readings?")]
    crow = "".join(f'<tr class="tt"><td class="l" style="width:8mm;text-align:center">{k}</td><td style="width:60mm"><b>{c}</b></td>'
                   f'<td style="width:30mm;font-size:7.2pt">&#9744; true &nbsp; &#9744; false<br>&#9744; sometimes</td><td style="font-size:7.2pt;color:#5A6B69"><i>Because&hellip;</i><br><i>Assumption I checked:</i> {a}</td></tr>' for k, c, a in claims)
    return f"""{HEAD("Judge it, then Apply", "Test It and Use It")}
<div class="card" style="margin-bottom:2mm">
  <h2 class="p">Judge the claims</h2>
  <p class="footnote" style="margin-bottom:1mm">Decide whether each claim is true, false or sometimes true. Use evidence from your own work. One counterexample is enough to show a claim is false.</p>
  <table class="cj">{crow}</table>
  <p style="margin:1.4mm 0 .2mm"><b>Which graph gave you the strongest evidence?</b> Was it exact, inexact, or one with complex assumptions? What made you decide?</p>{R(3, 6.4)}
</div>
<div class="card" style="margin-bottom:1mm">
  <h2 class="g">Apply and present · A fast charger near Jeddah</h2>
  <p style="margin-bottom:1mm">Model values, not real charger data. An electric car is plugged into a fast charger and the battery charge is recorded every 10 minutes.</p>
  <div class="grid" style="grid-template-columns:78mm 1fr;gap:3mm"><div>{img("fig/chg_doc.png", 78)}</div>
  <div style="font-size:7.8pt"><p><b>1</b> · Which variable is independent and which is dependent?</p>{R(2, 6.2)}
  <p><b>2</b> · Use the first five readings to draw a line and find its equation.</p>{R(3, 6.2)}
  <p><b>3</b> · Predict the charge after 25 minutes. Check on the graph.</p>{R(2, 6.2)}
  <p><b>4</b> · What if the car stays 90 minutes? Is the line still sensible? Say exact or inexact, and why.</p>{R(4, 6.2)}</div></div>
  <p class="footnote" style="margin-top:1.4mm"><b>My Mawhiba record.</b> Tick the value I showed today: &#9744; Inquiry &nbsp; &#9744; Risk taking &nbsp; &#9744; Perseverance &nbsp; &#9744; Collaboration &nbsp; &#9744; Concern for society &nbsp; Example: .........................................................</p>
</div>
{foot(FT, 3, 3)}"""
if __name__ == "__main__":
    ok = render([p1(), p2(), p3()], "U3A2_sheet"); print("OK" if ok else "FIX")

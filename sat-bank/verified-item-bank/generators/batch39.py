import numpy as np, math, itertools
from fractions import Fraction as Fr
SRC="House-authored, coverage-matched to a hard-SAT archetype in the thin skills of the gap analysis (archetype only; no source item, wording or numbers reproduced)."
EC="Problem-Solving and Data Analysis — Evaluating statistical claims: Observational studies and experiments"
INF="Problem-Solving and Data Analysis — Inference from sample statistics and margin of error"
PR="Problem-Solving and Data Analysis — Probability and conditional probability"
TV="Problem-Solving and Data Analysis — Two-variable data: Models and scatterplots"
NF="Advanced Math — Nonlinear functions"
NE="Advanced Math — Nonlinear equations in one variable and systems of equations in two variables"
LT="Geometry and Trigonometry — Lines, angles, and triangles"
I=[]
def add(id,skill,diff,q,rat,mis,opts=None,correct=None,ans=None):
    d=dict(id=id,skill=skill,diff=diff,q=q,rat=rat,mis=mis,opts=opts,correct=correct,ans=ans)
    if opts: assert len(set(opts))==4 and 0<=correct<4
    else: assert ans
    I.append(d)

# ---------------- Evaluating statistical claims ----------------
add("PS-133",EC,"Hard",
 r"A researcher recruited $120$ volunteers who responded to an online advertisement. She randomly assigned $60$ of them to study with method $X$ and $60$ to study with method $Y$ for a month. The method $X$ group had a higher mean score on a final test, and the difference was larger than would be expected from random assignment alone. Which conclusion is best supported by the study?",
 r"Random assignment supports a cause-and-effect conclusion, but the participants were volunteers and not a random sample of all students. So the conclusion can be drawn only for volunteers like those in the study.",
 r"Students think random assignment allows a conclusion about every student, or that volunteers make any causal statement impossible.",
 opts=[r"Method $X$ causes higher scores for all students.",r"Method $X$ caused higher scores for volunteers like those in the study.",r"Method $X$ is associated with higher scores, but no causal conclusion is possible.",r"The study provides no evidence about either method."],correct=1)
add("PS-134",EC,"Hard",
 r"A random sample of $500$ adults was selected from a large city, and each adult reported how many hours per week they exercise and how many hours they sleep each night. The adults who exercise more tend to sleep more. Which conclusion is best supported by this study?",
 r"The random sample lets the result be generalized to adults in the city, but no one was assigned to exercise, so the study shows association only.",
 r"Students see a random sample and jump to causation, or think the result cannot apply beyond the $500$ people sampled.",
 opts=[r"Exercising more causes adults in the city to sleep more.",r"Among adults in the city, exercise and sleep are positively associated, but exercise has not been shown to cause more sleep.",r"Among the $500$ adults only, exercise and sleep are associated; nothing can be said about the city.",r"Sleeping more causes adults in the city to exercise more."],correct=1)
add("PS-135",EC,"Medium",
 r"A website for a cycling club posted a poll asking, ``Should the city spend more on bike lanes?'' Of the $1{,}850$ people who chose to respond, $91\%$ voted yes. Which is the main reason the poll result should not be used to estimate the opinion of all city residents?",
 r"Respondents chose themselves, and visitors to a cycling club's site are not representative of all residents. A large number of responses does not fix this bias.",
 r"Students believe that a large sample ($1{,}850$) is enough to generalize.",
 opts=[r"The sample size is too large.",r"Respondents selected themselves and are likely to hold similar views.",r"The question has too few possible answers.",r"The poll was conducted online, and no online poll can be accurate."],correct=1)
add("PS-136",EC,"Medium",
 r"A random sample of $500$ adults reported their coffee consumption. The adults who drink coffee daily had a lower rate of a certain heart condition than those who do not. Which change to the study would make it possible to conclude that drinking coffee reduces the rate of the condition?",
 r"A causal conclusion needs random assignment: randomly choosing who drinks coffee and who does not balances other factors across the groups.",
 r"Students think more data or more measured variables turns an observational study into an experiment.",
 opts=[r"Increase the sample to $5{,}000$ adults.",r"Randomly assign the participants to drink coffee daily or not, then compare the rates.",r"Include only adults older than $40$.",r"Ask each adult about more lifestyle habits."],correct=1)

# ---------------- Inference / margin of error ----------------
add("PS-137",INF,"Hard",
 r"In a poll of a random sample of voters, $51\%$ said they support a proposed tax. The margin of error was $2.5\%$ at the $95\%$ confidence level. Based on the poll, which statement is best supported?",
 r"The plausible population values run from $51-2.5=48.5\%$ to $51+2.5=53.5\%$. Because $50\%$ is inside this interval, a majority is plausible but not established.",
 r"Students read $51>50$ and conclude a majority supports the tax.",
 opts=[r"A majority of all voters support the tax.",r"It is plausible that a majority support the tax, but less than half supporting it is also plausible.",r"Exactly $51\%$ of all voters support the tax.",r"Fewer than half of all voters support the tax."],correct=1)
M=3.2;e=0.4;N=18000
add("PS-138",INF,"Hard",
 r"A random sample of students at a university reported a mean of $3.2$ hours of study per day, with a margin of error of $0.4$ hours. The university has $18{,}000$ students. Based on the sample, what is the greatest total number of study hours per day that is plausible for the whole student body?",
 r"The plausible values of the population mean run from $3.2-0.4=2.8$ to $3.2+0.4=3.6$ hours. The greatest total is $3.6\cdot18{,}000=64{,}800$ hours.",
 r"Students multiply the sample mean by $18{,}000$ ($57{,}600$) and ignore the margin of error, or add $0.4$ to the total.",
 ans=r"$64{,}800$ (or $64800$)")
assert round((M+e)*N)==64800
add("PS-139",INF,"Medium",
 r"Two independent random samples were taken from the same population to estimate a proportion at the same confidence level. The first sample had $400$ members and a margin of error of $6\%$. The second sample had $1{,}600$ members. Which is most likely the margin of error for the second sample?",
 r"The margin of error shrinks in proportion to $\dfrac{1}{\sqrt n}$. The sample is $4$ times as large, so the margin of error is divided by $\sqrt4=2$, giving $3\%$.",
 r"Students divide by the sample ratio $4$ (getting $1.5\%$) instead of its square root.",
 opts=[r"$1.5\%$",r"$3\%$",r"$6\%$",r"$12\%$"],correct=1)
assert abs(6/math.sqrt(1600/400)-3)<1e-12
add("PS-140",INF,"Hard",
 r"A random sample of $500$ residents of Town $P$ gave an estimate of $30\%$ for the percent who favor a new park, with a margin of error of $4\%$. A random sample of $500$ residents of Town $Q$ gave an estimate of $38\%$, also with a margin of error of $4\%$. Which statement is best supported?",
 r"Town $P$ plausible values: $26\%$ to $34\%$. Town $Q$: $34\%$ to $42\%$. The intervals share the value $34\%$, so it is plausible that the two towns have the same percent. Neither a difference nor equality is established.",
 r"Students compare the two estimates ($30$ vs $38$) and declare a real difference.",
 opts=[r"Town $Q$ definitely has a greater percent in favor than Town $P$.",r"It is plausible that the percent in favor is the same in both towns.",r"The percent in favor in Town $P$ is exactly $4$ points less than that in Town $Q$.",r"It is not possible for the percents to be equal."],correct=1)
add("PS-141",INF,"Hard",
 r"A school has $1{,}200$ seniors and $2{,}800$ students in other grades. A random sample of $300$ seniors was surveyed, and an estimated $62\%$ plan to attend college, with a margin of error of $5\%$. Which statement is best supported by the survey?",
 r"The sample was drawn only from seniors, so the interval $57\%$ to $67\%$ applies to seniors at the school and not to all $4{,}000$ students.",
 r"Students apply the interval to the entire school population.",
 opts=[r"Between $57\%$ and $67\%$ of all students at the school plan to attend college.",r"It is plausible that between $57\%$ and $67\%$ of the seniors at the school plan to attend college.",r"Exactly $62\%$ of the seniors at the school plan to attend college.",r"Between $57\%$ and $67\%$ of the $300$ surveyed seniors plan to attend college."],correct=1)
add("PS-142",INF,"Hard",
 r"To estimate the number of fish in a lake, a biologist caught and tagged $150$ fish and released them. A week later she caught a random sample of $60$ fish from the lake, and $9$ of them were tagged. Assuming the sample is representative and the tagged fish mixed evenly, what is the best estimate of the number of fish in the lake?",
 r"The tagged fraction in the sample should match the tagged fraction in the lake: $\dfrac{9}{60}=\dfrac{150}{N}$, so $N=\dfrac{150\cdot60}{9}=1000$.",
 r"Students compute $150\cdot\dfrac{9}{60}=22.5$ (inverting the proportion) or $150+60-9=201$.",
 ans=r"$1000$")
assert Fr(150*60,9)==1000

# ---------------- Probability ----------------
add("PS-143",PR,"Hard",
 r"A company's customers were asked whether they renewed their contract. The results are shown in the table.\n\n| | Renewed | Did not renew |\n|---|---|---|\n| Plan $A$ | $84$ | $36$ |\n| Plan $B$ | $45$ | $35$ |\n\nIf one of the customers who did not renew is chosen at random, what is the probability that the customer was on Plan $B$?",
 r"There are $36+35=71$ customers who did not renew, and $35$ of them were on Plan $B$. The probability is $\dfrac{35}{71}\approx0.493$.",
 r"Students divide by all $200$ customers ($0.175$) or by Plan $B$'s total ($\tfrac{35}{80}$), conditioning on the wrong group.",
 ans=r"$\dfrac{35}{71}$ (or $0.493$)")
assert 36+35==71 and 84+36+45+35==200
pa,pb=Fr(2,5),Fr(1,2)
add("PS-144",PR,"Hard",
 r"Events $A$ and $B$ are independent. The probability of $A$ is $0.4$, and the probability that at least one of $A$ and $B$ occurs is $0.7$. What is the probability of $B$?",
 r"For independent events $P(A\text{ or }B)=P(A)+P(B)-P(A)P(B)$. So $0.7=0.4+b-0.4b$, giving $0.3=0.6b$ and $b=0.5$.",
 r"Students add the probabilities ($b=0.3$), forgetting the overlap term.",
 ans=r"$0.5$ (or $\dfrac12$)")
b_=Fr(1,2); assert Fr(2,5)+b_-Fr(2,5)*b_==Fr(7,10)
bag=[ 'R']*5+['B']*3
pairs=list(itertools.combinations(range(8),2)); same=sum(1 for i,j in pairs if bag[i]==bag[j])
assert Fr(same,len(pairs))==Fr(13,28)
add("PS-145",PR,"Hard",
 r"A bag holds $5$ red marbles and $3$ blue marbles. Two marbles are drawn at random, one after the other, without replacement. What is the probability that the two marbles are the same color?",
 r"Same color means both red or both blue: $\dfrac{5}{8}\cdot\dfrac47+\dfrac38\cdot\dfrac27=\dfrac{20+6}{56}=\dfrac{13}{28}$.",
 r"Students use replacement ($\tfrac{25}{64}+\tfrac{9}{64}=\tfrac{17}{32}$) or count only the red pair.",
 opts=[r"$\dfrac{5}{14}$",r"$\dfrac{13}{28}$",r"$\dfrac{17}{32}$",r"$\dfrac{15}{28}$"],correct=1)
assert Fr(17,32)!=Fr(13,28)
dice=[(a,b) for a in range(1,7) for b in range(1,7)]
cond=[(a,b) for a,b in dice if a%2==0 or b%2==0]; hit=[(a,b) for a,b in cond if a+b==8]
assert (len(hit),len(cond))==(3,27)
add("PS-146",PR,"Hard",
 r"Two fair six-sided dice are rolled. Given that at least one of the dice shows an even number, what is the probability that the sum of the two dice is $8$?",
 r"Among the $36$ outcomes, $9$ have both dice odd, so $27$ have at least one even die. Of the sums equal to $8$ ($(2,6),(3,5),(4,4),(5,3),(6,2)$), three include an even die. The probability is $\dfrac{3}{27}=\dfrac19$.",
 r"Students use all five outcomes with sum $8$ over $27$ ($\tfrac{5}{27}$) or divide by $36$.",
 ans=r"$\dfrac19$ (or $0.111$)")
car,bike,both,tot=240,180,70,500
assert tot-(car+bike-both)==150 and Fr(150,500)==Fr(3,10)
add("PS-147",PR,"Medium",
 r"Of $500$ residents surveyed, $240$ own a car, $180$ own a bicycle, and $70$ own both. If one of the surveyed residents is chosen at random, what is the probability that the resident owns neither a car nor a bicycle?",
 r"The residents owning at least one are $240+180-70=350$, so $500-350=150$ own neither. The probability is $\dfrac{150}{500}=0.3$.",
 r"Students forget to subtract the overlap and get $\dfrac{80}{500}$, or answer $\dfrac{350}{500}$.",
 ans=r"$0.3$ (or $\dfrac{3}{10}$)")
p60=Fr(3,10); v60=Fr(4,5); vn=Fr(1,2)
num=p60*v60; den=num+(1-p60)*vn
assert Fr(num,den)==Fr(24,59)
add("PS-148",PR,"Hard",
 r"In a town, $30\%$ of the residents are over $60$ years old. Of the residents over $60$, $80\%$ vote in elections; of the residents who are not over $60$, $50\%$ vote. A voter is chosen at random from all residents who vote. What is the probability that the voter is over $60$?",
 r"Per $100$ residents: voters over $60$ number $30\cdot0.8=24$; voters not over $60$ number $70\cdot0.5=35$. The probability is $\dfrac{24}{24+35}=\dfrac{24}{59}\approx0.407$.",
 r"Students answer $0.8$ (the share of over-$60$s who vote) or $0.3$ (the share of residents over $60$).",
 ans=r"$\dfrac{24}{59}$ (or $0.407$)")
assert Fr(90,120)/Fr(60,100)==Fr(5,4)
add("PS-149",PR,"Medium",
 r"In a trial, $90$ of $120$ patients given Drug $X$ improved, and $60$ of $100$ patients given Drug $Y$ improved. How many times as likely is a patient given Drug $X$ to improve as a patient given Drug $Y$?",
 r"The improvement rates are $\dfrac{90}{120}=0.75$ for $X$ and $\dfrac{60}{100}=0.6$ for $Y$. The ratio is $\dfrac{0.75}{0.6}=1.25$.",
 r"Students compare the counts ($\tfrac{90}{60}=1.5$) instead of the rates.",
 ans=r"$1.25$ (or $\dfrac54$)")

# ---------------- Two-variable data ----------------
add("PS-150",TV,"Medium",
 r"A teacher modeled the final score $y$ of students in a course with the line of best fit $\hat y=82-1.6x$, where $x$ is the number of days the student was absent. Which statement is the best interpretation of the number $82$ in this model?",
 r"The $y$-intercept is the predicted value when $x=0$: a student with no absences is predicted to score $82$.",
 r"Students read $82$ as the average score of the class or as the score lost per absence.",
 opts=[r"The predicted score decreases by $82$ for each day absent.",r"The predicted score of a student with no absences is $82$.",r"The mean score of all students in the class is $82$.",r"A student absent for $82$ days is predicted to score $0$."],correct=1)
X=np.arange(0,5); Y=8*1.5**X
cands={'A':lambda x:4*x+8,'B':lambda x:8*1.5**x,'C':lambda x:2*x**2+2*x+8,'D':lambda x:8*1.2**x}
fit={k:np.allclose(f(X),Y) for k,f in cands.items()}; assert fit=={'A':False,'B':True,'C':False,'D':False}
add("PS-151",TV,"Hard",
 r"The table shows values of $x$ and $y$ for a data set.\n\n| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |\n|---|---|---|---|---|---|\n| $y$ | $8$ | $12$ | $18$ | $27$ | $40.5$ |\n\nWhich equation fits all five pairs?",
 r"The ratios of consecutive $y$-values are all $\dfrac{12}{8}=\dfrac{18}{12}=1.5$, so $y=8(1.5)^x$ fits. The linear and quadratic options fail at $x=2$, where they give $16$ and $20$, and $8(1.2)^x$ gives $11.52$.",
 r"Students notice the first difference $4$ and choose a linear or quadratic model without testing the later values.",
 opts=[r"$y=4x+8$",r"$y=8(1.5)^x$",r"$y=2x^2+2x+8$",r"$y=8(1.2)^x$"],correct=1)
add("PS-152",TV,"Hard",
 r"A line of best fit for a data set is $\hat y=3.2x+14$. For the data point with $x=10$, the actual value is $y=51$. What is the residual for this point (actual value minus predicted value)?",
 r"The predicted value is $3.2(10)+14=46$. The residual is $51-46=5$.",
 r"Students reverse the subtraction (answer $-5$) or give the predicted value $46$.",
 ans=r"$5$")
assert 3.2*10+14==46.0
xs=np.arange(1,11,dtype=float); ys=2*xs+1
s0,i0=np.polyfit(xs,ys,1); s1,i1=np.polyfit(np.append(xs,11),np.append(ys,40),1)
assert abs(s0-2)<1e-9 and s1>s0 and i1<i0
add("PS-153",TV,"Hard",
 r"Ten data points lie exactly on the line $y=2x+1$, at $x=1,2,\ldots,10$. A new data point $(11,40)$, far above that line, is added. How does the least-squares line for all eleven points compare with the line $y=2x+1$?",
 r"The new point is above the line at the right end, so it pulls the right side of the line up. The slope increases above $2$, and the line pivots about the center of the data, so the $y$-intercept falls below $1$. (Computed: slope $\approx2.77$, intercept $\approx-2.09$.)",
 r"Students think an outlier at the right end raises both the slope and the intercept.",
 opts=[r"Greater slope and greater $y$-intercept",r"Greater slope and smaller $y$-intercept",r"Smaller slope and greater $y$-intercept",r"The same slope and the same $y$-intercept"],correct=1)
print("PS-153 refit",round(s1,2),round(i1,2))
add("PS-154",TV,"Medium",
 r"A model $y=0.85x+12$ was fitted to data in which $x$ ranged from $20$ to $80$. A student uses the model to predict $y$ when $x=150$. Which statement about this prediction is best?",
 r"The value $x=150$ is far outside the range of the data ($20$ to $80$), so using the model there is extrapolation and the prediction is unreliable even though the arithmetic is simple.",
 r"Students assume the line holds forever, or think any prediction is invalid.",
 opts=[r"It is reliable, because the model is linear.",r"It is less reliable, because $150$ is outside the range of the data.",r"It is impossible, because $y$ cannot be computed for $x>80$.",r"It is reliable, because the slope is positive."],correct=1)
add("PS-155",TV,"Hard",
 r"A least-squares line for a data set is $\hat y=1.5x+4$. The mean of the $x$-values is $10$. What is the mean of the $y$-values?",
 r"A least-squares line always passes through the point $(\bar x,\bar y)$ of the means. So $\bar y=1.5(10)+4=19$.",
 r"Students think the mean of $y$ cannot be found without the data.",
 ans=r"$19$")
add("PS-156",TV,"Hard",
 r"The residuals for the first four of five data points about a least-squares line are $-2$, $3$, $1$ and $-4$. What is the residual for the fifth point?",
 r"The residuals about a least-squares line sum to $0$. So $-2+3+1-4+r=0$, giving $r=2$.",
 r"Students think residuals should all be positive, or average to a nonzero value.",
 ans=r"$2$")
assert -2+3+1-4+2==0

# ---------------- Function composition and transformations ----------------
f=lambda x:x*x-4*x
assert (2,-4)==(2,f(2)) and f(-1+3)-2==-6
add("AM-288",NF,"Hard",
 r"The function $f$ is defined by $f(x)=x^2-4x$. The graph of $g(x)=f(x+3)-2$ is a parabola. What are the coordinates of its vertex?",
 r"The vertex of $f$ is at $x=2$, $f(2)=-4$, so $(2,-4)$. Replacing $x$ by $x+3$ shifts the graph $3$ units left and $-2$ shifts it $2$ units down, giving $(2-3,\,-4-2)=(-1,-6)$.",
 r"Students shift right for $x+3$, obtaining $(5,-6)$, or forget the vertical shift.",
 opts=[r"$(5,-6)$",r"$(-1,-6)$",r"$(-1,-2)$",r"$(1,-6)$"],correct=1)
F=lambda x:2*x+3; G=lambda x:x*x-1
co=np.roots([2-4,-12,1-8]) if False else None
# f(g)=2x^2+1 ; g(f)=4x^2+12x+8 ; equal: 2x^2+12x+7=0
r=np.roots([2,12,7]); assert all(abs(F(G(x))-G(F(x)))<1e-9 for x in r) and abs(sum(r)+6)<1e-9 and 144-56>0
add("AM-289",NF,"Hard",
 r"Let $f(x)=2x+3$ and $g(x)=x^2-1$. What is the sum of all real values of $x$ for which $f(g(x))=g(f(x))$?",
 r"$f(g(x))=2(x^2-1)+3=2x^2+1$ and $g(f(x))=(2x+3)^2-1=4x^2+12x+8$. Setting them equal gives $2x^2+12x+7=0$, which has two real solutions (discriminant $144-56>0$) with sum $-\dfrac{12}{2}=-6$.",
 r"Students compose in the wrong order or give the product $\tfrac72$.",
 ans=r"$-6$")
add("AM-290",NF,"Hard",
 r"The graph of $y=f(x)$ in the $xy$-plane has $x$-intercepts at $x=-2$ and $x=5$. The function $g$ is defined by $g(x)=f(2x)$. What are the $x$-intercepts of the graph of $y=g(x)$?",
 r"$g(x)=0$ when $2x=-2$ or $2x=5$, so $x=-1$ or $x=\dfrac52$. Replacing $x$ by $2x$ compresses the graph horizontally by a factor of $2$.",
 r"Students double the intercepts ($-4$ and $10$), as if the graph were stretched.",
 opts=[r"$x=-4$ and $x=10$",r"$x=-1$ and $x=\dfrac52$",r"$x=0$ and $x=3$",r"$x=-2$ and $x=\dfrac52$"],correct=1)
fm=lambda x:(x-3)**2-8
xs_=np.linspace(-20,20,400001); gv=-fm(xs_-2)+5
assert abs(gv.max()-13)<1e-6
add("AM-291",NF,"Hard",
 r"The function $f$ has the graph of a parabola that opens upward with vertex $(3,-8)$. The function $g$ is defined by $g(x)=-f(x-2)+5$. What is the maximum value of $g$?",
 r"The least value of $f$ is $-8$. Then $-f$ has greatest value $8$, and shifting horizontally does not change it. Adding $5$ gives $8+5=13$.",
 r"Students take $-8+5=-3$ or apply the horizontal shift to the value.",
 ans=r"$13$")
fT={1:3,2:4,3:1,4:2}; gT={1:4,2:1,3:2,4:3}
finv={v:k for k,v in fT.items()}; assert gT[finv[gT[3]]]==3
add("AM-292",NF,"Hard",
 r"The functions $f$ and $g$ are defined for the values in the table.\n\n| $x$ | $1$ | $2$ | $3$ | $4$ |\n|---|---|---|---|---|\n| $f(x)$ | $3$ | $4$ | $1$ | $2$ |\n| $g(x)$ | $4$ | $1$ | $2$ | $3$ |\n\nWhat is the value of $g\left(f^{-1}(g(3))\right)$?",
 r"$g(3)=2$. The value $f^{-1}(2)$ is the input where $f$ equals $2$, which is $x=4$. Then $g(4)=3$.",
 r"Students read $f^{-1}(2)$ as $f(2)=4$ or as $\dfrac{1}{f(2)}$.",
 ans=r"$3$")
cases=[lambda x:x**3,lambda x:x**5-x]
for h in cases:
    assert all(abs(h(-x)+h(x))<1e-9 for x in (1,2,3.5))
    assert all(abs((lambda y:y**2)(h(-x))-(lambda y:y**2)(h(x)))<1e-9 for x in (1,2,3.5))
add("AM-293",NF,"Hard",
 r"The function $f$ is odd, which means $f(-x)=-f(x)$ for every $x$. Which of the following functions must be even, meaning $h(-x)=h(x)$ for every $x$?",
 r"Squaring removes the sign: $[f(-x)]^2=[-f(x)]^2=[f(x)]^2$, so $[f(x)]^2$ is even. The function $f(f(x))$ is odd, $f(x)+x$ is odd, and $f(x)+1$ is neither.",
 r"Students think a composition of odd functions is even, or confuse the two types.",
 opts=[r"$f(x)+1$",r"$[f(x)]^2$",r"$f(f(x))$",r"$f(x)+x$"],correct=1)
fq=lambda x:(x-1)*(x-5)
assert fq(-2)+4==25
add("AM-294",NF,"Medium",
 r"The function $f$ is defined by $f(x)=(x-1)(x-5)$. The graph of $g$ is the reflection of the graph of $f$ across the $y$-axis, shifted up $4$ units. What is the value of $g(2)$?",
 r"Reflecting across the $y$-axis gives $f(-x)$, and shifting up $4$ gives $g(x)=f(-x)+4$. Then $g(2)=f(-2)+4=(-3)(-7)+4=25$.",
 r"Students compute $f(2)+4=1$ (no reflection) or reflect across the $x$-axis.",
 ans=r"$25$")
# domain of f(g(x)), f=sqrt(x-1), g=x^2-5 : x^2>=6
for x in (-3,-2.5,2.5,3): assert (x*x-5-1>=0)
for x in (-2,0,2): assert not (x*x-5-1>=0)
add("AM-295",NF,"Hard",
 r"Let $f(x)=\sqrt{x-1}$ and $g(x)=x^2-5$. Which describes all real values of $x$ for which $f(g(x))$ is defined?",
 r"$f(g(x))=\sqrt{x^2-5-1}=\sqrt{x^2-6}$, which needs $x^2\ge6$, so $x\le-\sqrt6$ or $x\ge\sqrt6$.",
 r"Students use the domain of $f$ ($x\ge1$) or of $g$ (all reals) alone, or solve $x^2\ge6$ as $-\sqrt6\le x\le\sqrt6$.",
 opts=[r"$x\ge1$",r"$x\le-\sqrt6$ or $x\ge\sqrt6$",r"$-\sqrt6\le x\le\sqrt6$",r"all real numbers"],correct=1)
fi=Fr(16,3); assert Fr(2*fi+1)/(fi-3)==5
add("AM-296",NF,"Hard",
 r"The function $f$ is defined by $f(x)=\dfrac{2x+1}{x-3}$ for $x\ne3$. What is the value of $f^{-1}(5)$?",
 r"$f^{-1}(5)$ is the input $x$ for which $f(x)=5$. Solve $\dfrac{2x+1}{x-3}=5$: $2x+1=5x-15$, so $3x=16$ and $x=\dfrac{16}{3}$.",
 r"Students compute $f(5)=\dfrac{11}{2}$ or the reciprocal $\dfrac{1}{f(5)}$.",
 ans=r"$\dfrac{16}{3}$ (or $5.333$)")
assert 3*(-2)+5==-1
add("AM-297",NF,"Hard",
 r"The graph of $y=f(x)$ passes through the point $(4,-2)$. Which point must lie on the graph of $y=3f(x-1)+5$?",
 r"If $x-1=4$, then $x=5$ and $y=3f(4)+5=3(-2)+5=-1$. So $(5,-1)$ lies on the graph.",
 r"Students shift left to $x=3$ or apply the vertical changes in the wrong order.",
 opts=[r"$(3,-1)$",r"$(5,-1)$",r"$(5,11)$",r"$(3,11)$"],correct=1)

# ---------------- Sum and product of solutions ----------------
k=Fr(13,4); rr=np.roots([2,-7,float(k)]); assert abs(sum(rr**2)-9)<1e-9 and 49-8*k>0
add("AM-298",NE,"Hard",
 r"The equation $2x^2-7x+k=0$, where $k$ is a constant, has two real solutions $r$ and $s$ with $r^2+s^2=9$. What is the value of $k$?",
 r"By Vieta, $r+s=\dfrac72$ and $rs=\dfrac k2$. Then $r^2+s^2=(r+s)^2-2rs=\dfrac{49}{4}-k=9$, so $k=\dfrac{13}{4}$. The discriminant $49-8k=23>0$, so the solutions are real.",
 r"Students use $r^2+s^2=(r+s)^2$ and get $k=0$, or forget the factor $2$ on $rs$.",
 ans=r"$\dfrac{13}{4}$ (or $3.25$)")
p,q=-6,5; rt=np.roots([1,p,q]); assert sorted(rt)==[1,5]
assert -(2*rt.sum())==-12 and 4*rt.prod()==20 and -12+20==8
add("AM-299",NE,"Hard",
 r"The solutions of $x^2-6x+5=0$ are $r$ and $s$. The equation $x^2+ax+b=0$ has solutions $2r$ and $2s$. What is the value of $a+b$?",
 r"$r+s=6$ and $rs=5$. The new solutions have sum $12$ and product $4\cdot5=20$, so $a=-12$ and $b=20$. Then $a+b=8$.",
 r"Students double the product as well ($b=10$) or keep the sign of $a$ wrong ($a=12$).",
 ans=r"$8$")
sol=[x for x in (6,Fr(4,3)) if abs(2*x-5)==x+1]; assert len(sol)==2 and sum(sol)==Fr(22,3)
add("AM-300",NE,"Hard",
 r"What is the sum of all solutions of the equation $|2x-5|=x+1$?",
 r"Case $2x-5=x+1$ gives $x=6$. Case $2x-5=-(x+1)$ gives $3x=4$ and $x=\dfrac43$. Both satisfy $x+1\ge0$ and the original equation, so the sum is $6+\dfrac43=\dfrac{22}{3}$.",
 r"Students keep only one case or reject $\tfrac43$ as extraneous without checking.",
 ans=r"$\dfrac{22}{3}$ (or $7.333$)")
ra=np.roots([1,0,-5,0,4]); assert abs(np.prod(ra)-4)<1e-9
add("AM-301",NE,"Hard",
 r"What is the product of all real solutions of $x^4-5x^2+4=0$?",
 r"Let $u=x^2$: $u^2-5u+4=0$ gives $u=1$ or $u=4$. So $x=\pm1$ or $x=\pm2$, and the product is $(1)(-1)(2)(-2)=4$.",
 r"Students answer $0$ (the sum) or $\pm$ only the positive roots ($2$).",
 ans=r"$4$")
xs2=[x for x in (1,2) if abs(2**(2*x)-6*2**x+8)<1e-9]; assert xs2==[1,2]
add("AM-302",NE,"Hard",
 r"What is the sum of all real solutions of $2^{2x}-6\cdot2^{x}+8=0$?",
 r"Let $u=2^x$: $u^2-6u+8=0$ gives $u=2$ or $u=4$. So $x=1$ or $x=2$, and the sum is $3$.",
 r"Students add the values of $u$ ($2+4=6$).",
 ans=r"$3$")

# ---------------- Similar triangles and area ratios ----------------
assert 24*5//3==40
add("GT-226",LT,"Hard",
 r"Triangle $ABC$ is similar to triangle $DEF$. The area of triangle $ABC$ is $36$ and the area of triangle $DEF$ is $100$. The perimeter of triangle $ABC$ is $24$. What is the perimeter of triangle $DEF$?",
 r"The ratio of areas is $\dfrac{36}{100}$, so the ratio of lengths is $\dfrac{6}{10}=\dfrac35$. The perimeter of $DEF$ is $24\cdot\dfrac53=40$.",
 r"Students use the area ratio directly and get $24\cdot\dfrac{100}{36}\approx66.7$.",
 ans=r"$40$")
assert Fr(2,5)**2==Fr(4,25) and 20*Fr(25,4)==125 and 125-20==105
add("GT-227",LT,"Hard",
 r"In triangle $ABC$, point $D$ lies on $\overline{AB}$ and point $E$ lies on $\overline{AC}$ so that $\overline{DE}$ is parallel to $\overline{BC}$. If $AD:DB=2:3$ and the area of triangle $ADE$ is $20$, what is the area of quadrilateral $DBCE$?",
 r"$AD:AB=2:5$, so the triangles $ADE$ and $ABC$ are similar with area ratio $\dfrac{4}{25}$. The area of $ABC$ is $20\cdot\dfrac{25}{4}=125$, so the quadrilateral has area $125-20=105$.",
 r"Students use the ratio $2:3$ for the areas ($30$ or $50$) instead of squaring $2:5$.",
 ans=r"$105$")
assert 15*3//5==9
add("GT-228",LT,"Medium",
 r"Two similar triangles have areas $18$ and $50$. The altitude to the longest side of the larger triangle is $15$. What is the corresponding altitude of the smaller triangle?",
 r"The area ratio is $\dfrac{18}{50}=\dfrac{9}{25}$, so lengths are in ratio $\dfrac35$. The smaller altitude is $15\cdot\dfrac35=9$.",
 r"Students use the area ratio $\tfrac{9}{25}$ for lengths and get $5.4$.",
 opts=[r"$5.4$",r"$9$",r"$10.8$",r"$12.5$"],correct=1)
AD=20/math.sqrt(2); assert round(AD,1)==14.1
add("GT-229",LT,"Hard",
 r"In triangle $ABC$, point $D$ is on $\overline{AB}$ and point $E$ is on $\overline{AC}$ with $\overline{DE}\parallel\overline{BC}$. The segment $\overline{DE}$ divides the triangle into two regions of equal area. If $AB=20$, what is the length of $\overline{AD}$, to the nearest tenth?",
 r"Triangle $ADE$ has half the area of $ABC$, so $\left(\dfrac{AD}{AB}\right)^2=\dfrac12$ and $AD=\dfrac{20}{\sqrt2}=10\sqrt2\approx14.1$.",
 r"Students answer $10$, halving the length instead of the area.",
 ans=r"$14.1$")
assert 24*Fr(25,4)==150
add("GT-230",LT,"Hard",
 r"A right triangle has legs of length $6$ and $8$. A larger, similar right triangle has area $150$. What is the length of the hypotenuse of the larger triangle?",
 r"The smaller triangle has area $24$ and hypotenuse $10$. The area ratio is $\dfrac{150}{24}=\dfrac{25}{4}$, so the scale factor is $\dfrac52$ and the hypotenuse is $10\cdot\dfrac52=25$.",
 r"Students use the area ratio as the scale factor ($62.5$).",
 ans=r"$25$")
assert Fr(144,9)==16
add("GT-231",LT,"Hard",
 r"A square pyramid has a base with area $144$. A plane parallel to the base cuts the pyramid at a point one-third of the way from the apex to the base, forming a smaller square cross-section. What is the area of the cross-section?",
 r"The cross-section is similar to the base with scale factor $\dfrac13$, so its area is $144\cdot\dfrac19=16$.",
 r"Students use the scale factor itself ($48$) for the area.",
 ans=r"$16$")

# ---------- replacements for archetypes already in the bank ----------
fe=lambda x:(x-4)**2-8; assert fe(0)==8 and fe(2)==-4
add("AM-R1",NF,"Hard",
 r"The graph of the quadratic function $f$ has vertex $(4,-8)$ and passes through the point $(0,8)$. The function $g$ is defined by $g(x)=f(2x)$. What is the value of $g(1)$?",
 r"Write $f(x)=a(x-4)^2-8$. Since $f(0)=16a-8=8$, $a=1$. Then $g(1)=f(2)=(2-4)^2-8=-4$.",
 r"Students halve the input instead of doubling it ($f(0.5)$), or substitute into the vertex form without finding $a$.",
 ans=r"$-4$")
ff=lambda x:(x-1)*(x-6); g3=lambda x:ff(3-x)
zs=[x for x in range(-10,10) if g3(x)==0]; assert zs==[-3,2]
add("AM-R2",NF,"Hard",
 r"The graph of $y=f(x)$ has $x$-intercepts at $x=1$ and $x=6$. The function $g$ is defined by $g(x)=f(3-x)$. What is the greatest $x$-intercept of the graph of $y=g(x)$?",
 r"$g(x)=0$ when $3-x=1$ or $3-x=6$, so $x=2$ or $x=-3$. The graph of $g$ is a reflection in the $y$-axis followed by a shift of $3$ units to the right, so the greatest intercept is $2$.",
 r"Students solve $x-3=1$ and $x-3=6$ and answer $9$, or treat $3-x$ as a plain shift.",
 ans=r"$2$")
ev_=7; assert 2*7==14 and 2*2==4 and 14+4==18
add("AM-R3",NF,"Hard",
 r"The function $f$ is even, so $f(-x)=f(x)$ for every $x$. The function $g$ is defined by $g(x)=f(x)+f(-x)$. If $f(3)=7$ and $f(-5)=2$, what is the value of $g(3)+g(5)$?",
 r"Since $f$ is even, $g(x)=2f(x)$. Then $g(3)=14$ and $g(5)=2f(5)=2f(-5)=4$, so the sum is $18$.",
 r"Students treat $f(-x)$ as $-f(x)$ (so $g=0$) or cannot find $f(5)$.",
 ans=r"$18$")
r_=np.roots([1,-7,3]); r_=np.roots([1,-5,2]); assert abs(r_[0]/r_[1]+r_[1]/r_[0]-21/2)<1e-9
add("AM-R4",NE,"Hard",
 r"The solutions of $x^2-5x+2=0$ are $r$ and $s$. What is the value of $\dfrac{r}{s}+\dfrac{s}{r}$?",
 r"By Vieta, $r+s=5$ and $rs=2$. Then $\dfrac rs+\dfrac sr=\dfrac{r^2+s^2}{rs}=\dfrac{(r+s)^2-2rs}{rs}=\dfrac{25-4}{2}=\dfrac{21}{2}$.",
 r"Students compute $\dfrac{r+s}{rs}=\dfrac52$ (the sum of reciprocals).",
 ans=r"$\dfrac{21}{2}$ (or $10.5$)")
zz=np.roots([1,-7,14,-8]); assert abs(sum(zz**2)-21)<1e-9
add("AM-R5",NE,"Hard",
 r"The polynomial $p(x)=x^3-7x^2+14x-8$ has three real zeros. What is the sum of the squares of the zeros?",
 r"By Vieta, the zeros add to $7$ and the sum of the pairwise products is $14$. So the sum of squares is $7^2-2(14)=21$. (Check: the zeros are $1,2,4$, and $1+4+16=21$.)",
 r"Students answer $49$ ($7^2$) or $7$, using the sum of the zeros.",
 ans=r"$21$")
DROP={"AM-288","AM-289","AM-291","AM-299","AM-300"}
I[:]=[it for it in I if it['id'] not in DROP]
cnt={'A':315,'AM':287,'GT':225,'PS':132}
for it in I:
    p=it['id'].split('-')[0]; cnt[p]+=1; it['id']=f"{p}-{cnt[p]}"
print(len(I),[it['id'] for it in I][:3],cnt)

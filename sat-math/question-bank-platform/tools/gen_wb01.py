import json, itertools, math, statistics as st
from fractions import Fraction as F
items=[]
D_PS='Problem-Solving and Data Analysis'
def mc(lv,dom,skill,sub,q,correct,dis,steps):
    n=len(items)+1
    pos=n%4
    opts=list(dis); opts.insert(pos,correct)
    items.append(dict(id=f'WB-{n:03d}',src_q=n,lv=lv,mc=True,domain=dom,skill=skill,sub=sub,q=q,opts=opts,key=pos,steps=steps))
def spr(lv,dom,skill,sub,q,ans,disp,steps):
    n=len(items)+1
    items.append(dict(id=f'WB-{n:03d}',src_q=n,lv=lv,mc=False,domain=dom,skill=skill,sub=sub,q=q,key=ans,disp=disp,steps=steps))

# 1 histogram median bin
bins=[6,14,18,8,4]; assert sum(bins)==50
cum=list(itertools.accumulate(bins)); assert cum[1]<25<=cum[2]  # 25th,26th in third bin
mc('M',D_PS,'One-variable data','Data displays and distributions',
 'A histogram shows the commute times, in minutes, of $50$ employees at a Jeddah logistics park. The bars cover $0$ to $10$, $10$ to $20$, $20$ to $30$, $30$ to $40$ and $40$ to $50$ minutes, with $6$, $14$, $18$, $8$ and $4$ employees respectively. Each bar includes its left endpoint but not its right endpoint. Which statement must be true?',
 'The median commute time is at least $20$ minutes and less than $30$ minutes.',
 ['The mean commute time is exactly $23$ minutes.','The most common single commute time is $25$ minutes.','The range of the commute times is exactly $50$ minutes.'],
 ['Add bar heights: $6$, $20$, $38$, so the $25$th and $26$th values both fall in the third bar.','Median of $50$ values is the mean of the $25$th and $26$th, which are in $[20,30)$.','Trap: bar midpoints give about $23$ for the mean, but grouped data cannot give the exact mean, mode or range.'])

# 2 box plots
A=dict(mn=12,q1=20,md=30,q3=44,mx=60); B=dict(mn=5,q1=22,md=28,q3=38,mx=80)
assert A['q3']-A['q1']>B['q3']-B['q1'] and A['mx']-A['mn']<B['mx']-B['mn'] and A['md']>B['md']
mc('H',D_PS,'One-variable data','Data displays and distributions',
 'Two box plots summarize the daily visitors, in hundreds, to two Red Sea resorts. Resort $A$: minimum $12$, first quartile $20$, median $30$, third quartile $44$, maximum $60$. Resort $B$: minimum $5$, first quartile $22$, median $28$, third quartile $38$, maximum $80$. Which statement is supported by the box plots?',
 'Resort $A$ has the greater interquartile range, and resort $B$ has the greater range.',
 ['Resort $B$ has the greater median and the greater interquartile range.','Resort $A$ has the greater range, because its box is longer.','More than half of the days at resort $A$ had more than $30$ hundred visitors.'],
 ['IQR: $A$ is $44-20=24$, $B$ is $38-22=16$.','Range: $A$ is $60-12=48$, $B$ is $80-5=75$.','Trap: a longer box means larger IQR, not larger range; exactly half the values lie above the median, never more than half.'])

# 3 median from frequency table SPR
vals=[5,6,7,8]; fr=[2,4,9,5]; data=sum(([v]*f for v,f in zip(vals,fr)),[])
assert len(data)==20 and st.median(data)==7
spr('M',D_PS,'One-variable data','Data displays and distributions',
 'A frequency table shows the scores of $20$ students on a quiz marked out of $8$: a score of $5$ occurred $2$ times, a score of $6$ occurred $4$ times, a score of $7$ occurred $9$ times and a score of $8$ occurred $5$ times. What is the median score?',
 7,'7',
 ['Type the list in Desmos: <code>L=[5,5,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8]</code> then <code>median(L)</code> returns $7$.','By hand: cumulative counts are $2$, $6$, $15$, $20$, so the $10$th and $11$th values are both $7$.','Trap: the middle of the four listed scores is $6.5$, and the mean is $6.85$; neither is the median.'])

# 4 outlier effect
base=[22,25,27,28,30,33]; new=base+[120]
ch={'mean':abs(st.mean(new)-st.mean(base)),'median':abs(st.median(new)-st.median(base)),'range':(max(new)-min(new))-(max(base)-min(base)),'sd':abs(st.pstdev(new)-st.pstdev(base))}
assert min(ch,key=ch.get)=='median'
mc('M',D_PS,'One-variable data','Data displays and distributions',
 'The weekly rainfall, in millimeters, recorded at six weather stations near Abha is $22$, $25$, $27$, $28$, $30$ and $33$. A seventh station reports $120$. Which of the following changes the least, in value, when the seventh station is added?',
 'The median',['The mean','The range','The standard deviation'],
 ['Median goes from $27.5$ to $28$, a change of $0.5$.','Mean rises from about $27.5$ to $40.7$; the range from $11$ to $98$; the standard deviation grows many times over.','Trap: the median depends on rank, not on how extreme the new value is.'])

# 5 add a value equal to the mean
mc('M',D_PS,'One-variable data','Spread: range and standard deviation',
 'A data set has $12$ values with a mean of $40$ and a standard deviation of $6$. A new value of $40$ is added to the data set. Which statement about the new data set is true?',
 'The mean stays at $40$ and the standard deviation decreases.',
 ['The mean stays at $40$ and the standard deviation stays at $6$.','The mean stays at $40$ and the standard deviation increases.','The mean increases and the standard deviation decreases.'],
 ['The new value equals the mean, so the sum of values over $13$ still gives a mean of $40$.','The new value has deviation $0$ from the mean, so the sum of squared deviations is unchanged while the count grows.','Spread per value shrinks, so the standard deviation decreases (about $5.77$ if $6$ was the population value).'])
assert abs(math.sqrt(12*36/13)-5.77)<0.01

# 6 range casework SPR
best=None
for a in range(1,12):
  for b in range(a,12):
    for d in range(11,40):
      for e in range(d,60):
        arr=[a,b,11,d,e]
        if sum(arr)!=60: continue
        c=st.multimode(arr)
        if c==[9]:
          r=e-a
          if best is None or r>best: best=r
assert best==10
spr('H',D_PS,'One-variable data','Spread: range and standard deviation',
 'Five positive integers, listed in order from least to greatest, have a mean of $12$, a median of $11$ and a unique mode of $9$. What is the greatest possible range of the five integers?',
 10,'10',
 ['Sum is $60$. The median is the third value, $11$. The mode $9$ must appear at least twice, and only the first two slots can hold values below $11$, so they are both $9$.','The last two values add to $60-9-9-11=31$. A second $11$ would tie the mode, so the fourth value is at least $12$ and the fifth is at most $19$.','Range is $19-9=10$. Trap: letting the fourth value equal $11$ creates a second mode.'])

# 7 transform mean + sd
m,s=20,3.2; nm=2.5*m-4; ns=2.5*s; assert nm==46 and abs(ns-8)<1e-9
spr('M',D_PS,'One-variable data','Spread: range and standard deviation',
 'The monthly electricity use, in kilowatt hours, of a group of homes has a mean of $20$ and a standard deviation of $3.2$. A new variable is formed by multiplying each value by $2.5$ and then subtracting $4$. What is the sum of the mean and the standard deviation of the new variable?',
 54,'54',
 ['New mean: $2.5(20)-4=46$.','New standard deviation: only the multiplier acts, so $2.5(3.2)=8$ (the subtraction does not change spread).','Sum is $46+8=54$. Trap: subtracting $4$ from the standard deviation gives $46$ or $50$.'])

# 8 exponential table
ys=[100*1.1**k for k in range(5)]
assert all(abs(ys[i+1]/ys[i]-1.1)<1e-9 for i in range(4))
mc('M',D_PS,'Two-variable data and scatterplots','Scatterplot and model choice',
 'The table gives the estimated number of followers, in thousands, of a Saudi football club\'s account $x$ years after it launched: $x=0$: $100$; $x=1$: $110$; $x=2$: $121$; $x=3$: $133.1$; $x=4$: $146.41$. Which function best models these data?',
 '$y=100(1.1)^x$',['$y=100+10x$','$y=100(0.9)^x$','$y=100+10x+x^2$'],
 ['Ratios of consecutive values are all $1.1$, so growth is exponential with starting value $100$.','Differences ($10$, $11$, $12.1$, $13.31$) are not constant, ruling out the linear model.','Trap: a base below $1$ is decay, and a quadratic does not match the constant ratio.'])

# 9 residual plot
mc('M',D_PS,'Two-variable data and scatterplots','Scatterplot and model choice',
 'A line of best fit is used to model the relationship between the age of a date palm and its yearly yield. The residual plot for the line shows the residuals forming a clear U shape, positive for the youngest and oldest palms and negative for the middle-aged palms. Which conclusion is best supported?',
 'A linear model is not appropriate, and a quadratic model would likely fit better.',
 ['The linear model is appropriate because the residuals have a mean of about zero.','The linear model is appropriate because the U shape shows the data are random.','An exponential decay model would fit best because the residuals are positive at both ends.'],
 ['A good linear fit has residuals scattered randomly around zero with no pattern.','A systematic U shape means the data curve; the residuals are positive at both ends and negative in the middle, matching an upward-opening parabola.','Trap: residuals can average near zero even for a poor model.'])

# 10 quadratic return level SPR
f=lambda t:-0.5*t*t+6*t+20
assert f(0)==20 and f(12)==20 and all(f(t)!=20 for t in range(1,12))
spr('H',D_PS,'Two-variable data and scatterplots','Scatterplot and model choice',
 'A model estimates the number of visitors, in hundreds, at a Riyadh exhibition $t$ hours after it opens as $f(t)=-0.5t^2+6t+20$ for $0\\le t\\le 14$. The model predicts the same number of visitors at a later time as it did at opening. How many hours after opening is that?',
 12,'12',
 ['Set $f(t)=f(0)=20$ in Desmos: <code>y=-0.5x^2+6x+20</code> and <code>y=20</code>; the intersections are $x=0$ and $x=12$.','Algebra: $-0.5t^2+6t=0$ gives $t(-0.5t+6)=0$, so $t=0$ or $t=12$.','Trap: $t=6$ is the vertex (the peak), not the return time; the parabola is symmetric about $t=6$ so the return is at $2(6)=12$.'])

# 11 interpret base
mc('M',D_PS,'Two-variable data and scatterplots','Scatterplot and model choice',
 'The model $N(t)=250(1.08)^t$ estimates the number of members of a NEOM cycling club $t$ years after it was founded. Which statement is the best interpretation of $1.08$ in this context?',
 'The membership is estimated to increase by $8\\%$ each year.',
 ['The membership is estimated to increase by $1.08$ members each year.','The membership is estimated to increase by $108\\%$ each year.','The membership is estimated to increase by $80\\%$ each year.'],
 ['Each year multiplies the previous membership by $1.08$.','$1.08=1+0.08$, so growth is $8\\%$ per year of the current membership.','Trap: reading the base as an added amount ($1.08$ members) or as a percent ($108\\%$).'])

# 12 sample subgroup
est=3000*F(135,500); assert est==810
mc('M',D_PS,'Inference and margin of error','Sample estimates and populations',
 'A school district in Jeddah has $8{,}400$ students, of whom $3{,}000$ are in Grade $11$. A researcher randomly selects $500$ of the Grade $11$ students and finds that $135$ of them take the school bus. Based on the sample, which is the best estimate of the number of students in the district who take the school bus?',
 'It cannot be determined from the sample, but about $810$ of the Grade $11$ students are estimated to take the bus.',
 ['About $2{,}268$ students in the district take the bus.','About $810$ students in the district take the bus.','About $135$ students in the district take the bus.'],
 ['Sample proportion is $\\dfrac{135}{500}=0.27$, for Grade $11$ only.','Estimate for Grade $11$: $0.27(3000)=810$.','Trap: $0.27(8400)=2268$ generalizes beyond the sampled group; the sample came only from Grade $11$.'])

# 13 population count from interval
hi=24000*(F(40,100)+F(35,1000)); assert hi==10440
spr('M',D_PS,'Inference and margin of error','Sample estimates and populations',
 'In a random sample of $600$ residents of a city of $24{,}000$ residents, $40\\%$ said they would use a new public park. The margin of error for the estimate is $3.5\\%$. Based on the interval, what is the greatest number of residents of the city that plausibly would use the park?',
 10440,'10440',
 ['Interval for the population percent: $40\\%\\pm3.5\\%$, so the upper end is $43.5\\%$.','Compute <code>24000*0.435</code> in Desmos to get $10440$.','Trap: applying $3.5\\%$ to the sample size ($600$) or using $40\\%$ alone ($9600$).'])

# 14 bias vs margin
mc('H',D_PS,'Inference and margin of error','Sample estimates and populations',
 'A researcher asks $800$ randomly chosen fans, interviewed as they leave a stadium right after a home victory, whether they support increasing ticket prices. The results give a margin of error of $3\\%$. Which statement is most accurate about generalizing to all fans of the club?',
 'The margin of error accounts only for random sampling variation, so the results may be biased and should not be generalized to all fans.',
 ['The margin of error of $3\\%$ guarantees the estimate is within $3\\%$ of the true value for all fans.','Because $800$ is a large sample, the results can be safely generalized to all fans.','Because the fans were chosen randomly, the results can be generalized to all residents of the city.'],
 ['The margin of error measures random sampling error only.','Fans leaving after a victory are not representative of all fans (selection bias), so a small margin of error does not fix it.','Trap: large size and random selection within a biased frame do not protect against bias.'])

# 15 divisible p(2)
ksol=F(36+6-27,3); assert ksol==5
p=lambda x:x**3-4*x**2+ksol*x-6; assert p(3)==0 and p(2)==-4
spr('M','Advanced Math','Equivalent expressions','Polynomial division and remainder',
 'The polynomial $p(x)=x^3-4x^2+kx-6$, where $k$ is a constant, is divisible by $x-3$. What is the value of $p(2)$?',
 -4,'-4',
 ['Divisible by $x-3$ means $p(3)=0$: $27-36+3k-6=0$, so $k=5$.','Then $p(2)=8-16+10-6=-4$. Check in Desmos: <code>f(x)=x^3-4x^2+5x-6</code>, <code>f(2)</code>.','Trap: using $p(-3)=0$ (wrong sign of the root) gives a different $k$.'])

# 16 divisor 2x-1
mval=F(7)-(4*F(1,8)+6*F(1,4)-5*F(1,2)); assert mval==F(15,2)
spr('H','Advanced Math','Equivalent expressions','Polynomial division and remainder',
 'When $4x^3+6x^2-5x+m$ is divided by $2x-1$, the remainder is $7$. What is the value of $m$?',
 7.5,'7.5',
 ['Remainder equals the value at the root of the divisor: $2x-1=0$ gives $x=\\dfrac12$.','$4\\left(\\dfrac18\\right)+6\\left(\\dfrac14\\right)-5\\left(\\dfrac12\\right)+m=7$, so $-0.5+m=7$ and $m=7.5$.','Trap: evaluating at $x=2$ or $x=1$ (the divisor coefficient) instead of $x=\\dfrac12$.'])

# 17 quotient and remainder form
P=lambda x:(x-2)*(x**2+3*x+1)+5; assert P(3)==24
mc('M','Advanced Math','Equivalent expressions','Polynomial division and remainder',
 'When the polynomial $p(x)$ is divided by $x-2$, the quotient is $x^2+3x+1$ and the remainder is $5$. What is $p(3)$?',
 '$24$',['$19$','$5$','$29$'],
 ['Division statement: $p(x)=(x-2)(x^2+3x+1)+5$.','At $x=3$: $(1)(9+9+1)+5=19+5=24$.','Trap: forgetting the remainder gives $19$; $p(2)=5$ is the remainder, not $p(3)$.'])
assert 19!=24

# 18 cylinder scaling
fac=F(2)**2*F(1,2); assert fac==2
mc('M','Geometry and Trigonometry','Area and volume','Surface area and scaling',
 'A cylindrical water tank has radius $r$ and height $h$. A second tank has twice the radius and half the height of the first tank. The volume of the second tank is how many times the volume of the first tank?',
 '$2$',['$1$','$4$','$\\dfrac12$'],
 ['$V=\\pi r^2h$.','Second tank: $\\pi(2r)^2\\left(\\dfrac h2\\right)=\\pi\\cdot4r^2\\cdot\\dfrac h2=2\\pi r^2h$.','Trap: radius counts squared, so the factor is $4\\cdot\\dfrac12=2$, not $2\\cdot\\dfrac12=1$.'])

# 19 sphere SA 44% -> volume percent
r=math.sqrt(1.44); assert abs(r-1.2)<1e-12; vp=(1.2**3-1)*100; assert abs(vp-72.8)<1e-9
spr('H','Geometry and Trigonometry','Area and volume','Surface area and scaling',
 'The surface area of a spherical balloon increases by $44\\%$. By what percent does its volume increase?',
 72.8,'72.8',
 ['Surface area scales with $r^2$: $r^2$ factor is $1.44$, so the radius factor is $\\sqrt{1.44}=1.2$.','Volume scales with $r^3$: $1.2^3=1.728$, an increase of $72.8\\%$.','Trap: using $44\\%$ for the volume, or $1.44^{3/2}$ misread as $1.44\\cdot1.5$.'])

# 20 corner cube surface area
e=2; SA0=6*e*e; small=1; SA1=SA0-3*small**2+3*small**2; assert SA1==SA0
mc('H','Geometry and Trigonometry','Area and volume','Surface area and scaling',
 'A solid cube has edge length $e$. A smaller cube with edge length $\\dfrac e2$ is cut from one corner of the cube, leaving a solid with an L-shaped notch. By what percent does the total surface area of the solid change after the corner is removed?',
 'It does not change.',['It decreases by $12.5\\%$.','It decreases by $25\\%$.','It increases by $12.5\\%$.'],
 ['Original surface area: $6e^2$.','Cutting the corner removes three small square faces of area $\\left(\\dfrac e2\\right)^2$ each from the surface.','It exposes three new small square faces of the same total area, so the surface area is unchanged ($0\\%$ change). Trap: subtracting the removed volume fraction $12.5\\%$.'])

# 21 hollow pipe
vol=math.pi*(6**2-5**2)*2000; assert abs(vol/math.pi-22000)<1e-6
spr('H','Geometry and Trigonometry','Area and volume','Other area and volume problems',
 'A hollow steel pipe is $20$ meters long. Its outer diameter is $12$ centimeters and its wall is $1$ centimeter thick. The volume of steel in the pipe is $k\\pi$ cubic centimeters. What is the value of $k$?',
 22000,'22000',
 ['Convert length: $20$ m $=2000$ cm. Outer radius $6$ cm; inner radius $6-1=5$ cm.','Steel volume $=\\pi(6^2-5^2)(2000)=\\pi(11)(2000)=22000\\pi$.','Trap: using the diameter $12$ as the radius, or leaving the length in meters.'])

# 22 square minus inscribed circle
mc('M','Geometry and Trigonometry','Area and volume','Other area and volume problems',
 'A square tile with side length $12$ centimeters has a circle inscribed in it so that the circle touches all four sides. What is the area, in square centimeters, of the part of the tile that lies outside the circle?',
 '$144-36\\pi$',['$144-12\\pi$','$144-144\\pi$','$144-9\\pi$'],
 ['The circle touches all sides, so its diameter is $12$ and its radius is $6$.','Circle area $=\\pi(6)^2=36\\pi$; square area $=144$.','Region outside: $144-36\\pi$. Trap: using the diameter as the radius ($144\\pi$) or the circumference ($12\\pi$).'])

# 23 circle area x4 circumference
mc('M','Geometry and Trigonometry','Circles','Circle measurements',
 'Circle $A$ has a circumference of $18\\pi$. The area of circle $B$ is $4$ times the area of circle $A$. What is the circumference of circle $B$?',
 '$36\\pi$',['$72\\pi$','$18\\pi$','$324\\pi$'],
 ['Circle $A$: $2\\pi r=18\\pi$, so $r=9$ and its area is $81\\pi$.','Circle $B$ area $=324\\pi$, so $r^2=324$ and $r=18$.','Circumference of $B$ is $2\\pi(18)=36\\pi$. Trap: area scales by $4$ means radius scales by $2$, not by $4$.'])

# 24 wheel revolutions
rev=F(1100*100)/F(220); assert rev==500
spr('M','Geometry and Trigonometry','Circles','Circle measurements',
 'A wheel on a Riyadh Metro maintenance cart has a diameter of $70$ centimeters. Use $\\dfrac{22}{7}$ for $\\pi$. How many complete revolutions does the wheel make while the cart travels $1.1$ kilometers in a straight line?',
 500,'500',
 ['Circumference: $\\pi d=\\dfrac{22}{7}(70)=220$ cm.','Distance: $1.1$ km $=110{,}000$ cm.','Revolutions: $\\dfrac{110000}{220}=500$. Trap: forgetting to convert kilometers to centimeters or using the radius.'])

json.dump(items,open('/home/claude/wb/out/wb01.json','w'),indent=1,ensure_ascii=False)
json.dump([],open('/home/claude/wb/out/wb01_skip.json','w'))
print(len(items))

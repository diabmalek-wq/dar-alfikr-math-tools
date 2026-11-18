import json, itertools, math
from fractions import Fraction as F
CMP=["A is greater","B is greater","they are equal","not enough information"]
items=[]
def add(sig,code,lvl,stem,key,wrong,trick,why,traps,cmp=None):
    if cmp is not None: opts=CMP; ans=cmp
    else:
        opts=[key]+wrong; ans=0
        assert len(set(opts))==4,(sig,opts)
    assert len(traps)==3,sig
    items.append(dict(sig=sig,code=code,lvl=lvl,stem=stem,opts=opts,ans=ans,trick=trick,why=why,traps=traps))

# 1 alternating sum
s=sum(n if n%2 else -n for n in range(1,91)); assert s==-45
add("alternating-sign-sum","GAT-Q-ARI.5",2,"Find the value of 1 − 2 + 3 − 4 + … + 89 − 90.","−45",["45","−90","−44"],
 "group the terms in PAIRS — every (odd − next even) pair is −1, so count the pairs",
 "Pair the terms: (1−2) + (3−4) + … + (89−90). Each pair equals −1 and there are 90 ÷ 2 = 45 pairs, so the sum is −45.",
 ["A: got the size right but dropped the negative sign.","C: forgot to halve — treated all 90 terms as separate −1s.","D: miscounted the pairs by one."])
# 2 integers strictly between, crossing zero
c=len([n for n in range(-50,50) if -6<n<19]); assert c==24
add("count-integers-strictly-between","GAT-Q-ARI.1",2,"How many integers lie strictly between −6 and 19?","24",["25","26","13"],
 "endpoints are EXCLUDED, and a range that crosses zero must count the negative side too: 19 − (−6) − 1",
 "The integers are −5, −4, …, 18, and their count is 19 − (−6) − 1 = 24.",
 ["A: used 19 − (−6) = 25 and forgot to remove the gap-versus-count off-by-one.","B: counted both endpoints as well (inclusive).","C: subtracted 19 − 6 and ignored the negative side."])
# 3 evens between fractions
ev=[n for n in range(-100,200) if n%2==0 and F(41,4)<n<F(317,5)]; assert len(ev)==26
add("even-integers-between-fractions","GAT-Q-ARI.1",3,"How many even integers lie between 41/4 and 317/5?","26",["27","28","53"],
 "convert each fraction to a decimal first (10.25 and 63.4), then use the first and last even integers INSIDE the range",
 "41/4 = 10.25 and 317/5 = 63.4. The even integers inside are 12, 14, …, 62, so the count is (62 − 12) ÷ 2 + 1 = 26.",
 ["x: started the list at 10, which is below 10.25.","x: started at 10 and ended at 64, both outside the range.","x: counted every integer from 11 to 63, not only the even ones."])
# 4 power add equal terms
assert 3**20*3==3**21 and 3**20+3**20+3**20==3**21
add("power-add-equal-terms","GAT-Q-ARI.4",2,"Find the value of 3²⁰ + 3²⁰ + 3²⁰, written as a single power.","3²¹",["9²⁰","3⁶⁰","9²¹"],
 "adding THREE equal powers of 3 is 3 × 3²⁰ — add one to the exponent, never multiply the bases or the exponents",
 "3²⁰ + 3²⁰ + 3²⁰ = 3 × 3²⁰ = 3²¹.",
 ["A: added the bases (3 + 3 + 3 = 9) and kept the exponent.","B: multiplied the exponent by 3.","C: combined the bases to 9 and also raised the exponent."])
# 5 boundary insufficient (x^2+x vs 2x^2)
vals=set((x*x+x>2*x*x)-(x*x+x<2*x*x) for x in range(1,30)); assert vals=={0,-1}
add("compare-equal-at-boundary","GAT-Q-ALG.4",3,"x is a positive integer. Which quantity is greater?   A: x² + x   B: 2x²","",[],
 "test the SMALLEST allowed value — if the two quantities tie there but separate later, the answer is 'not enough information'",
 "At x = 1: A = 2 and B = 2, so they are equal. At x = 2: A = 6 and B = 8, so B is greater. The relationship changes with x, so it cannot be decided.",
 ["x: assumed the extra x always outweighs x².","x: tested only x = 2 or larger, where B wins.","x: tested only x = 1, where they tie."],cmp=3)
# 6 x^2 y = k, possible x+y
k=200; sums={x+k//(x*x) for x in range(1,15) if k%(x*x)==0}; assert sums=={201,52,13,12}
add("square-factor-pairs-sum","GAT-Q-ALG.1",3,"x and y are positive integers and x²y = 200. Which of the following could be the value of x + y?","13",["30","33","45"],
 "x² must be a perfect-square factor of 200 (1, 4, 25, 100) — list each and read off y",
 "x² must divide 200, so x² is 1, 4, 25 or 100. The pairs (x, y) are (1, 200), (2, 50), (5, 8) and (10, 2), giving sums 201, 52, 13 and 12. Only 13 is listed.",
 ["x: treated the condition as xy = 200 and took (10, 20).","x: treated the condition as xy = 200 and took (8, 25).","x: treated the condition as xy = 200 and took (5, 40)."])
# 7 different colours without replacement
red,grn=6,4; tot=red+grn
p=F(red,tot)*F(grn,tot-1)+F(grn,tot)*F(red,tot-1); assert p==F(8,15)
pairs=list(itertools.permutations(range(tot),2)); n=sum(1 for a,b in pairs if (a<red)!=(b<red)); assert F(n,len(pairs))==F(8,15)
add("probability-different-colours","GAT-Q-DAT.3",3,"A bag holds 6 red and 4 green counters. Two are drawn one after the other without replacement. What is the probability that they are different colours?","8/15",["4/15","12/25","1/2"],
 "'different' has TWO orders (red then green, green then red) — add both, and remember the second draw is from 9",
 "P(R then G) = 6/10 × 4/9 = 4/15 and P(G then R) = 4/10 × 6/9 = 4/15. Total = 8/15.",
 ["A: counted only one order.","B: put 10 on the second draw as well (with replacement), 2 × 6/10 × 4/10.","C: assumed a half because there are two colours."])
# 8 five coins exactly two heads
n=sum(1 for t in itertools.product([0,1],repeat=5) if sum(t)==2); assert F(n,32)==F(5,16)
add("exactly-k-heads-coins","GAT-Q-DAT.3",2,"A fair coin is tossed 5 times. What is the probability of exactly 2 heads?","5/16",["1/32","2/5","1/10"],
 "count the arrangements of the 2 heads among 5 tosses (10 of them) over 2⁵ = 32 outcomes",
 "There are 2⁵ = 32 equally likely outcomes and C(5,2) = 10 contain exactly two heads, so the probability is 10/32 = 5/16.",
 ["x: counted ONE arrangement of the two heads, 1/32.","x: used 2 out of 5 as if each toss were a single trial.","x: counted the 10 arrangements but divided by 100 instead of 32."])
# 9 even numbers > 500 from digits, no repeat
dig=[1,2,4,5,6,7]
cnt=sum(1 for t in itertools.permutations(dig,3) if t[2]%2==0 and 100*t[0]+10*t[1]+t[2]>500); assert cnt==32
add("count-even-above-threshold-no-repeat","GAT-Q-DAT.4",3,"How many three-digit even numbers greater than 500 can be formed from the digits 1, 2, 4, 5, 6 and 7 if no digit may be repeated?","32",["60","120","24"],
 "two conditions fight over the same digits — fix the FIRST digit (5, 6 or 7), then count the allowed last digits, then fill the middle",
 "First digit 5: last digit 2, 4 or 6 (3 ways) × middle 4 ways = 12. First digit 6: last digit 2 or 4 (2) × 4 = 8. First digit 7: 3 × 4 = 12. Total 12 + 8 + 12 = 32.",
 ["x: applied only one condition (even only, or above 500 only): 60.","x: no restriction at all, 6 × 5 × 4 = 120.","x: left out 6 as a first digit, which gives 12 + 12 = 24."])
# 10 parity must be odd
ok=[]
exprs={"a² + b":lambda a,b:a*a+b,"ab + 2":lambda a,b:a*b+2,"3a + 2b":lambda a,b:3*a+2*b,"a + b + 1":lambda a,b:a+b+1}
for nme,f in exprs.items():
    ok.append((nme,all(f(a,b)%2==1 for a in range(0,40,2) for b in range(1,40,2))))
assert [n for n,v in ok if v]==["a² + b"]
add("parity-must-be-odd","GAT-Q-ALG.5",2,"a is an even integer and b is an odd integer. Which of the following MUST be odd?","a² + b",["ab + 2","3a + 2b","a + b + 1"],
 "replace every variable with its parity (even = 0, odd = 1 mod 2) and compute — a product with an even factor is even, whatever the other factor",
 "a² is even, so a² + b = even + odd = odd. ab is even, so ab + 2 is even. 3a and 2b are both even, so 3a + 2b is even. a + b is odd, so a + b + 1 is even.",
 ["B: thought ab is odd because b is odd.","C: thought 3a is odd because 3 is odd.","D: forgot the +1 flips the parity of the odd sum a + b."])
# 11 two dice different
n=sum(1 for a in range(1,7) for b in range(1,7) if a!=b); assert F(n,36)==F(5,6)
add("dice-different-numbers","GAT-Q-DAT.3",2,"Two fair six-sided dice are rolled. What is the probability that the two numbers shown are different?","5/6",["1/6","35/36","1/2"],
 "use the complement: P(different) = 1 − P(same), and there are only 6 'doubles' out of 36",
 "The pairs with the same number are (1,1), …, (6,6): 6 of the 36 outcomes, so P(same) = 1/6 and P(different) = 1 − 1/6 = 5/6.",
 ["A: gave P(same) instead of P(different).","B: removed only one outcome (1,1) from 36.","C: assumed a half because the dice either match or do not."])
# 12 notes: equal 10 and 20, fixed 50s, solve count
n=22; assert 10*n+20*n+50*7==1010
add("equal-pair-notes-solve-count","GAT-Q-LOG.4",3,"A cashier holds equal numbers of 10 SAR and 20 SAR notes, together with seven 50 SAR notes. The notes total 1,010 SAR. How many 10 SAR notes are there?","22",["33","66","44"],
 "pair one 10 with one 20 (30 SAR per pair), subtract the fixed notes FIRST, then divide",
 "Seven 50 SAR notes are 350 SAR. The rest is 1,010 − 350 = 660 SAR, made of pairs worth 10 + 20 = 30 SAR each. 660 ÷ 30 = 22 pairs, so there are 22 notes of 10 SAR.",
 ["A: divided 660 by 20, as if only 20 SAR notes were involved.","C: divided 660 by 10, as if only 10 SAR notes were involved.","D: divided 660 by 15, the mean value of one note."])
# rotate to balance answer positions: key positions A,B,C,D cycling
import json
pos=0
for it in items:
    if it['opts'] is CMP or it['opts']==CMP: continue
    opts=it['opts']; k=0
    r=pos%4; pos+=1
    new=[None]*4
    # place key at index r, distractors in order of the remaining slots
    others=opts[1:]; oi=0
    for i in range(4):
        if i==r: new[i]=opts[0]
        else: new[i]=others[oi]; oi+=1
    # remap trap letters: trap list notes are tagged with letter of original slot (A..D skipping key at 0 => B,C,D originally?) 
    it['opts']=new; it['ans']=r

import re as _re
for it in items:
    L='ABCD'; notes=[_re.sub(r'^[A-D]: |^x: ','',t) for t in it['traps']]
    if it['opts']==CMP:
        wrong=[i for i in range(4) if i!=it['ans']]
    else:
        wrong=[i for i in range(4) if i!=it['ans']]
    it['traps']=[L[wrong[j]]+': '+notes[j] for j in range(3)]
json.dump(items,open('out_p.json','w'),ensure_ascii=False,indent=1)
print(len(items),[i['ans'] for i in items])

import re,json,collections
t=open('bank_src.md').read()
a=t.index('## 2. Item Bank'); b=t.index('## 3. Bank Index')
blocks=re.split(r'^### (?=[A-Z]{1,3}-\d+\s*$)',t[a:b],flags=re.M)[1:]
CANON={
 'Linear equations in one variable':('Algebra','Linear equations in one variable'),
 'Linear equations in two variables':('Algebra','Linear equations in two variables'),
 'Linear functions':('Algebra','Linear functions'),
 'Linear inequalities in one or two variables':('Algebra','Linear inequalities'),
 'Systems of two linear equations in two variables':('Algebra','Systems of linear equations'),
 'Equivalent expressions':('Advanced Math','Equivalent expressions'),
 'Nonlinear functions':('Advanced Math','Nonlinear functions'),
 'Function notation':('Advanced Math','Nonlinear functions'),
 'Nonlinear equations in one variable':('Advanced Math','Nonlinear equations and systems'),
 'Nonlinear equations in one variable and systems of equations in two variables':('Advanced Math','Nonlinear equations and systems'),
 'Area and volume':('Geometry and Trigonometry','Area and volume'),
 'Circles':('Geometry and Trigonometry','Circles'),
 'Lines, angles, and triangles':('Geometry and Trigonometry','Lines, angles, and triangles'),
 'Right triangles and trigonometry':('Geometry and Trigonometry','Right triangles and trigonometry'),
 'Percentages':('Problem-Solving and Data Analysis','Percentages'),
 'Probability and conditional probability':('Problem-Solving and Data Analysis','Probability'),
 'Ratios, rates, proportional relationships, and units':('Problem-Solving and Data Analysis','Ratios, rates and units'),
 'One-variable data: Distributions and measures of center and spread':('Problem-Solving and Data Analysis','One-variable data'),
 'One-variable data: distributions and measures of center and spread':('Problem-Solving and Data Analysis','One-variable data'),
 'One-variable data: mean, median, range, standard deviation':('Problem-Solving and Data Analysis','One-variable data'),
 'Two-variable data: Models and scatterplots':('Problem-Solving and Data Analysis','Two-variable data and scatterplots'),
 'Inference from sample statistics and margin of error':('Problem-Solving and Data Analysis','Inference and margin of error'),
 'Evaluating statistical claims: Observational studies and experiments':('Problem-Solving and Data Analysis','Statistical claims and studies'),
}
def canon(s):
    s=s.strip().rstrip('|').strip()
    s=re.sub(r'^(Algebra|Advanced Math|Geometry and Trigonometry|Problem-Solving and Data Analysis)\s+—\s+','',s)
    return CANON[s]
def grab(blk,label):
    m=re.search(r'\*\*'+label+r':?\*\*:?\s*(.*?)(?=\n\s*\*\*(?:Skill|Difficulty|Format|Source|Question|Correct Answer|Answer|Rationale[^*]*|Misconception[^*]*|Solution)\b|\n---\s*$|\Z)',blk,re.S)
    return m.group(1).strip() if m else None
items=[];bad=[]
for blk in blocks:
    iid=re.match(r'([A-Z]{1,3}-\d+)',blk).group(1)
    skill=grab(blk,'Skill'); diff=grab(blk,'Difficulty'); q=grab(blk,'Question')
    raw_ans=grab(blk,'Correct Answer') or grab(blk,'Answer')
    rat=grab(blk,r'Rationale(?: \(worked solution\))?') ; mis=grab(blk,'Misconception addressed') or grab(blk,'Misconception')
    skill_line=skill.split('**')[0].strip() if skill else ''
    dm=re.search(r'\*\*Difficulty:\*\*\s*(\w+)',blk); diff=dm.group(1) if dm else diff
    fm=re.search(r'\*\*Format:\*\*\s*([^\n*]+)',blk); fmt=fm.group(1).strip() if fm else ''
    # answer: first line only
    ans_line=(raw_ans or '').split('\n')[0].strip()
    # rationale may live inside answer block (worked solution style)
    if not rat and raw_ans and '\n' in raw_ans: rat=raw_ans.split('\n',1)[1]
    rat=re.sub(r'^\*\*Rationale[^*]*\*\*:?\s*','',(rat or '').strip())
    opts=None;qq=q
    if q:
        lines=q.split('\n')
        idx=[i for i,l in enumerate(lines) if re.match(r'^\(?[A-D]\)\s',l.strip())]
        if len(idx)>=4 and [re.match(r'^\(?([A-D])\)',lines[i].strip()).group(1) for i in idx[-4:]]==list('ABCD'):
            s=idx[-4]; opts=[re.sub(r'^\(?[A-D]\)\s*','',lines[i].strip()) for i in idx[-4:]]; qq='\n'.join(lines[:s]).strip()
    d,sk=canon(skill_line)
    key=None;sprans=None
    if opts:
        m=re.match(r'^\(?([A-D])\)?',ans_line); key='ABCD'.index(m.group(1))
    elif 'Multiple' in fmt: bad.append(iid)   # table-option MC; handled separately
    else: sprans=ans_line
    items.append(dict(id=iid,domain=d,skill=sk,diff='M' if diff.startswith('Med') else 'H',q=qq,opts=opts,key=key,spr=sprans,rat=rat,mis=mis or ''))
print(len(items),'unparsed MC:',bad)
print(collections.Counter((i['domain'],i['skill']) for i in items).most_common(30))
sp=collections.Counter(re.sub(r'\d','9',i['spr'])[:25] for i in items if i['spr']); print(sp.most_common(40))
fig=[i['id'] for i in items if re.search(r'figure|diagram|shown below|graph (?:shown|below)|in the graph|scatterplot shown',i['q'],re.I)]; print('figure-ish',len(fig),fig[:15])
print('no rationale',sum(1 for i in items if not i['rat']))
json.dump(items,open('orig.json','w'))

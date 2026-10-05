import sys,json,re,os,subprocess
cfg=json.load(open(sys.argv[1])); errs=[]
def need(d,keys,where):
    for k in keys:
        if k not in d: errs.append(f"missing {where}.{k}")
need(cfg,["id","outName","grade","course","topicNo","lessonNo","titleLines","topicTitle","titleMath","codes","eq","mps","objectives","vocab","standards","diagnose","blocks","practice","production","gate","smart","exam","recap"],"cfg")
if not errs:
    if not (2<=len(cfg["titleLines"])<=2 or len(cfg["titleLines"])==1): errs.append("titleLines must have 1-2 lines")
    for s in cfg["standards"]: need(s,["code","text"],"standard")
    need(cfg["diagnose"],["items","doneWhen","notes"],"diagnose"); 
    if len(cfg["diagnose"]["items"])!=3: errs.append("diagnose needs 3 items")
    if not 3<=len(cfg["blocks"])<=4: errs.append("3 or 4 blocks")
    for i,b in enumerate(cfg["blocks"]):
        need(b,["title","rules","examples","fig","notes"],f"blocks[{i}]")
        if not 1<=len(b["rules"])<=3: errs.append(f"block {i} rules 1-3")
        n=len(b["examples"])
        if b["fig"]:
            if n!=2: errs.append(f"block {i}: with fig exactly 2 examples")
            need(b["fig"],["file","w","h"],f"blocks[{i}].fig")
            if not os.path.exists(b["fig"]["file"]): errs.append("fig file missing "+b["fig"]["file"])
        elif n not in (2,3): errs.append(f"block {i}: 2 or 3 examples")
        for e in b["examples"]:
            need(e,["q","steps"],"example")
            if not 1<=len(e["steps"])<=3: errs.append(f"block {i}: example steps 1-3")
    p=cfg["practice"]
    for k in ("practice","apply","investigate"):
        need(p[k],["items","done"],"practice."+k)
        if not 1<=len(p[k]["items"])<=2: errs.append(f"practice.{k} items 1-2")
    need(p,["notes"],"practice")
    need(cfg["production"],["title","context","given","tasks","doneWhen","hint","notes"],"production")
    if len(cfg["production"]["tasks"])!=3 or len(cfg["production"]["doneWhen"])!=4: errs.append("production: 3 tasks, 4 doneWhen")
    if len(cfg["production"]["given"])>2: errs.append("production.given max 2")
    need(cfg["gate"],["items","notes"],"gate")
    if len(cfg["gate"]["items"])!=3: errs.append("gate needs 3 items")
    need(cfg["smart"],["create","createDone","exit","exitIntro","next","notes"],"smart")
    if len(cfg["smart"]["create"])!=3 or not 1<=len(cfg["smart"]["exit"])<=2: errs.append("smart: 3 create, 1-2 exit")
    for k in ("sat","gat","saat"):
        need(cfg["exam"][k],["q","steps"],"exam."+k)
        if not 1<=len(cfg["exam"][k]["q"])<=2 or not 1<=len(cfg["exam"][k]["steps"])<=3: errs.append(f"exam.{k}: q 1-2, steps 1-3")
    need(cfg["exam"],["notes"],"exam")
    # no $ in strings; no latex backslashes in prose fields
    def walk(o,path=""):
        if isinstance(o,dict):
            for k,v in o.items(): walk(v,path+"."+k)
        elif isinstance(o,list):
            for i,v in enumerate(o): walk(v,path+f"[{i}]")
        elif isinstance(o,str):
            if "$" in o: errs.append("dollar sign in "+path)
            latexy=re.search(r"\.(items|q|steps|rules|given|exit)\[|titleMath|\.q$",path)
            if not latexy and "\\" in o: errs.append("backslash in prose field "+path)
            if o.count("{")!=o.count("}"): errs.append("unbalanced braces "+path)
    walk(cfg)
if not errs:
    from collect import collect
    from mathgen import render
    import io,contextlib
    try:
        E=collect(cfg); buf=io.StringIO()
        with contextlib.redirect_stdout(buf): render(E,"v_"+cfg["id"],"_vtmp_"+cfg["id"])
        print("LaTeX OK:",len(E),"expressions")
    except SystemExit as e: errs.append("LaTeX compile failed (see above)")
    except Exception as e: errs.append("LaTeX render error "+repr(e))
print("ERRORS:" if errs else "VALID"); [print(" -",e) for e in errs]
sys.exit(1 if errs else 0)

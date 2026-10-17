import sys,os,shutil
sys.path.insert(0,"/home/claude/w8ap")
os.chdir("/home/claude/w8ap/ws")
exec(open("/home/claude/w8ap/wsbase.py").read())
from wsitems import *
OUT="/home/claude/deliver/w8/AP"; os.makedirs(OUT,exist_ok=True)
for nm,top,title,M,F,ttl in (
 ("w11","AP PRECALCULUS · TOPIC 1.11","Equivalent Representations of Polynomial and Rational Expressions",M11,F11,"Topic 1.11 Equivalent Representations of Polynomial and Rational Expressions"),
 ("w12","AP PRECALCULUS · TOPIC 1.12","Transformations of Functions",M12,F12,"Topic 1.12 Transformations of Functions"),
 ("w13","AP PRECALCULUS · TOPIC 1.13",r"Function Model Selection and Assumption \mbox{Articulation}",M13,F13,"Topic 1.13 Function Model Selection and Assumption Articulation")):
    build(nm,top,title,M,F,None,False); build(nm+"s",top,title,M,F,None,True)
    shutil.copy(nm+".pdf",f"{OUT}/AP Precalculus {ttl} worksheet.pdf"); shutil.copy(nm+"s.pdf",f"{OUT}/AP Precalculus {ttl} worksheet solved.pdf")

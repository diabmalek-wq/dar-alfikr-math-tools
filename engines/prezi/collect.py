"""Collect every LaTeX string in a lesson config -> dict key -> (latex, colourHex)."""
import json,hashlib
INK,WHITE="222E2D","FFFFFF"
def key(t,c): return "k"+hashlib.md5((c+"|"+t).encode()).hexdigest()[:10]
def collect(cfg):
    E={}
    def add(t,c=INK):
        if t is None: return
        E[key(t,c)]=(t,c)
    add(cfg["titleMath"],WHITE)
    for t in cfg["diagnose"]["items"]: add(t)
    for b in cfg["blocks"]:
        for r in b["rules"]: add(r,WHITE)
        for e in b["examples"]:
            add(e["q"]); [add(s) for s in e["steps"]]
    for k in ("practice","apply","investigate"):
        for t in cfg["practice"][k]["items"]: add(t)
    for t in cfg["production"]["given"]: add(t)
    for t in cfg["gate"]["items"]: add(t)
    for t in cfg["smart"]["exit"]: add(t)
    for k in ("sat","gat","saat"):
        for t in cfg["exam"][k]["q"]+cfg["exam"][k]["steps"]: add(t)
    return E

"""
Fills each A3 project sheet to the foot of its single page.

There is no way to measure text height from the docx side, so this measures the
rendered page: build → PDF → PNG → find the lowest ink above the footer, then
add or remove ruled lines and go round again. Stops when every sheet ends inside
the target band and none has spilled onto a second page.
"""
import json, os, subprocess, glob
from PIL import Image

SHEETS = sorted(n[:-5] for n in os.listdir(".") if
                n.startswith("PBL_Task_") and n.endswith(".docx"))
SLUG = {n: n[len("PBL_Task_"):] for n in SHEETS}   # cfg.slug, as the engine keys it

LO, HI = 0.885, 0.925   # the last ruled line should land in here          # where the last ruled line should sit on the page
FOOTER = 0.945                 # ignore ink below this — that is the footer


def build():
    for js in ("w2_docs.js", "w3_docs.js", "w2_pbl_legacy.js"):
        subprocess.run(["node", js], capture_output=True)


def render():
    for f in glob.glob("cal/*"):
        os.remove(f)
    os.makedirs("cal", exist_ok=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", "cal"]
                   + [n + ".docx" for n in SHEETS], capture_output=True)
    out = {}
    for n in SHEETS:
        pdf = f"cal/{n}.pdf"
        pages = int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
                    .stdout.split("Pages:")[1].split()[0])
        subprocess.run(["pdftoppm", "-r", "50", "-png", "-f", "1", "-l", "1", pdf, f"cal/{n}"],
                       capture_output=True)
        png = glob.glob(f"cal/{n}-*.png")[0]
        im = Image.open(png).convert("L")
        w, h = im.size
        px = im.load()
        bottom = 0
        for y in range(int(h * FOOTER) - 1, 0, -1):
            row = min(px[x, y] for x in range(0, w, 2))
            if row < 240:
                bottom = y / h
                break
        out[n] = (pages, bottom)
    return out


extra = {SLUG[n]: 0 for n in SHEETS}
if os.path.exists("pbl_extra.json"):
    extra.update(json.load(open("pbl_extra.json")))

for it in range(9):
    json.dump(extra, open("pbl_extra.json", "w"), indent=1)
    build()
    m = render()
    done = True
    print(f"--- pass {it + 1}")
    for n in SHEETS:
        pages, bottom = m[n]
        slug = SLUG[n]
        tag = "ok"
        if pages > 1:
            extra[slug] -= 2; tag = "spilled → -2"; done = False
        elif bottom < LO:
            step = 2 if bottom < LO - 0.06 else 1
            extra[slug] += step; tag = f"short → +{step}"; done = False
        elif bottom > HI:
            extra[slug] -= 1; tag = "tight → -1"; done = False
        print(f"  {slug[:34]:34s} pages {pages}  bottom {bottom:.3f}  extra {extra[slug]:2d}  {tag}")
    if done:
        print("all sheets filled")
        break

json.dump(extra, open("pbl_extra.json", "w"), indent=1)
build()
print("final extras:", extra)

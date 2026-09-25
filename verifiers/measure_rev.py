import subprocess, glob, os, sys
from PIL import Image
f = sys.argv[1] if len(sys.argv) > 1 else "Revision_Ready_for_Algebra_II_Worksheet"
for p in glob.glob("mv-*.png"):
    os.remove(p)
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", f + ".docx"],
               capture_output=True)
n = int(subprocess.run(["pdfinfo", f + ".pdf"], capture_output=True, text=True)
        .stdout.split("Pages:")[1].split()[0])
subprocess.run(["pdftoppm", "-png", "-r", "50", f + ".pdf", "mv"], check=True)
print(f, "pages:", n)
for p in sorted(glob.glob("mv-*.png")):
    im = Image.open(p).convert("L")
    W, H = im.size
    px = im.load()
    bot = 0
    for y in range(int(H * 0.945), 0, -1):          # ignore the footer band
        if any(px[x, y] < 240 for x in range(0, W, 2)):
            bot = y / H
            break
    print(f"  {p}  last ink at {bot:.3f}")

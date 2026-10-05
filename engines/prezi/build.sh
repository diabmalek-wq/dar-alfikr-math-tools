#!/bin/bash
# usage: ./build.sh L6-3
set -e; cd /home/claude/fikr_pptx/prezi; ID=$1
OUT=$(python3 -c "import json;print(json.load(open('cfg/$ID.json'))['outName'])")
python3 render_math.py cfg/$ID.json m_$ID >/dev/null
node engine.js cfg/$ID.json
python3 morph2.py raw_$ID.pptx "out/$OUT.pptx"
python3 /root/.claude/skills/synced/*/pptx/scripts/office/validate.py "out/$OUT.pptx" | tail -2
cd out && python3 /root/.claude/skills/synced/*/pptx/scripts/office/soffice.py --headless --convert-to pdf "$OUT.pptx" >/dev/null 2>&1
rm -rf ../qa_$ID; mkdir ../qa_$ID; pdftoppm -png -r 50 "$OUT.pdf" ../qa_$ID/s
cd ../qa_$ID && python3 -c "
from PIL import Image;import glob
f=sorted(glob.glob('s-*.png'));ims=[Image.open(x) for x in f];w,h=ims[0].size;c=3;r=(len(ims)+c-1)//c
m=Image.new('RGB',(w*c,h*r),'white')
for i,im in enumerate(ims): m.paste(im,((i%c)*w,(i//c)*h))
m.save('mosaic.png');print(len(ims),'slides')"

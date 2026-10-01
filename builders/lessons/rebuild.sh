#!/bin/bash
# usage: rebuild.sh lessons_xxx.js Deck.pptx
S=/root/.claude/skills/synced/6d298923-714b-49f3-a001-d0048c23790a_76b2c490-423e-4dce-9177-99a8bff7b1bb/pptx
node $1 | tail -1 && python3 fix_bullets.py $2 && python3 animate_deck.py $2 | tail -1
python3 $S/scripts/office/validate.py $2 2>&1 | tail -2
R=r_$(basename $2 .pptx); rm -rf $R && mkdir $R && python3 $S/scripts/office/soffice.py --headless --convert-to pdf --outdir $R $2 >/dev/null 2>&1; pdftoppm -jpeg -r 80 $R/*.pdf $R/s
python3 - <<P
from PIL import Image; import glob
fs=sorted(glob.glob('$R/s-*.jpg')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size
for k in range(0,len(ims),4):
    g=Image.new('RGB',(w*2,h*2),'white')
    for i,im in enumerate(ims[k:k+4]): g.paste(im,((i%2)*w,(i//2)*h))
    g.save(f'$R/g{k//4}.jpg')
print(len(ims),'slides in $R')
P

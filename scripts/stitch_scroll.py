"""Stitch a vertical screen-recording scroll into one tall image.

Reading a scrolling recording frame by frame loses content: a question can be
half in one frame and half in the next, and at 2 fps a fast flick skips a whole
card. Stitching first guarantees every pixel of the scroll is seen exactly once.

Method: for each consecutive pair, slide a tall strip of the NEW frame over the
PREVIOUS frame and take the offset with the lowest mean absolute difference.
Only the newly revealed band is appended.
"""
import subprocess, sys, os
import numpy as np
import cv2

VID = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "scroll.png"
TMP = os.path.join(os.path.dirname(OUT) or ".", "_sf")
FPS = 5

# Crop away every FIXED overlay before matching. The "Recorded by mobizen"
# banner and the round timer button sit at constant screen positions, so a
# template match happily locks onto them instead of the scrolling content and
# the stitch duplicates whole cards. Excluding them is what makes this work.
TOP, BOT, RIGHT = 88, 1424, 652

os.makedirs(TMP, exist_ok=True)
for f in os.listdir(TMP):
    os.remove(os.path.join(TMP, f))
subprocess.run(["ffmpeg", "-y", "-i", VID, "-vf", f"fps={FPS}", "-q:v", "2",
                os.path.join(TMP, "s_%04d.png")], check=True, capture_output=True)

files = sorted(os.listdir(TMP))
frames = []
for f in files:
    im = cv2.imread(os.path.join(TMP, f), cv2.IMREAD_GRAYSCALE)
    col = cv2.imread(os.path.join(TMP, f))
    frames.append((im[TOP:BOT, :RIGHT], col[TOP:BOT, :RIGHT]))
print(f"{len(frames)} frames, tile {frames[0][0].shape}")

H, W = frames[0][0].shape
canvas = [frames[0][1]]
total_shift = 0
MAXS = H - 120           # never claim more movement than leaves an overlap

BAND = 180               # rows of the new frame used as the search pattern
for i in range(1, len(frames)):
    prev, cur = frames[i - 1][0], frames[i][0]
    patt = cur[0:BAND, :]
    # matchTemplate does the whole offset search in one optimised pass; the
    # python loop version took minutes per clip.
    res = cv2.matchTemplate(prev, patt, cv2.TM_CCOEFF_NORMED)
    _mn, mx, _ml, mloc = cv2.minMaxLoc(res)
    best = mloc[1]
    if best > 2 and mx > 0.90 and best <= H - BAND:
        canvas.append(frames[i][1][H - best:, :])
        total_shift += best

out = np.vstack(canvas)
cv2.imwrite(OUT, out)
print(f"stitched {out.shape[0]} px tall  (scrolled {total_shift})")

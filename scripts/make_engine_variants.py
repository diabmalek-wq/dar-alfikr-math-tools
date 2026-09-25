"""
Derives the engine-local asset variants that lesson_engine.js / docs_engine.js
expect next to themselves (engines/*.png, engines/*.jpg) from the three
canonical logo files committed at assets/logos/. These derived files are
build output — regenerable, gitignored, never committed — exactly like the
math/graph PNGs the generators produce.

Run once per fresh checkout before building any deck or docx set:
    python3 scripts/make_engine_variants.py

Produces, inside engines/:
  dept_logo.png, school_logo.png, cognia_badge.png   — direct copies
  dept_logo_white.png, school_logo_white.png          — white silhouettes,
                                                         alpha preserved, for
                                                         dark-background slides
  dept_logo_doc.png, school_logo_doc.png,
  cognia_badge_doc.png                                — same art, used by
                                                         docs_engine.js's
                                                         Word-document header
  bg_light.jpg, bg_dark.jpg                           — solid house-colour
                                                         slide backgrounds
  geogebra_qr_placeholder.png                          — placeholder QR box;
                                                         swap for a real QR
                                                         once the GeoGebra
                                                         activity link exists
"""
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

SRC = "assets/logos"
DST = "engines"
os.makedirs(DST, exist_ok=True)

TEAL_DEEP = (14, 79, 76)      # 0E4F4C — house dark
WHITE_BG = (255, 255, 255)    # house light


def white_silhouette(src_path, dst_path):
    im = Image.open(src_path).convert("RGBA")
    r, g, b, a = im.split()
    white = Image.new("RGBA", im.size, (255, 255, 255, 0))
    white.putalpha(a)
    white.save(dst_path)


def solid_bg(path, rgb, size=(2000, 1125)):
    Image.new("RGB", size, rgb).save(path, quality=92)


def qr_placeholder(path, size=600):
    im = Image.new("RGB", (size, size), WHITE_BG)
    d = ImageDraw.Draw(im)
    m = size // 12
    d.rectangle([m, m, size - m, size - m], outline=TEAL_DEEP, width=size // 60)
    # simple corner finder squares, QR-style, so it reads as "a QR code" at a glance
    fs = size // 5
    for cx, cy in [(m + fs // 2, m + fs // 2), (size - m - fs // 2, m + fs // 2),
                   (m + fs // 2, size - m - fs // 2)]:
        d.rectangle([cx - fs // 2, cy - fs // 2, cx + fs // 2, cy + fs // 2],
                    outline=TEAL_DEEP, width=size // 90)
        pad = fs // 4
        d.rectangle([cx - fs // 2 + pad, cy - fs // 2 + pad, cx + fs // 2 - pad, cy + fs // 2 - pad],
                    fill=TEAL_DEEP)
    try:
        font = ImageFont.load_default()
        d.text((size / 2, size - m * 1.6), "GEOGEBRA", fill=TEAL_DEEP, font=font, anchor="mm")
    except Exception:
        pass
    im.save(path)


# ---- direct copies (pptx logos + docx header logos share the same art) ----
for name in ("dept_logo.png", "school_logo.png", "cognia_badge.png"):
    shutil.copyfile(os.path.join(SRC, name), os.path.join(DST, name))
    stem, ext = os.path.splitext(name)
    shutil.copyfile(os.path.join(SRC, name), os.path.join(DST, f"{stem}_doc{ext}"))

# ---- white silhouettes for dark-background slides ----
white_silhouette(os.path.join(SRC, "dept_logo.png"), os.path.join(DST, "dept_logo_white.png"))
white_silhouette(os.path.join(SRC, "school_logo.png"), os.path.join(DST, "school_logo_white.png"))

# ---- solid house-colour slide backgrounds ----
solid_bg(os.path.join(DST, "bg_light.jpg"), WHITE_BG)
solid_bg(os.path.join(DST, "bg_dark.jpg"), TEAL_DEEP)

# ---- GeoGebra QR placeholder ----
qr_placeholder(os.path.join(DST, "geogebra_qr_placeholder.png"))

print("wrote engine asset variants to", DST)

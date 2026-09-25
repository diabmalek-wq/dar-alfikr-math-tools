"""Shrink a worksheet PDF so it can be pushed through the Drive connector.

The papers are heavy because every expression is a 460 dpi transparent PNG.
For a printed A4 worksheet ~230 dpi is already past what a laser printer
resolves, so halving the raster and re-flating is invisible on paper and
roughly quarters the file.

Math must stay crisp: images are kept lossless (PNG/flate), never JPEG,
because JPEG ringing around thin vinculum and fraction rules is exactly the
artefact that makes a radical unreadable.
"""
import sys, io, zlib
import pikepdf
from PIL import Image, ImageOps

SCALE = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
MIN_W = 40          # leave tiny glyphs alone, they cost nothing and blur fast

src, dst = sys.argv[1], sys.argv[2]
pdf = pikepdf.open(src)

done, saved = 0, 0
for name, raw in pdf.images.items() if hasattr(pdf, "images") else []:
    pass

# One XObject is often referenced from several pages. Rescaling per page
# would shrink a shared image once per reference — 0.55 three times over is
# 0.17, which is what turned the expressions to mush. Rescale each object
# once and reuse the result everywhere it appears.
seen = {}

for page in pdf.pages:
    for name, obj in list(page.images.items()):
        key = obj.objgen
        if key in seen:
            page.Resources.XObject[name] = seen[key]
            continue
        try:
            im = pikepdf.PdfImage(obj).as_pil_image()
        except Exception:
            continue
        w, h = im.size
        if w < MIN_W:
            continue

        # The mathtext and figure PNGs are solid black ink whose shape lives
        # entirely in a separate /SMask. as_pil_image() returns only the
        # colour channels, so ignoring the mask turns every expression into a
        # black rectangle. Pull the mask, resize it alongside, composite.
        mask = None
        if "/SMask" in obj and obj.SMask is not None:
            try:
                sm = obj.SMask
                mask = pikepdf.PdfImage(sm).as_pil_image().convert("L")
                # matplotlib writes these masks with /Decode [1 0], i.e. the
                # samples mean the OPPOSITE of their face value. Read it off
                # the object rather than assuming — getting this backwards is
                # what turns every expression into a solid black bar.
                dec = sm.get("/Decode")
                if dec is not None and float(dec[0]) > float(dec[1]):
                    mask = ImageOps.invert(mask)
            except Exception:
                mask = None

        nw, nh = max(1, int(w * SCALE)), max(1, int(h * SCALE))
        im = im.convert("RGB").resize((nw, nh), Image.LANCZOS)
        if mask is not None:
            bg = Image.new("RGB", (nw, nh), "white")
            bg.paste(im, mask=mask.resize((nw, nh), Image.LANCZOS))
            im = bg
        im = im.convert("L")                      # every figure is mono ink

        # A page of maths is overwhelmingly white. If the result is mostly
        # dark the composite went the wrong way round — refuse rather than
        # ship an unreadable worksheet.
        if sum(im.getdata()) / (nw * nh) < 110:
            raise SystemExit(f"{name}: composite came out dark — check /Decode")

        data = im.tobytes()
        before = len(bytes(obj.read_raw_bytes()))
        new = pikepdf.Stream(pdf, zlib.compress(data, 9))
        new.Type = pikepdf.Name("/XObject")
        new.Subtype = pikepdf.Name("/Image")
        new.Width, new.Height = nw, nh
        new.ColorSpace = pikepdf.Name("/DeviceGray")
        new.BitsPerComponent = 8
        new.Filter = pikepdf.Name("/FlateDecode")
        page.Resources.XObject[name] = new
        seen[key] = new
        done += 1
        saved += before - len(bytes(new.read_raw_bytes()))

pdf.save(dst, compress_streams=True,
         object_stream_mode=pikepdf.ObjectStreamMode.generate)
print(f"{done} images rescaled x{SCALE}, ~{saved/1024:.0f} KB of raster removed")

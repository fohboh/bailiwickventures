"""Export the Trajectory mark as production SVG + PNG assets."""
import os, sys, pathlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme import LINKS, NODES

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "brand"
if OUT.exists():
    shutil.rmtree(OUT)
(OUT / "svg").mkdir(parents=True)
(OUT / "png").mkdir(parents=True)

NAVY = "#12304F"
BLACK = "#0B0C0E"
WHITE = "#FFFDF9"


def mark_svg(c, small=False, pad=0):
    sw = 4.5 if small else 3.5
    r = (7.5, 7.5, 9.5, 6.0) if small else (7.0, 7.0, 9.0, 5.5)
    circles = "".join(f'<circle cx="{x}" cy="{y}" r="{rr}"/>'
                      for (x, y), rr in zip(NODES, r))
    return (f'<g stroke="{c}" stroke-width="{sw}" stroke-linecap="round" fill="none">'
            f'<path d="{LINKS}"/></g><g fill="{c}">{circles}</g>')


def doc(inner, vb="0 0 64 64"):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">\n  {inner}\n</svg>\n')


def tile_svg(bg, fg, radius=12):
    return doc(f'<rect width="64" height="64" rx="{radius}" fill="{bg}"/>'
               f'<g transform="translate(6.4 6.4) scale(0.8)">{mark_svg(fg, small=True)}</g>')


# ---------------------------------------------------------------- SVG
SVGS = {
    "mark-navy.svg":        doc(mark_svg(NAVY)),
    "mark-black.svg":       doc(mark_svg(BLACK)),
    "mark-white.svg":       doc(mark_svg(WHITE)),
    "mark-navy-small.svg":  doc(mark_svg(NAVY, small=True)),
    "mark-black-small.svg": doc(mark_svg(BLACK, small=True)),
    "mark-white-small.svg": doc(mark_svg(WHITE, small=True)),
    "tile-navy.svg":        tile_svg(NAVY, WHITE),
    "tile-black.svg":       tile_svg(BLACK, "#FFFFFF"),
    "tile-white.svg":       tile_svg("#FFFFFF", NAVY),
    "favicon.svg":          tile_svg(NAVY, WHITE, radius=10),
}

# lockups: live text, needs outlining before print
def lockup(mc, tc, sc, name, sub):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 96">\n'
            f'  <g transform="translate(6 16)">{mark_svg(mc)}</g>\n'
            f'  <text x="92" y="44" font-family="Inter, Helvetica, Arial, sans-serif" '
            f'font-size="30" font-weight="700" letter-spacing="-0.4" fill="{tc}">{name}</text>\n'
            f'  <text x="93" y="66" font-family="Inter, Helvetica, Arial, sans-serif" '
            f'font-size="10.5" font-weight="700" letter-spacing="3.6" fill="{sc}">{sub}</text>\n'
            '</svg>\n')

SVGS["lockup-ventures-navy.svg"] = lockup(NAVY, NAVY, "#6B8AA6", "Bailiwick", "VENTURES, INC.")
SVGS["lockup-ventures-black.svg"] = lockup(BLACK, BLACK, "#6E7278", "Bailiwick", "VENTURES, INC.")
SVGS["lockup-ventures-white.svg"] = lockup(WHITE, WHITE, "#9FB0BF", "Bailiwick", "VENTURES, INC.")
SVGS["lockup-venture-studio-navy.svg"] = lockup(NAVY, NAVY, "#6B8AA6", "Bailiwick", "VENTURE STUDIO")
SVGS["lockup-vibe-navy.svg"] = lockup(NAVY, NAVY, "#6B8AA6", "Bailiwick", "VIBE")

for fn, body in SVGS.items():
    (OUT / "svg" / fn).write_text(body, encoding="utf-8")
print(f"wrote {len(SVGS)} SVG files")

# ---------------------------------------------------------------- PNG
from playwright.sync_api import sync_playwright

JOBS = []
for size in (1024, 512, 256, 128, 64, 48, 32, 24, 16):
    small = size <= 30
    for label, color in (("navy", NAVY), ("black", BLACK), ("white", WHITE)):
        JOBS.append((f"mark-{label}-{size}.png", doc(mark_svg(color, small=small)), size, True))
for size in (1024, 512, 256, 192, 180, 128, 64, 32, 16):
    JOBS.append((f"tile-navy-{size}.png", tile_svg(NAVY, WHITE), size, False))
JOBS.append(("apple-touch-icon.png", tile_svg(NAVY, WHITE, radius=0), 180, False))
JOBS.append(("favicon-32.png", tile_svg(NAVY, WHITE, radius=6), 32, False))
JOBS.append(("favicon-16.png", tile_svg(NAVY, WHITE, radius=3), 16, False))

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 1200})
    for fn, svg, size, transparent in JOBS:
        html = ('<html><body style="margin:0;background:transparent">'
                f'<div id="t" style="width:{size}px;height:{size}px">{svg.split("?>")[1]}</div>'
                '</body></html>')
        pg.set_content(html)
        pg.wait_for_timeout(30)
        pg.locator("#t").screenshot(path=str(OUT / "png" / fn), omit_background=transparent)
    b.close()
print(f"wrote {len(JOBS)} PNG files")

(OUT / "README.txt").write_text("""BAILIWICK — BRAND MARK ASSETS
Direction 05, "Trajectory". August 2026.

THE MARK
  Four nodes connected, climbing left to right, with one branch peeling off.
  The terminal node is oversized on purpose — that is where the venture ends up.
  Single color by design. It has no color dependency at all.

FILES
  svg/    Vector originals. Use these for anything that will be resized.
  png/    Raster exports, transparent background where the mark stands alone.

  mark-*           The mark on its own.
  mark-*-small     Optical variant: thicker links, larger nodes. Use BELOW 30 px.
  tile-*           The mark inside a rounded tile. App icons, avatars, favicons.
  lockup-*         Mark plus wordmark.
  favicon.svg      Drop-in favicon.
  apple-touch-icon.png   180x180, square (iOS rounds it itself).

TWO OPTICAL WEIGHTS — THIS MATTERS
  Above ~30 px use the standard mark. Below ~30 px use the -small variant.
  The geometry is identical; only the stroke weight and node radii change so the
  form does not dissolve. Using the standard mark at 16 px will look broken.

COLOR
  Brand color is still undecided. Everything currently ships in:
    navy   #12304F   (what the website uses today)
    black  #0B0C0E   (one-color, print, embroidery, fax-safe)
    white  #FFFDF9   (reversed, for dark backgrounds)
  To change the brand color, edit one line: the `c` default in the `mark()`
  function in build/theme.py. Every use across the site follows.

CLEAR SPACE AND MINIMUM SIZE
  Clear space: the diameter of the largest node on all four sides.
  Minimum size: 16 px on screen, 6 mm in print, using the -small variant.

WHAT NOT TO DO
  Do not add a gradient. Do not outline it. Do not recolor individual nodes.
  Do not stretch it. Do not rotate it — the climb is the whole idea.
  Do not straighten the branch. The branch is what keeps it from being generic.

ONE THING TO FINISH
  The lockup SVGs contain LIVE TEXT, not outlines, because the container that
  generated them had no access to the Inter typeface. Before sending a lockup to
  a printer, a fabricator, or anyone outside the company, open it in Illustrator
  or Figma and convert the text to outlines. The mark files themselves are pure
  geometry and need nothing done to them.
""", encoding="utf-8")

total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
print(f"brand/ total {total/1024:.0f} KB")

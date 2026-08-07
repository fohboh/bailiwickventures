BAILIWICK — BRAND MARK ASSETS
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

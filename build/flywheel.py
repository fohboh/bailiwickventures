"""The Bailiwick flywheel — drawn in the same node-and-link language as the mark.

Not a circle: an outward spiral, because a flywheel that only goes in circles is
not compounding. The return arc is the heaviest line, because the return is the
argument. The mark sits at the axle.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme import LINKS, NODES

WARM = "#F6F1E8"
MUTED = "#AEBDCA"
DIM = "#8195A6"
BRONZE = "#C08A4A"

W, H = 1000.0, 672.0
CX, CY = 500.0, 336.0
R = 150.0           # the wheel itself is a true circle
R_OUT = 208.0       # where the return arc breaks out to
START = -90.0       # step 01 at the top
LABEL_R = 216.0     # labels ride just outside the wheel, close to their node

STEPS = [
    ("01", "Architect", "The venture is designed"),
    ("02", "Build", "The design is made real"),
    ("03", "Operate", "It becomes a company"),
    ("04", "Redeploy", "People and method return"),
]


def pt(a, r):
    t = math.radians(a)
    return CX + r * math.cos(t), CY + r * math.sin(t)


def sweep(a0, a1, r0, r1, step=1.5):
    """Arc from a0->a1 while the radius eases r0->r1."""
    n = max(2, int(abs(a1 - a0) / step))
    pts = []
    for i in range(n + 1):
        t = i / n
        e = t * t * (3 - 2 * t)              # smoothstep, so the break-out is graceful
        a = a0 + (a1 - a0) * t
        pts.append(pt(a, r0 + (r1 - r0) * e))
    d = f"M{pts[0][0]:.2f} {pts[0][1]:.2f}"
    for x, y in pts[1:]:
        d += f" L{x:.2f} {y:.2f}"
    return d


def axle_mark(scale=0.62):
    """The Trajectory mark, small and quiet, at the centre of the wheel."""
    circles = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for (x, y), r in
                      zip(NODES, (6.0, 6.0, 8.0, 5.0)))
    size = 64 * scale
    tx, ty = CX - size / 2, CY - size / 2
    return (f'<g transform="translate({tx:.1f} {ty:.1f}) scale({scale})" opacity="0.5">'
            f'<g stroke="{DIM}" stroke-width="3.5" stroke-linecap="round" fill="none">'
            f'<path d="{LINKS}"/></g><g fill="{DIM}">{circles}</g></g>')


def build(idp="fw"):
    p = []

    # the wheel: 01 -> 04, a true circle
    p.append(f'<path d="{sweep(START, START + 270, R, R)}" fill="none" stroke="{MUTED}" '
             f'stroke-width="1.7" stroke-linecap="round"/>')

    # the return: breaks outward and overshoots past 01 — this is the argument
    p.append(f'<path d="{sweep(START + 270, START + 366, R, R_OUT)}" fill="none" '
             f'stroke="{BRONZE}" stroke-width="3.2" stroke-linecap="round" '
             f'marker-end="url(#{idp}-a)"/>')

    p.append(axle_mark())

    for i, (num, title, dek) in enumerate(STEPS):
        a = START + i * 90
        x, y = pt(a, R)
        p.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{10.5 if i == 0 else 8}" fill="{WARM}"/>')

        lx, ly = pt(a, LABEL_R)
        if i == 0:      # top — text stacks upward from the node
            anchor, ny = "middle", ly - 86
        elif i == 1:    # right
            anchor, ny = "start", ly - 26
        elif i == 2:    # bottom
            anchor, ny = "middle", ly + 22
        else:           # left
            anchor, ny = "end", ly - 26

        p.append(f'<text x="{lx:.1f}" y="{ny:.1f}" text-anchor="{anchor}" '
                 f'font-family="Inter,ui-sans-serif,system-ui,sans-serif" font-size="11" '
                 f'font-weight="700" letter-spacing="0.2em" fill="{BRONZE}">{num}</text>')
        p.append(f'<text x="{lx:.1f}" y="{ny + 29:.1f}" text-anchor="{anchor}" '
                 f'font-family="Source Serif 4,Palatino,Georgia,serif" font-size="26" '
                 f'fill="{WARM}">{title}</text>')
        p.append(f'<text x="{lx:.1f}" y="{ny + 51:.1f}" text-anchor="{anchor}" '
                 f'font-family="Inter,ui-sans-serif,system-ui,sans-serif" font-size="13.5" '
                 f'fill="{DIM}">{dek}</text>')

    defs = (f'<defs><marker id="{idp}-a" viewBox="0 0 10 10" refX="7" refY="5" '
            f'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{BRONZE}"/></marker></defs>')

    label = ("The Bailiwick flywheel: Bailiwick Venture Studio architects a venture, "
             "BailiwickVibe builds it, it becomes an operating company, and its people "
             "and methods return to the Studio — each turn starting further out than the last.")

    return (f'<svg class="flywheel" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
            f'aria-label="{label}">{defs}{"".join(p)}</svg>')


if __name__ == "__main__":
    import pathlib
    pathlib.Path("/tmp/fw.html").write_text(
        f'<html><body style="margin:0;background:#0C2138;display:flex;align-items:center;'
        f'justify-content:center;height:100vh"><div style="width:1000px">{build()}</div>'
        f'</body></html>')
    print("preview written")

"""Sine weave: wavy ivory ribbons woven over and under on ink.

Horizontal and vertical ribbons follow sine waves. After both sets are drawn, every second
crossing repaints the horizontal ribbon on top, so the result is a true basket weave that
happens to wobble. Spacing 100 and wavelength 200 both divide the tile.
"""
import math

from common import run

W = H = 800
INK = "#14161c"
IVORY = "#e6dfcf"
S = 100
LAM = 200
AMP = 14
WIDTH = 12
HALO = WIDTH + 8
REACH = 24


def hpath(y0, x_from, x_to):
    pts, x = [], x_from
    while x <= x_to:
        pts.append((x, y0 + AMP * math.sin(2 * math.pi * x / LAM)))
        x += 4
    return pts


def vpath(x0, y_from, y_to):
    pts, y = [], y_from
    while y <= y_to:
        pts.append((x0 + AMP * math.sin(2 * math.pi * y / LAM), y))
        y += 4
    return pts


def stroke(t, pts, width, color):
    t.pensize(width)
    t.pencolor(color)
    t.goto(pts[0])
    t.pendown()
    for p in pts[1:]:
        t.goto(p)
    t.penup()


def draw(t):
    ys = [-H / 2 + S / 2 + i * S for i in range(H // S)]
    xs = [-W / 2 + S / 2 + j * S for j in range(W // S)]
    for y0 in ys:
        stroke(t, hpath(y0, -W / 2 - 10, W / 2 + 10), WIDTH, IVORY)
    for x0 in xs:
        pts = vpath(x0, -H / 2 - 10, H / 2 + 10)
        stroke(t, pts, HALO, INK)
        stroke(t, pts, WIDTH, IVORY)
    # every second crossing: horizontal ribbon back on top. The ivory stroke runs past the
    # halo so the halo's round caps never bite into the ribbon itself.
    for i, y0 in enumerate(ys):
        for j, x0 in enumerate(xs):
            if (i + j) % 2 == 0:
                cx = x0 + AMP * math.sin(2 * math.pi * y0 / LAM)
                stroke(t, hpath(y0, cx - REACH, cx + REACH), HALO, INK)
                stroke(t, hpath(y0, cx - REACH - 8, cx + REACH + 8), WIDTH, IVORY)


if __name__ == "__main__":
    run(draw, W, H, INK)

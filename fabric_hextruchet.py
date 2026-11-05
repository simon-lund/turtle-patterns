"""Hex Truchet: hexagonal tiles with arcs joining edge midpoints, chosen at random per cell.

Five tile variants (two all-arc tiles and three with a straight bar) are placed by a seeded
coin on a hexagonal torus of 12 x 12 cells, so the ivory paths close across the tile edges.
Tile 840 x 728 so that the hexagons stay regular.
"""
import math
import random

from common import run

W, H = 840, 728
COLS = ROWS = 12
HW = W / COLS
RH = H / ROWS
SIDE = RH / 1.5
APOTHEM = HW / 2
INK = "#14161c"
IVORY = "#e6dfcf"
SEED = 4
WIDTH = 6


def midpoint(cx, cy, k):
    a = math.radians(60 * k)
    return (cx + APOTHEM * math.cos(a), cy + APOTHEM * math.sin(a))


def vertex(cx, cy, k):
    a = math.radians(60 * k + 30)
    return (cx + SIDE * math.cos(a), cy + SIDE * math.sin(a))


def stroke(t, pts):
    t.goto(pts[0])
    t.pendown()
    for p in pts[1:]:
        t.goto(p)
    t.penup()


def arc(t, cx, cy, k):
    # from midpoint k to midpoint k + 1, bending around the vertex between them
    vx, vy = vertex(cx, cy, k)
    m0, m1 = midpoint(cx, cy, k), midpoint(cx, cy, k + 1)
    a0 = math.atan2(m0[1] - vy, m0[0] - vx)
    a1 = math.atan2(m1[1] - vy, m1[0] - vx)
    sweep = ((a1 - a0 + math.pi) % (2 * math.pi)) - math.pi
    r = SIDE / 2
    stroke(t, [(vx + r * math.cos(a0 + sweep * s / 14), vy + r * math.sin(a0 + sweep * s / 14))
               for s in range(15)])


def bar(t, cx, cy, k):
    stroke(t, [midpoint(cx, cy, k), midpoint(cx, cy, k + 3)])


def tile(t, cx, cy, variant):
    if variant < 2:
        for k in (variant, variant + 2, variant + 4):
            arc(t, cx, cy, k)
    else:
        r = variant - 2
        arc(t, cx, cy, r)
        arc(t, cx, cy, r + 3)
        bar(t, cx, cy, r + 1)


def draw(t):
    random.seed(SEED)
    choice = {(i, j): random.randrange(5) for i in range(COLS) for j in range(ROWS)}
    t.pensize(WIDTH)
    t.pencolor(IVORY)
    for j in range(-1, ROWS + 1):
        for i in range(-1, COLS + 1):
            cx = -W / 2 + HW / 2 + i * HW + (HW / 2 if j % 2 else 0)
            cy = -H / 2 + j * RH
            tile(t, cx, cy, choice[(i % COLS, j % ROWS)])


if __name__ == "__main__":
    run(draw, W, H, INK)

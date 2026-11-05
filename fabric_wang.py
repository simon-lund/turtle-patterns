"""Wang blobs: corner-colored Wang tiles that melt into rounded two-tone islands.

Every grid vertex gets a random bit. A cell is drawn from its four corner bits: a quarter disc
at each set corner, joined by a bar when two neighbouring corners are set. Sixteen cell types,
one for each corner combination, and the grid wraps.
"""
import math
import random

from common import polygon, run

W = H = 800
N = 16
CELL = W / N
INK = "#14161c"
IVORY = "#e6dfcf"
SEED = 21


def sector(t, cx, cy, r, a0, a1):
    pts = [(cx, cy)]
    for k in range(13):
        a = math.radians(a0 + (a1 - a0) * k / 12)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    polygon(t, pts, IVORY)


def rect(t, x, y, w, h):
    polygon(t, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], IVORY)


def draw(t):
    random.seed(SEED)
    bits = {(i, j): random.random() < 0.5 for i in range(N) for j in range(N)}
    r = CELL / 2
    for i in range(N):
        for j in range(N):
            x0, y0 = -W / 2 + i * CELL, -H / 2 + j * CELL
            bl, br = bits[(i, j)], bits[((i + 1) % N, j)]
            tl, tr = bits[(i, (j + 1) % N)], bits[((i + 1) % N, (j + 1) % N)]
            if bl:
                sector(t, x0, y0, r, 0, 90)
            if br:
                sector(t, x0 + CELL, y0, r, 90, 180)
            if tr:
                sector(t, x0 + CELL, y0 + CELL, r, 180, 270)
            if tl:
                sector(t, x0, y0 + CELL, r, 270, 360)
            if bl and br:
                rect(t, x0, y0, CELL, r)
            if tl and tr:
                rect(t, x0, y0 + r, CELL, r)
            if bl and tl:
                rect(t, x0, y0, r, CELL)
            if br and tr:
                rect(t, x0 + r, y0, r, CELL)


if __name__ == "__main__":
    run(draw, W, H, INK)

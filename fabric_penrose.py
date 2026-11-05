"""Penrose medallion: a sun of Penrose rhombi, grown by six rounds of deflation.

Robinson triangles are split by the golden ratio until the rhombi are about 20 px, thin ones
in deep teal and thick ones lighter, with gold edges. One decagonal medallion fills the tile,
so the repeat is a grid of medallions on an ink ground.
"""
import cmath
import math

from common import run

W = H = 800
PHI = (1 + 5 ** 0.5) / 2
DEPTH = 6
RADIUS = 390
INK = "#0f0f14"
THIN = "#15454d"
THICK = "#2a6b73"
GOLD = "#c9a24a"


def subdivide(tris):
    out = []
    for kind, a, b, c in tris:
        if kind == 0:
            p = a + (b - a) / PHI
            out += [(0, c, p, b), (1, p, c, a)]
        else:
            q = b + (a - b) / PHI
            r = b + (c - b) / PHI
            out += [(1, r, c, a), (0, q, r, b), (1, r, q, a)]
    return out


def draw(t):
    tris = []
    for i in range(10):
        b = cmath.rect(1, (2 * i - 1) * math.pi / 10)
        c = cmath.rect(1, (2 * i + 1) * math.pi / 10)
        if i % 2 == 0:
            b, c = c, b
        tris.append((0, 0j, b, c))
    for _ in range(DEPTH):
        tris = subdivide(tris)
    t.pensize(1)
    for kind, a, b, c in tris:
        pa, pb, pc = [(z.real * RADIUS, z.imag * RADIUS) for z in (a, b, c)]
        t.fillcolor(THIN if kind == 0 else THICK)
        t.goto(pa)
        t.begin_fill()
        t.goto(pb)
        t.goto(pc)
        t.goto(pa)
        t.end_fill()
        # rhombus edges meet at a; the edge b-c is the rhombus diagonal and stays hidden
        t.pencolor(GOLD)
        t.goto(pc)
        t.pendown()
        t.goto(pa)
        t.goto(pb)
        t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

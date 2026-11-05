"""Pythagorean tiling: two sizes of square that tile the plane with no gaps.

Big squares of side 3 and small squares of side 1, on the skew lattice spanned by (3, 1) and
(-1, 3). That lattice contains (10, 0) and (0, 10), so with a 20 px unit the period is 200 px.
"""
from common import polygon, run

W = H = 800
UNIT = 20
A, B = 3, 1
INK = "#0f0f14"
BIG = "#15454d"
SMALL = "#c9a24a"


def square(t, x, y, side, color):
    polygon(t, [(x, y), (x + side, y), (x + side, y + side), (x, y + side)], color, INK, 1.5)


def draw(t):
    v1, v2 = (A * UNIT, B * UNIT), (-B * UNIT, A * UNIT)
    for m in range(-10, 11):
        for n in range(-10, 11):
            px, py = m * v1[0] + n * v2[0], m * v1[1] + n * v2[1]
            if abs(px) > W / 2 + 4 * UNIT or abs(py) > H / 2 + 4 * UNIT:
                continue
            square(t, px, py, A * UNIT, BIG)
            square(t, px + A * UNIT, py, B * UNIT, SMALL)


if __name__ == "__main__":
    run(draw, W, H, INK)

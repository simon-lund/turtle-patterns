"""Asanoha: the Japanese hemp-leaf sashiko pattern, gold thread on charcoal.

A triangular grid where every triangle also gets three spokes from its center. Row height is
rounded from 57.74 to 57.14 px (1 percent) so fourteen rows fit the 800 px tile exactly.
"""
from common import run

W = H = 800
CHARCOAL = "#1c1c20"
GOLD = "#c9a24a"
COLS = 12
ROWS = 14
A = W / COLS
HGT = H / ROWS


def leaf(t, p, q, r):
    c = ((p[0] + q[0] + r[0]) / 3, (p[1] + q[1] + r[1]) / 3)
    for a, b in ((p, q), (q, r), (r, p), (c, p), (c, q), (c, r)):
        t.goto(a)
        t.pendown()
        t.goto(b)
        t.penup()


def draw(t):
    t.pensize(1.5)
    t.pencolor(GOLD)
    for j in range(-1, ROWS + 1):
        y0 = -H / 2 + j * HGT
        y1 = y0 + HGT
        offset = A / 2 if j % 2 else 0
        for i in range(-1, COLS + 1):
            x = -W / 2 + i * A + offset
            leaf(t, (x, y0), (x + A, y0), (x + A / 2, y1))
            leaf(t, (x + A / 2, y1), (x + A, y0), (x + 3 * A / 2, y1))


if __name__ == "__main__":
    run(draw, W, H, CHARCOAL)

"""Spiro lace: two different spirograph roses on alternate cells, overlapping into lace.

Hypotrochoids with a 4:1 and a 3:1 ratio, gold and ivory on plum. Cell size 100 divides the
tile, and the two-cell alternation gives a period of 200.
"""
import math

from common import run

W = H = 800
PLUM = "#2a1a2e"
GOLD = "#c9a24a"
IVORY = "#efe6d3"
S = 100
PTS = 400


def rose(t, cx, cy, R, r, d, color):
    t.pencolor(color)
    k = (R - r) / r
    first = True
    for n in range(PTS + 1):
        th = 2 * math.pi * n / PTS
        p = (cx + (R - r) * math.cos(th) + d * math.cos(k * th),
             cy + (R - r) * math.sin(th) - d * math.sin(k * th))
        t.goto(p)
        if first:
            t.pendown()
            first = False
    t.penup()


def draw(t):
    t.pensize(1.3)
    for i in range(-1, W // S + 1):
        for j in range(-1, H // S + 1):
            cx, cy = -W / 2 + S / 2 + i * S, -H / 2 + S / 2 + j * S
            if (i + j) % 2 == 0:
                rose(t, cx, cy, 60, 12, 22, GOLD)
            else:
                rose(t, cx, cy, 60, 15, 20, IVORY)


if __name__ == "__main__":
    run(draw, W, H, PLUM)

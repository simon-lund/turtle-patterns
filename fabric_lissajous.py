"""Lissajous lace: a 3:2 Lissajous knot in every cell, phase flipped on alternate cells.

The curves are a little wider than the cells, so neighbours overlap into a lattice of knots.
Cell size 100 and the two-cell color period both divide the tile.
"""
import math

from common import run

W = H = 800
GREEN = "#0f2a24"
GOLD = "#c9a24a"
IVORY = "#e6dfcf"
S = 100
A = 56
PTS = 240


def knot(t, cx, cy, phase, color):
    t.pencolor(color)
    first = True
    for k in range(PTS + 1):
        th = 2 * math.pi * k / PTS
        p = (cx + A * math.sin(3 * th + phase), cy + A * math.sin(2 * th))
        t.goto(p)
        if first:
            t.pendown()
            first = False
    t.penup()


def draw(t):
    t.pensize(1.5)
    for i in range(-1, W // S + 1):
        for j in range(-1, H // S + 1):
            even = (i + j) % 2 == 0
            knot(t, -W / 2 + S / 2 + i * S, -H / 2 + S / 2 + j * S,
                 math.pi / 2 if even else 0, GOLD if even else IVORY)


if __name__ == "__main__":
    run(draw, W, H, GREEN)

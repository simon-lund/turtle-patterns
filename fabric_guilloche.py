"""Guilloche: the engraved ribbons of banknotes and watch dials, as bands of fine lines.

Each band is eighteen sine curves with evenly spaced phases, so their crossings weave a rope
illusion; brightness follows the phase to give the rope its shading. Alternate bands are
mirrored and swap gold for ivory. Every wave count is a whole number, so the bands wrap.
"""
import math

from common import mix, run

W = H = 800
INK = "#0f1216"
GOLD = (0.79, 0.64, 0.29)
DIM = (0.36, 0.30, 0.14)
IVORY = (0.90, 0.87, 0.81)
DUSK = (0.42, 0.42, 0.40)
BAND = 100
LINES = 18


def draw(t):
    t.pensize(1)
    for b in range(H // BAND):
        y0 = -H / 2 + b * BAND + BAND / 2
        flip = -1 if b % 2 else 1
        lo, hi = (DUSK, IVORY) if b % 2 else (DIM, GOLD)
        for k in range(LINES):
            phase = 2 * math.pi * k / LINES
            t.pencolor(mix(lo, hi, 0.5 + 0.5 * math.cos(phase)))
            first = True
            x = -W / 2
            while x <= W / 2:
                a = 2 * math.pi * x / W
                y = y0 + flip * (36 * math.sin(2 * a + phase) + 8 * math.sin(6 * a - 2 * phase))
                t.goto(x, y)
                if first:
                    t.pendown()
                    first = False
                x += 4
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

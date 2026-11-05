"""Dial: a guilloche rosette like an engraved watch face, one medallion per tile.

Seven rings, each drawn as twenty-four phase-shifted rose curves whose crossings weave the
rope illusion of engine turning. Rings alternate gold and ivory, lobe counts grow outward.
Repeats as a block.
"""
import math

from common import mix, run

W = H = 800
INK = "#0f1216"
GOLD = (0.79, 0.64, 0.29)
DIM = (0.36, 0.30, 0.14)
IVORY = (0.90, 0.87, 0.81)
DUSK = (0.42, 0.42, 0.40)
RINGS = 7
LINES = 24
PTS = 480


def draw(t):
    t.pensize(1)
    for ring in range(RINGS):
        r0 = 60 + ring * 50
        lobes = 12 + ring * 4
        lo, hi = (DIM, GOLD) if ring % 2 == 0 else (DUSK, IVORY)
        for k in range(LINES):
            phase = 2 * math.pi * k / LINES
            t.pencolor(mix(lo, hi, 0.5 + 0.5 * math.cos(phase)))
            first = True
            for n in range(PTS + 1):
                th = 2 * math.pi * n / PTS
                r = r0 + 18 * math.sin(lobes * th + phase) + 6 * math.sin(2 * lobes * th - phase)
                t.goto(r * math.cos(th), r * math.sin(th))
                if first:
                    t.pendown()
                    first = False
            t.penup()
    t.goto(0, 0)
    t.dot(14, GOLD)
    t.dot(6, INK)


if __name__ == "__main__":
    run(draw, W, H, INK)

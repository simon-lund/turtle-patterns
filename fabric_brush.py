"""Brush: long tapered strokes following a slow periodic field, like hair or ink brushwork.

Fewer and longer threads than the current pattern, each one thickening in the middle and
thinning to a point at both ends. The field wraps, so strokes that leave one edge continue
from the other. Change SEED for a new sheet.
"""
import math
import random

from common import run, torus_segment

W = H = 800
INK = "#0f1216"
PALETTE = [(0.79, 0.64, 0.29), (0.90, 0.87, 0.81), (0.19, 0.46, 0.50), (0.54, 0.45, 0.25)]
SEED = 17
STROKES = 240
STEPS = 220
STEP = 3


def angle(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    return math.sin(a + 0.4) + 0.8 * math.cos(2 * b + 0.7) + 0.6 * math.sin(a + b)


def draw(t):
    random.seed(SEED)
    for _ in range(STROKES):
        x, y = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        t.pencolor(random.choice(PALETTE))
        t.goto(x, y)
        t.pendown()
        for s in range(STEPS):
            t.pensize(0.5 + 5.5 * math.sin(math.pi * s / STEPS) ** 1.4)
            th = angle(x, y)
            x, y = torus_segment(t, (x, y), (x + STEP * math.cos(th), y + STEP * math.sin(th)), W, H)
        t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

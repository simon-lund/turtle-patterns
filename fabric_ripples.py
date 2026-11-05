"""Ripples: threads riding the crests of waves from four sources that interfere on a torus.

Each thread follows a level line of the summed wave field, so it traces a ring where the
ripples agree and wavers where they cancel. Ivory on the crests, gold between, teal in the
troughs. Change SEED to move the sources.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
TEAL = (0.19, 0.46, 0.50)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 9
SOURCES = 4
WAVELENGTH = 58
SEEDS = 24
STEPS = 120
STEP = 2.5


def distance(x, y, sx, sy):
    # periodic distance: exact near the source, smooth everywhere, wraps at the edges
    a, b = 2 * math.pi * (x - sx) / W, 2 * math.pi * (y - sy) / H
    return math.sqrt(max(0.0, 2 - math.cos(a) - math.cos(b))) * W * math.sqrt(2) / (2 * math.pi)


def field(sources, x, y):
    return sum(math.sin(2 * math.pi * distance(x, y, sx, sy) / WAVELENGTH) for sx, sy in sources)


def along_crest(sources, x, y):
    e = 0.5
    gx = (field(sources, x + e, y) - field(sources, x - e, y)) / (2 * e)
    gy = (field(sources, x, y + e) - field(sources, x, y - e)) / (2 * e)
    n = math.hypot(gx, gy) or 1e-9
    return -gy / n, gx / n


def shade(v):
    s = max(-1, min(1, v / 2.5))
    return mix(GOLD, IVORY, s) if s > 0 else mix(GOLD, TEAL, -s)


def draw(t):
    random.seed(SEED)
    sources = [(random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)) for _ in range(SOURCES)]
    t.pensize(1.3)
    for i in range(SEEDS):
        for j in range(SEEDS):
            x = -W / 2 + (i + random.random()) * W / SEEDS
            y = -H / 2 + (j + random.random()) * H / SEEDS
            t.pencolor(shade(field(sources, x, y)))
            t.goto(x, y)
            t.pendown()
            for _ in range(STEPS):
                ux, uy = along_crest(sources, x, y)
                ux, uy = along_crest(sources, x + 0.5 * STEP * ux, y + 0.5 * STEP * uy)
                x, y = torus_segment(t, (x, y), (x + STEP * ux, y + STEP * uy), W, H)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

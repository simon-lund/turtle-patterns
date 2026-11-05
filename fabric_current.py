"""Current: hundreds of threads following a flow field, like marbled silk.

The field is a sum of sines whose wavelengths divide the tile, so it is periodic by
construction, and a thread that leaves one edge continues from the opposite edge. Thread color
comes from a second periodic field, so colors drift in currents instead of being scattered.
Change SEED for a tile nobody has seen before.
"""
import math
import random

from common import run, torus_segment

W = H = 800
INK = "#101418"
PALETTE = ["#c9a24a", "#8a7340", "#d8cfb8", "#4f6b6e"]
SEED = 9
SEEDS = 24
STEPS = 110
STEP = 2.5


def angle(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    v = (math.sin(2 * a) + math.cos(3 * b + 0.5)
         + 0.8 * math.sin(a + 2 * b) + 0.6 * math.cos(3 * a - b + 1.0))
    return v * 1.1


def shade(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    v = math.sin(3 * a + 0.7) + math.cos(2 * b)
    return PALETTE[min(3, int((v + 2) / 4 * 4))]


def draw(t):
    random.seed(SEED)
    t.pensize(1.6)
    for i in range(SEEDS):
        for j in range(SEEDS):
            x = -W / 2 + (i + random.random()) * W / SEEDS
            y = -H / 2 + (j + random.random()) * H / SEEDS
            t.pencolor(shade(x, y))
            t.goto(x, y)
            t.pendown()
            for _ in range(STEPS):
                th = angle(x, y)
                x, y = torus_segment(t, (x, y), (x + STEP * math.cos(th), y + STEP * math.sin(th)), W, H)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

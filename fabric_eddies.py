"""Eddies: threads caught in a checkerboard of whirlpools, teal one way and gold the other.

The flow is a cellular vortex field (a Taylor-Green flow with an extra wave) whose stream
function is periodic, so threads that leave one edge return from the other. Each thread takes
the color of the vortex it circles, and fades to ivory on the lines between vortices.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
TEAL = (0.19, 0.46, 0.50)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 4
SEEDS = 26
STEPS = 150
STEP = 2.5


def psi(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    return math.sin(2 * a) * math.sin(2 * b) + 0.35 * math.sin(3 * a + 1.3) * math.cos(b + 0.4)


def velocity(x, y):
    e = 0.5
    vx = (psi(x, y + e) - psi(x, y - e)) / (2 * e)
    vy = -(psi(x + e, y) - psi(x - e, y)) / (2 * e)
    n = math.hypot(vx, vy) or 1e-9
    return vx / n, vy / n


def shade(v):
    if v < 0:
        return mix(IVORY, TEAL, min(1, -v / 0.9))
    return mix(IVORY, GOLD, min(1, v / 0.9))


def draw(t):
    random.seed(SEED)
    t.pensize(1.5)
    for i in range(SEEDS):
        for j in range(SEEDS):
            x = -W / 2 + (i + random.random()) * W / SEEDS
            y = -H / 2 + (j + random.random()) * H / SEEDS
            t.pencolor(shade(psi(x, y)))
            t.goto(x, y)
            t.pendown()
            for _ in range(STEPS):
                ux, uy = velocity(x, y)
                ux, uy = velocity(x + 0.5 * STEP * ux, y + 0.5 * STEP * uy)
                x, y = torus_segment(t, (x, y), (x + STEP * ux, y + STEP * uy), W, H)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

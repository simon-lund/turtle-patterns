"""Vortices: threads spiraling around five point vortices on a torus, like a sky of galaxies.

The flow is the periodic stream function of alternating vortices, plus a slight drift that
makes threads spiral out of the gold ones and into the teal ones. Change SEED to move them.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
TEAL = (0.19, 0.46, 0.50)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 6
VORTICES = 5
MIN_SEP = 150
EPS = 0.02
DRIFT = 0.15
SEEDS = 26
STEPS = 160
STEP = 2.5


def torus_dist(ax, ay, bx, by):
    dx, dy = abs(ax - bx), abs(ay - by)
    return math.hypot(min(dx, W - dx), min(dy, H - dy))


def make_vortices():
    out = []
    while len(out) < VORTICES:
        x, y = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        if all(torus_dist(x, y, vx, vy) >= MIN_SEP for vx, vy, _ in out):
            out.append((x, y, 1 if len(out) % 2 == 0 else -1))
    return out


def psi(vortices, x, y):
    s = 0
    for vx, vy, g in vortices:
        s -= g * math.log(2 - math.cos(2 * math.pi * (x - vx) / W)
                          - math.cos(2 * math.pi * (y - vy) / H) + EPS)
    return s


def velocity(vortices, x, y):
    e = 0.5
    gx = (psi(vortices, x + e, y) - psi(vortices, x - e, y)) / (2 * e)
    gy = (psi(vortices, x, y + e) - psi(vortices, x, y - e)) / (2 * e)
    vx, vy = gy - DRIFT * gx, -gx - DRIFT * gy
    n = math.hypot(vx, vy) or 1e-9
    return vx / n, vy / n


def shade(v):
    s = math.tanh(v / 2.5)
    return mix(IVORY, GOLD, s) if s > 0 else mix(IVORY, TEAL, -s)


def draw(t):
    random.seed(SEED)
    vortices = make_vortices()
    t.pensize(1.4)
    for i in range(SEEDS):
        for j in range(SEEDS):
            x = -W / 2 + (i + random.random()) * W / SEEDS
            y = -H / 2 + (j + random.random()) * H / SEEDS
            t.pencolor(shade(psi(vortices, x, y)))
            t.goto(x, y)
            t.pendown()
            for _ in range(STEPS):
                ux, uy = velocity(vortices, x, y)
                ux, uy = velocity(vortices, x + 0.5 * STEP * ux, y + 0.5 * STEP * uy)
                x, y = torus_segment(t, (x, y), (x + STEP * ux, y + STEP * uy), W, H)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

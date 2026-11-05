"""Field lines: iron filings around six magnetic poles scattered over a torus.

A periodic potential is built from the poles and lines are traced down its gradient from every
positive pole until they reach a negative one, then the same from the negative poles upward.
Gold near positive poles, teal near negative ones, ivory in between.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
TEAL = (0.19, 0.46, 0.50)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 3
PAIRS = 3
LINES = 44
STEP = 2
MAX_STEPS = 800
EPS = 0.015
START_R = 10
STOP_R = 9
MIN_SEP = 180


def torus_dist(ax, ay, bx, by):
    dx, dy = abs(ax - bx), abs(ay - by)
    return math.hypot(min(dx, W - dx), min(dy, H - dy))


def make_poles():
    poles = []
    while len(poles) < 2 * PAIRS:
        x, y = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        if all(torus_dist(x, y, px, py) >= MIN_SEP for px, py, _ in poles):
            poles.append((x, y, 1 if len(poles) % 2 == 0 else -1))
    return poles


def potential(poles, x, y):
    s = 0
    for px, py, q in poles:
        s -= q * math.log(2 - math.cos(2 * math.pi * (x - px) / W)
                          - math.cos(2 * math.pi * (y - py) / H) + EPS)
    return s


def direction(poles, x, y, sign):
    e = 0.5
    gx = (potential(poles, x + e, y) - potential(poles, x - e, y)) / (2 * e)
    gy = (potential(poles, x, y + e) - potential(poles, x, y - e)) / (2 * e)
    n = math.hypot(gx, gy) or 1e-9
    return sign * gx / n, sign * gy / n


def shade(v):
    s = math.tanh(v / 3)
    return mix(IVORY, GOLD, s) if s > 0 else mix(IVORY, TEAL, -s)


def draw(t):
    random.seed(SEED)
    poles = make_poles()
    t.pensize(1.3)
    for px, py, q in poles:
        targets = [(tx, ty) for tx, ty, tq in poles if tq == -q]
        for k in range(LINES):
            a = 2 * math.pi * (k + 0.5) / LINES
            x, y = px + START_R * math.cos(a), py + START_R * math.sin(a)
            t.goto(x, y)
            t.pendown()
            for _ in range(MAX_STEPS):
                t.pencolor(shade(potential(poles, x, y)))
                ux, uy = direction(poles, x, y, -q)
                x, y = torus_segment(t, (x, y), (x + STEP * ux, y + STEP * uy), W, H)
                if any(torus_dist(x, y, tx, ty) < STOP_R for tx, ty in targets):
                    break
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

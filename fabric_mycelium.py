"""Mycelium: six fungal colonies growing outward from their spores, like a petri dish.

Every hypha heads away from its spore with a little random turning, splits now and then at a
shallow angle, and stops at the colony edge. Gold near the spore, ivory at the rim. Colonies
near the tile edge continue on the other side. Change SEED for a different culture.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 23
COLONIES = 6
RADIUS = 190
MIN_SEP = 230
INITIAL = 9
STEP = 2
TURN = 0.035
BRANCH = 0.03
MAX_STEPS = 160
MAX_TIPS = 420


def torus_dist(ax, ay, bx, by):
    dx, dy = abs(ax - bx), abs(ay - by)
    return math.hypot(min(dx, W - dx), min(dy, H - dy))


def draw(t):
    random.seed(SEED)
    spores = []
    attempts = 0
    while len(spores) < COLONIES:
        x, y = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        attempts += 1
        if attempts > 20000 or all(torus_dist(x, y, sx, sy) >= MIN_SEP for sx, sy in spores):
            spores.append((x, y))
    for sx, sy in spores:
        tips = [(sx, sy, 2 * math.pi * k / INITIAL + random.uniform(-0.2, 0.2), 0)
                for k in range(INITIAL)]
        born = len(tips)
        while tips:
            x, y, heading, depth = tips.pop()
            t.pensize(max(0.6, 2.8 - 0.55 * depth))
            t.goto(x, y)
            t.pendown()
            for _ in range(MAX_STEPS):
                d = torus_dist(x, y, sx, sy)
                if d > RADIUS * random.uniform(0.85, 1.0):
                    break
                t.pencolor(mix(GOLD, IVORY, d / RADIUS))
                heading += random.gauss(0, TURN)
                x, y = torus_segment(t, (x, y), (x + STEP * math.cos(heading), y + STEP * math.sin(heading)), W, H)
                if random.random() < BRANCH and depth < 5 and born < MAX_TIPS:
                    side = random.choice((-1, 1)) * random.uniform(0.25, 0.55)
                    tips.append((x, y, heading + side, depth + 1))
                    born += 1
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

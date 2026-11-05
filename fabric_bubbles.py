"""Terrazzo: circles thrown at random onto a torus and kept only when they fit.

Thousands of candidate circles, each kept if it overlaps nothing already placed, including
across the tile edges. Three tones with an ink outline on an ink ground.
"""
import random

from common import run

W = H = 800
TRIES = 4000
R_MIN, R_MAX = 10, 46
GAP = 4
SEED = 6
INK = "#0f0f14"
TONES = ["#d9cdb4", "#1f4e5a", "#c9a24a"]


def torus_dist(ax, ay, bx, by):
    dx, dy = abs(ax - bx), abs(ay - by)
    return (min(dx, W - dx) ** 2 + min(dy, H - dy) ** 2) ** 0.5


def draw(t):
    random.seed(SEED)
    circles = []
    for _ in range(TRIES):
        r = random.uniform(R_MIN, R_MAX)
        x, y = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        if all(torus_dist(x, y, cx, cy) >= r + cr + GAP for cx, cy, cr, _ in circles):
            circles.append((x, y, r, random.choice(TONES)))
    t.pensize(2)
    t.pencolor(INK)
    for x, y, r, tone in circles:
        t.fillcolor(tone)
        for dx in (-W, 0, W):
            for dy in (-H, 0, H):
                if abs(x + dx) > W / 2 + r or abs(y + dy) > H / 2 + r:
                    continue
                t.goto(x + dx, y + dy - r)
                t.setheading(0)
                t.pendown()
                t.begin_fill()
                t.circle(r)
                t.end_fill()
                t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

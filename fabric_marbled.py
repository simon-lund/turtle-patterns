"""Marbled: mathematical paper marbling on a torus, drops of color combed into feathers.

Every drop pushes whatever is already on the surface outward, every comb drags the surface
along a row of tines. Both are written as periodic deformations with compact support, so the
marbling wraps. Change SEED for a sheet nobody has marbled before.
"""
import math
import random

from common import polygon, run

W = H = 800
INK = "#0f1216"
COLORS = ["#15454d", "#c9a24a", "#e6dfcf", "#2a6b73", "#8a7340", "#0f1216"]
SEED = 12
BIG, SMALL = 16, 44
POINTS = 360


def drop_map(px, py, cx, cy, r):
    # a drop of radius r at (cx, cy) pushes a point outward; influence ends at 4 r
    rc, r1 = 4 * r, 2 * r
    for dx in (-W, 0, W):
        for dy in (-H, 0, H):
            ox, oy = cx + dx, cy + dy
            d = math.hypot(px - ox, py - oy)
            if d >= rc or d < 1e-9:
                continue
            w = 1 if d <= r1 else 0.5 * (1 + math.cos(math.pi * (d - r1) / (rc - r1)))
            nd = d + (math.sqrt(d * d + r * r) - d) * w
            return (ox + (px - ox) * nd / d, oy + (py - oy) * nd / d)
    return (px, py)


def comb(drops, vertical, tines, amplitude, alpha):
    # vertical combs drag along y with tines at fixed x; horizontal combs the other way
    period = W if vertical else H
    offsets = [random.uniform(0, period) + k * period / tines for k in range(tines)]
    for _, pts in drops:
        for k, (x, y) in enumerate(pts):
            s = x if vertical else y
            pull = amplitude * sum(math.exp(-alpha * (1 - math.cos(2 * math.pi * (s - o) / period)))
                                   for o in offsets)
            pts[k] = (x, y - pull) if vertical else (x + pull, y)


def draw(t):
    random.seed(SEED)
    drops = []
    for n in range(BIG + SMALL):
        r = random.uniform(70, 100) if n < BIG else random.uniform(25, 55)
        cx, cy = random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2)
        for _, pts in drops:
            for k, (px, py) in enumerate(pts):
                pts[k] = drop_map(px, py, cx, cy, r)
        circle = [(cx + r * math.cos(2 * math.pi * k / POINTS), cy + r * math.sin(2 * math.pi * k / POINTS))
                  for k in range(POINTS)]
        drops.append((COLORS[n % len(COLORS)], circle))
    comb(drops, True, 22, 70, 60)
    comb(drops, False, 6, 38, 10)
    comb(drops, True, 9, 28, 14)
    for color, pts in drops:
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        for dx in (-W, 0, W):
            for dy in (-H, 0, H):
                if (max(xs) + dx < -W / 2 or min(xs) + dx > W / 2
                        or max(ys) + dy < -H / 2 or min(ys) + dy > H / 2):
                    continue
                polygon(t, [(x + dx, y + dy) for x, y in pts], color)


if __name__ == "__main__":
    run(draw, W, H, INK)

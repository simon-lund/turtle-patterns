"""Voronoi crackle: cells around seeds scattered on a torus, like crazed glaze.

Seeds keep a minimum distance from each other. Each cell is cut from a large square by the
bisector of every other seed, including the wrapped copies, so cells crossing the edge continue
on the other side.
"""
import random

from common import polygon, run

W = H = 800
COUNT = 45
MIN_DIST = 55
SEED = 8
TONES = ["#1f4e5a", "#15454d", "#2a6b73"]
LINE = "#c9a24a"


def torus_dist(p, q):
    dx, dy = abs(p[0] - q[0]), abs(p[1] - q[1])
    return (min(dx, W - dx) ** 2 + min(dy, H - dy) ** 2) ** 0.5


def clip(poly, p, q):
    # keep the part of poly closer to p than to q
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    nx, ny = q[0] - p[0], q[1] - p[1]
    side = lambda v: (v[0] - mx) * nx + (v[1] - my) * ny
    out = []
    for k in range(len(poly)):
        a, b = poly[k], poly[(k + 1) % len(poly)]
        sa, sb = side(a), side(b)
        if sa <= 0:
            out.append(a)
        if (sa < 0 < sb) or (sb < 0 < sa):
            f = sa / (sa - sb)
            out.append((a[0] + f * (b[0] - a[0]), a[1] + f * (b[1] - a[1])))
    return out


def draw(t):
    random.seed(SEED)
    seeds = []
    while len(seeds) < COUNT:
        p = (random.uniform(-W / 2, W / 2), random.uniform(-H / 2, H / 2))
        if all(torus_dist(p, q) >= MIN_DIST for q in seeds):
            seeds.append(p)
    copies = [(x + dx * W, y + dy * H, k) for k, (x, y) in enumerate(seeds)
              for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    for x, y, k in copies:
        if abs(x) > W / 2 + 250 or abs(y) > H / 2 + 250:
            continue
        poly = [(x - 600, y - 600), (x + 600, y - 600), (x + 600, y + 600), (x - 600, y + 600)]
        for qx, qy, _ in copies:
            if (qx, qy) != (x, y) and poly:
                poly = clip(poly, (x, y), (qx, qy))
        if poly:
            polygon(t, poly, TONES[k % 3], LINE, 3)


if __name__ == "__main__":
    run(draw, W, H, "#0f0f14")

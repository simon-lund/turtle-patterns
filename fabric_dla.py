"""Coral: diffusion-limited aggregation on a torus, old growth in dark gold, new in ivory.

Particles wander at random until they touch the cluster and stick, which grows the branching
dendrites of frost, lichen and coral. The grid wraps, so branches that cross one edge
continue from the other.
"""
import math
import random

from common import mix, run

W = H = 800
CELL = 5
N = W // CELL
PARTICLES = 14000
SEEDS = 8
SEED = 2
INK = (0.06, 0.06, 0.08)
OLD = (0.54, 0.45, 0.25)
NEW = (0.90, 0.87, 0.81)


def draw(t):
    random.seed(SEED)
    cluster = {}
    for _ in range(SEEDS):
        cluster[(random.randrange(N), random.randrange(N))] = 0
    cells = list(cluster)
    for n in range(1, PARTICLES + 1):
        ci, cj = random.choice(cells)
        ang, dist = random.random() * 2 * math.pi, random.uniform(8, 14)
        i, j = int(ci + dist * math.cos(ang)) % N, int(cj + dist * math.sin(ang)) % N
        if (i, j) in cluster:
            continue
        for _ in range(3000):
            if (((i + 1) % N, j) in cluster or ((i - 1) % N, j) in cluster
                    or (i, (j + 1) % N) in cluster or (i, (j - 1) % N) in cluster):
                cluster[(i, j)] = n
                cells.append((i, j))
                break
            di, dj = random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
            i, j = (i + di) % N, (j + dj) % N
    for (i, j), n in cluster.items():
        t.goto(-W / 2 + (i + 0.5) * CELL, -H / 2 + (j + 0.5) * CELL)
        t.dot(6, mix(OLD, NEW, n / PARTICLES))


if __name__ == "__main__":
    run(draw, W, H, "#0f0f14")

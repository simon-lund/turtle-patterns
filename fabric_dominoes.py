"""Dominoes: a random domino tiling of a torus, in the four colors mathematicians use.

Start from rows of horizontal dominoes, then apply tens of thousands of random flips, where a
2 x 2 block of two parallel dominoes turns by 90 degrees. Color marks orientation and parity,
the convention from arctic-circle pictures. The grid wraps, so the tile repeats seamlessly.
"""
import random

from common import polygon, run

W = H = 800
N = 32
CELL = W / N
INK = "#14161c"
COLORS = {("h", 0): "#c9a24a", ("h", 1): "#8a7340", ("v", 0): "#e6dfcf", ("v", 1): "#4f6b6e"}
FLIPS = 80000
SEED = 3
GAP = 1.5


def draw(t):
    random.seed(SEED)
    partner = {}
    for j in range(N):
        for i in range(0, N, 2):
            partner[(i, j)], partner[(i + 1, j)] = (i + 1, j), (i, j)
    for _ in range(FLIPS):
        i, j = random.randrange(N), random.randrange(N)
        a, b = (i, j), ((i + 1) % N, j)
        c, d = (i, (j + 1) % N), ((i + 1) % N, (j + 1) % N)
        if partner[a] == b and partner[c] == d:
            partner[a], partner[c], partner[b], partner[d] = c, a, d, b
        elif partner[a] == c and partner[b] == d:
            partner[a], partner[b], partner[c], partner[d] = b, a, d, c
    seen = set()
    for cell, mate in partner.items():
        if cell in seen:
            continue
        seen.update((cell, mate))
        (i, j), (k, l) = cell, mate
        if j == l:
            orient, i0, j0, w, h = "h", (i if (k - i) % N == 1 else k), j, 2, 1
        else:
            orient, i0, j0, w, h = "v", i, (j if (l - j) % N == 1 else l), 1, 2
        color = COLORS[(orient, (i0 + j0) % 2)]
        # a domino that wraps is drawn twice, once on each side of the edge
        for di, dj in ((0, 0), (-N, 0), (0, -N)):
            x, y = -W / 2 + (i0 + di) * CELL, -H / 2 + (j0 + dj) * CELL
            if x + w * CELL < -W / 2 or y + h * CELL < -H / 2:
                continue
            polygon(t, [(x + GAP, y + GAP), (x + w * CELL - GAP, y + GAP),
                        (x + w * CELL - GAP, y + h * CELL - GAP), (x + GAP, y + h * CELL - GAP)], color)


if __name__ == "__main__":
    run(draw, W, H, INK)

"""Quilt: a square packed with squares, Mrs Perkins's quilt by way of a random quadtree.

The tile splits into four, each quarter splits again with a probability that shrinks with size,
down to 25 px. Every leaf is a patch in one of four tones with an ink seam.
"""
import random

from common import polygon, run

W = H = 800
MIN = 25
SEED = 12
INK = "#14161c"
TONES = ["#d9cdb4", "#1f4e5a", "#c9a24a", "#3b4a63"]
SPLIT = {800: 1.0, 400: 0.85, 200: 0.6, 100: 0.45, 50: 0.3}
GAP = 2


def leaves(x, y, size, out):
    if size > MIN and random.random() < SPLIT.get(size, 0):
        half = size / 2
        for dx, dy in ((0, 0), (half, 0), (0, half), (half, half)):
            leaves(x + dx, y + dy, half, out)
    else:
        out.append((x, y, size))


def draw(t):
    random.seed(SEED)
    out = []
    leaves(-W / 2, -H / 2, W, out)
    for x, y, s in out:
        polygon(t, [(x + GAP, y + GAP), (x + s - GAP, y + GAP),
                    (x + s - GAP, y + s - GAP), (x + GAP, y + s - GAP)], random.choice(TONES))


if __name__ == "__main__":
    run(draw, W, H, INK)

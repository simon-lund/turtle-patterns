"""Labyrinth: a perfect maze carved on a torus by a randomized depth-first search.

Every cell is reachable by exactly one path. The passages are drawn as an ivory ribbon, and
passages that leave one edge of the tile continue from the opposite edge.
"""
import random

from common import run

W = H = 800
N = 32
CELL = W / N
SEED = 7
INK = "#14161c"
IVORY = "#e6dfcf"
WIDTH = 11


def draw(t):
    random.seed(SEED)
    visited = {(0, 0)}
    stack = [(0, 0)]
    edges = []
    while stack:
        i, j = stack[-1]
        options = [(di, dj) for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if ((i + di) % N, (j + dj) % N) not in visited]
        if not options:
            stack.pop()
            continue
        di, dj = random.choice(options)
        nxt = ((i + di) % N, (j + dj) % N)
        visited.add(nxt)
        stack.append(nxt)
        edges.append((i, j, di, dj))
    t.pensize(WIDTH)
    t.pencolor(IVORY)
    for i, j, di, dj in edges:
        x, y = -W / 2 + (i + 0.5) * CELL, -H / 2 + (j + 0.5) * CELL
        # drawn twice so a passage that wraps shows on both sides of the edge
        for sx, sy in ((0, 0), (-di * W, -dj * H)):
            t.goto(x + sx, y + sy)
            t.pendown()
            t.goto(x + sx + di * CELL, y + sy + dj * CELL)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

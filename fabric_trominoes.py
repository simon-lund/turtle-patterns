"""Trominoes: the classic puzzle, a 32 x 32 board with one square missing, tiled by L-trominoes.

The proof is the construction: split the board in four, lay one tromino across the center so
each quarter is missing exactly one square, and recurse. 341 trominoes in four tones, the hole
in gold. Repeats as a block.
"""
import random

from common import polygon, run

W = H = 800
N = 32
CELL = W / N
SEED = 5
HOLE = (20, 13)
INK = "#14161c"
GOLD = "#c9a24a"
TONES = ["#d9cdb4", "#1f4e5a", "#2a6b73", "#3b4a63"]


def tile(x0, y0, size, hx, hy, out):
    if size == 2:
        out.append([(x, y) for x in (x0, x0 + 1) for y in (y0, y0 + 1) if (x, y) != (hx, hy)])
        return
    half = size // 2
    cx, cy = x0 + half, y0 + half
    quadrant = lambda x, y: (x >= cx, y >= cy)
    hole_quadrant = quadrant(hx, hy)
    centers = [(cx - 1, cy - 1), (cx, cy - 1), (cx - 1, cy), (cx, cy)]
    out.append([c for c in centers if quadrant(*c) != hole_quadrant])
    for qx in (False, True):
        for qy in (False, True):
            qx0, qy0 = (cx if qx else x0), (cy if qy else y0)
            if (qx, qy) == hole_quadrant:
                tile(qx0, qy0, half, hx, hy, out)
            else:
                tile(qx0, qy0, half, cx if qx else cx - 1, cy if qy else cy - 1, out)


def draw(t):
    random.seed(SEED)
    pieces = []
    tile(0, 0, N, HOLE[0], HOLE[1], pieces)
    owner = {cell: k for k, piece in enumerate(pieces) for cell in piece}
    for k, piece in enumerate(pieces):
        tone = TONES[k % 4] if k % 7 else random.choice(TONES)
        for i, j in piece:
            x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
            polygon(t, [(x, y), (x + CELL, y), (x + CELL, y + CELL), (x, y + CELL)], tone)
    t.pensize(2)
    t.pencolor(INK)
    for (i, j), k in owner.items():
        x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
        for di, dj, a, b in ((1, 0, (x + CELL, y), (x + CELL, y + CELL)), (-1, 0, (x, y), (x, y + CELL)),
                             (0, 1, (x, y + CELL), (x + CELL, y + CELL)), (0, -1, (x, y), (x + CELL, y))):
            if owner.get((i + di, j + dj)) != k:
                t.goto(a)
                t.pendown()
                t.goto(b)
                t.penup()
    hx, hy = -W / 2 + HOLE[0] * CELL, -H / 2 + HOLE[1] * CELL
    polygon(t, [(hx + 3, hy + 3), (hx + CELL - 3, hy + 3), (hx + CELL - 3, hy + CELL - 3), (hx + 3, hy + CELL - 3)], GOLD)


if __name__ == "__main__":
    run(draw, W, H, INK)

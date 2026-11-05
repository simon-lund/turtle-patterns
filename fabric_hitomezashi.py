"""Hitomezashi: running stitches whose on-off pattern comes from two random bit strings.

Each row and column of the grid gets a bit; stitches alternate along every line, offset by that
bit. The regions this creates can always be colored with two colors, which is done here in
indigo and sand, with the stitches in ivory. Bit counts are kept even so the torus closes.
"""
import random

from common import polygon, run

W = H = 800
N = 32
CELL = W / N
SEED = 14
INDIGO = "#1e2d66"
SAND = "#efe3cd"
IVORY = "#f6f1e6"
STITCH = 3


def bits():
    b = [random.randrange(2) for _ in range(N)]
    if sum(b) % 2:
        b[0] ^= 1
    return b


def draw(t):
    random.seed(SEED)
    rows, cols = bits(), bits()
    color = {(0, 0): 0}
    for i in range(1, N):
        color[(i, 0)] = color[(i - 1, 0)] ^ ((0 + cols[i]) % 2 == 0)
    for i in range(N):
        for j in range(1, N):
            color[(i, j)] = color[(i, j - 1)] ^ ((i + rows[j]) % 2 == 0)
    for (i, j), c in color.items():
        x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
        polygon(t, [(x, y), (x + CELL, y), (x + CELL, y + CELL), (x, y + CELL)], SAND if c else INDIGO)
    t.pensize(STITCH)
    t.pencolor(IVORY)
    for j in range(N + 1):
        y = -H / 2 + j * CELL
        for i in range(N):
            if (i + rows[j % N]) % 2 == 0:
                t.goto(-W / 2 + i * CELL, y)
                t.pendown()
                t.goto(-W / 2 + (i + 1) * CELL, y)
                t.penup()
    for i in range(N + 1):
        x = -W / 2 + i * CELL
        for j in range(N):
            if (j + cols[i % N]) % 2 == 0:
                t.goto(x, -H / 2 + j * CELL)
                t.pendown()
                t.goto(x, -H / 2 + (j + 1) * CELL)
                t.penup()


if __name__ == "__main__":
    run(draw, W, H, INDIGO)

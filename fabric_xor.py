"""XOR: the cell at column i, row j takes the shade of i XOR j, the oldest demo-scene texture.

The 32 possible values map onto a gradient from deep teal to gold, which reveals the nested
Sierpinski-style squares hiding in the exclusive or. The 32 x 32 block repeats as a block.
"""
from common import mix, polygon, run

W = H = 800
N = 32
CELL = W / N
INK = "#0f0f14"
TEAL = (0.06, 0.22, 0.27)
GOLD = (0.79, 0.64, 0.29)


def draw(t):
    for i in range(N):
        for j in range(N):
            x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
            tone = mix(TEAL, GOLD, (i ^ j) / (N - 1))
            polygon(t, [(x, y), (x + CELL, y), (x + CELL, y + CELL), (x, y + CELL)], tone, INK, 1)


if __name__ == "__main__":
    run(draw, W, H, INK)

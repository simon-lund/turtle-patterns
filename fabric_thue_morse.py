"""Thue-Morse: a checkerboard that never repeats, built from the parity of binary digits.

Cell (i, j) is sand when the number of one bits in i and in j have different parity, teal
otherwise. The 32 x 32 block repeats as a block.
"""
from common import polygon, run

W = H = 800
N = 32
CELL = W / N
INK = "#0f0f14"
SAND = "#d9cdb4"
TEAL = "#15454d"


def parity(n):
    return bin(n).count("1") % 2


def draw(t):
    for i in range(N):
        for j in range(N):
            x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
            tone = SAND if parity(i) ^ parity(j) else TEAL
            polygon(t, [(x, y), (x + CELL, y), (x + CELL, y + CELL), (x, y + CELL)], tone, INK, 1)


if __name__ == "__main__":
    run(draw, W, H, INK)

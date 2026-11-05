"""Ulam spiral: the integers wound into a square spiral, with the primes picked out in gold.

The diagonal streaks are real: primes cluster on certain quadratic polynomials. This is a
32 x 32 window on the spiral, repeated as a block.
"""
from common import polygon, run

W = H = 800
N = 32
CELL = W / N
INK = "#0f0f14"
DIM = "#1a1c24"
GOLD = "#c9a24a"


def spiral(count):
    # yields (n, i, j) along a square spiral starting at the grid center
    i, j = N // 2, N // 2
    n, step, k = 1, 1, 0
    yield n, i, j
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while n < count:
        for _ in range(2):
            di, dj = dirs[k % 4]
            for _ in range(step):
                i, j, n = i + di, j + dj, n + 1
                yield n, i, j
            k += 1
        step += 1


def draw(t):
    limit = 2 * N * N
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for q in range(p * p, limit + 1, p):
                sieve[q] = False
    for n, i, j in spiral(limit):
        if not (0 <= i < N and 0 <= j < N):
            continue
        x, y = -W / 2 + i * CELL, -H / 2 + j * CELL
        if sieve[n]:
            polygon(t, [(x + 3, y + 3), (x + CELL - 3, y + 3), (x + CELL - 3, y + CELL - 3), (x + 3, y + CELL - 3)], GOLD)
        else:
            polygon(t, [(x + 9, y + 9), (x + CELL - 9, y + 9), (x + CELL - 9, y + CELL - 9), (x + 9, y + CELL - 9)], DIM)


if __name__ == "__main__":
    run(draw, W, H, INK)

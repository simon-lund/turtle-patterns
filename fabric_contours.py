"""Contours: a topographic map of a periodic landscape, gold lines, ivory every fourth.

Marching squares over a 200 x 200 grid of a sum-of-sines height field. Lower contours are a
dimmer gold, so the valleys recede. The field wraps, so every contour closes across the edges.
"""
import math

from common import mix, run

W = H = 800
N = 200
LEVELS = 24
INK = "#0f1216"
DIM = (0.40, 0.33, 0.16)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
# marching squares: for each corner case, the edge pairs a contour crosses
# edges: 0 bottom, 1 right, 2 top, 3 left; corner bits: bottom-left, bottom-right, top-right, top-left
CASES = {1: [(3, 0)], 2: [(0, 1)], 3: [(3, 1)], 4: [(1, 2)], 5: [(3, 0), (1, 2)], 6: [(0, 2)],
         7: [(3, 2)], 8: [(2, 3)], 9: [(0, 2)], 10: [(0, 1), (2, 3)], 11: [(1, 2)], 12: [(1, 3)],
         13: [(0, 1)], 14: [(3, 0)]}


def height(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    return (math.sin(2 * a + 0.3) * math.cos(b) + 0.6 * math.sin(3 * b + 1.0)
            + 0.5 * math.cos(a + 2 * b + 2.0) + 0.3 * math.sin(5 * a - b))


def draw(t):
    cell = W / N
    grid = [[height(-W / 2 + i * cell, -H / 2 + j * cell) for j in range(N)] for i in range(N)]
    lo = min(min(col) for col in grid)
    hi = max(max(col) for col in grid)
    for k in range(1, LEVELS):
        level = lo + (hi - lo) * k / LEVELS
        index = k % 4 == 0
        t.pensize(2.2 if index else 1.1)
        t.pencolor(IVORY if index else mix(DIM, GOLD, k / LEVELS))
        for i in range(N):
            for j in range(N):
                v = [grid[i][j], grid[(i + 1) % N][j], grid[(i + 1) % N][(j + 1) % N], grid[i][(j + 1) % N]]
                case = sum(1 << c for c in range(4) if v[c] > level)
                if case not in CASES:
                    continue
                x0, y0 = -W / 2 + i * cell, -H / 2 + j * cell

                def cross(edge):
                    a, b = ((0, 1), (1, 2), (3, 2), (0, 3))[edge]
                    f = (level - v[a]) / (v[b] - v[a])
                    corners = ((x0, y0), (x0 + cell, y0), (x0 + cell, y0 + cell), (x0, y0 + cell))
                    (ax, ay), (bx, by) = corners[a], corners[b]
                    return (ax + f * (bx - ax), ay + f * (by - ay))

                for e1, e2 in CASES[case]:
                    t.goto(cross(e1))
                    t.pendown()
                    t.goto(cross(e2))
                    t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

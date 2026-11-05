"""Rhombitrihexagonal tiling: hexagons, squares and triangles meeting at every vertex (3.4.6.4).

Hexagons sit on a triangular lattice, a square bridges every neighbouring pair, and the
triangles are the ground showing through. The tile is 800 x 554 so that two rows of hexagons
fit without distortion.
"""
import math

from common import polygon, run

W, H = 800, 554
COLS, ROWS = 5, 4
D = W / COLS
RH = H / ROWS
SIDE = D / (1 + 3 ** 0.5)
INK = "#0f0f14"
HEX = "#1f4e5a"
SQUARE = "#c9a24a"


def hexagon(t, cx, cy):
    pts = [(cx + SIDE * math.cos(math.radians(30 + 60 * k)),
            cy + SIDE * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    polygon(t, pts, HEX, INK, 1.5)


def square(t, cx, cy, deg):
    a = math.radians(deg)
    ux, uy = math.cos(a), math.sin(a)
    mx, my = cx + D / 2 * ux, cy + D / 2 * uy
    h = SIDE / 2
    pts = [(mx + h * (sx * ux - sy * uy), my + h * (sx * uy + sy * ux))
           for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    polygon(t, pts, SQUARE, INK, 1.5)


def draw(t):
    for j in range(-1, ROWS + 2):
        for i in range(-1, COLS + 2):
            cx = -W / 2 + i * D + (D / 2 if j % 2 else 0)
            cy = -H / 2 + j * RH
            hexagon(t, cx, cy)
            for deg in (0, 60, 120):
                square(t, cx, cy, deg)


if __name__ == "__main__":
    run(draw, W, H, INK)

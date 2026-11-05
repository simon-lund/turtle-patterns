"""Voxels: a rolling landscape of stacked cubes, which is also a lozenge tiling.

Heights come from a periodic wave, columns are drawn back to front so nearer cubes hide farther
ones. The two lattice periods project to an 840 x 480 tile, so it repeats seamlessly.
"""
import math

from common import polygon, run

W, H = 840, 480
P = 12
A = 40
HW = 70
TOP, LEFT, RIGHT, EDGE = "#e8e1d2", "#6b6b72", "#26262b", "#15151a"


def height(i, j):
    v = (2.5 + 1.2 * math.sin(2 * math.pi * i / P + 1) + 1.2 * math.cos(2 * math.pi * j / P)
         + 0.8 * math.sin(2 * math.pi * (i + j) / P))
    return max(0, int(v))


def prism(t, i, j, h):
    cx, cy = (i - j) * HW / 2, -(i + j) * A / 2 + h * A
    top, ur, ul, c = (cx, cy + A), (cx + HW / 2, cy + A / 2), (cx - HW / 2, cy + A / 2), (cx, cy)
    if h > 0:
        bot = (cx, cy - h * A)
        lr, ll = (cx + HW / 2, cy + A / 2 - h * A), (cx - HW / 2, cy + A / 2 - h * A)
        polygon(t, [ul, c, bot, ll], LEFT, EDGE)
        polygon(t, [c, ur, lr, bot], RIGHT, EDGE)
    polygon(t, [top, ur, c, ul], TOP, EDGE)


def draw(t):
    cells = [(i, j) for i in range(-P, 2 * P + 1) for j in range(-P, 2 * P + 1)]
    cells.sort(key=lambda ij: ij[0] + ij[1])
    for i, j in cells:
        prism(t, i, j, height(i, j))


if __name__ == "__main__":
    run(draw, W, H, EDGE)

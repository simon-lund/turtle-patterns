"""Block print: a half-drop repeat of two hand-cut motifs, a flower and a sprig.

Columns alternate between the motifs and odd columns drop by half a row, like a stamped
textile. Column count is even and the grid divides 800 px, so the tile repeats seamlessly.
"""
import random

from common import run

W = H = 800
SAND = "#efe3cd"
PLUM = "#4a2545"
MUSTARD = "#d9a441"
DX = DY = 100


def petal(t, r):
    # vesica shape from two 60-degree arcs, tip at distance r from the start
    t.begin_fill()
    t.circle(r, 60)
    t.left(120)
    t.circle(r, 60)
    t.left(120)
    t.end_fill()


def flower(t, x, y, angle):
    t.color(PLUM, PLUM)
    for k in range(8):
        t.goto(x, y)
        t.setheading(angle + k * 45)
        petal(t, 38)
    t.goto(x, y)
    t.dot(14, SAND)
    t.dot(7, MUSTARD)


def sprig(t, x, y, angle):
    t.color(PLUM, PLUM)
    for k in range(4):
        t.goto(x, y)
        t.setheading(angle + 45 + k * 90)
        petal(t, 22)
    for k in range(4):
        t.goto(x, y)
        t.setheading(angle + k * 90)
        t.forward(26)
        t.dot(8, MUSTARD)


def draw(t):
    random.seed(3)
    cols, rows = W // DX, H // DY
    for i in range(-1, cols + 1):
        drop = DY / 2 if i % 2 else 0
        for j in range(-1, rows + 1):
            x, y = -W / 2 + i * DX + DX / 2, -H / 2 + j * DY + DY / 2 + drop
            jitter = random.uniform(-6, 6)
            if i % 2 == 0:
                flower(t, x, y, jitter)
            else:
                sprig(t, x, y, jitter)


if __name__ == "__main__":
    run(draw, W, H, SAND)

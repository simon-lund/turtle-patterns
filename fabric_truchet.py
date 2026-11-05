"""Truchet ribbons: quarter-circle arcs on a grid, each cell flipped by a seeded coin toss.

Every cell has arc ends at the same points on all four edges, so the lines always connect
across cells and the 800 px tile repeats seamlessly.
"""
import random

from common import run

W = H = 800
MOSS = "#1f3b2d"
SAND = "#e8dcc3"
SAGE = "#8fae8c"
CELL = 80
SPREAD = 12  # distance of the two thin side lines from the center line


def arc(t, x, y, heading, r):
    # quarter circle starting at (x, y) with the center to the left of the heading
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.circle(r, 90)
    t.penup()


def corner_arcs(t, cx, cy, heading, x0, y0):
    # three concentric arcs around one cell corner: thin, thick, thin
    half = CELL / 2
    for r, width, color in ((half - SPREAD, 2, SAGE), (half, 7, SAND), (half + SPREAD, 2, SAGE)):
        t.pensize(width)
        t.pencolor(color)
        # arc start lies on the cell edge at distance r from the corner
        if heading == 90:        # corner bottom-left, start on bottom edge
            arc(t, cx + r, cy, 90, r)
        elif heading == 270:     # corner top-right, start on top edge
            arc(t, cx - r, cy, 270, r)
        elif heading == 180:     # corner bottom-right, start on right edge
            arc(t, cx, cy + r, 180, r)
        else:                    # corner top-left, start on left edge
            arc(t, cx, cy - r, 0, r)


def draw(t):
    random.seed(11)
    cells = W // CELL
    for i in range(cells):
        for j in range(cells):
            x0, y0 = -W / 2 + i * CELL, -H / 2 + j * CELL
            if random.random() < 0.5:
                corner_arcs(t, x0, y0, 90, x0, y0)
                corner_arcs(t, x0 + CELL, y0 + CELL, 270, x0, y0)
            else:
                corner_arcs(t, x0 + CELL, y0, 180, x0, y0)
                corner_arcs(t, x0, y0 + CELL, 0, x0, y0)


if __name__ == "__main__":
    run(draw, W, H, MOSS)

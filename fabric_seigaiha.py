"""Seigaiha: the Japanese 'blue ocean wave' repeat, rows of overlapping concentric arcs.

The tile is 800 px and the pattern period is 2 * R in both directions, so it repeats seamlessly.
"""
from common import run

W = H = 800
INDIGO = "#1e2d66"
CREAM = "#f3ead7"
R = 50
RINGS = 4


def disk(t, x, y, r):
    t.goto(x, y - r)
    t.setheading(0)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def ring(t, x, y, r):
    t.goto(x, y - r)
    t.setheading(0)
    t.pendown()
    t.circle(r)
    t.penup()


def draw(t):
    t.pensize(3)
    t.color(CREAM, INDIGO)
    # draw top to bottom so each row hides the lower half of the row above it
    y = H / 2 + R
    row = 0
    while y >= -H / 2 - R:
        offset = R if row % 2 else 0
        x = -W / 2 - 2 * R + offset
        while x <= W / 2 + 2 * R:
            disk(t, x, y, R)
            for k in range(RINGS):
                ring(t, x, y, R * (1 - k / RINGS))
            x += 2 * R
        y -= R
        row += 1


if __name__ == "__main__":
    run(draw, W, H, INDIGO)

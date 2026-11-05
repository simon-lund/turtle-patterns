"""Koch snowflake: five nested, filled snowflakes stacked like layers of a crystal."""
import math

from common import mix, run

OUTER = (0.10, 0.25, 0.45)
INNER = (0.85, 0.97, 1.0)
LAYERS = 5


def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    for turn in (60, -120, 60, 0):
        koch(t, length / 3, depth - 1)
        t.left(turn)


def snowflake(t, side, depth, color):
    # start at the top-left vertex so the bumps point outward
    t.goto(-side / 2, side * math.sqrt(3) / 6)
    t.setheading(0)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        koch(t, side, depth)
        t.right(120)
    t.end_fill()
    t.penup()


def draw(t):
    for i in range(LAYERS):
        snowflake(t, 620 * 0.78 ** i, 4, mix(OUTER, INNER, i / (LAYERS - 1)))


if __name__ == "__main__":
    run(draw)

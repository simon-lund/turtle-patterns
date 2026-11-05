"""Art Deco fans: overlapping gold-rimmed fans on near-black, the Gatsby scallop.

Fans are 2 * R wide and rows step by STEP, so the periods are 2 * R across and 2 * STEP down.
Both divide the 800 px tile, so it repeats seamlessly.
"""
import math

from common import run

W = H = 800
BLACK = "#0f0f14"
BODY = "#1b1b25"
GOLD = "#c9a24a"
DIM = "#6e5b2f"
R = 100
STEP = 80
SPOKES = 8


def fan(t, x, y):
    # filled half disk with a gold rim and base line
    t.color(GOLD, BODY)
    t.pensize(2.5)
    t.goto(x + R, y)
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.circle(R, 180)
    t.goto(x + R, y)
    t.end_fill()
    t.penup()
    # dim spokes and an inner arc
    t.pencolor(DIM)
    t.pensize(1.5)
    for k in range(1, SPOKES):
        a = math.radians(k * 180 / SPOKES)
        t.goto(x, y)
        t.pendown()
        t.goto(x + R * math.cos(a), y + R * math.sin(a))
        t.penup()
    t.goto(x + R * 0.55, y)
    t.setheading(90)
    t.pendown()
    t.circle(R * 0.55, 180)
    t.penup()
    # gold hub
    t.goto(x, y)
    t.dot(int(R * 0.3), GOLD)
    t.dot(int(R * 0.18), BLACK)


def draw(t):
    # bottom to top so each row sits on top of the row below, like scales
    y = -H / 2 - 2 * R
    row = 0
    while y <= H / 2 + R:
        offset = R if row % 2 else 0
        x = -W / 2 - 2 * R + offset
        while x <= W / 2 + 2 * R:
            fan(t, x, y)
            x += 2 * R
        y += STEP
        row += 1


if __name__ == "__main__":
    run(draw, W, H, BLACK)

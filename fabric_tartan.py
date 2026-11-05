"""Tartan: a charcoal, slate and ivory sett with a single gold line, woven as a twill.

Weft bands are solid. Warp bands are drawn as 45 degree twill lines so every crossing blends
the two colors half and half, like real cloth. The sett is 400 px and repeats twice per tile.
"""
from common import run

W = H = 800
SETT = [
    ("#141416", 30), ("#2b2b30", 70), ("#e9e2d3", 10), ("#2b2b30", 70),
    ("#141416", 30), ("#3b4a63", 90), ("#c9a24a", 10), ("#3b4a63", 90),
]
PITCH = 8
TWILL = 4


def bands():
    pos = -W / 2
    while pos < W / 2:
        for color, width in SETT:
            yield pos, width, color
            pos += width


def rect(t, x, y, w, h, color):
    t.color(color, color)
    t.goto(x, y)
    t.setheading(0)
    t.begin_fill()
    for d in (w, h, w, h):
        t.forward(d)
        t.left(90)
    t.end_fill()


def draw(t):
    for y0, h, color in bands():
        rect(t, -W / 2, y0, W, h, color)
    t.pensize(TWILL)
    for x0, w, color in bands():
        t.pencolor(color)
        # start on the pitch grid below the tile so the twill phase matches top and bottom
        y = -H / 2 - (-(-w // PITCH)) * PITCH
        while y < H / 2:
            t.goto(x0, y)
            t.pendown()
            t.goto(x0 + w, y + w)
            t.penup()
            y += PITCH


if __name__ == "__main__":
    run(draw, W, H, SETT[0][0])

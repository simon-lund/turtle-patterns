"""Houndstooth: charcoal and ivory, generated from the actual weave rule.

Warp and weft threads alternate four dark, four light, woven as a 2/2 twill. Each pixel shows
whichever thread is on top. The repeat is 8 pixels, and 80 pixels of 10 px fill the 800 px tile.
"""
from common import run

W = H = 800
IVORY = "#e9e2d3"
CHARCOAL = "#1b1b1f"
PX = 10


def dark(x, y):
    warp_dark = x % 8 < 4
    weft_dark = y % 8 < 4
    warp_on_top = (x - y) % 4 < 2
    return warp_dark if warp_on_top else weft_dark


def square(t, x, y):
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(PX)
        t.left(90)
    t.end_fill()
    t.penup()


def draw(t):
    t.color(CHARCOAL, CHARCOAL)
    t.pensize(1)
    cells = W // PX
    for i in range(cells):
        for j in range(cells):
            if dark(i, j):
                square(t, -W / 2 + i * PX, -H / 2 + j * PX)


if __name__ == "__main__":
    run(draw, W, H, IVORY)

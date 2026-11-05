"""Ikat chevrons: indigo, ivory and teal bands that zigzag, blurred thread by thread.

The tile is drawn as horizontal threads. Each thread shifts the band pattern by the zigzag
plus a little random offset, which gives the feathered edges of resist-dyed ikat cloth.
Band period 160 and zigzag period 200 both divide 800.
"""
import random

from common import run

W = H = 800
INDIGO = "#1b2a5e"
IVORY = "#ece4d2"
TEAL = "#3f7f8c"
BANDS = [(INDIGO, 60), (IVORY, 40), (TEAL, 60)]
P = sum(width for _, width in BANDS)
ZIG = 200
AMP = 60
THREAD = 4
BLUR = 10


def zig(y):
    # triangle wave with period ZIG and amplitude AMP
    phase = ((y + H / 2) % ZIG) / ZIG
    tri = 1 - abs(2 * phase - 1)
    return (tri - 0.5) * 2 * AMP


def draw(t):
    random.seed(5)
    t.pensize(THREAD)
    y = -H / 2 + THREAD / 2
    while y < H / 2:
        shift = zig(y) + random.uniform(-BLUR, BLUR)
        x = -W / 2 - P + (shift % P)
        while x < W / 2:
            for color, width in BANDS:
                t.pencolor(color)
                t.goto(x, y)
                t.pendown()
                t.goto(x + width, y)
                t.penup()
                x += width
        y += THREAD


if __name__ == "__main__":
    run(draw, W, H, INDIGO)

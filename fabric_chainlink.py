"""Chain link: interlocking gold rings on near-black, woven over and under.

Rings sit on a 160 px grid with a radius large enough to overlap the four neighbours. After
all rings are drawn, each ring repaints four of its crossings so the weave alternates over and
under all the way round. The grid spacing divides the 800 px tile, so it repeats seamlessly.
"""
import math

from common import run

W = H = 800
BLACK = "#0e0e12"
GOLD = "#c9a24a"
S = 160
R = 90
WIDTH = 12
HALO = WIDTH + 8
WINDOW = 10  # degrees repainted on each side of a crossing


def arc(t, x, y, start, extent, width, color):
    a = math.radians(start)
    t.pensize(width)
    t.pencolor(color)
    t.goto(x + R * math.cos(a), y + R * math.sin(a))
    t.setheading(start + 90)
    t.pendown()
    t.circle(R, extent)
    t.penup()


def ring(t, x, y, start, extent):
    # halo in the ground color first, then the gold stroke. The stroke runs a few degrees
    # past the halo so the halo's round caps never bite into the ring itself.
    extra = 0 if extent >= 360 else 4
    arc(t, x, y, start, extent, HALO, BLACK)
    arc(t, x, y, start - extra, extent + 2 * extra, WIDTH, GOLD)


def draw(t):
    centers = [
        (-W / 2 + i * S, -H / 2 + j * S)
        for i in range(-1, W // S + 2)
        for j in range(-1, H // S + 2)
    ]
    for x, y in centers:
        ring(t, x, y, 0, 360)
    # crossing angle with a neighbour, measured from the line between the centers
    phi = math.degrees(math.acos(S / (2 * R)))
    for x, y in centers:
        for over in (phi, 90 + phi, 180 + phi, 270 + phi):
            ring(t, x, y, over - WINDOW, 2 * WINDOW)


if __name__ == "__main__":
    run(draw, W, H, BLACK)

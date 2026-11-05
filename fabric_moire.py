"""Moire: concentric rings around grid points interfere into op-art blooms.

Rings around neighbouring centers overlap, and the interference draws hyperbolic curves that no
single ring contains. Grid spacing 200 divides the tile; alternate centers get a second color.
"""
from common import run

W = H = 800
INK = "#121216"
IVORY = "#e6dfcf"
GOLD = "#b8963e"
G = 200
RING = 10
RMAX = 200


def draw(t):
    t.pensize(1)
    for i in range(-1, W // G + 2):
        for j in range(-1, H // G + 2):
            cx, cy = -W / 2 + i * G, -H / 2 + j * G
            t.pencolor(IVORY if (i + j) % 2 == 0 else GOLD)
            r = RING
            while r <= RMAX:
                t.goto(cx, cy - r)
                t.setheading(0)
                t.pendown()
                t.circle(r)
                t.penup()
                r += RING


if __name__ == "__main__":
    run(draw, W, H, INK)

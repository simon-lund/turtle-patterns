"""Star and cross: the Islamic eight-pointed star tiling, ivory and gold stars on deep teal.

Stars touch tip to tip on a grid of 2 * R, and the gaps between four stars form crosses in the
ground color. Star colors alternate like a checkerboard, so the period is 4 * R. Both divide 800.
"""
import math

from common import run

W = H = 800
TEAL = "#134e4a"
IVORY = "#efe6d3"
GOLD = "#c9a24a"
OUTLINE = "#0b2b29"
R = 50
S = 2 * R
INNER = R * math.cos(math.radians(45)) / math.cos(math.radians(22.5))


def star(t, cx, cy, color):
    pts = []
    for k in range(16):
        ang = math.radians(k * 22.5)
        r = R if k % 2 == 0 else INNER
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    t.color(OUTLINE, color)
    t.goto(pts[0])
    t.pendown()
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.goto(pts[0])
    t.end_fill()
    t.penup()


def draw(t):
    t.pensize(1.5)
    for i in range(-1, W // S + 2):
        for j in range(-1, H // S + 2):
            x, y = -W / 2 + i * S, -H / 2 + j * S
            star(t, x, y, IVORY if (i + j) % 2 == 0 else GOLD)
            t.goto(x + R, y + R)
            t.dot(8, GOLD)


if __name__ == "__main__":
    run(draw, W, H, TEAL)

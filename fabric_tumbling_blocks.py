"""Tumbling blocks: isometric cubes in ivory, graphite and charcoal.

Each cube is a hexagon split into three rhombi. The hexagon width is rounded from 69.28 to
70 px (a 1 percent squash nobody can see) so twelve cubes fit an 840 px tile exactly.
"""
from common import run

W = H = 840
A = 40        # cube edge, also the hexagon's circumradius
HW = 70       # hexagon width
TOP = "#e8e1d2"
LEFT = "#6b6b72"
RIGHT = "#26262b"
EDGE = "#15151a"


def rhombus(t, pts, color):
    t.color(EDGE, color)
    t.goto(pts[0])
    t.pendown()
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.goto(pts[0])
    t.end_fill()
    t.penup()


def cube(t, cx, cy):
    top = (cx, cy + A)
    ur = (cx + HW / 2, cy + A / 2)
    lr = (cx + HW / 2, cy - A / 2)
    bot = (cx, cy - A)
    ll = (cx - HW / 2, cy - A / 2)
    ul = (cx - HW / 2, cy + A / 2)
    c = (cx, cy)
    rhombus(t, [top, ur, c, ul], TOP)
    rhombus(t, [ul, c, bot, ll], LEFT)
    rhombus(t, [c, ur, lr, bot], RIGHT)


def draw(t):
    t.pensize(1)
    rows = int(H / (1.5 * A))
    for j in range(-1, rows + 2):
        y = -H / 2 + j * 1.5 * A
        offset = HW / 2 if j % 2 else 0
        x = -W / 2 - HW + offset
        while x <= W / 2 + HW:
            cube(t, x, y)
            x += HW


if __name__ == "__main__":
    run(draw, W, H, EDGE)

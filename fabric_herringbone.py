"""Herringbone suiting: taupe broken-twill chevrons on charcoal with a thin gold windowpane.

Columns alternate stripe direction and odd columns shift by half a stripe, as in woven
herringbone. Periods: 2 * COL across, GAP down, CHECK for the windowpane. All divide 800 px.
"""
from common import run

W = H = 800
CHARCOAL = "#1c1c20"
TAUPE = "#5e5648"
GOLD = "#b8963e"
COL = 50
GAP = 25
CHECK = 200


def draw(t):
    t.pensize(2)
    t.pencolor(TAUPE)
    for i in range(W // COL):
        x0 = -W / 2 + i * COL
        direction = 1 if i % 2 == 0 else -1
        y = -H / 2 - COL + (GAP / 2 if i % 2 else 0)
        while y <= H / 2 + COL:
            t.goto(x0, y)
            t.pendown()
            t.goto(x0 + COL, y + direction * COL)
            t.penup()
            y += GAP
    # gold windowpane, placed so no line lands on the tile edge
    t.pensize(1.5)
    t.pencolor(GOLD)
    for k in range(W // CHECK):
        p = -W / 2 + CHECK / 2 + k * CHECK
        t.goto(p, -H / 2)
        t.pendown()
        t.goto(p, H / 2)
        t.penup()
        t.goto(-W / 2, p)
        t.pendown()
        t.goto(W / 2, p)
        t.penup()


if __name__ == "__main__":
    run(draw, W, H, CHARCOAL)

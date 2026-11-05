"""Moore curve: one closed gold thread that visits every cell of a 32 x 32 grid.

A space-filling curve drawn as a ribbon with a thin ink channel down its middle. The loop is
inset half a cell from the tile edge, so neighbouring tiles sit exactly one cell apart and the
pattern repeats without a visible seam.
"""
from common import run

W = H = 800
INK = "#0f0f14"
GOLD = "#c9a24a"
ORDER = 5
CELL = W / 2 ** ORDER


def moore_points():
    s = "LFL+F+LFL"
    rules = {"L": "-RF+LFL+FR-", "R": "+LF-RFR-FL+"}
    for _ in range(ORDER - 1):
        s = "".join(rules.get(c, c) for c in s)
    x, y, dx, dy = 0, 0, 0, 1
    pts = [(x, y)]
    for c in s:
        if c == "F":
            x, y = x + dx, y + dy
            pts.append((x, y))
        elif c == "+":
            dx, dy = -dy, dx
        elif c == "-":
            dx, dy = dy, -dx
    return pts


def draw(t):
    pts = moore_points()
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    scaled = [((x - cx) * CELL, (y - cy) * CELL) for x, y in pts]
    scaled.append(scaled[0])
    for width, color in ((CELL * 0.5, GOLD), (2, INK)):
        t.pensize(width)
        t.pencolor(color)
        t.goto(scaled[0])
        t.pendown()
        for p in scaled[1:]:
            t.goto(p)
        t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

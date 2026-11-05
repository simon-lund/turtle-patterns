"""Dragon curve: the shape of a paper strip folded 13 times, colored along its length."""
from common import hsv, run

ORDER = 13
FIT = 720  # longest side of the curve in pixels


def turns(count):
    # the n-th fold turns left when the bit above the lowest set bit of n is clear
    for n in range(1, count):
        yield 1 if ((n & -n) << 1) & n == 0 else -1


def points():
    x, y, dx, dy = 0, 0, 1, 0
    pts = [(x, y)]
    for turn in turns(2 ** ORDER):
        x, y = x + dx, y + dy
        pts.append((x, y))
        dx, dy = -turn * dy, turn * dx
    pts.append((x + dx, y + dy))
    return pts


def draw(t):
    pts = points()
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    width, height = max(xs) - min(xs), max(ys) - min(ys)
    scale = FIT / max(width, height)
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    t.pensize(2)
    t.goto((pts[0][0] - cx) * scale, (pts[0][1] - cy) * scale)
    t.pendown()
    total = len(pts)
    for i, (x, y) in enumerate(pts[1:], start=1):
        t.pencolor(hsv(0.78 - 0.62 * i / total, 0.85, 1.0))
        t.goto((x - cx) * scale, (y - cy) * scale)
    t.penup()


if __name__ == "__main__":
    run(draw)

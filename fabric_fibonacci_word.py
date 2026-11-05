"""Fibonacci word fractal: a single gold line steered by the digits of the Fibonacci word.

Walk one step per digit; at every 0, turn left if the digit's position is even and right if
odd. The 75025 digits of Fibonacci word 24 draw a medallion of nested squares.
"""
from common import run

W = H = 800
ORDER = 24
FIT = 740
INK = "#0f0f14"
GOLD = "#c9a24a"


def word(order):
    a, b = "1", "0"
    for _ in range(order - 1):
        a, b = b, b + a
    return b


def draw(t):
    x, y, dx, dy = 0, 0, 1, 0
    pts = [(x, y)]
    for k, ch in enumerate(word(ORDER), start=1):
        x, y = x + dx, y + dy
        pts.append((x, y))
        if ch == "0":
            dx, dy = (-dy, dx) if k % 2 == 0 else (dy, -dx)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    scale = FIT / max(max(xs) - min(xs), max(ys) - min(ys))
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    t.pensize(1.6)
    t.pencolor(GOLD)
    t.goto((pts[0][0] - cx) * scale, (pts[0][1] - cy) * scale)
    t.pendown()
    for px, py in pts[1:]:
        t.goto((px - cx) * scale, (py - cy) * scale)
    t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

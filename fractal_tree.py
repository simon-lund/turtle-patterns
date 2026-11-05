"""Fractal tree: asymmetric binary branching, colored from bark at the trunk to mint at the tips."""
from common import mix, run

TRUNK = (0.45, 0.30, 0.22)
TIPS = (0.55, 0.95, 0.75)
DEPTH = 11


def branch(t, length, depth):
    if depth == 0:
        return
    t.pencolor(mix(TRUNK, TIPS, 1 - depth / DEPTH))
    t.pensize(max(1, depth * 1.1))
    t.pendown()
    t.forward(length)
    t.left(24)
    branch(t, length * 0.74, depth - 1)
    t.right(24 + 32)
    branch(t, length * 0.68, depth - 1)
    t.left(32)
    t.penup()
    t.backward(length)


def draw(t):
    t.goto(0, -370)
    t.setheading(90)
    branch(t, 150, DEPTH)


if __name__ == "__main__":
    run(draw)

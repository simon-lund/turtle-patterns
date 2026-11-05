"""Rosette: squares rotated around the center, hue cycling once per revolution."""
from common import hsv, run


def draw(t):
    count = 72
    t.pensize(1.5)
    for i in range(count):
        t.pencolor(hsv(i / count, 0.7, 1.0))
        t.setheading(i * 360 / count)
        t.pendown()
        for _ in range(4):
            t.forward(270)
            t.left(90)
        t.penup()
    # inner ring of circles adds a torus-shaped core
    t.pensize(1)
    for i in range(36):
        t.pencolor(hsv(0.55 + i / 72, 0.5, 0.95))
        t.setheading(i * 10)
        t.pendown()
        t.circle(95)
        t.penup()


if __name__ == "__main__":
    run(draw)

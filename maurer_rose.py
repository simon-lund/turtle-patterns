"""Maurer rose: 361 chords of the rose r = sin(6θ), stepping 71 degrees per chord."""
import math

from common import hsv, run

PETALS = 6
STEP = 71
SCALE = 380


def point(deg):
    k = math.radians(deg)
    r = SCALE * math.sin(PETALS * k)
    return r * math.cos(k), r * math.sin(k)


def draw(t):
    # thin chords, drifting from blue to violet
    t.pensize(1)
    t.goto(point(0))
    t.pendown()
    for i in range(1, 362):
        t.pencolor(hsv(0.6 + 0.15 * i / 361, 0.6, 0.9))
        t.goto(point(i * STEP))
    t.penup()
    # the rose itself as a golden outline
    t.pensize(3)
    t.pencolor((1.0, 0.85, 0.3))
    t.goto(point(0))
    t.pendown()
    for deg in range(1, 361):
        t.goto(point(deg))
    t.penup()


if __name__ == "__main__":
    run(draw)

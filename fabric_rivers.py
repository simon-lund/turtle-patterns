"""Rivers: thirteen hundred raindrops running downhill over a periodic landscape.

Every thread follows the steepest descent of a sum-of-sines height field and stops in a
basin, thickening as it goes. Drops converge on each basin from all sides, so the picture is a
field of tufts, like dandelion clocks, one per valley. Ivory where a drop starts high, teal low.
"""
import math
import random

from common import mix, run, torus_segment

W = H = 800
INK = "#0f1216"
TEAL = (0.19, 0.46, 0.50)
GOLD = (0.79, 0.64, 0.29)
IVORY = (0.90, 0.87, 0.81)
SEED = 5
SEEDS = 36
STEPS = 150
STEP = 3
FLAT = 0.0025


def height(x, y):
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    return (math.sin(2 * a + 0.5) * math.cos(b) + 0.7 * math.sin(3 * b + 1.2)
            + 0.5 * math.cos(a + 2 * b) + 0.35 * math.sin(5 * a - 2 * b + 0.3)
            + 0.25 * math.cos(4 * a + 3 * b))


def downhill(x, y):
    # analytic gradient of height, in height units per pixel
    a, b = 2 * math.pi * x / W, 2 * math.pi * y / H
    da = (2 * math.cos(2 * a + 0.5) * math.cos(b) - 0.5 * math.sin(a + 2 * b)
          + 1.75 * math.cos(5 * a - 2 * b + 0.3) - 1.0 * math.sin(4 * a + 3 * b))
    db = (-math.sin(2 * a + 0.5) * math.sin(b) + 2.1 * math.cos(3 * b + 1.2) - 1.0 * math.sin(a + 2 * b)
          - 0.7 * math.cos(5 * a - 2 * b + 0.3) - 0.75 * math.sin(4 * a + 3 * b))
    gx, gy = da * 2 * math.pi / W, db * 2 * math.pi / H
    n = math.hypot(gx, gy)
    return (-gx / n, -gy / n, n) if n > 0 else (0, 0, 0)


def draw(t):
    random.seed(SEED)
    for i in range(SEEDS):
        for j in range(SEEDS):
            x = -W / 2 + (i + random.random()) * W / SEEDS
            y = -H / 2 + (j + random.random()) * H / SEEDS
            h = (height(x, y) + 2.3) / 4.6
            t.pencolor(mix(GOLD, IVORY, h) if h > 0.5 else mix(TEAL, GOLD, h * 2))
            t.goto(x, y)
            t.pendown()
            for s in range(STEPS):
                ux, uy, slope = downhill(x, y)
                if slope < FLAT:
                    break
                if s % 6 == 0:
                    t.pensize(0.6 + 3.0 * (s / STEPS) ** 1.5)
                x, y = torus_segment(t, (x, y), (x + STEP * ux, y + STEP * uy), W, H)
            t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

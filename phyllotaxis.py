"""Phyllotaxis: seeds placed at the golden angle, the way a sunflower head grows."""
import math

from common import hsv, run

GOLDEN_ANGLE = math.radians(137.50776)


def draw(t):
    count = 1000
    scale = 11.5
    for n in range(count):
        angle = n * GOLDEN_ANGLE
        radius = scale * math.sqrt(n)
        t.goto(radius * math.cos(angle), radius * math.sin(angle))
        f = n / count
        t.dot(int(3 + 16 * f), hsv(0.55 + 0.35 * f, 0.75, 0.6 + 0.4 * f))


if __name__ == "__main__":
    run(draw)

"""Apollonian medallion: circles packed inside circles, all the way down, gold on ink.

Three mutually tangent circles inside a bounding circle leave gaps; Descartes' circle theorem
gives the circle that fits each gap, and the gaps it creates get the same treatment until the
circles are two pixels wide. One medallion per tile.
"""
from common import run

W = H = 800
R0 = 385
MIN_R = 2.2
INK = "#0f0f14"
GOLD = "#c9a24a"


def fourth(c1, c2, c3, known):
    # circles are (curvature, center) pairs; given three mutually tangent circles and one
    # circle tangent to all of them, Vieta's formula gives the other one
    k = 2 * (c1[0] + c2[0] + c3[0]) - known[0]
    z = (2 * (c1[0] * c1[1] + c2[0] * c2[1] + c3[0] * c3[1]) - known[0] * known[1]) / k
    return (k, z)


def draw(t):
    outer, a, b = (-1.0, 0j), (2.0, 0.5 + 0j), (2.0, -0.5 + 0j)
    c, d = (3.0, 2j / 3), (3.0, -2j / 3)
    circles = [outer, a, b, c, d]
    stack = [(outer, a, c, b), (outer, b, c, a), (a, b, c, outer),
             (outer, a, d, b), (outer, b, d, a), (a, b, d, outer)]
    while stack:
        c1, c2, c3, known = stack.pop()
        new = fourth(c1, c2, c3, known)
        if new[0] <= 0 or R0 / new[0] < MIN_R:
            continue
        circles.append(new)
        stack += [(c1, c2, new, c3), (c1, c3, new, c2), (c2, c3, new, c1)]
    t.pencolor(GOLD)
    for k, z in circles:
        r = R0 / abs(k)
        t.pensize(max(1, min(3, r / 25)))
        t.goto(z.real * R0, z.imag * R0 - r)
        t.setheading(0)
        t.pendown()
        t.circle(r)
        t.penup()


if __name__ == "__main__":
    run(draw, W, H, INK)

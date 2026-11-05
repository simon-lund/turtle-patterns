"""Cairo tiling: the pentagon tiling of Cairo's pavements, in four tones.

Built from a square grid where each cell holds an H or an I shaped bar, alternating like a
checkerboard. The two pentagons on either side of each bar get their own tone. Cell 100 px,
period 200 px.
"""
from common import polygon, run

W = H = 800
U = 50
S = 0.5 * U
INK = "#0f0f14"
TONES = ["#15454d", "#d9cdb4", "#2a6b73", "#c9a24a"]


def draw(t):
    for ci in range(-1, W // (2 * U) + 1):
        for cj in range(-1, H // (2 * U) + 1):
            ox, oy = -W / 2 + ci * 2 * U, -H / 2 + cj * 2 * U
            c00, c20 = (ox, oy), (ox + 2 * U, oy)
            c02, c22 = (ox, oy + 2 * U), (ox + 2 * U, oy + 2 * U)
            if (ci + cj) % 2 == 0:
                left, right = (ox + U - S, oy + U), (ox + U + S, oy + U)
                above = [c02, left, right, c22, (ox + U, oy + 3 * U - S)]
                below = [c00, left, right, c20, (ox + U, oy - U + S)]
                polygon(t, above, TONES[0], INK, 2)
                polygon(t, below, TONES[1], INK, 2)
            else:
                bottom, top = (ox + U, oy + U - S), (ox + U, oy + U + S)
                west = [c00, bottom, top, c02, (ox - U + S, oy + U)]
                east = [c20, bottom, top, c22, (ox + 3 * U - S, oy + U)]
                polygon(t, west, TONES[2], INK, 2)
                polygon(t, east, TONES[3], INK, 2)


if __name__ == "__main__":
    run(draw, W, H, INK)

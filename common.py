"""Shared helpers for the turtle patterns: screen setup, colors, PNG export."""
import colorsys
import os
import subprocess
import sys

BG = "#0b0f19"


def hsv(h, s=0.8, v=1.0):
    """Return an (r, g, b) tuple in 0..1 for a hue that wraps around."""
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


def mix(a, b, f):
    """Linear blend between two rgb tuples, f in 0..1."""
    return tuple(x + (y - x) * f for x, y in zip(a, b))


def setup(width, height, bg=BG):
    """Open a window of the given size, paint the background, return (screen, turtle)."""
    # Imported here so the notebooks can use the helpers below without Tk installed.
    import turtle

    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor(bg)
    screen.colormode(1.0)
    screen.tracer(0)
    t = turtle.Turtle(visible=False)
    t.speed(0)
    # Postscript export ignores bgcolor, so the background is painted as a shape.
    t.penup()
    t.goto(-width / 2 - 2, -height / 2 - 2)
    t.color(bg, bg)
    t.begin_fill()
    for _ in range(2):
        t.forward(width + 4)
        t.left(90)
        t.forward(height + 4)
        t.left(90)
    t.end_fill()
    t.home()
    return screen, t


def bounding_box(eps):
    """Return the four %%BoundingBox numbers of an EPS file."""
    with open(eps) as f:
        for line in f:
            if line.startswith("%%BoundingBox:"):
                return [int(v) for v in line.split()[1:5]]
    raise ValueError(f"no %%BoundingBox in {eps}")


def save_png(screen, path, width, height, dpi=144):
    """Export the drawn canvas to a PNG via postscript + ghostscript."""
    screen.update()
    eps = os.path.splitext(path)[0] + ".eps"
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    screen.getcanvas().postscript(
        file=eps, colormode="color",
        x=-width / 2, y=-height / 2, width=width, height=height,
        pagewidth=f"{width}p",
    )
    # Tk pads the bounding box by one point on the top and right. Render exactly the
    # requested area by moving its lower-left corner onto the origin of a fixed-size page.
    llx, lly = bounding_box(eps)[:2]
    px, py = round(width * dpi / 72), round(height * dpi / 72)
    subprocess.run(
        ["gs", "-q", "-dSAFER", "-dBATCH", "-dNOPAUSE", "-dGraphicsAlphaBits=4",
         "-sDEVICE=png16m", f"-r{dpi}", f"-g{px}x{py}", "-dFIXEDMEDIA",
         f"-sOutputFile={path}",
         "-c", f"<</Install {{{-llx} {-lly} translate}}>> setpagedevice",
         "-f", eps],
        check=True,
    )
    os.remove(eps)


def run(draw, width=800, height=800, bg=BG):
    """Show the pattern in a window, or write a PNG when called with --save PATH.

    --dpi N sets the export resolution (default 144, which gives 2 px per canvas unit).
    """
    screen, t = setup(width, height, bg)
    draw(t)
    screen.update()
    if "--save" in sys.argv:
        path = sys.argv[sys.argv.index("--save") + 1]
        dpi = int(sys.argv[sys.argv.index("--dpi") + 1]) if "--dpi" in sys.argv else 144
        save_png(screen, path, width, height, dpi)
        screen.bye()
    else:
        screen.exitonclick()


def polygon(t, pts, fill, outline=None, width=1):
    """Fill a closed polygon. The outline is drawn in the fill color unless another is given."""
    t.fillcolor(fill)
    t.pencolor(outline or fill)
    t.pensize(width)
    t.goto(pts[0])
    t.pendown()
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.goto(pts[0])
    t.end_fill()
    t.penup()


def torus_segment(t, p, q, width, height):
    """Draw p -> q on a torus: split at the tile edge and continue from the opposite edge."""
    (x, y), (nx, ny) = p, q
    for axis, size in ((0, width), (1, height)):
        half = size / 2
        n = (nx, ny)[axis]
        if n > half or n < -half:
            edge = half if n > half else -half
            f = (edge - p[axis]) / (n - p[axis])
            hit = [x + f * (nx - x), y + f * (ny - y)]
            hit[axis] = edge
            t.goto(*hit)
            t.penup()
            hit[axis] = -edge
            t.goto(*hit)
            t.pendown()
            shifted = [nx, ny]
            shifted[axis] += -size if n > half else size
            return torus_segment(t, tuple(hit), tuple(shifted), width, height)
    t.goto(nx, ny)
    return (nx, ny)

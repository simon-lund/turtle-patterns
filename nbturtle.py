"""A turtle for Jupyter: records what the turtle draws and shows it inline as a PNG.

The standard-library turtle needs a Tk window, which a notebook kernel doesn't have. This Turtle
covers the part of the turtle API the patterns use, with the same geometry, and matplotlib draws
the result. Lines get round caps and joins like Tk's, a fill sits below the lines drawn with it,
and one canvas unit is one point, so dpi=144 gives the same pixels as `--save` in common.py.
Anything else from the turtle API raises AttributeError instead of being silently skipped.
"""
import io
import math

from matplotlib.collections import PathCollection
from matplotlib.colors import to_rgba
from matplotlib.figure import Figure
from matplotlib.path import Path

from common import BG

CLEAR = (0, 0, 0, 0)


def _color(args):
    # turtle accepts a name, a hex string, an (r, g, b) tuple or r, g, b as three arguments
    return args[0] if len(args) == 1 else tuple(args)


class Turtle:
    """The drawing half of turtle.Turtle: moving, pen, fills and dots. Angles are in degrees."""

    def __init__(self, canvas):
        self._ops = canvas._ops
        self._x = self._y = 0.0
        self._heading = 0.0
        self._down = True
        self._pencolor = self._fillcolor = "black"
        self._pensize = 1
        self._line = None  # points of the line being drawn; a pen change starts a new one
        self._fill = None  # outline of the shape between begin_fill and end_fill
        self._fill_slot = None

    def goto(self, x, y=None):
        """Move to (x, y), or to the point x, drawing a line if the pen is down."""
        if y is None:
            x, y = x
        if self._down:
            if self._line is None:
                self._line = [(self._x, self._y)]
                self._ops.append(("line", self._line, self._pencolor, self._pensize))
            self._line.append((x, y))
        if self._fill is not None:
            self._fill.append((x, y))
        self._x, self._y = x, y

    def forward(self, distance):
        a = math.radians(self._heading)
        self.goto(self._x + distance * math.cos(a), self._y + distance * math.sin(a))

    def backward(self, distance):
        self.forward(-distance)

    def left(self, angle):
        self._heading = (self._heading + angle) % 360

    def right(self, angle):
        self.left(-angle)

    def setheading(self, angle):
        self._heading = angle % 360

    def home(self):
        self.goto(0, 0)
        self.setheading(0)

    def circle(self, radius, extent=None, steps=None):
        """Arc around a center radius units to the left, as an inscribed polygon like turtle's."""
        if extent is None:
            extent = 360
        if steps is None:
            steps = 1 + int(min(11 + abs(radius) / 6, 59) * abs(extent) / 360)
        w = extent / steps
        chord = 2 * radius * math.sin(math.radians(w / 2))
        if radius < 0:
            chord, w = -chord, -w
        self.left(w / 2)
        for _ in range(steps):
            self.forward(chord)
            self.left(w)
        self.left(-w / 2)

    def dot(self, size=None, *color):
        """Filled circle of diameter size at the turtle, in the pen color unless one is given."""
        if not color and isinstance(size, (str, tuple)):
            size, color = None, (size,)
        if not size:
            size = self._pensize + max(self._pensize, 4)
        self._line = None
        self._ops.append(("dot", (self._x, self._y), _color(color) if color else self._pencolor, size))

    def penup(self):
        if self._down:
            self._line = None
            self._down = False

    def pendown(self):
        if not self._down:
            self._line = None
            self._down = True

    def pensize(self, width=None):
        if width is None:
            return self._pensize
        if width != self._pensize:
            self._line = None
            self._pensize = width

    def pencolor(self, *color):
        if not color:
            return self._pencolor
        color = _color(color)
        if color != self._pencolor:
            self._line = None
            self._pencolor = color

    def fillcolor(self, *color):
        if not color:
            return self._fillcolor
        self._fillcolor = _color(color)

    def color(self, *colors):
        """color(c) sets pen and fill, color(pen, fill) sets them separately."""
        if not colors:
            return self._pencolor, self._fillcolor
        if len(colors) == 2:
            self.pencolor(colors[0])
            self.fillcolor(colors[1])
        else:
            self.pencolor(*colors)
            self.fillcolor(*colors)

    def begin_fill(self):
        # The fill takes its place in the drawing order now, below the lines that outline it.
        if self._fill is None:
            self._fill_slot = len(self._ops)
            self._ops.append(None)
        self._fill = [(self._x, self._y)]
        self._line = None

    def end_fill(self):
        if self._fill is not None and len(self._fill) > 2:
            self._ops[self._fill_slot] = ("fill", self._fill, self._fillcolor, 0)
        self._fill = None

    def speed(self, speed=None):
        """Accepted for compatibility; drawing is never animated."""

    def position(self):
        return self._x, self._y

    def heading(self):
        return self._heading

    def isdown(self):
        return self._down

    fd, bk, back, lt, rt, seth = forward, backward, backward, left, right, setheading
    setpos = setposition = goto
    pu, up, pd, down, width, pos = penup, penup, pendown, pendown, pensize, position


class Canvas:
    """A width x height drawing centered on the origin, y pointing up, like a turtle screen.

    The last expression of a notebook cell shows it; dpi sets that preview's resolution.
    """

    def __init__(self, width=800, height=800, bg=BG, dpi=72):
        self.width, self.height, self.bg, self.dpi = width, height, bg, dpi
        self._ops = []

    def turtle(self):
        """A new turtle at the center, heading east, pen down and black, like turtle.Turtle()."""
        return Turtle(self)

    def png(self, dpi=None):
        """Render to PNG bytes, (width * dpi / 72) pixels wide."""
        fig = Figure(figsize=(self.width / 72, self.height / 72), facecolor=self.bg)
        ax = fig.add_axes((0, 0, 1, 1))
        ax.set_xlim(-self.width / 2, self.width / 2)
        ax.set_ylim(-self.height / 2, self.height / 2)
        ax.set_axis_off()
        # One collection keeps the drawing order and stays fast at 100k lines.
        # Ops are (kind, points or center, color, line width or dot diameter).
        paths, faces, edges, widths = [], [], [], []
        for op in self._ops:
            if op is None:  # begin_fill without a matching end_fill
                continue
            kind, where, color, size = op
            if kind == "line":
                paths.append(Path(where))
                faces.append(CLEAR)
                edges.append(to_rgba(color))
                widths.append(size)
            else:
                paths.append(Path(where) if kind == "fill" else Path.circle(where, size / 2))
                faces.append(to_rgba(color))
                edges.append(CLEAR)
                widths.append(0)
        ax.add_collection(PathCollection(
            paths, facecolors=faces, edgecolors=edges, linewidths=widths,
            capstyle="round", joinstyle="round", snap=False,
        ))
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=dpi or self.dpi, facecolor=self.bg)
        return buf.getvalue()

    def save(self, path, dpi=144):
        """Write a PNG; dpi=144 gives 2 px per canvas unit, a 1600 px file for an 800 tile."""
        with open(path, "wb") as f:
            f.write(self.png(dpi))

    def repeat(self, n=2, dpi=None):
        """An n x n grid of this tile, to see whether a fabric repeats seamlessly.

        Each copy is drawn at dpi / n by default, so the grid previews at the tile's own size.
        """
        from PIL import Image

        tile = Image.open(io.BytesIO(self.png(dpi or self.dpi / n)))
        grid = Image.new("RGB", (tile.width * n, tile.height * n))
        for i in range(n):
            for j in range(n):
                grid.paste(tile, (i * tile.width, j * tile.height))
        buf = io.BytesIO()
        grid.save(buf, format="png")
        return Picture(buf.getvalue())

    def _repr_png_(self):
        return self.png()


class Picture:
    """Finished PNG bytes that show in a notebook as one image, and can be saved."""

    def __init__(self, data):
        self.data = data

    def save(self, path):
        with open(path, "wb") as f:
            f.write(self.data)

    def _repr_png_(self):
        return self.data


def render(draw, width=800, height=800, bg=BG, dpi=72):
    """Call draw(turtle) on a fresh canvas and return the canvas, the notebook twin of common.run.

    The turtle starts as common.setup leaves it: at the center, heading east, pen up and colored
    like the background.
    """
    canvas = Canvas(width, height, bg, dpi)
    t = canvas.turtle()
    t.penup()
    t.color(bg, bg)
    draw(t)
    return canvas

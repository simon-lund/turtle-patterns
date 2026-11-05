# Turtle patterns

Generative patterns and seamless fabric repeats drawn with Python's standard-library `turtle` module.
The scripts need nothing beyond Python; the notebooks need matplotlib.

## Notebooks

Ten of the patterns as Jupyter notebooks, from a rosette of squares to threads in a flow field. Each
one builds its pattern in steps: the code split into short explained cells, a picture after each
step, and things to try at the end. The fabric notebooks also show their tile repeated 2 × 2.
GitHub shows the notebooks with their pictures, so you can read them without running anything.

| | | | | |
| :-: | :-: | :-: | :-: | :-: |
| [<img src="gallery/rosette.jpg" width="150" alt="">](01_rosette.ipynb)<br>[Rosette](01_rosette.ipynb) | [<img src="gallery/phyllotaxis.jpg" width="150" alt="">](02_phyllotaxis.ipynb)<br>[Phyllotaxis](02_phyllotaxis.ipynb) | [<img src="gallery/koch_snowflake.jpg" width="150" alt="">](03_koch_snowflake.ipynb)<br>[Koch snowflake](03_koch_snowflake.ipynb) | [<img src="gallery/dragon_curve.jpg" width="150" alt="">](04_dragon_curve.ipynb)<br>[Dragon curve](04_dragon_curve.ipynb) | [<img src="gallery/maurer_rose.jpg" width="150" alt="">](05_maurer_rose.ipynb)<br>[Maurer rose](05_maurer_rose.ipynb) |
| [<img src="gallery/fabric_truchet.jpg" width="150" alt="">](06_fabric_truchet.ipynb)<br>[Truchet ribbons](06_fabric_truchet.ipynb) | [<img src="gallery/fabric_hitomezashi.jpg" width="150" alt="">](07_fabric_hitomezashi.ipynb)<br>[Hitomezashi](07_fabric_hitomezashi.ipynb) | [<img src="gallery/fabric_penrose.jpg" width="150" alt="">](08_fabric_penrose.ipynb)<br>[Penrose medallion](08_fabric_penrose.ipynb) | [<img src="gallery/fabric_marbled.jpg" width="150" alt="">](09_fabric_marbled.ipynb)<br>[Marbled paper](09_fabric_marbled.ipynb) | [<img src="gallery/fabric_vortices.jpg" width="150" alt="">](10_fabric_vortices.ipynb)<br>[Vortices](10_fabric_vortices.ipynb) |

To run them yourself:

```bash
pip install -r requirements.txt
```

```bash
jupyter lab
```

The standard `turtle` module needs a Tk window, which a notebook doesn't have. So the notebooks
draw with [`nbturtle.py`](nbturtle.py), a stand-in that takes the same commands (`forward`, `left`,
`circle`, `goto`, `begin_fill`, `dot`, …) and shows the drawing inline. `render(draw, width, height,
background)` is the notebook twin of `common.run`. It draws the same picture as the scripts, and
`canvas.save(path, dpi=288)` writes a print-size tile.

## Patterns

| | Script | Pattern |
| --- | --- | --- |
| <img src="gallery/rosette.jpg" width="100" alt=""> | `rosette.py` | 72 rotated squares with a cycling hue, plus a ring of circles in the core |
| <img src="gallery/phyllotaxis.jpg" width="100" alt=""> | `phyllotaxis.py` | 1000 seeds placed at the golden angle, like a sunflower head |
| <img src="gallery/dragon_curve.jpg" width="100" alt=""> | `dragon_curve.py` | order-13 dragon curve, colored along its length |
| <img src="gallery/fractal_tree.jpg" width="100" alt=""> | `fractal_tree.py` | asymmetric binary tree, bark at the trunk, mint at the tips |
| <img src="gallery/maurer_rose.jpg" width="100" alt=""> | `maurer_rose.py` | Maurer rose (n=6, d=71) with the underlying rose outlined in gold |
| <img src="gallery/koch_snowflake.jpg" width="100" alt=""> | `koch_snowflake.py` | five nested, filled Koch snowflakes |

## Fabric repeats

Most tiles are 800 px, the tables note the exceptions, and every motif period divides its tile, so the tiles repeat seamlessly in both directions.

| | Script | Fabric |
| --- | --- | --- |
| <img src="gallery/fabric_seigaiha.jpg" width="100" alt=""> | `fabric_seigaiha.py` | Japanese ocean-wave scallops, cream on indigo |
| <img src="gallery/fabric_truchet.jpg" width="100" alt=""> | `fabric_truchet.py` | Truchet ribbons, seeded random arcs, sand on moss green |
| <img src="gallery/fabric_blockprint.jpg" width="100" alt=""> | `fabric_blockprint.py` | half-drop block print, plum flowers and sprigs on sand |
| <img src="gallery/fabric_deco_fans.jpg" width="100" alt=""> | `fabric_deco_fans.py` | Art Deco fans, gold on near-black |
| <img src="gallery/fabric_houndstooth.jpg" width="100" alt=""> | `fabric_houndstooth.py` | houndstooth generated from the 2/2 twill weave rule, charcoal on ivory |
| <img src="gallery/fabric_herringbone.jpg" width="100" alt=""> | `fabric_herringbone.py` | herringbone suiting with a gold windowpane check |
| <img src="gallery/fabric_chainlink.jpg" width="100" alt=""> | `fabric_chainlink.py` | interlocking gold rings woven over and under, on near-black |
| <img src="gallery/fabric_tumbling_blocks.jpg" width="100" alt=""> | `fabric_tumbling_blocks.py` | isometric cubes in ivory, graphite and charcoal |
| <img src="gallery/fabric_tartan.jpg" width="100" alt=""> | `fabric_tartan.py` | charcoal, slate and ivory tartan with one gold line, twill-woven crossings |
| <img src="gallery/fabric_star_cross.jpg" width="100" alt=""> | `fabric_star_cross.py` | Islamic eight-pointed star and cross, ivory and gold on teal |
| <img src="gallery/fabric_ikat.jpg" width="100" alt=""> | `fabric_ikat.py` | chevron ikat, indigo, ivory and teal, feathered thread by thread |
| <img src="gallery/fabric_asanoha.jpg" width="100" alt=""> | `fabric_asanoha.py` | sashiko hemp-leaf grid, gold on charcoal |

## Generated patterns

These are not reproductions of a named motif. Each comes from a rule plus a seed, so changing the
seed or a constant gives a tile nobody has seen. No guarantee that nothing similar exists.

| | Script | Pattern |
| --- | --- | --- |
| <img src="gallery/fabric_sineweave.jpg" width="100" alt=""> | `fabric_sineweave.py` | wavy ivory ribbons in a true over-under basket weave |
| <img src="gallery/fabric_moore.jpg" width="100" alt=""> | `fabric_moore.py` | one closed gold thread filling a 32 x 32 grid, a digital meander |
| <img src="gallery/fabric_lissajous.jpg" width="100" alt=""> | `fabric_lissajous.py` | Lissajous knots overlapping into lace, gold and ivory on green |
| <img src="gallery/fabric_moire.jpg" width="100" alt=""> | `fabric_moire.py` | concentric rings interfering into op-art blooms |
| <img src="gallery/fabric_spirolace.jpg" width="100" alt=""> | `fabric_spirolace.py` | two spirograph roses alternating into lace on plum |

## Thread-drawn

The ones that look like cloth rather than diagrams. Hundreds of fine strands or contour lines
on ink, in gold, ivory and teal, all wrapping across the tile edges.

| | Script | Pattern |
| --- | --- | --- |
| <img src="gallery/fabric_current.jpg" width="100" alt=""> | `fabric_current.py` | threads following a periodic flow field, marbled currents |
| <img src="gallery/fabric_eddies.jpg" width="100" alt=""> | `fabric_eddies.py` | threads circling a checkerboard of whirlpools, teal one way, gold the other |
| <img src="gallery/fabric_magnetic.jpg" width="100" alt=""> | `fabric_magnetic.py` | field lines between six magnetic poles, like iron filings |
| <img src="gallery/fabric_contours.jpg" width="100" alt=""> | `fabric_contours.py` | topographic contour map of a periodic landscape |
| <img src="gallery/fabric_marbled.jpg" width="100" alt=""> | `fabric_marbled.py` | mathematical paper marbling, drops combed into feathers |
| <img src="gallery/fabric_brush.jpg" width="100" alt=""> | `fabric_brush.py` | long tapered brush strokes along a slow field |
| <img src="gallery/fabric_vortices.jpg" width="100" alt=""> | `fabric_vortices.py` | threads spiraling around five point vortices, galaxies on a torus |
| <img src="gallery/fabric_ripples.jpg" width="100" alt=""> | `fabric_ripples.py` | threads riding the crests of interfering ripples from four sources |
| <img src="gallery/fabric_rivers.jpg" width="100" alt=""> | `fabric_rivers.py` | raindrops running downhill, converging into dandelion-like tufts, one per basin |
| <img src="gallery/fabric_mycelium.jpg" width="100" alt=""> | `fabric_mycelium.py` | radial colonies of branching hyphae, like seed heads on ink |
| <img src="gallery/fabric_guilloche.jpg" width="100" alt=""> | `fabric_guilloche.py` | engraved guilloche ribbons, bands of phase-shifted sine lines |
| <img src="gallery/fabric_dial.jpg" width="100" alt=""> | `fabric_dial.py` | guilloche rosette like a watch face (block) |

## Twenty more, from tiling problems and other mathematics

Seamless unless marked "block", where a self-contained block repeats and its border shows.

| | Script | Pattern |
| --- | --- | --- |
| <img src="gallery/fabric_dominoes.jpg" width="100" alt=""> | `fabric_dominoes.py` | random domino tiling of a torus, four colors by orientation and parity |
| <img src="gallery/fabric_voxels.jpg" width="100" alt=""> | `fabric_voxels.py` | a landscape of stacked cubes, also a lozenge tiling, 840 x 480 |
| <img src="gallery/fabric_wang.jpg" width="100" alt=""> | `fabric_wang.py` | corner-colored Wang tiles melting into rounded two-tone islands |
| <img src="gallery/fabric_cairo.jpg" width="100" alt=""> | `fabric_cairo.py` | the Cairo pentagon tiling in four tones |
| <img src="gallery/fabric_pythagorean.jpg" width="100" alt=""> | `fabric_pythagorean.py` | Pythagorean tiling, big and small squares on a skew lattice |
| <img src="gallery/fabric_penrose.jpg" width="100" alt=""> | `fabric_penrose.py` | Penrose rhombus medallion from six rounds of deflation (block) |
| <img src="gallery/fabric_rhombitrihex.jpg" width="100" alt=""> | `fabric_rhombitrihex.py` | hexagons, squares and triangles, the 3.4.6.4 tiling, 800 x 554 |
| <img src="gallery/fabric_voronoi.jpg" width="100" alt=""> | `fabric_voronoi.py` | Voronoi crackle around seeds on a torus |
| <img src="gallery/fabric_quilt.jpg" width="100" alt=""> | `fabric_quilt.py` | a square packed with squares via a random quadtree |
| <img src="gallery/fabric_hextruchet.jpg" width="100" alt=""> | `fabric_hextruchet.py` | hexagonal Truchet tiles with arcs and bars, 840 x 728 |
| <img src="gallery/fabric_apollonian.jpg" width="100" alt=""> | `fabric_apollonian.py` | Apollonian gasket medallion, gold circles on ink (block) |
| <img src="gallery/fabric_dla.jpg" width="100" alt=""> | `fabric_dla.py` | diffusion-limited aggregation coral on a torus |
| <img src="gallery/fabric_maze.jpg" width="100" alt=""> | `fabric_maze.py` | a perfect maze on a torus, drawn as ivory passages |
| <img src="gallery/fabric_xor.jpg" width="100" alt=""> | `fabric_xor.py` | i XOR j on a teal-to-gold gradient (block) |
| <img src="gallery/fabric_fibonacci_word.jpg" width="100" alt=""> | `fabric_fibonacci_word.py` | Fibonacci word fractal medallion (block) |
| <img src="gallery/fabric_bubbles.jpg" width="100" alt=""> | `fabric_bubbles.py` | terrazzo of random non-overlapping circles on a torus |
| <img src="gallery/fabric_hitomezashi.jpg" width="100" alt=""> | `fabric_hitomezashi.py` | hitomezashi stitching from two random bit strings, two-colored |
| <img src="gallery/fabric_ulam.jpg" width="100" alt=""> | `fabric_ulam.py` | Ulam prime spiral, primes in gold (block) |
| <img src="gallery/fabric_thue_morse.jpg" width="100" alt=""> | `fabric_thue_morse.py` | Thue-Morse checkerboard from binary digit parity (block) |
| <img src="gallery/fabric_trominoes.jpg" width="100" alt=""> | `fabric_trominoes.py` | a 32 x 32 board with one hole tiled by L-trominoes (block) |

## Printing on fabric

Print-on-demand fabric services take a PNG tile at 150 dpi and repeat it across the cloth. A
1600 px tile prints as a 27 cm repeat. For a larger repeat, re-render at a higher resolution;
the source is vector, so lines thicken with it:

```bash
xvfb-run -a python3 fabric_vortices.py --save out/fabric_vortices_3200.png --dpi 288
```

That gives a 3200 px tile, a 54 cm repeat at 150 dpi, with the thinnest lines at about 0.9 mm.
At the 27 cm repeat the thread patterns' lines are about 0.45 mm, the limit of what digital
fabric printing resolves on smooth cloth. Order a test swatch before yardage; gold prints as
ochre and every colour comes out a little duller than on screen.

Stitch a tile 2x2 to check the repeat (needs ImageMagick):

```bash
convert \( out/fabric_truchet.png out/fabric_truchet.png +append \) \( out/fabric_truchet.png out/fabric_truchet.png +append \) -append out/fabric_truchet_repeat.png
```

## Running

Show one in a window (click the window to close it):

```bash
python3 rosette.py
```

Render all of them to `out/*.png` without opening windows (needs `xvfb-run` and `gs`):

```bash
xvfb-run -a python3 render_all.py
```

Each script exposes `draw(turtle)`; `common.py` handles the window, the dark background and the PNG export.

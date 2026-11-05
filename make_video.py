"""Record a pattern being drawn: saves a frame every few strokes, then encodes an MP4.

    xvfb-run -a python3 make_video.py fabric_vortices 6
"""
import importlib
import pathlib
import shutil
import subprocess
import sys

from common import BG, save_png, setup

name, every = sys.argv[1], int(sys.argv[2])
mod = importlib.import_module(name)
W, H = getattr(mod, "W", 800), getattr(mod, "H", 800)
frames = pathlib.Path("out/frames") / name
shutil.rmtree(frames, ignore_errors=True)
frames.mkdir(parents=True)
screen, t = setup(W, H, getattr(mod, "INK", BG))
count = {"strokes": 0, "frames": 0}
penup = t.penup


def snap():
    save_png(screen, str(frames / f"{count['frames']:05d}.png"), W, H, dpi=72)
    count["frames"] += 1


def counting_penup():
    penup()
    count["strokes"] += 1
    if count["strokes"] % every == 0:
        snap()


t.penup = t.pu = counting_penup
mod.draw(t)
snap()
last = frames / f"{count['frames'] - 1:05d}.png"
for _ in range(60):  # hold the finished pattern for 2.5 s
    shutil.copy(last, frames / f"{count['frames']:05d}.png")
    count["frames"] += 1
screen.bye()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "24", "-i", str(frames / "%05d.png"),
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", f"out/{name}.mp4"], check=True)
print(f"wrote out/{name}.mp4 from {count['frames']} frames")

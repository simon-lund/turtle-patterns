"""Render every pattern in this folder to out/<name>.png.

Run under xvfb-run so no windows pop up:
    xvfb-run -a python3 render_all.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
SKIP = {"common.py", "render_all.py", "make_video.py", "nbturtle.py"}


def main():
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    for script in sorted(HERE.glob("*.py")):
        if script.name in SKIP:
            continue
        target = out / f"{script.stem}.png"
        subprocess.run([sys.executable, str(script), "--save", str(target)], check=True, cwd=HERE)
        print(f"wrote {target.relative_to(HERE)}")


if __name__ == "__main__":
    main()

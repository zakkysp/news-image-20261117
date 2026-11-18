#!/usr/bin/env python3
"""Copy the news image for 17 November 2026 to the output directory.

The image itself is drawn by draw_image.py and ships in this
repository as entry.png; this program just places it where the
grader expects it.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
src = os.path.join(HERE, "entry.png")
with open(src, "rb") as f:
    magic = f.read(8)
if magic != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is not a PNG file")
if os.path.getsize(src) > 1048576:
    raise SystemExit("entry.png is over the 1 MiB limit")
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
# Confirm the copy landed intact: same size, still a PNG.
if os.path.getsize(dst) != os.path.getsize(src):
    raise SystemExit("copied entry.png has the wrong size")
with open(dst, "rb") as f:
    if f.read(8) != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("copied entry.png is not a PNG file")

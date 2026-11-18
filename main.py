#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261118.

Copies the bundled front-page image (entry.png, drawn for Wednesday
18 November 2026) to the harness output directory as entry.png.
Standard library only; no network; the copy is byte-identical every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    with open(target, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    size = os.path.getsize(target)
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

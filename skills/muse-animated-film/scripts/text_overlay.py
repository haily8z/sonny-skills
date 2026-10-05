#!/usr/bin/env python3
"""Render exact overlay text (Vietnamese-safe) onto an image, or into a transparent PNG.

Fallback for when the image model misspells overlay text, and for ffmpeg builds
without the drawtext filter. Requires Pillow (pip install pillow).

Examples:
  # Burn text onto a clean doodle image (top zone)
  python3 text_overlay.py --in s05_clean.png --out s05.png --text "Thức khuya là vay nợ" --zone top

  # Transparent text layer sized for a 720x1280 video, to use with ffmpeg overlay
  python3 text_overlay.py --size 720x1280 --out scene3_text.png --text "Mười năm sau" --zone bottom --style light
"""
import argparse
import glob
import os
import sys

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "~/Library/Fonts/BeVietnamPro-Bold.ttf",
    "/usr/share/fonts/truetype/bevietnampro/BeVietnamPro-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]
ZONES = {"top": 0.08, "center": 0.42, "bottom": 0.74}


def find_font(explicit):
    if explicit:
        return explicit
    for pattern in FONT_CANDIDATES:
        for path in glob.glob(os.path.expanduser(pattern)):
            return path
    sys.exit("No Vietnamese-capable font found; pass --font /path/to/BeVietnamPro-Bold.ttf")


def wrap(draw, text, font, max_width):
    # Explicit " / " forces a line break, matching the TEXT OVERLAY LOCK convention.
    lines = []
    for part in text.split(" / "):
        current = ""
        for word in part.split():
            trial = f"{current} {word}".strip()
            if draw.textlength(trial, font=font) <= max_width or not current:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="src", help="source image; omit to make a transparent layer")
    p.add_argument("--size", help="WxH for a transparent layer, e.g. 720x1280")
    p.add_argument("--out", required=True)
    p.add_argument("--text", help="exact text; ' / ' = line break")
    p.add_argument("--text-file", help="read exact text from a UTF-8 file")
    p.add_argument("--zone", choices=ZONES, default="top")
    p.add_argument("--style", choices=["dark", "light"], default="dark",
                   help="dark ink + white outline (paper backgrounds) or white + dark outline (video)")
    p.add_argument("--font")
    p.add_argument("--scale", type=float, default=0.085, help="font size as a fraction of image width")
    a = p.parse_args()

    text = a.text if a.text is not None else open(a.text_file, encoding="utf-8").read().strip()
    if a.src:
        img = Image.open(a.src).convert("RGBA")
    elif a.size:
        w, h = (int(v) for v in a.size.lower().split("x"))
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    else:
        sys.exit("pass --in or --size")

    w, h = img.size
    font = ImageFont.truetype(find_font(a.font), max(16, int(w * a.scale)))
    draw = ImageDraw.Draw(img)
    lines = wrap(draw, text, font, int(w * 0.84))
    fill, stroke = ((30, 30, 30, 255), (255, 255, 255, 255)) if a.style == "dark" else \
                   ((255, 255, 255, 255), (20, 20, 20, 230))
    stroke_w = max(2, font.size // 12)
    line_h = int(font.size * 1.25)
    y = int(h * ZONES[a.zone])
    if a.zone == "bottom":
        y = min(y, h - int(h * 0.08) - line_h * len(lines))
    for line in lines:
        lw = draw.textlength(line, font=font)
        draw.text(((w - lw) / 2, y), line, font=font, fill=fill,
                  stroke_width=stroke_w, stroke_fill=stroke)
        y += line_h

    out = img if a.out.lower().endswith(".png") else img.convert("RGB")
    out.save(a.out)
    print(a.out)


if __name__ == "__main__":
    main()

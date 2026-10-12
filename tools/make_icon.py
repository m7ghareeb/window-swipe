#!/usr/bin/env python3
# Draws window-swipe@ghareeb/icon.png (256x256, RGBA): two windows on a horizontal strip,
# the next one sliding in, with a swipe arrow. Rendered at 4x and downscaled for clean edges.
import os
from PIL import Image, ImageDraw, ImageFilter

S = 1024                      # working size; output is S // 4
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'window-swipe@ghareeb', 'icon.png')


def lerp(a, b, t): return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def rounded_mask(box, r):
    m = Image.new('L', (S, S), 0)
    ImageDraw.Draw(m).rounded_rectangle(box, r, fill=255)
    return m


img = Image.new('RGBA', (S, S), (0, 0, 0, 0))

# background: rounded square, diagonal blue -> indigo gradient
grad = Image.new('RGBA', (S, S))
top, bottom = (59, 130, 246, 255), (79, 70, 229, 255)
gd = ImageDraw.Draw(grad)
for y in range(S):
    gd.line([(0, y), (S, y)], fill=lerp(top, bottom, y / (S - 1)))
bg_box = (32, 32, S - 32, S - 32)
img.paste(grad, (0, 0), rounded_mask(bg_box, 200))


def window(box, alpha, bar=(226, 232, 240)):
    layer = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, 44, fill=(255, 255, 255, alpha))
    # title bar with three dots
    d.rounded_rectangle((x0, y0, x1, y0 + 96), 44, fill=bar + (alpha,))
    d.rectangle((x0, y0 + 50, x1, y0 + 96), fill=bar + (alpha,))
    for k in range(3):
        cx = x0 + 60 + k * 52
        d.ellipse((cx - 15, y0 + 33, cx + 15, y0 + 63), fill=(148, 163, 184, alpha))
    # content lines
    for k, w in enumerate((0.62, 0.78, 0.48)):
        ly = y0 + 160 + k * 74
        d.rounded_rectangle((x0 + 56, ly, x0 + 56 + (x1 - x0 - 112) * w, ly + 34), 17, fill=(203, 213, 225, alpha))
    return layer


# soft shadow under the front window
sh = Image.new('RGBA', (S, S), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((330, 232, 862, 682), 44, fill=(30, 27, 75, 110))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(28)))
# the window being left (behind, faded), then the next window sliding in
img.alpha_composite(window((150, 196, 600, 646), 120))
img.alpha_composite(window((350, 196, 860, 646), 255))

# swipe arrow under the windows: a leftward arrow led by three fingertips
d = ImageDraw.Draw(img)
y = 806
d.rounded_rectangle((268, y - 18, 690, y + 18), 18, fill=(255, 255, 255, 235))
d.polygon([(200, y), (300, y - 62), (300, y + 62)], fill=(255, 255, 255, 235))
d.ellipse((706, y - 34, 774, y + 34), fill=(255, 255, 255, 235))
d.ellipse((786, y - 34, 854, y + 34), fill=(255, 255, 255, 200))
d.ellipse((866, y - 34, 934, y + 34), fill=(255, 255, 255, 160))

img.resize((S // 4, S // 4), Image.LANCZOS).save(OUT, optimize=True)
print('wrote', os.path.normpath(OUT), Image.open(OUT).size)

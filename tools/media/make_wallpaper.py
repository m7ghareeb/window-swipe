#!/usr/bin/env python3
# Original abstract wallpaper for the Window Swipe demo scene: soft blurred colour fields
# on a deep blue-violet base. Generated, so it is free of third-party rights.
import sys, math, random
from PIL import Image, ImageDraw, ImageFilter
W, H = int(sys.argv[2]), int(sys.argv[3])
random.seed(7)
img = Image.new('RGB', (W, H))
d = ImageDraw.Draw(img)
top, bot = (22, 30, 64), (12, 16, 36)
for y in range(H):
    t = y / (H - 1)
    d.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bot)))
layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ld = ImageDraw.Draw(layer)
blobs = [  # (cx, cy, radius, colour) as fractions of the screen
    (0.18, 0.22, 0.42, (64, 120, 230, 170)),
    (0.82, 0.18, 0.38, (150, 90, 230, 150)),
    (0.70, 0.88, 0.46, (40, 170, 200, 140)),
    (0.25, 0.92, 0.34, (110, 70, 200, 120)),
    (0.50, 0.50, 0.30, (90, 110, 240, 70)),
]
for cx, cy, r, c in blobs:
    R = r * W
    ld.ellipse([cx * W - R, cy * H - R * 0.8, cx * W + R, cy * H + R * 0.8], fill=c)
layer = layer.filter(ImageFilter.GaussianBlur(W * 0.12))
img = Image.alpha_composite(img.convert('RGBA'), layer)
# fine grain to avoid banding in screenshots and GIF palettes
if len(sys.argv) <= 4 or sys.argv[4] != 'nograin':
    noise = Image.effect_noise((W, H), 6).convert('L')
    img = Image.blend(img, Image.merge('RGBA', (noise, noise, noise, Image.new('L', (W, H), 255))), 0.03)
img.convert('RGB').save(sys.argv[1], quality=95)
print(sys.argv[1], W, H)

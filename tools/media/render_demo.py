#!/usr/bin/env python3
# Renders the Window Swipe README illustration (GIF + still) entirely offline:
#   python3 tools/media/render_demo.py <output dir>
# Nothing is captured from a desktop: the scene, windows and content are drawn here, and the
# motion uses Window Swipe 1.0.0's own release logic (Balanced decision, Calm glide: cubic
# Hermite / power curve, velocity-matched) copied from extension.js.
import math, os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
W, H = 1600, 900                     # scene size (a 1600x900 "monitor")
FPS = 30
GIF_W = 960
HERE = os.path.dirname(os.path.abspath(__file__))
NOTO = '/usr/share/fonts/truetype/noto/NotoSans-'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
f_reg = lambda s: ImageFont.truetype(NOTO + 'Regular.ttf', s)
f_bold = lambda s: ImageFont.truetype(NOTO + 'Bold.ttf', s)
f_mono = lambda s: ImageFont.truetype(MONO, s)

# ---- Window Swipe 1.0.0 parameters (extension.js) ----
CALM = dict(min=299, base=299, perScreen=345, max=598, momentum=2.875)
BALANCED = dict(commit=0.50, minProgress=0.15, velocity=2.5, projectSec=0.10)
GLIDE_MAX_AWAY = 0.5
SMOOTHING_MS = 12

# ---------------------------------------------------------------- scene
def wallpaper(grain=True):
    import subprocess
    p = os.path.join(OUT, '_wallpaper.png')
    subprocess.run([sys.executable, os.path.join(HERE, 'make_wallpaper.py'), p, str(W), str(H)] + ([] if grain else ['nograin']), check=True,
                   stdout=subprocess.DEVNULL)
    return Image.open(p).convert('RGBA')

def panel(img):
    # a slim, generic bottom panel (no real app icons)
    d = ImageDraw.Draw(img)
    ph = 40
    bar = Image.new('RGBA', (W, ph), (16, 18, 28, 215))
    img.alpha_composite(bar, (0, H - ph))
    cy = H - ph // 2
    d.rounded_rectangle([14, cy - 12, 38, cy + 12], 6, fill=(98, 160, 90, 255))       # menu button
    for i, c in enumerate([(84, 140, 230), (232, 168, 60), (70, 70, 80), (180, 110, 220)]):
        x = 60 + i * 40
        d.rounded_rectangle([x, cy - 12, x + 24, cy + 12], 6, fill=c + (255,))
    t = '10:24'
    d.text((W - 20 - d.textlength(t, font=f_reg(17)), cy - 12), t, font=f_reg(17), fill=(220, 224, 232))
    return img

def window(w, h, title, kind):
    S = 2                                     # supersample for clean corners and text
    win = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(win)
    dark = kind == 'terminal'
    body = (30, 32, 40) if dark else (250, 250, 252)
    head = (42, 44, 54) if dark else (236, 237, 241)
    r = 12 * S
    d.rounded_rectangle([0, 0, w * S - 1, h * S - 1], r, fill=body)
    d.rounded_rectangle([0, 0, w * S - 1, 46 * S], r, fill=head)
    d.rectangle([0, 30 * S, w * S - 1, 46 * S], fill=head)
    d.line([0, 46 * S, w * S, 46 * S], fill=(20, 22, 28) if dark else (214, 216, 222), width=S)
    tf = f_bold(15 * S)
    tc = (210, 214, 224) if dark else (60, 64, 74)
    d.text(((w * S - d.textlength(title, font=tf)) / 2, 12 * S), title, font=tf, fill=tc)
    for i, c in enumerate([(120, 124, 136), (120, 124, 136), (232, 96, 84)]):   # min / max / close
        cx = w * S - (26 + (2 - i) * 26) * S
        d.ellipse([cx - 7 * S, 23 * S - 7 * S, cx + 7 * S, 23 * S + 7 * S], fill=c)
    top = 46 * S
    if kind == 'editor':
        # toolbar
        d.rectangle([0, top, w * S, top + 44 * S], fill=(244, 245, 248))
        for i in range(9):
            x = 22 * S + i * 44 * S
            d.rounded_rectangle([x, top + 12 * S, x + 22 * S, top + 32 * S], 5 * S, fill=(206, 210, 220))
        d.line([0, top + 44 * S, w * S, top + 44 * S], fill=(222, 224, 230), width=S)
        y = top + 74 * S; left = 70 * S; right = w * S - 70 * S
        d.text((left, y), 'Window Swipe', font=f_bold(34 * S), fill=(36, 40, 50)); y += 70 * S
        para = ('Swipe left or right with three or four fingers to slide between the windows of your '
                'workspace. The window follows your fingers as you swipe, and when you lift them it '
                'glides into place with the speed of your swipe. A short swipe springs back, a quick '
                'flick switches, and rapid swipes continue smoothly from wherever the windows are. '
                'Window order follows your Plank dock, so the next window is always the one you expect.')
        f = f_reg(22 * S); line = ''
        for word in para.split():
            test = (line + ' ' + word).strip()
            if d.textlength(test, font=f) > right - left:
                d.text((left, y), line, font=f, fill=(74, 78, 90)); y += 40 * S; line = word
            else:
                line = test
        d.text((left, y), line, font=f, fill=(74, 78, 90)); y += 64 * S
        for item in ('Follows your fingers', 'Glides into place', 'Springs back on a short swipe'):
            d.ellipse([left, y + 12 * S, left + 10 * S, y + 22 * S], fill=(84, 140, 230))
            d.text((left + 26 * S, y), item, font=f, fill=(74, 78, 90)); y += 40 * S
    elif kind == 'terminal':
        mono = f_mono(18 * S)
        rows = [('demo@mint', (110, 200, 120), ':~$ ', 'echo "Hello from Window Swipe"'),
                (None, (220, 224, 232), 'Hello from Window Swipe', ''),
                ('demo@mint', (110, 200, 120), ':~$ ', 'ls projects'),
                (None, (120, 170, 240), 'notes   photos   website', ''),
                ('demo@mint', (110, 200, 120), ':~$ ', '')]
        y = top + 26 * S
        for user, c, a, b in rows:
            x = 26 * S
            if user:
                d.text((x, y), user, font=mono, fill=c); x += d.textlength(user, font=mono)
                d.text((x, y), a, font=mono, fill=(220, 224, 232)); x += d.textlength(a, font=mono)
                d.text((x, y), b, font=mono, fill=(220, 224, 232)); x += d.textlength(b, font=mono)
            else:
                d.text((x, y), a, font=mono, fill=c)
            y += 34 * S
        d.rectangle([x + 2 * S, y - 34 * S + 4 * S, x + 13 * S, y - 34 * S + 26 * S], fill=(220, 224, 232))
    elif kind == 'gallery':
        pal = [((255, 154, 98), (255, 94, 120)), ((86, 204, 242), (47, 128, 237)), ((168, 230, 140), (56, 168, 120)),
               ((255, 210, 120), (247, 151, 30)), ((180, 140, 255), (110, 80, 220)), ((120, 230, 220), (40, 160, 190))]
        cols, gap = 3, 18 * S
        tw = (w * S - gap * (cols + 1)) // cols
        th = (h * S - top - gap * 3) // 2
        for i, (c1, c2) in enumerate(pal):
            x0 = gap + (i % cols) * (tw + gap); y0 = top + gap + (i // cols) * (th + gap)
            tile = Image.new('RGBA', (tw, th))
            td = ImageDraw.Draw(tile)
            for yy in range(th):
                t = yy / th
                td.line([(0, yy), (tw, yy)], fill=tuple(round(a + (b - a) * t) for a, b in zip(c1, c2)))
            # simple "landscape" shapes so the tiles read as photos
            td.ellipse([tw * 0.62, th * 0.18, tw * 0.80, th * 0.18 + tw * 0.18], fill=(255, 255, 255, 150))
            td.polygon([(0, th), (tw * 0.35, th * 0.55), (tw * 0.6, th * 0.8), (tw * 0.8, th * 0.6), (tw, th)], fill=(0, 0, 0, 60))
            m = Image.new('L', (tw, th), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, tw - 1, th - 1], 10 * S, fill=255)
            win.paste(tile, (x0, y0), m)
    win = win.resize((w, h), Image.LANCZOS)
    # soft shadow
    pad = 40
    out = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    sh = Image.new('RGBA', out.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([pad, pad + 10, pad + w, pad + h + 10], 14, fill=(0, 0, 0, 120))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    out.alpha_composite(win, (pad, pad))
    return out, pad

WIN = [('Notes — Text Editor', 'editor'), ('Terminal', 'terminal'), ('Photos', 'gallery')]
WW, WH = 1320, 690
WX, WY = (W - WW) // 2, 104

# ---------------------------------------------------------------- motion (extension logic)
class Slide:
    """One swipe: tracking with the 12 ms follower, then Balanced decision and Calm glide."""
    def __init__(self, direction):
        self.dir = direction; self.drawn = 0.0; self.recent = []; self.state = 'tracking'
    def track(self, t, finger, dt):
        a = 1 - math.exp(-dt / (SMOOTHING_MS / 1000))
        self.drawn += (finger - self.drawn) * a
        self.recent = (self.recent + [(t, self.drawn)])[-3:]
    def release(self, t, finger):
        (t0, x0), (t1, x1) = self.recent[-3], self.recent[-1]
        v_in = (x1 - x0) / (t1 - t0)                      # progress / s (finger velocity)
        f = BALANCED
        proj = finger + v_in * f['projectSec']
        commit = proj >= f['commit'] if finger >= f['commit'] else (v_in >= f['velocity'] and finger >= f['minProgress'] and proj >= f['commit'])
        self.commit = commit
        self.frm, self.to = self.drawn, (1.0 if commit else 0.0)
        dist = abs(self.to - self.frm); d = 1 if self.to >= self.frm else -1
        (ta, a), (tb, b) = self.recent[-2], self.recent[-1]
        toward = (b - a) / (tb - ta) * d
        g = CALM
        longest = min(g['max'], g['base'] + g['perScreen'] * dist)
        by_m = g['momentum'] * dist / toward * 1000 if toward > 1e-3 else longest
        self.ms = g['min'] if dist < 1e-4 else max(g['min'], min(longest, by_m))
        T = self.ms / 1000
        self.pow = toward * T / dist if dist > 0 and toward > 3 * dist / T else 0
        toward = max(toward, -GLIDE_MAX_AWAY) if dist > 0 else 0
        self.v0 = toward * d
        self.t0 = t; self.state = 'settling'
        return commit
    def settle(self, t):
        u = min(1, (t - self.t0) / (self.ms / 1000))
        if self.pow:
            self.drawn = self.frm + (self.to - self.frm) * (1 - (1 - u) ** self.pow)
        else:
            T = self.ms / 1000
            h00, h10, h01 = 2*u**3 - 3*u**2 + 1, u**3 - 2*u**2 + u, -2*u**3 + 3*u**2
            self.drawn = h00 * self.frm + h10 * T * self.v0 + h01 * self.to
        if u >= 1: self.state = 'done'

ease = lambda u: u * u * (3 - 2 * u)
# (direction, finger keyframes [(seconds, progress)], caption)
SCRIPT = [
    ('pause', 0.9, 'Swipe with three or four fingers'),
    ('left', [(0, 0), (0.55, 0.42), (0.95, 0.66)], 'The window follows your fingers'),
    ('pause', 0.9, 'Release past halfway: it glides into place'),
    ('left', [(0, 0), (0.45, 0.24), (0.6, 0.27)], 'A short swipe springs back'),
    ('pause', 0.9, 'A short swipe springs back'),
    ('left', [(0, 0), (0.13, 0.34)], 'A quick flick switches too', 'flick'),
    ('pause', 1.0, 'A quick flick switches too'),
    ('right', [(0, 0), (0.7, 0.62)], 'Swipe right for the previous window'),
    ('pause', 0.7, 'Swipe right for the previous window'),
    ('right', [(0, 0), (0.6, 0.6)], 'Swipe right for the previous window'),
    ('pause', 0.9, 'Smooth, macOS-inspired motion'),
]

def finger_at(keys, t, mode='ease'):
    # 'ease': fingers start and slow down smoothly; 'flick': they accelerate and lift while
    # still moving fast (ease-in), as in a real flick
    for (ta, pa), (tb, pb) in zip(keys, keys[1:]):
        if t <= tb:
            u = (t - ta) / (tb - ta)
            k = u * u if mode == 'flick' else (ease(u) if ta == 0 else u)
            return pa + (pb - pa) * k
    return keys[-1][1]

def simulate():
    """Yields per-frame states: (page float, finger dict or None, caption)."""
    frames = []; page = 0; dt_sim = 1 / 240; t = 0.0; next_frame = 0.0
    def emit(pos, finger, cap):
        nonlocal next_frame
        while t >= next_frame:
            frames.append((pos, finger, cap)); next_frame += 1 / FPS
    lift = None
    for step in SCRIPT:
        if step[0] == 'pause':
            end = t + step[1]
            while t < end:
                f = lift if lift and t - lift[1] < 0.25 else None
                emit(page, (f[0], 1 - (t - f[1]) / 0.25, f[2]) if f else None, step[2]); t += dt_sim
            continue
        direction, keys, cap = step[:3]
        mode = step[3] if len(step) > 3 else 'ease'
        sgn = 1 if direction == 'left' else -1
        s = Slide(direction); t0 = t
        while t - t0 <= keys[-1][0]:
            fp = finger_at(keys, t - t0, mode); s.track(t, fp, dt_sim)
            emit(page + sgn * s.drawn, (sgn * fp, 1.0, direction), cap); t += dt_sim
        s.release(t, fp); lift = (sgn * fp, t, direction)
        while s.state != 'done':
            s.settle(t)
            f = (lift[0], max(0, 1 - (t - lift[1]) / 0.25), direction)
            emit(page + sgn * s.drawn, f, cap); t += dt_sim
        if s.commit: page += sgn
    return frames

# ---------------------------------------------------------------- drawing
def touchpad(img, finger):
    pw, ph = 200, 118
    x0, y0 = (W - pw) // 2, H - 40 - ph - 14
    pad = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
    d = ImageDraw.Draw(pad)
    d.rounded_rectangle([0, 0, pw - 1, ph - 1], 18, fill=(14, 16, 26, 215), outline=(255, 255, 255, 120), width=2)
    lab = 'touchpad'
    lf = f_reg(15)
    d.text(((pw - d.textlength(lab, font=lf)) / 2, ph - 26), lab, font=lf, fill=(255, 255, 255, 90))
    if finger:
        prog, alpha, _ = finger
        cx = pw / 2 - prog * pw * 0.55
        for i in (-1, 0, 1):
            fx, fy = cx + i * 26, ph / 2 + (8 if i == 0 else 0) - 4
            a = int(235 * max(0, min(1, alpha)))
            d.ellipse([fx - 10, fy - 10, fx + 10, fy + 10], fill=(255, 255, 255, a))
    img.alpha_composite(pad, (x0, y0))

def caption(img, text):
    if not text: return
    d = ImageDraw.Draw(img); f = f_bold(26)
    tw = d.textlength(text, font=f)
    pw, ph = int(tw + 56), 54
    x0, y0 = (W - pw) // 2, 26
    chip = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
    ImageDraw.Draw(chip).rounded_rectangle([0, 0, pw - 1, ph - 1], 27, fill=(12, 14, 24, 170))
    img.alpha_composite(chip, (x0, y0))
    d.text((x0 + 28, y0 + 10), text, font=f, fill=(245, 247, 252))

def render(bg, wins, pos, finger, cap, show_cap=True, show_pad=True):
    img = bg.copy()
    for i, (wimg, pad) in enumerate(wins):
        x = WX + (i - pos) * W
        if -WW - 2 * pad < x < W:
            img.paste(wimg, (int(round(x)) - pad, WY - pad), wimg)   # paste clips negative offsets
    panel(img)
    if show_pad: touchpad(img, finger)
    if show_cap: caption(img, cap)
    return img

def main():
    os.makedirs(OUT, exist_ok=True)
    bg = wallpaper()
    bg_gif = wallpaper(grain=False)
    wins = [window(WW, WH, t, k) for t, k in WIN]
    frames = simulate()
    print('frames', len(frames), 'seconds', round(len(frames) / FPS, 1))
    # still: mid-slide between the editor and the terminal, at full resolution
    still = render(bg, wins, 0.42, (0.42, 1.0, 'left'), '', show_cap=False)
    still.convert('RGB').save(os.path.join(OUT, 'slide.png'), optimize=True)
    # GIF: shared palette, no dithering (flat UI) -> small and stable between frames
    gh = round(H * GIF_W / W)
    rgb = [render(bg_gif, wins, *fr).convert('RGB').resize((GIF_W, gh), Image.LANCZOS) for fr in frames]
    # palette: mostly wallpaper (its smooth gradient needs the most colours), plus the UI
    wall = render(bg_gif, [], 0, None, '', show_cap=False, show_pad=False).convert('RGB').resize((GIF_W, gh), Image.LANCZOS)
    picks = [0, len(rgb) // 4, len(rgb) // 2, 3 * len(rgb) // 4]
    centred = [render(bg_gif, wins, pg, None, '', show_cap=False).convert('RGB').resize((GIF_W, gh), Image.LANCZOS)
               for pg in (0, 1, 2)]                                   # each window at rest
    extra = [wall, wall, wall] + centred + centred + [rgb[i] for i in picks]
    sample = Image.new('RGB', (GIF_W, gh * len(extra)))
    for k, im in enumerate(extra):
        sample.paste(im, (0, gh * k))
    palette = sample.quantize(colors=255, method=Image.Quantize.MEDIANCUT, kmeans=4)
    dith = Image.Dither.FLOYDSTEINBERG if os.environ.get('DITHER') == 'fs' else Image.Dither.NONE
    q = [im.quantize(palette=palette, dither=dith) for im in rgb]
    q[0].save(os.path.join(OUT, 'demo.gif'), save_all=True, append_images=q[1:], duration=round(1000 / FPS),
              loop=0, optimize=True, disposal=1)
    print('wrote', os.path.join(OUT, 'demo.gif'), os.path.getsize(os.path.join(OUT, 'demo.gif')), 'bytes')

if __name__ == '__main__':
    main()

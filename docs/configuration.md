# Configuration guide

Open the settings from **System Settings → Extensions**: click the **gear** next to Window
Swipe.

![The Window Swipe settings window](images/settings.png)

- Changes apply from the **next swipe**. A swipe in progress is never interrupted, and nothing
  needs to be restarted.
- **More options (…) → Reset to defaults**, at the top right of the settings window, restores
  the recommended settings: **Calm**, **Balanced**, Plank dock order, three and four fingers.

## Animation

**Release animation** decides how the window glides into place after you lift your fingers.
Every profile starts at the speed your fingers were moving and slows down smoothly to rest
exactly on the window, with no jump and no overshoot. Only the timing differs, by about 15 %
from one profile to the next.

| Profile | Feel |
|---|---|
| Responsive | Quickest glide. For people who want the window in place as soon as possible. |
| Relaxed | A little calmer than Responsive. |
| **Calm** (default) | Smooth and unhurried. The recommended setting. |
| Gentle | Slowest, softest landing. |

Neighbouring profiles are deliberately close; Responsive and Gentle are clearly different.

## Switching sensitivity

**Switching sensitivity** decides what happens when you lift your fingers: switch to the next
window, or go back to where you started. It weighs how far you swiped and how fast your fingers
were moving at the end.

| Preset | When a swipe switches |
|---|---|
| **Balanced** (default) | Past halfway. A quick flick switches earlier; a short, slow swipe goes back. The recommended setting. |
| Sensitive | From 40 % for slow swipes, and flicks switch more easily. |
| Less sensitive | From 60 % for slow swipes, and flicks must be faster. |
| Flick-friendly | Short, quick flicks switch; slow partial swipes still go back. |
| Deliberate | Mostly how far you swiped; only very fast flicks switch early. |

Clear-cut swipes (a long swipe, or a short slow one) behave the same with every preset; the
presets only differ for borderline swipes.

**What the presets don't change:** how far your fingers have to travel to move the window, and
how fast the window follows them. Touchégg and your touchpad driver set those. The
*Activation thresholds → Swipe* slider in System Settings → Gestures only affects Cinnamon's
built-in gesture actions, not Window Swipe.

## Navigation

### Window order

| Option | Order |
|---|---|
| **Plank dock order** (default) | The order of the apps in your Plank dock. Apps that aren't pinned to the dock come after the pinned ones, in the order they were opened. Several windows of one app keep their opening order. |
| Window opening order | The order the windows were opened in. |

With Plank dock order, Window Swipe reads the first dock Plank has enabled at the start of every
swipe, so reordering the dock takes effect on the next swipe. If Plank isn't running, opening
order is used.

**Which windows take part:** the normal windows of the current workspace on the monitor of the
window you start from, including minimized, maximized and fullscreen ones. Windows hidden from
the taskbar, dialogs and windows that bypass the compositor (some games in exclusive
fullscreen) are left out. If a dialog has focus, the slide starts from its main window.

**Directions:** swipe **left** for the next window and **right** for the previous one. From the
desktop, swipe left for the first window and right for the last. At either end of the list the
window gives a little and springs back.

### Fingers

| Option | Swipes Window Swipe handles |
|---|---|
| **Three and four fingers** (default) | Left and right with three or four fingers. |
| Three fingers only | Three-finger swipes. Four-finger swipes run the action assigned to them in System Settings → Gestures. |
| Four fingers only | Four-finger swipes. Three-finger swipes run their assigned action. |

Up, down and pinch gestures, two-finger scrolling and touchscreen gestures are never touched.

## When swipes are ignored

While Window Swipe is enabled, a swipe it can't turn into a slide does nothing, rather than
running the gesture's assigned action. This happens while a menu, Scale or Expo is open, or when
the active window can't take part in a slide (see above).

## Where settings are stored

Cinnamon keeps the settings in
`~/.config/cinnamon/spices/window-swipe@ghareeb/window-swipe@ghareeb.json`. Use the settings
window to change them; if the file is edited by hand and contains an invalid value, Window Swipe
uses the default instead.

<p align="center"><img src="window-swipe@ghareeb/icon.png" width="96" alt=""></p>

<h1 align="center">Window Swipe</h1>

<p align="center">Three- and four-finger touchpad swipes that slide between your windows in the Cinnamon desktop.</p>

<p align="center"><img src="docs/images/demo.gif" width="720" alt="A window sliding out while the next one slides in, following a touchpad swipe"></p>

Window Swipe brings a macOS-inspired way of moving between windows to Cinnamon. Swipe
horizontally with three or four fingers and the current window slides away while the next one
slides in, following your fingers. When you lift them, the window glides into place with the
momentum of your swipe. Swipe quickly several times and each new swipe continues smoothly from
where the last one is.

## Features

- **Follows your fingers.** The windows move with the swipe, so you can look at the next window
  and change your mind before letting go.
- **Smooth, macOS-inspired animation.** The glide starts at your fingers' speed and slows down to
  rest exactly on the window, with no jump at release and no overshoot.
- **Three- and four-finger swipes.** Use either, or limit Window Swipe to one of them.
- **Rapid swipes.** A new swipe takes over the moving windows instead of waiting or jumping.
- **Four animation profiles:** Responsive, Relaxed, **Calm** (default) and Gentle.
- **Five switching-sensitivity presets:** **Balanced** (default), Sensitive, Less sensitive,
  Flick-friendly and Deliberate.
- **Plank-aware order.** Windows follow the order of their apps in the Plank dock, falling back
  to the order they were opened when Plank isn't running.
- **Minimized, maximized and fullscreen windows**, and the desktop, are all part of the slide.
- **Native settings window.** Configure everything from Cinnamon's System Settings; changes apply
  from the next swipe, with no restart needed.
- **Leaves everything else alone.** Real windows never move during a slide, other gestures keep
  their actions, and disabling the extension restores Cinnamon's normal behaviour.

<p align="center"><img src="docs/images/slide.png" width="720" alt="Two windows halfway through a slide"></p>

## Requirements

| | |
|---|---|
| Desktop | Cinnamon 6.6 (X11) |
| Gestures | [Touchégg](https://github.com/JoseExposito/touchegg) installed and running (Linux Mint includes it) |
| Touchpad | Any touchpad with multi-finger gesture support |
| Optional | [Plank](https://launchpad.net/plank) for dock-ordered navigation |

**Gesture settings.** In **System Settings → Gestures**, gestures must be enabled, and **swipe
left** and **swipe right** with **three** and **four** fingers must each have an action assigned.
Any action will do. Cinnamon only passes a gesture on when an action is set for it; while Window
Swipe is enabled it handles these swipes itself, so the assigned action doesn't run.

**Tested on** Linux Mint 22.3 with Cinnamon 6.6.9 (X11), Touchégg 2.0.16, and a single
1920×1080 monitor. Other Cinnamon versions, Wayland and multi-monitor setups have not been
tested yet; reports are welcome.

## Installation

### From Cinnamon Spices

Window Swipe is not yet available in the Cinnamon Spices catalogue; it is being prepared for
submission. Once it is accepted, you'll be able to install it from **System Settings →
Extensions → Download**, by searching for **Window Swipe**.

### From GitHub

1. Download `window-swipe@ghareeb-v1.0.0.zip` from the
   [latest release](https://github.com/m7ghareeb/window-swipe/releases/latest).
2. Extract it into `~/.local/share/cinnamon/extensions/`, so that the folder
   `~/.local/share/cinnamon/extensions/window-swipe@ghareeb/` contains `extension.js`:

   ```sh
   unzip window-swipe@ghareeb-v1.0.0.zip -d ~/.local/share/cinnamon/extensions/
   ```

3. Open **System Settings → Extensions**, select **Window Swipe** and enable it.

To check the download, compare it with `SHA256SUMS` from the same release:
`sha256sum -c SHA256SUMS`.

<p align="center"><img src="docs/images/extensions-list.png" width="620" alt="Window Swipe in the Extensions list, with its settings button"></p>

## Configuration

Click the gear next to Window Swipe in **System Settings → Extensions**. Changes apply from the
next swipe; a swipe in progress is never interrupted. To start over, use **⋮ → Reset to
defaults** in the settings window.

<p align="center"><img src="docs/images/settings.png" width="560" alt="The Window Swipe settings window"></p>

### Animation

How the window glides into place after you lift your fingers. Every profile uses the same smooth
curve and continues at your fingers' speed; they differ only in timing, about 15 % apart.

| Profile | Feel |
|---|---|
| Responsive | Quickest glide |
| Relaxed | A little calmer |
| **Calm** (default) | Smooth and unhurried |
| Gentle | Slowest, softest landing |

Neighbouring profiles are deliberately subtle. Responsive and Gentle are clearly different.

### Touchpad sensitivity

What happens when you lift your fingers: switch to the next window or go back.

| Preset | Behaviour |
|---|---|
| **Balanced** (default) | Past halfway switches. A quick flick switches earlier. A short, slow swipe goes back. |
| Sensitive | Slow swipes switch from 40 %, and flicks switch more easily. |
| Less sensitive | Slow swipes need 60 %, and flicks must be faster. |
| Flick-friendly | Short, quick flicks switch; slow partial swipes still go back. |
| Deliberate | Mostly how far you swiped decides; only very fast flicks switch early. |

These presets change only the decision at release. How far your fingers must travel and how
fast the window follows them are set by Touchégg and your touchpad driver, and are not changed.
Clear-cut swipes behave the same with every preset; only borderline swipes differ.

### Navigation

- **Window order:** *Plank dock order* (default) or *window opening order*. With Plank order,
  windows follow their apps' positions in the dock, and apps that aren't pinned come after the
  pinned ones. If Plank isn't running, opening order is used.
- **Fingers:** *three and four* (default), *three only* or *four only*. Swipes with the other
  finger count run the action assigned to them in System Settings → Gestures.

Swipe **left** for the next window and **right** for the previous one. From the desktop, swipe
left for the first window and right for the last. At either end of the list the window gives a
little and springs back.

## Updates

Cinnamon looks for extension updates in the Cinnamon Spices catalogue. When Window Swipe is
available there and installed from it, new versions will appear in **System Settings →
Extensions** once they have been reviewed and accepted into Cinnamon Spices. Copies installed
manually from GitHub are not updated automatically; download the new release, or reinstall from
Cinnamon Spices once available. New versions are listed on the
[releases page](https://github.com/m7ghareeb/window-swipe/releases).

## Troubleshooting and FAQ

**Nothing happens when I swipe.**
Check that gestures are enabled in **System Settings → Gestures** and that swipe left and swipe
right with three and four fingers each have an action assigned. Then check that Touchégg is
running: `systemctl status touchegg`.

**Swipes run my old action (for example Alt+Tab) instead of sliding.**
Make sure Window Swipe is enabled, and check the *Fingers* setting: swipes with a finger count
that Window Swipe doesn't handle keep their assigned action.

**Can I swipe toward one window, change my mind, and continue to the window on the other side
without lifting my fingers?**
You can move toward a window and back, but not past the starting window to the other side within
the same swipe. Lift your fingers and swipe again; the new swipe continues smoothly from where the
windows are. See [Known limitations](#known-limitations).

**The order of my windows looks wrong.**
With Plank order, windows follow the apps pinned in your first Plank dock. Reorder the dock and
the next swipe uses the new order. Choose *Window opening order* if you prefer that.

**Some windows are skipped.**
Only windows on the current workspace and on the same monitor are included. Windows that bypass
the compositor, such as some games in exclusive fullscreen, can't be shown in the slide and are
skipped.

**Nothing happens on the lock screen.** Cinnamon ignores touchpad gestures while the screen is locked.

**Where can I see errors?** Open Looking Glass (`Alt+F2`, then `lg`) or look in
`~/.xsession-errors` for lines containing `window-swipe`.

## Known limitations

- **One direction per swipe.** Touchégg fixes a swipe's direction when it starts and reports no
  movement once the fingers return past the starting point, so a single swipe can't continue past
  the starting window to the window on the other side. Lift your fingers and swipe again.
- Only the current workspace and the monitor of the starting window are included; multi-monitor
  setups have not been tested.
- Windows that bypass the compositor are skipped.
- Tested on Cinnamon 6.6 (X11) only.

## Privacy

Window Swipe makes no network connections, runs no other programs and writes no files. Its only
stored data is its settings, kept by Cinnamon in
`~/.config/cinnamon/spices/window-swipe@ghareeb/`.

## Reporting bugs and requesting features

Please use [GitHub Issues](https://github.com/m7ghareeb/window-swipe/issues) and choose
*Bug report* or *Feature request*. For bugs, include your Linux distribution, Cinnamon version
(`cinnamon --version`), Touchégg version (`touchegg --version`) and the steps to reproduce. For
security issues, see [SECURITY.md](SECURITY.md).

## Contributing

Contributions are welcome: bug fixes, improvements, new animation profiles, documentation and
translations. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our
[Code of Conduct](CODE_OF_CONDUCT.md). In short: fork the repository, make your change on a
branch, test it, and open a pull request against `main`.

## License

Window Swipe is free software, released under the
[GNU General Public License v3.0 or later](LICENSE).

## Credits

**Created by Mohamed Ghareeb**
GitHub: [@m7ghareeb](https://github.com/m7ghareeb)

Window Swipe builds on the Cinnamon desktop, the Muffin window manager and Touchégg.

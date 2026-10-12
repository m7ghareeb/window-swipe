# Contributing to Window Swipe

Thank you for your interest in Window Swipe! Everyone is welcome to read the code, learn from it,
report problems, suggest ideas and propose changes.

## Ways to contribute

- **Report a bug** or **suggest a feature** with [GitHub Issues](https://github.com/m7ghareeb/window-swipe/issues).
- **Improve the documentation**: README, explanations, screenshots.
- **Fix a bug or improve the code** with a pull request.
- **Suggest a new animation profile or sensitivity preset.** Please describe the feel you are aiming
  for and how it differs from the existing ones, ideally after trying it on a real touchpad.
- **Translate** the settings window, once translation files are set up (see below).

For larger changes, please open an issue first to discuss the idea. It saves time for everyone,
and some changes may not fit the project's goals.

## How to propose a change

1. **Fork** the repository on GitHub.
2. **Create a branch** for your change, for example `fix/edge-bounce` or `feature/new-profile`:
   ```sh
   git clone https://github.com/<your-username>/window-swipe.git
   cd window-swipe
   git checkout -b fix/short-description
   ```
3. **Make and test your change** (see *Testing* below).
4. **Open a pull request** against the `main` branch of `m7ghareeb/window-swipe`, and fill in the
   pull request template: what changed, why, and how you tested it.
5. **Wait for review.** The maintainer will review your pull request, may ask questions or
   request changes, and decides whether to merge it.

A pull request is a proposal. Opening one does not mean it will be accepted. Changes are merged
only after review and approval by the maintainer, Mohamed Ghareeb (@m7ghareeb), who is the only
person who merges into `main`. Thank you for your understanding. Every contribution is read and
appreciated, even when it isn't merged.

## Project layout

| Path | Contents |
|---|---|
| `window-swipe@ghareeb/` | The extension: `extension.js`, `metadata.json`, `settings-schema.json`, `icon.png` |
| `spices/` | Files for the Cinnamon Spices catalogue: `info.json`, `screenshot.png`, `README.md` |
| `tools/` | Build scripts for release archives and the Cinnamon Spices folder |
| `docs/` | Images, release notes and maintainer documentation |

`extension.js` is commented. Good places to start reading: `patchedMakeAction` (how swipes are
intercepted), `SlideSession` (the slide and its animation) and `eligibleWindows` (window order).

## Testing

To try your change, copy the extension folder over your installed copy, then reload it:

```sh
cp window-swipe@ghareeb/* ~/.local/share/cinnamon/extensions/window-swipe@ghareeb/
```

Disable and re-enable Window Swipe in **System Settings → Extensions** (or restart Cinnamon with
`Ctrl+Alt+Esc`). Watch for errors in Looking Glass (`Alt+F2`, `lg`) or in `~/.xsession-errors`.

Please test on a real touchpad, and mention the results in your pull request:

- Three- and four-finger swipes, left and right: a full swipe, a slow swipe, a quick flick, a short
  swipe that goes back, and pulling back after passing halfway.
- Several quick swipes in a row, including changing direction during the glide.
- Starting from a minimized target, a maximized window, a fullscreen window and the desktop, and
  swiping past the first and last windows.
- With Plank running and without it, if your change touches window order.
- Changing settings in the settings window while using the extension.
- Disabling the extension during a swipe: nothing should be left on screen.

Include your Cinnamon version, distribution and touchpad. If your change affects the animation,
a short screen recording helps a lot.

The automatic checks on pull requests validate the JavaScript syntax, the JSON files, the
Cinnamon Spices folder layout (using the official `validate-spice` script) and the reproducible
release build. They don't replace testing on a touchpad.

## Coding guidelines

- Follow the existing style: 4-space indentation, `const`/`let`, comments that explain *why*.
- Keep changes focused. One pull request should do one thing.
- Release everything you create in `disable()`: timers, signal handlers, actors.
- No network access, no external programs, no files written outside Cinnamon's settings.
- Use only JavaScript that Cinnamon's engine supports (SpiderMonkey 102 or newer).
- Don't change the defaults (Calm and Balanced) or the existing profiles without discussing it
  first in an issue. They were tuned and measured on real touchpad swipes.
- Keep `metadata.json` ASCII-only. Cinnamon Spices requires that.

## Translations

The settings window's text comes from `settings-schema.json`. Translation files (`.po`) would go
in `window-swipe@ghareeb/po/`, following the Cinnamon Spices conventions. If you'd like to
translate, please open an issue first so the template can be set up.

## Code of Conduct

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions are licensed under the
[GPL-3.0-or-later](LICENSE), the same license as the project.

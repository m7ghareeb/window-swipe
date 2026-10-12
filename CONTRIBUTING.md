# Contributing to Window Swipe

Thank you for your interest in Window Swipe! Everyone is welcome to read the code, learn from it,
ask questions, report problems, suggest ideas and propose changes.

## Where to start

| You want to… | Go to |
|---|---|
| Ask a question or get help | [Discussions → Q&A](https://github.com/m7ghareeb/window-swipe/discussions/categories/q-a) |
| Share an idea or discuss a possible feature | [Discussions → Ideas](https://github.com/m7ghareeb/window-swipe/discussions/categories/ideas) |
| Report a bug | [Issues → Bug report](https://github.com/m7ghareeb/window-swipe/issues/new?template=bug_report.yml) |
| Request a specific, actionable feature | [Issues → Feature request](https://github.com/m7ghareeb/window-swipe/issues/new?template=feature_request.yml) |
| Report a security problem | Privately, as described in [SECURITY.md](SECURITY.md) |
| Change code or documentation | A pull request, as described below |

Other welcome contributions: improving the documentation and screenshots, testing on setups that
haven't been tested yet (other Cinnamon versions, multiple monitors) and sharing the results,
suggesting a new animation profile or sensitivity preset (please describe the feel you're aiming
for, ideally after trying it on a real touchpad), and translations, once translation files are
set up (see below).

For larger changes, please start a discussion or open an issue first. It saves time for
everyone, and some changes may not fit the project's goals.

## How to propose a change

1. **Fork** the repository on GitHub.
2. **Create a branch** for your change, for example `fix/edge-bounce` or `feature/new-profile`.
3. **Make and test your change.** The [developer guide](docs/development.md) explains the setup,
   the code and the tools; test with the [checklist below](#testing-checklist).
4. **Open a pull request** against the `main` branch of `m7ghareeb/window-swipe`, and fill in the
   pull request template: what changed, why, and how you tested it.
5. **Wait for review.** The maintainer reviews every pull request, may ask questions or request
   changes, and decides whether to merge it. The automatic checks run once the maintainer has
   approved them.

A pull request is a proposal. Opening one doesn't mean it will be accepted. Changes are merged
only after review and approval by the maintainer, Mohamed Ghareeb (@m7ghareeb), who is the only
person who merges into `main`. Every contribution is read and appreciated, even when it isn't
merged. Thank you for your understanding.

## Testing checklist

Please test on a real touchpad and mention the results in your pull request:

- Three- and four-finger swipes, left and right: a full swipe, a slow swipe, a quick flick, a short
  swipe that goes back, and pulling back after passing halfway.
- Several quick swipes in a row, including changing direction during the glide.
- Starting from a minimized target, a maximized window, a fullscreen window and the desktop, and
  swiping past the first and last windows.
- With Plank running and without it, if your change touches window order.
- Changing settings in the settings window while using the extension.
- Disabling the extension during a swipe: nothing should be left on screen.
- No `[window-swipe]` errors in Looking Glass or `~/.xsession-errors`.

Include your Cinnamon version, distribution and touchpad. If your change affects the animation,
a short screen recording helps a lot.

The automatic checks validate the JavaScript syntax, the JSON files, the Cinnamon Spices folder
layout and the reproducible release build. They don't replace testing on a touchpad.

## Guidelines

- Keep changes focused: one pull request should do one thing.
- Follow the existing code style; see [Code style](docs/development.md#code-style).
- Don't change the defaults (Calm and Balanced) or the existing profiles without discussing it
  first. They were tuned and measured on real touchpad swipes.
- If your change is visible to users, add a line under `## [Unreleased]` in
  [CHANGELOG.md](CHANGELOG.md) and update the documentation.

## Translations

The settings window's text comes from `settings-schema.json`. Translation files (`.po`) would go
in `window-swipe@ghareeb/po/`, following the Cinnamon Spices conventions. If you'd like to
translate, please open an issue first so the template can be set up.

## Code of Conduct

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions are licensed under the
[GPL-3.0-or-later](LICENSE), the same license as the project.

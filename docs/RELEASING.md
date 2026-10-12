# Maintainer guide: releases and Cinnamon Spices updates

This document is for the maintainer. It describes how a change goes from this repository to
users, and how Cinnamon Spices fits in.

## How the pieces relate

| | This GitHub repository | Cinnamon Spices |
|---|---|---|
| What it is | The upstream source: development, issues, pull requests, GitHub Releases | The official catalogue that Cinnamon installs from (`linuxmint/cinnamon-spices-extensions`) |
| Who merges | The maintainer (@m7ghareeb) | The Linux Mint Spices team, after their review |
| What users see | Release notes and archives on the Releases page | System Settings → Extensions → Download, plus update notifications |

Merging into `main` here, or publishing a GitHub Release, **does not** update Cinnamon Spices.
Each Spices update is a separate pull request to `linuxmint/cinnamon-spices-extensions`, which
the Spices team reviews and merges.

## How Cinnamon finds updates

These points were checked in Cinnamon 6.6 (`cinnamon-settings/bin/Spices.py`) and against the live
index at <https://cinnamon-spices.linuxmint.com/json/extensions.json>.

- Cinnamon downloads the catalogue index `extensions.json`. Each entry has a `last_edited`
  timestamp (the last upstream commit touching the spice), a `last_commit_subject`, and the
  download file.
- When a spice is installed from the catalogue, Cinnamon writes that `last_edited` value into the
  installed `metadata.json` as `last-edited`.
- **An update is offered when the catalogue's `last_edited` is newer than the installed
  `last-edited`.** The `version` field in `metadata.json` is not used for this. It is shown to
  users, so keep it correct (SemVer), but bumping it doesn't trigger updates. Any accepted Spices
  commit to the spice does.
- The text users see about a change comes from the upstream Spices commit (its subject). The
  GitHub Release notes and `CHANGELOG.md` here are the detailed changelog for people who visit the
  repository. Spices also displays the spice's `README.md` (`spices/README.md`), and `CHANGELOG.md`
  is copied into the Spices folder.
- Copies installed manually (unzipped from GitHub) carry no `last-edited` and get no update
  notifications.

## Release workflow

1. **Develop on branches.** Every change reaches `main` through a pull request. CI (`Validate`)
   must pass, and the maintainer reviews and merges.
2. **Regression-test on a real touchpad.** Use the checklist in `CONTRIBUTING.md`, plus anything
   specific to the change. Record results in the release pull request.
3. **Prepare the release in a pull request:**
   - Raise `version` in `window-swipe@ghareeb/metadata.json` following SemVer: 1.0.1 for fixes,
     1.1.0 for compatible features, 2.0.0 for breaking changes.
   - Add a `## [x.y.z] - date` section at the top of `CHANGELOG.md`; CI checks that the two match.
   - Add release notes as `docs/releases/vx.y.z.md`.
4. **Tag and publish the GitHub Release** from the merged commit on `main`:
   ```sh
   git switch main && git pull
   git tag -a vX.Y.Z -m "Window Swipe X.Y.Z"
   git push origin vX.Y.Z
   tools/build-release.sh vX.Y.Z
   gh release create vX.Y.Z dist/vX.Y.Z/window-swipe@ghareeb-vX.Y.Z.zip dist/vX.Y.Z/SHA256SUMS \
      --title "Window Swipe vX.Y.Z" --notes-file docs/releases/vX.Y.Z.md
   ```
   `tools/build-release.sh` builds from the tag with fixed timestamps and permissions, so anyone
   can rebuild the same archive and compare checksums.
5. **Prepare the Cinnamon Spices update** (local only; nothing is pushed):
   ```sh
   tools/prepare-spices-pr.sh vX.Y.Z ~/Projects/cinnamon-spices-extensions "Update to X.Y.Z"
   ```
   The script builds the Spices folder from the tag, copies it into a local clone of your fork of
   `linuxmint/cinnamon-spices-extensions` on a new branch, runs the official `validate-spice`, and
   commits as `window-swipe@ghareeb: Update to X.Y.Z`. It stops there and prints the push and PR
   commands. Run them only when you have decided to submit.
6. **Submit for review.** Push the branch to your fork and open the pull request to
   `linuxmint/cinnamon-spices-extensions`. Titles must follow `window-swipe@ghareeb: description`,
   with one spice per pull request. Answer the reviewers' questions there.
7. **After the Spices team merges**, the Spices website and index update. Cinnamon then shows the
   update in System Settings → Extensions. Check it on a machine with the previous version
   installed from Spices.

## First-time Spices submission

The same as step 5, with the subject `Initial release`, and a fresh fork:
```sh
gh repo fork linuxmint/cinnamon-spices-extensions --clone=true    # once, into ~/Projects
tools/prepare-spices-pr.sh v1.0.0 ~/Projects/cinnamon-spices-extensions "Initial release"
```

## Automation policy

CI builds the release archive and the Spices folder for every change and uploads them as a
workflow artifact. Submitting to Cinnamon Spices is always a manual, deliberate step by the
maintainer. No workflow pushes to Spices, opens upstream pull requests or merges anything.

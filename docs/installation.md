# Installation guide

This guide covers installing, updating and removing Window Swipe. For a quick start, see the
[README](../README.md#installation).

## Before you start

- **Cinnamon 6.6 on X11.** Check with `cinnamon --version`. Linux Mint 22.3 uses Cinnamon 6.6.
- **Touchégg** must be installed and running. Linux Mint installs it by default. Check with:

  ```sh
  systemctl status touchegg
  ```

  It should say `active (running)`. If Touchégg is missing, install it with
  `sudo apt install touchegg`.
- A touchpad that supports **three- and four-finger** gestures.

## Install from Cinnamon Spices *(coming soon)*

Window Swipe is not yet available in the Cinnamon Spices catalogue. Once it is, you'll be able
to install it from **System Settings → Extensions → Download** by searching for *Window Swipe*,
and Cinnamon will offer updates automatically.

## Install from GitHub

### With a terminal

```sh
cd ~/Downloads
wget https://github.com/m7ghareeb/window-swipe/releases/download/v1.0.0/window-swipe@ghareeb-v1.0.0.zip \
     https://github.com/m7ghareeb/window-swipe/releases/download/v1.0.0/SHA256SUMS
sha256sum -c SHA256SUMS
mkdir -p ~/.local/share/cinnamon/extensions
unzip -o window-swipe@ghareeb-v1.0.0.zip -d ~/.local/share/cinnamon/extensions/
```

`sha256sum -c` should print `window-swipe@ghareeb-v1.0.0.zip: OK`. If it reports `FAILED`, the
download is damaged or isn't the published file: delete it and download it again.

### Without a terminal

1. Open the [latest release](https://github.com/m7ghareeb/window-swipe/releases/latest) and
   download `window-swipe@ghareeb-v1.0.0.zip`.
2. Open the zip and extract it. You get a folder named `window-swipe@ghareeb`.
3. In your home folder, press **Ctrl+H** to show hidden folders, then open
   `.local/share/cinnamon/extensions` (create the `extensions` folder if it's missing).
4. Move the `window-swipe@ghareeb` folder there. It must contain `extension.js` directly, not
   another folder.

### Enable the extension

1. Open **System Settings → Extensions**.
2. Select **Window Swipe** and click the **+** button (*Enable*) at the bottom. A check mark
   appears next to it.
3. Set up gestures once, as described in the next section.

## Set up gestures (one time)

Window Swipe receives swipes through Cinnamon's gesture support:

1. Open **System Settings → Gestures**. On the **Settings** tab, turn on **Enable gestures**.
2. On the **Swipe** tab, under **Swipe with 3 fingers** and **Swipe with 4 fingers**, check that
   **Left** and **Right** each have an action, not *Disabled*. Cinnamon's defaults already
   assign actions to them (switching workspace with three fingers, moving the window to
   another workspace with four), so usually there is nothing to change.

**Any action works.** Cinnamon only passes on swipes that have an action. While Window Swipe is
enabled, it handles these swipes itself and the action doesn't run. The action is used again
when you turn Window Swipe off, or for a finger count you exclude in the
[Fingers setting](configuration.md#fingers). If one of them is *Disabled*, *Switch to right
workspace* for **Left** and *Switch to left workspace* for **Right** are sensible choices.

Now swipe **left** with three or four fingers for the next window and **right** for the
previous one. If nothing happens, see the [troubleshooting guide](troubleshooting.md).

## Updating

Window Swipe isn't on Cinnamon Spices yet, so copies installed from GitHub aren't updated
automatically. To be notified of new versions, click **Watch → Custom → Releases** on the
[repository page](https://github.com/m7ghareeb/window-swipe).

To update a GitHub installation:

1. Download the new release's zip and `SHA256SUMS` from the
   [releases page](https://github.com/m7ghareeb/window-swipe/releases), and check them with
   `sha256sum -c SHA256SUMS`.
2. Replace the old files, so that none are left behind:

   ```sh
   rm -r ~/.local/share/cinnamon/extensions/window-swipe@ghareeb
   unzip window-swipe@ghareeb-vX.Y.Z.zip -d ~/.local/share/cinnamon/extensions/
   ```

   Replace `X.Y.Z` with the new version. Your settings are stored elsewhere and are kept.
3. Restart Cinnamon to load the new version: press **Ctrl+Alt+Esc**, or log out and back in.
   Your open windows stay open.

The [changelog](../CHANGELOG.md) lists what changed in each version.

Once Window Swipe is available on Cinnamon Spices, installing it from there replaces these
manual steps: Cinnamon shows updates in **System Settings → Extensions**.

## Uninstalling

1. In **System Settings → Extensions**, select **Window Swipe** and click the **−** button to
   disable it. Your gestures go back to the actions assigned in System Settings → Gestures.
2. Remove its files:

   ```sh
   rm -r ~/.local/share/cinnamon/extensions/window-swipe@ghareeb
   ```

3. Optionally, remove its settings too:

   ```sh
   rm -r ~/.config/cinnamon/spices/window-swipe@ghareeb
   ```

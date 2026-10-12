# Troubleshooting and FAQ

If your problem isn't covered here, ask in
[Discussions → Q&A](https://github.com/m7ghareeb/window-swipe/discussions/categories/q-a) or
[report a bug](https://github.com/m7ghareeb/window-swipe/issues/new/choose).

## Nothing happens when I swipe

Check these in order:

1. **Is Window Swipe enabled?** In **System Settings → Extensions**, Window Swipe should have a
   check mark next to it.
2. **Are gestures enabled?** In **System Settings → Gestures → Settings**, **Enable gestures**
   must be on. If the Gestures page says *The Touchegg service is not running*, see step 4.
3. **Do the swipes have an action?** In **System Settings → Gestures → Swipe**, **Left** and
   **Right** under **Swipe with 3 fingers** and **Swipe with 4 fingers** must each have an
   action, not *Disabled*. Any action works; Cinnamon ignores swipes that have none. See
   [Gesture setup](installation.md#set-up-gestures-one-time).
4. **Is Touchégg running?**

   ```sh
   systemctl status touchegg
   ```

   It should say `active (running)`. If it doesn't, start it with
   `sudo systemctl restart touchegg`, or install it with `sudo apt install touchegg`.
5. **Does your touchpad report multi-finger gestures?** Try a three-finger swipe up, which opens
   Expo (the workspace overview) with Cinnamon's default gestures. If that doesn't work either,
   the problem is with the touchpad or Touchégg, not Window Swipe.

## My old action runs instead of a slide

- Window Swipe is disabled. Enable it in **System Settings → Extensions**.
- The **Fingers** setting excludes that finger count. For example, with *Three fingers only*,
  four-finger swipes run the action assigned to them in System Settings → Gestures. See
  [Fingers](configuration.md#fingers).
- Touchscreen swipes are never handled by Window Swipe; only touchpad swipes are.

## A swipe does nothing

While Window Swipe is enabled, a swipe that can't become a slide is ignored. This is
intentional, and happens:

- while a menu, Scale or Expo is open;
- when the active window can't take part in a slide, for example a window hidden from the
  taskbar or one that bypasses the compositor;
- at either end of the window list, where the window gives a little and springs back.

## Some windows are skipped

Only the normal windows of the **current workspace** on the **monitor of the window you start
from** take part. Dialogs, windows hidden from the taskbar and windows that bypass the
compositor (such as some games in exclusive fullscreen) are left out. Minimized, maximized and
fullscreen windows are included.

## The window order looks wrong

- With **Plank dock order**, windows follow the apps pinned in the **first** Plank dock. Apps
  that aren't pinned come after the pinned ones, in the order they were opened. Reorder the dock
  and the next swipe uses the new order.
- If Plank isn't running, windows follow the order they were opened in.
- To ignore the dock, choose **Window opening order** in the settings.

## Switching feels too easy or too hard

Try another **Switching sensitivity** preset: *Sensitive* switches more easily, *Less
sensitive* and *Deliberate* need more. If the window feels like it needs too much or too little
finger travel overall, that's set by Touchégg and your touchpad driver, not by Window Swipe. See
[Switching sensitivity](configuration.md#switching-sensitivity).

## Can I go past the starting window within one swipe?

No. Within one swipe you can move toward a window and back, but not past the starting window to
the window on the other side: Touchégg fixes a swipe's direction when it starts and reports no
movement once your fingers return past the starting point. Lift your fingers and swipe again;
the new swipe continues smoothly from where the windows are.

## Nothing happens on the lock screen

Cinnamon ignores touchpad gestures while the screen is locked.

## Does it work on Wayland, with multiple monitors, or other Cinnamon versions?

Window Swipe has been tested on Cinnamon 6.6 on X11 with a single monitor. Other setups haven't
been tested. With several monitors, only the windows on the monitor of the window you start from
take part. If you try another setup, please share your results in
[Discussions](https://github.com/m7ghareeb/window-swipe/discussions).

## Collecting information for a bug report

- **Versions:**

  ```sh
  cinnamon --version
  touchegg --version
  grep '"version"' ~/.local/share/cinnamon/extensions/window-swipe@ghareeb/metadata.json
  ```

- **Log messages.** Window Swipe's messages start with `[window-swipe]`:

  ```sh
  grep -i 'window-swipe' ~/.xsession-errors | tail -n 50
  ```

  You can also open Looking Glass (**Alt+F2**, type `lg`, press **Enter**) and look at its
  **Logs** tab.
- **Your settings:** animation, sensitivity, window order and fingers, as shown in the settings
  window. Say whether the problem also happens with the defaults (**More options (…) → Reset to
  defaults**).

Then [open a bug report](https://github.com/m7ghareeb/window-swipe/issues/new?template=bug_report.yml).

## Turning Window Swipe off

Disable it in **System Settings → Extensions** (select it and click **−**). Your swipes go back
to the actions assigned in System Settings → Gestures immediately. If Cinnamon ever behaves
strangely, restarting it with **Ctrl+Alt+Esc** keeps your windows open.

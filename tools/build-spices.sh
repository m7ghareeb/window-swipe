#!/bin/sh
# Assembles the Cinnamon Spices submission folder from a committed revision (default HEAD):
#   dist/spices/window-swipe@ghareeb/{info.json, screenshot.png, README.md (from spices/), CHANGELOG.md,
#                                     files/window-swipe@ghareeb/{extension.js, metadata.json,
#                                     settings-schema.json, icon.png, LICENSE}}
# and runs the official validate-spice script on it if it is given as $2.
#   tools/build-spices.sh [revision] [path/to/validate-spice]
set -eu
REV=${1:-HEAD}
UUID=window-swipe@ghareeb
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)
cd "$ROOT"
OUT="$ROOT/dist/spices"
rm -rf "$OUT"; mkdir -p "$OUT/$UUID/files/$UUID"
for f in info.json screenshot.png README.md; do git show "$REV:spices/$f" > "$OUT/$UUID/$f"; done
git show "$REV:CHANGELOG.md" > "$OUT/$UUID/CHANGELOG.md"
for f in extension.js metadata.json settings-schema.json icon.png; do git show "$REV:$UUID/$f" > "$OUT/$UUID/files/$UUID/$f"; done
git show "$REV:LICENSE" > "$OUT/$UUID/files/$UUID/LICENSE"
find "$OUT" -type d -exec chmod 755 {} +; find "$OUT" -type f -exec chmod 644 {} +
echo "assembled $OUT/$UUID from $(git rev-parse --short "$REV")"
if [ $# -ge 2 ]; then
    cp "$2" "$OUT/validate-spice"
    (cd "$OUT" && python3 -I validate-spice "$UUID")
    rm "$OUT/validate-spice"
fi

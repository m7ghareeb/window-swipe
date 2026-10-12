#!/bin/sh
# Builds the release archive from a committed revision (default HEAD), reproducibly:
# same revision -> byte-identical zip. Output: dist/v<version>/
#   tools/build-release.sh [revision]
set -eu
REV=${1:-HEAD}
UUID=window-swipe@ghareeb
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)
cd "$ROOT"
VERSION=$(git show "$REV:$UUID/metadata.json" | python3 -c 'import json,sys; print(json.load(sys.stdin)["version"])')
EPOCH=$(git log -1 --format=%ct "$REV")
OUT="$ROOT/dist/v$VERSION"
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT

mkdir -p "$STAGE/$UUID" "$OUT"
for f in extension.js metadata.json settings-schema.json icon.png; do
    git show "$REV:$UUID/$f" > "$STAGE/$UUID/$f"
done
for f in LICENSE README.md CHANGELOG.md; do
    git show "$REV:$f" > "$STAGE/$UUID/$f"
done
# normalise everything that could differ between builds
find "$STAGE" -type d -exec chmod 755 {} +
find "$STAGE" -type f -exec chmod 644 {} +
find "$STAGE" -exec touch -h -d "@$EPOCH" {} +
ZIP="$OUT/$UUID-v$VERSION.zip"
rm -f "$ZIP"
(cd "$STAGE" && find "$UUID" -type f | LC_ALL=C sort | TZ=UTC zip -X -D -q "$ZIP" -@)
(cd "$OUT" && sha256sum "$(basename "$ZIP")" > SHA256SUMS)
echo "built $ZIP from $(git rev-parse --short "$REV") (version $VERSION)"
cat "$OUT/SHA256SUMS"

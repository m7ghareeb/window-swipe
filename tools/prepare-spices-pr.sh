#!/bin/sh
# Prepares (but never submits) a Cinnamon Spices pull request for a released version.
#   tools/prepare-spices-pr.sh <tag> <path to local clone of your fork of linuxmint/cinnamon-spices-extensions> "<subject>"
# Builds the Spices folder from <tag>, copies it into the fork clone on a new branch, runs the
# official validate-spice from that clone and commits "window-swipe@ghareeb: <subject>".
# It does NOT push or open a pull request; it prints those commands for the maintainer.
set -eu
TAG=$1; FORK=$2; SUBJECT=$3
UUID=window-swipe@ghareeb
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)
git -C "$ROOT" rev-parse --verify --quiet "$TAG^{commit}" > /dev/null || { echo "unknown tag $TAG"; exit 1; }
test -f "$FORK/validate-spice" || { echo "$FORK is not a clone of cinnamon-spices-extensions"; exit 1; }
test -z "$(git -C "$FORK" status --porcelain)" || { echo "$FORK has uncommitted changes"; exit 1; }

"$ROOT/tools/build-spices.sh" "$TAG"
BRANCH="$UUID-$TAG"
git -C "$FORK" fetch -q https://github.com/linuxmint/cinnamon-spices-extensions.git master
git -C "$FORK" switch -q -c "$BRANCH" FETCH_HEAD
rm -rf "$FORK/$UUID"
cp -r "$ROOT/dist/spices/$UUID" "$FORK/$UUID"
(cd "$FORK" && python3 validate-spice "$UUID")
git -C "$FORK" add "$UUID"
git -C "$FORK" commit -q -m "$UUID: $SUBJECT"
echo
echo "Prepared branch $BRANCH in $FORK (not pushed):"
git -C "$FORK" show --stat --oneline HEAD | head -20
echo
echo "To submit, after review and only when you decide to:"
echo "  git -C '$FORK' push -u origin $BRANCH"
echo "  gh pr create --repo linuxmint/cinnamon-spices-extensions --base master --head m7ghareeb:$BRANCH \\"
echo "     --title '$UUID: $SUBJECT' --body-file '$ROOT/docs/releases/$TAG.md'"

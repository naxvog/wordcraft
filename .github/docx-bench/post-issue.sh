#!/bin/sh
# usage: post-issue.sh [issue]   Run on your machine, not in Actions: a token from this fork can't edit an issue in
# storytold/wordcraft. Posts the body the last bench round rendered into the bench-results branch; runs no PR code.
set -e
f=$(mktemp); trap 'rm -f "$f"' EXIT
gh api -H 'Accept: application/vnd.github.raw' 'repos/naxvog/wordcraft/contents/issue-body.md?ref=bench-results' > "$f"
[ -s "$f" ] && gh issue edit "${1:-5711}" -R storytold/wordcraft --body-file "$f"

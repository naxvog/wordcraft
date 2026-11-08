#!/bin/bash
# usage: score.sh <tree> <run dir>   (after harness.sh, whose output is in $W/harness.txt)
# Builds wordcraft-cli from <tree> without network (its build scripts and proc macros may be a PR's) and scores
# the whole suite with it; the compact results go to <run dir>. Fails if the build or the suite fails.
set -euo pipefail; . "$(dirname "$0")/lib.sh"
T=$(realpath "$1"); D=$2
docker run --rm "${U[@]}" -v "$T:/src:ro" -w /src docx-build cargo fetch -q --locked
docker run --rm "${U[@]}" "${OFF[@]}" -v "$T:/src:ro" -v "$W/fonts:/fonts:ro" -v "$HOME/c/wc-target:/target" \
  -e CARGO_TARGET_DIR=/target -e CRAFT_FONTS_DIR=/fonts -e CARGO_PROFILE_DEV_DEBUG=0 -w /src docx-build bash -c '
  set -o pipefail
  pk=$(cargo metadata --no-deps --format-version 1 | python3 -c "import json,sys; print(\" \".join(\"-p \"+p[\"name\"] for p in json.load(sys.stdin)[\"packages\"]))")
  cargo clean -q $pk && cargo build -q -p wordcraft-cli 2>&1 | tail -30 && cp /target/debug/wordcraft-cli /target/wordcraft-cli'
rm -rf "$W/out"; mkdir -p "$W/out"
docker run --rm "${U[@]}" "${OFF[@]}" -v "$W/dx:/docxide:ro" -v "$W/out:/docxide/tests/output" -v "$HOME/c/dx-target:/target:ro" \
  -v "$HOME/c/wc-target:/wcpr:ro" -w /docxide docx-bench bash -c "
  WORDCRAFT_CLI=/wcpr/wordcraft-cli $(cat "$W/harness.txt") wordcraft_comparison --nocapture 2>&1 | grep -E 'wrote|panicked|^  (docxide-pdf|WordCraft) '
  python3 textcmp.py"
python3 "$S/compact.py" "$W/out" "$D"

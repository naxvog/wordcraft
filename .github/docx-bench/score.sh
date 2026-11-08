#!/bin/bash
# usage: score.sh <tree> <run dir>   (after harness.sh, whose output is in $W/harness.txt)
# Scores the whole suite with a wordcraft-cli built from <tree>; the compact results go to <run dir>.
#  1. build, without network (the build scripts and proc macros may be a PR's)
#  2. convert every fixture, in a container that sees only copies of the .docx files: the PR's binary never sees
#     Word's reference PDFs, the harness or the scores
#  3. score, in a container that runs no PR code: the harness gets the PDFs from step 2 through convert-stub.sh
# Exit 2: the tree doesn't build. Any other failure is the bench's own (the caller retries the PR next round).
set -euo pipefail; . "$(dirname "$0")/lib.sh"
T=$(realpath "$1"); D=$2
fetch "$T"
docker run --rm "${USR[@]}" "${OFF[@]}" -v "$T:/src:ro" -v "$W/fonts:/fonts:ro" -v "$HOME/c/wc-target:/target" \
  -e CARGO_TARGET_DIR=/target -e CRAFT_FONTS_DIR=/fonts -e CARGO_PROFILE_DEV_DEBUG=0 -w /src docx-bench \
  bash -c 'set -o pipefail; cargo build -q -p wordcraft-cli 2>&1 | tail -30' || exit 2
rm -rf "$W/in" "$W/pdf" "$W/out"; mkdir -p "$W/pdf" "$W/out"
(cd "$W/dx/tests/fixtures" && find . -name input.docx -exec install -D -m 644 {} "$W/in/{}" \;)
docker run --rm "${USR[@]}" "${OFF[@]}" -v "$W/in:/in:ro" -v "$W/pdf:/pdf" -v "$HOME/c/wc-target:/wcpr:ro" -w /in docx-bench bash -c '
  find . -name input.docx -printf "%h\n" | xargs -P "$(nproc)" -I{} sh -c "mkdir -p /pdf/{} && WORDCRAFT_NO_PREFS=1 timeout 180 \
    /wcpr/debug/wordcraft-cli convert /in/{}/input.docx /pdf/{}/wordcraft.pdf >/dev/null 2>&1 || rm -f /pdf/{}/wordcraft.pdf"'
docker run --rm "${USR[@]}" "${OFF[@]}" -v "$W/dx:/docxide:ro" -v "$W/out:/docxide/tests/output" -v "$HOME/c/dx-target:/target:ro" \
  -v "$W/pdf:/pdf:ro" -v "$S/convert-stub.sh:/stub:ro" -w /docxide docx-bench bash -c "
  WORDCRAFT_CLI=/stub $(cat "$W/harness.txt") wordcraft_comparison --nocapture 2>&1 | grep -E 'wrote|panicked|^  (docxide-pdf|WordCraft) '
  python3 textcmp.py"
python3 "$S/compact.py" "$W/out" "$D"

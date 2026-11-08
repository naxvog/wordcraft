#!/bin/bash
# Builds the docxide-pdf suite (our harness, trusted) into ~/c/dx-target before any PR code runs in the job, and
# prints the test binary's path inside the container. Later steps mount the target read-only.
set -euo pipefail; . "$(dirname "$0")/lib.sh"
docker run --rm "${U[@]}" -v "$W/dx:/docxide:ro" -v "$HOME/c/dx-target:/target" -w /docxide docx-bench bash -c \
  'CARGO_TARGET_DIR=/target cargo test -q --release --test suite --no-run --message-format=json 2>/dev/null' \
  | python3 -c 'import json,sys; print([m["executable"] for m in map(json.loads, sys.stdin) if m.get("reason") == "compiler-artifact" and m.get("executable") and m["target"]["name"] == "suite"][-1])'

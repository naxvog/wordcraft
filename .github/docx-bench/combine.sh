#!/bin/bash
# usage: combine.sh <name> [<excluded pr>...]   (in a combine job, after collect.py put this round's runs in $BENCH_STATE)
# Merges every PR whose run raised the suite's SSIM (against that run's baseline) into the current baseline, in
# descending order of gain, at the head scan.py planned; after each merge `cargo check -p wordcraft-cli` must pass
# (no network) or the merge is undone. Records why PRs were left out, then scores the result into $W/run/<name>.
set -uo pipefail; . "$(dirname "$0")/lib.sh"
name=$1; shift; EX="$*"; D=$W/run/$name; base=$(cat "$BENCH_STATE/current-main"); base_sha=$(g rev-parse HEAD)
order=$(EX="$EX" python3 -I - <<'PY'
import os, sys
sys.path.insert(0, os.environ['GITHUB_WORKSPACE'] + '/.github/docx-bench')
from benchlib import B, VER, load, delta, run_base
ex = set(os.environ['EX'].split()); rows = []
for d in os.listdir(f'{B}/runs'):
    if not d.startswith(f'{VER}-pr') or d[len(VER) + 3:] in ex or not (r := load(d)):
        continue
    g = delta(load(run_base(d)), r)['ssim']
    if g > 0.0005: rows.append((g, d[len(VER) + 3:]))
print(' '.join(n for _, n in sorted(rows, reverse=True)))
PY
)
heads=$(python3 -c 'import json,sys; print(" ".join(f"{q[\"n\"]}={q[\"head\"]}" for q in json.load(open(sys.argv[1]))))' "$BENCH_STATE/v66-prs.json")
head_of() { for kv in $heads; do [ "${kv%%=*}" = "$1" ] && echo "${kv#*=}" && return; done; }
check() {
  fetch "$W/wc" >/dev/null 2>&1 &&
  docker run --rm "${U[@]}" "${OFF[@]}" -v "$W/wc:/src:ro" -w /src -v "$HOME/c/wc-target:/target" -v "$W/fonts:/fonts:ro" \
    -e CRAFT_FONTS_DIR=/fonts -e CARGO_TARGET_DIR=/target/check docx-build cargo check -q --locked -p wordcraft-cli >/dev/null 2>&1
}
merged=(); cmain=(); cprs=(); broken=(); gated=()
for p in $order; do
  h=$(head_of "$p")
  { [ -n "$h" ] && g fetch -q origin "pull/$p/head:refs/heads/pr/$p" && [ "$(g rev-parse "pr/$p")" = "$h" ]; } || { gated+=("$p"); continue; }
  python3 -I "$S/gate.py" "$p" >/dev/null || { gated+=("$p"); continue; }
  pre=$(g rev-parse HEAD)
  if g merge-tree --write-tree --name-only --no-messages "$pre" "pr/$p" | tail -n +2 | grep -Ev "$NONCLI" | grep -q .; then
    # conflicts with main itself or with a PR merged before it
    if g merge-tree --write-tree --name-only --no-messages "$base_sha" "pr/$p" | tail -n +2 | grep -Ev "$NONCLI" | grep -q .; then cmain+=("$p"); else cprs+=("$p"); fi
    continue
  fi
  if ! g merge -q --no-edit "pr/$p" >/dev/null 2>&1; then
    u=$(g diff --name-only --diff-filter=U)
    g checkout -q --ours -- $u && g add $u && g commit -q --no-edit || { g merge --abort; g reset -q --hard "$pre"; cprs+=("$p"); continue; }
  fi
  if ! check; then g reset -q --hard "$pre"; broken+=("$p"); continue; fi
  g diff --quiet || g commit -qam "bench: refresh Cargo.lock after #$p"
  merged+=("$p")
done
echo "merged: ${merged[*]}"; echo "conflict with main: ${cmain[*]}"; echo "conflict with earlier PRs: ${cprs[*]}"
echo "doesn't compile with them: ${broken[*]}"; echo "moved or needs a look first: ${gated[*]}"
st=ok; "$S/score.sh" "$W/wc" "$D" || st="bench failed"
meta "$D" name="$name" base="$base" commit="$(g rev-parse HEAD)" status="$st" merged="${merged[*]}" conflicts_main="${cmain[*]}" \
  conflicts_prs="${cprs[*]}" broken="${broken[*]}" gated="${gated[*]}" excluded="$EX"

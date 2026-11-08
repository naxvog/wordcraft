#!/bin/bash
# usage: combine.sh <name> [<excluded pr>...]   (in a combine job, after collect.py put this round's runs in $BENCH_STATE)
# Merges every open PR whose run raised the suite's SSIM (against that run's baseline) into the current baseline, in
# descending order of gain, at the head scan.py planned and gated; after each merge `cargo check -p wordcraft-cli`
# must pass (no network) or the merge is undone. Records why PRs were left out, then scores the result into $W/run/<name>.
set -uo pipefail; . "$(dirname "$0")/lib.sh"
name=$1; shift; EX="$*"; D=$W/run/$name; base=$(cat "$BENCH_STATE/current-main")
# three lines: the merge order as pr=head pairs, PRs that conflict with main, PRs scan.py holds back
mapfile -t plan < <(EX="$EX" python3 -I - <<'PY'
import json, os, sys
sys.path.insert(0, os.environ['GITHUB_WORKSPACE'] + '/.github/docx-bench')
from benchlib import B, VER, TRUSTED, load, delta, run_base
ex = set(os.environ['EX'].split()); rows, cmain, held = [], [], []
for q in json.load(open(f'{B}/{VER}-prs.json')):
    n = str(q['n'])
    if q['draft'] or n in ex or not (r := load(f'{VER}-pr{n}')) or not (b := load(run_base(f'{VER}-pr{n}'))):
        continue
    g = delta(b, r)['ssim']
    if g <= 0.0005:
        continue
    if q['conflicts']:
        cmain.append(n)
    elif not ((q['assoc'] in TRUSTED and not q['risky']) or q['allowed']):
        held.append(n)
    else:
        rows.append((g, f"{n}={q['head']}"))
print(' '.join(p for _, p in sorted(rows, reverse=True))); print(' '.join(cmain)); print(' '.join(held))
PY
)
[ ${#plan[@]} = 3 ] || { echo "could not work out the merge order"; exit 1; }
cmain=(${plan[1]}); gated=(${plan[2]}); merged=(); cprs=(); broken=()
check() {
  fetch "$W/wc" rw >/dev/null 2>&1 &&
  docker run --rm "${USR[@]}" "${OFF[@]}" -v "$W/wc:/src:ro" -w /src -v "$HOME/c/wc-target:/target" -v "$W/fonts:/fonts:ro" \
    -e CRAFT_FONTS_DIR=/fonts -e CARGO_TARGET_DIR=/target/check docx-bench cargo check -q --locked -p wordcraft-cli >/dev/null 2>&1
}
for ph in ${plan[0]}; do
  p=${ph%%=*}; h=${ph#*=}
  { g fetch -q origin "pull/$p/head:refs/heads/pr/$p" && [ "$(g rev-parse "pr/$p")" = "$h" ]; } || { gated+=("$p"); continue; }
  pre=$(g rev-parse HEAD)
  if ! g merge -q --no-edit "pr/$p" >/dev/null 2>&1; then
    u=$(g diff --name-only --diff-filter=U)
    # scan.py found no code conflict with main, so one here is with a PR merged before it
    if [ -z "$u" ] || echo "$u" | grep -Eqv "$NONCLI"; then g merge --abort 2>/dev/null; g reset -q --hard "$pre"; cprs+=("$p"); continue; fi
    g checkout -q --ours -- $u && g add $u && g commit -q --no-edit || { g reset -q --hard "$pre"; cprs+=("$p"); continue; }
  fi
  if ! check; then g reset -q --hard "$pre"; broken+=("$p"); continue; fi
  g diff --quiet || g commit -qam "bench: refresh Cargo.lock after #$p"
  merged+=("$p")
done
echo "merged: ${merged[*]}"; echo "conflict with main: ${cmain[*]}"; echo "conflict with earlier PRs: ${cprs[*]}"
echo "doesn't compile with them: ${broken[*]}"; echo "moved or needs a look first: ${gated[*]}"
"$S/score.sh" "$W/wc" "$D"; rc=$?
[ $rc = 0 ] || [ $rc = 2 ] || exit 1
meta "$D" name="$name" base="$base" commit="$(g rev-parse HEAD)" status="$([ $rc = 0 ] && echo ok || echo 'bench failed: does not build')" \
  merged="${merged[*]}" conflicts_main="${cmain[*]}" conflicts_prs="${cprs[*]}" broken="${broken[*]}" gated="${gated[*]}" excluded="$EX"

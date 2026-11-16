#!/bin/bash
# usage: pr.sh <pr> <head sha> <base run>   (in a bench job: wc/ is storytold/wordcraft at the baseline commit)
# Merges the head scan.py planned into the baseline, moves every craft-libs crate to the round's craft-libs main
# (as in the baseline) and scores it into $W/run/<VER>-pr<n>. Conflicts in
# files wordcraft-cli doesn't build take main's side; code conflicts skip the PR. PR outcomes end in meta.json
# (status=ok or the reason); a failure of the bench itself fails the job, so the PR stays queued for the next round.
set -uo pipefail; . "$(dirname "$0")/lib.sh"
p=$1; head=$2; base=$3; D=$W/run/v67-pr$p
skip() { meta "$D" name="v67-pr$p" pr="$p" pr_head="$head" base="$base" status="$1"; echo "#$p: $1"; exit 0; }
g fetch -q origin "pull/$p/head:refs/heads/pr/$p" || { echo "fetch failed"; exit 1; }
[ "$(g rev-parse "pr/$p")" = "$head" ] || { echo "#$p moved since the plan; benched next round"; exit 0; }
g merge-base --is-ancestor "$(g merge-base "pr/$p" origin/main)" HEAD || skip "contains main commits newer than the baseline"
g merge -q --no-edit "pr/$p" >/dev/null 2>&1
u=$(g diff --name-only --diff-filter=U)
if echo "$u" | grep -Eqv -e "$NONCLI|^$"; then skip "code conflict with main"; fi
if [ -n "$u" ]; then g checkout -q --ours -- $u && g add $u && g commit -q --no-edit || skip "could not take main's side of a docs conflict"; fi
g merge-base --is-ancestor "pr/$p" HEAD || skip "merge failed, not benched"
# every craft-libs crate at the round's craft-libs main, as in the baseline; then re-resolve Cargo.lock (taking
# main's side of a Cargo.toml can leave it stale too)
pre=$(g rev-parse HEAD)
libs || exit 1
fetch "$W/wc" rw >/dev/null 2>&1 || skip "dependencies don't resolve once merged"
g diff --quiet || g commit -qam 'bench: craft-libs main, Cargo.lock' || exit 1
"$S/score.sh" "$W/wc" "$D"; rc=$?
if [ $rc = 2 ]; then  # tell a PR that needs other craft-libs versions from one that doesn't build at all
  g reset -q --hard "$pre"
  builds "$W/wc" && skip "bench failed: doesn't build with craft-libs main"
  skip "bench failed: doesn't build once merged with main"
fi
[ $rc = 0 ] || exit 1
meta "$D" name="v67-pr$p" pr="$p" pr_head="$head" base="$base" commit="$(g rev-parse HEAD)" status=ok

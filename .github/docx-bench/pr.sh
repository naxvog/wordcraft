#!/bin/bash
# usage: pr.sh <pr> <head sha> <base run>   (in a bench job: wc/ is storytold/wordcraft at the baseline commit)
# Merges the head scan.py planned into the baseline and scores it into $W/run/<VER>-pr<n>. Conflicts in
# files wordcraft-cli doesn't build take main's side; code conflicts skip the PR. PR outcomes end in meta.json
# (status=ok or the reason); a failure of the bench itself fails the job, so the PR stays queued for the next round.
set -uo pipefail; . "$(dirname "$0")/lib.sh"
p=$1; head=$2; base=$3; D=$W/run/v66-pr$p
skip() { meta "$D" name="v66-pr$p" pr="$p" pr_head="$head" base="$base" status="$1"; echo "#$p: $1"; exit 0; }
g fetch -q origin "pull/$p/head:refs/heads/pr/$p" || { echo "fetch failed"; exit 1; }
[ "$(g rev-parse "pr/$p")" = "$head" ] || { echo "#$p moved since the plan; benched next round"; exit 0; }
g merge-base --is-ancestor "$(g merge-base "pr/$p" origin/main)" HEAD || skip "contains main commits newer than the baseline"
g merge -q --no-edit "pr/$p" >/dev/null 2>&1
u=$(g diff --name-only --diff-filter=U)
if echo "$u" | grep -Eqv -e "$NONCLI|^$"; then skip "code conflict with main"; fi
if [ -n "$u" ]; then g checkout -q --ours -- $u && g add $u && g commit -q --no-edit || skip "could not take main's side of a docs conflict"; fi
g merge-base --is-ancestor "pr/$p" HEAD || skip "merge failed, not benched"
# taking main's side of a Cargo.toml can leave the merged Cargo.lock stale
fetch "$W/wc" >/dev/null 2>&1 || { fetch "$W/wc" rw && g commit -qam 'bench: refresh Cargo.lock'; } || skip "dependencies don't resolve once merged"
"$S/score.sh" "$W/wc" "$D"; rc=$?
[ $rc = 2 ] && skip "bench failed: doesn't build once merged with main"
[ $rc = 0 ] || exit 1
meta "$D" name="v66-pr$p" pr="$p" pr_head="$head" base="$base" commit="$(g rev-parse HEAD)" status=ok

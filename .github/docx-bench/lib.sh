# Shared by the bench scripts (sourced). Every container runs as the runner's user with no capabilities; the
# ones that build or run PR code also have no network, so they can't reach the runner's tokens or the internet.
# Cargo's home (registry and git checkouts) and the target dirs live under ~/c, which actions/cache keeps.
W=${GITHUB_WORKSPACE:?}; S=$W/.github/docx-bench
mkdir -p ~/c/cargo ~/c/wc-target ~/c/dx-target
U=(--user "$(id -u):$(id -g)" -e HOME=/tmp -e CARGO_HOME=/cargo -v "$HOME/c/cargo:/cargo" --cap-drop=ALL --security-opt=no-new-privileges)
OFF=(--network=none --pids-limit=8192 -e CARGO_NET_OFFLINE=true)
NONCLI='\.(md|tsv)$|^(docs|contributors|crates/ui-egui|apps/wordcraft|apps/wordcraft-web|\.github|packaging)/|tests\.rs$|/tests/|^NOTICE$'
# no hooks: the tree holds PR files, and git must never run anything from it
g() { git -C "$W/wc" -c core.hooksPath=/dev/null -c user.name=bench -c user.email=bench@localhost -c commit.gpgsign=false "$@"; }
# fetch what a tree needs with network but without running its code (gate.py refuses .cargo/ config)
fetch() { docker run --rm "${U[@]}" -v "$1:/src" -w /src docx-build bash -c 'cargo metadata -q --format-version 1 >/dev/null && cargo fetch -q'; }
# meta <run dir> key=value...: the run's meta.json (collect.py validates it)
meta() { local d=$1; shift; mkdir -p "$d"; python3 -c 'import json,sys,time; m=dict(a.split("=",1) for a in sys.argv[2:]); m["date"]=str(int(time.time())); json.dump(m,open(sys.argv[1]+"/meta.json","w"))' "$d" "$@"; }

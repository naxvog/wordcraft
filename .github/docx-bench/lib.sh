# Shared by the bench scripts (sourced). Every container runs as the runner's user with no capabilities. Cargo's home
# (~/c/cargo) is written only by `cargo fetch`, which runs no code from the tree; containers that build or run PR
# code see it read-only and have no network, so they can't reach the runner's tokens, the cache or the internet.
W=${GITHUB_WORKSPACE:?}; S=$W/.github/docx-bench
mkdir -p ~/c/cargo ~/c/wc-target ~/c/dx-target
USR=(--user "$(id -u):$(id -g)" -e HOME=/tmp -e CARGO_HOME=/cargo --cap-drop=ALL --security-opt=no-new-privileges)
OFF=(--network=none --pids-limit=8192 -e CARGO_NET_OFFLINE=true -v "$HOME/c/cargo:/cargo:ro")
NONCLI='\.(md|tsv)$|^(docs|contributors|crates/ui-egui|apps/wordcraft|apps/wordcraft-web|\.github|packaging)/|tests\.rs$|/tests/|^NOTICE$'
# the tree holds PR files: git must never run anything from it (hooks, fsmonitor) or follow its LFS config
export GIT_LFS_SKIP_SMUDGE=1
g() { git -C "$W/wc" -c core.hooksPath=/dev/null -c core.fsmonitor=false -c user.name=bench -c user.email=bench@localhost -c commit.gpgsign=false "$@"; }
# <tree> [rw]: fetch the tree's dependencies with network but without running its code. Run from /tmp, cargo and
# rustup don't see the tree's .cargo/config or toolchain file (both could name a program from the PR to run here),
# and RUSTUP_TOOLCHAIN/RUSTC/RUSTC_WRAPPER pin what runs anyway. rw lets cargo update a stale Cargo.lock.
fetch() { local m=ro lk=--locked; [ "${2:-}" = rw ] && m=rw lk=
  docker run --rm "${USR[@]}" -v "$HOME/c/cargo:/cargo" -v "$1:/src:$m" -w /tmp \
    -e RUSTUP_TOOLCHAIN=1.99.0 -e RUSTC=/opt/cargo/bin/rustc -e RUSTC_WRAPPER= docx-bench \
    bash -c "cargo metadata -q $lk --format-version 1 --manifest-path /src/Cargo.toml >/dev/null && cargo fetch -q --manifest-path /src/Cargo.toml"; }
# meta <run dir> key=value...: the run's meta.json (collect.py validates it)
meta() { local d=$1; shift; mkdir -p "$d"; python3 -c 'import json,sys,time; m=dict(a.split("=",1) for a in sys.argv[2:]); m["date"]=str(int(time.time())); json.dump(m,open(sys.argv[1]+"/meta.json","w"))' "$d" "$@"; }

"""usage: scan.py [--all] [--top N]
Refreshes the PR list from GitHub and decides what the next bench round reruns. Writes:
  <VER>-prs.json     every candidate PR (touches a layout/rendering/reading crate): title, author, author_association,
                     head, draft, conflicts with main (code, or only docs = main_side), render (changes a file that can
                     move the score), risky (reasons a person must look first), allowed (allow.txt covers its head),
                     stale (reasons its run no longer reflects the PR on today's main)
  <VER>-removed.json PRs that left the list (merged or closed)
  <VER>-todo.txt     PRs to bench now: benchable and gated through, and never benched, or with new commits, or stale
                     against main while their run changed fixtures
--all also benches PRs that change no rendering file (a safety net for the RENDER filter, once per suite version)."""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # run with -I, which leaves the script's dir out
from benchlib import B, GH, VER, REPO, NONCLI, TRUSTED, git, render_files, risky, allowed, stale, load, delta, run_base

ALL = '--all' in sys.argv
CORE = ('crates/layout/', 'crates/render/', 'crates/pdf/', 'crates/fonts/src/', 'crates/docx/src/', 'crates/doc/src/',
        'crates/metafile/', 'crates/geom/')
UI = re.compile(r'(?i)\b(ui|ribbon|dialog|caret|cursor|selection|click|drag|scroll|keyboard|shortcut|hover|tooltip|menu|pane|'
                r'screen reader|accessib|ime|typing|backspace|undo|ruler|zoom|android|windows|macos|linux|web|wasm|mcp|perf|'
                r'speed|faster|cache|memory|panic|crash|overflow|hostile|bound|limit|refuse|cap )')
GOOD = re.compile(r'(?i)(layout|table|font|docx|render|pdf|picture|image|border|list|number|text box|shape|metafile|wmf|emf|'
                  r'hyphen|equation|field|footnote|endnote|header|footer|section|column|spacing|indent|tab|wrap|float|chart|'
                  r'smartart|wordart|shading|underline|line break|justif|kerning|east asian|cjk|rtl|bidi|arabic|thai|page|vml|'
                  r'drawing|text|line)')


def code(f):
    return not f.endswith('tests.rs') and '/tests' not in f


def gh(*a):
    return subprocess.run(['gh', *a], capture_output=True, text=True, check=True).stdout


subprocess.run(['git', '-C', REPO, 'fetch', '-q', 'origin', 'main'], check=True)
P = json.loads(gh('pr', 'list', '-R', GH, '--state', 'open', '--limit', '3000',
                  '--json', 'number,title,author,isDraft,headRefOid,files'))
assoc = dict(l.split() for l in gh('api', '--paginate', f'repos/{GH}/pulls?state=open&per_page=100',
                                   '--jq', '.[] | "\\(.number) \\(.author_association)"').splitlines())
cand = [p for p in P if any(f['path'].startswith(CORE) and code(f['path']) for f in p['files'])
        or (any(f['path'].startswith('crates/engine/src/') and code(f['path']) for f in p['files'])
            and GOOD.search(p['title']) and not UI.search(p['title']))]

old_path = f'{B}/{VER}-prs.json'
old = {q['n']: q for q in json.load(open(old_path))} if os.path.exists(old_path) else {}
open_n = {p['number'] for p in P}
rem_path = f'{B}/{VER}-removed.json'
removed = json.load(open(rem_path)) if os.path.exists(rem_path) else []
gone = [n for n in old if n not in open_n and n not in {r['n'] for r in removed}]
for n in gone:
    removed.append(dict(n=n, title=old[n]['title'], state=gh('pr', 'view', str(n), '-R', GH, '--json', 'state', '-q', '.state').strip()))

refetch = [p['number'] for p in cand if git('rev-parse', '-q', '--verify', f"pr/{p['number']}").strip() != p['headRefOid']]
for i in range(0, len(refetch), 100):
    subprocess.run(['git', '-C', REPO, 'fetch', '-q', '-f', 'origin',
                    *[f'+pull/{n}/head:refs/heads/pr/{n}' for n in refetch[i:i + 100]]], check=True)

Q, todo = [], []
for p in cand:
    n, head = p['number'], p['headRefOid']
    out = git('merge-tree', '--write-tree', '--name-only', '--no-messages', 'origin/main', f'pr/{n}').splitlines()[1:]
    conf = [f for f in out if f and not f.endswith('.md')]
    q = dict(n=n, title=p['title'], author=p['author']['login'], assoc=assoc.get(str(n), 'NONE'), draft=p['isDraft'],
             head=head, mine=p['author']['login'] == 'naxvog',
             conflicts=[f for f in conf if not NONCLI.search(f)], main_side=[f for f in conf if NONCLI.search(f)],
             render=bool(render_files([f['path'] for f in p['files']])), risky=risky(n), allowed=allowed(n, head))
    run = load(f'{VER}-pr{n}')
    q['stale'] = stale(n, head) if run else []
    gated = (q['assoc'] in TRUSTED and not q['risky']) or q['allowed']
    if not q['draft'] and not q['conflicts'] and (q['render'] or ALL) and gated:
        if not run or 'new commits' in q['stale']:
            todo.append(q)
        elif q['stale'] and delta(load(run_base(f'{VER}-pr{n}')), run)['changed']:
            todo.append(q)
    Q.append(q)
Q.sort(key=lambda q: (not q['mine'], q['n']))
todo.sort(key=lambda q: (not q['mine'], q['n']))

for path, data in ((old_path, Q), (rem_path, removed)):
    json.dump(data, open(path + '.new', 'w'), indent=0)
    os.replace(path + '.new', path)
open(f'{B}/{VER}-todo.txt', 'w').write(''.join(f"{q['n']}\n" for q in todo))
ok = [q for q in Q if not q['draft'] and not q['conflicts']]
print(f"{len(Q)} candidates; {len(gone)} left the list; {len(ok)} merge with main, of which "
      f"{sum(not q['render'] for q in ok)} change no rendering file, "
      f"{sum(q['assoc'] not in TRUSTED and not q['allowed'] for q in ok)} from untrusted authors, "
      f"{sum(bool(q['risky']) and not q['allowed'] for q in ok)} risky, "
      f"{sum(bool(q['stale']) for q in ok)} stale; {len(todo)} to bench")

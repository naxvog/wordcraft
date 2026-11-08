"""Prints the tracking issue's body (Markdown): a summary for reviewers first (what to merge next, what needs a look,
what needs a rebase), then the method, every benched PR, the combined branches and what isn't benched. Reads the
runs (runs/<VER>-pr<n>, each against the baseline in its `base` file), <VER>-prs.json from scan.py, the combined
runs and <VER>-notes.md. Asks GitHub for CI, review state and size of the PRs in the summary."""
import datetime, json, os, re, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # run with -I, which leaves the script's dir out
from benchlib import B, GH, VER, TRUSTED, load, means, delta, run_base, run_date, pr_head, current_base

FORK = 'https://github.com/naxvog/docxide-pdf/tree/wordcraft-comparison'
GIST = 'https://gist.github.com/naxvog/54e2039e999cdeacfc0ed59b8da3c6e6'
DROP = 5.0  # a fixture losing more SSIM points than this puts the PR under "Needs a look"

prs = json.load(open(f'{B}/{VER}-prs.json'))
base_run = current_base()
MAIN = base_run.split('-')[-1]
base = load(base_run)
bm, dm = means(base), means(base, 'docxide')
bases = {base_run: base}


def short(n):
    return n.split('/', 1)[-1]


def fx(lst, k=3):
    s = ', '.join(f'{short(n)} {x:+.1f}' for x, n in lst[:k])
    return s + (f' (+{len(lst) - k} more)' if len(lst) > k else '')


def md(s):
    """PR titles and logins are the PR author's text: no table breaks, mentions, links, images or HTML."""
    return re.sub(r'([\\`*_\[\]<>!|~&])', r'\\\1', s).replace('@', '@\u200b')


def age(run):
    d = (time.time() - run_date(run)) / 86400
    return 'today' if d < 1 else f'{d:.0f} d ago'


measured, nochange = [], []
for q in prs:
    run = load(f"{VER}-pr{q['n']}")
    if not run or q['draft']:
        continue
    if pr_head(q['n']) == q['head'] and run_base(f"{VER}-pr{q['n']}") == base_run:
        q['stale'] = []  # benched after scan.py looked: on today's baseline at today's head
    bn = run_base(f"{VER}-pr{q['n']}")
    if bn not in bases:
        bases[bn] = load(bn)
    d = delta(bases[bn], run)
    d['base'] = bn.split('-')[-1]
    d['age'] = age(f"{VER}-pr{q['n']}")
    (measured if d['changed'] or abs(d['ssim']) > 0.0005 else nochange).append((q, d))
measured.sort(key=lambda x: -x[1]['ssim'])
by_n = {str(q['n']): (q, d) for q, d in measured}
ok = [q for q in prs if not q['draft'] and not q['conflicts']]
gated = [q for q in ok if not q['allowed'] and (q['assoc'] not in TRUSTED or q['risky'])]
norender = [q for q in ok if not q['render'] and not load(f"{VER}-pr{q['n']}")]
conflicting = [q for q in prs if q['conflicts'] and not q['draft']]
done = {str(q['n']) for q, _ in measured + nochange}
failed = sorted({l.split(':')[0] for l in open(f'{B}/{VER}-summary.tsv') if ': bench failed' in l} - done)
todo = [l.strip() for l in open(f'{B}/{VER}-todo.txt') if l.strip()] if os.path.exists(f'{B}/{VER}-todo.txt') else []
_rm = json.load(open(f'{B}/{VER}-removed.json')) if os.path.exists(f'{B}/{VER}-removed.json') else []
removed_txt = '; '.join(f"{lab} {', '.join('#' + str(r['n']) for r in _rm if r['state'] == s)}"
                        for s, lab in (('MERGED', 'merged'), ('CLOSED', 'closed without merging'))
                        if any(r['state'] == s for r in _rm)) or 'none'


def lst(name, f):
    p = f'{B}/runs/{name}/{f}'
    return open(p).read().split() if os.path.exists(p) else []


# --- summary: merge next = the combined branch without known bad interactions, in its merge order
# the combined run behind "Merge next": the one without known bad interactions, if it was measured on today's baseline
# and merged something; otherwise the list falls back to the measured PRs and claims no combined total
cur = [r for r in (f'{VER}-combined-excl', f'{VER}-combined') if load(r) and run_base(r) == base_run and lst(r, 'merged')]
excl_run = cur[0] if cur else None
excl = lst(excl_run, 'excluded') if excl_run else []
order = [n for n in lst(excl_run, 'merged') if n in by_n and by_n[n][1]['ssim'] > 0.0005] if excl_run else []
if not order:
    order = [str(q['n']) for q, d in measured if d['ssim'] > 0.0005 and not q['conflicts']]
# positive and mergeable, but not in the combined branch (rebased or new since it was built)
# (PRs that clash with the ones above are explained under *Combined branch* instead)
clash = lst(excl_run, 'conflicts_prs') + lst(excl_run, 'broken') + lst(excl_run, 'gated')
later = [str(q['n']) for q, d in measured if d['ssim'] > 0.0005 and not q['conflicts'] and str(q['n']) not in order + excl + clash]
rebase = [(q, d) for q, d in measured if d['ssim'] > 0.0005 and q['conflicts']]
look = [(q, d) for q, d in measured if str(q['n']) in order and d['down'] and d['down'][0][0] < -DROP]


def gh_info(ns):
    """CI, review decision and size per PR, in one GraphQL call."""
    if not ns:
        return {}
    fields = 'reviewDecision additions deletions commits(last:1){nodes{commit{statusCheckRollup{state}}}}'
    qry = 'query{repository(owner:"%s",name:"%s"){%s}}' % (*GH.split('/'), ' '.join(f'p{n}:pullRequest(number:{n}){{{fields}}}' for n in ns))
    r = subprocess.run(['gh', 'api', 'graphql', '-f', f'query={qry}'], capture_output=True, text=True)
    data = json.loads(r.stdout or '{}').get('data', {}).get('repository') or {}
    out = {}
    for n in ns:
        p = data.get(f'p{n}') or {}
        nodes = (p.get('commits') or {}).get('nodes') or [{}]
        ci = ((nodes[0].get('commit') or {}).get('statusCheckRollup') or {}).get('state')
        out[n] = dict(ci={'SUCCESS': '✅', 'FAILURE': '❌', 'ERROR': '❌', 'PENDING': '⏳', 'EXPECTED': '⏳'}.get(ci, '–'),
                      review={'APPROVED': 'approved', 'CHANGES_REQUESTED': 'changes requested'}.get(p.get('reviewDecision'), '–'),
                      size=f"+{p.get('additions', '?')} −{p.get('deletions', '?')}")
    return out


info = gh_info(order + later + [str(q['n']) for q, _ in rebase])


def when(q, d):
    s = f"`{d['base']}`, {d['age']}"
    return s + (f" ⚠ stale: {'; '.join(q['stale'])}" if q['stale'] else '')


def srow(n, mark=''):
    q, d = by_n[n]
    i = info.get(n, {})
    worst = f"{short(d['down'][0][1])} {d['down'][0][0]:+.1f}" if d['down'] else '–'
    return (f"| #{n}{mark} | {md(q['author'])} | {md(q['title'])} | **{d['ssim']:+.3f}** | {len(d['up'])}↑ {len(d['down'])}↓ | "
            f"{worst} | {i.get('ci', '–')} | {i.get('review', '–')} | {i.get('size', '')} | {when(q, d)} |")


SHEAD = ('| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Measured on `main` |\n'
         '|---|---|---|---|---|---|---|---|---|---|')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
cd = delta(base, load(excl_run)) if excl_run else None
gap = dm['ssim'] - bm['ssim']
out = [f"""This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated {now}.

## Summary for reviewers

`main` {MAIN} scores **{bm['ssim']:.2f}** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores {dm['ssim']:.2f}
({gap:.1f} points ahead)."""
       + (f""" Merging the {len(order)} PRs below, in this order, gives **{bm['ssim'] + cd['ssim']:.2f} ({cd['ssim']:+.2f})**,
measured on one branch with all of them merged (see *Combined branch*)."""
          if cd else '') + f"""

### Merge next

Ranked by what each adds on its own; they merge cleanly with `main` and with each other in this order. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

{SHEAD}"""]
out += [srow(n) for n in order] + [srow(n, ' †') for n in later] or ['| – | | nothing yet | | | | | | | |']
if later:
    out.append('\n† Not in the combined branch yet (rebased or benched since it was built), so not in its total either.')
looks = [f"- **#{q['n']}** ({md(q['author'])}): {fx(d['down'], 4)}" for q, d in look]
if os.path.exists(f'{B}/{VER}-notes.md'):
    looks.append('- ' + open(f'{B}/{VER}-notes.md').read().strip().replace('\n', ' '))
if excl:
    looks.append(f"- Left out of *Merge next* on purpose: {', '.join('#' + n for n in excl)} (see *Combined branch*).")
out.append(f"""
### Needs a look

PRs above that also make a fixture worse by more than {DROP:.0f} SSIM points, and interactions between PRs:

""" + ('\n'.join(looks) or '- nothing'))
if rebase:
    out.append(f"""
### Would help, needs a rebase

These raised the score when they were benched, but now conflict with `main` in code.

{SHEAD}""")
    out += [srow(str(q['n'])) for q, _ in rebase]
n_stale = sum(bool(q['stale']) for q, _ in measured + nochange)
out.append(f"""
**Coverage:** {len(done)} PRs benched ({len(measured)} change the score), {n_stale} of them stale; {len(todo)} queued for the
next round; {len(gated)} waiting for a person to look before they're built; {len(conflicting)} conflict with `main`.

<details><summary><b>How it's measured</b></summary>

- **Suite:** docxide-pdf's fixtures ({bm['n']} DOCX files with Word's own PDF export as the reference: handcrafted
  `cases/`, `hyphenation/` and real-world `scraped/` documents). The WordCraft harness is an opt-in suite module on
  the fork branch [{FORK.split('/', 3)[3]}]({FORK}) (`tests/suite/wordcraft_comparison.rs`):
  `WORDCRAFT_CLI=<wordcraft-cli> cargo test --release --test suite wordcraft_comparison -- --nocapture`.
  It converts every fixture with `wordcraft-cli convert`, rasterises at 150 dpi with mutool and scores each page
  with the suite's own Jaccard (ink overlap) and SSIM.
- **Line match:** [textcmp.py]({GIST}) compares the text lines of both PDFs.
- **Scores** are means over all fixtures, strict: a page WordCraft doesn't produce counts as 0. Deltas are in
  percentage points of that mean, so a fix that perfects one fixture moves it by at most ~0.1.
- **Per PR:** the PR is merged into the round's baseline (`main` at the start of the round) and the whole suite is
  rerun; its delta is against that baseline. Conflicts in files `wordcraft-cli` doesn't build (documentation,
  translation catalogs, the UI crate, the desktop and web apps, tests) take main's side, which can't change a PDF;
  PRs with conflicts in anything else are not benched. A fixture counts as changed at ±0.1 SSIM points; gains and
  regressions list fixtures that moved by more than 0.5.
- **Rounds:** a new baseline whenever `main` moves; a PR is rerun when it gets new commits, or when its result
  changed fixtures and `main` has since changed a rendering file it changes too. PRs that change no file in
  `crates/{{docx,layout,render,pdf,fonts}}/src` aren't benched (in 321 runs, none of them changed a fixture).
- **Safety:** PR code is built and run in containers without network or capabilities, with their own cargo caches,
  seeing the suite read-only. PRs from authors without a merged PR, and PRs that add build scripts, proc macros,
  cargo config or dependencies, wait until someone has read the diff.
- **Environment:** Linux container, debug build of `wordcraft-cli` (the layout code is the same as release), fonts
  from Debian packages plus Microsoft's core web fonts. Calibri, Cambria, Aptos and the other Office fonts are
  not installed, so WordCraft draws those documents in metric-compatible substitutes (Carlito, Caladea, …) while
  Word's references use the originals. docxide-pdf runs in the same container without its private font set.

| `main` {MAIN} | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| WordCraft | {bm['ssim']:.2f} | {bm['j']:.2f} | {bm['pages']}/{bm['n']} | {bm['lines']:.1f} |
| docxide-pdf (for reference) | {dm['ssim']:.2f} | {dm['j']:.2f} | {dm['pages']}/{dm['n']} | {dm['lines']:.1f} |

</details>

<details><summary><b>Every PR that changes the score ({len(measured)})</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Measured on `main` |
|---|---|---|---|---|---|---|---|---|---|""")
out += [f"| #{q['n']} | {md(q['author'])} | {md(q['title'])} | {d['ssim']:+.3f} | {d['j']:+.3f} | {d['pages']:+d} | "
        f"{d['changed']} ({len(d['up'])}↑ {len(d['down'])}↓) | {fx(d['up']) or '–'} | {fx(d['down']) or '–'} | {when(q, d)} |"
        for q, d in measured]
out.append(f"""
**Benched, no change on the suite ({len(nochange)}):** {', '.join(f"#{q['n']}" for q, _ in nochange) or '–'}. These may
still be right; the suite just has no document that exercises them.

</details>""")


def comb_block(name, label):
    c = load(name)
    if not c:
        return None
    bn = run_base(name)
    cb = bases.setdefault(bn, load(bn))
    d, cm, b0 = delta(cb, c), means(c), means(cb)
    mlist = lst(name, 'merged')
    summed = sum(by_n[n][1]['ssim'] for n in mlist if n in by_n)
    left = [f"{why}: {', '.join('#' + n for n in lst(name, f))}" for f, why in (
        ('conflicts_main', 'code conflict with `main`'), ('conflicts_prs', 'code conflict with PRs merged before it'),
        ('broken', "doesn't compile with the PRs merged before it"), ('gated', 'waiting for a look before it is built'),
        ('excluded', 'left out on purpose')) if lst(name, f)]
    return f"""**{label}**: {len(mlist)} PRs merged into `main` {bn.split('-')[-1]}: {', '.join('#' + n for n in mlist)}.{(' Left out: ' + '; '.join(left) + '.') if left else ''}

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` {bn.split('-')[-1]} | {b0['ssim']:.2f} | {b0['j']:.2f} | {b0['pages']}/{b0['n']} | {b0['lines']:.1f} |
| combined | {cm['ssim']:.2f} ({d['ssim']:+.3f}) | {cm['j']:.2f} ({d['j']:+.3f}) | {cm['pages']}/{cm['n']} ({d['pages']:+d}) | {cm['lines']:.1f} ({d['lines']:+.2f}) |

The merged PRs' individual SSIM changes add up to {summed:+.3f}; the difference to the combined {d['ssim']:+.3f} is where
they overlap or interact. {d['changed']} fixtures change ({len(d['up'])}↑ {len(d['down'])}↓). Regressions over 0.5: {fx(d['down'], 8) or 'none'}."""


blocks = [b for b in (comb_block(f'{VER}-combined', 'Every PR with a positive score'),
                      comb_block(f'{VER}-combined-excl', 'The same without ' + ', '.join('#' + n for n in excl)) if excl else None) if b]
out.append(f"""
## Combined branch

""" + ('\n\n'.join(blocks) or 'Pending: every PR with a positive score merged together and benched the same way.') + f"""

## Not benched

- **Code conflicts with `main`** ({len(conflicting)} PRs): not rerun until rebased.
- **Waiting for a look before they're built** ({len(gated)}): {', '.join(f"#{q['n']}" for q in gated if q['risky']) or 'none'} change
  build scripts, cargo config or dependencies; {sum(not q['risky'] for q in gated)} more are from authors without a merged PR yet.
- **Change no rendering file** ({len(norender)}): not benched.
- **Doesn't build once merged with `main`:** {', '.join('#' + n for n in failed) or '–'}.
- **Removed from this list** since they're no longer open: {removed_txt}.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).
""")
print('\n'.join(out))

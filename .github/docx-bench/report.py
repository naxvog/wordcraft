"""usage: report.py <previous baseline run> <run>...   (BENCH_STATE: a bench-results checkout after the round)
Prints what changed in a round, for the person who started it: the baseline and whether it moved, both combined
totals, every run of this round (PR runs with SSIM change, fixtures changed and drops over 5 points; the user's
own PRs first), the PRs the gate holds back (counted by reason) and the queue left. PRs that failed or were
skipped are the lines this round added to <VER>-summary.tsv."""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # run with -I, which leaves the script's dir out
from benchlib import B, VER, TRUSTED, load, means, delta, run_base, current_base

prev, runs = sys.argv[1], sys.argv[2:]
base = current_base()
bm = means(load(base))
print(f"Baseline {base.split('-')[-1]}: SSIM {bm['ssim']:.2f}" + (' (unchanged)' if base == prev else f" (new; was {prev.split('-')[-1]})"))
for c in (f'{VER}-combined-excl', f'{VER}-combined'):
    if (r := load(c)) and run_base(c) == base:
        merged = open(f'{B}/runs/{c}/merged').read().split()
        print(f"{c}: {means(r)['ssim']:.2f} ({delta(load(base), r)['ssim']:+.2f}), {len(merged)} PRs merged")

prs = {str(q['n']): q for q in json.load(open(f'{B}/{VER}-prs.json'))}
rows = []
for r in runs:
    if r.startswith(f'{VER}-pr') and (run := load(r)):
        n = r[len(VER) + 3:]
        q = prs.get(n, {})
        d = delta(load(run_base(r)), run)
        drops = ', '.join(f'{f.split("/")[-1]} {x:+.1f}' for x, f in d['down'] if x < -5) or '–'
        rows.append((not q.get('mine'), -d['ssim'], f"#{n} {q.get('author', '?')}: {d['ssim']:+.3f}, {d['changed']} fixtures changed, drops >5: {drops}"))
print(f'PRs benched this round ({len(rows)}):')
print('\n'.join('  ' + t for *_, t in sorted(rows)) or '  none')

# held = what scan.py keeps out of the queue: benchable, but the gate doesn't let it through
def kind(why):
    for key, label in (('Cargo.toml', 'changes a Cargo.toml'), ('Cargo.lock', 'new packages in Cargo.lock'), ('build.rs', 'a build script'),
                       ('xtask/', 'xtask'), ('.cargo/', 'cargo config'), ('rust-toolchain', 'toolchain file')):
        if key in why:
            return label
    return why


held = [q for q in prs.values() if not (q['draft'] or q['conflicts'] or not q['render'] or q['allowed'])
        and (q['assoc'] not in TRUSTED or q['risky'])]
why = collections.Counter(k for q in held for k in {kind(w) for w in q['risky']} | ({'author without a merged PR'} if q['assoc'] not in TRUSTED else set()))
print(f'Held by the gate: {len(held)} PRs (' + ', '.join(f'{w}: {c}' for w, c in why.most_common()) + ')')
todo = [l for l in open(f'{B}/{VER}-todo.txt') if l.strip()]
print(f'Still queued: {len(todo)}')

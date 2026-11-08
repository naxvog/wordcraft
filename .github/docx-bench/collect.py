"""usage: collect.py <artifacts dir> <fixtures dir>
Installs this round's runs (one directory per run: meta.json plus the compact JSON from compact.py) into
$BENCH_STATE/runs. The files come from jobs that ran PR code, so only what is expected gets through: known run
names and fixture names, scores in [0, 1], plain counts, commit hashes and PR numbers. A run whose status isn't ok
only adds a line to <VER>-summary.tsv; a run that fails a check is dropped."""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # run with -I, which leaves the script's dir out
from benchlib import B, VER

art, fx = sys.argv[1:]
known = {f'{g}/{c}' for g in os.listdir(fx) if os.path.isdir(f'{fx}/{g}') for c in os.listdir(f'{fx}/{g}')}
NAME = re.compile(rf'^{VER}-(main-[0-9a-f]{{9}}|pr[0-9]{{1,6}}|combined(-excl)?)$')
SHA = re.compile(r'^[0-9a-f]{40}$')
PRS = re.compile(r'^[0-9]{1,6}( [0-9]{1,6})*$|^$')


def score(x):
    return x is None or (type(x) in (int, float) and 0 <= x <= 1)


def count(x):
    return x is None or (type(x) is int and 0 <= x <= 100000)


def rows(R, T):
    assert len({r['name'] for r in R}) == len(R) > 0
    for r in R:
        assert set(r) == {'name', 'group', 'ref_pages', 'wordcraft', 'docxide'} and r['name'] in known
        assert r['group'] == r['name'].split('/')[0] and count(r['ref_pages'])
        for e in ('wordcraft', 'docxide'):
            v = r[e]
            assert set(v) == {'ssim_strict', 'jaccard_strict', 'pages'}
            assert score(v['ssim_strict']) and score(v['jaccard_strict']) and count(v['pages'])
    for t in T:
        assert set(t) <= {'name', 'wordcraft', 'docxide'} and t['name'] in known
        assert all(set(t[e]) == {'line_match'} and score(t[e]['line_match']) for e in ('wordcraft', 'docxide') if e in t)


done = []
for a in sorted(os.listdir(art)):
    d = f'{art}/{a}'
    try:
        m = json.load(open(f'{d}/meta.json'))
        assert type(m) is dict and all(type(v) is str for v in m.values())
        assert NAME.match(m['name']) and a == 'run-' + m['name'] and m['date'].isdigit()
        assert all(SHA.match(m[k]) for k in ('commit', 'pr_head') if k in m) and NAME.match(m.get('base', m['name']))
        assert all(PRS.match(m[k]) for k in ('pr', 'merged', 'conflicts_main', 'conflicts_prs', 'broken', 'gated', 'excluded') if k in m)
        if m['status'] != 'ok':
            with open(f'{B}/{VER}-summary.tsv', 'a') as f:  # the reason is our own text (pr.sh), cut to one line
                f.write(f"{m.get('pr', m['name'])}: {m['status'][:200].splitlines()[0]}\n")
            print(f"{a}: {m['status'][:200]}")
            continue
        R, T = json.load(open(f'{d}/wordcraft_comparison.json')), json.load(open(f'{d}/textcmp.json'))
        rows(R, T)
    except (AssertionError, KeyError, ValueError, TypeError, AttributeError, IndexError, OSError) as e:
        print(f'{a}: rejected ({type(e).__name__} {e})')
        continue
    out = f"{B}/runs/{m['name']}"
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    json.dump(R, open(f'{out}/wordcraft_comparison.json', 'w'), separators=(',', ':'))
    json.dump(T, open(f'{out}/textcmp.json', 'w'), separators=(',', ':'))
    for k in ('commit', 'pr_head', 'base', 'date', 'merged', 'conflicts_main', 'conflicts_prs', 'broken', 'gated', 'excluded'):
        if k in m:
            open(f'{out}/{k}', 'w').write(m[k] + '\n')
    done.append(m['name'])
print(f'installed {len(done)}: {" ".join(done)}')

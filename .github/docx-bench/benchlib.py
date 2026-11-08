"""Shared by scan.py, gate.py and issue.py: paths, file classes, the safety checks and the score maths."""
import functools, json, os, re, statistics as st, subprocess

# BENCH_STATE: the runs and state files (the bench-results branch in Actions); BENCH_REPO: a storytold/wordcraft clone
B = os.environ.get('BENCH_STATE') or os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get('BENCH_REPO') or '/home/naxvog/Projects/wordcraft'
GH = 'storytold/wordcraft'
VER = 'v66'
# Files whose change can move the docxide score. In the 321 runs of the v66 round, no PR that changed none of
# them changed a single fixture (97 runs would have been skipped). scan.py --all benches the rest too.
RENDER = re.compile(r'^crates/(docx|layout|render|pdf|fonts)/src/')
TESTS = re.compile(r'(^|/)tests?(\.rs$|/)')
# conflicts in these take main's side in a bench merge: wordcraft-cli doesn't build them
NONCLI = re.compile(r'\.(md|tsv)$|^(docs|contributors|crates/ui-egui|apps/wordcraft|apps/wordcraft-web|\.github|packaging)/'
                    r'|tests\.rs$|/tests/|^NOTICE$')
# code that runs while building, or config that changes what cargo fetches or runs: a person looks first (allow.txt)
RISKY = re.compile(r'(^|/)build\.rs$|^\.cargo/|(^|/)rust-toolchain(\.toml)?$|^xtask/')
TRUSTED = {'OWNER', 'MEMBER', 'COLLABORATOR', 'CONTRIBUTOR'}  # GitHub: CONTRIBUTOR = has had a PR merged


def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True).stdout


@functools.lru_cache(None)
def names(a, b):
    return tuple(git('diff', '--name-only', a, b).split())


@functools.lru_cache(None)
def main_packages():
    return set(re.findall(r'^name = "([^"]+)"', git('show', 'origin/main:Cargo.lock'), re.M))


def render_files(files):
    return [f for f in files if RENDER.match(f) and not TESTS.search(f)]


def crates(files):
    return {f.split('/')[1] for f in files}


def pr_files(n, upto='origin/main'):
    """Files PR n changes against its merge base with `upto`."""
    mb = git('merge-base', f'pr/{n}', upto).strip()
    return git('diff', '--name-only', mb, f'pr/{n}').split() if mb else []


def risky(n):
    """Why PR n needs a person's look before it is built, from its fetched head (empty if nothing)."""
    mb = git('merge-base', f'pr/{n}', 'origin/main').strip()
    if not mb:
        return ['no merge base with main']
    files = git('diff', '--name-only', mb, f'pr/{n}').split()
    why = [f for f in files if RISKY.search(f)]
    tomls = [f for f in files if f.endswith('Cargo.toml')]
    if tomls and re.search(r'^\+\s*proc-macro\s*=\s*true', git('diff', mb, f'pr/{n}', '--', *tomls), re.M):
        why.append('new proc-macro crate')
    if 'Cargo.lock' in files:
        new = sorted(set(re.findall(r'^\+name = "([^"]+)"', git('diff', mb, f'pr/{n}', '--', 'Cargo.lock'), re.M)) - main_packages())
        if new:
            why.append('new dependencies: ' + ', '.join(new))
    return why


def allowed(n, head):
    """allow.txt: '<pr> <head sha prefix>  # who looked and why', one per line. Bound to the head that was read."""
    p = f'{B}/allow.txt'
    if not os.path.exists(p):
        return False
    for l in open(p):
        w = l.split('#')[0].split()
        if len(w) >= 2 and w[0] == str(n) and head.startswith(w[1]):
            return True
    return False


def current_base():
    return open(f'{B}/current-main').read().strip()


def run_base(run):
    p = f'{B}/runs/{run}/base'
    return open(p).read().strip() if os.path.exists(p) else f'{VER}-main-e919982fa'


def run_commit(run):
    p = f'{B}/runs/{run}/commit'
    return open(p).read().strip() if os.path.exists(p) else None


def run_date(run):
    """When the run was benched: its `date` file (git checkouts don't keep mtimes), else the file's mtime."""
    p = f'{B}/runs/{run}/date'
    if os.path.exists(p):
        return float(open(p).read().strip())
    return os.path.getmtime(f'{B}/runs/{run}/wordcraft_comparison.json')


def pr_head(n):
    p = f'{B}/runs/{VER}-pr{n}/pr_head'
    return open(p).read().strip() if os.path.exists(p) else None


def stale(n, head, main='origin/main'):
    """Why PR n's run no longer reflects the PR on today's main (empty if it still does)."""
    run = f'{VER}-pr{n}'
    why = []
    ph = pr_head(n)
    if ph and head and not ph.startswith(head[:9]):
        why.append('new commits')
    bc = run_commit(run_base(run))
    if bc:
        # file level: main touches crates/layout almost daily, so a crate-level test would rerun every PR every day
        both = sorted(set(render_files(names(bc, main))) & set(render_files(pr_files(n))))
        if both:
            why.append('main changed ' + ', '.join(f.split('/src/')[-1] for f in both[:3]) + (' …' if len(both) > 3 else ''))
    return why


def load(run):
    d = f'{B}/runs/{run}'
    if not os.path.exists(d + '/wordcraft_comparison.json'):
        return None
    R = {r['name']: r for r in json.load(open(d + '/wordcraft_comparison.json')) if r['group'] != 'private'}
    T = {t['name']: t for t in json.load(open(d + '/textcmp.json'))}
    return R, T


def means(run, e='wordcraft'):
    R, T = run
    rs = list(R.values())
    lm = [T[r['name']][e]['line_match'] for r in rs if T.get(r['name'], {}).get(e)]
    return dict(ssim=st.mean((r[e]['ssim_strict'] or 0) * 100 for r in rs),
                j=st.mean((r[e]['jaccard_strict'] or 0) * 100 for r in rs),
                pages=sum(r[e]['pages'] == r['ref_pages'] for r in rs), n=len(rs),
                lines=st.mean(lm) * 100 if lm else 0.0)


def delta(base, run):
    a, b = means(base), means(run)
    Ra, Rb = base[0], run[0]
    d = {n: ((Rb[n]['wordcraft']['ssim_strict'] or 0) - (Ra[n]['wordcraft']['ssim_strict'] or 0)) * 100
         for n in Ra if n in Rb}
    return dict(ssim=b['ssim'] - a['ssim'], j=b['j'] - a['j'], pages=b['pages'] - a['pages'],
                lines=b['lines'] - a['lines'],
                changed=sum(abs(x) > 0.1 for x in d.values()),
                up=sorted(((x, n) for n, x in d.items() if x > 0.5), reverse=True),
                down=sorted((x, n) for n, x in d.items() if x < -0.5))

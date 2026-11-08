"""usage: gate.py <pr>
Exit 0 if the fetched head of pr/<n> may be built unattended: its author has had a PR merged (or is a member) and it
changes nothing that runs at build time or changes what cargo fetches (benchlib.RISKY, proc macros, new
dependencies). Otherwise prints why and exits 1. A line '<pr> <head sha prefix>' in allow.txt, added after
reading the diff, lets that exact head through."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # run with -I, which leaves the script's dir out
from benchlib import B, GH, VER, TRUSTED, git, risky, allowed

n = sys.argv[1]
head = git('rev-parse', f'pr/{n}').strip()
if allowed(n, head):
    sys.exit(0)
q = {str(q['n']): q for q in json.load(open(f'{B}/{VER}-prs.json'))}.get(n)
assoc = (q or {}).get('assoc') or subprocess.run(['gh', 'api', f'repos/{GH}/pulls/{n}', '--jq', '.author_association'],
                                            capture_output=True, text=True).stdout.strip()
why = ([f'author not yet trusted ({assoc or "unknown"})'] if assoc not in TRUSTED else []) + risky(n)
if why:
    print(f"needs a look before it's built: {'; '.join(why)} (allow.txt: {n} {head[:9]})")
    sys.exit(1)

"""usage: compact.py <harness output dir> <run dir>
Keeps what scan.py and issue.py read (per fixture: strict SSIM and Jaccard, page counts, line match) and drops
per-page arrays, timings, errors and drift: ~10x smaller, so every run fits in the bench-results branch."""
import json, os, sys

src, dst = sys.argv[1:]
os.makedirs(dst, exist_ok=True)
E = ('wordcraft', 'docxide')
R = [{'name': r['name'], 'group': r['group'], 'ref_pages': r['ref_pages'],
      **{e: {k: r[e].get(k) for k in ('ssim_strict', 'jaccard_strict', 'pages')} for e in E}}
     for r in json.load(open(f'{src}/wordcraft_comparison.json'))]
T = [{'name': t['name'], **{e: {'line_match': t[e]['line_match']} for e in E if t.get(e)}}
     for t in json.load(open(f'{src}/textcmp.json'))]
json.dump(R, open(f'{dst}/wordcraft_comparison.json', 'w'), separators=(',', ':'))
json.dump(T, open(f'{dst}/textcmp.json', 'w'), separators=(',', ':'))

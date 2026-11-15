This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated 2026-11-15 10:01 UTC.

## Summary for reviewers

`main` e9750c5cb scores **73.27** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores 88.84
(15.6 points ahead). Merging the 1 PRs below, in this order, gives **73.35 (+0.07)**,
measured on one branch with all of them merged (see *Combined branch*).

### Merge next

Ranked by what each adds on its own, with green CI and no changes requested. They merge cleanly with `main` and with
each other in this order, together with the PRs under *Not ready yet*. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | **+0.074** | 7↑ 2↓ | lithuanian_excise_tax_amendment -30.7 | ✅ | – | +1513 −136 | `dd4ef8d0f` on `e9750c5cb`, today |

### Needs a look

PRs above that also make a fixture worse by more than 5 SSIM points, and interactions between PRs:

- **#1172** (naxvog): lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8
- **Interaction found:** #3821 and #2792 together drop the six `nested-floats-spaced-text-*` fixtures from 92.5 to 31.2 SSIM; neither changes them alone (found by merging prefixes of the list above). #2792 reads a `w:tblCellMar` that sets only some sides into `partial_cell_margins` and leaves `cell_margins` empty; #3821 then sees no `cell_margins` in a file without a default table style and sets all four to 0, which overrides the sides the table does set. Whichever lands second should check `partial_cell_margins` too and fill only the missing sides with 0.
- **Interaction found:** #2523 and #5455 together drop `continuous-context-frame1-same0-ctx1` from 98.5 to 51.3 SSIM; neither changes it alone (a probe round merged only these two). There the continuous section break sits on an empty framed paragraph of another style. #5455 makes a section's closing mark the paragraph above for the next paragraph's contextual spacing, in `place_para` after the mark is laid out; #2523 places framed paragraphs in `place_framed_para`, which returns at the top of `place_para`, before that. So the paragraph after the break is compared with the one before the mark, matches its style and drops its 12 pt space before, which Word keeps. Whichever lands second should leave a section's empty closing mark to the normal path, or set `pb.prev` for it in the framed path as #5455 does.
- Left out of *Merge next* on purpose: #2792 (see *Combined branch*).

**Coverage:** 2 PRs benched (2 change the score), 0 of them stale; 223 queued for the
next round; 473 conflict with `main`.

<details><summary><b>How it's measured</b></summary>

- **Suite:** docxide-pdf's fixtures (1220 DOCX files with Word's own PDF export as the reference: handcrafted
  `cases/`, `hyphenation/` and real-world `scraped/` documents). The WordCraft harness is an opt-in suite module on
  the fork branch [naxvog/docxide-pdf/tree/wordcraft-comparison](https://github.com/naxvog/docxide-pdf/tree/wordcraft-comparison) (`tests/suite/wordcraft_comparison.rs`):
  `WORDCRAFT_CLI=<wordcraft-cli> cargo test --release --test suite wordcraft_comparison -- --nocapture`.
  It converts every fixture with `wordcraft-cli convert`, rasterises at 150 dpi with mutool and scores each page
  with the suite's own Jaccard (ink overlap) and SSIM.
- **Line match:** [textcmp.py](https://gist.github.com/naxvog/54e2039e999cdeacfc0ed59b8da3c6e6) compares the text lines of both PDFs.
- **Scores** are means over all fixtures, strict: a page WordCraft doesn't produce counts as 0. Deltas are in
  percentage points of that mean, so a fix that perfects one fixture moves it by at most ~0.1.
- **Per PR:** the PR is merged into the round's baseline (`main` at the start of the round) and the whole suite is
  rerun; its delta is against that baseline. Conflicts in files `wordcraft-cli` doesn't build (documentation,
  translation catalogs, the UI crate, the desktop and web apps, tests) take main's side, which can't change a PDF;
  PRs with conflicts in anything else are not benched. A fixture counts as changed at ±0.1 SSIM points; gains and
  regressions list fixtures that moved by more than 0.5.
- **Rounds:** a new baseline whenever `main` moves; a PR is rerun when it gets new commits, or when its result
  changed fixtures and `main` has since changed a rendering file it changes too. PRs that change no file in
  `crates/{docx,layout,render,pdf,fonts}/src` aren't benched (in 321 runs, none of them changed a fixture).
- **Safety:** PR code is built and run in containers without network or capabilities, with their own cargo caches,
  seeing the suite read-only; dependencies are downloaded without running any of the PR's code.
- **Environment:** Linux container, debug build of `wordcraft-cli` (the layout code is the same as release), fonts
  from Debian packages plus Microsoft's core web fonts. Calibri, Cambria, Aptos and the other Office fonts are
  not installed, so WordCraft draws those documents in metric-compatible substitutes (Carlito, Caladea, …) while
  Word's references use the originals. docxide-pdf runs in the same container without its private font set.

| `main` e9750c5cb | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| WordCraft | 73.27 | 55.47 | 1181/1220 | 93.3 |
| docxide-pdf (for reference) | 88.84 | 79.41 | 1203/1220 | 95.2 |

</details>

<details><summary><b>Every PR that changes the score (2)</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | +0.074 | +0.069 | +0 | 9 (7↑ 2↓) | case49 +43.4, case4 +39.6, border-group-between-rule-fill +30.3 (+4 more) | lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8 | `dd4ef8d0f` on `e9750c5cb`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | +0.007 | +0.004 | +0 | 7 (2↑ 0↓) | paragraph-border-styles +6.6, cell-paragraph-bottom-wide +1.1 | – | `8c689e973` on `e9750c5cb`, today |

**Benched, no change on the suite (0):** –. These may
still be right; the suite just has no document that exercises them.

</details>

## Combined branch

**Every PR with a positive score**: 1 PRs merged into `main` e9750c5cb in this order, at these heads (merge commit `aae61616e`, made in the bench job and not pushed): #1172 `dd4ef8d0f`. Left out: code conflict with PRs merged before it: #1757.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` e9750c5cb | 73.27 | 55.47 | 1181/1220 | 93.3 |
| combined | 73.35 (+0.074) | 55.54 (+0.069) | 1181/1220 (+0) | 93.3 (+0.00) |

The merged PRs' individual SSIM changes add up to +0.074; the difference to the combined +0.074 is where
they overlap or interact. 9 fixtures change (7↑ 2↓). Regressions over 0.5: lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8.

**The same without #2792**: 1 PRs merged into `main` e9750c5cb in this order, at these heads (merge commit `5ff52bfc2`, made in the bench job and not pushed): #1172 `dd4ef8d0f`. Left out: code conflict with PRs merged before it: #1757; left out on purpose: #2792.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` e9750c5cb | 73.27 | 55.47 | 1181/1220 | 93.3 |
| combined | 73.35 (+0.074) | 55.54 (+0.069) | 1181/1220 (+0) | 93.3 (+0.00) |

The merged PRs' individual SSIM changes add up to +0.074; the difference to the combined +0.074 is where
they overlap or interact. 9 fixtures change (7↑ 2↓). Regressions over 0.5: lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8.

## Not benched

- **Code conflicts with `main`** (473 PRs): not rerun until rebased.
- **Change no rendering file** (228): not benched.
- **Doesn't build once merged with `main`:** –.
- **Removed from this list** since they're no longer open: none.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).


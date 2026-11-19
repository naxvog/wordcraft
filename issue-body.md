This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated 2026-11-19 13:12 UTC.

## Summary for reviewers

`main` 6ef13b2cc scores **74.57** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores 88.84
(14.3 points ahead). That's with every craft-libs crate at craft-libs `main` 129230011, as for every PR below;
with the craft-libs versions `main` pins it scores 74.57, so +0.00 waits in craft-libs
for a PR that updates the pins. Merging the 30 PRs under *Merge next* and *Not ready yet*, in this order, gives **77.70 (+3.13)**,
measured on one branch with all of them merged (see *Combined branch*).

### Merge next

Ranked by what each adds on its own, with green CI and no changes requested. They merge cleanly with `main` and with
each other in this order, together with the PRs under *Not ready yet*. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #6497 | Menonro | Layout: an empty paragraph after a nested table ends its cell without a line (#6496) | **+0.553** | 34↑ 4↓ | case51 -50.4 | ✅ | – | +92 −5 | `8ddd667b3` on `5ac7c9664`, 3 d ago |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | **+0.358** | 10↑ 0↓ | – | ✅ | – | +231 −13 | `de04a1fc7` on `9a6d89420`, 3 d ago |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | **+0.270** | 8↑ 2↓ | nested-adjacent-negative-large-offset -10.5 | ✅ | – | +161 −7 | `7207e8835` on `9a6d89420`, 3 d ago |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | **+0.195** | 9↑ 1↓ | czech_municipal_grant_form -7.8 | ✅ | – | +135 −10 | `417337bb4` on `9a6d89420`, 3 d ago |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | **+0.134** | 5↑ 0↓ | – | ✅ | – | +533 −7 | `5307ce5a0` on `129230011`, today |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | **+0.134** | 5↑ 0↓ | – | ✅ | – | +280 −15 | `09bea6e3a` on `9a6d89420`, 3 d ago |
| #6632 | Menonro | Fonts: a line in Caladea takes Cambria's ascent and descent (#6631) | **+0.128** | 28↑ 8↓ | slovak_pedagogical_practice_agreement -40.0 | ✅ | – | +29 −5 | `e4df576c5` on `5ac7c9664`, 3 d ago |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | **+0.086** | 3↑ 0↓ | – | ✅ | – | +308 −4 | `dce01cdd7` on `9a6d89420`, 3 d ago |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | **+0.069** | 3↑ 0↓ | – | ✅ | – | +479 −47 | `58d9b4749` on `9a6d89420`, 3 d ago |
| #6571 | Menonro | Layout: a non-breaking hyphen the font lacks is drawn as Word draws it, on a line no taller (#6570) | **+0.060** | 9↑ 0↓ | – | ✅ | – | +159 −12 | `4eab3963e` on `5ac7c9664`, 3 d ago |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | **+0.035** | 1↑ 0↓ | – | ✅ | – | +200 −8 | `7e86e2ea5` on `9a6d89420`, 3 d ago |
| #6566 | Menonro | Layout: text in a shape keeps clear of half its outline's width (#6564) | **+0.035** | 22↑ 5↓ | text-box-table-autofit-wide -4.0 | ✅ | – | +409 −25 | `7e1159387` on `5ac7c9664`, 3 d ago |
| #6542 | Menonro | Layout: the room borders take in a table row: double and triple borders, shared edges, every cell of the row (#6540) | **+0.032** | 4↑ 2↓ | turkish_chemistry_course_plan -2.3 | ✅ | – | +228 −24 | `5e81d463a` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #6114 | kevinj24fr | Fix/footnote continued bottom | **+0.030** | 2↑ 0↓ | – | ✅ | – | +206 −13 | `4afcb2812` on `129230011`, today |
| #6659 | Menonro | Layout: how far the word ending a justified line may overrun it goes with the line's spaces (#6655) | **+0.025** | 3↑ 2↓ | squeeze-keep-slack -4.8 | ✅ | – | +87 −19 | `0c00a6ff1` on `5ac7c9664`, 3 d ago |
| #5546 | mmazzieri | Different first page: no first-page header on a continuous section's second page | **+0.020** | 1↑ 0↓ | – | ✅ | – | +108 −13 | `6eb03bf4e` on `d6b5b16bb`, 2 d ago |
| #6646 | Menonro | Layout: the part of an at-least row left on a page lines its cells up within the row's least height (#6645) | **+0.020** | 2↑ 0↓ | – | ✅ | – | +524 −45 | `32df6161d` on `5ac7c9664`, 3 d ago |
| #6586 | Menonro | Layout: every part of an at-least row split across pages is at least that tall (#6585) | **+0.020** | 2↑ 0↓ | – | ✅ | – | +142 −33 | `80761d385` on `5ac7c9664`, 3 d ago |
| #5170 | ro-legal-docx | Layout: ignore trailing spacing after footnote separators | **+0.019** | 1↑ 0↓ | – | ✅ | – | +286 −8 | `140af517c` on `129230011`, today |
| #6459 | dfgodvan | Layout: a line may break after any space, before closing punctuation or after an opening bracket, as in Word | **+0.018** | 9↑ 2↓ | period-after-space-filler-period-small-compat15 -57.6 | ✅ | – | +45 −0 | `783d2ce93` on `129230011`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | **+0.012** | 1↑ 0↓ | – | ✅ | – | +506 −5 | `c14375951` on `9a6d89420`, 3 d ago |
| #6808 | vangel76 | Persian and Arabic text in a font that is not installed now has the same line height as in Word, so pages break in the same place | **+0.006** | 1↑ 0↓ | – | ✅ | – | +304 −7 | `cf3719e8d` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #2674 | finwarman | Reserve font math leading in equation line metrics | **+0.005** | 1↑ 1↓ | pendulum_mechanics_oscillation_lab -1.8 | ✅ | – | +229 −9 | `8812f4d7d` on `9a6d89420`, 3 d ago |
| #6509 | Menonro | Layout: a word stays on its line only if it is no more than a thousandth of a point too wide (#6508) | **+0.002** | 2↑ 1↓ | case61 -0.8 | ✅ | – | +60 −4 | `e900c0c6e` on `5ac7c9664`, 3 d ago |
| #6162 | tsw2k | fix(render): frame shapes draw with a hole; frame presets open as frames | **+0.002** | 2↑ 0↓ | – | ✅ | – | +159 −14 | `8d2579542` on `129230011`, today |
| #6622 | Menonro | Layout: the spaces before a justified line's first character don't shrink and give no room for it (#6621) | **+0.001** | 1↑ 0↓ | – | ✅ | – | +76 −15 | `fc0439eda` on `5ac7c9664`, 3 d ago |

### Not ready yet

These raise the score too, but their CI fails or is still running, or a reviewer requested changes. The score says
nothing about whether the code is right; fix those first.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | **+0.807** | 29↑ 12↓ | frame-balanced-columns -41.3 | ✅ | changes requested | +770 −41 | `0edeb3c58` on `d6b5b16bb`, 2 d ago |
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | **+0.138** | 8↑ 2↓ | continued-gap-cell-after0-before4 -6.9 | ✅ | changes requested | +105 −10 | `ff079766e` on `129230011`, today |
| #4638 | arcanii | Fonts: Japanese text falls back to a Japanese font, not a Chinese one | **+0.003** | 1↑ 0↓ | – | ✅ | changes requested | +407 −23 | `fe30bfbfe` on `129230011`, today |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +90 −6 | `05fbde50f` on `9a6d89420`, 3 d ago |

### Needs a look

PRs above that also make a fixture worse by more than 5 SSIM points, and interactions between PRs:

- **#2523** (D13GOOOO): frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0, empty-margin-frame-15-one-empty -11.1 (+8 more)
- **#6497** (Menonro): case51 -50.4, connector-paragraph-anchor-240 -13.7, full-width-float-empty-anchor -10.3, table-cell-shading-edges -0.7
- **#5458** (naxvog): nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8
- **#5439** (naxvog): czech_municipal_grant_form -7.8
- **#5808** (kevinj24fr): continued-gap-cell-after0-before4 -6.9, text_align_center_mixed -0.8
- **#6632** (Menonro): slovak_pedagogical_practice_agreement -40.0, oahu_burial_council_minutes -1.8, eco_int_agriculture_registration -1.0, case39 -0.9 (+4 more)
- **#6459** (dfgodvan): period-after-space-filler-period-small-compat15 -57.6, period-after-space-filler-period-normal-compat15 -55.0
- **Interaction found:** #3821 and #2792 together dropped the six `nested-floats-spaced-text-*` fixtures from 92.5 to 31.2 SSIM on suite v66; neither changes them alone. Since #6603 the DOCX reader is `craft-docx` in craft-libs. #3821's reader change landed there as storytold/craft-libs#1278 (`1f96d6b6`), so #3821 has in effect landed first: it is now a craft-libs `rev` update plus its test and docs. #2792 has to move to `craft-docx` too. Its reader puts a `w:tblCellMar` that sets only some sides into `partial_cell_margins` and leaves `cell_margins` empty, which storytold/craft-libs#1278 reads as "no margins" and sets all four sides to 0. In `craft-docx`, #2792 should read `partial_cell_margins` and fill only the sides a partial `w:tblCellMar` leaves out, instead of keeping 0 for every side. Until then #2792 stays out of *Merge next*.
- **Interaction found:** #2523 and #5455 together drop `continuous-context-frame1-same0-ctx1` from 98.5 to 51.3 SSIM on suite v66; neither changes it alone (a probe round merged only these two). There the continuous section break sits on an empty framed paragraph of another style. #5455 makes a section's closing mark the paragraph above for the next paragraph's contextual spacing, in `place_para` after the mark is laid out; #2523 places framed paragraphs in `place_framed_para`, which returns at the top of `place_para`, before that. So the paragraph after the break is compared with the one before the mark, matches its style and drops its 12 pt space before, which Word keeps. Whichever lands second should leave a section's empty closing mark to the normal path, or set `pb.prev` for it in the framed path as #5455 does.
- Left out of *Merge next* on purpose: #2792 (see *Combined branch*).

### Would help, needs a rebase

These raised the score when they were benched, but now conflict with `main` in code.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | **+0.074** | 7↑ 2↓ | lithuanian_excise_tax_amendment -30.7 | ✅ | – | +1513 −136 | `dd4ef8d0f` on `4444eaa13`, 4 d ago |
| #3588 | dpkruse | #3585: automatic text is white on dark cell and paragraph shading | **+0.001** | 1↑ 0↓ | – | ✅ | – | +284 −24 | `739f2962d` on `d6b5b16bb`, 2 d ago |
| #5630 | kennyfs | Layout: a table in a text frame floats where the frame says | **+0.001** | 1↑ 0↓ | – | ✅ | – | +325 −26 | `e43415431` on `5ac7c9664`, 3 d ago |
| #2533 | finwarman | Fit floating text box frames to their content | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +1742 −34 | `8073a9009` on `9a6d89420`, 3 d ago |

**Coverage:** 232 PRs benched (88 change the score), 89 of them stale; 46 queued for the
next round; 475 conflict with `main`.

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
- **Per PR:** the PR is merged into the round's baseline (`main` at the start of the round, with craft-libs as below)
  and the whole suite is rerun; its delta is against that baseline. Conflicts in files `wordcraft-cli` doesn't build (documentation,
  translation catalogs, the UI crate, the desktop and web apps, tests) take main's side, which can't change a PDF;
  PRs with conflicts in anything else are not benched. A fixture counts as changed at ±0.1 SSIM points; gains and
  regressions list fixtures that moved by more than 0.5.
- **Rounds:** a new baseline whenever `main` moves; a PR is rerun when it gets new commits, or when its result
  changed fixtures and `main` has since changed a rendering file it changes too. PRs that change no file in
  `crates/{docx,layout,render,pdf,fonts}/src` aren't benched (in 321 runs, none of them changed a fixture),
  unless they move a git dependency.
- **craft-libs:** since #6603 and #6661 the DOCX and RTF readers, zip and image decoding are
  [craft-libs](https://github.com/storytold/craft-libs) crates, so a reader fix lands there and reaches WordCraft
  through a PR that moves the craft-libs pins in `Cargo.toml`. Every run (baseline, PRs, combined branches) builds
  with all craft-libs crates at the craft-libs `main` commit of the round's start, so a PR is measured on its own
  code, not on craft-libs changes its pins carry; the summary says how much craft-libs `main` adds to the versions
  `main` pins. A PR that builds only with other craft-libs versions is listed under *Not benched*.
- **Safety:** PR code is built and run in containers without network or capabilities, with their own cargo caches,
  seeing the suite read-only; dependencies are downloaded without running any of the PR's code.
- **Environment:** Linux container, debug build of `wordcraft-cli` (the layout code is the same as release), fonts
  from Debian packages plus Microsoft's core web fonts. Calibri, Cambria, Aptos and the other Office fonts are
  not installed, so WordCraft draws those documents in metric-compatible substitutes (Carlito, Caladea, …) while
  Word's references use the originals. docxide-pdf runs in the same container without its private font set.

| `main` 6ef13b2cc | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| WordCraft | 74.57 | 56.55 | 1182/1220 | 93.5 |
| docxide-pdf (for reference) | 88.84 | 79.41 | 1203/1220 | 95.2 |

</details>

<details><summary><b>Every PR that changes the score (88)</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | +0.807 | +0.810 | +1 | 43 (29↑ 12↓) | frame-float-clearance-f1-y1000-h700 +83.8, frame-float-clearance-f0-y400-h400 +80.5, frame-float-clearance-f1-y400-h700 +77.9 (+26 more) | frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0 (+9 more) | `0edeb3c58` on `d6b5b16bb`, 2 d ago |
| #6497 | Menonro | Layout: an empty paragraph after a nested table ends its cell without a line (#6496) | +0.553 | +0.587 | -1 | 40 (34↑ 4↓) | case118 +36.9, nested_table_nested_inline +36.5, case120 +36.5 (+31 more) | case51 -50.4, connector-paragraph-anchor-240 -13.7, full-width-float-empty-anchor -10.3 (+1 more) | `8ddd667b3` on `5ac7c9664`, 3 d ago |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | +0.358 | +0.242 | +0 | 15 (10↑ 0↓) | nested-autofit-padding-d3-p108-w4200 +48.4, nested-autofit-padding-d1-p108-w4200 +48.3, nested-autofit-padding-d1-p108-w6000 +45.8 (+7 more) | – | `de04a1fc7` on `9a6d89420`, 3 d ago |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | +0.270 | +0.183 | +0 | 10 (8↑ 2↓) | negative-x-nested-x-142-y1-w4820-n4 +52.7, negative-x-nested-x142-y-33-w4820-n0 +48.2, nested-final-mark-w5100-y1-h400-n1 +47.8 (+5 more) | nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8 | `7207e8835` on `9a6d89420`, 3 d ago |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | +0.195 | +0.361 | +0 | 10 (9↑ 1↓) | shifted-text-position-7-mixed0-mark1 +50.7, shifted-text-position-7-mixed0-mark0 +50.7, raised-empty-size12-position7-count2 +35.3 (+6 more) | czech_municipal_grant_form -7.8 | `417337bb4` on `9a6d89420`, 3 d ago |
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | +0.138 | +0.332 | +0 | 36 (8↑ 2↓) | nested-table-keep-next +53.8, heading-keep-next-exact +52.1, keep-next-inline-image +44.5 (+5 more) | continued-gap-cell-after0-before4 -6.9, text_align_center_mixed -0.8 | `ff079766e` on `129230011`, today |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | +0.134 | +0.122 | +3 | 5 (5↑ 0↓) | modern-oversized-lines55-cant1-prefix0 +60.7, modern-oversized-lines55-cant1-prefix330 +45.5, modern-oversized-lines55-cant1-prefix160 +45.5 (+2 more) | – | `5307ce5a0` on `129230011`, today |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | +0.134 | +0.109 | +0 | 5 (5↑ 0↓) | leading-tab-four-tabs +47.1, leading-tab-two-tabs +46.5, leading-tab-visible-prefix +38.1 (+2 more) | – | `09bea6e3a` on `9a6d89420`, 3 d ago |
| #6632 | Menonro | Fonts: a line in Caladea takes Cambria's ascent and descent (#6631) | +0.128 | +0.357 | +0 | 61 (28↑ 8↓) | welsh_palliative_care_abstract_form +61.2, case20 +20.2, handels_messiah_biblical_analysis +14.6 (+25 more) | slovak_pedagogical_practice_agreement -40.0, oahu_burial_council_minutes -1.8, eco_int_agriculture_registration -1.0 (+5 more) | `e4df576c5` on `5ac7c9664`, 3 d ago |
| #6827 | vangel76 | A table row split across pages no longer runs off the bottom of the page | +0.124 | +0.112 | +3 | 3 (3↑ 0↓) | modern-oversized-lines55-cant1-prefix0 +60.7, modern-oversized-lines55-cant1-prefix330 +45.5, modern-oversized-lines55-cant1-prefix160 +45.5 | – | `48bca16ad` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | +0.086 | +0.100 | +0 | 3 (3↑ 0↓) | continuous-context-frame1-same1-ctx1 +48.3, continuous-context-frame0-same1-ctx1 +28.5, continuous-context-after-same1-ctx1 +28.5 | – | `dce01cdd7` on `9a6d89420`, 3 d ago |
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | +0.074 | +0.069 | +0 | 9 (7↑ 2↓) | case49 +43.4, case4 +39.6, border-group-between-rule-fill +30.3 (+4 more) | lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8 | `dd4ef8d0f` on `4444eaa13`, 4 d ago |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | +0.069 | +0.057 | +0 | 3 (3↑ 0↓) | case49 +43.4, case4 +39.6, uk_commercial_lease_template +1.6 | – | `58d9b4749` on `9a6d89420`, 3 d ago |
| #6535 | TheGalitube | Place body text frames at page anchors | +0.062 | +0.056 | +0 | 1 (1↑ 0↓) | massachusetts_community_sanitation +75.0 | – | `8b40b9e0f` on `5ac7c9664`, 3 d ago |
| #6571 | Menonro | Layout: a non-breaking hyphen the font lacks is drawn as Word draws it, on a line no taller (#6570) | +0.060 | +0.101 | +1 | 10 (9↑ 0↓) | western_australia_owner_drivers_act +21.0, carbon_farming_initiative_rule +15.4, bush_fires_act_comparison +9.7 (+6 more) | – | `4eab3963e` on `5ac7c9664`, 3 d ago |
| #6606 | Menonro | Layout: a table sized by its columns takes them from its cells and is narrowed to the room it has (#6604) | +0.054 | +0.041 | -1 | 19 (11↑ 5↓) | case100 +32.4, case101 +23.7, text-box-table-autofit-wide +22.7 (+8 more) | case51 -51.4, nested-autofit-padding-d2-p108-w4200 -11.1, victorian_universal_design_policy -2.7 (+2 more) | `e36f30975` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #5887 | batistalucasv | Layout: a justified line with a tab shrinks the spaces after its last tab (#5847) | +0.049 | +0.044 | +0 | 7 (7↑ 0↓) | czech_council_resolutions_2023 +31.3, ukrainian_municipal_heating_resolution +19.2, uk_commercial_lease_template +4.4 (+4 more) | – | `0e006257e` on `129230011`, today |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | +0.048 | +0.051 | +0 | 5 (5↑ 0↓) | short-cell-widows-m14-l3-room2-w1-none +29.7, advocacy_initiative_newsletter_2013 +15.3, toc_pageref_after_tall_table +12.4 (+2 more) | – | `979077101` on `9a6d89420`, 3 d ago |
| #6652 | pakiat | Tables: a cell's text stays clear of a side border wider than twice its margin | +0.039 | +0.037 | +0 | 32 (16↑ 4↓) | case195 +6.4, case199 +6.2, case194 +6.2 (+13 more) | shape-outline-dash-cells -3.9, nested-percent-2500-2400 -1.9, nested-percent-2500-4800 -1.9 (+1 more) | `d526f6645` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #5457 | naxvog | Layout: a hidden end-of-cell mark after a closing line break takes no room | +0.038 | +0.048 | +0 | 5 (4↑ 1↓) | nested-first-row-prefix300-cant0 +22.0, nested-first-row-prefix330-cant0 +14.2, nested-first-row-prefix330-cant1 +5.9 (+1 more) | maine_criminal_history_record -1.7 | `841d4c0e2` on `9a6d89420`, 3 d ago |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | +0.035 | +0.033 | +0 | 1 (1↑ 0↓) | ut_koer_annual_meeting_minutes +43.3 | – | `7e86e2ea5` on `9a6d89420`, 3 d ago |
| #6566 | Menonro | Layout: text in a shape keeps clear of half its outline's width (#6564) | +0.035 | +0.031 | +0 | 37 (22↑ 5↓) | textbox-outline-inset +9.4, shape-outline-dash +8.3, textbox-outline-inset-style +5.8 (+19 more) | text-box-table-autofit-wide -4.0, vml-textbox-fill-color -3.4, vml-textbox-fill-default -3.4 (+2 more) | `7e1159387` on `5ac7c9664`, 3 d ago |
| #6542 | Menonro | Layout: the room borders take in a table row: double and triple borders, shared edges, every cell of the row (#6540) | +0.032 | +0.109 | +0 | 12 (4↑ 2↓) | japanese_hr_consultation_application +15.1, table-cell-shading-edges +14.8, master_thesis_learning_agreement +10.0 (+1 more) | turkish_chemistry_course_plan -2.3, turkish_ancient_religions_plan -1.3 | `5e81d463a` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #6114 | kevinj24fr | Fix/footnote continued bottom | +0.030 | +0.026 | +0 | 2 (2↑ 0↓) | zimbabwe_gold_mining_judgment +32.4, uk_commercial_lease_template +4.3 | – | `4afcb2812` on `129230011`, today |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | +0.027 | +0.023 | +0 | 2 (1↑ 0↓) | zimbabwe_gold_mining_judgment +32.4 | – | `7fce65fcc` on `9a6d89420`, 3 d ago |
| #6659 | Menonro | Layout: how far the word ending a justified line may overrun it goes with the line's spaces (#6655) | +0.025 | +0.029 | +0 | 8 (3↑ 2↓) | squeeze-lead-space +26.4, squeeze-threshold-after-hyphen +8.7, squeeze-threshold-after-space +3.9 | squeeze-keep-slack -4.8, ul-trail-space-runs -3.7 | `0c00a6ff1` on `5ac7c9664`, 3 d ago |
| #5546 | mmazzieri | Different first page: no first-page header on a continuous section's second page | +0.020 | +0.015 | +0 | 4 (1↑ 0↓) | cont-first-first-fits +24.5 | – | `6eb03bf4e` on `d6b5b16bb`, 2 d ago |
| #6586 | Menonro | Layout: every part of an at-least row split across pages is at least that tall (#6585) | +0.020 | +0.020 | +0 | 2 (2↑ 0↓) | table-row-split-lines +13.5, master_thesis_learning_agreement +10.4 | – | `80761d385` on `5ac7c9664`, 3 d ago |
| #6646 | Menonro | Layout: the part of an at-least row left on a page lines its cells up within the row's least height (#6645) | +0.020 | +0.020 | +0 | 2 (2↑ 0↓) | table-row-split-lines +13.5, master_thesis_learning_agreement +10.4 | – | `32df6161d` on `5ac7c9664`, 3 d ago |
| #5170 | ro-legal-docx | Layout: ignore trailing spacing after footnote separators | +0.019 | +0.002 | +0 | 1 (1↑ 0↓) | frame-clip-page-break +22.9 | – | `140af517c` on `129230011`, today |
| #6459 | dfgodvan | Layout: a line may break after any space, before closing punctuation or after an opening bracket, as in Word | +0.018 | +0.027 | +0 | 12 (9↑ 2↓) | period-after-space-filler-period-small +57.9, period-after-space-filler-period-normal +57.8, ukrainian_municipal_heating_resolution +9.2 (+6 more) | period-after-space-filler-period-small-compat15 -57.6, period-after-space-filler-period-normal-compat15 -55.0 | `783d2ce93` on `129230011`, today |
| #2463 | Nghiathan13 | Layout: a paragraph-anchored floating table that doesn't fit runs on across pages (#2359) | +0.017 | +0.023 | +1 | 4 (1↑ 2↓) | croatian_grant_guidelines +48.0 | pendulum_mechanics_oscillation_lab -25.4, line-anchor-overrides -1.5 | `dcf186c7f` on `129230011`, today |
| #2493 | finwarman | Close split table fragments at fitted content | +0.015 | +0.012 | +0 | 15 (5↑ 0↓) | master_thesis_learning_agreement +10.7, table-row-split-lines +2.6, cote_dazur_phd_grants_call +1.4 (+2 more) | – | `a4f4b668b` on `9a6d89420`, 3 d ago |
| #5176 | pakiat | Tables: a percentage-width table before Word 2013 adds its outer cell margins | +0.013 | +0.008 | +0 | 4 (3↑ 0↓) | chinese_costume_design_course +9.2, zimbabwe_broadcasting_corporation_judgment +3.5, zimbabwe_gold_mining_judgment +2.5 | – | `7e0f9556f` on `129230011`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | +0.012 | +0.000 | +0 | 1 (1↑ 0↓) | japanese_hr_consultation_application +14.8 | – | `c14375951` on `9a6d89420`, 3 d ago |
| #2465 | finwarman | Retain minimum heights on split-row continuations | +0.010 | +0.009 | +0 | 2 (2↑ 0↓) | master_thesis_learning_agreement +10.4, table-row-split-lines +1.9 | – | `06741cf45` on `9a6d89420`, 3 d ago |
| #6640 | Menonro | Layout: where a page ends inside a table row, the closing border has its room, and a nested row that can't split goes on whole (#6638) | +0.009 | +0.008 | +0 | 3 (2↑ 0↓) | nabl_lab_preassessment_guidelines +10.1, slovak_eu_directive_compliance_table +0.8 | – | `604efc82e` on `5ac7c9664`, 3 d ago |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | +0.006 | +0.006 | +1 | 1 (1↑ 0↓) | carbon_farming_initiative_rule +7.6 | – | `2ed7b6233` on `d6b5b16bb`, 2 d ago |
| #6808 | vangel76 | Persian and Arabic text in a font that is not installed now has the same line height as in Word, so pages break in the same place | +0.006 | +0.002 | +1 | 1 (1↑ 0↓) | arabic_rice_benefits_article +7.4 | – | `cf3719e8d` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #2674 | finwarman | Reserve font math leading in equation line metrics | +0.005 | -0.001 | +0 | 2 (1↑ 1↓) | case221 +8.0 | pendulum_mechanics_oscillation_lab -1.8 | `8812f4d7d` on `9a6d89420`, 3 d ago |
| #6538 | Menonro | Fonts: a space character the font lacks comes from its installed metric twin (#6513) | +0.005 | +0.004 | +0 | 3 (2↑ 0↓) | victorian_universal_design_policy +3.4, scottish_fundraising_awards_campaign +1.8 | – | `ee2ac6096` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #5850 | batistalucasv | layout: wrap field results across multiple lines within margins (#5838) | +0.004 | +0.005 | +0 | 5 (4↑ 1↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3, wa_child_services_regulations +0.7 (+1 more) | field-result-formatting -0.9 | `394405a53` on `129230011`, today |
| #2508 | Nghiathan13 | Layout: field results mixing scripts draw each glyph in its own face (#2491) | +0.004 | +0.003 | +0 | 5 (2↑ 1↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3 | field-result-formatting -0.9 | `0b8fea2f7` on `d6b5b16bb`, 2 d ago |
| #4638 | arcanii | Fonts: Japanese text falls back to a Japanese font, not a Chinese one | +0.003 | +0.003 | +0 | 6 (1↑ 0↓) | taiwanese_education_fraud_ruling +4.0 | – | `fe30bfbfe` on `129230011`, today |
| #6523 | finwarman | Layout: page-anchored frames in a table cell stay in the cell | +0.003 | +0.002 | +0 | 1 (1↑ 0↓) | massachusetts_community_sanitation +3.8 | – | `370489a59` on `129230011`, today |
| #6509 | Menonro | Layout: a word stays on its line only if it is no more than a thousandth of a point too wide (#6508) | +0.002 | +0.003 | +0 | 4 (2↑ 1↓) | squeeze-threshold-after-space +2.0, lithuanian_public_information_law +1.1 | case61 -0.8 | `e900c0c6e` on `5ac7c9664`, 3 d ago |
| #6162 | tsw2k | fix(render): frame shapes draw with a hole; frame presets open as frames | +0.002 | +0.006 | +0 | 2 (2↑ 0↓) | case35 +1.8, case34 +0.9 | – | `8d2579542` on `129230011`, today |
| #6620 | Menonro | Layout: the text after a centre tab stays within its line (#6619) | +0.002 | +0.002 | +0 | 4 (3↑ 1↓) | clean_energy_regulator_act +1.3, western_australia_owner_drivers_act +1.2, wa_child_services_regulations +0.9 | carbon_farming_initiative_rule -1.3 | `e1cfb0016` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #4614 | dfgodvan | Layout: a right tab past the right indent takes its text up to the stop, as in Word | +0.002 | +0.001 | +0 | 5 (3↑ 1↓) | clean_energy_regulator_act +1.3, western_australia_owner_drivers_act +1.2, wa_child_services_regulations +0.9 | carbon_farming_initiative_rule -1.3 | `af9dca95d` on `d6b5b16bb`, 2 d ago |
| #3588 | dpkruse | #3585: automatic text is white on dark cell and paragraph shading | +0.001 | +0.000 | +0 | 2 (1↑ 0↓) | radiographer_interventional_job_desc +1.8 | – | `739f2962d` on `d6b5b16bb`, 2 d ago |
| #2488 | Nghiathan13 | Layout: In Front of Text objects draw over the whole page's text (#1993) | +0.001 | +0.002 | +0 | 5 (2↑ 0↓) | through-picture-columns +0.7, text-box-story-pictures +0.6 | – | `d69845dfd` on `129230011`, today |
| #6526 | finwarman | Layout: behind-text objects in table cells paint by z-order | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | behind-text-layer +1.5 | – | `0ec8f9a60` on `5ac7c9664`, 3 d ago |
| #5630 | kennyfs | Layout: a table in a text frame floats where the frame says | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | massachusetts_community_sanitation +1.1 | – | `e43415431` on `5ac7c9664`, 3 d ago |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | +0.001 | +0.001 | +0 | 4 (1↑ 0↓) | through-picture-columns +0.7 | – | `05fbde50f` on `9a6d89420`, 3 d ago |
| #6395 | Nghiathan13 | #5534: floating pictures are drawn over the shading of the paragraphs below them | +0.001 | +0.001 | +0 | 4 (1↑ 0↓) | through-picture-columns +0.7 | – | `51eb0f372` on `129230011`, today |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `69578bbc6` on `9a6d89420`, 3 d ago |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `3d04c471a` on `9a6d89420`, 3 d ago |
| #5166 | ro-legal-docx | Layout: keep headings with following inline tables | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `534211c68` on `9a6d89420`, 3 d ago |
| #2533 | finwarman | Fit floating text box frames to their content | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | tab-only-line-own-font +0.8 | – | `8073a9009` on `9a6d89420`, 3 d ago |
| #6622 | Menonro | Layout: the spaces before a justified line's first character don't shrink and give no room for it (#6621) | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | czech_council_resolutions_2023 +0.7 | – | `fc0439eda` on `5ac7c9664`, 3 d ago |
| #6302 | ljkx | #6260: character shading and highlight are one fill per run of letters, with no seams between them | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `2acaf870a` on `5ac7c9664`, 3 d ago |
| #3462 | midasdf | Layout: hanging punctuation (overflowPunct) and line-start punctuation compression (topLinePunct) | +0.000 | +0.001 | +0 | 2 (0↑ 0↓) | – | – | `61a16a5d8` on `129230011`, today |
| #6506 | Menonro | Layout: a cell spanning columns that fits their preferred widths leaves them alone (#6504) | +0.000 | +0.001 | +0 | 2 (1↑ 0↓) | strategi_pengembangan_information_center_resort +0.7 | – | `b1ad8c8db` on `5ac7c9664`, 3 d ago |
| #2454 | finwarman | Fix automatic leading on picture-only lines | +0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `3411f542d` on `9a6d89420`, 3 d ago |
| #6501 | Menonro | Layout: text in a shape is set in the shape's text rectangle (#6500) | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `d823f7b56` on `5ac7c9664`, 3 d ago |
| #6625 | Menonro | Layout: the space after a text box's last paragraph is part of the box's text (#6624) | +0.000 | +0.000 | +0 | 2 (1↑ 0↓) | case34 +0.5 | – | `d6cb5c8db` on `5ac7c9664`, 3 d ago |
| #4867 | cyfung1031 | #4859: multiple line spacing on a document grid | +0.000 | +0.001 | +0 | 1 (0↑ 0↓) | – | – | `1f6fabcd7` on `9a6d89420`, 3 d ago |
| #6576 | Nghiathan13 | Layout: a right tab at the margin keeps its text there beside a float | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `af9b866ca` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #2662 | finwarman | Respect the font minimum height for display operators | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `d4b9c5865` on `9a6d89420`, 3 d ago |
| #5789 | kevinj24fr | Layout: a line of only pictures takes its paragraph mark's height (#3984 follow-up) | -0.000 | +0.044 | +0 | 1 (0↑ 0↓) | – | – | `ad320eccc` on `129230011`, today |
| #5634 | kennyfs | Layout: turned cell text never makes a row taller, as in Word | -0.000 | +0.001 | +0 | 1 (0↑ 0↓) | – | – | `a224da94d` on `5ac7c9664`, 3 d ago |
| #5003 | xiaojunyang0805 | layout: character-grid cells for large text, \*Chars indents in grid cells | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `5bb02c46e` on `d6b5b16bb`, 2 d ago |
| #5935 | frandavid100 | layout: reserve table footnotes before fitting row fragments | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `0130efd73` on `5ac7c9664`, 3 d ago |
| #6678 | jayzed80 | fix(layout): a right tab stop past the right indent keeps its text on the page (#6447) | -0.000 | -0.000 | +0 | 3 (0↑ 0↓) | – | – | `594c59fc2` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #5102 | VoiceLessQ | Text boxes keep a line while its text ends inside the box (#5059) | -0.001 | -0.001 | +0 | 3 (0↑ 1↓) | – | text-box-table-linked -0.9 | `6bdc7fb38` on `d6b5b16bb`, 2 d ago |
| #6258 | appyx123 | Fonts: resolve Yu Mincho and Yu Gothic aliases and macOS AssetData (#6237) | -0.001 | -0.000 | +0 | 1 (0↑ 1↓) | – | japanese_medical_consultation_form -1.3 | `c82e61eaf` on `5ac7c9664`, 3 d ago |
| #1486 | dfgodvan | Tables: a page break inside a vertical merge takes the merged cell's text along (#1485) | -0.001 | -0.002 | +0 | 1 (0↑ 1↓) | – | go_math_grade4_guide -1.6 | `127edec15` on `d6b5b16bb`, 2 d ago |
| #2709 | finwarman | Honor complete rounded percentage cell widths | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | primary_care_safeguarding_annual_review -2.5 | `40afc9b79` on `9a6d89420`, 3 d ago |
| #5181 | pakiat | Tables: a percentage-width table from Word 2013 takes its share after its outer borders | -0.002 | +0.000 | +0 | 7 (3↑ 2↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.6 | italian_project_proposal -6.8, japanese_land_development_sign_form -1.2 | `1f8c020fc` on `129230011`, today |
| #6002 | pakiat | Tables: right-to-left start edges, mode 14 end edges and style parts' inner lines as Word | -0.002 | +0.000 | +0 | 7 (3↑ 2↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.6 | italian_project_proposal -6.8, japanese_land_development_sign_form -1.2 | `4005e1ede` on `129230011`, today |
| #4564 | OPUZZLES | Tables: keep fitting hanging-indent labels at their grid width | -0.004 | -0.003 | +0 | 1 (0↑ 1↓) | – | australian_higher_education_guidelines -4.5 | `ce2d2deb8` on `9a6d89420`, 3 d ago |
| #3559 | MichaelMuClaude | Tables: an older-mode table moves out by its default cell margin, not the first cell's own (#3407) | -0.005 | -0.004 | +0 | 1 (0↑ 1↓) | – | candidate_reference_check_form -5.6 | `20a2238ee` on `d6b5b16bb`, 2 d ago |
| #2502 | midasmatterhorn | Layout: a square-wrapped logo in the default header is drawn and pushes the body down | -0.007 | -0.016 | +0 | 3 (1↑ 2↓) | czech_municipal_grant_form +10.7 | cote_dazur_phd_grants_call -17.1, bosch_software_ai_announcement -2.3 | `7e7b40168` on `9a6d89420`, 3 d ago |
| #2604 | finwarman | Choose justified breaks by spacing cost | -0.016 | -0.012 | +0 | 5 (2↑ 2↓) | squeeze-lead-space +23.0, squeeze-threshold-after-space +3.9 | czech_village_budget_commentary -43.9, squeeze-keep-slack -2.5 | `4f6ea07aa` on `9a6d89420`, 3 d ago |
| #6219 | pakiat | Paragraph defaults: a file without w:pPrDefault gets Word's 8 pt after | -0.017 | -0.009 | +0 | 1 (0↑ 1↓) | – | tabbed_cjk_justify -21.1 | `b473f5964` on `129230011`, today |
| #6795 | TheGalitube | Honor preferred cell widths with mismatched table grids | -0.070 | -0.063 | +0 | 20 (2↑ 16↓) | case111 +23.9, autofit-cell-widths +4.4 | autofit-saved-grid-auto-nested-address -35.9, case112 -23.5, case109 -18.9 (+13 more) | `d3793ce15` on `5ac7c9664`, 3 d ago |
| #6671 | Menonro | Layout: text set out of its table cell is cut off at the cell's edges (#6670) | -0.088 | +0.026 | +0 | 18 (9↑ 3↓) | cell-label-double-level-center-para-left-text0 +2.1, cell-label-narrow-20-level-center-para-left-text0 +1.7, cell-label-narrow-35-level-center-para-left-text0 +1.6 (+6 more) | case204 -42.5, case210 -42.5, nested-table-picture-width -35.4 | `5f4bfe87a` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |
| #6587 | jayzed80 | Layout: place negative-offset floats from a first line pushed down by a wrapping float (#6567) | -0.108 | -0.111 | +0 | 9 (1↑ 8↓) | line-anchor-follows-push +5.2 | connector-paragraph-anchor-0 -62.4, connector-paragraph-anchor-240 -62.4, japanese_hr_consultation_application -3.4 (+5 more) | `50041c808` on `5ac7c9664`, 3 d ago ⚠ stale: new commits |

**Benched, no change on the suite (144):** #6003, #1563, #1588, #1713, #1715, #2117, #2120, #2186, #2356, #2496, #2514, #2655, #2719, #2817, #3072, #3089, #3119, #3148, #3185, #3198, #3253, #3332, #3472, #3825, #3878, #3935, #4089, #4134, #4183, #4214, #4260, #4278, #4316, #4338, #4339, #4413, #4445, #4493, #4521, #4565, #4571, #4580, #4581, #4656, #4791, #4795, #4874, #4901, #4905, #4932, #5002, #5004, #5041, #5067, #5071, #5134, #5153, #5159, #5177, #5200, #5283, #5293, #5302, #5317, #5362, #5422, #5470, #5516, #5545, #5557, #5576, #5628, #5764, #5767, #5791, #5831, #5834, #5852, #5872, #5888, #5891, #5917, #5950, #5951, #5953, #5954, #5986, #6034, #6077, #6091, #6092, #6100, #6103, #6107, #6112, #6122, #6142, #6144, #6171, #6197, #6313, #6347, #6361, #6363, #6389, #6399, #6401, #6406, #6422, #6425, #6457, #6471, #6485, #6487, #6489, #6524, #6525, #6528, #6529, #6545, #6573, #6575, #6578, #6580, #6581, #6582, #6594, #6607, #6611, #6614, #6616, #6628, #6634, #6642, #6649, #6662, #6665, #6737, #6744, #6772, #6796, #6809, #6828, #6835. These may
still be right; the suite just has no document that exercises them.

</details>

## Combined branch

**Every PR with a positive score**: 30 PRs merged into `main` 129230011 in this order, at these heads (merge commit `773a78a65`, made in the bench job and not pushed): #2523 `0edeb3c58`, #6497 `8ddd667b3`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #5808 `ff079766e`, #4840 `5307ce5a0`, #2552 `09bea6e3a`, #6632 `e4df576c5`, #5455 `dce01cdd7`, #5095 `58d9b4749`, #6571 `4eab3963e`, #3823 `7e86e2ea5`, #6566 `7e1159387`, #6542 `e353018fa`, #6114 `4afcb2812`, #6659 `0c00a6ff1`, #5546 `6eb03bf4e`, #6646 `32df6161d`, #6586 `80761d385`, #5170 `140af517c`, #6459 `783d2ce93`, #2834 `c14375951`, #6808 `62b84b3e8`, #2674 `8812f4d7d`, #4638 `fe30bfbfe`, #6509 `e900c0c6e`, #6162 `8d2579542`, #4186 `05fbde50f`, #6622 `fc0439eda`. Left out: code conflict with `main`: #1172, #2533, #3588, #5630; code conflict with PRs merged before it: #6827, #6535, #6606, #5887, #3833, #6652, #5457, #4065, #2463, #2493, #5176, #2465, #6640, #3604, #6538, #5850, #2508, #6523, #6620, #4614, #2488, #6526, #6395, #5166, #3834, #3832.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 129230011 | 74.57 | 56.55 | 1182/1220 | 93.5 |
| combined | 77.70 (+3.128) | 60.37 (+3.819) | 1187/1220 (+5) | 93.8 (+0.26) |

The merged PRs' individual SSIM changes add up to +3.218; the difference to the combined +3.128 is where
they overlap or interact. 290 fixtures change (187↑ 39↓). Regressions over 0.5: period-after-space-filler-period-small-compat15 -57.6, period-after-space-filler-period-normal-compat15 -55.0, case51 -48.9, continuous-context-frame1-same0-ctx1 -47.1, frame-balanced-columns -41.3, slovak_pedagogical_practice_agreement -40.0, frame-moved-space-before -31.4, case128 -26.0 (+31 more).

**The same without #2792**: 30 PRs merged into `main` 129230011 in this order, at these heads (merge commit `38ef434c2`, made in the bench job and not pushed): #2523 `0edeb3c58`, #6497 `8ddd667b3`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #5808 `ff079766e`, #4840 `5307ce5a0`, #2552 `09bea6e3a`, #6632 `e4df576c5`, #5455 `dce01cdd7`, #5095 `58d9b4749`, #6571 `4eab3963e`, #3823 `7e86e2ea5`, #6566 `7e1159387`, #6542 `e353018fa`, #6114 `4afcb2812`, #6659 `0c00a6ff1`, #5546 `6eb03bf4e`, #6646 `32df6161d`, #6586 `80761d385`, #5170 `140af517c`, #6459 `783d2ce93`, #2834 `c14375951`, #6808 `62b84b3e8`, #2674 `8812f4d7d`, #4638 `fe30bfbfe`, #6509 `e900c0c6e`, #6162 `8d2579542`, #4186 `05fbde50f`, #6622 `fc0439eda`. Left out: code conflict with `main`: #1172, #2533, #3588, #5630; code conflict with PRs merged before it: #6827, #6535, #6606, #5887, #3833, #6652, #5457, #4065, #2463, #2493, #5176, #2465, #6640, #3604, #6538, #5850, #2508, #6523, #6620, #4614, #2488, #6526, #6395, #5166, #3834, #3832; left out on purpose: #2792.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 129230011 | 74.57 | 56.55 | 1182/1220 | 93.5 |
| combined | 77.70 (+3.128) | 60.37 (+3.819) | 1187/1220 (+5) | 93.8 (+0.26) |

The merged PRs' individual SSIM changes add up to +3.218; the difference to the combined +3.128 is where
they overlap or interact. 290 fixtures change (187↑ 39↓). Regressions over 0.5: period-after-space-filler-period-small-compat15 -57.6, period-after-space-filler-period-normal-compat15 -55.0, case51 -48.9, continuous-context-frame1-same0-ctx1 -47.1, frame-balanced-columns -41.3, slovak_pedagogical_practice_agreement -40.0, frame-moved-space-before -31.4, case128 -26.0 (+31 more).

## Not benched

- **Code conflicts with `main`** (475 PRs): not rerun until rebased.
- **Change no rendering file** (214): not benched.
- **Doesn't build once merged with `main`:** #1303, #2512, #3160, #4408, #4645, #5451, #5737, #6400.
- **Doesn't build with craft-libs `main`** (builds with the craft-libs versions it pins): –.
- **Removed from this list** since they're no longer open: merged #5073, #2860, #3933, #4393, #4474, #4836, #5062, #5494, #5569, #5601, #5616, #5810, #5824, #5880, #5971, #6048, #6085, #6207, #6477, #6507, #6547, #6589, #6658, #6666, #6690, #6695, #6696, #6698, #6703, #6706, #6709, #6714, #6719, #6724, #6725, #6759, #6776, #6785, #6789, #6793, #6818, #6826, #1757, #2345, #2711, #3022, #4219, #4964, #5074, #5096, #5129, #5638; closed without merging #1791, #5702, #5703, #5723, #3024, #3587, #4460, #5187, #5462, #5665, #5940, #5995, #6218, #6309, #6458, #6527, #6654, #1630, #2063, #2064, #2065, #3764.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).


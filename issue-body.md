This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated 2026-11-12 17:42 UTC.

## Summary for reviewers

`main` 10e5bb8bc scores **73.70** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores 87.34
(13.6 points ahead). Merging the 32 PRs under *Merge next* and *Not ready yet*, in this order, gives **77.79 (+4.09)**,
measured on one branch with all of them merged (see *Combined branch*).

### Merge next

Ranked by what each adds on its own, with green CI and no changes requested. They merge cleanly with `main` and with
each other in this order, together with the PRs under *Not ready yet*. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3821 | naxvog | Tables: a file with no default table style gives its tables no cell margins | **+1.361** | 88↑ 11↓ | case91 -6.2 | ✅ | – | +88 −4 | `1c5a2ec36` on `d40d1b271`, 3 d ago |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | **+0.916** | 23↑ 6↓ | case128 -26.0 | ✅ | – | +675 −39 | `5ae458526` on `060768f1e`, 1 d ago |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | **+0.425** | 16↑ 2↓ | case91 -8.6 | ✅ | – | +231 −13 | `de04a1fc7` on `4b0d39959`, 4 d ago |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | **+0.307** | 8↑ 2↓ | nested-adjacent-negative-large-offset -10.5 | ✅ | – | +161 −7 | `7207e8835` on `060768f1e`, 1 d ago |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | **+0.220** | 8↑ 1↓ | czech_municipal_grant_form -7.8 | ✅ | – | +135 −10 | `417337bb4` on `e0d8312fb`, 4 d ago |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | **+0.152** | 5↑ 0↓ | – | ✅ | – | +280 −15 | `09bea6e3a` on `a42c9eaab`, 2 d ago |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | **+0.141** | 3↑ 0↓ | – | ✅ | – | +470 −7 | `f7196220a` on `661a79054`, 4 d ago |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | **+0.098** | 3↑ 0↓ | – | ✅ | – | +198 −2 | `de5f71f7e` on `060768f1e`, 1 d ago |
| #6030 | pakiat | Tables: Word gives a table nothing from Normal Table, and Table Grid is based on it | **+0.097** | 4↑ 1↓ | wide-nested-float-edge-wide-m14-left-o108-i0 -23.8 | ✅ | – | +262 −4 | `a1d416e33` on `7b8c0ba5e`, 3 d ago |
| #4507 | vu2jpr | Word parity for a table- and chart-heavy report: tables, charts, fonts, picture fills | **+0.071** | 5↑ 2↓ | turkish_chemistry_course_plan -1.0 | ✅ | – | +3378 −282 | `e23ee246a` on `a8db235e0`, today |
| #2463 | Nghiathan13 | Layout: a paragraph-anchored floating table that doesn't fit runs on across pages (#2359) | **+0.056** | 2↑ 1↓ | pendulum_mechanics_oscillation_lab -25.4 | ✅ | – | +160 −20 | `a7ca977ee` on `10e5bb8bc`, today |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | **+0.040** | 1↑ 0↓ | – | ✅ | – | +200 −8 | `7e86e2ea5` on `661a79054`, 4 d ago |
| #6114 | kevinj24fr | Fix/footnote continued bottom | **+0.034** | 2↑ 0↓ | – | ✅ | – | +138 −9 | `6997afcc3` on `2922fe566`, 3 d ago |
| #5546 | mmazzieri | Different first page: no first-page header on a continuous section's second page | **+0.023** | 1↑ 0↓ | – | ✅ | – | +108 −13 | `892235af0` on `411a4915a`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | **+0.014** | 1↑ 0↓ | – | ✅ | – | +506 −5 | `c14375951` on `7b8c0ba5e`, 3 d ago |
| #5206 | MarekSpodBiedry | DOCX: keep negative picture crop values and pad the picture instead of squeezing it (#5194) | **+0.013** | 1↑ 0↓ | – | ✅ | – | +59 −13 | `e070b8a0c` on `a42c9eaab`, 2 d ago |
| #5006 | xiaojunyang0805 | doc, docx, layout: East Asian punctuation compression (w:characterSpacingControl) | **+0.008** | 2↑ 0↓ | – | ✅ | – | +723 −18 | `da0ab31dc` on `a8db235e0`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | **+0.008** | 2↑ 0↓ | – | ✅ | – | +147 −54 | `8c689e973` on `060768f1e`, 1 d ago |
| #2674 | finwarman | Reserve font math leading in equation line metrics | **+0.006** | 1↑ 1↓ | pendulum_mechanics_oscillation_lab -1.8 | ✅ | – | +229 −9 | `8812f4d7d` on `d40d1b271`, 3 d ago |
| #6162 | tsw2k | fix(docx): frame shapes have a hole; header drawings aren't dimmed | **+0.003** | 2↑ 0↓ | – | ✅ | – | +297 −20 | `4a7a9f3db` on `06c2ae6f9`, today |
| #5096 | dfgodvan | Layout: no line break after the '?' of a query, nor after a slash before an underscore | **+0.001** | 1↑ 0↓ | – | ✅ | – | +83 −5 | `f63e31c07` on `7b8c0ba5e`, 3 d ago |
| #5074 | pakiat | Tables: percentage cell widths size their columns whichever rows give them | **+0.001** | 0↑ 0↓ | – | ✅ | – | +341 −7 | `cbbb8ee5d` on `7b8c0ba5e`, 3 d ago |
| #4846 | jpc7k1 | Layout: with useFELayout + balanceSingleByteDoubleByteWidth, runs of spaces take the East Asian space width | **+0.001** | 1↑ 0↓ | – | ✅ | – | +110 −2 | `8ba7b65bb` on `d40d1b271`, 3 d ago |
| #2608 | finwarman | Honor row table cell margin exceptions | **+0.001** | 1↑ 0↓ | – | ✅ | – | +261 −12 | `c11c3fa85` on `7b8c0ba5e`, 3 d ago |
| #6302 | ljkx | #6260: character shading and highlight are one fill per run of letters, with no seams between them | **+0.001** | 0↑ 0↓ | – | ✅ | – | +145 −10 | `5e32115b4` on `07f977372`, today |

### Not ready yet

These raise the score too, but their CI fails or is still running, or a reviewer requested changes. The score says
nothing about whether the code is right; fix those first.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | **+0.153** | 6↑ 1↓ | continued-gap-cell-after0-before4 -2.8 | ✅ | changes requested | +105 −10 | `575797399` on `ad5e1a65f`, 1 d ago |
| #2711 | Nghiathan13 | #2702: a missing font is drawn in its font table's altName, as Word does | **+0.048** | 2↑ 2↓ | missing_font_substitution -1.7 | ✅ | changes requested | +391 −50 | `498f6a23c` on `a42c9eaab`, 2 d ago |
| #6219 | pakiat | DOCX: a default part the file leaves out is Word's own (12 pt run, 8 pt after) | **+0.016** | 4↑ 0↓ | – | ❌ | – | +230 −18 | `e31d4c0e5` on `ad5e1a65f`, 1 d ago |
| #2465 | finwarman | Retain minimum heights on split-row continuations | **+0.010** | 1↑ 0↓ | – | ✅ | changes requested | +179 −14 | `06741cf45` on `7b8c0ba5e`, 4 d ago |
| #5564 | chamber074 | Draw a picture's outline (Picture Border) on screen and in PDF | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +1394 −35 | `4ce8daa1d` on `d86d2b69f`, today ⚠ stale: new commits |
| #5695 | prasertsakd | Add Thai Distributed alignment and capped Thai justification | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +1379 −30 | `b8094ceec` on `06c2ae6f9`, today |
| #5339 | MichaelMuClaude | A DOCX drop cap's letter takes the text's size instead of being scaled twice (#5294) | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +34 −2 | `28dff24e4` on `729cd0a5f`, 6 d ago |

### Needs a look

PRs above that also make a fixture worse by more than 5 SSIM points, and interactions between PRs:

- **#3821** (naxvog): case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7, nested_table_center_positive -1.7 (+7 more)
- **#2523** (D13GOOOO): case128 -26.0, empty-margin-frame-15-one-empty -11.1, empty-margin-frame-15-two-empty -10.5, empty-margin-frame-15-two-space-only -10.5 (+2 more)
- **#5443** (naxvog): case91 -8.6, case89 -8.5
- **#5458** (naxvog): nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8
- **#5439** (naxvog): czech_municipal_grant_form -7.8
- **#6030** (pakiat): wide-nested-float-edge-wide-m14-left-o108-i0 -23.8
- **#2463** (Nghiathan13): pendulum_mechanics_oscillation_lab -25.4
- **Interaction found:** #3821 and #2792 together drop the six `nested-floats-spaced-text-*` fixtures from 92.5 to 31.2 SSIM; neither changes them alone (found by merging prefixes of the list above). #2792 reads a `w:tblCellMar` that sets only some sides into `partial_cell_margins` and leaves `cell_margins` empty; #3821 then sees no `cell_margins` in a file without a default table style and sets all four to 0, which overrides the sides the table does set. Whichever lands second should check `partial_cell_margins` too and fill only the missing sides with 0.
- Left out of *Merge next* on purpose: #2792 (see *Combined branch*).

### Would help, needs a rebase

These raised the score when they were benched, but now conflict with `main` in code.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3787 | cyril265 | Layout: a page break at the end of the document or of a section starts no blank page | **+0.105** | 2↑ 0↓ | – | ✅ | – | +611 −30 | `9a1a34e4d` on `e919982fa`, 6 d ago ⚠ stale: main changed ctx.rs, flow.rs |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | **+0.079** | 3↑ 0↓ | – | ✅ | – | +482 −47 | `8cd2a0ad3` on `e919982fa`, 6 d ago ⚠ stale: main changed flow.rs |
| #4845 | jpc7k1 | Layout: a justified line with a tab shrinks the spaces after its last tab, as Word does | **+0.054** | 5↑ 0↓ | – | ✅ | – | +66 −18 | `59cbe9ad1` on `e919982fa`, 6 d ago ⚠ stale: main changed para/lines.rs |
| #3790 | cyril265 | Layout: text before a floating table or shape on its page wraps around it | **+0.050** | 2↑ 0↓ | – | ✅ | – | +1545 −75 | `4314cc213` on `e919982fa`, 7 d ago ⚠ stale: main changed ctx.rs, floats.rs, flow.rs … |
| #2047 | finwarman | Layout: keep picture-only anchors with their pictures | **+0.031** | 2↑ 0↓ | – | ✅ | – | +586 −8 | `f57a937fe` on `e919982fa`, 6 d ago ⚠ stale: main changed flow.rs |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | **+0.029** | 3↑ 0↓ | – | ✅ | – | +225 −3 | `c29995c9d` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, para/paragraph.rs, table_flow.rs |
| #4619 | Harrison-Booth | Fonts: report a missing Word core font with no metric twin | **+0.024** | 1↑ 0↓ | – | ✅ | – | +119 −15 | `0aaef7a5b` on `e919982fa`, 6 d ago ⚠ stale: main changed word.rs |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | **+0.001** | 1↑ 0↓ | – | ✅ | – | +157 −2 | `3b415d7f5` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | **+0.001** | 1↑ 0↓ | – | ✅ | – | +192 −3 | `e391c2c86` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #5562 | Znerual | Layout: a footnote mark stays with the text before it (#5402) | **+0.001** | 1↑ 0↓ | – | ✅ | – | +272 −6 | `638fd79f0` on `e919982fa`, 7 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs, para/paragraph.rs |

**Coverage:** 402 PRs benched (101 change the score), 175 of them stale; 39 queued for the
next round; 373 conflict with `main`.

<details><summary><b>How it's measured</b></summary>

- **Suite:** docxide-pdf's fixtures (1073 DOCX files with Word's own PDF export as the reference: handcrafted
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

| `main` 10e5bb8bc | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| WordCraft | 73.70 | 56.17 | 1044/1073 | 93.2 |
| docxide-pdf (for reference) | 87.34 | 70.90 | 1055/1073 | 93.9 |

</details>

<details><summary><b>Every PR that changes the score (101)</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3821 | naxvog | Tables: a file with no default table style gives its tables no cell margins | +1.361 | +1.155 | +0 | 102 (88↑ 11↓) | table-wrap-indent-inline-i5100-r0 +60.0, table-wrap-indent-inline-i5100-r240 +59.3, case211 +43.6 (+85 more) | case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7 (+8 more) | `1c5a2ec36` on `d40d1b271`, 3 d ago |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | +0.916 | +0.890 | +0 | 30 (23↑ 6↓) | frame-float-clearance-f1-y1000-h700 +83.8, frame-float-clearance-f0-y400-h400 +80.5, frame-float-clearance-f1-y400-h700 +77.9 (+20 more) | case128 -26.0, empty-margin-frame-15-one-empty -11.1, empty-margin-frame-15-two-empty -10.5 (+3 more) | `5ae458526` on `060768f1e`, 1 d ago |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | +0.425 | +0.277 | +0 | 25 (16↑ 2↓) | nested-autofit-padding-d3-p108-w4200 +48.4, nested-autofit-padding-d1-p108-w4200 +48.3, nested-autofit-padding-d1-p108-w6000 +45.8 (+13 more) | case91 -8.6, case89 -8.5 | `de04a1fc7` on `4b0d39959`, 4 d ago |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | +0.307 | +0.205 | +0 | 10 (8↑ 2↓) | negative-x-nested-x-142-y1-w4820-n4 +52.7, negative-x-nested-x142-y-33-w4820-n0 +48.2, nested-final-mark-w5100-y1-h400-n1 +47.8 (+5 more) | nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8 | `7207e8835` on `060768f1e`, 1 d ago |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | +0.220 | +0.409 | +0 | 9 (8↑ 1↓) | shifted-text-position-7-mixed0-mark1 +50.7, shifted-text-position-7-mixed0-mark0 +50.7, raised-empty-size12-position7-count2 +35.3 (+5 more) | czech_municipal_grant_form -7.8 | `417337bb4` on `e0d8312fb`, 4 d ago |
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | +0.153 | +0.101 | +0 | 15 (6↑ 1↓) | nested-table-keep-next +53.8, heading-keep-next-exact +52.1, keep-next-inline-image +44.5 (+3 more) | continued-gap-cell-after0-before4 -2.8 | `575797399` on `ad5e1a65f`, 1 d ago |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | +0.152 | +0.124 | +0 | 5 (5↑ 0↓) | leading-tab-four-tabs +47.1, leading-tab-two-tabs +46.5, leading-tab-visible-prefix +38.1 (+2 more) | – | `09bea6e3a` on `a42c9eaab`, 2 d ago |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | +0.141 | +0.128 | +3 | 3 (3↑ 0↓) | modern-oversized-lines55-cant1-prefix0 +60.7, modern-oversized-lines55-cant1-prefix330 +45.5, modern-oversized-lines55-cant1-prefix160 +45.5 | – | `f7196220a` on `661a79054`, 4 d ago |
| #3787 | cyril265 | Layout: a page break at the end of the document or of a section starts no blank page | +0.105 | +0.089 | +2 | 2 (2↑ 0↓) | geneva_waste_facility_permit_request +63.4, stem_partnerships_guide +49.3 | – | `9a1a34e4d` on `e919982fa`, 6 d ago ⚠ stale: main changed ctx.rs, flow.rs |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | +0.098 | +0.114 | +0 | 3 (3↑ 0↓) | continuous-context-frame1-same1-ctx1 +48.3, continuous-context-frame0-same1-ctx1 +28.5, continuous-context-after-same1-ctx1 +28.5 | – | `de5f71f7e` on `060768f1e`, 1 d ago |
| #6030 | pakiat | Tables: Word gives a table nothing from Normal Table, and Table Grid is based on it | +0.097 | +0.085 | +0 | 5 (4↑ 1↓) | section-mark-after-table-inline-compat14 +51.1, case196 +30.4, short-float-clear-inline-table +25.5 (+1 more) | wide-nested-float-edge-wide-m14-left-o108-i0 -23.8 | `a1d416e33` on `7b8c0ba5e`, 3 d ago |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | +0.079 | +0.065 | +0 | 3 (3↑ 0↓) | case49 +43.4, case4 +39.6, uk_commercial_lease_template +1.6 | – | `8cd2a0ad3` on `e919982fa`, 6 d ago ⚠ stale: main changed flow.rs |
| #4507 | vu2jpr | Word parity for a table- and chart-heavy report: tables, charts, fonts, picture fills | +0.071 | +0.080 | +0 | 15 (5↑ 2↓) | welsh_palliative_care_abstract_form +69.0, clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3 (+2 more) | turkish_chemistry_course_plan -1.0, turkish_ancient_religions_plan -0.9 | `e23ee246a` on `a8db235e0`, today |
| #2463 | Nghiathan13 | Layout: a paragraph-anchored floating table that doesn't fit runs on across pages (#2359) | +0.056 | +0.062 | +1 | 4 (2↑ 1↓) | croatian_grant_guidelines +48.0, indigenous_innovation_sandbox_agreement +37.6 | pendulum_mechanics_oscillation_lab -25.4 | `a7ca977ee` on `10e5bb8bc`, today |
| #5887 | batistalucasv | Layout: a justified line with a tab shrinks the spaces after its last tab (#5847) | +0.055 | +0.050 | +0 | 6 (6↑ 0↓) | czech_council_resolutions_2023 +31.3, ukrainian_municipal_heating_resolution +19.2, uk_commercial_lease_template +4.4 (+3 more) | – | `cad9a4e6a` on `ad5e1a65f`, 1 d ago |
| #4845 | jpc7k1 | Layout: a justified line with a tab shrinks the spaces after its last tab, as Word does | +0.054 | +0.048 | +0 | 5 (5↑ 0↓) | czech_council_resolutions_2023 +31.5, ukrainian_municipal_heating_resolution +19.5, uk_commercial_lease_template +4.4 (+2 more) | – | `59cbe9ad1` on `e919982fa`, 6 d ago ⚠ stale: main changed para/lines.rs |
| #2010 | dkhlapov | SVG pictures: insert, draw sharp, read and write Word's svgBlip (#1910) | +0.054 | +0.081 | +0 | 1 (1↑ 0↓) | svg-pictures +58.0 | – | `745e32fc3` on `4706420e9`, today |
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | +0.050 | +0.050 | +0 | 4 (3↑ 1↓) | case49 +43.4, case4 +39.6, uk_commercial_lease_template +1.6 | lithuanian_excise_tax_amendment -30.7 | `dd4ef8d0f` on `060768f1e`, 1 d ago |
| #3790 | cyril265 | Layout: text before a floating table or shape on its page wraps around it | +0.050 | +0.019 | +0 | 2 (2↑ 0↓) | full-width-float-empty-anchor +37.5, bosch_software_ai_announcement +15.6 | – | `4314cc213` on `e919982fa`, 7 d ago ⚠ stale: main changed ctx.rs, floats.rs, flow.rs … |
| #2711 | Nghiathan13 | #2702: a missing font is drawn in its font table's altName, as Word does | +0.048 | +0.045 | +0 | 6 (2↑ 2↓) | auditor_regulatory_report_template +51.6, seminary_hill_board_meeting +2.0 | missing_font_substitution -1.7, eco_int_agriculture_registration -0.6 | `498f6a23c` on `a42c9eaab`, 2 d ago |
| #5457 | naxvog | Layout: a hidden end-of-cell mark after a closing line break takes no room | +0.043 | +0.055 | +0 | 5 (4↑ 1↓) | nested-first-row-prefix300-cant0 +22.0, nested-first-row-prefix330-cant0 +14.2, nested-first-row-prefix330-cant1 +5.9 (+1 more) | maine_criminal_history_record -1.7 | `841d4c0e2` on `4b0d39959`, 4 d ago |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | +0.040 | +0.037 | +0 | 1 (1↑ 0↓) | ut_koer_annual_meeting_minutes +43.3 | – | `7e86e2ea5` on `661a79054`, 4 d ago |
| #6114 | kevinj24fr | Fix/footnote continued bottom | +0.034 | +0.030 | +0 | 2 (2↑ 0↓) | zimbabwe_gold_mining_judgment +32.4, uk_commercial_lease_template +4.3 | – | `6997afcc3` on `2922fe566`, 3 d ago |
| #2047 | finwarman | Layout: keep picture-only anchors with their pictures | +0.031 | +0.026 | +1 | 2 (2↑ 0↓) | indonesian_benchmarking_guide +32.3, brazilian_logistics_study +0.5 | – | `f57a937fe` on `e919982fa`, 6 d ago ⚠ stale: main changed flow.rs |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | +0.030 | +0.027 | +0 | 2 (1↑ 0↓) | zimbabwe_gold_mining_judgment +32.4 | – | `7fce65fcc` on `060768f1e`, 1 d ago |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | +0.029 | +0.039 | +0 | 3 (3↑ 0↓) | short-cell-widows-m14-l3-room2-w1-none +29.7, wa_child_services_regulations +0.9, romanian_quality_evaluation_strategy +0.8 | – | `c29995c9d` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, para/paragraph.rs, table_flow.rs |
| #4619 | Harrison-Booth | Fonts: report a missing Word core font with no metric twin | +0.024 | +0.012 | +1 | 1 (1↑ 0↓) | arabic_rice_benefits_article +25.4 | – | `0aaef7a5b` on `e919982fa`, 6 d ago ⚠ stale: main changed word.rs |
| #5546 | mmazzieri | Different first page: no first-page header on a continuous section's second page | +0.023 | +0.018 | +0 | 3 (1↑ 0↓) | cont-first-first-fits +24.5 | – | `892235af0` on `411a4915a`, today |
| #6219 | pakiat | DOCX: a default part the file leaves out is Word's own (12 pt run, 8 pt after) | +0.016 | +0.017 | +0 | 7 (4↑ 0↓) | seq-heading-reset +9.9, alfies_arc_adult_safeguarding_policy +4.1, polish_building_procurement_spec +2.3 (+1 more) | – | `e31d4c0e5` on `ad5e1a65f`, 1 d ago |
| #5176 | pakiat | Tables: a percentage-width table before Word 2013 adds its outer cell margins | +0.015 | +0.011 | +0 | 5 (4↑ 0↓) | chinese_costume_design_course +9.2, zimbabwe_broadcasting_corporation_judgment +3.5, zimbabwe_gold_mining_judgment +2.5 (+1 more) | – | `ff4e71a17` on `7b8c0ba5e`, 3 d ago |
| #2493 | finwarman | Close split table fragments at fitted content | +0.015 | +0.011 | +0 | 13 (4↑ 0↓) | master_thesis_learning_agreement +10.7, cote_dazur_phd_grants_call +1.4, education_consultant_posting +1.1 (+1 more) | – | `a4f4b668b` on `a42c9eaab`, 2 d ago |
| #2834 | finwarman | Keep empty row continuations with their labels | +0.014 | +0.000 | +0 | 1 (1↑ 0↓) | japanese_hr_consultation_application +14.8 | – | `c14375951` on `7b8c0ba5e`, 3 d ago |
| #2027 | dkhlapov | Picture Format › Crop: Crop to Shape, Aspect Ratio, Fill and Fit (UI gap) | +0.013 | +0.017 | +0 | 3 (1↑ 0↓) | case78 +13.2 | – | `df3583145` on `d40d1b271`, 3 d ago |
| #5206 | MarekSpodBiedry | DOCX: keep negative picture crop values and pad the picture instead of squeezing it (#5194) | +0.013 | +0.017 | +0 | 2 (1↑ 0↓) | case78 +13.2 | – | `e070b8a0c` on `a42c9eaab`, 2 d ago |
| #2465 | finwarman | Retain minimum heights on split-row continuations | +0.010 | +0.008 | +0 | 1 (1↑ 0↓) | master_thesis_learning_agreement +10.4 | – | `06741cf45` on `7b8c0ba5e`, 4 d ago |
| #5006 | xiaojunyang0805 | doc, docx, layout: East Asian punctuation compression (w:characterSpacingControl) | +0.008 | +0.007 | +0 | 4 (2↑ 0↓) | taiwanese_education_fraud_ruling +6.5, chinese_costume_design_course +3.0 | – | `da0ab31dc` on `a8db235e0`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | +0.008 | +0.004 | +0 | 7 (2↑ 0↓) | paragraph-border-styles +6.6, cell-paragraph-bottom-wide +1.1 | – | `8c689e973` on `060768f1e`, 1 d ago |
| #5948 | keithcsqueensu | Charts: draw bubble charts instead of a placeholder (#5941) | +0.008 | +0.007 | +0 | 1 (1↑ 0↓) | case31 +8.1 | – | `6b2e81c95` on `ad5e1a65f`, 1 d ago ⚠ stale: new commits |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | +0.007 | +0.007 | +1 | 1 (1↑ 0↓) | carbon_farming_initiative_rule +7.6 | – | `02b9edd57` on `4706420e9`, today |
| #6092 | pakiat | Tables: a table style's shading is what Word paints | +0.006 | +0.014 | +0 | 2 (1↑ 1↓) | table-style-valign-merged +7.6 | physical_therapy_comparison_table -0.8 | `4e48f4296` on `8548b33be`, 2 d ago |
| #5850 | batistalucasv | layout: wrap field results across multiple lines within margins (#5838) | +0.006 | +0.005 | +0 | 4 (4↑ 0↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3, wa_child_services_regulations +0.7 (+1 more) | – | `8f14b5446` on `8548b33be`, 2 d ago |
| #2674 | finwarman | Reserve font math leading in equation line metrics | +0.006 | -0.002 | +0 | 2 (1↑ 1↓) | case221 +8.0 | pendulum_mechanics_oscillation_lab -1.8 | `8812f4d7d` on `d40d1b271`, 3 d ago |
| #6215 | sebastian-schmitt | ODT: double borders keep their exact stroke widths (gap 19) | +0.006 | -0.001 | +0 | 1 (1↑ 0↓) | paragraph-border-styles +6.1 | – | `b90e06e28` on `07f977372`, today |
| #2393 | dkhlapov | #1534: more preset shapes and picture fills | +0.006 | +0.009 | +0 | 3 (2↑ 0↓) | case34 +4.8, case35 +0.8 | – | `a3d770582` on `2922fe566`, 3 d ago |
| #5462 | xiaojunyang0805 | layout: a field result in more than one font keeps a cluster per font | +0.005 | +0.003 | +0 | 4 (2↑ 0↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3 | – | `5f1d5cc23` on `d86d2b69f`, today |
| #2792 | finwarman | Inherit omitted table-wide cell margins | +0.004 | +0.003 | +0 | 2 (2↑ 0↓) | english_town_council_report +3.3, maine_criminal_history_record +0.5 | – | `09a0c68df` on `7b8c0ba5e`, 3 d ago |
| #6162 | tsw2k | fix(docx): frame shapes have a hole; header drawings aren't dimmed | +0.003 | +0.007 | +0 | 2 (2↑ 0↓) | case35 +1.8, case34 +0.9 | – | `4a7a9f3db` on `06c2ae6f9`, today |
| #4460 | fluorine | Critical batch: some approved, CI-green PRs merged together | +0.002 | +0.002 | +0 | 2 (2↑ 0↓) | case77 +1.2, torture_test +1.0 | – | `728a33c50` on `a8db235e0`, today |
| #4614 | dfgodvan | Layout: a right tab past the right indent takes its text up to the stop, as in Word | +0.002 | +0.002 | +0 | 5 (3↑ 1↓) | clean_energy_regulator_act +1.3, western_australia_owner_drivers_act +1.2, wa_child_services_regulations +0.9 | carbon_farming_initiative_rule -1.3 | `210a596d4` on `661a79054`, 4 d ago |
| #3588 | dpkruse | #3585: automatic text is white on dark cell and paragraph shading | +0.002 | +0.000 | +0 | 1 (1↑ 0↓) | radiographer_interventional_job_desc +1.8 | – | `cb6a1bde0` on `4706420e9`, today |
| #5564 | chamber074 | Draw a picture's outline (Picture Border) on screen and in PDF | +0.001 | +0.000 | +0 | 3 (1↑ 0↓) | case57 +0.8 | – | `4ce8daa1d` on `d86d2b69f`, today ⚠ stale: new commits |
| #5695 | prasertsakd | Add Thai Distributed alignment and capped Thai justification | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `b8094ceec` on `06c2ae6f9`, today |
| #3072 | inmean | Add Thai Distributed and Khmer Justify paragraph alignments | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `32df8c240` on `d40d1b271`, 3 d ago ⚠ stale: new commits |
| #5590 | xullul | Home › Paragraph: a Thai Distributed button after Justify | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `a5a3f3b1f` on `06c2ae6f9`, today |
| #5630 | kennyfs | Layout: a table in a text frame floats where the frame says | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | massachusetts_community_sanitation +1.1 | – | `e43415431` on `060768f1e`, 1 d ago |
| #5096 | dfgodvan | Layout: no line break after the '?' of a query, nor after a slash before an underscore | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | erasmus_plus_staff_mobility_agreement +1.0 | – | `f63e31c07` on `7b8c0ba5e`, 3 d ago |
| #5339 | MichaelMuClaude | A DOCX drop cap's letter takes the text's size instead of being scaled twice (#5294) | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | torture_test +0.9 | – | `28dff24e4` on `729cd0a5f`, 6 d ago |
| #5166 | ro-legal-docx | Layout: keep headings with following inline tables | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `534211c68` on `060768f1e`, 1 d ago |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `3b415d7f5` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `e391c2c86` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #4142 | SusieeTheLinuxUser | DOCX: a drop cap's letter takes the text's size back, not the file's enlarged one (#3000) | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | torture_test +0.7 | – | `c1c8d6d9b` on `7b8c0ba5e`, 3 d ago |
| #5562 | Znerual | Layout: a footnote mark stays with the text before it (#5402) | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | mongolian_human_rights_law +0.6 | – | `638fd79f0` on `e919982fa`, 7 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs, para/paragraph.rs |
| #5074 | pakiat | Tables: percentage cell widths size their columns whichever rows give them | +0.001 | +0.000 | +0 | 2 (0↑ 0↓) | – | – | `cbbb8ee5d` on `7b8c0ba5e`, 3 d ago |
| #4846 | jpc7k1 | Layout: with useFELayout + balanceSingleByteDoubleByteWidth, runs of spaces take the East Asian space width | +0.001 | +0.001 | +0 | 4 (1↑ 0↓) | japanese_interlibrary_loan +0.7 | – | `8ba7b65bb` on `d40d1b271`, 3 d ago |
| #2608 | finwarman | Honor row table cell margin exceptions | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | maine_criminal_history_record +0.5 | – | `c11c3fa85` on `7b8c0ba5e`, 3 d ago |
| #6302 | ljkx | #6260: character shading and highlight are one fill per run of letters, with no seams between them | +0.001 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `5e32115b4` on `07f977372`, today |
| #3462 | midasdf | Layout: hanging punctuation (overflowPunct) and line-start punctuation compression (topLinePunct) | +0.000 | +0.001 | +0 | 2 (0↑ 0↓) | – | – | `cb235350e` on `7b8c0ba5e`, 3 d ago |
| #2454 | finwarman | Fix automatic leading on picture-only lines | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `3411f542d` on `a42c9eaab`, 2 d ago |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `05fbde50f` on `060768f1e`, 1 d ago |
| #5102 | VoiceLessQ | Text boxes keep a line while its text ends inside the box (#5059) | +0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `cd4a43252` on `661a79054`, 4 d ago |
| #2708 | finwarman | Honor nested display fraction sizing | +0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `be7b27470` on `d40d1b271`, 3 d ago |
| #3828 | arc-uri-el | fix(docx): write and read a turned object's effect extent as Word does | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `c9348402b` on `e919982fa`, 7 d ago ⚠ stale: main changed read/story/drawing.rs, write/embed.rs, write/story/drawing.rs |
| #4867 | cyfung1031 | #4859: multiple line spacing on a document grid | +0.000 | +0.001 | +0 | 1 (0↑ 0↓) | – | – | `1f6fabcd7` on `661a79054`, 4 d ago |
| #4638 | arcanii | Fonts: Japanese text falls back to a Japanese font, not a Chinese one | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `018794e92` on `661a79054`, 4 d ago |
| #5129 | pakiat | Fields: PDFs and prints show body PAGEREF pages, as Word fills them in | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `4d74d2c02` on `7b8c0ba5e`, 3 d ago ⚠ stale: main changed lib.rs, pass.rs, export.rs … |
| #2488 | Nghiathan13 | Layout: In Front of Text objects draw over the whole page's text (#1993) | +0.000 | +0.000 | +0 | 2 (0↑ 0↓) | – | – | `c19b28c96` on `10e5bb8bc`, today |
| #5252 | scks1 | Layout: a continuous section after a page break and an empty closing mark starts the new page (#2109) | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `76cc35b2a` on `e919982fa`, 7 d ago ⚠ stale: new commits; main changed flow.rs, page.rs, pass.rs |
| #2662 | finwarman | Respect the font minimum height for display operators | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `d4b9c5865` on `e919982fa`, 6 d ago |
| #3217 | MichaelMuClaude | A display operator without a cataloged size variant still enlarges (#3208) | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `fd3ec0185` on `d40d1b271`, 3 d ago |
| #5634 | kennyfs | Layout: turned cell text never makes a row taller, as in Word | -0.000 | +0.002 | +0 | 1 (0↑ 0↓) | – | – | `a224da94d` on `060768f1e`, 1 d ago |
| #5735 | benandez | Watermark: picture watermarks and transparency (#3001) | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `c36e6e680` on `729cd0a5f`, 5 d ago ⚠ stale: main changed read.rs, read/parts.rs, read/story/runs.rs … |
| #5005 | xiaojunyang0805 | doc, docx, layout: w:hint="eastAsia" and named East Asian substitutes | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `b9081fa80` on `a8db235e0`, today |
| #5003 | xiaojunyang0805 | layout: character-grid cells for large text, \*Chars indents in grid cells | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `528951ac8` on `a8db235e0`, today |
| #5935 | frandavid100 | layout: reserve table footnotes before fitting row fragments | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `0130efd73` on `ad5e1a65f`, 1 d ago |
| #6258 | appyx123 | Fonts: resolve Yu Mincho and Yu Gothic aliases and macOS AssetData (#6237) | -0.001 | -0.001 | +0 | 1 (0↑ 1↓) | – | japanese_medical_consultation_form -1.3 | `c82e61eaf` on `07f977372`, today |
| #5313 | Harrison-Booth | Preserve table cell diagonal borders | -0.001 | -0.001 | +0 | 3 (0↑ 1↓) | – | italian_academic_cv_form -0.8 | `857e371a0` on `7b8c0ba5e`, 3 d ago |
| #1486 | dfgodvan | Tables: a page break inside a vertical merge takes the merged cell's text along (#1485) | -0.001 | -0.001 | +0 | 1 (0↑ 1↓) | – | go_math_grade4_guide -1.6 | `947cf1b51` on `4b0d39959`, 4 d ago |
| #4558 | ro-legal-docx | Borders: preserve dashSmallGap and align border previews | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | paragraph-border-styles -2.2 | `2fef96870` on `661a79054`, 4 d ago |
| #542 | krinry | feat(shapes): full Office shapes gallery and canvas drag-to-draw tool | -0.002 | -0.003 | +0 | 3 (1↑ 2↓) | case34 +1.1 | case35 -1.8, japanese_land_development_sign_form -1.3 | `9675dab46` on `4b0d39959`, 4 d ago ⚠ stale: main changed read/story/drawing.rs, exporter.rs, lib.rs |
| #2709 | finwarman | Honor complete rounded percentage cell widths | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | primary_care_safeguarding_annual_review -2.5 | `40afc9b79` on `7b8c0ba5e`, 3 d ago |
| #6002 | pakiat | Tables: right-to-left start edges, mode 14 end edges and style parts' inner lines as Word | -0.003 | -0.000 | +0 | 6 (3↑ 2↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.7 | italian_project_proposal -6.8, japanese_land_development_sign_form -1.2 | `5aab683ff` on `ad5e1a65f`, 1 d ago |
| #5181 | pakiat | Tables: a percentage-width table from Word 2013 takes its share after its outer borders | -0.003 | -0.000 | +0 | 6 (3↑ 2↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.7 | italian_project_proposal -6.8, japanese_land_development_sign_form -1.2 | `17b972967` on `7b8c0ba5e`, 3 d ago |
| #4564 | OPUZZLES | Tables: keep fitting hanging-indent labels at their grid width | -0.004 | -0.003 | +0 | 1 (0↑ 1↓) | – | australian_higher_education_guidelines -4.5 | `ce2d2deb8` on `7b8c0ba5e`, 3 d ago |
| #3559 | MichaelMuClaude | Tables: an older-mode table moves out by its default cell margin, not the first cell's own (#3407) | -0.005 | -0.005 | +0 | 1 (0↑ 1↓) | – | candidate_reference_check_form -5.6 | `37d524030` on `7b8c0ba5e`, 3 d ago |
| #2714 | finwarman | Preserve equation size and superscript ink bounds | -0.013 | -0.003 | +0 | 1 (0↑ 1↓) | – | pendulum_mechanics_oscillation_lab -13.6 | `fc20c8931` on `661a79054`, 4 d ago ⚠ stale: main changed read/story/runs.rs |
| #4864 | cyfung1031 | Read w:textAlignment and w:adjustLineHeightInTable; honour the grid in table cells | -0.026 | +0.003 | +0 | 4 (1↑ 2↓) | physical_therapy_comparison_table +58.4 | center-body-list-height-center-space0 -43.3, center-body-list-height-center-space1 -42.8 | `8fa65bb78` on `060768f1e`, 1 d ago |
| #6197 | pakiat | Tables: a nested table wider than its cell is cut off at the cell's edges | -0.033 | -0.020 | +0 | 2 (0↑ 2↓) | – | case204 -17.8, case210 -17.8 | `b183835e0` on `a42c9eaab`, 2 d ago |
| #2604 | finwarman | Choose justified breaks by spacing cost | -0.037 | -0.036 | +0 | 3 (1↑ 1↓) | squeeze-threshold-after-space +3.9 | czech_village_budget_commentary -43.9 | `4f6ea07aa` on `7b8c0ba5e`, 3 d ago |
| #1630 | Morzilla | Tables without w:tblGrid take their grid from the cells, and widths wider than the page are squeezed like Word | -0.038 | -0.034 | +0 | 3 (0↑ 3↓) | – | parish_housing_data_profile -35.9, victorian_universal_design_policy -2.7, russian_construction_org_council_minutes -2.0 | `34c0369d4` on `4b0d39959`, 4 d ago |
| #4436 | dfgodvan | Layout: line height of an inline picture in multiple line spacing, as in Word | -0.044 | +0.070 | -2 | 21 (7↑ 5↓) | picture-mark-leading-compat15-line480 +42.8, czech_village_budget_commentary +22.1, brazilian_logistics_study +22.0 (+4 more) | picture-mark-leading-mark22-line360-text0 -41.2, picture-mark-leading-compat14-line480 -39.3, picture-mark-leading-mark28-line480-text0 -39.3 (+2 more) | `431251e13` on `e919982fa`, 7 d ago ⚠ stale: main changed flow.rs, para/lines.rs |
| #2578 | finwarman | Reserve page-colour clearance in initial header stories | -0.113 | -0.090 | -1 | 2 (0↑ 2↓) | – | traditional_skills_job_form -65.5, czech_village_council_minutes_2025 -55.8 | `0d82383ac` on `e919982fa`, 6 d ago ⚠ stale: main changed page.rs, pass.rs |

**Benched, no change on the suite (301):** #4635, #4652, #5349, #6003, #1123, #1217, #1278, #1303, #1493, #1713, #1715, #1753, #1791, #1838, #1927, #1928, #1931, #1952, #1999, #2022, #2056, #2063, #2064, #2100, #2117, #2120, #2141, #2260, #2288, #2340, #2345, #2356, #2372, #2384, #2414, #2455, #2473, #2533, #2586, #2643, #2655, #2664, #2703, #2719, #2732, #2733, #2817, #2901, #2995, #3022, #3077, #3089, #3148, #3198, #3200, #3309, #3332, #3388, #3404, #3465, #3472, #3506, #3587, #3778, #3788, #3825, #3829, #3878, #3884, #3933, #3935, #3960, #3961, #3965, #3972, #3980, #3993, #4089, #4134, #4183, #4214, #4260, #4266, #4278, #4316, #4320, #4321, #4322, #4338, #4353, #4393, #4407, #4413, #4437, #4443, #4445, #4473, #4474, #4483, #4504, #4521, #4532, #4571, #4580, #4582, #4615, #4625, #4631, #4642, #4647, #4655, #4656, #4688, #4703, #4709, #4714, #4716, #4717, #4719, #4723, #4737, #4747, #4766, #4773, #4781, #4783, #4786, #4791, #4795, #4797, #4826, #4836, #4839, #4849, #4852, #4856, #4860, #4874, #4901, #4905, #4932, #4934, #4972, #4993, #5002, #5004, #5007, #5013, #5015, #5020, #5024, #5041, #5061, #5064, #5067, #5073, #5076, #5098, #5112, #5113, #5153, #5158, #5159, #5170, #5172, #5177, #5187, #5200, #5209, #5228, #5251, #5254, #5259, #5283, #5293, #5302, #5312, #5314, #5331, #5351, #5357, #5362, #5378, #5386, #5387, #5390, #5407, #5422, #5427, #5435, #5447, #5451, #5461, #5463, #5470, #5483, #5494, #5500, #5516, #5521, #5541, #5545, #5557, #5560, #5565, #5576, #5599, #5600, #5613, #5616, #5628, #5631, #5638, #5639, #5651, #5665, #5670, #5675, #5702, #5703, #5731, #5737, #5738, #5764, #5767, #5772, #5778, #5779, #5789, #5791, #5810, #5820, #5823, #5831, #5852, #5859, #5864, #5869, #5870, #5872, #5880, #5881, #5882, #5885, #5888, #5889, #5891, #5901, #5907, #5916, #5917, #5918, #5940, #5950, #5951, #5953, #5954, #5968, #5969, #5971, #5972, #5977, #5980, #5986, #5991, #5992, #6035, #6036, #6037, #6051, #6077, #6080, #6081, #6082, #6091, #6093, #6100, #6103, #6107, #6112, #6127, #6130, #6136, #6141, #6142, #6144, #6170, #6171, #6203, #6207, #6231, #6233, #6243, #6244, #6245, #6246, #6300, #6313, #6347, #6361, #6362. These may
still be right; the suite just has no document that exercises them.

</details>

## Combined branch

**Every PR with a positive score**: 32 PRs merged into `main` 10e5bb8bc in this order, at these heads (merge commit `d9bdd2dd2`, made in the bench job and not pushed): #3821 `1c5a2ec36`, #2523 `5ae458526`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #5808 `575797399`, #2552 `09bea6e3a`, #4840 `f7196220a`, #5455 `de5f71f7e`, #6030 `a1d416e33`, #4507 `e23ee246a`, #2463 `a7ca977ee`, #2711 `498f6a23c`, #3823 `7e86e2ea5`, #6114 `6997afcc3`, #5546 `892235af0`, #6219 `e31d4c0e5`, #2834 `c14375951`, #5206 `e070b8a0c`, #2465 `06741cf45`, #5006 `da0ab31dc`, #1757 `8c689e973`, #2674 `8812f4d7d`, #2792 `09a0c68df`, #6162 `4a7a9f3db`, #5564 `9360719ea`, #5695 `b8094ceec`, #5096 `f63e31c07`, #5339 `28dff24e4`, #5074 `cbbb8ee5d`, #4846 `8ba7b65bb`, #6302 `5e32115b4`. Left out: code conflict with `main`: #2047, #3787, #3790, #3832, #3833, #3834, #4619, #4845, #5095, #5562; code conflict with PRs merged before it: #5887, #2010, #1172, #5457, #4065, #5176, #2493, #5948, #3604, #6092, #5850, #6215, #2393, #5462, #4460, #4614, #3588, #5590, #3072, #5630, #4142, #2608; doesn't compile with the PRs merged before it: #2027, #5166.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 10e5bb8bc | 73.70 | 56.17 | 1044/1073 | 93.2 |
| combined | 76.73 (+3.031) | 59.15 (+2.973) | 1048/1073 (+4) | 93.6 (+0.36) |

The merged PRs' individual SSIM changes add up to +4.229; the difference to the combined +3.031 is where
they overlap or interact. 260 fixtures change (181↑ 44↓). Regressions over 0.5: nested-floats-spaced-text-long-one -62.9, nested-floats-spaced-text-bottom-cell -61.8, nested-floats-spaced-text-long-two -61.8, nested-floats-spaced-text-nonzero-x -61.8, nested-floats-spaced-text-inline-reference -60.6, nested-floats-spaced-text-short-spacers -58.8, section-mark-after-table-inline-compat15 -53.6, section-mark-after-table-float-compat15 -51.4 (+36 more).

**The same without #2792 (#2608 merges here instead, so the difference between the two isn't #2792 alone)**: 32 PRs merged into `main` 10e5bb8bc in this order, at these heads (merge commit `6f0a46948`, made in the bench job and not pushed): #3821 `1c5a2ec36`, #2523 `5ae458526`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #5808 `575797399`, #2552 `09bea6e3a`, #4840 `f7196220a`, #5455 `de5f71f7e`, #6030 `a1d416e33`, #4507 `e23ee246a`, #2463 `a7ca977ee`, #2711 `498f6a23c`, #3823 `7e86e2ea5`, #6114 `6997afcc3`, #5546 `892235af0`, #6219 `e31d4c0e5`, #2834 `c14375951`, #5206 `e070b8a0c`, #2465 `06741cf45`, #5006 `da0ab31dc`, #1757 `8c689e973`, #2674 `8812f4d7d`, #6162 `4a7a9f3db`, #5564 `9360719ea`, #5695 `b8094ceec`, #5096 `f63e31c07`, #5339 `28dff24e4`, #5074 `cbbb8ee5d`, #4846 `8ba7b65bb`, #2608 `c11c3fa85`, #6302 `5e32115b4`. Left out: code conflict with `main`: #2047, #3787, #3790, #3832, #3833, #3834, #4619, #4845, #5095, #5562; code conflict with PRs merged before it: #5887, #2010, #1172, #5457, #4065, #5176, #2493, #5948, #3604, #6092, #5850, #6215, #2393, #5462, #4460, #4614, #3588, #5590, #3072, #5630, #4142; doesn't compile with the PRs merged before it: #2027, #5166; left out on purpose: #2792.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 10e5bb8bc | 73.70 | 56.17 | 1044/1073 | 93.2 |
| combined | 77.79 (+4.094) | 59.93 (+3.761) | 1048/1073 (+4) | 93.8 (+0.56) |

The merged PRs' individual SSIM changes add up to +4.226; the difference to the combined +4.094 is where
they overlap or interact. 249 fixtures change (189↑ 25↓). Regressions over 0.5: continuous-context-frame1-same0-ctx1 -47.1, case128 -26.0, pendulum_mechanics_oscillation_lab -25.5, wide-nested-float-edge-wide-m14-left-o108-i0 -23.8, empty-margin-frame-15-one-empty -11.1, nested-adjacent-negative-large-offset -10.5, empty-margin-frame-15-two-empty -10.5, empty-margin-frame-15-two-space-only -10.5 (+17 more).

## Not benched

- **Code conflicts with `main`** (373 PRs): not rerun until rebased.
- **Change no rendering file** (128): not benched.
- **Doesn't build once merged with `main`:** #1292, #2783, #2876, #3160, #3520, #4265, #4408, #4640, #4645, #5570, #675.
- **Removed from this list** since they're no longer open: merged #5684, #5448, #5442, #5450, #5346, #5347, #5348, #5437, #5440, #5456, #4579, #5055, #5392, #5655, #5691, #5287, #5343, #5410, #5452, #5697, #4702, #5533, #5594, #5295, #5411, #5729, #5734, #5761, #5784, #5788, #5796, #5802, #5811, #5830, #5851, #5459, #5414, #5453, #5426, #2783, #3195, #3197, #5705, #5721, #6039, #2251, #4683, #6033, #6049, #6022, #6161, #6169, #6120, #6124, #6004; closed without merging #1579, #1809, #2415, #3082, #3984, #4267, #4297, #2437, #2495, #2670, #3241, #3915, #4307, #4837, #5632, #5633, #4249, #5666, #3187, #1448, #3141, #3883, #4189, #4938, #5678, #5119, #5974, #1518, #1806, #1807, #1810, #1814, #1815, #2039, #2642, #2706, #3090, #3097, #3101, #3111, #3443, #6066, #4251, #4399, #4566, #4665, #6118, #5949.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).


This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated 2026-11-15 11:04 UTC.

## Summary for reviewers

`main` e9750c5cb scores **73.27** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores 88.84
(15.6 points ahead). Merging the 16 PRs under *Merge next* and *Not ready yet*, in this order, gives **76.42 (+3.15)**,
measured on one branch with all of them merged (see *Combined branch*).

### Merge next

Ranked by what each adds on its own, with green CI and no changes requested. They merge cleanly with `main` and with
each other in this order, together with the PRs under *Not ready yet*. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #4316 | dotCooCoo | Proofing: hide spelling or grammar errors in this document only | **+1.247** | 98↑ 11↓ | case91 -6.2 | ✅ | – | +318 −64 | `4eeac27b3` on `e9750c5cb`, today |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | **+0.807** | 29↑ 12↓ | frame-balanced-columns -41.3 | ✅ | – | +675 −39 | `5ae458526` on `e9750c5cb`, today |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | **+0.373** | 16↑ 2↓ | case91 -8.6 | ✅ | – | +231 −13 | `de04a1fc7` on `e9750c5cb`, today |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | **+0.270** | 8↑ 2↓ | nested-adjacent-negative-large-offset -10.5 | ✅ | – | +161 −7 | `7207e8835` on `e9750c5cb`, today |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | **+0.195** | 9↑ 1↓ | czech_municipal_grant_form -7.8 | ✅ | – | +135 −10 | `417337bb4` on `e9750c5cb`, today |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | **+0.134** | 5↑ 0↓ | – | ✅ | – | +280 −15 | `09bea6e3a` on `e9750c5cb`, today |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | **+0.086** | 3↑ 0↓ | – | ✅ | – | +308 −4 | `dce01cdd7` on `e9750c5cb`, today |
| #2463 | Nghiathan13 | Layout: a paragraph-anchored floating table that doesn't fit runs on across pages (#2359) | **+0.048** | 2↑ 2↓ | pendulum_mechanics_oscillation_lab -25.4 | ✅ | – | +160 −20 | `a7ca977ee` on `e9750c5cb`, today |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | **+0.035** | 1↑ 0↓ | – | ✅ | – | +200 −8 | `7e86e2ea5` on `e9750c5cb`, today |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | **+0.027** | 1↑ 0↓ | – | ✅ | – | +123 −16 | `7fce65fcc` on `e9750c5cb`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | **+0.012** | 1↑ 0↓ | – | ✅ | – | +506 −5 | `c14375951` on `e9750c5cb`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | **+0.007** | 2↑ 0↓ | – | ✅ | – | +147 −54 | `8c689e973` on `e9750c5cb`, today |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | **+0.006** | 1↑ 0↓ | – | ✅ | – | +95 −17 | `02b9edd57` on `e9750c5cb`, today |
| #2674 | finwarman | Reserve font math leading in equation line metrics | **+0.005** | 1↑ 1↓ | pendulum_mechanics_oscillation_lab -1.8 | ✅ | – | +229 −9 | `8812f4d7d` on `e9750c5cb`, today |

### Not ready yet

These raise the score too, but their CI fails or is still running, or a reviewer requested changes. The score says
nothing about whether the code is right; fix those first.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #2465 | finwarman | Retain minimum heights on split-row continuations | **+0.010** | 2↑ 0↓ | – | ✅ | changes requested | +179 −14 | `06741cf45` on `e9750c5cb`, today |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +90 −6 | `05fbde50f` on `e9750c5cb`, today |

### Needs a look

PRs above that also make a fixture worse by more than 5 SSIM points, and interactions between PRs:

- **#4316** (dotCooCoo): case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7, nested_table_center_positive -1.7 (+7 more)
- **#2523** (D13GOOOO): frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0, empty-margin-frame-15-one-empty -11.1 (+8 more)
- **#5443** (naxvog): case91 -8.6, case89 -8.5
- **#5458** (naxvog): nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8
- **#5439** (naxvog): czech_municipal_grant_form -7.8
- **#2463** (Nghiathan13): pendulum_mechanics_oscillation_lab -25.4, line-anchor-overrides -1.6
- **Interaction found:** #3821 and #2792 together drop the six `nested-floats-spaced-text-*` fixtures from 92.5 to 31.2 SSIM; neither changes them alone (found by merging prefixes of the list above). #2792 reads a `w:tblCellMar` that sets only some sides into `partial_cell_margins` and leaves `cell_margins` empty; #3821 then sees no `cell_margins` in a file without a default table style and sets all four to 0, which overrides the sides the table does set. Whichever lands second should check `partial_cell_margins` too and fill only the missing sides with 0.
- **Interaction found:** #2523 and #5455 together drop `continuous-context-frame1-same0-ctx1` from 98.5 to 51.3 SSIM; neither changes it alone (a probe round merged only these two). There the continuous section break sits on an empty framed paragraph of another style. #5455 makes a section's closing mark the paragraph above for the next paragraph's contextual spacing, in `place_para` after the mark is laid out; #2523 places framed paragraphs in `place_framed_para`, which returns at the top of `place_para`, before that. So the paragraph after the break is compared with the one before the mark, matches its style and drops its 12 pt space before, which Word keeps. Whichever lands second should leave a section's empty closing mark to the normal path, or set `pb.prev` for it in the framed path as #5455 does.
- Left out of *Merge next* on purpose: #2792 (see *Combined branch*).

**Coverage:** 58 PRs benched (34 change the score), 0 of them stale; 163 queued for the
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

<details><summary><b>Every PR that changes the score (34)</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Head, measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #4316 | dotCooCoo | Proofing: hide spelling or grammar errors in this document only | +1.247 | +1.070 | +0 | 119 (98↑ 11↓) | table-wrap-indent-inline-i5100-r0 +60.0, table-wrap-indent-inline-i5100-r240 +59.3, case211 +43.6 (+95 more) | case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7 (+8 more) | `4eeac27b3` on `e9750c5cb`, today |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | +0.807 | +0.799 | +1 | 43 (29↑ 12↓) | frame-float-clearance-f1-y1000-h700 +83.8, frame-float-clearance-f0-y400-h400 +80.5, frame-float-clearance-f1-y400-h700 +77.9 (+26 more) | frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0 (+9 more) | `5ae458526` on `e9750c5cb`, today |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | +0.373 | +0.243 | +0 | 25 (16↑ 2↓) | nested-autofit-padding-d3-p108-w4200 +48.4, nested-autofit-padding-d1-p108-w4200 +48.3, nested-autofit-padding-d1-p108-w6000 +45.8 (+13 more) | case91 -8.6, case89 -8.5 | `de04a1fc7` on `e9750c5cb`, today |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | +0.270 | +0.180 | +0 | 10 (8↑ 2↓) | negative-x-nested-x-142-y1-w4820-n4 +52.7, negative-x-nested-x142-y-33-w4820-n0 +48.2, nested-final-mark-w5100-y1-h400-n1 +47.8 (+5 more) | nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8 | `7207e8835` on `e9750c5cb`, today |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | +0.195 | +0.361 | +0 | 10 (9↑ 1↓) | shifted-text-position-7-mixed0-mark1 +50.7, shifted-text-position-7-mixed0-mark0 +50.7, raised-empty-size12-position7-count2 +35.3 (+6 more) | czech_municipal_grant_form -7.8 | `417337bb4` on `e9750c5cb`, today |
| #2552 | naxvog | Layout: a left tab whose text doesn't fit moves to the next line with it (#2531) | +0.134 | +0.109 | +0 | 5 (5↑ 0↓) | leading-tab-four-tabs +47.1, leading-tab-two-tabs +46.5, leading-tab-visible-prefix +38.1 (+2 more) | – | `09bea6e3a` on `e9750c5cb`, today |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | +0.086 | +0.100 | +0 | 3 (3↑ 0↓) | continuous-context-frame1-same1-ctx1 +48.3, continuous-context-frame0-same1-ctx1 +28.5, continuous-context-after-same1-ctx1 +28.5 | – | `dce01cdd7` on `e9750c5cb`, today |
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | +0.074 | +0.069 | +0 | 9 (7↑ 2↓) | case49 +43.4, case4 +39.6, border-group-between-rule-fill +30.3 (+4 more) | lithuanian_excise_tax_amendment -30.7, text_align_center_mixed -0.8 | `dd4ef8d0f` on `e9750c5cb`, today |
| #2463 | Nghiathan13 | Layout: a paragraph-anchored floating table that doesn't fit runs on across pages (#2359) | +0.048 | +0.050 | +1 | 5 (2↑ 2↓) | croatian_grant_guidelines +48.0, indigenous_innovation_sandbox_agreement +37.6 | pendulum_mechanics_oscillation_lab -25.4, line-anchor-overrides -1.6 | `a7ca977ee` on `e9750c5cb`, today |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | +0.045 | +0.048 | +0 | 5 (5↑ 0↓) | short-cell-widows-m14-l3-room2-w1-none +29.7, advocacy_initiative_newsletter_2013 +15.3, toc_pageref_after_tall_table +8.5 (+2 more) | – | `979077101` on `e9750c5cb`, today |
| #5457 | naxvog | Layout: a hidden end-of-cell mark after a closing line break takes no room | +0.038 | +0.048 | +0 | 5 (4↑ 1↓) | nested-first-row-prefix300-cant0 +22.0, nested-first-row-prefix330-cant0 +14.2, nested-first-row-prefix330-cant1 +5.9 (+1 more) | maine_criminal_history_record -1.7 | `841d4c0e2` on `e9750c5cb`, today |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | +0.035 | +0.033 | +0 | 1 (1↑ 0↓) | ut_koer_annual_meeting_minutes +43.3 | – | `7e86e2ea5` on `e9750c5cb`, today |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | +0.027 | +0.023 | +0 | 2 (1↑ 0↓) | zimbabwe_gold_mining_judgment +32.4 | – | `7fce65fcc` on `e9750c5cb`, today |
| #2493 | finwarman | Close split table fragments at fitted content | +0.015 | +0.012 | +0 | 15 (5↑ 0↓) | master_thesis_learning_agreement +10.7, table-row-split-lines +2.6, cote_dazur_phd_grants_call +1.4 (+2 more) | – | `a4f4b668b` on `e9750c5cb`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | +0.012 | +0.000 | +0 | 1 (1↑ 0↓) | japanese_hr_consultation_application +14.8 | – | `c14375951` on `e9750c5cb`, today |
| #2465 | finwarman | Retain minimum heights on split-row continuations | +0.010 | +0.009 | +0 | 2 (2↑ 0↓) | master_thesis_learning_agreement +10.4, table-row-split-lines +1.9 | – | `06741cf45` on `e9750c5cb`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | +0.007 | +0.004 | +0 | 7 (2↑ 0↓) | paragraph-border-styles +6.6, cell-paragraph-bottom-wide +1.1 | – | `8c689e973` on `e9750c5cb`, today |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | +0.006 | +0.006 | +1 | 1 (1↑ 0↓) | carbon_farming_initiative_rule +7.6 | – | `02b9edd57` on `e9750c5cb`, today |
| #2674 | finwarman | Reserve font math leading in equation line metrics | +0.005 | -0.001 | +0 | 2 (1↑ 1↓) | case221 +8.0 | pendulum_mechanics_oscillation_lab -1.8 | `8812f4d7d` on `e9750c5cb`, today |
| #2508 | Nghiathan13 | Layout: field results mixing scripts draw each glyph in its own face (#2491) | +0.004 | +0.003 | +0 | 5 (2↑ 1↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3 | field-result-formatting -0.9 | `8ff2fe54a` on `e9750c5cb`, today |
| #3588 | dpkruse | #3585: automatic text is white on dark cell and paragraph shading | +0.001 | +0.000 | +0 | 2 (1↑ 0↓) | radiographer_interventional_job_desc +1.8 | – | `cb6a1bde0` on `e9750c5cb`, today |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | +0.001 | +0.001 | +0 | 4 (1↑ 0↓) | through-picture-columns +0.7 | – | `05fbde50f` on `e9750c5cb`, today |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `69578bbc6` on `e9750c5cb`, today |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `3d04c471a` on `e9750c5cb`, today |
| #2533 | finwarman | Fit floating text box frames to their content | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | tab-only-line-own-font +0.8 | – | `8073a9009` on `e9750c5cb`, today |
| #2488 | Nghiathan13 | Layout: In Front of Text objects draw over the whole page's text (#1993) | +0.001 | +0.002 | +0 | 3 (1↑ 0↓) | text-box-story-pictures +0.6 | – | `732bb67be` on `e9750c5cb`, today |
| #3462 | midasdf | Layout: hanging punctuation (overflowPunct) and line-start punctuation compression (topLinePunct) | +0.000 | +0.001 | +0 | 2 (0↑ 0↓) | – | – | `cb235350e` on `e9750c5cb`, today |
| #2454 | finwarman | Fix automatic leading on picture-only lines | +0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `3411f542d` on `e9750c5cb`, today |
| #2662 | finwarman | Respect the font minimum height for display operators | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `d4b9c5865` on `e9750c5cb`, today |
| #1486 | dfgodvan | Tables: a page break inside a vertical merge takes the merged cell's text along (#1485) | -0.001 | -0.002 | +0 | 1 (0↑ 1↓) | – | go_math_grade4_guide -1.6 | `94f87a146` on `e9750c5cb`, today |
| #2709 | finwarman | Honor complete rounded percentage cell widths | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | primary_care_safeguarding_annual_review -2.5 | `40afc9b79` on `e9750c5cb`, today |
| #3559 | MichaelMuClaude | Tables: an older-mode table moves out by its default cell margin, not the first cell's own (#3407) | -0.005 | -0.004 | +0 | 1 (0↑ 1↓) | – | candidate_reference_check_form -5.6 | `37d524030` on `e9750c5cb`, today |
| #2502 | midasmatterhorn | Layout: a square-wrapped logo in the default header is drawn and pushes the body down | -0.007 | -0.016 | +0 | 3 (1↑ 2↓) | czech_municipal_grant_form +10.7 | cote_dazur_phd_grants_call -17.1, bosch_software_ai_announcement -2.3 | `9de723f64` on `e9750c5cb`, today |
| #2604 | finwarman | Choose justified breaks by spacing cost | -0.016 | -0.012 | +0 | 5 (2↑ 2↓) | squeeze-lead-space +23.0, squeeze-threshold-after-space +3.9 | czech_village_budget_commentary -43.9, squeeze-keep-slack -2.5 | `4f6ea07aa` on `e9750c5cb`, today |

**Benched, no change on the suite (24):** #6003, #1713, #1715, #2064, #2117, #2345, #2356, #2496, #2514, #2711, #2817, #3022, #3148, #3198, #3332, #3472, #3878, #3935, #4089, #4134, #4183, #4260, #4278, #4338. These may
still be right; the suite just has no document that exercises them.

</details>

## Combined branch

**Every PR with a positive score**: 16 PRs merged into `main` e9750c5cb in this order, at these heads (merge commit `51336f2a7`, made in the bench job and not pushed): #4316 `4eeac27b3`, #2523 `5ae458526`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #2552 `09bea6e3a`, #5455 `dce01cdd7`, #2463 `a7ca977ee`, #3823 `7e86e2ea5`, #4065 `7fce65fcc`, #2834 `c14375951`, #2465 `06741cf45`, #1757 `8c689e973`, #3604 `02b9edd57`, #2674 `8812f4d7d`, #4186 `05fbde50f`. Left out: code conflict with PRs merged before it: #1172, #3833, #5457, #2493, #2508, #3588, #3834, #3832, #2533, #2488.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` e9750c5cb | 73.27 | 55.47 | 1181/1220 | 93.3 |
| combined | 76.42 (+3.147) | 58.38 (+2.909) | 1184/1220 (+3) | 93.5 (+0.22) |

The merged PRs' individual SSIM changes add up to +3.264; the difference to the combined +3.147 is where
they overlap or interact. 222 fixtures change (170↑ 26↓). Regressions over 0.5: continuous-context-frame1-same0-ctx1 -47.1, frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0, pendulum_mechanics_oscillation_lab -25.4, empty-margin-frame-15-one-empty -11.1, nested-adjacent-negative-large-offset -10.5, empty-margin-frame-15-two-empty -10.5 (+18 more).

**The same without #2792**: 16 PRs merged into `main` e9750c5cb in this order, at these heads (merge commit `e03484345`, made in the bench job and not pushed): #4316 `4eeac27b3`, #2523 `5ae458526`, #5443 `de04a1fc7`, #5458 `7207e8835`, #5439 `417337bb4`, #2552 `09bea6e3a`, #5455 `dce01cdd7`, #2463 `a7ca977ee`, #3823 `7e86e2ea5`, #4065 `7fce65fcc`, #2834 `c14375951`, #2465 `06741cf45`, #1757 `8c689e973`, #3604 `02b9edd57`, #2674 `8812f4d7d`, #4186 `05fbde50f`. Left out: code conflict with PRs merged before it: #1172, #3833, #5457, #2493, #2508, #3588, #3834, #3832, #2533, #2488; left out on purpose: #2792.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` e9750c5cb | 73.27 | 55.47 | 1181/1220 | 93.3 |
| combined | 76.42 (+3.147) | 58.38 (+2.909) | 1184/1220 (+3) | 93.5 (+0.22) |

The merged PRs' individual SSIM changes add up to +3.264; the difference to the combined +3.147 is where
they overlap or interact. 222 fixtures change (170↑ 26↓). Regressions over 0.5: continuous-context-frame1-same0-ctx1 -47.1, frame-balanced-columns -41.3, frame-moved-space-before -29.8, case128 -26.0, pendulum_mechanics_oscillation_lab -25.4, empty-margin-frame-15-one-empty -11.1, nested-adjacent-negative-large-offset -10.5, empty-margin-frame-15-two-empty -10.5 (+18 more).

## Not benched

- **Code conflicts with `main`** (473 PRs): not rerun until rebased.
- **Change no rendering file** (228): not benched.
- **Doesn't build once merged with `main`:** #1303, #2512, #3160, #4339.
- **Removed from this list** since they're no longer open: none.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).


This issue tracks how close WordCraft's DOCX → PDF output is to Word's, measured with the
[docxide-pdf](https://github.com/sverrejb/docxide-pdf) test suite, and what each open PR that touches layout,
rendering, fonts, DOCX reading or PDF export does to that score. It's regenerated as benches finish; last updated 2026-11-09 05:14 UTC.

## Summary for reviewers

`main` 7b8c0ba5e scores **73.70** SSIM against Word's PDFs; docxide-pdf, in the same setup, scores 87.34
(13.6 points ahead). Merging the 21 PRs below, in this order, gives **77.43 (+3.73)**,
measured on one branch with all of them merged (see *Combined branch*).

### Merge next

Ranked by what each adds on its own; they merge cleanly with `main` and with each other in this order. A row marked
stale was measured before the PR got new commits, or before `main` changed files it changes too; it's rerun in the
next round.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3821 | naxvog | Tables: a file with no default table style gives its tables no cell margins | **+1.361** | 88↑ 11↓ | case91 -6.2 | ✅ | – | +88 −4 | `661a79054`, today |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | **+0.916** | 23↑ 6↓ | case128 -26.0 | ✅ | – | +675 −39 | `661a79054`, today ⚠ stale: main changed para.rs |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | **+0.425** | 16↑ 2↓ | case91 -8.6 | ✅ | – | +231 −13 | `4b0d39959`, today |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | **+0.307** | 8↑ 2↓ | nested-adjacent-negative-large-offset -10.5 | ✅ | – | +161 −7 | `4b0d39959`, today |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | **+0.220** | 8↑ 1↓ | czech_municipal_grant_form -7.8 | ✅ | – | +135 −10 | `e0d8312fb`, today |
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | **+0.153** | 6↑ 1↓ | continued-gap-cell-after0-before4 -2.8 | ✅ | changes requested | +72 −8 | `661a79054`, today |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | **+0.141** | 3↑ 0↓ | – | ✅ | – | +470 −7 | `661a79054`, today |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | **+0.098** | 3↑ 0↓ | – | ✅ | – | +198 −2 | `661a79054`, today |
| #5887 | batistalucasv | Layout: a justified line with a tab shrinks the spaces after its last tab (#5847) | **+0.055** | 6↑ 0↓ | – | ✅ | – | +336 −21 | `729cd0a5f`, 2 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | **+0.040** | 1↑ 0↓ | – | ✅ | – | +200 −8 | `661a79054`, today |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | **+0.030** | 1↑ 0↓ | – | ✅ | – | +123 −16 | `661a79054`, today |
| #2834 | finwarman | Keep empty row continuations with their labels | **+0.014** | 1↑ 0↓ | – | ✅ | – | +506 −5 | `661a79054`, today ⚠ stale: main changed table.rs |
| #2465 | finwarman | Retain minimum heights on split-row continuations | **+0.010** | 1↑ 0↓ | – | ✅ | changes requested | +179 −14 | `7b8c0ba5e`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | **+0.008** | 2↑ 0↓ | – | ✅ | – | +147 −54 | `4b0d39959`, today |
| #5850 | batistalucasv | layout: wrap field results across multiple lines within margins (#5838) | **+0.006** | 4↑ 0↓ | – | ✅ | changes requested | +795 −50 | `661a79054`, today ⚠ stale: main changed para.rs, para/paragraph.rs |
| #2674 | finwarman | Reserve font math leading in equation line metrics | **+0.006** | 1↑ 1↓ | pendulum_mechanics_oscillation_lab -1.8 | ✅ | – | +229 −9 | `e919982fa`, 3 d ago ⚠ stale: main changed math.rs |
| #4614 | dfgodvan | Layout: a right tab past the right indent takes its text up to the stop, as in Word | **+0.002** | 3↑ 1↓ | carbon_farming_initiative_rule -1.3 | ✅ | – | +65 −5 | `661a79054`, today |
| #5339 | MichaelMuClaude | A DOCX drop cap's letter takes the text's size instead of being scaled twice (#5294) | **+0.001** | 1↑ 0↓ | – | ✅ | changes requested | +34 −2 | `729cd0a5f`, 2 d ago |
| #5074 | pakiat | Tables: percentage cell widths size their columns whichever rows give them | **+0.001** | 0↑ 0↓ | – | ✅ | – | +341 −7 | `661a79054`, today ⚠ stale: main changed table.rs |
| #4846 | jpc7k1 | Layout: with useFELayout + balanceSingleByteDoubleByteWidth, runs of spaces take the East Asian space width | **+0.001** | 1↑ 0↓ | – | ✅ | – | +110 −2 | `661a79054`, today ⚠ stale: main changed para/paragraph.rs |
| #2608 | finwarman | Honor row table cell margin exceptions | **+0.001** | 1↑ 0↓ | – | ✅ | – | +261 −12 | `661a79054`, today ⚠ stale: main changed table.rs |

### Needs a look

PRs above that also make a fixture worse by more than 5 SSIM points, and interactions between PRs:

- **#3821** (naxvog): case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7, nested_table_center_positive -1.7 (+7 more)
- **#2523** (D13GOOOO): case128 -26.0, empty-margin-frame-15-one-empty -11.1, empty-margin-frame-15-two-empty -10.5, empty-margin-frame-15-two-space-only -10.5 (+2 more)
- **#5443** (naxvog): case91 -8.6, case89 -8.5
- **#5458** (naxvog): nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8
- **#5439** (naxvog): czech_municipal_grant_form -7.8
- **Interaction found:** #3821 and #2792 together drop the six `nested-floats-spaced-text-*` fixtures from 92.5 to 31.2 SSIM; neither changes them alone (found by merging prefixes of the list above). #2792 reads a `w:tblCellMar` that sets only some sides into `partial_cell_margins` and leaves `cell_margins` empty; #3821 then sees no `cell_margins` in a file without a default table style and sets all four to 0, which overrides the sides the table does set. Whichever lands second should check `partial_cell_margins` too and fill only the missing sides with 0.
- Left out of *Merge next* on purpose: #2792 (see *Combined branch*).

### Would help, needs a rebase

These raised the score when they were benched, but now conflict with `main` in code.

| PR | Author | What it changes | SSIM Δ | Fixtures | Worst fixture | CI | Review | Size | Measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3787 | cyril265 | Layout: a page break at the end of the document or of a section starts no blank page | **+0.105** | 2↑ 0↓ | – | ✅ | – | +611 −30 | `e919982fa`, 3 d ago ⚠ stale: main changed ctx.rs, flow.rs |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | **+0.079** | 3↑ 0↓ | – | ✅ | – | +482 −47 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs |
| #4845 | jpc7k1 | Layout: a justified line with a tab shrinks the spaces after its last tab, as Word does | **+0.054** | 5↑ 0↓ | – | ✅ | – | +66 −18 | `e919982fa`, 3 d ago ⚠ stale: main changed para/lines.rs |
| #3790 | cyril265 | Layout: text before a floating table or shape on its page wraps around it | **+0.050** | 2↑ 0↓ | – | ✅ | – | +1545 −75 | `e919982fa`, 3 d ago ⚠ stale: main changed ctx.rs, floats.rs, flow.rs … |
| #2047 | finwarman | Layout: keep picture-only anchors with their pictures | **+0.031** | 2↑ 0↓ | – | ✅ | – | +586 −8 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | **+0.029** | 3↑ 0↓ | – | ✅ | – | +225 −3 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, para/paragraph.rs, table_flow.rs |
| #4619 | Harrison-Booth | Fonts: report a missing Word core font with no metric twin | **+0.024** | 1↑ 0↓ | – | ✅ | – | +119 −15 | `e919982fa`, 3 d ago ⚠ stale: main changed word.rs |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | **+0.007** | 1↑ 0↓ | – | ✅ | – | +95 −17 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, para.rs |
| #4460 | fluorine | Critical batch: some approved, CI-green PRs merged together | **+0.002** | 2↑ 0↓ | – | ✅ | – | +4851 −354 | `729cd0a5f`, 2 d ago ⚠ stale: main changed read/props.rs, write/props.rs, write/story/drawing.rs … |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | **+0.001** | 1↑ 0↓ | – | ✅ | – | +157 −2 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | **+0.001** | 1↑ 0↓ | – | ✅ | – | +192 −3 | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #5562 | Znerual | Layout: a footnote mark stays with the text before it (#5402) | **+0.001** | 1↑ 0↓ | – | ✅ | – | +272 −6 | `e919982fa`, 3 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs, para/paragraph.rs |

**Coverage:** 325 PRs benched (74 change the score), 193 of them stale; 50 queued for the
next round; 100 waiting for a person to look before they're built; 391 conflict with `main`.

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
  seeing the suite read-only. PRs from authors without a merged PR, and PRs that add build scripts, proc macros,
  cargo config or dependencies, wait until someone has read the diff.
- **Environment:** Linux container, debug build of `wordcraft-cli` (the layout code is the same as release), fonts
  from Debian packages plus Microsoft's core web fonts. Calibri, Cambria, Aptos and the other Office fonts are
  not installed, so WordCraft draws those documents in metric-compatible substitutes (Carlito, Caladea, …) while
  Word's references use the originals. docxide-pdf runs in the same container without its private font set.

| `main` 7b8c0ba5e | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| WordCraft | 73.70 | 56.17 | 1044/1073 | 93.2 |
| docxide-pdf (for reference) | 87.34 | 70.90 | 1055/1073 | 93.9 |

</details>

<details><summary><b>Every PR that changes the score (74)</b></summary>

Sorted by SSIM change. The sum of these rows is not what all of them together would give: several touch the
same fixtures (see *Combined branch*).

| PR | Author | What it changes | SSIM Δ | Jaccard Δ | Pages Δ | Fixtures changed | Biggest gains | Regressions | Measured on `main` |
|---|---|---|---|---|---|---|---|---|---|
| #3821 | naxvog | Tables: a file with no default table style gives its tables no cell margins | +1.361 | +1.155 | +0 | 102 (88↑ 11↓) | table-wrap-indent-inline-i5100-r0 +60.0, table-wrap-indent-inline-i5100-r240 +59.3, case211 +43.6 (+85 more) | case91 -6.2, case89 -5.6, nested_table_bottom_positive -1.7 (+8 more) | `661a79054`, today |
| #2523 | D13GOOOO | Text frames in the body go where their frame puts them (#2406) | +0.916 | +0.890 | +0 | 30 (23↑ 6↓) | frame-float-clearance-f1-y1000-h700 +83.8, frame-float-clearance-f0-y400-h400 +80.5, frame-float-clearance-f1-y400-h700 +77.9 (+20 more) | case128 -26.0, empty-margin-frame-15-one-empty -11.1, empty-margin-frame-15-two-empty -10.5 (+3 more) | `661a79054`, today ⚠ stale: main changed para.rs |
| #5443 | naxvog | Tables: a nested table in an older-mode document keeps its edge at its cell's text | +0.425 | +0.277 | +0 | 25 (16↑ 2↓) | nested-autofit-padding-d3-p108-w4200 +48.4, nested-autofit-padding-d1-p108-w4200 +48.3, nested-autofit-padding-d1-p108-w6000 +45.8 (+13 more) | case91 -8.6, case89 -8.5 | `4b0d39959`, today |
| #5458 | naxvog | Layout: a cell's end mark below its floating table adds no line, as in Word | +0.307 | +0.205 | +0 | 10 (8↑ 2↓) | negative-x-nested-x-142-y1-w4820-n4 +52.7, negative-x-nested-x142-y-33-w4820-n0 +48.2, nested-final-mark-w5100-y1-h400-n1 +47.8 (+5 more) | nested-adjacent-negative-large-offset -10.5, nested-adjacent-negative-positive -7.8 | `4b0d39959`, today |
| #5439 | naxvog | Layout: a raised or lowered run moves its line's box instead of growing it | +0.220 | +0.409 | +0 | 9 (8↑ 1↓) | shifted-text-position-7-mixed0-mark1 +50.7, shifted-text-position-7-mixed0-mark0 +50.7, raised-empty-size12-position7-count2 +35.3 (+5 more) | czech_municipal_grant_form -7.8 | `e0d8312fb`, today |
| #5808 | kevinj24fr | Layout: an exactly spaced line puts its baseline 0.8 of its height down | +0.153 | +0.101 | +0 | 15 (6↑ 1↓) | nested-table-keep-next +53.8, heading-keep-next-exact +52.1, keep-next-inline-image +44.5 (+3 more) | continued-gap-cell-after0-before4 -2.8 | `661a79054`, today |
| #4840 | ro-legal-docx | Layout: continue oversized cantSplit rows across pages | +0.141 | +0.128 | +3 | 3 (3↑ 0↓) | modern-oversized-lines55-cant1-prefix0 +60.7, modern-oversized-lines55-cant1-prefix330 +45.5, modern-oversized-lines55-cant1-prefix160 +45.5 | – | `661a79054`, today |
| #3787 | cyril265 | Layout: a page break at the end of the document or of a section starts no blank page | +0.105 | +0.089 | +2 | 2 (2↑ 0↓) | geneva_waste_facility_permit_request +63.4, stem_partnerships_guide +49.3 | – | `e919982fa`, 3 d ago ⚠ stale: main changed ctx.rs, flow.rs |
| #5455 | naxvog | Layout: contextual spacing reaches across a continuous section break, as in Word | +0.098 | +0.114 | +0 | 3 (3↑ 0↓) | continuous-context-frame1-same1-ctx1 +48.3, continuous-context-frame0-same1-ctx1 +28.5, continuous-context-after-same1-ctx1 +28.5 | – | `661a79054`, today |
| #5095 | dfgodvan | Layout: keep with next lets the last line's leading run into the bottom margin, as when the line is placed | +0.079 | +0.065 | +0 | 3 (3↑ 0↓) | case49 +43.4, case4 +39.6, uk_commercial_lease_template +1.6 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs |
| #5887 | batistalucasv | Layout: a justified line with a tab shrinks the spaces after its last tab (#5847) | +0.055 | +0.050 | +0 | 6 (6↑ 0↓) | czech_council_resolutions_2023 +31.3, ukrainian_municipal_heating_resolution +19.2, uk_commercial_lease_template +4.4 (+3 more) | – | `729cd0a5f`, 2 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs |
| #4845 | jpc7k1 | Layout: a justified line with a tab shrinks the spaces after its last tab, as Word does | +0.054 | +0.048 | +0 | 5 (5↑ 0↓) | czech_council_resolutions_2023 +31.5, ukrainian_municipal_heating_resolution +19.5, uk_commercial_lease_template +4.4 (+2 more) | – | `e919982fa`, 3 d ago ⚠ stale: main changed para/lines.rs |
| #1172 | naxvog | Layout: picture-only lines keep no descent, line spacing may hang into the bottom margin, paragraph border groups take between borders and end at page breaks | +0.050 | +0.050 | +0 | 4 (3↑ 1↓) | case49 +43.4, case4 +39.6, uk_commercial_lease_template +1.6 | lithuanian_excise_tax_amendment -30.7 | `4b0d39959`, today |
| #3790 | cyril265 | Layout: text before a floating table or shape on its page wraps around it | +0.050 | +0.019 | +0 | 2 (2↑ 0↓) | full-width-float-empty-anchor +37.5, bosch_software_ai_announcement +15.6 | – | `e919982fa`, 3 d ago ⚠ stale: main changed ctx.rs, floats.rs, flow.rs … |
| #5457 | naxvog | Layout: a hidden end-of-cell mark after a closing line break takes no room | +0.043 | +0.055 | +0 | 5 (4↑ 1↓) | nested-first-row-prefix300-cant0 +22.0, nested-first-row-prefix330-cant0 +14.2, nested-first-row-prefix330-cant1 +5.9 (+1 more) | maine_criminal_history_record -1.7 | `4b0d39959`, today |
| #3823 | naxvog | Layout: in older documents, tabs behind a float keep their text on the row | +0.040 | +0.037 | +0 | 1 (1↑ 0↓) | ut_koer_annual_meeting_minutes +43.3 | – | `661a79054`, today |
| #2047 | finwarman | Layout: keep picture-only anchors with their pictures | +0.031 | +0.026 | +1 | 2 (2↑ 0↓) | indonesian_benchmarking_guide +32.3, brazilian_logistics_study +0.5 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs |
| #4065 | jpc7k1 | Layout: a long note referenced on a paragraph's last lines continues below them, as in Word (#3820) | +0.030 | +0.027 | +0 | 2 (1↑ 0↓) | zimbabwe_gold_mining_judgment +32.4 | – | `661a79054`, today |
| #3833 | dfgodvan | Layout: tables at the foot of a page before Word 2013 layout (compatibility mode 12 and 14) | +0.029 | +0.039 | +0 | 3 (3↑ 0↓) | short-cell-widows-m14-l3-room2-w1-none +29.7, wa_child_services_regulations +0.9, romanian_quality_evaluation_strategy +0.8 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, para/paragraph.rs, table_flow.rs |
| #4619 | Harrison-Booth | Fonts: report a missing Word core font with no metric twin | +0.024 | +0.012 | +1 | 1 (1↑ 0↓) | arabic_rice_benefits_article +25.4 | – | `e919982fa`, 3 d ago ⚠ stale: main changed word.rs |
| #5176 | pakiat | Tables: a percentage-width table before Word 2013 adds its outer cell margins | +0.015 | +0.011 | +0 | 5 (4↑ 0↓) | chinese_costume_design_course +9.2, zimbabwe_broadcasting_corporation_judgment +3.5, zimbabwe_gold_mining_judgment +2.5 (+1 more) | – | `661a79054`, today ⚠ stale: new commits; main changed table.rs |
| #2834 | finwarman | Keep empty row continuations with their labels | +0.014 | +0.000 | +0 | 1 (1↑ 0↓) | japanese_hr_consultation_application +14.8 | – | `661a79054`, today ⚠ stale: main changed table.rs |
| #2465 | finwarman | Retain minimum heights on split-row continuations | +0.010 | +0.008 | +0 | 1 (1↑ 0↓) | master_thesis_learning_agreement +10.4 | – | `7b8c0ba5e`, today |
| #1757 | naxvog | Borders: lines meet in closed corners, as in Word | +0.008 | +0.004 | +0 | 7 (2↑ 0↓) | paragraph-border-styles +6.6, cell-paragraph-bottom-wide +1.1 | – | `4b0d39959`, today |
| #3604 | dpkruse | #3009: a paragraph opening with a page or column break moves once, whatever it keeps | +0.007 | +0.007 | +1 | 1 (1↑ 0↓) | carbon_farming_initiative_rule +7.6 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, para.rs |
| #5850 | batistalucasv | layout: wrap field results across multiple lines within margins (#5838) | +0.006 | +0.005 | +0 | 4 (4↑ 0↓) | clean_energy_regulator_act +2.4, carbon_farming_initiative_rule +2.3, wa_child_services_regulations +0.7 (+1 more) | – | `661a79054`, today ⚠ stale: main changed para.rs, para/paragraph.rs |
| #2674 | finwarman | Reserve font math leading in equation line metrics | +0.006 | -0.002 | +0 | 2 (1↑ 1↓) | case221 +8.0 | pendulum_mechanics_oscillation_lab -1.8 | `e919982fa`, 3 d ago ⚠ stale: main changed math.rs |
| #2792 | finwarman | Inherit omitted table-wide cell margins | +0.004 | +0.003 | +0 | 2 (2↑ 0↓) | english_town_council_report +3.3, maine_criminal_history_record +0.5 | – | `661a79054`, today ⚠ stale: main changed table.rs |
| #4460 | fluorine | Critical batch: some approved, CI-green PRs merged together | +0.002 | +0.002 | +0 | 2 (2↑ 0↓) | case77 +1.2, torture_test +1.0 | – | `729cd0a5f`, 2 d ago ⚠ stale: main changed read/props.rs, write/props.rs, write/story/drawing.rs … |
| #4614 | dfgodvan | Layout: a right tab past the right indent takes its text up to the stop, as in Word | +0.002 | +0.002 | +0 | 5 (3↑ 1↓) | clean_energy_regulator_act +1.3, western_australia_owner_drivers_act +1.2, wa_child_services_regulations +0.9 | carbon_farming_initiative_rule -1.3 | `661a79054`, today |
| #5564 | chamber074 | Draw a picture's outline (Picture Border) on screen and in PDF | +0.001 | +0.000 | +0 | 3 (1↑ 0↓) | case57 +0.8 | – | `e0d8312fb`, today ⚠ stale: new commits; main changed table.rs |
| #5695 | prasertsakd | Add Thai Distributed alignment and capped Thai justification | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `729cd0a5f`, 2 d ago ⚠ stale: new commits; main changed read/props.rs, write/props.rs, kinsoku.rs … |
| #3072 | inmean | Add Thai Distributed and Khmer Justify paragraph alignments | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `661a79054`, today ⚠ stale: main changed lib.rs, para.rs, para/paragraph.rs |
| #5590 | xullul | Home › Paragraph: a Thai Distributed button after Justify | +0.001 | +0.002 | +0 | 1 (1↑ 0↓) | case77 +1.2 | – | `e919982fa`, 3 d ago ⚠ stale: main changed read/props.rs, write/props.rs, xml.rs … |
| #5096 | dfgodvan | Layout: no line break after the '?' of a query, nor after a slash before an underscore | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | erasmus_plus_staff_mobility_agreement +1.0 | – | `661a79054`, today ⚠ stale: main changed para/paragraph.rs |
| #5339 | MichaelMuClaude | A DOCX drop cap's letter takes the text's size instead of being scaled twice (#5294) | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | torture_test +0.9 | – | `729cd0a5f`, 2 d ago |
| #5166 | ro-legal-docx | Layout: keep headings with following inline tables | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `661a79054`, today |
| #3832 | dfgodvan | Layout: a paragraph kept with a table needs its header rows and the start of its first row | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #3834 | dfgodvan | Layout: a paragraph kept with a table counts its space after | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | wa_child_services_regulations +0.9 | – | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, table_flow.rs |
| #4142 | SusieeTheLinuxUser | DOCX: a drop cap's letter takes the text's size back, not the file's enlarged one (#3000) | +0.001 | +0.000 | +0 | 1 (1↑ 0↓) | torture_test +0.7 | – | `661a79054`, today ⚠ stale: main changed para/paragraph.rs |
| #5562 | Znerual | Layout: a footnote mark stays with the text before it (#5402) | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | mongolian_human_rights_law +0.6 | – | `e919982fa`, 3 d ago ⚠ stale: new commits; main changed para.rs, para/lines.rs, para/paragraph.rs |
| #5074 | pakiat | Tables: percentage cell widths size their columns whichever rows give them | +0.001 | +0.000 | +0 | 2 (0↑ 0↓) | – | – | `661a79054`, today ⚠ stale: main changed table.rs |
| #4846 | jpc7k1 | Layout: with useFELayout + balanceSingleByteDoubleByteWidth, runs of spaces take the East Asian space width | +0.001 | +0.001 | +0 | 4 (1↑ 0↓) | japanese_interlibrary_loan +0.7 | – | `661a79054`, today ⚠ stale: main changed para/paragraph.rs |
| #2608 | finwarman | Honor row table cell margin exceptions | +0.001 | +0.001 | +0 | 1 (1↑ 0↓) | maine_criminal_history_record +0.5 | – | `661a79054`, today ⚠ stale: main changed table.rs |
| #3462 | midasdf | Layout: hanging punctuation (overflowPunct) and line-start punctuation compression (topLinePunct) | +0.000 | +0.001 | +0 | 2 (0↑ 0↓) | – | – | `661a79054`, today ⚠ stale: main changed kinsoku.rs, para.rs, para/paragraph.rs |
| #4186 | Silvertree2010 | Draw in-front-of-text pictures above tables laid out after them | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today |
| #5102 | VoiceLessQ | Text boxes keep a line while its text ends inside the box (#5059) | +0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today |
| #2708 | finwarman | Honor nested display fraction sizing | +0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `e919982fa`, 3 d ago ⚠ stale: main changed math.rs |
| #3828 | arc-uri-el | fix(docx): write and read a turned object's effect extent as Word does | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `e919982fa`, 3 d ago ⚠ stale: main changed read/story/drawing.rs, write/embed.rs, write/story/drawing.rs |
| #4867 | cyfung1031 | #4859: multiple line spacing on a document grid | +0.000 | +0.001 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today |
| #4638 | arcanii | Fonts: Japanese text falls back to a Japanese font, not a Chinese one | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today |
| #5129 | pakiat | Fields: PDFs and prints show body PAGEREF pages, as Word fills them in | +0.000 | +0.000 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today ⚠ stale: new commits; main changed fields.rs, lib.rs, para/paragraph.rs |
| #5252 | scks1 | Layout: a continuous section after a page break and an empty closing mark starts the new page (#2109) | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `e919982fa`, 3 d ago ⚠ stale: new commits; main changed flow.rs, page.rs, pass.rs |
| #2662 | finwarman | Respect the font minimum height for display operators | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `e919982fa`, 3 d ago |
| #3217 | MichaelMuClaude | A display operator without a cataloged size variant still enlarges (#3208) | -0.000 | -0.001 | +0 | 1 (0↑ 0↓) | – | – | `e919982fa`, 3 d ago |
| #5634 | kennyfs | Layout: turned cell text never makes a row taller, as in Word | -0.000 | +0.002 | +0 | 1 (0↑ 0↓) | – | – | `e0d8312fb`, today ⚠ stale: main changed table.rs |
| #5735 | benandez | Watermark: picture watermarks and transparency (#3001) | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `729cd0a5f`, 2 d ago ⚠ stale: main changed read/parts.rs, read/story/runs.rs, read/story/vml.rs … |
| #5935 | frandavid100 | layout: reserve table footnotes before fitting row fragments | -0.000 | -0.000 | +0 | 1 (0↑ 0↓) | – | – | `661a79054`, today ⚠ stale: main changed table.rs |
| #5313 | Harrison-Booth | Preserve table cell diagonal borders | -0.001 | -0.001 | +0 | 3 (0↑ 1↓) | – | italian_academic_cv_form -0.8 | `661a79054`, today ⚠ stale: main changed table.rs |
| #1486 | dfgodvan | Tables: a page break inside a vertical merge takes the merged cell's text along (#1485) | -0.001 | -0.001 | +0 | 1 (0↑ 1↓) | – | go_math_grade4_guide -1.6 | `4b0d39959`, today |
| #4558 | ro-legal-docx | Borders: preserve dashSmallGap and align border previews | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | paragraph-border-styles -2.2 | `661a79054`, today |
| #542 | krinry | feat(shapes): full Office shapes gallery and canvas drag-to-draw tool | -0.002 | -0.003 | +0 | 3 (1↑ 2↓) | case34 +1.1 | case35 -1.8, japanese_land_development_sign_form -1.3 | `4b0d39959`, today |
| #5181 | pakiat | Tables: a percentage-width table from Word 2013 takes its share after its outer borders | -0.002 | -0.000 | +0 | 5 (3↑ 1↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.7 | italian_project_proposal -6.8 | `661a79054`, today ⚠ stale: new commits; main changed table.rs |
| #6002 | pakiat | Tables: right-to-left start edges, mode 14 end edges and style parts' inner lines as Word | -0.002 | -0.000 | +0 | 5 (3↑ 1↓) | traditional_skills_job_form +3.0, czech_wastewater_discharge_permit +1.1, polish_ministry_accessibility_report +0.7 | italian_project_proposal -6.8 | `661a79054`, today ⚠ stale: new commits; main changed table.rs |
| #2709 | finwarman | Honor complete rounded percentage cell widths | -0.002 | -0.001 | +0 | 2 (0↑ 1↓) | – | primary_care_safeguarding_annual_review -2.5 | `661a79054`, today ⚠ stale: main changed table.rs |
| #5630 | kennyfs | Layout: a table in a text frame floats where the frame says | -0.002 | -0.001 | +0 | 1 (0↑ 1↓) | – | massachusetts_community_sanitation -2.4 | `e919982fa`, 3 d ago ⚠ stale: new commits; main changed boxes.rs, ctx.rs, page.rs … |
| #4564 | OPUZZLES | Tables: keep fitting hanging-indent labels at their grid width | -0.004 | -0.003 | +0 | 1 (0↑ 1↓) | – | australian_higher_education_guidelines -4.5 | `661a79054`, today ⚠ stale: main changed table.rs |
| #3559 | MichaelMuClaude | Tables: an older-mode table moves out by its default cell margin, not the first cell's own (#3407) | -0.005 | -0.005 | +0 | 1 (0↑ 1↓) | – | candidate_reference_check_form -5.6 | `661a79054`, today ⚠ stale: main changed table.rs |
| #2714 | finwarman | Preserve equation size and superscript ink bounds | -0.013 | -0.003 | +0 | 1 (0↑ 1↓) | – | pendulum_mechanics_oscillation_lab -13.6 | `661a79054`, today |
| #4864 | cyfung1031 | Read w:textAlignment and w:adjustLineHeightInTable; honour the grid in table cells | -0.026 | +0.003 | +0 | 4 (1↑ 2↓) | physical_therapy_comparison_table +58.4 | center-body-list-height-center-space0 -43.3, center-body-list-height-center-space1 -42.8 | `e0d8312fb`, today ⚠ stale: main changed display/lines.rs, para.rs |
| #2604 | finwarman | Choose justified breaks by spacing cost | -0.037 | -0.036 | +0 | 3 (1↑ 1↓) | squeeze-threshold-after-space +3.9 | czech_village_budget_commentary -43.9 | `661a79054`, today ⚠ stale: main changed para.rs |
| #1630 | Morzilla | Tables without w:tblGrid take their grid from the cells, and widths wider than the page are squeezed like Word | -0.038 | -0.034 | +0 | 3 (0↑ 3↓) | – | parish_housing_data_profile -35.9, victorian_universal_design_policy -2.7, russian_construction_org_council_minutes -2.0 | `4b0d39959`, today |
| #4436 | dfgodvan | Layout: line height of an inline picture in multiple line spacing, as in Word | -0.044 | +0.070 | -2 | 21 (7↑ 5↓) | picture-mark-leading-compat15-line480 +42.8, czech_village_budget_commentary +22.1, brazilian_logistics_study +22.0 (+4 more) | picture-mark-leading-mark22-line360-text0 -41.2, picture-mark-leading-compat14-line480 -39.3, picture-mark-leading-mark28-line480-text0 -39.3 (+2 more) | `e919982fa`, 3 d ago ⚠ stale: main changed flow.rs, para/lines.rs |
| #2578 | finwarman | Reserve page-colour clearance in initial header stories | -0.113 | -0.090 | -1 | 2 (0↑ 2↓) | – | traditional_skills_job_form -65.5, czech_village_council_minutes_2025 -55.8 | `e919982fa`, 3 d ago ⚠ stale: main changed page.rs, pass.rs |

**Benched, no change on the suite (251):** #4635, #4652, #5349, #6003, #1123, #1217, #1278, #1303, #1713, #1715, #1791, #1838, #1928, #1931, #1952, #2022, #2056, #2063, #2064, #2117, #2120, #2141, #2288, #2340, #2345, #2356, #2372, #2384, #2455, #2473, #2586, #2642, #2643, #2655, #2664, #2703, #2719, #2732, #2733, #2817, #2901, #2995, #3022, #3077, #3089, #3148, #3198, #3200, #3309, #3332, #3388, #3404, #3465, #3472, #3506, #3778, #3788, #3825, #3829, #3878, #3884, #3933, #3935, #3960, #3961, #3965, #3972, #3980, #3993, #4089, #4134, #4183, #4214, #4260, #4266, #4278, #4316, #4320, #4321, #4322, #4338, #4353, #4393, #4407, #4413, #4437, #4443, #4445, #4473, #4474, #4483, #4504, #4521, #4532, #4571, #4580, #4582, #4615, #4625, #4631, #4642, #4647, #4655, #4656, #4688, #4703, #4709, #4714, #4716, #4717, #4719, #4723, #4737, #4747, #4766, #4773, #4781, #4783, #4786, #4791, #4795, #4797, #4826, #4836, #4839, #4849, #4852, #4856, #4860, #4874, #4901, #4905, #4932, #4934, #4972, #4993, #5007, #5013, #5015, #5020, #5024, #5041, #5061, #5067, #5073, #5076, #5098, #5112, #5113, #5153, #5158, #5159, #5170, #5172, #5177, #5200, #5209, #5228, #5251, #5254, #5259, #5283, #5293, #5312, #5314, #5331, #5351, #5357, #5362, #5378, #5386, #5387, #5390, #5407, #5422, #5427, #5435, #5447, #5451, #5461, #5483, #5494, #5500, #5516, #5521, #5541, #5545, #5557, #5560, #5565, #5576, #5599, #5600, #5613, #5616, #5628, #5631, #5638, #5639, #5651, #5665, #5670, #5675, #5702, #5703, #5705, #5721, #5731, #5737, #5738, #5764, #5767, #5772, #5778, #5779, #5789, #5791, #5810, #5820, #5823, #5831, #5852, #5859, #5864, #5869, #5870, #5872, #5880, #5881, #5882, #5885, #5888, #5889, #5891, #5901, #5907, #5916, #5917, #5918, #5940, #5950, #5951, #5953, #5954, #5968, #5969, #5971, #5980, #5986, #5991, #5992. These may
still be right; the suite just has no document that exercises them.

</details>

## Combined branch

**Every PR with a positive score**: 21 PRs merged into `main` 7b8c0ba5e: #3821, #2523, #5443, #5458, #5439, #5808, #4840, #5455, #5887, #3823, #4065, #2834, #2465, #1757, #5850, #2674, #2792, #4614, #5339, #5074, #4846. Left out: code conflict with `main`: #2047, #3604, #3787, #3790, #3832, #3833, #3834, #4460, #4619, #4845, #5095, #5562; code conflict with PRs merged before it: #1172, #5457, #5176, #3072, #5096, #4142, #2608; doesn't compile with the PRs merged before it: #5166; waiting for a look before it is built: #5564, #5590, #5695.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 7b8c0ba5e | 73.70 | 56.17 | 1044/1073 | 93.2 |
| combined | 76.46 (+2.765) | 58.88 (+2.704) | 1047/1073 (+3) | 93.4 (+0.24) |

The merged PRs' individual SSIM changes add up to +3.797; the difference to the combined +2.765 is where
they overlap or interact. 222 fixtures change (162↑ 39↓). Regressions over 0.5: nested-floats-spaced-text-long-one -62.9, nested-floats-spaced-text-bottom-cell -61.8, nested-floats-spaced-text-long-two -61.8, nested-floats-spaced-text-nonzero-x -61.8, nested-floats-spaced-text-inline-reference -60.6, nested-floats-spaced-text-short-spacers -58.8, section-mark-after-table-inline-compat15 -53.6, section-mark-after-table-float-compat15 -51.4 (+31 more).

**The same without #2792**: 21 PRs merged into `main` 7b8c0ba5e: #3821, #2523, #5443, #5458, #5439, #5808, #4840, #5455, #5887, #3823, #4065, #2834, #2465, #1757, #5850, #2674, #4614, #5339, #5074, #4846, #2608. Left out: code conflict with `main`: #2047, #3604, #3787, #3790, #3832, #3833, #3834, #4460, #4619, #4845, #5095, #5562; code conflict with PRs merged before it: #1172, #5457, #5176, #3072, #5096, #4142; doesn't compile with the PRs merged before it: #5166; waiting for a look before it is built: #5564, #5590, #5695; left out on purpose: #2792.

| | SSIM | Jaccard | Pages matching | Line match |
|---|---|---|---|---|
| `main` 7b8c0ba5e | 73.70 | 56.17 | 1044/1073 | 93.2 |
| combined | 77.43 (+3.731) | 59.58 (+3.406) | 1047/1073 (+3) | 93.6 (+0.44) |

The merged PRs' individual SSIM changes add up to +3.794; the difference to the combined +3.731 is where
they overlap or interact. 206 fixtures change (166↑ 19↓). Regressions over 0.5: continuous-context-frame1-same0-ctx1 -47.1, case128 -26.0, empty-margin-frame-15-one-empty -11.1, nested-adjacent-negative-large-offset -10.5, empty-margin-frame-15-two-empty -10.5, empty-margin-frame-15-two-space-only -10.5, empty-margin-frame-visible-body-before-frame -8.0, nested-adjacent-negative-positive -7.8 (+11 more).

## Not benched

- **Code conflicts with `main`** (391 PRs): not rerun until rebased.
- **Waiting for a look before they're built** (100): #4649, #4652, #1217, #1292, #1493, #1713, #1926, #1927, #1948, #2815, #3337, #3878, #4136, #5113, #5158, #5307, #5331, #5357, #5778, #5791, #6039, #6066 change
  build scripts, cargo config or dependencies; 78 more are from authors without a merged PR yet.
- **Change no rendering file** (100): not benched.
- **Doesn't build once merged with `main`:** #1292, #2783, #2876, #3160, #3520, #4265, #4408, #4640, #4645, #5570, #675.
- **Removed from this list** since they're no longer open: merged #5684, #5448, #5442, #5450, #5346, #5347, #5348, #5437, #5440, #5456, #4579, #5055, #5392, #5655, #5691, #5287, #5343, #5410, #5452, #5697, #4702, #5533, #5594, #5295, #5411, #5729, #5734, #5761, #5784, #5788, #5796, #5802, #5811, #5830, #5851, #5459, #5414, #5453, #5426, #2783, #3195, #3197; closed without merging #1579, #1809, #2415, #3082, #3984, #4267, #4297, #2437, #2495, #2670, #3241, #3915, #4307, #4837, #5632, #5633, #4249, #5666, #3187, #1448, #3141, #3883, #4189, #4938, #5678, #5119, #5974, #1518.
- **PDF export issues the bench can't see** (it compares rendered pages): file size (#5309), reproducible output
  (#3083, #4300), `/Suspects` in `/MarkInfo` (#3410), tracked-change colours with markup
  (#5232, #5233), the numeral display mode (#4461), embedded objects (#5393), Arabic chart text (#4199),
  Cambria accents on real documents (#4476).


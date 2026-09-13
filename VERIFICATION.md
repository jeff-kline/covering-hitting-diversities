# Local verification record

Checked September 13, 2026 UTC. Scope: local release candidate, not admission.

Environment: macOS; Python 3.9.6 at /usr/bin/python3; pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2021/MacPorts 2021.58693_2), kpathsea 6.3.3,
with default fonts; amsmath 2.17i, amssymb 3.01, amsthm 2.20.6, geometry 5.9,
microtype 2.8c, and hyperref 7.00k. Poppler rendered pages.
No environment or dependency installation was performed.

Commands run from the candidate root:

```sh
make paper PYTHON=/usr/bin/python3 PDFLATEX=/opt/local/bin/pdflatex
make verify PYTHON=/usr/bin/python3
shasum -a 256 -c MANIFEST.sha256
git diff --check
pdfinfo paper/main.pdf
pdftoppm -r 90 -png paper/main.pdf build/pages/page
/usr/bin/python3 ~/.codex/skills/admit-research-release/scripts/release_audit.py \
  --root . --state candidate --tag v0.1.0 --require-clean
```

Build result: two clean two-pass builds were byte-identical. Final logs contained
no warnings, undefined references, or overfull/underfull boxes. PDF: 11 US Letter
pages, 354426 bytes; 14 cited references. Title and author PDF metadata agree.
The source date fixes PDF creation metadata to September 13, 2026 00:00 UTC;
it is not a release date. Rendered pages 1–11 were individually inspected by root:
no clipping, overlap, broken mathematical glyphs, or displaced radicals observed.
The bibliography occupies page 11. TeX reading order in extracted text is not
used as a substitute for rendered inspection.

Paper source SHA-256:
`8ef19cd8b90ad3ba7dc30340f8ad21aee533c526fef08e086c3b90b0f834ffdc`.
PDF SHA-256:
`4073aa822ca291f68c94a0e148ca3f92e10216cc6ad6065b148d3cf799fa72ed`.

The project checker verifies the P07 proof region (excluding the declared figure input), two original initial
seals, the 14/14 citation-key bijection, and complete tracked manifest coverage.
Git-checkout and extracted-archive modes passed. Deliberately corrupting the
extracted README and emptying the initial seal each produced the required
failure; see AUDIT_LEDGER.md for the test-harness correction.
Script hashes and every retained artifact hash are in MANIFEST.sha256.
Shared release-audit script SHA-256:
`d996876f7ce15f77828b959dc55aa2a09eb54feb52a7e964e3a25c6259b8120b`.

The final clean candidate audit is run after committing; its exact output and
commit are retained in the local delivery receipt outside the commit to avoid
circular self-hashing. An absent v0.1.0 tag is an expected prepublication warning.
This mechanical check does not judge proofs or close P1/R1.

Excluded: exploratory numerical tests, source-workspace campaigns, third-party
PDFs, build logs and rendered images (ignored build/), and authenticated portals.
The selected P07 reports are reused only with their original scopes. The original candidate was publicly pushed with authorization. These later local
revisions have not been pushed; no tag, archive upload, DOI activation, or site
deployment was performed.

## Title-alignment correction

The user caught a right-shifted subtitle missed by the initial visual review.
Replacing the title's LaTeX newline command with a centered line break fixes
the alignment. The corrected first page was rendered and visually inspected.
The subtitle and author bounding-box centers are both 306.00 pt; the first
line's ink center is 307.07 pt (font/microtype protrusion). Pages 2–10 render
pixel-identically to the prior candidate at 72 dpi. Two clean two-pass builds
still match exactly and have no warnings. Only the title command changed in
TeX; the mathematical text and bibliography remain identical. Earlier audit
source pins remain historical and are not rewritten to imply fresh exposure.

## First-use definition and original-source credit

Replaced the informal opening with a metric-generalization explanation and
credited Bryant and Tupper at first use, citing their 2012 Advances in
Mathematics paper (preprint arXiv:1006.1095, first posted in 2010). Its arXiv
abstract explicitly introduces diversities; journal metadata and DOI were
checked there. The publisher full-text endpoint returned HTTP 403; no full
publisher-text inspection is claimed. The introductory explanation agrees
with Definition 3.1 of the already checked Jozefiak–Shepherd v1.

At that revision, the PDF had 14 references and ten pages. Two clean builds match and
final logs are warning-free. Changed pages 1, 2, and 10 were visually checked;
pages 3–9 render pixel-identically to the preceding title-corrected candidate
at 75 dpi. The P07 proof region is unchanged. Earlier thirteen-reference
audit reports are historical and retain their original pins and scope.

## Reproducible q=3 illustration

Added a full-page figure after the construction, bringing the PDF to eleven
pages. Root inspected all eleven rendered pages. The figure generator produced
byte-identical PDF and PNG artifacts in two clean builds; the paper likewise
passed two clean two-pass builds without warnings. The figure uses TikZ and
fix-cm; rendering uses Poppler. No filled spatial region represents the cut.

The exact standard-library checker enumerates all 512 grid subsets, including
511 nonempty sets: the maximum hitting-probability ratio is 3/2, attained by
18 non-collinear triples. The example hits three columns and six supplies.
The general moment constant is (2q-1)/q, equal to 5/3 only at q=3.
See audit/Q3-FIGURE.md for the separate finite check and its exposure limits.
The general theorem/proof text remains identical after removing only the
single declared figure-input line from the continuity comparison.

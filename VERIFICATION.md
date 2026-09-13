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
no warnings, undefined references, or overfull/underfull boxes. PDF: 10 US Letter
pages, 249789 bytes; 14 cited references. Title and author PDF metadata agree.
The source date fixes PDF creation metadata to September 13, 2026 00:00 UTC;
it is not a release date. Rendered pages 1–10 were individually inspected by root:
no clipping, overlap, broken mathematical glyphs, or displaced radicals observed.
The bibliography occupies page 10. TeX reading order in extracted text is not
used as a substitute for rendered inspection.

Paper source SHA-256:
`6fe05e3d8688e8b56549e4a5152803eb027fa48b2c6d94367221d4d86f2cba38`.
PDF SHA-256:
`17a634d5a44387ce1bfcfa20c127c3945f59e03057e664e5c9f9a363c2f46b21`.

The project checker verifies the unchanged P07 proof region, two original initial
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
The selected P07 reports are reused only with their original scopes. No public
push, tag, archive upload, DOI activation, or site deployment was tested or done.

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

The current PDF has 14 references and ten pages. Two clean builds match and
final logs are warning-free. Changed pages 1, 2, and 10 were visually checked;
pages 3–9 render pixel-identically to the preceding title-corrected candidate
at 75 dpi. The P07 proof region is unchanged. Earlier thirteen-reference
audit reports are historical and retain their original pins and scope.

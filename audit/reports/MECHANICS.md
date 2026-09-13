# Fresh release mechanics audit — initial returned findings

Scoped verdict: PARTIAL — build and retained-evidence integrity pass; archive
verification portability needs correction before publication.

Must fix: scripts/verify.py:31–35 unconditionally requires a Git checkout.
The planned GitHub/Zenodo zipball lacks .git, so documented make verify fails.
Add archive mode verifying hashes without Git while retaining tracked-file
coverage and whitespace checks for a checkout. Document the distinction.

Optional hardening: require exactly the two expected historical seal paths;
require unique proof-region delimiters; add staged git diff --cached --check.

Passed: independent scratch build using /usr/bin/python3 and the recorded
pdfLaTeX gives two clean two-pass PDFs matching the candidate SHA-256
6531d409331a1e9a18b8ab975a34425bd0f3bdea9128e8780c082b333fd8398c.
Protected proof region and both initial seals match. All eight retained files
represented in the original manifest match their historical hashes.
Reviewed citation/license/version/prepublication metadata are consistent;
DOI and date-released are absent. Public mutations require authorization and
Zenodo authenticated interaction remains with the user.

Exposure: read-only candidate inspection and scratch-only reproduction. No
candidate edits, external actions, publication, installations, or email. No
final manifest, clean-tree, commit, mathematical, external citation-content,
or rendered-layout certification. Root transcribed the returned findings;
local scratch path omitted. Dispositions belong in AUDIT_LEDGER.md.

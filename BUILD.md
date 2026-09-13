# Build and verification

Requirements: Python 3.8 or later (standard library only), Git, and pdfLaTeX
with amsmath, amssymb, amsthm, geometry, microtype, and hyperref. No solver,
external bibliography tool, shell escape, or package installation is needed.
The paper uses the TeX installation's default Computer Modern fonts.

From the repository root:

```sh
make paper
make verify
```

The checked installation uses:

```sh
make paper PYTHON=/usr/bin/python3 PDFLATEX=/opt/local/bin/pdflatex
make verify PYTHON=/usr/bin/python3
```

The build script copies the TeX into two separate temporary directories and
runs pdfLaTeX twice in each. It fixes SOURCE_DATE_EPOCH to September 13, 2026
00:00 UTC, FORCE_SOURCE_DATE=1 and TZ=UTC. It rejects final warnings, undefined
references, and overfull/underfull boxes, then requires identical PDF bytes.
It writes paper/main.pdf and an ignored build/main.log. This date is a build
reproducibility parameter, not a publication date.

Exact PDF identity is checked within the recorded TeX installation. Different
TeX/package/font versions may change the bytes or pagination. Run make verify
after rebuilding to compare with the committed PDF and manifest. A hash change
on another installation requires inspection, not automatic replacement of the
recorded artifact. Do not regenerate MANIFEST.sha256 merely to hide a mismatch.

Verification checks the P07 proof-region identity, both original initial seals,
the 14 citation keys, all tracked-file hashes, and staged/unstaged Git whitespace.
In an extracted archive without .git, make verify instead checks all regular
files against the manifest; ignored build/, __pycache__, and .DS_Store are
excluded. It skips Git history/whitespace checks there. Both modes reject
hash mismatches and missing or extra release files. It does not
prove the mathematics or verify external source content. There are no material
computational claims requiring a numerical reproduction suite.

For rendered inspection with Poppler:

```sh
mkdir -p build/pages
pdftoppm -r 110 -png paper/main.pdf build/pages/page
pdfinfo paper/main.pdf
```

The author's additional release audit is external shared tooling, not a project
dependency. Its script hash and result are recorded in VERIFICATION.md:

```sh
/usr/bin/python3 ~/.codex/skills/admit-research-release/scripts/release_audit.py \
  --root . --state candidate --tag v0.1.0 --require-clean
```

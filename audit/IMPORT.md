# Deliberate import and provenance

Source: the author's non-Git `hypergraph-emd` research workspace. `git rev-parse`
reported that it was not a repository; no source commit or branch is asserted.
The authoritative source was `notes/affine-obstruction.tex`.

Before import on September 13, 2026 UTC, all 11 entries of P07 MANIFEST.sha256
passed and `cmp notes/affine-obstruction.tex rounds/p07/cold/PAPER.tex` exited 0.
The original 11-entry manifest is retained verbatim as
[p07/ORIGINAL-MANIFEST.txt](p07/ORIGINAL-MANIFEST.txt). It uses historical source
paths and is a record, not the release manifest or a command for this repository.

Selected records under p07/ are verbatim: isolated claim packet, initial attack,
initial seal, frozen paper source, subsequent proof audit, literature report,
root transfer check, gates, and visual QA. The release-level MANIFEST.sha256
pins their new locations. The initial seal uses the old source namespace;
`make verify` checks its two entries through an explicit path mapping.
The source reading PDF and broad campaign README are not imported; their hashes
remain in the original manifest. This bundle includes the new reading PDF.

No exploration code or experimental certificates are imported: the paper's
claims use self-contained proofs, not a numerical experiment. No neighboring
workspace or source file was moved or modified. Bibliographic source PDFs are
not part of the public bundle.

The release changes abstract/introduction/status wording, PDF metadata, and
release date/status presentation. `make verify` checks that the text from
Definitions and construction through the end of Related work before Status
is identical to the P07 proof source. The raw audit is not rewritten to extend
its verdict to unexamined sources or all bibliography entries.

Naming: the proposed local destination did not exist; authenticated `gh repo
view jeff-kline/covering-hitting-diversities` returned no repository, covering
public and private repositories accessible to that account. This is a dated
collision check, not a reservation; recheck immediately before repository creation.

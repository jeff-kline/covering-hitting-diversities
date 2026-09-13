# Audit ledger

Root owns the dispositions below. The records describe AI checking processes,
not independent expert review, peer review, or an admission certificate.

## P07 evidence reused — source check September 13, 2026 UTC

The 11-entry source manifest passed before import. The active TeX equaled the
frozen cold paper. [IMPORT](audit/IMPORT.md) documents deliberate selection.
The [initial attack](audit/p07/cold/INITIAL.md) was sealed before proof exposure;
its NOT-BROKEN verdict did not verify a proof. The subsequent
[proof audit](audit/p07/cold/PROOF-AUDIT.md) verified Theorem 5, Lemma 8,
Corollary 10 and their in-paper dependencies. It explicitly left a supplemental
exact-source check incomplete. The separate literature/root source checks are
retained as separate evidence and do not overwrite that limitation.

The P07 original source SHA-256 is
30aaa33bfeafa8dd6023a740bf5a61c4adbba1a62ce8120a9944f0288db6e8df.
The release source changes prose and presentation but preserves the entire
proof region from Definitions through Related work before Status. The project
checker enforces this equality. Material future mathematical edits reopen it.

## Fresh release proof review — September 13, 2026 UTC

[Returned report](audit/reports/PROOF.md). Fresh context; actual proofs exposed
at the start; no old reviews read. Bounded to twelve minutes, two external
retrieval calls, no research computations. Paper SHA-256
26872f223a38a09ae9638634048d9364213c95788dc746bad49939a1c4d28fdc.

Disposition: accept VERIFIED for the self-contained arguments and PASS for
README/abstract/introduction consistency. No mathematical repair required.
Exact source identification remains outside that report's verdict and is
handled by the source record. Optional zero-cost terminology clarification is
not applied: the principal results use positive/unit costs, and the introductory
nonnegative convention follows the cited source. No zero-cost nondegeneracy
claim is promoted. Minimum attainment also follows from the finite cut LP;
no additional claim or edit is needed.

## Fresh release mechanics review — September 13, 2026 UTC

[Initial findings](audit/reports/MECHANICS.md). Read-only review and independent
scratch build, six-minute allocation; no external requests or numerical research.
The scratch PDF matches the root PDF exactly. The initial verdict was PARTIAL
because verification required .git and would fail in a provider archive.

Disposition: accepted and repaired by root. scripts/verify.py now supports both
Git and extracted-archive modes, checks exactly the two historical seal paths,
requires unique ordered proof-region boundaries, and checks staged as well as
unstaged whitespace. Root tested Git mode and an extracted tree successfully.
A corrupted extracted README and an emptied initial seal both failed with the
expected diagnostic. The negative-test harness initially checked stdout although
SystemExit writes the diagnostic to stderr; the harness was corrected and both
controls rerun. No checker defect was hidden by that harness correction.
The original PARTIAL report is preserved; this disposition records the repair.

## Root source, visual, and final mechanics checks

Root checked the exact primary-source conjecture, LP, and predecessor final
inequality; see [PRIOR_WORK](audit/PRIOR_WORK.md). Two clean two-pass builds
matched byte-for-byte; all ten rendered pages were inspected. The PDF contains
13 references and no observed glyph/layout defects. The abstract's radicals
are correct in the rendering. Final mechanically pinned results and environment
are in [VERIFICATION](VERIFICATION.md), with the clean-commit receipt outside
the candidate to avoid circular self-identification.

No public tag, GitHub Release, archive, DOI, or result-site publication occurred.

## Fresh compact prior-art review — September 13, 2026 UTC

[Returned report](audit/reports/PRIOR-ART.md). Fresh context, no earlier reviews,
initial allocation twelve minutes and ten batched source/retrieval calls, no
research computations. Root stopped further retrieval and requested a report
from completed evidence; the closing follow-up authorized no tools. Exact
observed source-call consumption was not provided by the lane and is not
claimed here. The agent did not finish reading the standard's concluding text
after output truncation; root had separately read the full standard. This lane
therefore does not certify complete compliance with its reading instruction.

Disposition: accept the completed JS conjecture/LP, SVF ancestry, classical
pairwise-independence, and ER mechanism comparisons. Keep P1 PARTIAL. The lane
did not finish the SVF final-constant check, finite-field subsection, CW full
paper, manuscript date, author-page journal-status verification, or the rest
of the bibliography. Root's direct SVF final-inequality check and the retained
P07 source records are separate evidence, not amendments to this raw verdict.
No exact earlier compact consequence was found in its inspected corpus, but
priority and equivalent-formulation occupation remain unresolved. No source
absence, private revision absence, or worldwide novelty is inferred. No
mathematical edit is required by these findings.

## User-found title defect and root correction — September 13, 2026 UTC

The initial ten-page visual pass missed an off-center subtitle caused by
\newline in the standard article title. The user identified it before tagging.
Root replaced it with \\, rebuilt twice reproducibly, and inspected the
corrected title. Rendered pages 2–10 are unchanged. No mathematics or claims
changed; the proof-region check continues to pass. VERIFICATION.md carries
the corrected source/PDF pins. The research-release skill now explicitly
checks multiline title alignment. This finding corrects the earlier overly
broad visual-QA conclusion; no old audit report is altered.

The prior candidate commit was pushed to the public repository with user
authorization. This typography correction is prepared locally and needs exact
updated publication authorization before pushing or tagging the new commit.
Zenodo integration confirmation is still pending; no tag or Release exists.

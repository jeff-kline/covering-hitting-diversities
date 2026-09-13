# Fresh compact prior-art audit — returned report

Read-only compact prior-art audit, closed on completed evidence. I read
paper/main.tex and README.md in the specified candidate; no previous reports,
edits, computations, publication, installation, contact, or subagents. This is
process-separated AI review, not independent expert review. No priority or
admission verdict is supplied.

## Confirmed source comparisons

1. Jozefiak–Shepherd, arXiv:2303.04199v1, 7 March 2023. Definition 1.6 uses
connected hyperedge collections spanning terminals. Conjecture 1.7 asks for an
algorithm achieving distortion polylogarithmic in the inducing hypergraph's
encoding size. Equation (24), PDF page 12, has supply-length variables,
nonnegative demand variables, weighted-demand normalization, and one connector
inequality per demand and connector. The candidate specializes this formulation
correctly. Its polynomial encoding and unbounded linear-in-q lower bound
contradict that version's conjecture, assuming the candidate proof. This
consequence concerns existence; it does not establish hardness of all sparsest-cut
algorithms. [Versioned paper](https://arxiv.org/html/2303.04199v1)

2. Public JS revision availability. The retrieved arXiv abstract page listed
only v1. Focused searches did not produce an obtainable journal revision. This
establishes only the retrieved public record, not absence of another version.
The candidate's qualification restricting the comparison to v1 must remain.
Its phrase “a reported journal revision” was not independently substantiated by
this lane. [arXiv record](https://arxiv.org/abs/2303.04199)

3. Badanidiyuru et al., Sketching Valuation Functions, cited author manuscript.
Appendix 6, Theorem 6.1, defines the maximum group-occupancy function on equal
groups and proves a square-root separation from submodular approximants. The
candidate's full-transversal rooted realization is a valid deduction from that
set function: coverage of a query needs exactly its maximum group occupancy.
This establishes the ancestry of the existential diversity obstruction. The
retrieved proof begins the final greedy marginal argument, but my direct
retrieval did not complete inspection of the final displayed inequality.
Consequently I independently confirm the square-root ancestry, while the precise
q²/(2q−1) extraction remains unverified in this lane. Root separately reported
checking that final inequality. I did not independently verify the manuscript's
October 2011 date. [Author manuscript](https://timroughgarden.org/papers/approxxos.pdf)

4. Luby–Wigderson, Pairwise Independence and Derandomization, 1(4), 237–301,
2005. The PDF's own preferred citation matches the candidate. Section 2.1,
Claim 2.1, explicitly uses uniformly sampled (a,b) and the linear functions
ax+b modulo a prime, proving uniform marginals and pairwise independence. Its
contents identify §2.2 as “Linear polynomial space,” but I did not finish
inspecting that section's finite-field extension. The candidate correctly
credits the underlying small sample-space mechanism as classical. Its all-cut
comparison and rooted diversity/connector interpretation are additional
deductions, not claims I found in the inspected source.
[Author PDF](https://www.ias.edu/sites/default/files/math/csdm/05-06/mluby_pairwise_independence_and_derandomization.pdf)

5. Emek–Rosén, Semi-Streaming Set Cover, August 2016 author PDF. The inspected
construction starts from an affine plane with q² points and q(q+1) lines,
randomly partitions lines, and uses memory/information restrictions to force
large covers. This is close finite-geometric ancestry, but differs from the
candidate's deterministic q² rooted nonvertical supplies and uniform inequality
against every nonnegative cut mixture. The source excerpts support the
candidate's distinction between streaming restrictions and unrestricted
embeddings. [Author manuscript](https://www.irif.fr/~adiro/publ/ER.pdf)

6. Chakrabarti–Wirth, ECCC TR15-113. The report landing page was obtainable and
identifies the 9 July 2015 report. The full paper was not inspected before
closure, so its mechanism comparison remains unchecked here.
[ECCC report](https://eccc.weizmann.ac.il/report/2015/113/)

## Bounded search result and uncertainty

Focused queries covered the exact JS title and public revision,
diversity/affine/distortion combinations, hypergraph sparsest-cut/affine,
projective-plane LP gaps, and affine-plane coverage/submodular approximation.
No inspected source supplied the exact earlier compact rooted construction
with the stated all-cut inequality and encoding-size/connector-LP consequences.
This is a bounded search result, not evidence sufficient for global priority.
Search results included classical projective-plane matching/packing LP gaps,
but I did not inspect those papers fully; their LPs and objectives cannot be
treated as identical to the connector relaxation.

The compact contribution's priority remains unsettled. The candidate's explicit
uncertainty is appropriate and should not be strengthened on the basis of this
review.

## Credit and citation findings

No confirmed material citation mismatch in the completed JS, LW, or ER checks.
Preserve the distinction between the earlier existential square-root result
and the compact realization. Preserve both the 2019 earth-mover credit and
the later range-EMD/prefix-width credit. The candidate already separates the
geometric motivation from the obstruction's dependency. Neither EMD source was
independently inspected in this bounded lane. SVF manuscript date, precise
finite constant, CW full mechanism, journal-revision status, and other cited
sources remain as described above; do not mark them all verified by this report.

## Public-standard limitation and must-fix integration point

The public standard was retrieved as version 0.4 (draft), published 1 August
2026. I read its substantive claim, credit, evidence, adversarial-checking,
AI-responsibility, and stewardship requirements. Output truncation prevented
complete inspection of its concluding text; the attempted final retrieval was
interrupted. Thus the instruction to read the full public standard was not
completely fulfilled in this lane, and the audit ledger must not claim
otherwise. [Public standard](https://jeff-kline.github.io/posts/research-program/index.html)

No new mathematical must-fix issue was established by the completed source
audit. The must-fix reporting requirement is to retain these incomplete checks
and exact version boundaries in the audit record, and not turn this bounded
negative search into a novelty certification.

Root transcription note: mathematical typography and line wrapping normalized;
findings and limits retained. The original response remains in the local task
record. This report is not retroactively expanded by root's separate checks.

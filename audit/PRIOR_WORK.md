# Bounded prior-work comparison

Checked September 13, 2026 UTC. P1: PARTIAL. This review seeks the precise
compact affine realization and its encoding-size and specified connector-LP
consequences; it does not seek stronger theorems or restart the research campaign.
Priority remains unresolved. Absence from the searched corpus is not a global
novelty result, and unavailable versions are not negative evidence.

## Mechanism comparison

| Source | Established mechanism / consequence | Relation to this paper |
|---|---|---|
| Badanidiyuru et al., Sketching Valuation Functions, SODA 2012; October 2011 author manuscript, §6 Theorem 6.1 | The maximum occupied group size on q groups of q points has a square-root lower bound against submodular approximation. | A rooted realization using all q^q transversals yields the diversity consequence. Retaining the proof's final inequality gives q²/(2q−1). Neither the existential growth nor constant is claimed new. |
| Luby–Wigderson, Pairwise Independence and Derandomization, §§2.1–2.2 | Uniform affine evaluations form a classical pairwise-independent sample space. | The q² supplies use this standard construction. The all-cut covering/hitting argument and compact diversity consequences are the combination under comparison, not a new sample space. |
| Jozefiak–Shepherd, arXiv:2303.04199v1, Conjecture 1.7 and Eq. (24) | Encoding-size polylogarithmic embedding conjecture and connector LP for hypergraph sparsest cut. | Polynomial incidence encoding and a lower bound q/2 contradict the exact v1 conjecture regardless of runtime. The stated capacities/demands specialize Eq. (24); the paper proves optimum 1/q and the gap. |
| Jia et al., STOC 2005; Ezra et al., 2024 author manuscript | Universal set-cover assignments and restricted-service/greedy lower bounds. | Assignment approximation bounds are credited antecedents. Their transfer needs cover cost to control connected cost. Representation-restricted lower bounds cannot automatically obstruct arbitrary coverage or diversity embeddings. |
| Emek–Rosén; Chakrabarti–Wirth | Finite-plane set systems in streaming set-cover lower bounds. | Finite geometry is antecedent; information restrictions in streaming differ from an inequality against every nonnegative cut sum. Exact occupation of the compact consequence is not settled by this distinction alone. |
| Devanur et al., arXiv:1304.4948 | Coverage approximation and budgeted-additive conversion. | The factor e/(e−1) is established prior work; the paper applies it to the greedy-bad family. |
| Bryant–Tupper, 2014, 2017, and 2026 works cited in paper | Cut/diversity framework, general embedding question, and rooted set-function connections. | The paper gives special-class matching exponents, not a general square-root upper bound. |

## Direct source checks by root

The root reread [JS v1](https://arxiv.org/html/2303.04199v1), specifically
Conjecture 1.7 and Eq. (24). The displayed conjecture is in the inducing
hypergraph's encoding size and does not explicitly require polynomial runtime.
Substituting capacities 1/q², demand weights 1/q, and rooted columns into that
LP gives precisely the paper's relaxation. These source facts and the
paper's proved asymptotic implication are separate obligations.

The root also reread [SVF's author manuscript](https://timroughgarden.org/papers/approxxos.pdf),
PDF pages 10–11: its final estimates have b≤1/q and q≤alpha(1+(q−1)b).
The finite constant follows arithmetically. The full-transversal diversity
transfer is a deduction explained in the paper, not a diversity theorem
stated by those authors. The exponential representation has log encoding
already of order q log q, so it does not provide the compact conjecture
counterexample by itself.

## Reused and fresh review evidence

[P07 literature](p07/literature/RESULT.md) and the separate
[P07 root transfer check](p07/ROOT-PRIOR-TRANSFER.md) preserve the earlier
source inspection. The [P07 proof audit](p07/cold/PROOF-AUDIT.md) verified its
assigned mathematics and transfer but did not finish its supplemental
exact-appendix check. That limitation remains intact; these distinct checks
do not retrospectively change that auditor's verdict.

The fresh release literature report and root dispositions are recorded in
AUDIT_LEDGER.md. No fresh proof auditor's report is treated as literature
verification where its source scope was explicitly incomplete.

## Credit and residuals

The 2019 earth-moving paper and subsequent prefix-width/range-EMD work remain
credited in the introduction and bibliography. The geometric starting point
is separated from the obstruction; the later transport-rigidity theorem is
not required by this proof.

The checked public target remains arXiv:2303.04199v1. The author's page reports
a DMTCS minor revision, but no newer public manuscript was located in the
recorded checks. Private revision status is unknown. Priority of the compact
construction, its equivalent formulations, and the exact combined consequences
remains unresolved. No first existential polynomial/square-root bound, new
finite constant, or first-ever affine construction is asserted.

## Fresh-lane completion limits

The [fresh compact audit](reports/PRIOR-ART.md) confirms the exact JS v1
comparison, SVF square-root ancestry, LW's prime-field sample space, and the
ER streaming distinction. Its check of CW stopped at the report landing page;
the corresponding table row is the paper's credited contextual comparison,
not a fresh full-text verification of CW. It also left LW's finite-field
subsection, SVF manuscript date/final constant, journal-status author page,
and EMD source texts unchecked. Its reading of the standard's conclusion was
incomplete after truncation and closure. Root read the full standard separately
and checked the SVF final constant directly; P07 retains the author-page/date
checks. These scopes are not combined into a fictitious all-sources verdict.

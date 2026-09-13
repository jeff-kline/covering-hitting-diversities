# Fresh release proof audit

Read-only proof-aware fresh-context audit completed.

Audited snapshot: staged release candidate (local staging path omitted by root).

`paper/main.tex` SHA256:
`26872f223a38a09ae9638634048d9364213c95788dc746bad49939a1c4d28fdc`

**Proof scope: VERIFIED for the self-contained mathematical arguments. INCOMPLETE for exact external-source identification and attribution. No mathematical GAP found.**

**Abstract/introduction/README consistency: PASS.**

The complete public standard, version 0.4 draft, was read: direct web opening failed; curl retrieved the page, with the truncated final portion supplied by the parent. No older reports were read.

Proof findings, with line evidence in `paper/main.tex`:

- **Affine construction and cut lemma, lines 107–186: VERIFIED.** There are q² supplies, each containing q+1 vertices; explicit identifiers require O(q³ log q) bits. Root connectivity makes connected cost equal cover cost on every nonsingleton terminal set, including sets omitting the root. Each point lies on q supplies; ordered distinct pairs in different columns lie on one supply, and same-column pairs on none. This gives the stated second moment and C_q=(2q−1)/q. The empty test set is treated separately, avoiding division by zero. Prime powers have q≥2.

- **Embedding theorem, lines 169–213: VERIFIED.** Coordinate gaps give a finite nonnegative cut representation without restricting target dimension. The averaged demand cost is q, yielding D≥q/C_q=q²/(2q−1). Singleton point cuts have value |A∩X| on every nonsingleton; the cover bounds give D≤q. Empty sets and singletons agree at zero. If literal attainment in “minimum distortion” is desired, it follows from the finite cut-variable LP: the displayed feasible upper bound bounds every cut weight through a crossed pair.

- **Conjecture corollary, lines 215–224: VERIFIED conditional mathematical implication; external comparison INCOMPLETE.** Polynomial encoding makes every fixed polylogarithm of encoding size o(q), whereas distortion is at least q/2. I did not retrieve JS v1 to independently verify that its Conjecture 1.7 has exactly the asserted wording and scope.

- **Specified connector LP, lines 230–278: VERIFIED.** Nontrivial root-oriented cuts have positive demand denominator. Normalized crossing indicators satisfy every connector constraint. Constant lengths 1/q and demands one are feasible because a column requires at least q supplies. Every fixed-slope resolution is a connector for every column; averaging demand constraints and summing slopes proves the matching lower objective 1/q. Consequently the gap is at least q²/(2q−1). The distinction between capacities and original lengths is explicit. No algorithmic-hardness conclusion is inferred beyond failure of polylogarithmic approximation relative to this LP.

- **Moment certificate, lines 280–325: VERIFIED.** Covering and full support imply M>0; nonempty demands imply K≥1 and gamma>0. The two branches of min(gamma M,1)(a+bM)/M each give a gamma+b. The proposed LP point is feasible with objective 1/K, and full-support capacities bound its optimum away from zero. Zero-demand cuts are correctly excluded from ratio optimization.

- **Transversal corollary and finite-field realization, lines 327–378: VERIFIED.** The same moments give comparison (q+k−1)/k and lower bound kq/(k+q−1). Resolution classes prove optimum 1/q. Singleton cuts and finite fair-bit cut averaging yield upper bounds k and 2q, with min(k,2q)≤sqrt(2kq). The boundary k=1 is sound. Pairwise independence follows from the two distinct coefficient vectors; indexed duplicates do not invalidate the probability or LP arguments.

- **Assignment and lifting lemmas, lines 380–447: VERIFIED.** Positive-cost greedy assignment terminates with a finite partition. At supply-hit steps the positive integers a_i strictly decrease, giving the harmonic bound. The unit-cost threshold proof also works at N=1. The lift explicitly compares only nonsingletons. Pairwise-independent bits preserve the required crossing lower bound; 2^ceil(log_2(m+1))≤4m, including m=1, proves the finite coordinate count.

- **Upper theorem and non-root corollary, lines 449–504: VERIFIED.** Scaling the lifted coverage function by kappa gives precisely the stated constants. Pairwise intersection ensures every cover is connected. The three-root modification has empty global intersection and preserves the old diversity upon restriction. The diameter argument adds at most (d−1)(k−1) intermediate edges; d=0 is handled separately. Its restriction to unit costs is explicit.

- **Transversal-cover lemma, lines 516–539: VERIFIED.** Petal points force their blocks, giving f=F+min(1,u), including singleton blocks and the empty query. The exponential random hitting construction gives H≤Q≤alpha H, hence factor 1+alpha≈2.581977<2.583, and the doubled factor is approximately 5.163953<5.165. Its support is finite because the underlying set is finite; polynomial support is expressly unclaimed.

The abstract at lines 21–38, introduction at 52–82, and README at 11–43 consistently distinguish the compact construction from the earlier existential bound, qualify priority, restrict the conjecture comparison to v1, and confine matching upper bounds to the stated special class. The arbitrary-hypergraph connectivity limitation is real: endpoints of a long ordinary path have cover cost two but connected cost equal to their distance.

**Must-fix findings:** None within the reviewed mathematical and consistency scope.

**Optional clarification:** Lines 86–95 allow zero edge lengths; under the strict convention requiring positive value on every nonsingleton, this is a pseudodiversity unless nondegeneracy is added. All principal results use positive or unit costs, so this does not affect them.

**Exposure and limits:** I read the actual proofs before evaluating them; this was not an isolated statement-only attack. No experiments, edits, builds, publication actions, installations, or email occurred. Exact literature claims—including JS numbering, the predecessor proof’s retained constant, and descriptions of cited greedy lower bounds—were not independently source-checked. Release artifacts linked from README, provenance, reproducibility, and publication state were outside the authorized two-file review. This report is an AI proof audit, not expert review, priority verification, or an admission verdict.

Root transcription note: mathematical typography normalized to Unicode/plain notation;
staging path omitted. Findings, qualifications, and dispositions above are the returned
report, not an expanded verdict. Original response remains in the local task record.

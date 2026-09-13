# Proof audit of the frozen p07 paper

STAGE: PROOF-AUDIT

VERDICT: VERIFIED for Theorem 5, Lemma 8, and Corollary 10, including their load-bearing dependencies in the frozen paper. The optional source-specific related-work check is INCOMPLETE, as distinguished below.

CLAIM: The named statements in `rounds/p07/cold/PAPER.tex`, SHA-256 `30aaa33bfeafa8dd6023a740bf5a61c4adbba1a62ce8120a9944f0288db6e8df`. This verdict concerns mathematical correctness of those statements and their supplied proofs, not novelty, priority, the cited conjecture's exact wording, or the entire bibliography.

## Theorem 5: verified

The proof's hypotheses ensure that every nonempty test set has M > 0. Since demands are nonempty with total probability one, some demand marginal is positive; coverage and full support give positive supply marginals, forcing gamma > 0. Cauchy–Schwarz gives supply hitting at least M/(a+bM); the denominator is positive because the second moment is positive. The union bound gives demand hitting at most min(gamma M,1). On the first branch the ratio is at most a gamma + b gamma M <= a gamma + b; on the second it is at most a/M+b <= a gamma+b. Empty test sets and zero values of either coefficient are handled without division by zero. Expanding the ordered off-diagonal terms under the sufficient incidence condition gives the stated M+beta M^2 bound.

The paper's threshold decomposition is valid on every terminal subset simultaneously: sorting coordinate values decomposes each range into nonnegative gap-weighted cuts, and complementing cut sides preserves their values. Root-free orientation turns supply and rooted-demand crossing into the hitting events just bounded. Every unit-cost rooted supply has diversity exactly one, while each rooted demand has diversity tau(B). Averaging domination on demands and the distortion upper bound on supplies therefore gives K <= CD, with no dimension restriction beyond the defined finite-dimensional embedding.

The LP argument is valid as written. Rooted supply collections are connected, so its covering and connector constraints coincide. K >= 1; constant lengths 1/K and demand variables tau(B)/K are feasible and have objective 1/K. The hitting inequality bounds each positive-demand cut ratio below by 1/C. Averaging the full-supply connector constraint gives sum d_S >= 1, so full support bounds the LP optimum away from zero by min mu(S). Consequently the ratio of minimum cut value to LP optimum is at least K/C. The signs and the direction of the division are correct. The cut-to-LP feasibility argument supplied earlier in the paper applies to this rooted setting as well.

## Lemma 8: verified

For a fixed atom, the independent-bit calculation gives crossing probability zero when the atom is missed; otherwise it is 1-2^(-|A intersection T|) when A also has an outside terminal, or 1-2^(1-|A|) when A is contained in the atom. On the required domain |A| >= 2 both relevant probabilities lie between one half and one. Twice the expectation therefore gives both required inequalities after summing nonnegative atom weights. Its support is finite. The proof does not incorrectly impose coverage-function values on singletons.

The reduced-support construction uses distinct nonzero binary vectors. Distinct such vectors are linearly independent over F_2, so their inner products with a uniform seed are pairwise independent fair bits. One inside point paired with an outside terminal, or two distinct inside points, witnesses a crossing with probability one half. This establishes the same lower bound without requiring full independence; the upper bound remains one. A size-m atom uses at most 2^ceil(log_2(m+1)) <= 4m cuts. Partition atoms have total size N, so the stated 4N coordinate bound follows. Empty atoms have no effect; N = 1 has no constrained nonsingleton sets.

## Corollary 10 lower bound: verified through Theorem 2 and Lemma 1

The affine construction has q^2 nonvertical lines over F_q, with q >= 2. A point lies on q of them. Distinct points in different columns lie on exactly one; two points in the same column lie on none together. Thus Lemma 1's first and second moments, including the ordered-pair subtraction sum_x t_x^2, are correct. For t > 0, Cauchy–Schwarz, sum_x t_x^2 >= t^2/h, t >= h, and h <= q give the claimed (2q-1)/q ratio with all denominators positive. The empty case is explicit.

The construction's common root makes every nonempty supply collection connected. A column demand needs q edges because each line contributes one point, and q horizontal lines suffice. A supply demand has cost one. Applying the checked cut decomposition to Lemma 1 gives the displayed averaged inequality; Theorem 2 correctly deduces D >= q/C_q = q^2/(2q-1). Its upper bound is also sound: on nonsingletons the sum of point singleton cuts equals s = |A intersection X|, and the line-cover cost lies between s/q and s. Empty and singleton values are zero. These arguments cover terminal sets omitting the root as well as rooted ones.

For Corollary 10's replacement, each supply contains two of three new roots. Any two such root pairs intersect, hence all supplies pairwise intersect. Every root is omitted by some edges. Every affine point is omitted by an affine line, so no affine point belongs to all new edges either. The global intersection is therefore empty for every allowed q.

On terminal subsets of X union {r_1}, projection of any new cover to its distinct affine lines gives an old rooted cover of no greater cost. Conversely, replacing every old rooted edge by its version containing {r_1,r_2} gives a new cover of the same cost. All these covers are connected. Nonsingletons in this restricted vertex set contain an affine point, avoiding a root-only exceptional case; singletons and the empty set have zero diversity in both systems. The equality of restricted diversities claimed in the actual proof follows. Restriction of any embedding consequently retains Theorem 2's lower bound.

Finally n = q^2+3, and q^2/(2q-1) is bounded below by a positive constant times sqrt(n) along unbounded prime powers. The result is a family lower bound, not an assertion that every pairwise-intersecting instance has large distortion.

## Corollary 10 upper bound: verified through Theorem 9 and Lemma 7

I checked both branches of Lemma 7 because Theorem 9 states both weighted and unit-cost conclusions. In the weighted greedy assignment, each chosen residual block is nonempty and the process terminates. At a step hitting a fixed supply S, that supply is an available candidate, giving c(S_i) <= c(S) sqrt(b_i/a_i). The positive integers a_i strictly decrease at such steps. Disjointness gives sum b_i <= N, and decreasing a_i gives sum 1/a_i <= H_N. Cauchy–Schwarz yields the claimed bound on g(S). Charged supplies cover a query, so f <= g; monotonicity and subadditivity applied to a minimum cover then give the upper bound on arbitrary queries.

For unit costs, the large residual blocks number at most N/t with t = ceil(sqrt(N)). Each remaining supply contains at most t-1 residual vertices. Any cover of A therefore bounds |A intersection R| by (t-1)f(A). For nonempty A, f(A) >= 1, and N/t+t-1 <= 2 sqrt(N), since N/t <= sqrt(N) and t-1 <= sqrt(N). The singleton residual blocks are valid blocks associated with covering supplies even though they need not themselves be supplies. Thus this construction has the claimed partition support and approximation factor.

Theorem 9's scaling chain is valid: delta <= kappa f <= kappa Delta_0 <= 2 kappa g <= 2 kappa D f <= 2 kappa D delta. Lemma 8 supplies at most 4n coordinates because the assignment blocks partition the original vertex set. Both actual diversities vanish on small terminal sets. Pairwise intersection ensures that every nonempty cover is connected, hence kappa = 1 and the universal 4 sqrt(n) bound. Together with the preceding constructed family this establishes the claimed tight exponent.

For the general diameter assertion, a minimum k-edge cover has k >= 1 on nonsingletons. Joining its edges to one chosen edge by paths of length at most d adds at most (d-1)(k-1) non-cover edges; overlap can only reduce the count. The total k+(d-1)(k-1) <= dk is correct for d >= 1, giving delta <= d f. A connected graph of diameter zero has a single supply edge, which covers all vertices by hypothesis, so kappa = 1. Theorem 9 therefore gives exactly 4 max(1,d) sqrt(n), including 8 sqrt(n) for diameter two. No weighted-cost version is inferred from this counting argument.

## Supplemental related-work scope

The full-transversal reduction in the paper is mathematically sound: for q groups of size q, the minimum number of full transversals covering S is max_i |S intersection Q_i|. Rooting makes the cover connected. Dividing the embedding's rooted cut sum by D gives a coverage function between f/D and f; coverage is submodular. This verifies the stated transfer conditional on the cited set-function theorem.

I used the single permitted web call to open the [October 2011 author manuscript](https://timroughgarden.org/papers/approxxos.pdf). The returned extraction exposed the beginning of the paper and its description of a square-root separation from submodular approximation, but did not expose Appendix 6 or Theorem 6.1. Thus this audit does not verify the exact theorem citation or the asserted unrounded final inequality. No second call was made. This is an incomplete supplemental source check, not a gap in the named core claims, whose proofs are self-contained.

## Dependencies, errata, and limitations

All load-bearing in-paper mathematical dependencies of the three named claims were checked above. The elementary finite-field incidence calculation requires no separate geometric theorem beyond field arithmetic. No computational certificate or empirical assumption is used.

Required mathematical repairs: none found in the audited claims or dependency proofs. No alternative proof was substituted to conceal a defective supplied argument. The supplemental source attribution should remain independently unchecked in this review record until the exact appendix and its final inequality are inspected; lack of that inspection does not justify changing or withdrawing the mathematical claims.

Excluded from the verdict: exact external conjecture wording and publication-version comparisons, bibliographic accuracy beyond the single accessed source, novelty and priority, the entire unrelated discussion, and any empirical evaluation of the review workflow. This is a same-model agent proof audit, not external peer review.

## Exposure and resources

The initial report was saved and sealed before this stage. Initial report SHA-256 supplied and confirmed by the coordinator: `910e25f824e9d3b301fb95a6a07bfeb274ad9222a546c9d8603c4c5c888d7f00`. It has not been edited.

This stage read the complete frozen PAPER.tex and the explicit primary-source PDF described above; the earlier stage read only the skill and claim packet. No campaign notes, state files, prior reviews, or external verdicts were consulted. The coordinator's follow-up assigned dependency coverage and optional source scope; its expectations were not treated as evidence.

Allocation: at most twelve minutes, zero research compute jobs, at most one web call. Used one paper read, one paper hash, one web call, and creation of this report; completed within the allocation. No experiments, subagents, installations, automations, email, contact, or publication actions.

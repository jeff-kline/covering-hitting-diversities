# Isolated initial examination

STAGE: INITIAL

VERDICT: NOT-BROKEN

No counterexample was found in the bounded closed-book search. This is not a proof-audit verdict and does not certify the asserted asymptotic lower-bound family.

## Evidence and probes

### Theorem 5

For a fixed nonempty test set write m = E Z_T and q = Pr(Z_T > 0). Full support and coverage imply m > 0. Cauchy–Schwarz and the supplied moment hypothesis give q >= m/(a + bm). Demand hitting h is at most min(1, gamma m). Splitting at gamma m = 1 gives h/q <= a gamma + b on either side. The denominator cannot vanish for m > 0, since the second moment is then positive. The empty test set has both hitting probabilities zero. Although gamma is only declared real, the hypotheses force gamma > 0: the demand distribution is on nonempty sets, so some b_x > 0, and p_x > 0.

I checked the limiting coefficient cases a = 0 and b = 0 against this calculation; neither reverses an inequality or introduces a zero denominator. The off-diagonal incidence hypothesis expands to E Z_T^2 <= m + beta m^2, so its stated sufficient constant survives the probe.

For the rooted embedding obstruction, each cut can be oriented away from r. Its supply crossing and rooted demand crossing are precisely the corresponding hitting events. Every supply edge has diversity one, while the rooted demand {r} union B has diversity tau(B). Averaging a cut sum therefore yields K <= C D. This checks the scaling direction and the rooted-versus-unrooted convention.

For the LP, d_S = 1/K and y_B = tau(B)/K is feasible and has objective 1/K. The hitting bound makes every positive-demand cut ratio at least 1/C. The optimum is positive: averaging the constraint for the cover consisting of all supplies gives sum_S d_S >= 1, and full support gives objective at least min_S mu(S) > 0. Thus division by the optimum is legitimate and the claimed gap direction survives. Nonempty demands imply K >= 1.

### Lemma 8

I tested a single atom T by randomly selecting a subset U of T with independent fair bits, leaving all points outside T unselected. If A misses T, its cut value is zero. If A hits T and has a point outside T, crossing probability is at least 1/2. If A is contained in T and |A| >= 2, crossing probability is at least 1/2 because any selected pair disagrees with probability 1/2. Crossing probability is always at most one. Twice the expected cut therefore lies between the atom's hitting indicator and twice that indicator on the required domain. Summing atoms gives the claimed inequalities; singleton values need not agree, exactly as the packet warns.

The coordinate bound also survived a direct probe. For an atom of size m >= 1, choose m distinct nonzero labels in F_2^k with k = ceil(log_2(m+1)), and use their inner products with a uniform vector in F_2^k as selection bits. Individual fairness and pairwise independence suffice for the preceding argument. The support has 2^k < 2(m+1) <= 4m elements. Disjoint nonempty atoms have total size at most N, so at most 4N cuts suffice. Empty atoms contribute nothing. For N = 1 the inequality domain is empty and the zero cut sum is admissible.

### Corollary 10

Diameter bookkeeping survived a separate probe. A cover of k terminal-containing supply edges can be joined by choosing shortest paths from one chosen edge to the others in the edge-intersection graph. At most 1 + d(k-1) edges are needed when d >= 1, hence delta(A) <= d tau(A) for |A| >= 2, while delta(A) >= tau(A). The d = 0 case consists of one supply edge covering the entire vertex set and is handled by max(1,d).

The coefficient in the upper bound is compatible with an independent covering estimate. Repeatedly choose a supply having at least sqrt(n) uncovered vertices and make those vertices a block. There are at most sqrt(n) such blocks. At termination every supply has fewer than sqrt(n) residual vertices. Let g count blocks hit plus residual vertices hit. Each block is coverable by one original supply, so tau(A) <= g(A). A minimum cover of a nonempty A bounds its residual vertices by sqrt(n) tau(A), and the total number of blocks bounds its block hits by sqrt(n) <= sqrt(n) tau(A). Thus g(A) <= 2 sqrt(n) tau(A). Combining the preceding diameter estimate with the lift's factor two produces the displayed 4 max(1,d) sqrt(n) upper bound. This calculation did not expose the paper's proof.

Pairwise intersection implies the requisite connectivity, including its one-edge boundary case. Empty global intersection does not imply disconnection. I considered projective-plane-type intersecting families as a possible stress test of the lower-bound assertion, but did not verify or import finite-geometric existence results. No concrete contradiction to the unbounded-family lower bound was obtained. The universal upper bound must not be mistaken for verification of that lower bound.

## Coverage and dependencies

Covered: empty test sets, singleton terminal conventions, N = 1, one supply edge, d = 0, coefficient-zero boundaries, the implicit sign of gamma, positivity of the LP optimum, cut orientation, averaging directions, finite cut support, and the constants in the upper-bound construction.

Unchecked: the paper's actual arguments and citations, its construction of an unbounded lower-bound family with empty global intersection, all computational certificates, and novelty. No source-dependent mathematical fact was verified. The algebraic probes use elementary probability, finite-dimensional Cauchy–Schwarz, binary linear algebra, and shortest-path counting only.

## Exposure

Fresh process-separated assignment; no campaign history or earlier reviews were supplied. Read only the cold-examiner skill and the isolated CLAIMS.md packet. No AGENTS files, state, paper, campaign notes, proof, or prior review were read. The assignment supplied applicable authorization and restrictions.

Packet: `rounds/p07/cold/CLAIMS.md`.

Packet SHA-256: `7116fd09b98db5a6b782d9f78cf5892a5faf485f3d7997dc5dfb1a0818c7e7cf`.

Tools used: file reads, packet hashing, and creation of this report. No external sources, web tools, research compute jobs, subagents, email, contact, publication, installations, or automations.

## Resources

Allocation: at most eight minutes, zero source calls, zero research compute jobs. Examination and report preparation completed within that allocation. No actual-proof exposure occurred before saving this report. Leave this initial report unchanged; any correction or proof audit belongs in a separate file.

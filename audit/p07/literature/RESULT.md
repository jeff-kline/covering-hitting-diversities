# P07 focused literature / revision check

Checked 2026-09-12. Scope: unrestricted-dimensional existential lower bounds polynomial in the number of diversity points, including consequences of prior set-function results. No research computation, contact, installation, or publication. Ten batched web calls used. No previous campaign literature verdict was read.

## Verdict

**A prior result implies an existential square-root lower bound for finite diversities, hence also hypergraph Steiner diversities.** It is not merely a computational, oracle, or target-dimension bound. The direct source uses XOS/submodular set-function language, and the diversity conclusion below is an explicit mathematical deduction. I did not find a prior source stating that deduction in diversity terminology. The broad claim “first existential polynomial lower bound” is therefore not supported. An explicit polynomial-size hypergraph realization remains a materially narrower contribution.

## Decisive primary source

Badanidiyuru, Dobzinski, Fu, Kleinberg, Nisan, Roughgarden, *Sketching Valuation Functions*: [author PDF](https://timroughgarden.org/papers/approxxos.pdf), dated October 4, 2011; [SODA 2012 publisher record](https://epubs.siam.org/doi/10.1137/1.9781611973099.81), pp. 1025–1035.

Section 6, Theorem 6.1 (PDF pages 10–11): partition an N=q²-element set into q groups Q_i of size q and put f(S)=max_i |S∩Q_i|. Every submodular g satisfying f/α≤g≤f on every subset has α≥q/2. There is no restriction on g's representation, computational accessibility, or dimension. The proof's final displayed estimates are q≤α(1+(q−1)b), b≤1/q, before rounding to 2α. Retaining that arithmetic yields α≥q²/(2q−1). This sharpening is our deduction from their proof, not their stated theorem. The preliminary sentence claiming no O(√N) approximation is imprecise; use the quantified theorem instead.

## Transfer to the question (deduction, not a quotation)

Let U be the grouped ground set, adjoin a root r, and let X=U∪{r}. For every full transversal T (one element from each Q_i), create a unit-weight hyperedge {r}∪T. There are q^q such edges, and |X|=q²+1.

All edges share r, so every nonempty edge collection is connected. Covering S⊆U needs at least max_i |S∩Q_i| edges. Conversely, k=max_i |S∩Q_i| full transversals suffice: in each group place its requested elements into different one of k slots and fill remaining slots arbitrarily. Hence the hypergraph Steiner diversity satisfies δ(S∪{r})=f(S), including S=∅ under the singleton convention. The hypergraph is connected and positive-weight, so this is a genuine finite diversity.

For any ℓ1-diversity approximation δ', orient each cut in its nonnegative cut decomposition away from r. Then

    g(S)=δ'(S∪{r})=Σ_{∅≠A⊆U} w_A 1[S∩A≠∅],   w_A≥0.

Thus g is a coverage function and in particular submodular. Rescale the embedding so δ/D≤δ'≤δ. Its restriction gives f/D≤g≤f, and Theorem 6.1 forces D≥q/2. The sharpened proof gives D≥q²/(2q−1). Since the number of points is q²+1, this is an unrestricted existential Ω(√|X|) lower bound. The argument applies to all finite target dimensions; on a finite source even an integral cut representation reduces to the finitely many cut types.

The source theorem does not provide this hypergraph encoding. Our full-transversal realization uses q^q hyperedges and Θ(q^(q+1) log(q²)) bits in a straightforward incidence encoding. It does not refute a polylogarithmic-in-hypergraph-encoding claim: the encoding logarithm is already Θ(q log q). The current affine construction's q² unit edges, if independently verified, supplies the missing polynomial-size incidence representation while maintaining the lower bound. This report does not prove that narrower result is novel.

## Independent weaker prior route

Devanur, Dughmi, Schwartz, Sharma, Singh, *On the Approximation of Submodular Functions*, [arXiv:1304.4948v1](https://arxiv.org/html/1304.4948v1), April 17, 2013: Theorem F.1/G.1 and Lemma F.7/G.7 give Ω(N^(1/3)/log²N) against the unrestricted class of coverage functions. The duplicated appendices use compression of arbitrary coverage functions and counting of matroid rank functions; their conclusion is existential, despite relying on sketching tools. Lemma 4.1 identifies coverage with nonnegative sums of set-hit indicators. This yields a weaker polynomial diversity obstruction through rooted set functions. It is not needed once the stronger 2011/2012 theorem above is used.

## Jozefiak–Shepherd revision and conjecture

The author's name is **Adam D. Jozefiak**, not Alex. His [MIT author page](https://www.mit.edu/~jozefiak/), marked last updated August 2026, lists the paper as “Minor revision, Discrete Mathematics & Theoretical Computer Science.” Its paper link goes to [arXiv:2303.04199](https://arxiv.org/abs/2303.04199), whose checked submission history lists only v1, March 7, 2023. Targeted title/DMTCS searches did not find a publicly obtainable newer manuscript or published DMTCS article. This does not establish that no private revision exists.

In [v1 §1.4, Conjecture 1.7](https://arxiv.org/html/2303.04199v1#S1.SS4), the precise content is: an algorithm embeds any hypergraph Steiner diversity into ℓ1 with distortion polylogarithmic in the inducing hypergraph's encoding size; with polynomially bounded weights the distortion is poly(log(m,n)). The sentence does not explicitly impose polynomial runtime. Theorem 1.4 instead concerns polynomial-time embedding with bounded-cardinality diversity queries, conditional on P≠NP. Lemma 3.20 converts nonnegative monotone subadditive functions to pseudodiversities by zeroing singleton values. These are different statements; the algorithmic lower bound cannot establish existential nonembeddability.

If the affine construction is correct, its polynomial incidence encoding and unit weights contradict the existential part of Conjecture 1.7 as written in v1, hence contradict its algorithmic assertion regardless of runtime. Version qualification is essential.

## Other checked primary-source distinctions

- Wu, Bryant, Tupper, [*Negative type diversities* §4](https://arxiv.org/html/1809.06523v1#S4): their ground set has n=binomial(2m,m), and their stated unrestricted lower bound is Ω(√log n). A bound polynomial in m there is not polynomial in the number of diversity points.
- Bryant–Tupper, [*Linear and Sublinear Diversities*, v3, March 3, 2026](https://arxiv.org/html/2412.07092v3#S3): §3 explicitly limits its investigation to exact embeddings. It supplies no competing asymptotic distortion lower bound.
- Bryant–Tupper, [*Diversities and the Geometry of Hypergraphs*](https://dmtcs.episciences.org/2080): gives the diversity/flow-cut framework. General finite diversity results remain relevant to hypergraph Steiner diversities; restricting the search to titles containing “hypergraph Steiner” would miss the decisive set-function consequence.

## Limitations

This is a focused source check, not a complete bibliographic census or proof of novelty. The positive match above is sufficient to defeat the broad existential-first claim. It does not settle priority for explicitly stating the diversity deduction, optimal general upper bounds, sparse/compact hypergraph witnesses, or the affine construction itself. The current local theorem was not mathematically audited in this literature assignment.

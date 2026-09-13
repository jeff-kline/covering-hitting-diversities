# Isolated examination packet
Only this packet may be read during initial attack. No campaign notes or reviews.
Finite hypergraph supply edges have positive costs and cover the vertex set; Steiner diversity delta(A) is minimum cost of a supply edge collection whose edge-intersection graph is connected and whose union contains A, for |A|>=2; delta=0 on empty/singletons. Coordinate-width l1 diversity is sum_j(max_A F_j-min_A F_j) from a map F into finite-dimensional real space, with zero empty value. Distortion D means delta<=Delta<=D delta on every subset, after rescaling. A cut diversity c_T(A) is1 if A hits both T and its complement, else0. Finite nonnegative cut sums are exactly finite-domain l1 diversities by threshold decomposition.
For Theorem5: a finite family of nonempty supplies S covers nonempty X; supply hyperedges are {r} union S of unit cost. tau(B) is minimum number of supplies covering B. mu has full support on supplies; nu is a probability on nonempty subsets B of X. p_x=Pr_mu(x in S), b_x=Pr_nu(x in B), K=E_nu tau(B). Gamma is a real constant satisfying displayed marginal condition. Connector LP minimizes sum_S mu(S)d_S over nonnegative d,y, with E_nu y_B>=1 and sum_{S in J}d_S>=y_B for every supply cover J of B, equivalently connector for {r} union B. Cut ratio is supply crossing capacity divided by positive demand crossing weight. Gap is optimal cut ratio divided by LP optimum.
For Lemma8: X finite of size N>=1. A coverage function is g(A)=sum_T w_T 1[A intersects T], w_T>=0, with T subsets X. Cuts are on original X. No claim that g vanishes on singletons.
For Corollary10: finite hypergraph on n>=2 vertices, nonempty unit-cost supplies covering all vertices; pairwise-intersecting means every pair of edges meets. General diameter assertion assumes connected edge-intersection graph; diameter of its one-vertex case is0. Tight exponent means an O(sqrt n) upper bound for the entire stated class and an Omega(sqrt n) lower bound along an unbounded family, not each instance. Exact claims follow verbatim from paper.
\begin{theorem}\label{thm:moment}
Suppose $b_x\le\gamma p_x$ for all $x$ and, for every $T\subseteq X$,
$Z_T=|S\cap T|$ satisfies
\[
 \E Z_T^2\le a\E Z_T+b(\E Z_T)^2,\qquad a,b\ge0.
\]
Put $C=a\gamma+b>0$. Then demand hitting is at most $C$ times supply
hitting for every $T$, and every $\ell_1$ diversity embedding has distortion
at least $K/C$. With capacities $\mu$ and rooted demand weights $\nu$,
the connector-LP gap is also at least $K/C$.
A sufficient incidence condition is
$\Prob_\mu(x,y\in S)\le\beta p_xp_y$ for $x\ne y$, with $\beta\ge0$;
it gives $C=\gamma+\beta$.
\end{theorem}

\begin{lemma}\label{lem:lift}
If $g(A)=\sum_Tw_T\ind\{A\cap T\ne\varnothing\}$ is a coverage function on
$X$, there is a nonnegative cut sum $\Delta_0$ on $X$ such that
$g(A)\le\Delta_0(A)\le2g(A)$ for $|A|\ge2$.
If its nonempty atoms form a partition, at most $4N$ cut coordinates suffice.
\end{lemma}

\begin{corollary}\label{cor:nonroot}
The square-root exponent is tight for unit-cost pairwise-intersecting
supply hypergraphs, even when their global edge intersection is empty.
If a unit-cost supply hypergraph has connected edge-intersection graph
of diameter $d$, its distortion is at most $4\max(1,d)\sqrt n$;
in particular diameter two gives $8\sqrt n$.
\end{corollary}
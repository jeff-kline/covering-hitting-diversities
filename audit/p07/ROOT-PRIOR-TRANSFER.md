# Independently checked prior consequence (root)
Primary source opened: https://timroughgarden.org/papers/approxxos.pdf, Appendix6,
Theorem6.1, PDFpages10–11. q groups Q_i of qpoints, f(A)=max_i |A intersect Q_i|.
For every submodular g satisfying f/alpha<=g<=f on all subsets, alpha>=q/2.
This is an existential all-subset approximation statement, not a sketch-size condition.
The source section header's O(sqrt n) wording is imprecise; use displayedtheorem.

Make all q^q fulltransversals (onepoint/group) into unit supply edges by addingr.
For rooted terminal sets {r}unionA, minimumconnectedcost equals minimumcovercost
and equalsf(A): everytransversal covers at mostonepoint/group; f(A)transversals
suffice by distributing eachgroup's selectedpoints among f(A) rows, filling others
arbitrarily. Everycollectionconnectedthroughr. Positive f onnonemptyA ensuresdiversity.
Given any l1embedding delta<=Delta<=Ddelta, orientitscuts awayfromr. g(A)=Delta({r}unionA)/D
is a nonnegative sum of hitting indicators and hence submodular; f(A)/D<=g(A)<=f(A).
Theorem6.1 gives D>=q/2. Thus an existential Omega(sqrt(vertexcount)) lower bound for
hypergraphSteinerdiversities follows from published2012 theorem (2011authorversion),
with n=q²+1 but exponential explicit supply representation. This is our inference
from primarysource+elementarytransfer, not a claim they stated a diversity theorem.
It rules out asserting new polynomial existential distortion growth in isolation.
The q²affinesupply explicitcompression remains a different novelty question; standard
pairwiseindependence is credited. The old bound is only logarithmic in exponential
hypergraphencoding and doesnotbyitself refute encoding-polylogConj1.7.

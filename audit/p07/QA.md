# Abstract and final PDF QA
Root inspected actual abstract render and reproduced the reported errors via
pdftotext -layout: radicals are emitted on preceding textlines by extraction.
There is no radical before 'incidence moments' in rendered PDF; 4sqrt(n) and
2sqrt(nH_n) are correct. The TeX source confirms their proper formula boundaries.
No formula changed merely to accommodate extraction order.

Final paper remains10pages13references. All10finalpages visuallyinspected at1050px;
clean two-passpdflatex with no warnings/undefined references/overfull/underfull boxes.
Bibliography on separate page. Generalconnectivity limitation now in introduction
before theorems. New priorconsequence and compactencoding distinction also visible
in introduction and proved/explained in Section9. No coretheorem/proof changed.
Unbounded costratio assertion checked internally: a unit path with endpoints as
terminals has covercost2 but connectorcost arbitrarilylarge.

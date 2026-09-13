# Finite q=3 figure audit

September 13, 2026 UTC. Read-only process-separated AI check; not independent
expert review. No must-fix findings within the assigned finite-example scope.

An independent modular-membership/bitset implementation, without importing
candidate code, confirmed:

- All 512 generated JSON rows, including 511 nonempty ratios and the empty
  set's undefined ratio.
- Maximum ratio 3/2, with exactly 18 maximizers: non-collinear triples meeting
  each column once.
- Selected T={(0,0),(1,0),(2,1)}, mask 137, hits three columns and six supplies:
  (0,0), (0,1), (1,0), (1,2), (2,0), (2,1).
- Enumeration of all 512 supply subfamilies gives minimum cover cost three
  for each rooted column. These covers are connected through the common root.
- All 27 grid-incidence dots in generated TikZ have correct positions/colors.
- The 5/3 bound holds for every enumerated subset; the example gives 3/2<5/3.

The generator, caption and README distinguish the exact q=3 maximum from the
general moment certificate. Finite enumeration does not establish that theorem.

Exposure: the examiner read candidate scripts, caption, README, generated TikZ
and JSON before completing its independent calculation. It did not read prior
audit verdicts, inspect the general proof, rebuild rendered images, assess
novelty, or modify candidate files. Root accepted these findings and separately
reviewed the rendering. Artifact hashes are pinned in MANIFEST.sha256.

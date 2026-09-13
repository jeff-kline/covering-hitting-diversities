# Publication checkpoint

Proposed repository: `jeff-kline/covering-hitting-diversities` (public).
Proposed default branch: `main`. Proposed annotated tag: `v0.1.0`.
Title: Covering versus hitting in diversity embeddings: an affine obstruction and matching bounds.
Creator: Jeff Kline. Version: 0.1.0. License: GPL-3.0-only.
Resource type for permanent archive: publication / preprint.

## Ownership

| Action | Owner / authorization |
|---|---|
| Local edits, checks, candidate commit | Root agent; authorized by preparation request |
| Repository creation | Root only after exact public authorization |
| Review-branch push | Not requested; requires separate explicit scope |
| Default-branch initial push | Root only after exact candidate authorization |
| Public annotated tag and GitHub Release | Root only after exact freeze authorization |
| Zenodo authenticated portal / enabling integration | User alone |
| Public archive verification | Root, read-only after public record exists |
| Living metadata and public-site listing | Separate later admission authorization |

## Selected route: Zenodo GitHub integration

Do not create a manual deposit or reserve a separate DOI. The CFF message is
timeless and omits DOI and date-released. The user must enable this repository
in Zenodo before the GitHub Release; no agent opens the authenticated portal.
If the route changes to manual upload, rebuild and re-audit a new candidate
with the user-reserved identifier visibly inactive before any immutable tag.

The proposed freeze bundle is limited to the following actions, at the exact
candidate commit presented to the user:

1. Recheck the local and authenticated GitHub name and create the public repository.
2. Push the audited candidate to main. Do not force-push over unexpected state.
3. Wait for the user's confirmation that Zenodo integration is enabled.
4. Create and push the annotated v0.1.0 tag at that exact commit using the
   established GitHub noreply identity; never move a public tag.
5. Generate git archive v0.1.0 twice and compare bytes. Download the canonical
   GitHub API zipball/v0.1.0 twice, require matching bytes, and pin its size and hash.
6. Create the GitHub Release to trigger Zenodo. Release notes must retain P1
   PARTIAL and the compact-priority qualification, with no claim of admission.
7. Read the public archive record, verify metadata and resolving version DOI,
   download its file, and compare it byte-for-byte to the pinned GitHub zipball.

Before requesting public authorization, inspect author and committer identities
for every outgoing commit. This is an initial repository with no remote base:
check all history using git log --format=fuller and validate both address fields
against the established noreply identity. The bundled release auditor's
--publish-base check is usable once a real remote base exists; do not invent one
or silently omit the initial commit from identity review. Inspect an annotated
tagger before pushing when the tag exists.

No public action is covered merely by this plan or the local preparation request.
The exact local commit and candidate audit result are delivered separately.
A later living-metadata/site admission bundle must state its exact commit and
approved actions after archive verification. P1's residual uncertainty remains
visible throughout.

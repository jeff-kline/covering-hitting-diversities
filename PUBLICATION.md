# Publication checkpoint

Repository: `jeff-kline/covering-hitting-diversities` (public).
Default branch: `main`. Proposed annotated tag: `v0.1.0`.
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
timeless and omits DOI and date-released. The user confirmed that this repository is enabled in Zenodo. This is
user-reported setup; no agent inspected the authenticated portal.
If the route changes to manual upload, rebuild and re-audit a new candidate
with the user-reserved identifier visibly inactive before any immutable tag.

The proposed freeze bundle is limited to the following actions, at the exact
candidate commit presented to the user:

1. Verify the existing public repository and remote main against the reviewed base.
2. Push the audited final candidate to main. Do not force-push over unexpected state.
3. Retain the author's confirmation that Zenodo integration is enabled.
4. Create and push the annotated v0.1.0 tag at that exact commit using the
   established GitHub noreply identity; never move a public tag.
5. Generate git archive v0.1.0 twice and compare bytes. Download the canonical
   GitHub API zipball/v0.1.0 twice, require matching bytes, and pin its size and hash.
6. Create the GitHub Release to trigger Zenodo. Release notes must retain P1
   PARTIAL and the compact-priority qualification, with no claim of admission.
7. Read the public archive record, verify metadata and resolving version DOI,
   download its file, and compare it byte-for-byte to the pinned GitHub zipball.

Before requesting public authorization, inspect author and committer identities
for every outgoing commit. This repository now has an actual origin/main base:
use the bundled release auditor with --publish-base origin/main and
--require-github-noreply. Initial publication identities were checked separately
before the first push. Inspect the annotated tagger before pushing the tag.

No public action is covered merely by this plan or the local preparation request.
The exact local commit and candidate audit result are delivered separately.
A later living-metadata/site admission bundle must state its exact commit and
approved actions after archive verification. P1's residual uncertainty remains
visible throughout.

## Completed freeze and next publication boundary

The exact authorized commit 8ce97341f77cf3c406c9a2909fc77ac6be085e8e was pushed,
tagged v0.1.0, and released. The Zenodo archive is publicly verified at
https://doi.org/10.5281/zenodo.22731697; ADMISSION.md records the checksums and
corrected metadata. The earlier sequence above is the retained freeze plan.

The next bundle is limited to the exact reviewed living-metadata commit pushed
to main. It does not move the tag, replace archive bytes, or publish a site.
The user authorized local preparation; the exact push is presented separately.

# Stop Slop Refined integration

Status, 4 October 2026: a [small local implementation proposal](proposal/README.md) and original fixtures are prepared. No changes, installations, issues or pull requests have been made in the upstream repository. The proposal checks declared review-input bytes; it does not change style rules or score fiction.

The private lab has since tested two optional fiction overlays; neither passed its advancement criterion. The [roadmap's campaign update](roadmap.md#campaign-evidence-update) now prioritizes exact revision records and separate assessment of repairs, preserved constraints and aesthetic disagreements. Those prototypes are not shipped upstream behavior.

The completed novel supplied concrete review/versioning problems for this bounded proposal. Its engineering checks demonstrate stale-input rejection, not improved reader experience. Broader contributions to [odinfree/stop-slop-refined](https://github.com/odinfree/stop-slop-refined) still need appropriate evidence. A cleaner count or fewer flagged phrases does not establish better fiction.

## Verified baseline

Inspected on 3 October 2026 through GitHub and a local reference clone; fetched again on 4 October before preparing the patch, with the same HEAD and `origin/main`:

- Default branch: `main`.
- Commit: [`1d384cd0b6577ce5ad15297c8e867334e0ba1af1`](https://github.com/odinfree/stop-slop-refined/tree/1d384cd0b6577ce5ad15297c8e867334e0ba1af1).
- Package version: `3.1.1` in `SKILL.md` and `README.md`.
- Package: a Markdown skill and references, a static browser workbench, and two Node scripts. The repository has no package manifest or automated literary-quality test runner at this revision.
- Validation: 14 written regression cases in `references/examples.md`; CI regenerates browser data and rejects drift in `docs/site-data.js`.
- Local read-only checks passed: `node --check` for `docs/app.js`, `scripts/generate-site-data.mjs`, and `scripts/build_revision_artifact.mjs`. These are syntax checks, not editing-quality evaluations. The 14 rewrite cases were inspected but not executed.

The local clone is under ignored `.local/reference/stop-slop-refined/`; it is research material, not a vendored dependency. The proposal was tested in separate scratch checkouts against this pin. Refresh it again before a later upstream contribution.

## What already works

The skill already protects supported claims, uncertainty, literal technical terms, useful repetition, intentional fragments, and an established voice. It distinguishes a review prompt from evidence of AI authorship. Its detect mode can return a clean pass without inventing faults. Preserve these behaviors.

The revision artifact records sentence edits but explicitly cannot explain section moves well. Keep that artifact for line editing and use a separate structural change record for scenes and chapters.

## What needs investigation

| Observed boundary | Research question |
|---|---|
| The documented contexts focus on nonfiction, technical, personal, and promotional prose; there is no fiction profile. | Which defaults need an explicit fiction route, and which transfer without change? |
| The AI-role guidance favors a human first draft for voice-sensitive work. | How can a contest requiring AI-generated prose retain human direction without asking the entrant to supply manuscript sentences? |
| Some word rules apply everywhere, while other rules already contain contextual exceptions. | When do literal objects, character speech, deliberate rhythm, or narrative distance justify keeping a flagged form? |
| The browser workbench counts lexical and regular-expression matches in one text input. | Which repeated phrases deserve attention across chapters, and which are purposeful motifs or stable character diction? |
| No explicit canon, chronology, character-knowledge, or scene-state review exists. | Which small, reviewable workflow additions help catch contradictions without inventing new story facts? |

These are scope gaps and testable hypotheses. We have not demonstrated that the current skill damages fiction or that the proposed additions improve it.

Two optional fiction overlays have now failed their private exploratory advancement checks. The [revision evidence update](../../research/notes/2026-10-03-revision-evidence.md) explains why action-label agreement, diagnosis and proposed repair need separate review. Some frozen labels also encode disputable rhythm preferences. Original counts are retained; neither overlay is proposed for adoption upstream.

## Contribution boundary

1. Investigate the contest and writing research before implementing upstream changes.
2. Record the passage-level problem, intended effect, candidate repair, reader judgment, and counterexample in this project.
3. Turn a useful lesson into an independently invented public fixture. Keep manuscript text, private prompts, and personal voice material out of the public package.
4. Add the smallest contextual rule that explains both the failure and the counterexample. Prefer opt-in fiction behavior over a global rewrite of short-form rules.
5. Recheck existing regression cases and build behavior before proposing a patch.

The [roadmap](roadmap.md) retains broader hypotheses and acceptance checks. Only the linked review-input proposal has been implemented locally. Its [independent review](../../book/reviews/2026-10-04-stop-slop-proposal-review.md) retains an actual failed CLI invocation and the subsequent repair check. No upstream submission has been made.

## Pinned sources

- [Router, editing order, voice, profiles, and maintenance](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/SKILL.md)
- [AI-role guidance and limits of its cited research](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/references/ai-role-and-reader-fit.md)
- [Examples and 14 regression cases](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/references/examples.md)
- [Word tiers and hard house rules](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/references/words.md)
- [Browser detection implementation](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/docs/app.js)
- [Revision artifact boundary](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/references/revision-artifact.md)
- [Existing CI](https://github.com/odinfree/stop-slop-refined/blob/1d384cd0b6577ce5ad15297c8e867334e0ba1af1/.github/workflows/site-data-sync.yml)

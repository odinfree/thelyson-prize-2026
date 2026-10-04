# Selected-book workflow

Updated 4 October 2026. Applies to *The Fifteenth Year*. Read the [brief](../book/brief/creative-brief.md), [plan](fifteenth-year-next-steps.md), [milestones](goals.json), and [resume record](RESUME.md) before substantial work. This workflow does not run on a timer.

## Ownership without overlapping edits

| Role | Owns | Boundary |
| --- | --- | --- |
| Integrator | Brief, goals, outline, timeline, provenance and merges | Assign exact paths and reconcile sources before merging |
| Scene author | One assigned new scene or candidate revision | Preserve input version and brief; do not change the outline or another writer's scene silently |
| Researcher | Scene-specific factual notes and sources | Separate researched facts from invented world rules; no manuscript edits |
| Reviewer | Separate notes on an immutable candidate | Identify exact problems and retained ambiguity; do not rewrite the candidate during review |
| Human reader/director | Concept preference, criticism, intended experience | Record received input separately; AI composes any resulting manuscript wording |

Roles may run sequentially. A separate agent can research or review while the author works when scopes are independent. Use an existing suitable worktree or `codex/` branch, and assign exclusive paths before parallel edits. Root integrates and pushes reviewed work under the existing project authorization. Do not start duplicate writers on the same scene or infer that more reviewers establish human agreement.

## A scene cycle

1. Read the current outline card and required preceding prose. Identify source versions, outstanding actions, time window, objects and knowledge limits.
2. Write a small scene brief: intended change, characters' immediate desires, constraints to preserve, and any unresolved factual question. Research only what affects the scene.
3. Generate original English prose. Retain its source, candidate and actual authoring method. Use known model labels; leave unavailable snapshots/seeds/tokens unknown.
4. Review the actual scene for consequential action, viewpoint, continuity and the stated brief. Assess optional aesthetic preferences separately. An authentic quotation alone does not prove an interpretation.
5. Apply a bounded repair if needed. Inspect both the target and collateral changes, including within the edited paragraph. Keep an unsuccessful candidate and the reason it failed.
6. Produce a German reading version in chat when useful to the user's reading sequence. Text only; no automatic audio. Translation feedback becomes an editorial note, then an AI revision to the English source if adopted.
7. Update continuity, outline consequences and the generation log for substantive source changes. Record translation provenance separately if it is saved as a durable artifact. Never silently overwrite the pinned development baseline.
8. Validate changed links/structured records and relevant tooling, commit, merge as appropriate, push and verify the remote head. Update goals with evidence and RESUME with one next action.

## From development to manuscript

The two original development sources remain pinned in the private lab and were deliberately imported into chapter 1 with provenance. The complete public manuscript now has 22 chapters and a [final manifest](../book/reviews/final-manifest.json). Preserve the private development baseline and first-draft Git commit when making later revisions. Count manuscript prose separately from chapter headings, notes and reading translations.

Structural revision reads the whole arc before sentence polishing. Maintain separate factual continuity, character-knowledge and artistic questions. A brief, outline or promising sample does not certify a novel-length payoff. Once manuscript tooling exists, use relevant word-count/order/export checks; do not add tests that assert literary taste.

## Milestone and resumption rules

`goals.json` is the authoritative milestone status. `queued` means planned, `active` means being worked on, `complete` requires the stated evidence, and `awaiting_instruction` applies to external submission. Dates are targets, not proof of work or automatic scheduling. If a target slips, record the reason and revise the plan while protecting structural revision and packaging time; do not pad prose to keep a number.

At each session end, record the current branch/commit or evidence path, completed work, unresolved decisions, any owned live jobs and the next action. No service campaign is active now. A later service experiment needs its own bounded allocation, not the closed campaign's ledger.

The public repository remains public. Submission, contact messages, payments, wallets and market activity require the relevant later user instruction. Prepare reviewable materials first. Submitted and accepted remain separate states.

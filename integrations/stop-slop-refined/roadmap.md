# Research-to-contribution roadmap

Status: proposed work, 3 October 2026. Baseline: [`1d384cd0b6577ce5ad15297c8e867334e0ba1af1`](https://github.com/odinfree/stop-slop-refined/tree/1d384cd0b6577ce5ad15297c8e867334e0ba1af1). No implementation is included in this plan.

## Campaign evidence update

The private lab implemented and tested two optional fiction overlays. Neither passed its advancement criterion; the [revision evidence note](../../research/notes/2026-10-03-revision-evidence.md) preserves the failures and disputed labels. The candidate patches below remain proposals, not a queue of approved upstream changes. No third overlay or browser feature is justified by those runs.

The more promising transfer is a small review-record extension: distinguish diagnosis, proposed operation, actual revised prose, constraint preservation and aesthetic preference. A bounded actual repair has now been independently assessed by another AI reviewer and replayed through source persistence and the review ledger. This demonstrates interoperability and exact revision binding, not better human-rated writing. Before an upstream patch, use new public fixtures and test a repair that fails despite a plausible diagnosis, an unchanged quote with changed attribution, and an unresolved preference dispute. Keep private manuscript material out of those fixtures.

| Proposed transfer | Current evidence | Next acceptance evidence |
| --- | --- | --- |
| Fiction-specific style route | Two diagnostic overlays did not advance | Fresh comparison of actual applied revisions, with repair and preservation assessed separately |
| Source and revision identity in review records | Working private prototype and actual-repair replay | Small public fixture demonstrating stale-review rejection without claiming semantic validation |
| Separate aesthetic disagreement from requirement failure | Three diagnostic labels remained disputable on audit | A public example retaining both interpretations without forcing a universal rewrite rule |
| Reader comparison guidance | Four-opening packet prepared; no participants or responses | Actual reading evidence with exposure, order and missingness retained |

These are implementation priorities inferred from local evidence. They do not establish a literary advantage or change the upstream skill.

The later [64-presentation evidence-window comparison](../../research/notes/2026-10-03-evidence-window-results.md) adds two required counterexamples for any future review-record extension: a genuine quotation used for an unsupported inference, and a full-source-correct answer unsupported by the excerpt actually supplied. A quote link or matching label must not automatically approve a repair. Record the supplied evidence boundary alongside source revision identity, and preserve a separate semantic assessment.

The subsequent [typed-claim pilot](../../research/notes/2026-10-03-typed-claim-results.md) adds a narrower engineering lesson: bind a fidelity assessment to the exact claim program it reviewed, and reject a changed program paired with a stale assessment. Its small semantic gain clusters around one conjunction; a new timing error and one malformed response remain. Preserve attempts, complete pairs and failure costs separately. This supports inspectable review records, not automatic acceptance of a typed verdict.

## First: establish the evidence

Read the contest rules and investigate AI-assisted creative writing, long-form narrative evaluation, stylistic diversity, revision, and reader response. Read the original studies before extending claims from advertising copy or social replies to novels. The existing AI-role reference already warns against overgeneralizing its evidence; preserve that discipline.

For each proposed lesson, keep a record with:

| Field | Required content |
|---|---|
| Question | The specific reader problem or process failure under investigation. |
| Source | URL or bibliographic identifier, access date, study population/task, and stated limitations. |
| Status | Observation, hypothesis, tested local finding, or rejected idea. |
| Passage evidence | Stable scene/revision identifiers and exact affected span in the contest project. |
| Intended effect | What the sentence or scene should make possible for the reader. |
| Comparison | Original and candidate revision, with the same surrounding context. |
| Evaluation | Who reviewed it, which version they saw, their reasoning, and any unresolved disagreement. |
| Counterexample | A case where the apparent problem should be preserved. |
| Transfer | A new public fixture and the smallest proposed upstream change. |

Use paired comparisons with order varied when practical. Evaluate meaning, reader comprehension, narrative effect, and voice separately. Keep a worse revision and a rejected rule as negative evidence. A model score or a preference from one scene is exploratory evidence, not proof of a general improvement. Synthetic fixtures test a rule's behavior; they do not establish artistic quality.

## Candidate patch 1: an explicit fiction route

**Observed issue:** `SKILL.md` has no fiction context profile. `references/ai-role-and-reader-fit.md` routes voice-sensitive work toward a human first draft. That default needs a defined exception for an AI-prose-only contest workflow.

**Hypothesis:** a short opt-in route can preserve useful critique and human direction while satisfying the project's authorship constraints.

**Proposed targets:**

- Amend `SKILL.md` mode/context routing.
- Amend `references/ai-role-and-reader-fit.md` with a scoped route for AI-generated fiction under explicit authorship constraints.
- Add `references/fiction.md` for narrative intent, point of view, canon, and revision order.
- Extend `references/examples.md` with an AI-only contest scenario.
- Update `README.md` and `CHANGELOG.md` only when the behavior is implemented.

**Behavior to test:** human choices may supply premise, constraints, outlines, criticism, and selection; all manuscript prose and textual corrections are generated by AI when the applicable rules require it. Do not ask the entrant to rewrite a passage themselves. Compare materially different AI-generated approaches before investing in line edits. Keep the authorship record in the contest project rather than making it a public skill dependency.

**Acceptance:** the new route is explicit; nonfiction defaults remain intact; the workflow does not imply that AI-first drafting is proven superior, that a prompt proves authorship, or that a contest entry is automatically compliant. Confirm the actual contest wording before drafting this exception.

## Candidate patch 2: protect purposeful fictional language

**Observed issue:** the skill already protects intentional fragments and useful repetition, but its global hard-word rules and broad actor-first guidance lack a fiction-specific treatment. `references/words.md` bans literal uses of `surface` in drafted prose; `references/patterns.md` tells a passive-voice sentence to lead with the actor.

**Hypothesis:** context-aware exceptions can avoid flattening narrative distance, character diction, uncertainty, and deliberate rhythm.

**Proposed targets:** `references/fiction.md`, `references/patterns.md`, `references/words.md`, and `references/examples.md`. Do not quietly weaken the current hard-word behavior for existing profiles. Case 14 remains unchanged for its current default profile; a fiction exception requires an explicit profile and paired case.

**Invented fixture directions, to develop later:**

- A literal physical object uses a flagged word accurately; a vague promotional use still needs revision.
- A passive construction withholds an unknown actor without inventing the culprit.
- Interrupted dialogue earns a dash; decorative punctuation added to every sentence does not.
- A repeated phrase changes meaning with each recurrence; a redundant paraphrase adds no narrative effect.
- Two characters have distinct syntax and vocabulary; cleanup preserves their differences.
- An unreliable narrator makes a false claim; the editor distinguishes characterization from a canon contradiction.
- A triad, fragment, metaphor, or distant narrator has an articulated purpose; no numeric ban overrides that purpose.

**Acceptance:** every added exception includes a keep case and a repair case. Every repair preserves the original proposition or intended narrative ambiguity, emotional force, and relevant information. Fewer flagged words alone cannot pass the evaluation.

## Candidate patch 3: scene and chapter review

**Observed issue:** the current final-reader pass addresses prose, claims, and reader fit. It has no explicit cross-scene chronology, character-knowledge, or object-state workflow. The sentence diff explicitly excludes structural moves.

**Hypothesis:** a lightweight optional review can catch consequential contradictions and empty scenes before sentence cleanup.

**Proposed targets:** extend the new `references/fiction.md`; add `references/fiction-examples.md` if the cases outgrow the existing examples; add a routing link in `SKILL.md`. Explain structural records in `references/revision-artifact.md` without overloading its sentence-record schema.

**Review order to test:**

1. State the scene's intended change, viewpoint, and unresolved question. Do not require every scene to follow the same beat pattern.
2. Compare chronology, location, object states, and character knowledge with the supplied canon. Cite the conflicting scene identifiers.
3. Separate deliberate withheld information from contradiction. Mark missing context as unknown; do not invent a repair fact.
4. Inspect recurring scene openings, endings, imagery, emotional explanations, and dialogue rhythms across adjacent chapters.
5. Revise structure before sentences. Recheck affected canon after the change.
6. Produce the existing sentence artifact only for an appropriate line-edit pass. Record moved or removed scenes separately.

**Acceptance:** invented two-scene fixtures catch a planted contradiction and preserve a deliberate reveal; a motif survives review; detect mode produces no rewrite; no canon is inferred from an absent passage. Store actual manuscript maps in this project, not upstream.

## Candidate patch 4: browser support, only if evidence warrants it

**Observed issue:** `docs/app.js` reports lexical and regex matches in a single input. `scripts/generate-site-data.mjs` generates its data from the word and pattern references. There is no context-profile selector or chapter-aware state in that implementation.

**Hypothesis:** an optional profile with contextual explanations may be useful. Automatic novel rewriting, an AI-authorship score, and a numeric literary-quality score are outside this proposal.

**Possible existing targets:** `docs/app.js`, `docs/index.html`, `docs/styles.css`, `scripts/generate-site-data.mjs`, generated `docs/site-data.js`, and `.github/workflows/site-data-sync.yml` if validation needs extending.

**Possible new targets:** `tests/fixtures/fiction.json` and `scripts/check-fiction-fixtures.mjs`, only after defining what deterministic behavior the checks can meaningfully verify. These files and a test command do not exist at the inspected revision.

**Acceptance:** the current default keeps its documented behavior; fiction prompts explain their uncertainty; counts are review prompts rather than verdicts; text remains inspectable; public examples contain no manuscript material. Do not build this until the earlier evidence shows a useful interaction that the existing skill cannot provide.

## Verification for a future contribution

Refresh the baseline, inspect intervening changes, and read the current upstream contribution guidance. Use a separate branch and review a small patch at a time.

Run the existing documented checks from the future upstream working checkout:

```bash
node scripts/generate-site-data.mjs
git diff --exit-code -- docs/site-data.js
node --check docs/app.js
node --check scripts/generate-site-data.mjs
node --check scripts/build_revision_artifact.mjs
```

The generator writes `docs/site-data.js`. After a deliberate reference change, regenerate and review that file, include it in the candidate commit, then run the generator and drift check again against that candidate. A changed generated file during development is not by itself a bug.

Run all 14 existing manual regression cases in `references/examples.md` and the new fiction cases with the intended profile. Record the model/version, prompt, output, and assessment so a result can be reviewed. Do not report these cases as automated tests or infer literary quality from the JavaScript syntax checks.

If browser code changes, verify default detection, the selected profile, empty input, deliberate exceptions, generated-data consistency, and rendering. If the revision builder changes, verify its existing record validation and safe HTML embedding using invented text. Add narrowly scoped automated checks only for new deterministic behavior.

Before a proposed upstream pull request, confirm:

- The rule solves an observed problem and has a counterexample.
- Any literature claim states its actual task and limits.
- Existing factual boundaries and short-form behavior still pass.
- Fiction fixtures are independently invented and contain no private prose or voice profile.
- Documentation distinguishes a shipped change, a local experiment, and an untested hypothesis.

The initial output of this workstream is a researched proposal. A later implementation should be driven by the writing evidence, with the current contest rules rechecked before relying on any authorship route.

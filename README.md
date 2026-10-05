# Thelyson Prize 2026

A public workspace for our entry to the [Thélyson Orélien Prize for New Writing](https://thelyson.ai/): research the contest, develop an original book, write and revise it with AI, and preserve what we learn.

**Stage, 5 October 2026:** *The Fifteenth Year* is a complete, revised English novel: **22 chapters and 44,552 prose words**. The first draft is preserved at commit `38e7942b5e4e6fe62baec71101f860efac34eeef`. A whole-book review led to bounded revisions, which separate agents checked against the actual changed prose. The [final manifest](book/reviews/final-manifest.json) records the current order, count and source hashes. The revised manuscript is preserved at `e739f40896e8b08828bf22e8809dcc0873998225` on public main. **The verified [entry package](submission/README.md) was submitted on 5 October 2026; the official receipt is confirmed. Eligibility and judging remain unconfirmed.** See the public [submission status](submission/status.json).

Read from [chapter 1](book/chapters/01-seven.md), or start with the [book guide](book/README.md), [resume record](planning/RESUME.md) and [goals](planning/goals.json). The user chose the concept and authorized autonomous completion. The subsequent setting, plot and wording are AI decisions; no human approval of the complete novel or contest score is claimed.

The advertised deadline is **31 October 2026, 23:59 Anywhere on Earth** — **1 November, 12:59 Europe/Zurich**. The published rules require an English PDF of **40,000–120,000 words** whose wording is entirely AI-generated. Human planning and editorial feedback are allowed. These core conditions were rechecked **4 October 2026** in the [package-stage rules check](contest/2026-10-04-package-check.md); that dated preparation record remains separate from the submission status.

## Start here

1. Read the [contest dossier](contest/README.md), especially its unresolved questions.
2. Follow the [research agenda](research/README.md) for the source register and dated findings on long-form generation, revision, reader evidence and retrieval.
3. Follow the [selected-book plan](planning/fifteenth-year-next-steps.md), [workflow](planning/workflow.md), and [persistent milestones](planning/goals.json).
4. Keep the [authorship record](provenance/README.md) from the first manuscript passage onward.
5. Capture transferable lessons in the [Stop Slop integration plan](integrations/stop-slop-refined/README.md).

## Layout

```text
contest/                       Rules, selection, context, unanswered questions
research/                      Reading agenda, source register, dated synthesis
planning/                      Milestones and decisions
book/
  brief/                       Premise, audience, form, voice, constraints
  outline/                     Structure and scene sequence
  chapters/                    AI-authored manuscript source
  continuity/                  Characters, chronology, knowledge, unresolved threads
experiments/                   Small comparisons before adopting a writing method
provenance/                    Model/method records and human editorial input
submission/                    Entry checklist; local exports and receipts
integrations/stop-slop-refined/ Evidence and plan for later public skill improvements
templates/                     Source, experiment, and generation-record templates
scripts/                       Manuscript assembly, checks and PDF export tooling
```

## Working approach

The initial research campaign informed the process; the user chose the book. The [whole-book review](book/reviews/2026-10-04-whole-book-review.md) assessed the complete arc before sentence changes. [Early/middle verification](book/reviews/2026-10-04-revision-01-a-verification.md) and [late-chapter verification](book/reviews/2026-10-04-revision-01-c-verification.md) record the actual repair checks and their limits. Counts and hashes cannot certify literary quality, originality or authorship. The [3 October synthesis](research/notes/2026-10-03-campaign-summary.md) preserves the closed research campaign, including unsuccessful methods; its automation and allocation have not been restarted.

The human can direct and critique; the AI writes and revises all manuscript wording. Store feedback separately and record how it changed the draft. Preserve intended meaning, force, and useful rhythm during editing. Never make prose bland merely to remove a flagged pattern.

Keep full third-party works out of this repository. Cite sources and write original summaries. Keep credentials, personal contact details, payout details, and submission receipts in ignored local storage.

This repository is public by the user's choice, including committed manuscript drafts. Publication-history eligibility remains an [open contest question](contest/open-questions.md), not a stated restriction. A [local Stop Slop proposal](integrations/stop-slop-refined/proposal/README.md) translates a demonstrated review-context problem into a small input-checking utility with original fixtures. It has not been contributed upstream. The user separately authorized the completed submission on 5 October. Receipt confirmation does not establish eligibility or a judging outcome. No monitoring or resubmission automation has been created.

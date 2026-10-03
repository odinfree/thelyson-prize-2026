# Revision evidence: what to measure before adding more critique

Checked 3 October 2026, following the [frontier update](2026-10-03-frontier-update.md). This note combines primary-source findings with explicitly exploratory private-lab results. The underlying private prototypes and raw runs are not published as a public benchmark here.

## Feedback, repairs and reader outcomes differ

| Primary source | Useful evidence | Transfer limit |
| --- | --- | --- |
| [Feedback-Only AI for Writing Instruction](https://journals.sagepub.com/doi/10.1177/23294906251414835), February 2026 | Human students' revised narratives were preferred in blind before/after comparisons. | No unaided-revision control; students wrote the revisions. This does not test an autonomous AI fiction editor. |
| [LLM Review](https://arxiv.org/html/2601.08003v1), January 2026 | Tests private revisions after peer feedback and ablates iteration count. | Human ratings cover the candidate arm, not a comparative test of initial drafts and alternatives. Additional rounds are not automatically beneficial. |
| [Modifying LLM Post-Training for Diverse Creative Writing](https://arxiv.org/html/2503.17126v1), March 2025 | Human judges preferred the diversity of sets produced by the proposed training method. | Judges saw summaries. Prose voice was not tested; an inconclusive quality comparison leaves the tradeoff unresolved. |
| [Generating Constructive Feedback on Stories via Reinforcement Learning](https://arxiv.org/html/2609.04824v1), September 2026 | Human raters found some trained feedback more constructive; actionability alone exceeded the combined reward. | Feedback was rated; its implementation in revised stories was not evaluated. |
| [LitBench](https://arxiv.org/pdf/2507.00769), July 2025 | A separate human study provides some support for a trained story-preference evaluator. | Its upvote-derived benchmark and fresh-story human experiment are different endpoints. Neither certifies an individual repair. |
| [The Limits of Automatic Evaluation of Creativity](https://arxiv.org/pdf/2608.23705), August 2026 | Reports weak agreement between human creativity judgments and the tested automatic methods. | The LLM judge was one specific model; short-story results cannot establish the performance of every evaluator or a whole novel. |

These sources justify testing critique, while separating its effects. A useful instruction can produce a poor edit. A preferred edit can alter a protected fact. Increased variation across plot summaries does not necessarily preserve distinct prose voices.

## What the private pilots exposed

Two opt-in fiction overlays were compared against pinned Stop Slop instructions using original paired keep/repair examples. Neither met its prospectively recorded advancement criterion. The second comparison returned 14/16 original-key action matches for baseline and 12/16 for the overlay. Those figures describe a small synthetic diagnostic set, not literary quality or a general accuracy estimate.

The subsequent audit preserved the original keys and counts but challenged three labels that partly equated connected syntax with clear chronology or continuous movement. Fragmentation can be an editorial preference rather than a missing fact. Other failures were less ambiguous: a generic reflection was defended as potentially thematic despite an explicit immediate-discovery requirement; a matching `revise` action proposed a forbidden later outcome. Correct action labels concealed incorrect operations.

Exact quotations were present in both sound and unsound diagnoses. Source linkage is therefore a necessary mechanical check, not sufficient semantic evidence. A high-probability typed answer can also be confidently wrong. Small short-source success did not establish reliability on a longer passage with competing time and belief information.

No overlay is being adopted into the upstream skill on this evidence. No actual human reader outcomes or contest scores exist for these pilots.

## A more useful structure

Keep these records separate:

1. **Intent and constraints:** what the author requires, what remains deliberately unknown, and which effects are preferences rather than obligations.
2. **Diagnosis:** the exact passage, applicable requirement and interpretation connecting them; include reasonable disagreement.
3. **Proposed operation:** which defect it targets and what it must preserve. A suggestion is not an applied revision.
4. **Actual revision:** immutable before/after text, affected spans and new commitments.
5. **Review:** repair success, collateral damage and aesthetic preference recorded independently, with the reviewer's provenance.

For narrative state, source changes should invalidate dependent claims for review. An unchanged quotation may sit inside a newly negated sentence or belong to a different speaker. Automatically relocating its text does not renew its meaning. Conversely, an invalidation queue should preserve historical evidence rather than silently erase it.

The current deterministic prototype propagates staleness through declared dependencies. It cannot discover omitted dependencies or certify a new interpretation. Its next integration test uses a retained approximately 1,000-word draft and actual revisions, extending beyond sentence-sized controls without claiming novel-scale validation.

## Creative work and next decisions

Three original openings now explore an orchard harvest, a comedy revival and a one-day return after fifteen years. Independent AI reviews found useful staging and disclosure questions; they are not reader tests. A fourth concept follows a team building a night-bus service and broadens the portfolio toward collective discovery and accomplishment. These are private research drafts, not a selected entry.

The next useful decisions are which story deserves expansion, which precise revision improves its intended effect, and whether readers want to continue. Research can improve the process and expose unreliable shortcuts. It cannot choose a winning book from an automatic score.

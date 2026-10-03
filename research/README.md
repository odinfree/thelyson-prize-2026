# Research

For the current decisions, start with the [3 October campaign synthesis](notes/2026-10-03-campaign-summary.md).

Begin with the [contest dossier](../contest/README.md), [initial AI-fiction review](notes/2026-10-03-ai-fiction-baseline.md), and [October frontier update](notes/2026-10-03-frontier-update.md). The update covers the September novel-length preprints, verified limits, and early diagnostic experiments. This is a growing research base, not an exhaustive literature review.

The later [revision evidence update](notes/2026-10-03-revision-evidence.md) distinguishes useful feedback, valid repairs, prose preference and diversity. It records unsuccessful editing hypotheses as well as the next implementation questions.

The [retrieval boundaries note](notes/2026-10-03-retrieval-boundaries.md) examines confident errors, fallback retrieval and the risk of turning inferred narrative time into canon.

The completed [evidence-window comparison](notes/2026-10-03-evidence-window-results.md) found lower prompt-token use without better semantic agreement. It also records answers that matched a full-story key despite missing support in the excerpt actually shown.

The later [typed-claim comparison](notes/2026-10-03-typed-claim-results.md) found a narrow benefit concentrated in variants of one conjunction, alongside a new timing error and a retained output failure. It separates complete pairs, failed attempts and quotation accuracy.

## Agenda

| Priority | Question | Evidence to seek | Output |
| --- | --- | --- | --- |
| 1 | What exactly are we entering? | Current official rules, entry form, judging details, publication and rights terms | Contest dossier and unresolved questions |
| 2 | How can a long AI-written book remain coherent? | Primary studies of hierarchical planning, state tracking, long-context generation, and revision | Candidate methods with explicit limitations |
| 3 | What do readers value in AI-assisted stories? | Study designs, human ratings, narrative length, reader populations, diversity measures | Reader rubric and testable hypotheses |
| 4 | What does generic prose cost this particular story? | Original samples and before/after reader comparisons | Context-sensitive editing guidance |
| 5 | What does our eventual setting require? | Reliable domain sources selected after the creative brief | Fact notes separated from invented story facts |
| 6 | What can improve the public skill? | Replicated results across original examples and counterexamples | Bounded implementation proposals |

## Evidence records

- `sources/contest.json` records the contest sources checked during setup.
- `sources/literature.json` records primary writing research.
- `notes/` holds dated synthesis with inline source links.
- Use the [source template](../templates/source-note.md) for deeper reading.

Every material claim should link to a source. Label organizer statements as such; label our deductions as inferences. Record when a claim was checked and what remains uncertain. A paper using short stories or earlier models does not establish performance on our novel.

Keep source summaries original and concise. External pages can change: recheck requirements before submission. Full-page downloads or copyrighted PDFs, if needed for private study, belong in ignored `.local/` storage rather than the GitHub repo.

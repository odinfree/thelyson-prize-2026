# Optional review-input binding — local proposal

Prepared 4 October 2026. **Proposed patch only; not contributed or installed upstream.** The primary book work remains separate. This adds a deterministic input-identity preflight, not a fiction style overlay, literary score, or replacement for editorial judgment.

## Problem and smallest change

A saved review may refer to a source, candidate and surrounding context that have since changed. Reusing its conclusion without checking those inputs can conceal that mismatch. The [development review](../../../book/reviews/2026-10-04-development-review.md) found that the independently useful boat-shed candidate could not simply be inserted later: earlier chapters had already disclosed the house sale, changed Flora's clothes and moved the scene to the afternoon; the paddle and rowing equipment also needed reconciling. During complete drafting, the adjacent concert chapters gave incompatible accounts of whether Flora remembered her promise. Both sources were needed to see that conflict.

The proposed utility checks a manifest's declared files against SHA-256 before a workflow reuses its review. It requires source and candidate roles and permits multiple context inputs. A change to any declared input rejects the check. The existing HTML builder, browser behavior, skill routing and lexical rules remain untouched. One optional section is added to the revision-artifact reference so the checker is discoverable.

This is a **retrospective engineering demonstration** motivated by actual revision problems. It was not used prospectively to prevent those mistakes, and there is no controlled evidence that it improves prose, reader preference or contest scores. It also cannot discover an omitted chapter or detect the semantic contradiction between two unchanged chapters. Declaring sufficient context and reviewing it remain separate responsibilities.

The [learning-origin record](learning-evidence.json) pins the adjacent chapters to the frozen first-draft commit, so later manuscript repairs do not silently replace that evidence. It contains metadata and a summary, not copied manuscript passages.

## Files and use

- [Applicable patch](review-input-binding.patch) targets upstream commit `1d384cd0b6577ce5ad15297c8e867334e0ba1af1`.
- [Standalone Node utility](files/scripts/check_review_inputs.mjs) reads files without changing them.
- [Node tests](files/tests/check_review_inputs.test.mjs) exercise match/rejection behavior and CLI outcomes.
- [Public fixture directory](files/tests/fixtures/review-inputs/) contains newly invented depot notices, no novel text or private prompts.
- The [patch](review-input-binding.patch) includes a short optional section for `references/revision-artifact.md`; its relative links are evaluated inside the upstream tree.
- [Actual validation commands and results](validation-commands.json) retain local run evidence. Workspace paths are represented by `{PROJECT_ROOT}` in that record.
- [Validation summary](validation-summary.json) records the passing checks and the author-stage independent-review status; the later completion is recorded below.

Run directly from this proposal's `files/` directory:

```sh
node scripts/check_review_inputs.mjs \
  --manifest tests/fixtures/review-inputs/unchanged.json \
  --root tests/fixtures/review-inputs
node --test tests/check_review_inputs.test.mjs
```

Inputs are exact bytes, including line endings. The manifest has version 1, an identifying `review_id`, and unique input IDs with roles, relative paths and lowercase SHA-256 values. The root is explicit. The checker rejects missing roles, duplicate IDs, bad hashes, absent paths, missing/nonregular files, absolute/traversal paths and symlinks resolving outside the root. It returns `declared_inputs_match` rather than approval. Invalid or stale inputs produce exit 1 and JSON on stderr.

Matching bytes do not authenticate a reviewer or manifest, assess a review's reasoning, bind the review's own prose, prove all relevant context was supplied, or prove that files stayed unchanged between separate operations. Use trusted immutable snapshots. The checker is not a filesystem security sandbox, an atomic snapshot mechanism, or protection against concurrent mutation. Never refresh hashes merely to make an old review pass; review the new inputs and record a new manifest.

## Method and evidence

Applied the local `typesafe-ai` skill's direction to keep known rules in code and test small composable behavior. No Jev, API inference, GPU or new spending was used. The [live documentation index](https://docs.typesafe.ai/llms.txt) was read on 4 October; the detailed building-guide/state pages failed in the web reader, and no current SDK/API claim is made. This patch has no TypeSafe dependency.

The upstream README and revision-artifact documentation were read at the pinned commit. No upstream `AGENTS.md` was present. The root agent had freshly fetched that reference; HEAD and origin/main both matched the pin. All changes were assembled and tested in ignored scratch clones, leaving the reference checkout clean.

Validation completed with Node **v26.8.1**:

- **18 Node tests passed**, including unchanged inputs, stale source/candidate/context, changed line endings, optional context, absent required roles, malformed manifests, duplicate IDs, invalid hashes, invalid files, path traversal, symlink escape and CLI failures.
- `git apply --check` passed against a pristine checkout of the pinned upstream. The patch was then applied there and all tests passed again.
- Existing JavaScript syntax checks passed; browser-data regeneration produced no `docs/site-data.js` drift.
- The existing revision builder produced identical HTML before and after the patch for an original fixture containing a literal script-closing string. Its existing safe embedding remained present. This is a bounded compatibility check, not exhaustive builder coverage.
- `git diff --check` passed. The original reference checkout remained unchanged.

Patch SHA-256: `fee91932f93a2abebe5d45c2404848a91f502bf18bde23fa7572b0e5e6d23ba0` (22,977 bytes).

Independent review rejected version 1 despite its 15 passing tests: invoking the CLI through a filesystem symlink silently skipped validation and exited 0. The repaired entrypoint compares resolved real paths. Three added tests exercise unchanged, stale and malformed manifests through a symlink, both with Node's default behavior and `--preserve-symlinks-main`. The [rejected patch](history/review-input-binding-v1.patch) and [original test summary](history/validation-v1-summary.json) remain available; passing that earlier suite did not establish complete invocation coverage.

Independent recheck of version 2 remains required before marking the transfer milestone complete. No upstream push, pull request or merge is claimed.

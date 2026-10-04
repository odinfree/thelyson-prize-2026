# Stop Slop proposal — independent review

Reviewed 4 October 2026 by Codex agent `/root/setting_and_reading`; exact model label unavailable. Review scope: the [local proposal](../../integrations/stop-slop-refined/proposal/README.md), its implementation, tests, original fixtures, upstream patch and recorded evidence. No implementation, manuscript or reference-checkout changes were made by this reviewer.

**Current disposition: the repaired version 2 has no remaining actionable finding in this bounded review.** The reviewer reproduced one CLI failure in version 1 and independently verified its repair. Both patch identities and the failure history are retained; byte identity is not semantic approval.

## SS-01 — medium, repaired: a symlinked CLI entrypoint silently skipped validation

Original location: `files/scripts/check_review_inputs.mjs`, lines 139–141. The guard compares lexical `path.resolve(process.argv[1])` with `fileURLToPath(import.meta.url)`. Node resolves an entrypoint symlink for the module URL but retains the alias in `argv[1]`, so the guard is false and `main` never runs.

With identical arguments naming `stale-candidate.json` and the fixture root:

| Invocation | Exit | Output |
| --- | --- | --- |
| `node /actual/path/check_review_inputs.mjs ...` | 1 | JSON rejection, `STALE_INPUT`, on stderr |
| `node /symlink/to/check_review_inputs.mjs ...` | 0 | Empty stdout and stderr |

A caller relying on the exit code could therefore proceed after no input check. This is a CLI invocation failure, distinct from the correctly tested rejection of an **input file** symlink escaping the root. A consumer that also requires a valid `declared_inputs_match` response would detect the empty response.

Requested repair was to resolve both entrypoint identities or separate the CLI wrapper, with successful, stale-input and malformed-input symlink regression cases. Version 2 compares the real paths of both identities and adds the three regression tests. Each test runs with default Node behavior and with `--preserve-symlinks-main`.

## Version 1 checks actually performed

The reviewer used a separate ignored scratch clone at upstream `1d384cd0b6577ce5ad15297c8e867334e0ba1af1`. The read-only reference clone stayed clean, with local HEAD and `origin/main` at that pin. No fresh remote fetch was performed by this reviewer.

- All **15 existing tests passed** under Node **v26.8.1**, both directly and after applying the patch.
- `git apply --check` passed on the pristine baseline. Applying the patch yielded all 12 proposed implementation/test/fixture files byte-for-byte. No existing builder, template, router, browser implementation or data-generation code changed.
- Existing JavaScript syntax checks passed. Browser-data regeneration produced no tracked data drift, and `git diff --check` passed.
- A separately invented builder fixture included keep/edit/delete records and a literal `</script><script>` sequence. The existing builder produced identical HTML before and after the patch; encoded script-closing text remained in the data. This verifies that specific compatibility claim, not every builder behavior, browser rendering or security property.
- Both manuscript-origin SHA-256 values in `learning-evidence.json` match the stated first-draft Git commit `38e7942b5e4e6fe62baec71101f860efac34eeef`. The record correctly calls the utility a retrospective demonstration; it does not claim the checker detected or prevented the original semantic contradiction.

Original reviewed patch: `d0c18b7b4b7f70d93dc66138f2253ad445ed0628d62c7603876a73dbb545c727`, 21,733 bytes. The [machine-readable review record](2026-10-04-stop-slop-proposal-review.json) pins all 17 original proposal files, the independent fixture, commands and reproduction outputs.

## Version 2 repair verification

Reviewed patch: `fee91932f93a2abebe5d45c2404848a91f502bf18bde23fa7572b0e5e6d23ba0`, 22,977 bytes. The [review record](2026-10-04-stop-slop-proposal-review.json) additionally pins all 20 version 2 proposal/history files. The retained version 1 patch matches the rejected patch hash.

The reviewer read the changed code and tests, replayed the original reproduction against the actual new file, and applied version 2 in a second pristine scratch clone of the same upstream pin. All **18 supplied tests passed**. The applied implementation, tests and fixtures match the proposal bytes; only the intended optional reference section changes an existing tracked upstream file.

The independent CLI matrix covered **18 cases**: direct, file-symlink and directory-symlink invocation; unchanged, stale and malformed manifests; each with default Node behavior and `--preserve-symlinks-main`. Every unchanged case emitted `declared_inputs_match` and exited 0. Every stale or malformed case emitted the proper JSON rejection, no stdout, and exited 1. Importing the module through a separate helper produced only the helper's output and did not execute the CLI.

The fresh version 2 checkout also passed `git apply --check`, syntax checks, browser-data regeneration without drift, and `git diff --check`. The same independent keep/edit/delete builder fixture again produced identical before/after HTML with script-closing text encoded. The read-only reference clone stayed clean. **SS-01 is closed as repaired and independently verified for these paths and runtime.** No new actionable issue was identified from the changed context.

## Scope and limits

No unresolved actionable issue remains in the bounded review. The normal CLI validates argument shape, manifest roles/IDs/hash syntax, root/file existence, path containment and exact bytes. The implementation rejects changed declared context, but context is optional and omitted context is invisible. Reusing or editing a manifest can misrepresent a review; the documentation explicitly makes this a trusted-snapshot preflight, not review authentication or an atomic filesystem operation.

The checker does not inspect semantic consistency, bind the review's own prose, prove the reviewer read anything, or establish literary improvement. Source and candidate roles identify declarations; they do not prove those declarations are complete or appropriate. The original dispatch fixtures demonstrate byte mismatch rejection, not improved writing.

This reviewer did not author the proposal. It is nevertheless another AI agent in the same project, not external review or human agreement; the reviewer also authored chapter 14 and reviewed the late novel chapters. The original narrative evidence is therefore checked here for accurate origin/version description, not independently validated as a writing-quality experiment. Testing was local macOS/Node v26.8.1; no Windows or broader runtime compatibility result is claimed. The proposal has not been contributed upstream, and this review authorizes no publication, pull request or merge.

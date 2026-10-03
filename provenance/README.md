# Authorship and method records

The contest asks how the book was written, including the models/method and what the human did. The current form limits this explanation to 300 words. Our detailed records support an accurate short disclosure later.

## Record each substantive manuscript session

Append a row to [generation-log.csv](generation-log.csv). Use [generation-record.json](../templates/generation-record.json) for a detailed record when useful. Link prompts or instructions, generated paths, feedback, and the resulting commit. If a commit is not yet made, write `pending` and resolve it later.

Record the actual model label when available; use `unknown` for details we cannot verify. Do not infer an exact model build from a product label. Do not add passwords, tokens, private endpoints, personal contact details, or wallet information.

Keep human direction in [human-inputs.md](human-inputs.md). It can include concept choices, structure, criticism, and factual corrections. AI must compose the resulting manuscript wording. Research quotations and human-provided text must not be copied into the book.

Git history and these logs document our process. They do not certify originality, rule compliance, or contest acceptance.

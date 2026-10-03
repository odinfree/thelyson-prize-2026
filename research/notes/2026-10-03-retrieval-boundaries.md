# Retrieval does not settle interpretation

Checked 3 October 2026. These additional primary readings inform later experiments; they do not change our already frozen evidence-window comparison.

[RIME, a 28 September preprint](https://arxiv.org/abs/2609.34438), forms conversational memory through generic retrieval questions and joint consolidation. Its fallback retrieves original dialogue only after an initial answer of `NONE`. Evaluation covers 1,540 non-adversarial LoCoMo questions with model judges; reported costs cover query-time tokens, not total memory construction. The work does not test human reception of fiction.

Our inference is that abstention-triggered retrieval leaves a distinct failure case: a confidently unsupported answer never requests more evidence. We should test that case explicitly before adopting the trigger. A successful recovery after abstention does not establish that the system reliably notices missing evidence.

[KnowMe-Bench, ACL 2026](https://aclanthology.org/2026.acl-long.1394/), separates factual, temporal and interpretive tasks over reconstructed literary narratives. Some precise temporal anchors are synthesized when the original narration is underspecified. Truncated base inputs and externally retrieved evidence are unequal information conditions. Model grading of expert answers is also distinct from agreement between human annotators. Inspected aggregate tables contain unresolved scope differences, so we do not quote a single superiority figure.

For our writing system, event time, narration time and inferred time should remain distinguishable. Missing precision should remain missing until the manuscript actually establishes it. Similarly, an interpretation can be plausible without becoming the only permitted reading. These are design hypotheses supported by the failure surfaces, not measured gains in novel quality.

Both papers are recorded in the [source register](../sources/literature.json). No new corpus, model or architecture was adopted from these readings.

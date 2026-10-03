# Typed claim checks: a narrow benefit and a new error

3 October 2026. This local diagnostic compared a direct judgment with explicit typed obligations on two original fictional sources. It follows the [evidence-window comparison](2026-10-03-evidence-window-results.md), where shorter prompts did not improve semantic agreement. These are engineering results, not contest scores or reader ratings.

The experiment froze six claims, twenty source presentations and forty requests before inference. One typed response exhausted its 512-token output allowance and returned incomplete JSON. A separate continuation attempted the twenty-two untouched requests with unchanged prompts and limits. The failed request was not retried or interpreted from partial JSON.

Among **nineteen complete pairs**, direct judgments matched the supplied-evidence key in **15/19**, and typed judgments in **18/19**. Four cases improved, one worsened and fourteen were correct under both methods. Across all completed outputs the counts are 15/20 and 18/19; the unequal denominators must remain visible. The unpaired direct error is not counted as a typed gain.

Three gains repeat variants of the only two-part conjunction. The typed approach kept the combined claim unknown when one part was supported and the other unresolved. Another gain concerned a character's knowledge. The typed loss reversed an explicit open/closed interval. Both methods correctly abstained on the single selected excerpt whose key changed after removing necessary evidence.

Seventy-one of seventy-two output quotations were exact, but exact text still accompanied mistaken reasoning. Even a correct final label sometimes rested on a faulty explanation. Quotation presence is therefore useful for inspection and insufficient for automatic acceptance.

The forty attempts used **57,198 returned prompt tokens and 8,683 completion tokens**, including the failed response. Typed requests used more tokens in the paired comparison. Program construction, source authoring and annotation add unmetered work. Different prompts and preparation prevent attributing the result solely to decomposition. There are only two diagnostic source families, and the annotations are AI assessments.

The result supports retaining typed checks as a review aid and testing the conjunction mechanism on new sources. It does not establish a general semantic advantage, validated confidence threshold, better prose or a higher chance of winning. The earlier style-overlay and retrieval failures remain relevant counterexamples.

The private [results report](https://github.com/odinfree/thelyson-research-lab/blob/main/experiments/narrative/fresh-source-v1/results-report.md), combined analysis and independent output audit retain the raw-case distinctions, exact artifact versions and failure accounting. The public [writing-system plan](../../planning/writing-system.md) explains where such checks fit into drafting; the [Stop Slop roadmap](../../integrations/stop-slop-refined/roadmap.md) remains a proposed transfer, with no upstream change yet.

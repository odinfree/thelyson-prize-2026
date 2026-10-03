# Smaller evidence windows did not improve this judge

Completed 3 October 2026. A local Qwen3-Coder-30B-A3B-Instruct Q4_K_M model judged 16 frozen claims about one 933-word original synthetic story in four evidence presentations. All 64 scheduled calls completed. This is a diagnostic experiment on correlated claims from one exposed story, not a novel benchmark or contest score.

| Presentation | Full-story key matches | Reported prompt tokens |
| --- | ---: | ---: |
| Whole source, one item | 9/16 | 25,202 |
| Same source, segmented | 9/16 | 30,146 |
| Lexical paragraph selection, at most 400 words | 9/16 | 17,246 |
| Section-constrained neighboring paragraphs, at most 400 words | 8/16 | 16,537 |

Claims, model and output ceiling were held fixed. Prompt lengths were not equal. The lexical and neighboring selections used about 32% and 34% fewer prompt tokens than the whole-source arm. These are request-token observations, not equal-compute comparisons, billing savings or a throughput benchmark.

## The important errors

Full-source answer keys cannot by themselves assess an excerpt. Separate isolated excerpt reviews and a later full-source audit retained three disputed interpretations. On the 29 uncontested excerpt presentations, the model matched 14 excerpt-relative labels. Both excerpts assessed as omitting deciding evidence received definite answers. Those answers happened to match the full-story key, while the shown evidence did not justify them.

Exact quotation checks also failed to distinguish sound inference from error. Across the experiment, 23 of 54 records with valid quote links disagreed with the full-source key; excluding the disputed full-source claim leaves 19. The judge sometimes used a real quotation about one event to assert a different time, actor, quantity or causal connection. Some correct labels also carried faulty explanations. Segmentation removed five invalid citation entries seen in the whole-source arm, but did not improve aggregate semantic agreement.

The four arms exchanged errors rather than behaving identically. Removing the disputed full-source claim leaves 9/15, 9/15, 9/15 and 8/15. No selector is promoted on these results. Exact source spans remain useful provenance; they do not certify the conclusion drawn from them.

## Next hypothesis

A fresh-source design will test explicit claim obligations while preserving quantifiers, time, belief holders and entity identity. It remains prospective. A recent decomposition study itself documents divergence between verifier confidence and accuracy; its positive results are not a general guarantee for fiction. [Lu et al., ACL 2025](https://aclanthology.org/2025.acl-long.254/)

Another study shows how independently supported atoms can combine facts about different people into an incorrect biography. This motivates preserving identity across obligations, not treating atom-level support as proof of the whole. [Chiang and Lee, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.160/)

The private lab retains frozen source hashes, exact requests, isolated annotations, disputed labels, raw response bindings, usage records, deterministic analysis and an independent all-cell audit. Local compute was stopped after the run. No human reader experiment, selected book, autonomous manuscript edit or upstream skill change follows from this diagnostic.

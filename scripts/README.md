# Manuscript tooling

These tools assemble declared sources and check mechanical properties. They do not judge literary quality, verify AI authorship or establish contest acceptance.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/manuscript.py report --allow-incomplete
python3 scripts/manuscript.py report --entry --output submission/exports/manuscript-report.json
python3 scripts/manuscript.py assemble --entry --output submission/exports/the-fifteenth-year.md
python3 scripts/export_pdf.py
python3 scripts/verify_pdf.py submission/exports/the-fifteenth-year.pdf
```

`book/manifest.json` defines the complete chapter order. Sources require one numbered title and manuscript prose only. Draft reporting can name missing chapters; assembly and export refuse incomplete sequences. Counts exclude chapter titles and standalone scene separators. Fingerprints bind reports to the exact complete source bytes, including headings. A changed fingerprint invalidates prior whole-manuscript review applicability; it does not say which semantic finding changed.

PDF export needs Python with `reportlab` and `pypdf`, plus the Georgia regular and bold fonts; the default font directory is the macOS system supplemental directory and can be overridden. Verification additionally uses `pdfplumber`. In Codex, use the bundled workspace Python when these packages are not installed in the shell Python. The verifier checks both the complete whitespace-token sequence and every non-whitespace character, including punctuation, after removing the known footer area. It also checks bounds, blank pages, bookmarks and the observed size limits. Render and visually inspect all pages separately. Generated files stay in ignored `submission/exports/`.

The [verified package report](../submission/package-report.json) records the delivered source fingerprint, PDF hash and actual visual-review scope. A rebuilt PDF may have different metadata and bytes: rerun extraction and rendered-page checks before replacing that record. Keep the manuscript's Unicode punctuation intact; it is embedded and checked in the output.

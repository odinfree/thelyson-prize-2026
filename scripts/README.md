# Manuscript tooling

These tools assemble declared sources and check mechanical properties. They do not judge literary quality, verify AI authorship or establish contest acceptance.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/manuscript.py report --allow-incomplete
python3 scripts/manuscript.py report --entry --output submission/exports/manuscript-report.json
python3 scripts/manuscript.py assemble --entry --output submission/exports/the-fifteenth-year.md
python3 scripts/export_pdf.py
```

`book/manifest.json` defines the complete chapter order. Sources require one numbered title and manuscript prose only. Draft reporting can name missing chapters; assembly and export refuse incomplete sequences. Counts exclude chapter titles and standalone scene separators. Fingerprints bind reports to the exact complete source bytes, including headings. A changed fingerprint invalidates prior whole-manuscript review applicability; it does not say which semantic finding changed.

PDF export needs Python with `reportlab` and `pypdf`, plus the Georgia regular and bold fonts; the default font directory is the macOS system supplemental directory and can be overridden. In Codex, use the bundled workspace Python when these packages are not installed in the shell Python. Render and visually inspect the result, then independently compare extracted body text with the sources before delivering it. Generated files stay in ignored `submission/exports/`.

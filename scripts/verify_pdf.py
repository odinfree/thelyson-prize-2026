#!/usr/bin/env python3
"""Independently compare exported PDF text to the current declared manuscript."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
from manuscript import inspect


def compact(value: str) -> str:
    return re.sub(r'\s+', '', value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    manifest = json.loads((args.root / 'book/manifest.json').read_text())
    source, chapters = inspect(args.root, manifest)
    expected = manifest['title'] + '\nA novel\n' + '\n'.join(f"{c['number']}. {c['title']}\n{c['body']}" for c in chapters)
    pages, bounds_issues, blank = [], [], []
    with pdfplumber.open(args.pdf) as pdf:
        for index, page in enumerate(pdf.pages, 1):
            # Page numbers occupy the bottom40pt; source text is above the49pt margin.
            content = page.crop((0, 0, page.width, page.height - 40))
            text = content.extract_text(x_tolerance=2, y_tolerance=3) or ''
            pages.append(text)
            if not text.strip():
                blank.append(index)
            for word in content.extract_words():
                if word['x0'] < 46 or word['x1'] > page.width - 46 or word['top'] < 30 or word['bottom'] > page.height - 44:
                    bounds_issues.append({'page': index, 'text': word['text'], 'box': [word['x0'], word['top'], word['x1'], word['bottom']]})
    actual = '\n'.join(pages)
    args.pdf.with_suffix('.extracted.txt').write_text(actual + '\n')
    expected_compact, actual_compact = compact(expected), compact(actual)
    same = expected_compact == actual_compact
    tokens_same = expected.split() == actual.split()
    mismatch = None
    if not same:
        offset = next((i for i, pair in enumerate(zip(expected_compact, actual_compact)) if pair[0] != pair[1]), min(len(expected_compact), len(actual_compact)))
        mismatch = {'compact_character_offset': offset, 'expected_context': expected_compact[max(0,offset-70):offset+100], 'actual_context': actual_compact[max(0,offset-70):offset+100]}
    reader = PdfReader(args.pdf)
    result = {'schema_version': 1, 'source_manuscript_fingerprint': source['manuscript_fingerprint'],
              'pdf_sha256': hashlib.sha256(args.pdf.read_bytes()).hexdigest(), 'pdf_bytes': args.pdf.stat().st_size,
              'pages': len(pages), 'declared_chapters': len(chapters), 'source_prose_words': source['prose_words'],
              'extracted_words_with_title_and_chapter_headings_and_scene_marker': len(actual.split()),
              'complete_text_sequence_matches_ignoring_whitespace': same,
              'complete_whitespace_token_sequence_matches': tokens_same,
              'expected_words_including_front_matter': len(expected.split()),
              'match_method': 'pdfplumber independently extracts every page above footer; compare every non-whitespace character including punctuation against declared source plus title and chapter headings',
              'blank_body_pages': blank, 'out_of_bounds_words': bounds_issues, 'mismatch': mismatch,
              'bookmarks': len(reader.outline), 'live_observed_size_range_satisfied': 1024 <= args.pdf.stat().st_size <= 15728640,
              'limits': 'Text/order/size/geometry checks do not replace rendered-page inspection, editorial review or organizer acceptance.'}
    result['mechanical_checks_passed'] = same and tokens_same and not blank and not bounds_issues and result['bookmarks'] == len(chapters) and result['live_observed_size_range_satisfied']
    output = args.output or args.pdf.with_suffix('.verification.json')
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'out_of_bounds_words'},indent=2,ensure_ascii=False))
    if not result['mechanical_checks_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

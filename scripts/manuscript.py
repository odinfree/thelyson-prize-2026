#!/usr/bin/env python3
"""Assemble declared manuscript sources; report bytes and counts, not literary quality."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def chapter_body(text: str, number: int) -> tuple[str, str]:
    lines = text.splitlines()
    prefix = f'# {number}. '
    if not lines or not lines[0].startswith(prefix):
        raise ValueError(f'Chapter {number}: expected numbered title')
    title = lines[0][len(prefix):].strip()
    if not title:
        raise ValueError('Empty title')
    if any(line.startswith('#') for line in lines[1:]):
        raise ValueError(f'Chapter {number}: unexpected metadata/heading inside prose')
    body = '\n'.join(lines[1:]).strip()
    if not body:
        raise ValueError(f'Chapter {number}: empty body')
    return title, body


def word_count(body: str) -> int:
    return len(' '.join(line for line in body.splitlines() if line.strip() != '* * *').split())


def inspect(root: Path, manifest: dict, allow_incomplete: bool = False) -> tuple[dict, list[dict]]:
    root = root.resolve()
    entries = manifest['chapters']
    if not entries or [x['number'] for x in entries] != list(range(1, len(entries) + 1)):
        raise ValueError('Chapter numbers must be consecutive and ordered from 1')
    paths = [x['path'] for x in entries]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate chapter path')
    chapters, missing = [], []
    for entry in entries:
        path = (root / entry['path']).resolve()
        if not path.is_relative_to((root / 'book/chapters').resolve()):
            raise ValueError('Chapter path escapes manuscript directory')
        if not path.is_file():
            missing.append(entry['path'])
            continue
        data = path.read_bytes()
        title, body = chapter_body(data.decode('utf-8'), entry['number'])
        chapters.append({**entry, 'title': title, 'body': body, 'sha256': sha(data), 'words': word_count(body)})
    undeclared = sorted(str(p.relative_to(root)) for p in (root / 'book/chapters').glob('*.md') if str(p.relative_to(root)) not in paths)
    if undeclared:
        raise ValueError(f'Undeclared chapter files: {undeclared}')
    if missing and not allow_incomplete:
        raise ValueError(f'Missing chapters: {missing}')
    records = [{k: v for k, v in x.items() if k != 'body'} for x in chapters]
    fingerprint = sha(json.dumps(records, sort_keys=True, ensure_ascii=False).encode())
    count = sum(x['words'] for x in chapters)
    report = {'schema_version': 1, 'title': manifest['title'], 'manuscript_fingerprint': fingerprint,
              'complete_sequence': not missing, 'chapter_count': len(chapters), 'expected_chapters': len(entries),
              'prose_words': count, 'count_method': 'whitespace tokens; excludes numbered chapter titles and standalone scene separators',
              'published_length_range_satisfied': not missing and 40000 <= count <= 120000,
              'missing': missing, 'chapters': records,
              'limits': 'Order, source bytes and mechanical count only; no literary, originality or eligibility certification.'}
    return report, chapters


def assemble(title: str, chapters: list[dict]) -> str:
    return '# ' + title + '\n\n' + '\n\n'.join(f"# {c['number']}. {c['title']}\n\n{c['body']}" for c in chapters) + '\n'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['report', 'assemble'])
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--manifest', default='book/manifest.json')
    parser.add_argument('--allow-incomplete', action='store_true')
    parser.add_argument('--entry', action='store_true', help='Require the published 40,000–120,000-word range')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    manifest = json.loads((args.root / args.manifest).read_text())
    report, chapters = inspect(args.root, manifest, args.allow_incomplete)
    if args.entry and not report['published_length_range_satisfied']:
        parser.error('Incomplete manuscript or prose count outside published range')
    if args.action == 'assemble' and not report['complete_sequence']:
        parser.error('Refusing to assemble an incomplete manuscript')
    text = json.dumps(report, indent=2, ensure_ascii=False) + '\n' if args.action == 'report' else assemble(manifest['title'], chapters)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()

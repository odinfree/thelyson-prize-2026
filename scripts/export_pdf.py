#!/usr/bin/env python3
"""Render the complete declared English manuscript, retaining a source fingerprint."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from pypdf import PdfReader
from manuscript import inspect


class BookDoc(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapter_starts = {}

    def afterFlowable(self, flowable):
        number = getattr(flowable, 'chapter_number', None)
        if number is not None:
            self.chapter_starts[number] = self.page
            key = f'chapter-{number}'
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.getPlainText(), key, level=0)


def footer(canvas, doc):
    if doc.page == 1:
        return
    canvas.saveState()
    canvas.setFont('BookSerif', 9)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawCentredString(doc.pagesize[0] / 2, 28, str(doc.page - 1))
    canvas.restoreState()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, default=Path('submission/exports/the-fifteenth-year.pdf'))
    parser.add_argument('--font-dir', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads((root / 'book/manifest.json').read_text())
    report, chapters = inspect(root, manifest)
    if not report['published_length_range_satisfied']:
        raise ValueError('Refusing entry PDF outside published manuscript length range')
    for name, file in [('BookSerif', 'Georgia.ttf'), ('BookSerifBold', 'Georgia Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(args.font_dir / file)))
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = BookDoc(str(output), pagesize=(432, 648), rightMargin=48, leftMargin=48,
                  topMargin=48, bottomMargin=49, title=manifest['title'],
                  author='', subject='A novel', pageCompression=1,
                  allowSplitting=1)
    body = ParagraphStyle('Body', fontName='BookSerif', fontSize=10.5, leading=15,
                          alignment=TA_JUSTIFY, firstLineIndent=13, spaceAfter=3,
                          allowWidows=0, allowOrphans=0)
    first = ParagraphStyle('First', parent=body, firstLineIndent=0)
    title = ParagraphStyle('Title', fontName='BookSerif', fontSize=29, leading=37, alignment=TA_CENTER)
    sub = ParagraphStyle('Subtitle', fontName='BookSerif', fontSize=11, leading=16, alignment=TA_CENTER)
    heading = ParagraphStyle('Chapter', fontName='BookSerif', fontSize=19, leading=26, spaceBefore=30, spaceAfter=26, keepWithNext=True)
    separator = ParagraphStyle('Separator', parent=sub, spaceBefore=8, spaceAfter=8)
    flow = [Spacer(1, 133), Paragraph(escape(manifest['title']), title), Spacer(1, 22), Paragraph('A novel', sub), PageBreak()]
    for index, chapter in enumerate(chapters):
        if index:
            flow.append(PageBreak())
        h = Paragraph(f"{chapter['number']}. {escape(chapter['title'])}", heading)
        h.chapter_number = chapter['number']
        flow.append(h)
        first_paragraph = True
        paragraphs = [p.strip() for p in chapter['body'].split('\n\n') if p.strip()]
        tail_start = len(paragraphs)
        tail_words = 0
        while tail_start > 0 and tail_words < 60:
            tail_start -= 1
            tail_words += len(paragraphs[tail_start].split())
        tail = []
        for paragraph_index, paragraph in enumerate(paragraphs):
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            destination = tail if paragraph_index >= tail_start else flow
            if paragraph == '* * *':
                destination.append(Paragraph('* * *', separator))
                first_paragraph = True
            else:
                destination.append(Paragraph(escape(' '.join(paragraph.splitlines())), first if first_paragraph else body))
                first_paragraph = False
        # Keep a small closing block together, avoiding a two-line chapter tail on a page of its own.
        flow.append(KeepTogether(tail))
    doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    reader = PdfReader(output)
    export = {'schema_version': 1, 'source_manuscript_fingerprint': report['manuscript_fingerprint'],
              'pdf_file': output.name, 'pdf_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
              'bytes': output.stat().st_size, 'pages': len(reader.pages), 'prose_words': report['prose_words'],
              'chapter_starts_pdf_page_1_based': doc.chapter_starts,
              'rendering': '6x9 inches, embedded Georgia, 10.5 pt on 15 pt leading',
              'checks_remaining': ['Independent text extraction comparison', 'Rendered page inspection', 'Live contest requirements refresh']}
    output.with_suffix('.build.json').write_text(json.dumps(export, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(export, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from manuscript import inspect, word_count


class ManuscriptChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'book/chapters').mkdir(parents=True)
        self.path = 'book/chapters/01-one.md'
        (self.root / self.path).write_text('# 1. One\n\nThree prose words.\n\n* * *\n\nTwo more.\n')
        self.manifest = {'title': 'Fixture', 'chapters': [{'number': 1, 'path': self.path}]}

    def test_count_excludes_title_and_separator(self):
        report, _ = inspect(self.root, self.manifest)
        self.assertEqual(report['prose_words'], 5)
        self.assertFalse(report['published_length_range_satisfied'])

    def test_duplicate_path_rejected(self):
        self.manifest['chapters'].append({'number': 2, 'path': self.path})
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            inspect(self.root, self.manifest)

    def test_missing_source_is_never_complete(self):
        self.manifest['chapters'].append({'number': 2, 'path': 'book/chapters/02-two.md'})
        with self.assertRaisesRegex(ValueError, 'Missing'):
            inspect(self.root, self.manifest)
        report, _ = inspect(self.root, self.manifest, True)
        self.assertFalse(report['complete_sequence'])
        self.assertEqual(len(report['missing']), 1)

    def test_numbering_and_undeclared_source(self):
        self.manifest['chapters'][0]['number'] = 2
        with self.assertRaisesRegex(ValueError, 'consecutive'):
            inspect(self.root, self.manifest)
        self.manifest['chapters'][0]['number'] = 1
        (self.root / 'book/chapters/02-hidden.md').write_text('# 2. Hidden\n\nProse.\n')
        with self.assertRaisesRegex(ValueError, 'Undeclared'):
            inspect(self.root, self.manifest)

    def test_fingerprint_changes_on_prose_change(self):
        first, _ = inspect(self.root, self.manifest)
        p = self.root / self.path
        p.write_text(p.read_text().replace('Three', 'Four'))
        second, _ = inspect(self.root, self.manifest)
        self.assertNotEqual(first['manuscript_fingerprint'], second['manuscript_fingerprint'])

    def test_escape_and_metadata_rejected(self):
        self.manifest['chapters'][0]['path'] = '../../outside.md'
        with self.assertRaisesRegex(ValueError, 'escapes'):
            inspect(self.root, self.manifest)
        self.manifest['chapters'][0]['path'] = self.path
        (self.root / self.path).write_text('# 1. One\n\n# editorial notes\n\nDraft\n')
        with self.assertRaisesRegex(ValueError, 'metadata'):
            inspect(self.root, self.manifest)


if __name__ == '__main__':
    unittest.main()

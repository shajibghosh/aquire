"""Regression checks for evidence, identity, and export integrity boundaries."""
import copy
import base64
import hashlib
import re
import csv
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from atlas_tools import ROOT, csv_text, generated_files, load_atlas, validate_atlas, verify_edition


class CatalogRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = load_atlas()

    def setUp(self):
        self.a = copy.deepcopy(self.source)

    def rejects(self, text):
        with self.assertRaisesRegex(ValueError, text):
            validate_atlas(self.a)

    def test_reference_snapshot_is_valid(self):
        validate_atlas(self.a)
        verify_edition(self.a)

    def test_duplicate_doi_is_rejected(self):
        r = self.a['resources']
        r[1]['doi'], r[1]['url'] = r[0]['doi'], r[0]['url']
        self.rejects('duplicate DOI')

    def test_unsafe_link_is_rejected(self):
        self.a['resources'][0]['url'] = 'javascript:alert(1)'
        self.rejects('unsafe url')

    def test_doi_url_identity_must_match(self):
        self.a['resources'][0]['url'] = 'https://doi.org/10.1234/wrong'
        self.rejects('identity mismatch')

    def test_unknown_related_topic_is_rejected(self):
        self.a['resources'][0]['assignments'][0]['topic_id'] = 'D99T99'
        self.rejects('unknown related topic')

    def test_year_cannot_be_inferred_from_retrieval(self):
        r = next(x for x in self.a['resources'] if x['year'] is None)
        r['year'] = 2099
        self.rejects('year beyond snapshot')

    def test_primary_labels_must_match_taxonomy(self):
        self.a['resources'][0]['topic'] = 'Unrelated label'
        self.rejects('labels disagree')

    def test_future_retrieval_is_rejected(self):
        self.a['resources'][0]['retrieved'] = '2099-01-01'
        self.rejects('retrieval beyond snapshot')

    def test_stale_counts_are_rejected(self):
        self.a['counts']['resources'] += 1
        self.rejects('counts disagree')

    def test_embedded_metadata_cannot_terminate_data_script(self):
        marker = '</script><script>alert(1)</script>'
        self.a['resources'][0]['title'] = marker
        html = generated_files(self.a)['index.html'].decode()
        self.assertNotIn(marker, html)
        embedded = html.split('<script id="atlas-data" type="application/json">', 1)[1].split('</script>', 1)[0]
        self.assertEqual(json.loads(embedded)['resources'][0]['title'], marker)

    def test_csv_preserves_rows_and_protects_formula_prefix(self):
        self.a['resources'][0]['title'] = '=HYPERLINK("https://example.com")'
        rows = list(csv.DictReader(io.StringIO(csv_text(self.a).lstrip('\ufeff'))))
        self.assertEqual(len(rows), len(self.a['resources']))
        self.assertEqual(rows[0]['title'], "'" + self.a['resources'][0]['title'])
        self.assertEqual({r['id'] for r in rows}, {r['id'] for r in self.a['resources']})

    def test_script_policy_matches_built_application(self):
        html = generated_files(self.a)['index.html'].decode()
        script = re.findall(r'<script>([\s\S]*?)</script>', html)[0]
        digest = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
        self.assertIn("script-src 'sha256-" + digest + "'", html)
        self.assertIn("connect-src 'none'", html)
        self.assertNotIn("script-src 'unsafe-inline'", html)


if __name__ == '__main__':
    unittest.main()

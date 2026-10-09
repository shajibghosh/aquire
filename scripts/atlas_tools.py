"""Deterministic catalog validation and serialization (Python standard library)."""
from __future__ import annotations

import collections
import base64
import csv
import datetime as dt
import hashlib
import io
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('id title authors year date type metadata_type venue conference publisher '
          'volume issue pages article_number doi url source metadata_url retrieved '
          'domain topic topic_id subcategories classification assignments discovery_query '
          'score access landing_check link_status isbn core').split()


def load_atlas(path=None):
    return json.loads((Path(path) if path else ROOT / 'data/atlas.json').read_text(encoding='utf-8'))


def counts_for(a):
    r, t = a['resources'], a['taxonomy']
    years = [x['year'] for x in r if x['year'] is not None]
    return dict(resources=len(r), domains=len(t), topics=sum(len(d['topics']) for d in t),
                subcategories=sum(len(p['subcategories']) for d in t for p in d['topics']),
                types=dict(collections.Counter(x['type'] for x in r)),
                official_pages=sum(x['metadata_type'] == 'official-web-resource' for x in r),
                registered_dois=sum(bool(x['doi']) for x in r),
                year_min=min(years) if years else None, year_max=max(years) if years else None)


def validate_atlas(a):
    """Raise ValueError for unsupported identities, URLs, dates, or taxonomy references."""
    def need(test, message):
        if not test:
            raise ValueError(message)

    need(isinstance(a, dict), 'Catalog must be an object')
    for key in ('title', 'snapshot_date', 'counts', 'taxonomy', 'paths', 'methods', 'resources'):
        need(key in a, f'Missing catalog field: {key}')
    snapshot = dt.date.fromisoformat(a['snapshot_date'])
    need(bool(a['resources']) and bool(a['taxonomy']), 'Empty catalog or taxonomy')
    domains, topics = {}, {}
    for d in a['taxonomy']:
        need(re.fullmatch(r'D[0-9]{2,}', d['id']) and d['id'] not in domains,
             f'Duplicate or malformed domain ID: {d["id"]}')
        domains[d['id']] = d
        need(bool(d['topics']), f'Empty domain: {d["id"]}')
        for t in d['topics']:
            need(t['id'].startswith(d['id'] + 'T') and t['id'] not in topics,
                 f'Duplicate or unsupported topic ID: {t["id"]}')
            need(all(isinstance(s, str) and s for s in t['subcategories']), 'Invalid fine vocabulary')
            topics[t['id']] = (d, t)
    ids, dois, urls, signatures, covered = set(), set(), set(), set(), set()
    for r in a['resources']:
        need(isinstance(r, dict), 'Resource must be an object')
        need(all(k in r for k in FIELDS), 'Missing resource field')
        structured = {'year', 'authors', 'isbn', 'subcategories', 'core', 'score', 'assignments'}
        need(all(isinstance(r[k], str) for k in FIELDS if k not in structured), 'Invalid text metadata field')
        rid = r['id']
        need(re.fullmatch(r'Q[0-9]{4,}', rid) and rid not in ids, f'Duplicate or malformed resource ID: {rid}')
        ids.add(rid)
        need(isinstance(r['title'], str) and r['title'].strip(), f'{rid}: missing title')
        need(r['topic_id'] in topics, f'{rid}: unknown primary topic')
        d, t = topics[r['topic_id']]
        covered.add(t['id'])
        need(r['domain'] == d['name'] and r['topic'] == t['name'], f'{rid}: primary taxonomy labels disagree')
        need((isinstance(r['year'], int) and not isinstance(r['year'], bool)) or r['year'] is None,
             f'{rid}: invalid year')
        need(r['year'] is None or 1000 <= r['year'] <= snapshot.year, f'{rid}: year beyond snapshot')
        for key in ('authors', 'isbn', 'subcategories'):
            need(isinstance(r[key], list) and all(isinstance(v, str) for v in r[key]), f'{rid}: invalid {key}')
        need(isinstance(r['core'], bool), f'{rid}: invalid core flag')
        need(isinstance(r['score'], (int, float)), f'{rid}: invalid matching score')
        need(bool(r['subcategories']), f'{rid}: missing fine classification')
        for key in ('url', 'metadata_url'):
            u = urlparse(r[key])
            need(u.scheme in ('https', 'http') and bool(u.netloc) and not u.username and not u.password,
                 f'{rid}: unsafe {key}')
        retrieval = dt.date.fromisoformat(r['retrieved'])
        need(retrieval <= snapshot, f'{rid}: retrieval beyond snapshot')
        if r['date']:
            parts = r['date'].split('-')
            need(len(parts) in (1, 2, 3) and re.fullmatch(r'\d{4}(?:-\d{2})?(?:-\d{2})?', r['date']),
                 f'{rid}: malformed source date')
            dt.date(int(parts[0]), int(parts[1]) if len(parts) > 1 else 1,
                    int(parts[2]) if len(parts) > 2 else 1)
            need(r['year'] == int(parts[0]), f'{rid}: date and year disagree')
        need(bool(r['assignments']), f'{rid}: missing assignments')
        for p in r['assignments']:
            need(p['topic_id'] in topics, f'{rid}: unknown related topic')
            ad, at = topics[p['topic_id']]
            need(p['domain'] == ad['name'] and p['topic'] == at['name'], f'{rid}: related labels disagree')
        need(any(p['topic_id'] == r['topic_id'] for p in r['assignments']), f'{rid}: primary assignment absent')
        vocabulary = set(t['subcategories'])
        need(all(s in vocabulary or s == 'Topic level only' for s in r['subcategories']), f'{rid}: unknown fine tag')
        if r['doi']:
            doi = r['doi'].casefold()
            need(re.fullmatch(r'10\.\d{4,9}/\S+', doi), f'{rid}: malformed DOI')
            need(doi not in dois, f'{rid}: duplicate DOI')
            dois.add(doi)
            u = urlparse(r['url'])
            need(u.hostname == 'doi.org' and unquote(u.path.lstrip('/')).casefold() == doi,
                 f'{rid}: DOI resolver identity mismatch')
            need(r['link_status'] == 'Registered DOI', f'{rid}: DOI verification mismatch')
        else:
            canonical = r['url'].rstrip('/').casefold()
            need(canonical not in urls, f'{rid}: duplicate official URL')
            urls.add(canonical)
            need(r['metadata_type'] == 'official-web-resource' and r['link_status'] == 'Page retrieved',
                 f'{rid}: official verification mismatch')
        norm = lambda s: re.sub(r'\W+', '', unicodedata.normalize('NFKC', s).casefold())
        signature = (norm(r['title']), norm(r['authors'][0]) if r['authors'] else '', r['year'])
        need(signature not in signatures, f'{rid}: duplicate title/lead-author/year')
        signatures.add(signature)
    need(covered == set(topics), 'Some topics lack primary resource coverage')
    for path in a['paths']:
        for step in path['steps']:
            need(step['topic_id'] in topics, 'Reading path refers to unknown topic')
    need(a['counts'] == counts_for(a), 'Catalog counts disagree with data')
    return a['counts']


def verify_edition(a, root=ROOT):
    """Verify preserved document assets independently of evolving catalog counts."""
    m = json.loads((root / 'docs/edition.json').read_text(encoding='utf-8'))
    if len(m['resource_ids']) != len(set(m['resource_ids'])):
        raise ValueError('Duplicate reference-edition IDs')
    if not set(m['resource_ids']).issubset({r['id'] for r in a['resources']}):
        raise ValueError('Reference-edition resources removed from catalog')
    for name, digest in m['documents'].items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Reference-edition digest mismatch: {name}')
    md = (root / 'exports/AQuIRE.md').read_text(encoding='utf-8')
    if set(re.findall(r'^#### (Q[0-9]+)\b', md, re.M)) != set(m['resource_ids']):
        raise ValueError('Markdown reference-edition IDs disagree')


def csv_text(a):
    fields = 'id title authors year date type domain topic subcategories venue conference publisher doi url source classification landing_check'.split()
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\r\n')
    writer.writerow(fields)
    def cell(v):
        if isinstance(v, list):
            v = '; '.join(v)
        s = '' if v is None else str(v)
        return "'" + s if s.startswith(('=', '+', '-', '@')) else s
    writer.writerows([cell(r[k]) for k in fields] for r in a['resources'])
    return '\ufeff' + stream.getvalue()


def bib_text(a):
    def escape(v):
        # Preserve Unicode; escape BibTeX/TeX-sensitive characters without dropping metadata.
        table = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '%': r'\%',
                 '&': r'\&', '_': r'\_', '#': r'\#', '$': r'\$'}
        return ''.join(table.get(c, c) for c in str(v).replace('\n', ' '))
    records = []
    for r in a['resources']:
        kind = {'Journal article': 'article', 'Conference paper': 'inproceedings',
                'Book': 'book', 'Edited book': 'book', 'Reference book': 'book',
                'Book chapter': 'incollection'}.get(r['type'], 'misc')
        values = {'title': r['title'], 'author': ' and '.join(r['authors']),
                  'year': r['year'], 'publisher': r['publisher'], 'doi': r['doi'],
                  'url': r['url'], 'note': r['domain'] + '; ' + r['topic']}
        if r['venue']:
            values['journal' if kind == 'article' else 'booktitle'] = r['venue']
        for source, dest in (('volume', 'volume'), ('issue', 'number'), ('pages', 'pages')):
            if r[source]:
                values[dest] = r[source]
        fields = [f'  {k} = {{{escape(v)}}}' for k, v in values.items() if v not in ('', None)]
        records.append('@' + kind + '{' + r['id'] + ',\n' + ',\n'.join(fields) + '\n}')
    return '\n\n'.join(records) + '\n'


def taxonomy_text(a):
    lines = ['# Subject taxonomy', '', 'Fine vocabulary is scoped to each topic. Related technologies are included explicitly; this is a broad map rather than an exhaustive classification.', '']
    for d in a['taxonomy']:
        lines.extend(['## ' + d['id'] + ' — ' + d['name'], '', d['description'], '',
                      '**Prerequisites:** ' + d['prerequisites'], '', '**Assessment:** ' + d['assessment'], ''])
        for t in d['topics']:
            lines.extend(['### ' + t['id'] + ' — ' + t['name'], '', t['description'], ''])
            lines.extend('- ' + s for s in t['subcategories'])
            lines.append('')
    return '\n'.join(lines)


def generated_files(a, root=ROOT):
    template = (root / 'src/template.html').read_text(encoding='utf-8')
    if template.count('__ATLAS_DATA__') != 1:
        raise ValueError('Template must contain exactly one data placeholder')
    raw = json.dumps(a, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    html = template.replace('__ATLAS_DATA__', raw)
    snapshot = dt.date.fromisoformat(a['snapshot_date'])
    label = f'{snapshot.day} {snapshot.strftime("%B")} {snapshot.year}'
    html = html.replace('__SNAPSHOT_LABEL__', label).replace('__SNAPSHOT_YEAR__', str(snapshot.year))
    scripts = re.findall(r'<script>([\s\S]*?)</script>', html)
    if len(scripts) != 1:
        raise ValueError('Expected one inline application script')
    digest = base64.b64encode(hashlib.sha256(scripts[0].encode('utf-8')).digest()).decode('ascii')
    policy = ("default-src 'none'; script-src 'sha256-" + digest + "'; "
              "style-src 'unsafe-inline'; img-src 'self' data:; connect-src 'none'; "
              "object-src 'none'; base-uri 'none'; form-action 'none'; frame-src 'none'; worker-src 'none'")
    security = '<meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="' + policy + '">'
    html = html.replace('<meta name="viewport"', security + '<meta name="viewport"', 1)
    return {'index.html': html.encode('utf-8'), 'exports/resources.csv': csv_text(a).encode('utf-8'),
            'exports/references.bib': bib_text(a).encode('utf-8'),
            'docs/TAXONOMY.md': taxonomy_text(a).encode('utf-8')}

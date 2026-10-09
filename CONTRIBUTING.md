# Contributing

Use an issue for proposed resources, factual corrections, taxonomy changes, and interface problems. Pull requests should state the resulting behavior and include source evidence and the checks performed.

## Resource and taxonomy changes

1. Edit `data/atlas.json`, the canonical catalog. Follow [the data dictionary](docs/DATA_DICTIONARY.md).
2. Retain existing `Q` identifiers. New records should use the next unused identifier, without renumbering older records. Retain topic IDs and document any intentionally retired IDs.
3. Supply a DOI and retrieved bibliographic record, or a first-party URL, observed page title, and retrieval date. Never infer publication dates from retrieval dates. Keep posted content distinct from journal articles.
4. Choose a primary topic supported by title evidence or a documented editorial assessment. Add related assignments only when supported. Use `Topic level only` when finer classification is uncertain.
5. Recompute `counts` with `python scripts/build.py --refresh-counts`, then run the validator, build, and tests. This option recalculates descriptive counts; it does not retrieve or verify sources.
6. Record methodological or edition changes in `CHANGELOG.md`. Reference-edition DOCX, PDF, and complete Markdown remain frozen until an explicitly prepared new document edition; do not label older documents as current after expanding the catalog.

## Interface and build changes

Edit `src/template.html`, rather than the generated `index.html`. Run the lightweight build and the browser smoke test. Include a screenshot when a visible layout changes. Escape catalog text before inserting it into HTML, and retain HTTP/HTTPS-only resource links.

## Validation

```bash
python scripts/validate.py
python scripts/build.py --check
python scripts/checksums.py
python -m unittest discover -s tests -v
npm ci
npx playwright install chromium
npm test
```

Review source metadata directly before making a scientific or bibliographic claim. Automated checks establish structural consistency and UI behavior; they do not assess the scientific quality or full-text accuracy of every indexed work.

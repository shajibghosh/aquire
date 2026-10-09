# Development

## Layout

| Path | Role |
| --- | --- |
| `data/atlas.json` | Canonical catalog, taxonomy, methods, and reading paths |
| `data/schema.json` | JSON Schema for catalog interchange |
| `src/template.html` | Browser application and embedded-data placeholder |
| `index.html` | Generated self-contained explorer |
| `scripts/atlas_tools.py` | Validation and deterministic serialization |
| `scripts/build.py` | HTML and machine-readable export build |
| `scripts/validate.py` | Catalog and edition-integrity checks |
| `scripts/checksums.py` | Distribution SHA-256 manifest refresh and checks |
| `tests/` | Validation regression tests and browser smoke test |
| `exports/` | Machine-readable exports and frozen reference documents |
| `docs/edition.json` | Reference document snapshot, IDs, and SHA-256 digests |
| `.github/workflows/` | Validation and static-site workflows |

The Python tools use only the standard library and support Python 3.11+. Run commands from the repository root. Builds use explicit UTF-8 and deterministic serialization. Source retrieval is not performed during builds or continuous integration.

`python scripts/build.py --check` checks that generated files match their source bytes without writing them. `--refresh-counts` recalculates counts before validation and regeneration; it does not update the snapshot date or verification labels. Set a new snapshot date only after the corresponding retrieval and editorial work has been completed.

## Browser checks

Node.js 22+ is used only for development testing. Install locked dependencies with `npm ci`, then `npx playwright install chromium`. On Linux CI, use `npx playwright install --with-deps chromium`. Run `npm test` after building. `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` can point to an existing compatible Chromium executable when downloading a browser is impractical.

The smoke test checks phrase/type/year combinations, taxonomy filtering, undated records, resource types, bookmark persistence, filtered exports, all navigation sections, themes, and mobile overflow. It loads the committed HTML through a local file URL and does not retrieve external resource pages.

## Reference editions

The Word, PDF, and complete Markdown are immutable reference-edition assets for the snapshot identified in `docs/edition.json`. The validator checks their recorded hashes and resource IDs, while the lightweight build regenerates only HTML, CSV, BibTeX, and `docs/TAXONOMY.md`. A changed live catalog may extend a preserved document edition; README statistics and edition labels must then be revised accordingly. A new document edition requires a separate document generation and visual review process, followed by an intentional manifest update.

## Boundaries

This repository reconstructs the explorer and exports from the included catalog snapshot. It does not include a crawler capable of independently reproducing the original retrieval or scientific review. Per-record retrieval URLs, dates, discovery queries, and classification evidence remain in the JSON for audit and correction.

After making release changes, refresh file digests with `python scripts/checksums.py` and verify them with `python scripts/checksums.py --check`.

## Security checks

`distribution.json` lists the public project files. `scripts/audit_publish.py` checks those files for common credential patterns and private runtime references, including DOCX XML. Browser script-policy hashes are generated from the current template automatically.

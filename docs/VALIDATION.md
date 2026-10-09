# Release validation

Project version **1.0.3**, reference snapshot **2026-10-08**, preserved reading edition **1.0.1**.

The distributed release was checked locally before packaging:

- Catalog validation passed for all 1,600 resource identifiers, taxonomy references, source URL schemes, DOI resolver identities, dates, duplicate identities, and derived counts.
- All 164 topics have primary catalog coverage.
- The HTML, CSV, BibTeX, and taxonomy build passed deterministic generated-file checks.
- All 12 validation regression tests passed, including unsafe URLs, duplicate DOIs, unknown topics, date inconsistencies, stale counts, embedded script termination, CSV formula-prefix handling, and the exact application-script security hash.
- The browser smoke test passed using the locked Playwright 1.58.2 dependency and Chromium: combined filters, undated records, resource types, bookmark persistence and legacy preference migration, AQuIRE branding and download filenames, filtered JSON export, taxonomy search, reading paths, coverage tables, themes, and mobile overflow.
- All 1,600 resource IDs were confirmed in the complete Markdown, DOCX, and 215-page PDF. Preserved reference documents passed SHA-256 integrity checks.
- Workflow YAML and local documentation links were checked. The committed explorer screenshot was visually reviewed.
- The explicit publication allowlist passed the credential-pattern scan. Browser checks confirmed that an unapproved inline script was blocked and ordinary search and export operations made no HTTP/HTTPS requests.

These checks do not test every external destination or independently assess full-text classifications. GitHub Actions and Pages deployment were configured and reviewed but were not executed on an external GitHub repository as part of this local release.

The AQuIRE rebranding preserves the source records, taxonomy, counts, reading paths, source methods, and retrieval snapshot. All 215 document pages were rendered; body text and glyph positions on 213 pages match the preceding edition exactly, excluding the renamed running header. The updated cover and acknowledgment page were visually reviewed.

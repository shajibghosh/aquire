# Methodology

Reference snapshot: **2026-10-08**.

## Scope and taxonomy

This is a broad research and learning map, not a claim to enumerate every possible topic or every available resource. The hierarchy contains major categories, topics, and fine subcategories. Networking, sensing, and classical post quantum cryptography are explicitly included as adjacent areas. These areas should not be conflated with quantum computation.

## Authentic source records

Scholarly entries were retrieved from the Crossref REST API using publisher deposited metadata and identifiable DOIs. Official web entries were retrieved from first party institutions, software projects, or providers and required a successful HTTP response and an identifiable page title. Failed or unrelated sources were excluded. The catalog is a metadata based bibliography, not a full text systematic review or a ranking of research quality.

## Subject assignments and finer tags

Topic searches were screened using title wording and subject context. Ambiguous results received editorial corrections or exclusion. Multiple supported discovery paths are retained as related topics. Fine subcategory tags are conservative lexical assignments from titles. Topic level only means that no precise fine tag was established; the full vocabulary shown in the taxonomy is not automatically assigned to every resource.

## Dates and publication types

Years and publication types follow retrieved bibliographic metadata. Posted content is kept separate from journal articles because peer review cannot be inferred from a DOI. Books and book chapters are distinct resource types, and separate editions can be retained when their years differ. Undated official pages stay undated; the retrieval year is not substituted for a publication year. Conference names are shown only when the source supplies an event or a proceedings venue.

## Deduplication and selection

DOIs and canonical web URLs were deduplicated. Identical normalized titles with matching lead author and publication year were also merged, preferring a journal or conference record over posted content when a match was clear. The selection balances topic coverage and retains curated foundational material. The same stable Q identifiers and resource records are used in HTML, DOCX, Markdown, PDF, CSV, and JSON.

## What the verification status means

Registered DOI means that a corresponding bibliographic record was retrieved from Crossref. It does not mean that every DOI resolver or full text download was individually tested. Page retrieved means that the official web page and its title were successfully retrieved on the snapshot date. Links can redirect, change, require authentication, or lead to paywalled content after delivery. No publication year, author, venue, or review status was invented to fill missing fields.

## Coverage and limitations

Coverage is selective and varies by topic, especially standards, economics, and specialized engineering. Bibliographic identity is stronger evidence than an unverified reference string, but it is not a guarantee of scientific validity, peer review quality, or practical advantage. Metadata can contain publisher errors or incomplete fields. Papers were not systematically screened for retractions and corrections across all external databases. Use the source record and paper itself when a claim is important.

## Offline use and exports

The HTML is self contained and uses no external scripts or fonts. Search, topic browsing, sorting, saved resources, and exports operate locally. External resource links need internet access. Browser saved resources use local storage and are not sent to a server. Search supports words combined with AND and quoted phrases. Journal, conference, author, publisher, year, type, topic, and verification filters can be combined. Exports contain all filtered results, while printing prints the currently displayed page of cards.

## Reproducibility and evidence

`data/atlas.json` preserves per-record DOI or source URL, metadata retrieval URL, retrieval date, classification notes, discovery query, and related topic assignments. Its counts describe the selected snapshot. The build reproduces the explorer and machine-readable exports without network access; it does not independently reconstruct historical source retrievals or perform full-text assessment.

Structural validation checks identifiers, hierarchy references, primary assignments, source URL schemes, dates, count consistency, duplicate identities, coverage, and document-edition integrity. Browser tests exercise user-facing behavior. These checks do not constitute external link monitoring or scientific peer review.

Primary source documentation: [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/), [NIST quantum information science](https://www.nist.gov/quantum-information-science), [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning), and [MIT OpenCourseWare](https://ocw.mit.edu/).

# Security

The explorer is a static browser application with no account system or backend. Bookmarks and theme preferences use browser local storage. External resource links are opened only when selected. Search and exports operate locally.

For a vulnerability, use GitHub's private vulnerability reporting feature if it is enabled on the published repository. Otherwise contact a maintainer through their published GitHub profile; avoid placing exploit details or sensitive information in a public issue. No private reporting address is configured in this distribution.

Contributions should keep resource URLs restricted to HTTP/HTTPS, escape source text in rendered HTML, and protect CSV cells that could be interpreted as spreadsheet formulas. A successful source retrieval is not a guarantee that an external site remains safe or unchanged.

## Browser policy

The generated HTML permits the exact inline application script through a SHA-256 Content Security Policy hash. External scripts, app network connections, frames, plugins, workers, form submissions, and base-URL overrides are blocked. Inline CSS is permitted for the existing UI. External resource links remain usable and use a no-referrer policy. This policy is defense in depth; it does not assess the safety of external resource destinations.

## Public indexing and access

The full catalog is intentionally public in the HTML, JSON, and reference exports. Its browser search index contains public bibliographic fields. User keywords, bookmarks, and theme preferences stay in the browser and are not part of release archives. Public GitHub and Pages content can be read, copied, and indexed. Robots directives do not provide authentication or confidentiality. Hosting providers may keep their own operational logs.

## Release checks

An explicit publication allowlist excludes Git history, credential files, private data indexes, environments, caches, test outputs, and runtime helpers. The audit checks common token patterns, private paths, internal file references, and signed-URL patterns without printing candidate secret values. These bounded checks do not establish that every possible secret format or vulnerability has been detected.

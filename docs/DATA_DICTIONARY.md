# Data dictionary

The canonical `data/atlas.json` object contains `title`, `snapshot_date`, `counts`, `taxonomy`, `paths`, `methods`, and `resources`. Empty strings or empty lists preserve unavailable metadata; `year` uses `null`.

## Resource fields

| Field | Meaning |
| --- | --- |
| `id` | Stable resource ID (Q followed by at least four digits). |
| `title` | Title from source metadata or the retrieved official page. |
| `authors` | Ordered list of author names; an empty list means unavailable. |
| `year` | Source publication/issue year, or null; never inferred from retrieval. |
| `date` | Source date as YYYY, YYYY-MM, or YYYY-MM-DD; empty when unknown. |
| `type` | Display resource type; posted content is distinct from journal articles. |
| `metadata_type` | Original source type or official-web-resource. |
| `venue` | Supplied journal, proceedings, book container, or official provider. |
| `conference` | Supplied conference/event or proceedings venue; empty when unavailable. |
| `publisher` | Publisher or official resource provider. |
| `volume` | Supplied bibliographic volume; empty when unavailable. |
| `issue` | Supplied issue number; empty when unavailable. |
| `pages` | Supplied page range or page identifier. |
| `article_number` | Supplied electronic article number. |
| `doi` | DOI identity without resolver prefix; empty for official web resources. |
| `url` | HTTP/HTTPS link to the resource or DOI resolver. |
| `source` | Source attribution for the record. |
| `metadata_url` | Retrieved Crossref API record URL or first-party page URL. |
| `retrieved` | ISO date on which source metadata or the page was retrieved. |
| `domain` | Primary major-category name. |
| `topic` | Primary topic name. |
| `topic_id` | Stable topic ID, e.g. D01T01. |
| `subcategories` | Conservative title-supported tags, or Topic level only. |
| `classification` | Editorial description of the assignment method. |
| `assignments` | Primary and related domain/topic/topic_id assignments with optional score and title_pattern. |
| `discovery_query` | Query used in initial discovery; provenance rather than a relevance guarantee. |
| `score` | Internal title-matching signal; not a scientific quality or confidence metric. |
| `access` | Access note; not a license or guarantee of free full text. |
| `landing_check` | Precise scope of source verification. |
| `link_status` | Registered DOI or Page retrieved. |
| `isbn` | List of supplied book ISBN values. |
| `core` | Editorial flag for foundational or landmark material, not a quality rating. |

## Hierarchy

A domain has `id`, `name`, `description`, `prerequisites`, `assessment`, and `topics`. A topic has `id`, `name`, `description`, `query`, `pattern`, and `subcategories`. Fine entries are scoped to their topic, so a vocabulary term may occur in multiple branches. Resource primary domain/topic labels must match their referenced hierarchy entry.

Reading paths contain `name`, `goal`, `steps` (each with `topic_id` and `text`), and `output`. Methods contain `heading` and `text`. Counts are derived summaries and must agree with records and hierarchy entries.

## Export conventions

CSV flattens list fields with semicolons and leaves unknown years blank. Cells beginning with `=`, `+`, `-`, or `@` receive a leading apostrophe to reduce spreadsheet-formula interpretation. JSON retains the complete record structure. BibTeX uses resource IDs as citation keys and omits unavailable fields; Unicode metadata is retained, so Unicode-capable citation tools are recommended. Original records and source URLs are authoritative when formatting differs.

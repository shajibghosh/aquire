"""Check canonical data and preserved document-edition integrity."""
from atlas_tools import load_atlas, validate_atlas, verify_edition


def main():
    a = load_atlas()
    counts = validate_atlas(a)
    verify_edition(a)
    print(f"Validated {counts['resources']:,} resources, {counts['topics']} topics, and reference-edition digests.")


if __name__ == '__main__':
    main()

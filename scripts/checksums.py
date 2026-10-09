"""Refresh the distributable-file SHA-256 manifest."""
import argparse
import hashlib
from pathlib import Path
from audit_publish import publication_files

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without updating the manifest')
    args = parser.parse_args()
    files = sorted(p for name, p in publication_files(ROOT) if name != 'SHA256SUMS')
    text = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' +
                   p.relative_to(ROOT).as_posix() + '\n' for p in files)
    dest = ROOT / 'SHA256SUMS'
    if args.check:
        if not dest.exists() or dest.read_text(encoding='utf-8') != text:
            raise SystemExit('SHA256SUMS is stale; run python scripts/checksums.py')
    else:
        dest.write_text(text, encoding='utf-8')
    print(f'Checked {len(files)} file digests.' if args.check else f'Wrote {len(files)} file digests.')


if __name__ == '__main__':
    main()

"""Build offline assets; optionally prepare the dedicated GitHub Pages directory."""
import argparse
import json
import shutil
from pathlib import Path
from atlas_tools import ROOT, counts_for, generated_files, load_atlas, validate_atlas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated assets are stale, without writing')
    parser.add_argument('--refresh-counts', action='store_true', help='Recalculate catalog summary counts')
    parser.add_argument('--site-dir', type=Path, help='Prepare a static deployment directory')
    args = parser.parse_args()
    if args.check and (args.refresh_counts or args.site_dir):
        parser.error('--check cannot be combined with mutation options')
    a = load_atlas()
    if args.refresh_counts:
        a['counts'] = counts_for(a)
    validate_atlas(a)
    if args.refresh_counts:
        (ROOT / 'data/atlas.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    generated = generated_files(a)
    stale = []
    for name, body in generated.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != body:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
    if stale:
        raise SystemExit('Stale generated assets: ' + ', '.join(stale))
    if args.site_dir:
        target = args.site_dir.resolve()
        # Restrict deployment destinations to a dedicated directory inside the checkout.
        if target == ROOT or ROOT not in target.parents or target.name not in ('_site', 'site-build'):
            parser.error('--site-dir must be _site or site-build inside the repository')
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)
        for name in ['index.html', '.nojekyll', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'data/atlas.json',
                     'exports/resources.csv', 'exports/references.bib', 'exports/AQuIRE.pdf',
                     'exports/AQuIRE.docx', 'exports/AQuIRE.md']:
            dest = target / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)
    print('Generated assets are current.' if args.check else f'Built {len(generated)} assets.')


if __name__ == '__main__':
    main()

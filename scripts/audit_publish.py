"""Audit the explicit publication file list without printing potential secret values."""
from pathlib import Path
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    'private-key material': rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'GitHub access-token pattern': rb'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{35,})',
    'API secret-key pattern': rb'sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}',
    'AWS access-key pattern': rb'(?:AKIA|ASIA)[A-Z0-9]{16}',
    'Slack token pattern': rb'xox[baprs]-[A-Za-z0-9-]{20,}',
    'private workspace path': rb'/(?:workspace/scratch|root|Users)/|[A-Z]:\\Users\\',
    'private file-reference pattern': rb'(?:libfile_|file_)[0-9a-f]{24,}|oai[-]library://',
    'signed URL pattern': rb'(?:X-Amz-Signature|X-Goog-Signature|sig)=[A-Za-z0-9%]{24,}',
}


def publication_files(root=ROOT):
    names = json.loads((root / 'distribution.json').read_text(encoding='utf-8'))['files']
    if len(names) != len(set(names)):
        raise ValueError('Duplicate publication file path')
    files = []
    for name in names:
        path = root / name
        if Path(name).is_absolute() or '..' in Path(name).parts or path.is_symlink():
            raise ValueError('Unsafe publication path')
        if root.resolve() not in path.resolve().parents:
            raise ValueError('Publication path escapes repository')
        basename = path.name.lower()
        if (basename.startswith(('.env', 'credentials', 'token', 'id_rsa', 'id_ed25519'))
                or path.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.sqlite', '.sqlite3', '.db', '.faiss'}):
            raise ValueError(f'Forbidden credential or private-index file: {name}')
        if not path.is_file():
            raise ValueError(f'Missing publication file: {name}')
        if any(p in {'.git', 'node_modules', '__pycache__', '.venv', '_site', 'test-results', 'dist'}
               for p in Path(name).parts):
            raise ValueError(f'Forbidden publication path: {name}')
        files.append((name, path))
    return files


def audit(root=ROOT):
    findings = []
    files = publication_files(root)
    for name, path in files:
        payloads = [(name, path.read_bytes())]
        if path.suffix == '.docx':
            with zipfile.ZipFile(path) as z:
                payloads += [(name + ':' + entry, z.read(entry))
                             for entry in z.namelist() if entry.endswith(('.xml', '.rels'))]
        for location, body in payloads:
            for description, pattern in RULES.items():
                if re.search(pattern, body):
                    findings.append(f'{location}: {description}')
    if findings:
        raise ValueError('Publication audit failed:\n' + '\n'.join(findings))
    return len(files)


if __name__ == '__main__':
    print(f'Publication audit passed for {audit()} allowlisted files.')

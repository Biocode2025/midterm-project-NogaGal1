from pathlib import Path
p = Path(__file__).resolve().parent.parent / 'data' / 'exterme_organism_proteins.txt'
print('Resolved path:', p)
print('Exists:', p.exists())
try:
    text = p.read_text()
except Exception as e:
    print('Read error:', e)
    text = ''
lines = text.splitlines()
headers = [l for l in lines if l.startswith('>')]
print('Total lines:', len(lines))
print('Header count:', len(headers))
headers_with_os = [h for h in headers if 'OS=' in h]
print('Headers with OS=:', len(headers_with_os))
print('\nFirst 6 headers:')
for h in headers[:6]:
    print(h)

print('\nParsed organism names (first 10):')
parsed = []
for h in headers_with_os:
    start = h.index('OS=') + 3
    rest = h[start:].split()
    name = rest[0] + ((' ' + rest[1]) if len(rest) > 1 else '')
    parsed.append(name)
    if len(parsed) >= 10:
        break
for p in parsed:
    print(p)

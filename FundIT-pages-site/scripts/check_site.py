"""Check generated links, fragment targets, unchanged downloads, and search coverage."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '.site-build/output'
PREFIX = '/FundIT/'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for attribute in ('href', 'src'):
            if attribute in attrs and tag != 'link':
                self.links.append(attrs[attribute])


def check():
    pages = {p.resolve(): Page(p.read_text()) for p in OUTPUT.rglob('*.html')
             if p.name != 'spoilguard.html'}  # The prototype is published as-is.
    errors = []
    count = 0
    for path, page in pages.items():
        if path.name == '404.html':
            continue  # Relative assets intentionally depend on the missing URL.
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            count += 1
            if url.path.startswith(PREFIX):
                target = OUTPUT / unquote(url.path.removeprefix(PREFIX))
            else:
                target = path.parent / unquote(url.path) if url.path else path
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            if not target.exists():
                errors.append(f'{path.relative_to(OUTPUT)}: missing {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(OUTPUT)}: missing anchor {link}')
    downloads = [*ROOT.glob('Simple_Calculator_Lab/*.py'), *ROOT.glob('Beyond_Calculator_Projects/*.py'),
                 *ROOT.glob('Database_basics_postgress/sql/**/*.sql'), *ROOT.glob('Database_basic_SQL_lite/*.ipynb'),
                 ROOT / 'final_project/spoilguard.html']
    for source in downloads:
        relative = source.relative_to(ROOT)
        assert (OUTPUT / relative).read_bytes() == source.read_bytes(), f'Changed download: {relative}'
        if source.suffix in ('.py', '.sql'):
            rendered = (ROOT / '.site-build/source' / relative.with_suffix('.md')).read_text()
            assert source.read_text().rstrip() in rendered, f'Changed code: {relative}'
    search = json.loads((OUTPUT / 'search/search_index.json').read_text())
    for script in ROOT.glob('Beyond_Calculator_Projects/*.py'):
        assert any(script.stem in entry['location'] for entry in search['docs']), script
    assert not errors, '\n'.join(errors)
    print(f'PASS: {len(pages)} pages, {count} local links/anchors, {len(downloads)} unchanged downloads, '
          'all projects searchable.')


if __name__ == '__main__':
    check()

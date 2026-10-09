"""Generate the course website from the canonical lab files. Never runs any lab code."""
import json
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.site-build/source'
REPO = 'https://github.com/ntious/FundIT'
BINDER = 'https://mybinder.org/v2/gh/ntious/FundIT/HEAD?labpath='
COLAB = 'https://colab.research.google.com/github/ntious/FundIT/blob/main/'

# Order and focus follow the table in the repository README.
PROJECTS = [
    ('temperature_converter', 'Functions and validation'),
    ('advanced_calculator', 'State management'),
    ('bill_splitter', 'Arithmetic and formatted output'),
    ('age_calculator', 'Working with datetime'),
    ('guessing_game', 'Loops and logic'),
    ('palindrome_checker', 'String manipulation'),
    ('expense_tracker', 'File I/O and CSV'),
    ('password_checker', 'Rules and regular expressions'),
    ('file_organizer', 'Automation and the filesystem'),
    ('grade_analyzer', 'Lists, loops, and averages'),
]
SQL_LABS = [
    ('lab1_select', 'Lab 1 · SELECT and ORDER BY'),
    ('lab2_filter_join', 'Lab 2 · Filtering and joins'),
    ('lab3_groupby', 'Lab 3 · GROUP BY and aggregates'),
    ('lab4_subqueries', 'Lab 4 · Subqueries'),
    ('lab5_updates_indexes', 'Lab 5 · Updates and indexes'),
]
SQL_SETUP = [('00_init', 'Database initialisation'), ('01_schema', 'Table definitions'), ('02_seed', 'Sample data')]


def fence(text, language, title=''):
    # Choose a fence longer than any backtick run in the content.
    marks = '`' * max(3, max((len(s) + 1 for s in re.findall(r'`+', text)), default=3))
    attrs = f' title="{title}"' if title else ''
    return f'{marks}{language}{attrs}\n{text.rstrip()}\n{marks}'


def rewrite_links(text, page):
    """Point source-file links at their reading pages and drop links to files that do not exist."""
    def replace(match):
        label, target = match.group(1), match.group(2)
        if '://' in target or target.startswith(('#', 'mailto:')):
            return match.group(0)
        if '@' in target and '/' not in target:
            return f'[{label}](mailto:{target})'
        path, _, anchor = target.partition('#')
        if path.endswith('.py'):
            path = path[:-3] + '.md'
        if not (SOURCE / page.parent / path).resolve().exists() and not (ROOT / page.parent / path).exists():
            return label  # e.g. placeholder screenshots in a student template
        return f'[{label}]({path}{"#" + anchor if anchor else ""})'
    # Repair links written as [text]([label](url)) so they point at the inner URL.
    text = re.sub(r'\]\(\[[^\]]*\]\(([^)\s]+)\)\)', r'](\1)', text)
    return re.sub(r'\[([^\]]*)\]\(([^)\s]+)\)', replace, text)


def copy(relative, destination=None):
    target = SOURCE / (destination or relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / relative, target)
    return target


def write(relative, text, links=True):
    target = SOURCE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rewrite_links(text, Path(relative)) if links else text, encoding='utf-8')


def buttons(*links):
    return ' '.join(f'[{label}]({url}){{ .md-button{" .md-button--primary" if i == 0 else ""} }}'
                    for i, (label, url) in enumerate(links))


def docstring(path):
    match = re.match(r'\s*"""(.*?)"""', path.read_text(encoding='utf-8'), re.S)
    lines = [line.strip() for line in match.group(1).strip().splitlines()] if match else [path.stem]
    body = [line for line in lines[1:] if line and not line.startswith(('Author', 'Date', 'Inputs', 'Structured'))]
    return lines[0], ' '.join(body)


def script_page(relative, title, summary, back):
    path = ROOT / relative
    copy(relative)
    return '\n\n'.join([
        f'# {title}',
        summary,
        buttons(('Run in Binder', BINDER + relative), ('Download script', path.name),
                ('View on GitHub', f'{REPO}/blob/main/{relative}')),
        '!!! tip "Read here. Run it in a terminal."\n'
        f'    Binder opens JupyterLab with this file. Choose **File → New → Terminal**, then run '
        f'`python {relative}`. On your own computer, run `python {path.name}` from its folder. '
        'Binder sessions are temporary, so download any changes before you leave.',
        '## The program',
        'Look for the `INPUTS`, `STORAGE`, `PROCESSING` and `OUTPUT` sections as you read.',
        fence(path.read_text(encoding='utf-8'), 'python', path.name),
        f'[← {back[0]}]({back[1]})',
    ]) + '\n'


def notebook_page(relative):
    path = ROOT / relative
    copy(relative)
    chunks = []
    for cell in json.loads(path.read_text(encoding='utf-8'))['cells']:
        source = ''.join(cell['source'])
        if cell['cell_type'] == 'code':
            chunks.append(fence(source, 'sql' if source.lstrip().startswith('%%sql') else 'python'))
        else:
            chunks.append(source)
    chunks.insert(1, buttons(('Run in Binder', BINDER + relative), ('Open in Colab', COLAB + relative),
                             ('Download notebook', path.name)) + '\n\n'
                  '!!! tip "Read here. Practice in a notebook."\n'
                  '    This page shows the original notebook without outputs. Open it in Binder or Colab and '
                  'run the cells from top to bottom; the first code cell installs what the lab needs. '
                  'Download your work before leaving, because sessions are temporary.\n\n'
                  f'[View original source]({REPO}/blob/main/{relative})')
    return '\n\n'.join(chunks) + '\n'


def sql_page(relative, title):
    path = ROOT / relative
    copy(relative)
    return '\n\n'.join([
        f'# {title}',
        buttons(('Download SQL file', path.name), ('View on GitHub', f'{REPO}/blob/main/{relative}')),
        'Run these tasks in Adminer\'s **SQL command** tab or in `psql`. '
        '[Set up the PostgreSQL lab first](../../index.md) if you have not already.',
        fence(path.read_text(encoding='utf-8'), 'sql', path.name),
    ]) + '\n'


def build():
    if SOURCE.exists():
        shutil.rmtree(SOURCE)  # Only our generated directory.
    SOURCE.mkdir(parents=True)
    shutil.copytree(ROOT / 'website/stylesheets', SOURCE / 'stylesheets')

    # Copy downloadable files first so link rewriting can see them.
    copy('LICENSE', 'LICENSE.txt')
    for relative in ['final_project/spoilguard.html',
                     'final_project/doc/Semester Project Milestone 5 Sample submission file.pdf']:
        copy(relative)

    # Repository-level documents.
    write('repository.md', (ROOT / 'README.md').read_text(encoding='utf-8'))
    write('CONTRIBUTING.md', (ROOT / 'CONTRIBUTING.md').read_text(encoding='utf-8'))
    write('SECURITY.md', (ROOT / 'SECURITY.md').read_text(encoding='utf-8'))
    write('LICENSE.md', '# License\n\n' + fence((ROOT / 'LICENSE').read_text(encoding='utf-8'), 'text')
          + '\n\n[Download the license file](LICENSE.txt)\n', links=False)

    # Lab 1: simple calculator.
    write('Simple_Calculator_Lab/calculator.md', script_page(
        'Simple_Calculator_Lab/calculator.py', 'Calculator program',
        'The finished in-class program. Compare it with your own version once you have tried the lab.',
        ('Back to the lab instructions', 'index.md')), links=False)
    write('Simple_Calculator_Lab/index.md', (ROOT / 'Simple_Calculator_Lab/README.md').read_text(encoding='utf-8')
          + '\n\n---\n\n[Read the finished calculator program](calculator.md){ .md-button }\n')

    # Optional projects.
    cards, project_nav = [], []
    for i, (stem, focus) in enumerate(PROJECTS, 1):
        relative = f'Beyond_Calculator_Projects/{stem}.py'
        title, summary = docstring(ROOT / relative)
        write(f'Beyond_Calculator_Projects/{stem}.md',
              script_page(relative, title, f'**Focus:** {focus}. {summary}',
                          ('All optional projects', 'index.md')), links=False)
        cards.append(f'- **{i:02d} · [{title}](Beyond_Calculator_Projects/{stem}.md)**\n\n    {focus}')
        project_nav.append({f'{i:02d} · {title}': f'Beyond_Calculator_Projects/{stem}.md'})
    write('Beyond_Calculator_Projects/index.md', (ROOT / 'Beyond_Calculator_Projects/README.md').read_text(encoding='utf-8'))

    # Lab 2: SQLite notebook.
    write('Database_basic_SQL_lite/SQL_Lab.md', notebook_page('Database_basic_SQL_lite/SQL_Lab.ipynb'), links=False)
    write('Database_basic_SQL_lite/index.md', (ROOT / 'Database_basic_SQL_lite/README.md').read_text(encoding='utf-8')
          + '\n\n---\n\n[Read the lab notebook](SQL_Lab.md){ .md-button .md-button--primary }\n')

    # Lab 3: PostgreSQL in Codespaces.
    sql_nav = []
    for stem, title in SQL_LABS:
        write(f'Database_basics_postgress/sql/labs/{stem}.md',
              sql_page(f'Database_basics_postgress/sql/labs/{stem}.sql', title), links=False)
        sql_nav.append({title: f'Database_basics_postgress/sql/labs/{stem}.md'})
    for stem, title in SQL_SETUP:
        write(f'Database_basics_postgress/sql/{stem}.md',
              sql_page(f'Database_basics_postgress/sql/{stem}.sql', title).replace('../../index.md', '../index.md'),
              links=False)
    readme = (ROOT / 'Database_basics_postgress/README.md').read_text(encoding='utf-8')
    readme = re.sub(r'`(lab\d_\w+)\.sql`', r'[`\1.sql`](sql/labs/\1.md)', readme)
    write('Database_basics_postgress/index.md', readme)

    # Lab 4: semester project prototype.
    write('final_project/prototype.md', '\n\n'.join([
        '# SpoilGuard live prototype',
        'A sample Milestone 5 prototype. Click through all four use cases, then look at how each screen maps '
        'to a requirement. Remember: study it, do not copy it.',
        buttons(('Open full screen', 'spoilguard.html'), ('Read the prototype guide', 'index.md'),
                ('Sample submission (PDF)', 'doc/Semester Project Milestone 5 Sample submission file.pdf')),
        '<iframe class="prototype-frame" src="../spoilguard.html" title="SpoilGuard prototype" loading="lazy"></iframe>',
    ]) + '\n', links=False)
    for name in ('Student_README.md', 'testing_plan.md'):
        write(f'final_project/doc/{name}', (ROOT / 'final_project/doc' / name).read_text(encoding='utf-8'))

    readme = (ROOT / 'final_project/README.md').read_text(encoding='utf-8').replace(
        '### Option 2 (If GitHub Pages is enabled)\n- Open the live link provided in the repo',
        '### Option 2 (Online)\n- [Open the live prototype](prototype.md)')
    write('final_project/index.md', readme
          + '\n\n---\n\n[Open the live prototype](prototype.md){ .md-button .md-button--primary } '
          '[Student README template](doc/Student_README.md){ .md-button } '
          '[Testing plan template](doc/testing_plan.md){ .md-button }\n')
    home = (ROOT / 'website/home.md').read_text(encoding='utf-8').replace('<!-- PROJECTS -->', '\n\n'.join(cards))
    write('index.md', home)

    config = yaml.safe_load((ROOT / 'mkdocs.yml').read_text())
    config['nav'] = [
        {'Welcome': 'index.md'},
        {'Python labs': [
            {'Simple Calculator Lab': 'Simple_Calculator_Lab/index.md'},
            {'Calculator program': 'Simple_Calculator_Lab/calculator.md'},
            {'Beyond the calculator': 'Beyond_Calculator_Projects/index.md'},
            *project_nav]},
        {'Databases': [
            {'SQLite lab': 'Database_basic_SQL_lite/index.md'},
            {'SQLite notebook': 'Database_basic_SQL_lite/SQL_Lab.md'},
            {'PostgreSQL lab': 'Database_basics_postgress/index.md'},
            *sql_nav,
            *[{title: f'Database_basics_postgress/sql/{stem}.md'} for stem, title in SQL_SETUP]]},
        {'Semester project': [
            {'Prototype guide': 'final_project/index.md'},
            {'Live prototype': 'final_project/prototype.md'},
            {'Student README template': 'final_project/doc/Student_README.md'},
            {'Testing plan template': 'final_project/doc/testing_plan.md'}]},
        {'About': [
            {'Repository overview': 'repository.md'},
            {'Contributing': 'CONTRIBUTING.md'},
            {'Security policy': 'SECURITY.md'},
            {'License': 'LICENSE.md'}]},
    ]
    # Absolute paths keep the generated config independent of its own location.
    config['docs_dir'] = str(SOURCE)
    config['site_dir'] = str(ROOT / '.site-build/output')
    (ROOT / '.site-build/mkdocs.yml').write_text(yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
    print(f'Prepared {len(PROJECTS) + 1} Python pages, {len(SQL_LABS) + len(SQL_SETUP)} SQL pages and 1 notebook; '
          'originals unchanged.')


if __name__ == '__main__':
    build()

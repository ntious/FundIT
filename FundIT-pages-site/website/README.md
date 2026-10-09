# Course website maintenance

The website is built with MkDocs Material, in the same style as the Python Foundations course site. The lab folders, READMEs, scripts, SQL files and notebook remain the authoritative teaching materials. Do not edit generated pages.

From the repository root, in a separate website virtual environment:

```sh
python -m pip install -r requirements-site.txt
python scripts/build_site.py
mkdocs build --strict -f .site-build/mkdocs.yml
python scripts/check_site.py
mkdocs serve -f .site-build/mkdocs.yml
```

The generator copies only public course files: lab READMEs, Python scripts, SQL files, the SQLite notebook, the SpoilGuard prototype and its sample PDF, and the license. Each script and SQL file gets a reading page with its exact source plus Binder and download buttons. The notebook is shown cell by cell without running it. Downloads are byte-for-byte copies of the originals.

Edit `website/home.md` for the welcome page and `website/stylesheets/course.css` for appearance. To add an optional project, add the script to `Beyond_Calculator_Projects/` and add a line to `PROJECTS` in `scripts/build_site.py`. New SQL labs go in `SQL_LABS`.

GitHub Actions builds and checks links on pull requests. A successful build on `main` publishes to GitHub Pages using the `github-pages` environment. In repository Settings → Pages, the source must be **GitHub Actions**.

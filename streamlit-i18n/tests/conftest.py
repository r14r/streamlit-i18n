import sys
from pathlib import Path

import pytest


@pytest.fixture
def demo_tree(tmp_path: Path, monkeypatch):
    """
    Create a minimal demo project layout in a temp folder:

      <tmp>/lib/i18n/dataclasses.py
      <tmp>/lib/i18n/locales/en.yml
      <tmp>/lib/i18n/locales/de.yml
    """

    lib = tmp_path / "lib"
    i18n_pkg = lib / "i18n"
    locales = i18n_pkg / "locales"
    i18n_pkg.mkdir(parents=True, exist_ok=True)
    locales.mkdir(parents=True, exist_ok=True)

    # Make i18n a package
    (i18n_pkg / "__init__.py").write_text("", encoding="utf-8")

    # Minimal generated dataclasses module (no instance fields)
    (i18n_pkg / "dataclasses.py").write_text(
        """from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = ''
    DESC: str = ''

@dataclass
class PAGES:
    @dataclass
    class PAGE1:
        TITLE: str = ''
        DESC: str = ''
    @dataclass
    class PAGE2:
        TITLE: str = ''
""",
        encoding="utf-8",
    )

    # YAMLs
    (locales / "en.yml").write_text(
        """app:
  title: "TITLE"
  desc: "DESCRIBES"
pages:
  page1:
    title: "TITLE"
    desc: "DESCRIPTION"
  page2:
    title: "Another title"
""",
        encoding="utf-8",
    )

    (locales / "de.yml").write_text(
        """app:
  title: "TITEL"
  desc: "BESCHREIBT"
pages:
  page1:
    title: "TITEL"
""",
        encoding="utf-8",
    )

    # Make lib importable
    monkeypatch.chdir(tmp_path)
    if str(lib) not in sys.path:
        sys.path.insert(0, str(lib))

    return {
        "root": tmp_path,
        "lib": lib,
        "i18n_pkg": i18n_pkg,
        "locales": locales,
    }

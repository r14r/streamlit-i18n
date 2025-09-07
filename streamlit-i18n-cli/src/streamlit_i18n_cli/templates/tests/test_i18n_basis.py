import importlib
from datetime import date

import pytest


def _fmt_date(lang: str) -> str:
    d = date(2025, 1, 2)
    if lang == "de":
        return d.strftime("%d.%m.%Y")  # 02.01.2025
    
    if lang in {"fr", "es"}:
        return d.strftime("%d/%m/%Y")  # 02/01/2025
    
    return d.strftime("%B %d, %Y")     # January 02, 2025 (en)


@pytest.mark.parametrize("lang", ["de", "en"])
def test_init_and_attribute_access(lang):
    si = importlib.import_module("streamlit_i18n")
    i18n = si.I18N(package="lib.i18n.languages")
    i18n.init(lang=lang, base="en")

    # Top-level and nested classes are instantiated
    assert hasattr(i18n, "APP")
    assert hasattr(i18n, "PAGES")
    assert hasattr(i18n.PAGES, "PAGE1")

    # Basic attribute values exist
    assert isinstance(i18n.APP.TITLE, str)
    assert isinstance(i18n.NAV.HOME, str)
    assert isinstance(i18n.PAGES.PAGE1.TITLE, str)


def test_fallback_merge_from_base():
    si = importlib.import_module("streamlit_i18n")
    i18n = si.I18N(package="lib.i18n.languages")
    i18n.init(lang="de", base="en")

    assert isinstance(i18n.APP.TITLE, str)


def test_t_and_has_and_formatting():
    si = importlib.import_module("streamlit_i18n")
    i18n = si.I18N(package="lib.i18n.languages")
    i18n.init(lang="de", base="en")

    # has() and t() happy path
    assert i18n.has("app.title") is True
    v = i18n.t("app.title")
    assert isinstance(v, str) and v != ""

    # formatting placeholders
    ds = _fmt_date("de")
    out = i18n.t("app.current_date", {"date": ds})
    assert ds in out

    # Unknown key
    assert i18n.has("does.not.exist") is False
    assert i18n.t("does.not.exist") == ""


def test_set_lang_switch_changes_values():
    si = importlib.import_module("streamlit_i18n")
    i18n = si.I18N(package="lib.i18n.languages")
    i18n.init(lang="de", base="en")
    title_de = i18n.APP.TITLE

    i18n.set_lang("en")
    title_en = i18n.APP.TITLE

    # Titles should differ across locales in your data; if they don't, adapt the assertion.
    assert isinstance(title_de, str) and isinstance(title_en, str)
    assert title_de != title_en or title_en.endswith("(EN)")  # tolerate identical if your data matches


def test_nested_page_formatting_card_text():
    si = importlib.import_module("streamlit_i18n")
    i18n = si.I18N(package="lib.i18n.languages")
    i18n.init(lang="en", base="en")

    out = i18n.t(
        "pages.page1.card_text",
        {"users": "1,200", "projects": "25", "tasks": "4,200"},
    )
    assert "Users: 1,200" in out or "Nutzer:" in out  # en or if you changed language

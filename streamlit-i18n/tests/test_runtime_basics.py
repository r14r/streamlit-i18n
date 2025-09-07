import importlib


def test_init_and_access(demo_tree):
    # Import runtime from package under test
    streamlit_i18n = importlib.import_module("streamlit_i18n")

    # initialize with de, fallback to en; locales dir is lib/i18n/locales (default)
    streamlit_i18n.init("de", base_lang="en")

    import i18n  # generated dataclasses module lives under lib/i18n

    # German overrides
    assert i18n.APP.TITLE == "TITEL"
    assert i18n.APP.DESC == "BESCHREIBT"

    # Present in en but missing in de -> fallback (pages.page2.title)
    assert i18n.PAGES.PAGE2.TITLE == "Another title"

    # Dotted access
    assert streamlit_i18n.t("app.title") == "TITEL"
    assert streamlit_i18n.t("pages.page2.title") == "Another title"


def test_set_lang_switches_language(demo_tree):
    streamlit_i18n = importlib.import_module("streamlit_i18n")
    streamlit_i18n.init("de", base_lang="en")
    assert streamlit_i18n.t("app.title") == "TITEL"
    streamlit_i18n.set_lang("en")
    assert streamlit_i18n.t("app.title") == "TITLE"


def test_missing_keys(demo_tree):
    streamlit_i18n = importlib.import_module("streamlit_i18n")
    streamlit_i18n.init("de", base_lang="en")
    miss = set(streamlit_i18n.missing_keys())
    # 'pages.page2.title' exists in base but not in current (de)
    assert "pages.page2.title" in miss


def test_interpolation(demo_tree):
    streamlit_i18n = importlib.import_module("streamlit_i18n")
    # Add a string with formatting to english file
    (demo_tree["locales"] / "en.yml").write_text(
        """app:
  title: "TITLE"
  desc: "Hello, {name}!"
""",
        encoding="utf-8",
    )
    streamlit_i18n.init("en")
    assert streamlit_i18n.t("app.desc", {"name": "Ralph"}) == "Hello, Ralph!"

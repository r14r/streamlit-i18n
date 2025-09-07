import importlib


def test_env_override_module_name(demo_tree, monkeypatch):
    # Rename dataclasses.py -> custom_dataclasses.py and import via env var
    (demo_tree["i18n_pkg"] / "custom_dataclasses.py").write_text(
        (demo_tree["i18n_pkg"] / "dataclasses.py").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (demo_tree["i18n_pkg"] / "dataclasses.py").unlink()

    # Now point to custom module
    monkeypatch.setenv("I18N_DATACLASSES", "i18n.custom_dataclasses")

    streamlit_i18n = importlib.import_module("streamlit_i18n")
    streamlit_i18n.init("en")  # should import via env override

    import i18n as _  # noqa: F401  # still the package namespace

    # Sanity check
    assert streamlit_i18n.t("app.title") == "TITLE"

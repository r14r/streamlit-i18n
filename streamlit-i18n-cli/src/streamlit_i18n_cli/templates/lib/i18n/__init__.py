from streamlit_i18n import I18N

base = "en"
i18n = I18N(package="lib.i18n.languages")
i18n.init(lang="de", base=base)


__all__ = ["I18N", "i18n"]

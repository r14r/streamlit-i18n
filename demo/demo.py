import sys
from streamlit_i18n import I18N

def main(lang = "de") -> None:
    i18n = I18N(package="lib.i18n.languages")
    i18n.init(lang=lang, base="en")

    print("# APP / HEADER")
    print(i18n.APP.TITLE)
    print(i18n.t("app.desc"))
    print(i18n.t("app.current_user", {"name": "Ralph"}))
    print(i18n.t("app.copyright", {"year": 2025}))
    print("")

    print("# NAVIGATION")
    print("NAV:", i18n.NAV.HOME, "|", i18n.NAV.ABOUT, "|", i18n.NAV.CONTACT, "|", i18n.NAV.SETTINGS)

    print("# MESSAGES & ERRORS")
    print(i18n.t("messages.welcome", {"name": "Ralph"}))
    print(i18n.t("messages.items_found", {"count": 7}))
    print(i18n.ERRORS.INVALID_EMAIL)
    print(i18n.t("errors.too_short", {"min": 3}))
    print("")

    print("# FORMS")
    print(i18n.FORMS.LOGIN.TITLE)
    print(i18n.FORMS.LOGIN.EMAIL, "/", i18n.FORMS.LOGIN.PASSWORD, "→", i18n.FORMS.LOGIN.SUBMIT)
    print(i18n.FORMS.PROFILE.TITLE, "→", i18n.FORMS.PROFILE.SAVE)
    print("")

    print("# PAGES")
    print(i18n.PAGES.HOME.TITLE)
    print(i18n.PAGES.HOME.LEAD)
    print(i18n.PAGES.HOME.CTA_PRIMARY, "/", i18n.PAGES.HOME.CTA_SECONDARY)

    print(i18n.PAGES.PAGE1.TITLE)
    print(i18n.PAGES.PAGE1.DESC)
    print(i18n.t("pages.page1.card_text", {"users": 12, "projects": 5, "tasks": 42}))

    print(i18n.PAGES.PAGE2.TITLE)
    print(i18n.PAGES.PAGE2.DESC, "|", i18n.PAGES.PAGE2.EDIT, "|", i18n.PAGES.PAGE2.DELETE)

    print(i18n.PAGES.ADMIN.TITLE, "→", i18n.PAGES.ADMIN.USERS, "/", i18n.PAGES.ADMIN.ROLES, "/", i18n.PAGES.ADMIN.AUDIT)
    print("")

    print("# — Tables")
    print(i18n.TABLE.USERS.TITLE, "→", i18n.TABLE.USERS.COL_NAME, i18n.TABLE.USERS.COL_EMAIL, i18n.TABLE.USERS.COL_ROLE)
    print(i18n.TABLE.PROJECTS.TITLE, "→", i18n.TABLE.PROJECTS.COL_TITLE, i18n.TABLE.PROJECTS.COL_OWNER, i18n.TABLE.PROJECTS.COL_STATUS)
    print("")

    print("# FOOTER")
    print(i18n.FOOTER.LINKS_TITLE, "→", i18n.FOOTER.IMPRINT, "/", i18n.FOOTER.PRIVACY, "/", i18n.FOOTER.HELP)

    print("# Dotted-API: beliebige Schlüssel")
    print("Dotted:", i18n.t("nav.language"))

    print("# Existenz prüfen")
    print("Has app.title?", i18n.has("app.title"))
    print("Has pages.missing.key?", i18n.has("pages.missing.key"))

if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "de"
    print(f"Using language: {lang}")

    main(lang=lang)

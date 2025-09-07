from __future__ import annotations
from dataclasses import dataclass
from typing import Any

# Auto-generated from: lib/i18n/locales/en.yml
# Do not edit by hand.

@dataclass
class APP:
    TITLE: str = ''
    DESC: str = ''
    COPYRIGHT: str = ''
    LOCALE_NAME: str = ''
    CURRENT_USER: str = ''

@dataclass
class NAV:
    HOME: str = ''
    ABOUT: str = ''
    CONTACT: str = ''
    SETTINGS: str = ''
    LOGOUT: str = ''
    LANGUAGE: str = ''

@dataclass
class MESSAGES:
    WELCOME: str = ''
    ITEMS_FOUND: str = ''
    SAVED: str = ''
    UPDATED: str = ''
    DELETED: str = ''
    CONFIRM_DELETE: str = ''

@dataclass
class ERRORS:
    REQUIRED: str = ''
    INVALID_EMAIL: str = ''
    TOO_SHORT: str = ''
    UNAUTHORIZED: str = ''
    NOT_FOUND: str = ''
    SERVER: str = ''

@dataclass
class FORMS:

    @dataclass
    class LOGIN:
        TITLE: str = ''
        EMAIL: str = ''
        PASSWORD: str = ''
        SUBMIT: str = ''
        FORGOT: str = ''

    @dataclass
    class PROFILE:
        TITLE: str = ''
        NAME: str = ''
        BIO: str = ''
        SAVE: str = ''

@dataclass
class PAGES:

    @dataclass
    class HOME:
        TITLE: str = ''
        LEAD: str = ''
        CTA_PRIMARY: str = ''
        CTA_SECONDARY: str = ''

    @dataclass
    class PAGE1:
        TITLE: str = ''
        DESC: str = ''
        CARD_TITLE: str = ''
        CARD_TEXT: str = ''

    @dataclass
    class PAGE2:
        TITLE: str = ''
        DESC: str = ''
        EDIT: str = ''
        DELETE: str = ''
        BACK: str = ''

    @dataclass
    class ADMIN:
        TITLE: str = ''
        USERS: str = ''
        ROLES: str = ''
        AUDIT: str = ''

@dataclass
class TABLE:

    @dataclass
    class USERS:
        TITLE: str = ''
        COL_NAME: str = ''
        COL_EMAIL: str = ''
        COL_ROLE: str = ''
        EMPTY: str = ''

    @dataclass
    class PROJECTS:
        TITLE: str = ''
        COL_TITLE: str = ''
        COL_OWNER: str = ''
        COL_STATUS: str = ''
        EMPTY: str = ''

@dataclass
class FOOTER:
    LINKS_TITLE: str = ''
    IMPRINT: str = ''
    PRIVACY: str = ''
    HELP: str = ''


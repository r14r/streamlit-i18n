from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = 'Streamlit i18n – Demo (DE)'
    DESC: str = 'Beispielanwendung für vor-generierte Dataclasses mit Fallback auf Englisch.'
    COPYRIGHT: str = '© {year} Deine Firma'
    LOCALE_NAME: str = 'Deutsch (DE)'
    CURRENT_USER: str = 'Angemeldet als: {name}'


@dataclass
class NAV:
    HOME: str = 'Start'
    ABOUT: str = 'Über'
    CONTACT: str = 'Kontakt'
    SETTINGS: str = 'Einstellungen'
    LOGOUT: str = 'Abmelden'
    LANGUAGE: str = 'Sprache'


@dataclass
class MESSAGES:
    WELCOME: str = 'Willkommen, {name}!'
    ITEMS_FOUND: str = '{count} Elemente gefunden'
    SAVED: str = 'Erfolgreich gespeichert.'
    UPDATED: str = 'Aktualisierung erfolgreich.'
    DELETED: str = 'Eintrag gelöscht.'
    CONFIRM_DELETE: str = 'Möchtest du „{title}“ wirklich löschen?'


@dataclass
class ERRORS:
    REQUIRED: str = 'Dieses Feld ist erforderlich.'
    INVALID_EMAIL: str = 'Bitte eine gültige E-Mail-Adresse eingeben.'
    TOO_SHORT: str = 'Der Wert ist zu kurz (min. {min} Zeichen).'
    UNAUTHORIZED: str = 'Nicht autorisiert.'
    NOT_FOUND: str = 'Nicht gefunden.'
    SERVER: str = 'Unerwarteter Serverfehler. Bitte später erneut versuchen.'


@dataclass
class FORMS:

    @dataclass
    class LOGIN:
        TITLE: str = 'Anmeldung'
        EMAIL: str = 'E-Mail'
        PASSWORD: str = 'Passwort'
        SUBMIT: str = 'Einloggen'
        FORGOT: str = 'Passwort vergessen?'

    @dataclass
    class PROFILE:
        TITLE: str = 'Profil'
        NAME: str = 'Name'
        BIO: str = 'Kurzbeschreibung'
        SAVE: str = 'Speichern'


@dataclass
class PAGES:

    @dataclass
    class HOME:
        TITLE: str = 'Startseite'
        LEAD: str = 'Das ist die Startseite deiner Demo.'
        CTA_PRIMARY: str = 'Jetzt starten'
        CTA_SECONDARY: str = 'Mehr erfahren'

    @dataclass
    class PAGE1:
        TITLE: str = 'Seite 1 – Überblick'
        DESC: str = 'Diese Seite zeigt eine Übersicht mit dynamischen Werten.'
        CARD_TITLE: str = 'Zusammenfassung'
        CARD_TEXT: str = 'Nutzer: {users}, Projekte: {projects}, Tasks: {tasks}'

    @dataclass
    class PAGE2:
        TITLE: str = 'Seite 2 – Details'
        DESC: str = 'Detailinformationen und Aktionen.'
        EDIT: str = 'Bearbeiten'
        DELETE: str = 'Löschen'
        BACK: str = 'Zurück'

    @dataclass
    class ADMIN:
        TITLE: str = 'Administration'
        USERS: str = 'Benutzerverwaltung'
        ROLES: str = 'Rollen & Rechte'
        AUDIT: str = 'Audit-Log'


@dataclass
class TABLE:

    @dataclass
    class USERS:
        TITLE: str = 'Benutzer'
        COL_NAME: str = 'Name'
        COL_EMAIL: str = 'E-Mail'
        COL_ROLE: str = 'Rolle'
        EMPTY: str = 'Keine Benutzer gefunden.'

    @dataclass
    class PROJECTS:
        TITLE: str = 'Projekte'
        COL_TITLE: str = 'Titel'
        COL_OWNER: str = 'Owner'
        COL_STATUS: str = 'Status'
        EMPTY: str = 'Keine Projekte vorhanden.'


@dataclass
class FOOTER:
    LINKS_TITLE: str = 'Links'
    IMPRINT: str = 'Impressum'
    PRIVACY: str = 'Datenschutz'
    HELP: str = 'Hilfe'

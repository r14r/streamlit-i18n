from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = 'Streamlit i18n – Demo (EN)'
    DESC: str = 'Sample app using pre-generated dataclasses with English fallback.'
    COPYRIGHT: str = '© {year} Your Company'
    LOCALE_NAME: str = 'English (EN)'
    CURRENT_USER: str = 'Signed in as: {name}'


@dataclass
class NAV:
    HOME: str = 'Home'
    ABOUT: str = 'About'
    CONTACT: str = 'Contact'
    SETTINGS: str = 'Settings'
    LOGOUT: str = 'Logout'
    LANGUAGE: str = 'Language'


@dataclass
class MESSAGES:
    WELCOME: str = 'Welcome, {name}!'
    ITEMS_FOUND: str = '{count} items found'
    SAVED: str = 'Saved successfully.'
    UPDATED: str = 'Updated successfully.'
    DELETED: str = 'Item deleted.'
    CONFIRM_DELETE: str = 'Do you really want to delete “{title}”?'


@dataclass
class ERRORS:
    REQUIRED: str = 'This field is required.'
    INVALID_EMAIL: str = 'Please enter a valid email address.'
    TOO_SHORT: str = 'The value is too short (min. {min} characters).'
    UNAUTHORIZED: str = 'Unauthorized.'
    NOT_FOUND: str = 'Not found.'
    SERVER: str = 'Unexpected server error. Please try again later.'


@dataclass
class FORMS:

    @dataclass
    class LOGIN:
        TITLE: str = 'Sign in'
        EMAIL: str = 'Email'
        PASSWORD: str = 'Password'
        SUBMIT: str = 'Log in'
        FORGOT: str = 'Forgot password?'

    @dataclass
    class PROFILE:
        TITLE: str = 'Profile'
        NAME: str = 'Name'
        BIO: str = 'Bio'
        SAVE: str = 'Save'


@dataclass
class PAGES:

    @dataclass
    class HOME:
        TITLE: str = 'Home'
        LEAD: str = 'This is the home page of your demo.'
        CTA_PRIMARY: str = 'Get started'
        CTA_SECONDARY: str = 'Learn more'

    @dataclass
    class PAGE1:
        TITLE: str = 'Page 1 – Overview'
        DESC: str = 'This page shows an overview with dynamic values.'
        CARD_TITLE: str = 'Summary'
        CARD_TEXT: str = 'Users: {users}, Projects: {projects}, Tasks: {tasks}'

    @dataclass
    class PAGE2:
        TITLE: str = 'Page 2 – Details'
        DESC: str = 'Detailed information and actions.'
        EDIT: str = 'Edit'
        DELETE: str = 'Delete'
        BACK: str = 'Back'

    @dataclass
    class ADMIN:
        TITLE: str = 'Administration'
        USERS: str = 'User Management'
        ROLES: str = 'Roles & Permissions'
        AUDIT: str = 'Audit Log'


@dataclass
class TABLE:

    @dataclass
    class USERS:
        TITLE: str = 'Users'
        COL_NAME: str = 'Name'
        COL_EMAIL: str = 'Email'
        COL_ROLE: str = 'Role'
        EMPTY: str = 'No users found.'

    @dataclass
    class PROJECTS:
        TITLE: str = 'Projects'
        COL_TITLE: str = 'Title'
        COL_OWNER: str = 'Owner'
        COL_STATUS: str = 'Status'
        EMPTY: str = 'No projects available.'


@dataclass
class FOOTER:
    LINKS_TITLE: str = 'Links'
    IMPRINT: str = 'Imprint'
    PRIVACY: str = 'Privacy'
    HELP: str = 'Help'

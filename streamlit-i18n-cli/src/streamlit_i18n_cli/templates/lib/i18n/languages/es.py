from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = 'Streamlit i18n – Demo (ES)'
    DESC: str = 'Aplicación de ejemplo con dataclasses pre-generadas y respaldo en inglés.'
    COPYRIGHT: str = '© {year} Tu empresa'
    LOCALE_NAME: str = 'Español (ES)'
    CURRENT_USER: str = 'Conectado como: {name}'


@dataclass
class NAV:
    HOME: str = 'Inicio'
    ABOUT: str = 'Acerca de'
    CONTACT: str = 'Contacto'
    SETTINGS: str = 'Ajustes'
    LOGOUT: str = 'Cerrar sesión'
    LANGUAGE: str = 'Idioma'


@dataclass
class MESSAGES:
    WELCOME: str = '¡Bienvenido, {name}!'
    ITEMS_FOUND: str = '{count} elementos encontrados'
    SAVED: str = 'Guardado correctamente.'
    UPDATED: str = 'Actualizado correctamente.'
    DELETED: str = 'Elemento eliminado.'
    CONFIRM_DELETE: str = '¿Seguro que deseas eliminar “{title}”?'


@dataclass
class ERRORS:
    REQUIRED: str = 'Este campo es obligatorio.'
    INVALID_EMAIL: str = 'Introduce un correo electrónico válido.'
    TOO_SHORT: str = 'El valor es demasiado corto (mín. {min} caracteres).'
    UNAUTHORIZED: str = 'No autorizado.'
    NOT_FOUND: str = 'No encontrado.'
    SERVER: str = 'Error de servidor inesperado. Inténtalo de nuevo más tarde.'


@dataclass
class FORMS:

    @dataclass
    class LOGIN:
        TITLE: str = 'Iniciar sesión'
        EMAIL: str = 'Correo'
        PASSWORD: str = 'Contraseña'
        SUBMIT: str = 'Entrar'
        FORGOT: str = '¿Olvidaste tu contraseña?'

    @dataclass
    class PROFILE:
        TITLE: str = 'Perfil'
        NAME: str = 'Nombre'
        BIO: str = 'Biografía'
        SAVE: str = 'Guardar'


@dataclass
class PAGES:

    @dataclass
    class HOME:
        TITLE: str = 'Inicio'
        LEAD: str = 'Esta es la página de inicio de tu demo.'
        CTA_PRIMARY: str = 'Comenzar'
        CTA_SECONDARY: str = 'Saber más'

    @dataclass
    class PAGE1:
        TITLE: str = 'Página 1 – Resumen'
        DESC: str = 'Esta página muestra un resumen con valores dinámicos.'
        CARD_TITLE: str = 'Resumen'
        CARD_TEXT: str = 'Usuarios: {users}, Proyectos: {projects}, Tareas: {tasks}'

    @dataclass
    class PAGE2:
        TITLE: str = 'Página 2 – Detalles'
        DESC: str = 'Información detallada y acciones.'
        EDIT: str = 'Editar'
        DELETE: str = 'Eliminar'
        BACK: str = 'Volver'

    @dataclass
    class ADMIN:
        TITLE: str = 'Administración'
        USERS: str = 'Gestión de usuarios'
        ROLES: str = 'Roles y permisos'
        AUDIT: str = 'Registro de auditoría'


@dataclass
class TABLE:

    @dataclass
    class USERS:
        TITLE: str = 'Usuarios'
        COL_NAME: str = 'Nombre'
        COL_EMAIL: str = 'Correo'
        COL_ROLE: str = 'Rol'
        EMPTY: str = 'No se encontraron usuarios.'

    @dataclass
    class PROJECTS:
        TITLE: str = 'Proyectos'
        COL_TITLE: str = 'Título'
        COL_OWNER: str = 'Responsable'
        COL_STATUS: str = 'Estado'
        EMPTY: str = 'No hay proyectos disponibles.'


@dataclass
class FOOTER:
    LINKS_TITLE: str = 'Enlaces'
    IMPRINT: str = 'Aviso legal'
    PRIVACY: str = 'Privacidad'
    HELP: str = 'Ayuda'

from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = 'Streamlit i18n – Démo (FR)'
    DESC: str = 'Application d’exemple avec dataclasses pré-générées et secours en anglais.'
    COPYRIGHT: str = '© {year} Votre entreprise'
    LOCALE_NAME: str = 'Français (FR)'
    CURRENT_USER: str = 'Connecté en tant que : {name}'


@dataclass
class NAV:
    HOME: str = 'Accueil'
    ABOUT: str = 'À propos'
    CONTACT: str = 'Contact'
    SETTINGS: str = 'Paramètres'
    LOGOUT: str = 'Se déconnecter'
    LANGUAGE: str = 'Langue'


@dataclass
class MESSAGES:
    WELCOME: str = 'Bienvenue, {name} !'
    ITEMS_FOUND: str = '{count} éléments trouvés'
    SAVED: str = 'Enregistré avec succès.'
    UPDATED: str = 'Mise à jour réussie.'
    DELETED: str = 'Élément supprimé.'
    CONFIRM_DELETE: str = 'Voulez-vous vraiment supprimer « {title} » ?'


@dataclass
class ERRORS:
    REQUIRED: str = 'Ce champ est obligatoire.'
    INVALID_EMAIL: str = 'Veuillez saisir une adresse e-mail valide.'
    TOO_SHORT: str = 'La valeur est trop courte (min. {min} caractères).'
    UNAUTHORIZED: str = 'Non autorisé.'
    NOT_FOUND: str = 'Introuvable.'
    SERVER: str = 'Erreur serveur inattendue. Réessayez plus tard.'


@dataclass
class FORMS:

    @dataclass
    class LOGIN:
        TITLE: str = 'Connexion'
        EMAIL: str = 'E-mail'
        PASSWORD: str = 'Mot de passe'
        SUBMIT: str = 'Se connecter'
        FORGOT: str = 'Mot de passe oublié ?'

    @dataclass
    class PROFILE:
        TITLE: str = 'Profil'
        NAME: str = 'Nom'
        BIO: str = 'Bio'
        SAVE: str = 'Enregistrer'


@dataclass
class PAGES:

    @dataclass
    class HOME:
        TITLE: str = 'Accueil'
        LEAD: str = 'Page d’accueil de votre démo.'
        CTA_PRIMARY: str = 'Commencer'
        CTA_SECONDARY: str = 'En savoir plus'

    @dataclass
    class PAGE1:
        TITLE: str = 'Page 1 – Vue d’ensemble'
        DESC: str = 'Cette page affiche un aperçu avec des valeurs dynamiques.'
        CARD_TITLE: str = 'Résumé'
        CARD_TEXT: str = 'Utilisateurs : {users}, Projets : {projects}, Tâches : {tasks}'

    @dataclass
    class PAGE2:
        TITLE: str = 'Page 2 – Détails'
        DESC: str = 'Informations détaillées et actions.'
        EDIT: str = 'Modifier'
        DELETE: str = 'Supprimer'
        BACK: str = 'Retour'

    @dataclass
    class ADMIN:
        TITLE: str = 'Administration'
        USERS: str = 'Gestion des utilisateurs'
        ROLES: str = 'Rôles et permissions'
        AUDIT: str = 'Journal d’audit'


@dataclass
class TABLE:

    @dataclass
    class USERS:
        TITLE: str = 'Utilisateurs'
        COL_NAME: str = 'Nom'
        COL_EMAIL: str = 'E-mail'
        COL_ROLE: str = 'Rôle'
        EMPTY: str = 'Aucun utilisateur trouvé.'

    @dataclass
    class PROJECTS:
        TITLE: str = 'Projets'
        COL_TITLE: str = 'Titre'
        COL_OWNER: str = 'Responsable'
        COL_STATUS: str = 'Statut'
        EMPTY: str = 'Aucun projet disponible.'


@dataclass
class FOOTER:
    LINKS_TITLE: str = 'Liens'
    IMPRINT: str = 'Mentions légales'
    PRIVACY: str = 'Confidentialité'
    HELP: str = 'Aide'

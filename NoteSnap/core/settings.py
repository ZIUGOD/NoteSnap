"""
Django settings for the Nyra project.
"""

from os import path
from pathlib import Path
import dj_database_url
import environ
from django.core.management.utils import get_random_secret_key
from .utils import color, get_local_ip

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment setup
env = environ.Env()
environ.Env.read_env()

# Debug
DEBUG = env.bool("DEBUG", default=False)

# Secret Key
if DEBUG:  # dev
    SECRET_KEY = env.str("SECRET_KEY", default=get_random_secret_key())
else:  # prod
    # Ensure the secret key is set in the environment for production
    SECRET_KEY = env.str("SECRET_KEY")

# Allowed Hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
if DEBUG:  # dev
    local_ip = get_local_ip()
    if local_ip:
        ALLOWED_HOSTS.extend(["0.0.0.0", local_ip])
    print(f"<> {color['cyan']}My allowed hosts: {ALLOWED_HOSTS}{color['end']}")
else:  # prod
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=ALLOWED_HOSTS)

# CSRF & Security Settings
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS",default=[
    "https://localhost:8000/",
    "https://127.0.0.1:8000/",
    "https://0.0.0.0:8000/",
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/u/login_user/",
    ] + ([f"http://{get_local_ip()}:8000"] if DEBUG else [])
)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=2592000)  # default == 30 days
SECURE_REFERRER_POLICY = "no-referrer"
SECURE_SSL_REDIRECT = DEBUG  # Set to True in production
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
X_FRAME_OPTIONS = "DENY"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Email
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="example@gmail.com")

# Database
if DEBUG:  # dev
    # Use SQLite for development
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:  # prod
    # Use PostgreSQL for production
    DATABASE_URL = env.str("DATABASE_URL")
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL, conn_max_age=500, conn_health_checks=True
        )
    }

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "features.members",
    "features.notes",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_ckeditor_5",
]

MIDDLEWARE = [
    # Django default middlewares 
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    # custom middlewares 
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Authentication redirects
LOGIN_REDIRECT_URL = "home_page"
LOGOUT_REDIRECT_URL = "member:login_user"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization
LANGUAGE_CODE = "en"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Static & Media files
STATIC_URL = "/static/"
STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "static_django"

MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, "media")

# Django crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# CKEditor 5
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"
CKEDITOR_5_CONFIGS = {
    "default": {
        "language": "en",
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "|",
            "link",
            "blockQuote",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "alignment:left",
            "alignment:center",
            "alignment:right",
            "alignment:justify",
            "|",
            "insertTable",
            "mediaEmbed",
            "|",
            "undo",
            "redo",
            "|",
            "highlight",
            "fontSize",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "imageUpload",
            "horizontalLine",
            "codeBlock",
            "|",
            "removeFormat",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "imageStyle:alignLeft",
                "imageStyle:alignCenter",
                "imageStyle:alignRight",
            ],
            "styles": [
                "alignLeft",
                "alignCenter",
                "alignRight",
                "alignBlockLeft",
                "alignBlockRight",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableCellProperties",
                "tableProperties",
            ]
        },
        "mediaEmbed": {"previewsInData": True},
        "fontSize": {"options": ["tiny", "small", "default", "big", "huge"]},
        "alignment": {"options": ["left", "center", "right", "justify"]},
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "upload": {
            "types": ["image/jpeg", "image/png", "image/gif", "image/webp", "video/mp4"]
        },
    },
    "minimal": {
        "language": "en",
        "toolbar": ["bold", "italic", "|", "link", "|", "undo", "redo"],
    },
    "full": {
        "language": "en",
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "|",
            "link",
            "blockQuote",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "alignment:left",
            "alignment:center",
            "alignment:right",
            "alignment:justify",
            "|",
            "insertTable",
            "mediaEmbed",
            "|",
            "undo",
            "redo",
            "|",
            "highlight",
            "fontSize",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "imageUpload",
            "horizontalLine",
            "codeBlock",
            "|",
            "removeFormat",
            "sourceEditing",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "imageStyle:alignLeft",
                "imageStyle:alignCenter",
                "imageStyle:alignRight",
            ]
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableCellProperties",
                "tableProperties",
            ]
        },
        "mediaEmbed": {"previewsInData": True},
        "fontSize": {"options": ["tiny", "small", "default", "big", "huge"]},
        "alignment": {"options": ["left", "center", "right", "justify"]},
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "upload": {
            "types": ["image/jpeg", "image/png", "image/gif", "image/webp", "video/mp4"]
        },
    },
}

# Auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

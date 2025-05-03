"""
Django settings for the Nyra project.
"""

from os import path
from pathlib import Path
import dj_database_url
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

# Security keys and debug mode
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)

# Allowed hosts and security settings
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=2592000)


if DEBUG:  # Development environment
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    SSL_KEY = env.str("SSL_KEY", default=None)

    # Use SQLite for local development
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": path.join(BASE_DIR, "db.sqlite3"),
        }
    }

else:  # Production environment
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    HOST_SCHEME = "https://"
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # Use database from environment variable in production (e.g., PostgreSQL or other)
    DATABASE_URL = env(
        "DATABASE_URL"
    )  # Example: postgresql://USER:PASSWORD@HOST:PORT/DBNAME
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL, conn_max_age=500, conn_health_checks=True
        )
    }

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="example@gmail.com")

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

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"

LOGOUT_REDIRECT_URL = "member:login_user"
LOGIN_REDIRECT_URL = "home_page"

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

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "static_django"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-ckeditor5 settings section
MEDIA_URL = "/media/"
MEDIA_ROOT = path.join(BASE_DIR, "media")

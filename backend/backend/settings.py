from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Basisverzeichnis des Projekts (backend/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Geheimer Schlüssel für Verschlüsselung (in Produktion durch sicheren ersetzen!)
SECRET_KEY = 'django-insecure-2s3j5tejle6xa%l!+f@phrgqp+!384ct&m5ifood2bxcl5$_+h'

# Debug-Modus: zeigt Fehlerdetails an - in Produktion auf False setzen!
DEBUG = True

# Erlaubte Hosts/ Domains ( "*" erlaubt alle - in Produktion einschränken!)
ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Registrierte Apps/ Komponenten
INSTALLED_APPS = [
    'django.contrib.admin',          # Admin-Oberfläche
    'django.contrib.auth',           # Authentifizierung
    'django.contrib.contenttypes',   # Inhaltstypen
    'django.contrib.sessions',       # Sitzungsverwaltung
    'django.contrib.messages',       # Flash-Nachrichten
    'django.contrib.staticfiles',    # Statische Dateien (CSS, JS)
    "api",                           # Eigene Todo-API-App
    "rest_framework",                # Django REST Framework
    "corsheaders",                   # Erlaubt Frontend-Anfragen von anderer Domain
]

# Middleware (wird bei jeder Anfrage durchlaufen)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",          # CORS-Header setzen
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',       # CSRF-Schutz
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Verweist auf die zentrale urls.py-Datei
ROOT_URLCONF = 'backend.urls'

# Template-Konfiguration (für Djangos Admin-Oberfläche)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-Konfiguration für den Produktionsserver
WSGI_APPLICATION = 'backend.wsgi.application'

# Datenbank-Konfiguration (hier SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',          # SQLite-Datenbank
        'NAME': BASE_DIR / 'db.sqlite3',                 # Speicherort der DB-Datei
    }
}

# Passwort-Validierungsregeln (für Admin-Benutzer)
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },  # Ähnlichkeit mit Benutzername
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },             # Mindestlänge
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },            # Keine geläufigen Passwörter
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },           # Nicht nur Zahlen
]

# Sprache und Zeitzone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True         # Internationalisierung aktivieren
USE_TZ = True           # Zeitzonen-Unterstützung

# Statische Dateien (CSS, JS, Bilder)
STATIC_URL = 'static/'

# Erlaubt Anfragen von allen Domains (für Entwicklung)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

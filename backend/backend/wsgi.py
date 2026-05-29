"""
WSGI-Konfiguration für das Backend-Projekt.

WSGI (Web Server Gateway Interface) ist der Standard,
um Django mit Produktionsservern (z.B. Apache, Nginx) zu verbinden.
"""

import os

from django.core.wsgi import get_wsgi_application

# Welche settings.py verwendet werden soll
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# WSGI-Anwendung - von Servern (wie Gunicorn) referenziert
application = get_wsgi_application()

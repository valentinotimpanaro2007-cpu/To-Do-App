"""
ASGI-Konfiguration für das Backend-Projekt.

ASGI (Asynchronous Server Gateway Interface) ist der moderne Nachfolger
von WSGI und ermöglicht asynchrone Verbindungen (z.B. WebSockets).
"""

import os

from django.core.asgi import get_asgi_application

# Welche settings.py verwendet werden soll
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# ASGI-Anwendung - von asynchronen Servern referenziert
application = get_asgi_application()

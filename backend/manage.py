#!/usr/bin/env python
"""Djangos Kommandozeilen-Dienstprogramm für administrative Aufgaben."""
import os
import sys


def main():
    """Führt administrative Aufgaben aus (z.B. Server starten, Migrationen)."""
    # Legt fest, welche settings.py-Datei Django verwenden soll
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        # Importiert Djangos interne Befehlszeilen-Ausführungsfunktion
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django konnte nicht importiert werden. Ist es installiert und "
            "die virtuelle Umgebung aktiviert?"
        ) from exc
    # Führt den übergebenen Befehl aus (z.B. "runserver", "migrate")
    execute_from_command_line(sys.argv)


# Nur ausführen, wenn diese Datei direkt aufgerufen wird (nicht beim Importieren)
if __name__ == '__main__':
    main()

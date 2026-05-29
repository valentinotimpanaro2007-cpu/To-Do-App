# Diese Migration wurde automatisch von Django erstellt.
# Sie erzeugt die erste Version der "Note"-Tabelle in der Datenbank.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True  # Dies ist die allererste Migration

    dependencies = []  # Keine Vorgänger-Migrationen

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Automatische ID
                ('title', models.CharField(max_length=100)),    # Titel-Spalte
                ('content', models.TextField()),                # Inhalt-Spalte
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Erstellungsdatum
            ],
        ),
    ]

# Zweite Migration: Fügt das Feld "completed" zur Note-Tabelle hinzu

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),  # Baut auf der ersten Migration auf
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='completed',
            field=models.BooleanField(default=False),  # Neues Boolean-Feld (Default: False)
        ),
    ]

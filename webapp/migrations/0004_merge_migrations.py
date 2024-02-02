#0004_merge_migrations.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
        ('webapp', '0003_auto_20231210_1501'),  # Use the correct migration name
    ]

    operations = [
        # Add the operations from both migrations
    ]

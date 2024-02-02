#0003_auto_20231210_1501.py

# Generated by Django 4.2.7 on 2023-12-10 07:01

from django.db import migrations, models

def set_default_size_unit(apps, schema_editor):
    CustomizedBoxOrder = apps.get_model('webapp', 'CustomizedBoxOrder')
    CustomizedBoxOrder.objects.filter(size_unit__isnull=True).update(size_unit='cm')

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),  # Add dependency on '0001_initial'
    ]

    operations = [
        migrations.AddField(
            model_name='customizedboxorder',
            name='size_unit',
            field=models.CharField(max_length=10, default='cm'),
        ),
        migrations.RunPython(set_default_size_unit),
    ]

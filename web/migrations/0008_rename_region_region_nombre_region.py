# Generated by Django 4.2 on 2024-06-03 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_inmueble_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='nombre_region',
        ),
    ]

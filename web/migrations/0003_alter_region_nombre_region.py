# Generated by Django 4.2 on 2024-05-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_comuna_region_tipo_inmueble_tipo_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='nombre_region',
            field=models.CharField(choices=[('Arica y Parinacota', 'Arica y Parinacota'), ('Tarapaca', 'Tarapaca'), ('Antofagasta', 'Antofagasta'), ('Atacama', 'Atacama'), ('Coquimbo', 'Coquimbo'), ('Valparaiso', 'Valparaiso'), ('Metropolitana', 'Metropolitana'), ('O Higgins', 'O Higgins'), ('Maule', 'Maule'), ('Nuble', 'Nuble'), ('Biobio', 'Biobio'), ('La Araucania', 'La Araucania'), ('Los Rios', 'Los Rios'), ('Los Lagos', 'Los Lagos'), ('Aysen', 'Aysen'), ('Magallanes', 'Magallanes')]),
        ),
    ]

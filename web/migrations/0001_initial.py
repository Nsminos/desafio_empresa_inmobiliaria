# Generated by Django 4.2 on 2024-05-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono_personal', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('tipo_de_usuario', models.CharField(choices=[('arrendatario', 'arrendatario'), ('arrendador', 'arrendador')], max_length=15)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-05-25 16:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_inmueble', models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Parcela', 'Parcela')])),
            ],
        ),
        migrations.CreateModel(
            name='tipo_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Arrendador', 'Arrendador'), ('Arrendatario', 'Arrendatario')])),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono_personal',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_de_usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono_personal', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipo_usuario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_inmueble', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_Totales_o_del_terreno', models.FloatField()),
                ('cantidad_de_estacionamientos', models.PositiveIntegerField(default=0)),
                ('cantidad_de_Habitaciones', models.PositiveIntegerField(default=0)),
                ('cantidad_de_banos', models.PositiveIntegerField(default=0)),
                ('precio_mensual_de_arriendo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('estado', models.BooleanField()),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.comuna')),
                ('id_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipo_inmueble')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.region')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

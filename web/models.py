from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

def validate_min_value(value):
    if value < 0:
        raise ValidationError(
            'El valor debe ser positivo'
        )



class Usuario(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    
    def __str___(self):
        return self.id_usuario.username

class Inmueble(models.Model):
    CHOICES=[
         ('Disponible', 'Disponible'),
        ('No Disponible', 'No Disponible')
    ]
    id_inmueble = models.ForeignKey('Tipo_inmueble', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)
    nombre_inmueble = models.CharField(max_length=50, null=False, unique=True)
    direccion = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=200, null=False, blank=False, default='Sin Descripcion')
    m2_construidos = models.FloatField(null=False, blank=False)
    m2_Totales_o_del_terreno = models.FloatField(null=False, blank=False)
    cantidad_de_estacionamientos = models.PositiveIntegerField(default=0, null=False, blank=False)
    cantidad_de_Habitaciones = models.PositiveIntegerField(default=0, null=False, blank=False)
    cantidad_de_banos = models.PositiveIntegerField(default=0, null=False, blank=False)
    precio_mensual_de_arriendo = models.IntegerField(validators=[MinValueValidator(0)],default=0, null=False, blank=False)
    estado = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.nombre_inmueble


class Tipo_usuario(models.Model):
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]
    tipo = models.CharField(choices=CHOICES, unique=True)
    
    def __str__(self):
        return self.tipo

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre_comuna
    
class Region(models.Model):
    nombre_region = models.TextField()
    #como esta hecho para chile podriamos poner un ChoiceField de todas las regiones de chile
    def __str__(self):
        return self.region
    
"""class Region(models.Model):
    CHOICES=[('Arica y Parinacota','Arica y Parinacota'),
            ('Tarapaca','Tarapaca'),
            ('Antofagasta','Antofagasta'),
            ('Atacama','Atacama'),
            ('Coquimbo','Coquimbo'),
            ('Valparaiso','Valparaiso'),
            ('Metropolitana','Metropolitana'),
            ('O Higgins','O Higgins'),
            ('Maule','Maule'),
            ('Nuble','Nuble'),
            ('Biobio','Biobio'),
            ('La Araucania','La Araucania'),
            ('Los Rios','Los Rios'),
            ('Los Lagos','Los Lagos'),
            ('Aysen','Aysen'),
            ('Magallanes','Magallanes')]
    nombre_region = models.CharField(choices=CHOICES)
    
    def __str__(self):
        return self.nombre_region"""

class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey('Tipo_usuario', on_delete=models.CASCADE)
    rut = models.CharField(max_length=9,null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    telefono_personal = models.CharField(max_length=10, null=False, blank=False)
    correo_electronico = models.EmailField()
    
    def __str__(self):
        return self.usuario.username
""" usuario = models.OneToOneField(User, ...)"""


class Tipo_inmueble(models.Model):
    CHOICES =[
        ("Casa","Casa"),
        ("Departamento","Departamento"),
        ("Parcela","Parcela")]
    tipo_inmueble = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.tipo_inmueble
from django.db import models

# Create your models here.
class Usuario(models.Model):
    CHOICES=[("arrendatario","arrendatario"),
            ("arrendador","arrendador")]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=9, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    telefono_personal = models.CharField(max_length=10, null=False, blank=False)
    correo_electronico = models.EmailField()
    
    tipo_de_usuario = models.CharField(max_length=15, choices=CHOICES)

#class Inmueble(models.Model):
    """id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(defaul='')
    m2_construidos = models.IntegerField(null=False, blank=False)
    m2_Totales_o_del_terreno = models.IntegerField(null=False, blank=False)
    cantidad_de_estacionamientos = models.IntegerField(null=False, blank=False)
    cantidad_de_Habitaciones = models.FloatField(null=False, blank=False)
    cantidad_de_banos = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    comuna = models.CharField(max_length=10, null=False, blank=False)
    tipo_de_inmueble_choices ={"casa","departamento","parcela"}
    tipo_de_inmueble = models.CharField(max_length=15, choices=tipo_de_inmueble_choices)
    precio_mensual_de_arriendo = models.IntegerField(null=False, blank=False)
    estado = models.BooleanField(null=False, blank= False) """



#class tipo_usuario(models.Model):
    """id_tipo_user = models.OneToOneField('Usuario', related_name='usuario', on_delete=models.PROTECT)
    nombre_tipo_usuario_choices= {"arrendatario", "arrendador"}
    nombre_tipo_usuario = models.CharField(max_length=15, choices=nombre_tipo_usuario_choices)"""


#class Comuna(models.Model):
    """id_comuna = models.OneToOneField('Inmueble', related_name='inmueble', on_delete=models.PROTECT)
    nombre_comuna = models.CharField(max_length=50, null=False, blank=False)"""


#class Region(models.Model):
    """ id_region = models.OneToOneField('Inmueble', related_name='inmueble', on_delete=models.PROTECT)
    nombre_region = models.CharField(max_length=50, null=False)"""
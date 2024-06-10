from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Inmueble, Contact
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre', 
            'last_name': 'Apellido',
            'email':'Correo electronico', 
            'password1':'Contraseña', 
            'password2':'Repita la contraseña'
        }
    
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('tipo_usuario','rut','direccion','telefono')


class InmuebleForm(forms.ModelForm):
    #id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:

        model = Inmueble
        fields = (
            'id_tipo_inmueble','id_comuna','id_region','image_url', 
            'nombre_inmueble','m2_construidos','m2_totales','cant_de_banos', 
            'cant_de_hab','cant_de_estac','direccion','precio_mensual_de_arriendo','descripcion','estado',
            )   #registra todos los campos disponibles

        labels = {
            'id_tipo_inmueble':'Tipo de Inmueble',
            'id_comuna':'Comuna',
            'id_region':'Region',
            'image_url': 'Imagen',
            'nombre_inmueble':'Nombre Inmueble',
            'm2_construidos':'Metros cuadrados construidos',
            'm2_totales': 'Metros cuadrados totales del terreno', 
            'cant_de_banos':'Numero de Baños', 
            'cant_de_hab':'Numero de habitaciones',
            'cant_de_estac':'Numero de Estacionamientos',
            'precio_mensual_de_arriendo':'precio_mensual_de_arriendo',
            'direccion':'Direccion',
            'descripcion':'Descripcion',
            'estado' : 'Estado',
            }   #registra todos los campos disponibles

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('correo','nombre','mensaje')


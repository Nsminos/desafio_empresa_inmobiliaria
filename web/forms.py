from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Inmueble
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
            'id_inmueble','id_comuna','id_region', 
            'nombre_inmueble', 'm2_construidos', 'cantidad_de_banos', 
            'cantidad_de_Habitaciones','direccion', 'descripcion','estado',
            )   #registra todos los campos disponibles

        labels = {
            'id_inmueble':'Tipo de Inmueble',
            'id_comuna':'Comuna',
            'id_region':'Region', 
            'nombre_inmueble':'Nombre Inmueble',
            'm2_construidos':'Metros cuadrados construidos', 
            'cantidad_de_banos':'Numero de Baños', 
            'cantidad_de_Habitaciones':'Numero de habitaciones',
            'direccion':'Direccion',
            'descripcion':'Descripcion',
            'estado' : 'Estado',
            }   #registra todos los campos disponibles


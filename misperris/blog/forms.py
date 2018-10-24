from django import forms

from .models import Usuario

from .models import Mascotas


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre_completo', 'fecha_nacimiento', 'telefono', 'email', 'region', 'ciudad', 'tipo_vivienda')


class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = ('foto','nombre','raza','descripcion','estado')

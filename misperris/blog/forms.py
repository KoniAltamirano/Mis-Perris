from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre_completo', 'fecha_nacimiento', 'telefono', 'email', 'region', 'ciudad', 'tipo_vivienda')

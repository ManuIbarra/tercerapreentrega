from django import forms
from .models import Alumnos, Maestros, Administracion

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'email', 'edad']

class MaestrosForm(forms.ModelForm):
    class Meta:
        model = Maestros
        fields = ['nombre', 'email', 'asignatura']

class AdministracionForm(forms.ModelForm):
    class Meta:
        model = Administracion
        fields = ['nombre', 'email', 'rol']

"""
importnado modelos para crear los formularios
"""
from django import forms
from .models import Docente, Permiso, Sede


class DocenteForm(forms.ModelForm):
    """
    Formulario docente
    """
    class Meta:
        """
        modelo docente
        """
        model = Docente
        fields = '__all__'


class PermisoForm(forms.ModelForm):
    """
    Formulario Permiso
    """
    class Meta:
        """
        modelo Permiso
        """
        model = Permiso
        fields = ['docente', 'fecha_inicio_permiso',
                  'fecha_fin_permiso', 'descripcion', 'imagen_solicitud']
        widgets = {
            'fecha_inicio_permiso': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            },
                format='%Y-%m-%d'),
            'fecha_fin_permiso': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            },
                format='%Y-%m-%d'),

        }


class SedeForm(forms.ModelForm):
    """
    Formulario Permiso
    """
    class Meta:
        """
        modelo Permiso
        """
        model = Sede
        fields = '__all__'

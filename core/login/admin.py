"""
administrador
"""
from django.contrib import admin
from .models import Sede, Docente, Permiso

# Register your models here.
admin.site.register(Sede)
admin.site.register(Docente)
admin.site.register(Permiso)

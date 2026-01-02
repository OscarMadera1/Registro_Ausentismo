"""
path
"""
from django.urls import path
from login.views import Contacto, CrearSede, EditarSede, EliminarSede, Index, CrearDocente, ListarDocente, EditarDocente, EliminarDocente, ListarPermisos,ver_permiso, CrearPermiso, EditarPermiso, EliminarPermiso, ListarSedes, Reportes


urlpatterns = [
    # index
    path('', Index.as_view(), name='index'),

    # Urls Docente
    path('listar_docente/', ListarDocente.as_view(), name='listar_docente'),
    path('crear_docente/', CrearDocente.as_view(), name='crear_docente'),
    path('editar_docente/<int:pk>',
         EditarDocente.as_view(), name='editar_docente'),
    path('eliminar_docente/<int:pk>',EliminarDocente.as_view(), name='eliminar_docente'),
    # Urls Permisos
    path('listar_permiso/', ListarPermisos.as_view(), name='listar_permiso'),
    path('ver_permiso/<int:pk>', ver_permiso, name='ver_permiso'),
    path('crear_permiso/', CrearPermiso.as_view(), name='crear_permiso'),
    path('editar_permiso/<int:pk>',
         EditarPermiso.as_view(), name='editar_permiso'),
    path('eliminar_permiso/<int:pk>',
         EliminarPermiso.as_view(), name='eliminar_permiso'),

    # Urls Sedes
    path('listar_sedes/', ListarSedes.as_view(), name='listar_sedes'),
    path('crear_sede/', CrearSede.as_view(), name='crear_sede'),
    path('editar_sede/<int:pk>',
         EditarSede.as_view(), name='editar_sede'),
    path('eliminar_sede/<int:pk>',
         EliminarSede.as_view(), name='eliminar_sede'),

    # urls Reportes
    path('reportes/',
         Reportes.as_view(), name='reportes'),

    # urls Contacto
    path('contacto/',
         Contacto, name='contacto'),



]

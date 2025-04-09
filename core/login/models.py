"""
modelos
"""
from django.db import models


class Sede(models.Model):
    """
    Este modo crea las diferentes sedes de la institución educativa
    """
    nombre = models.CharField(max_length=200)

    def __str__(self):
        """
        devolviendo str
        """
        return f"{self.nombre}"

    class Meta:
        """para ordenar las sedes por mombre"""
        ordering = ['nombre']


class Docente(models.Model):
    """
    Este modo crea las diferentes docentes de la institución educativa
    """

    cedula = 'CC'
    cedula_extranjeria = 'CE'
    pasaporte = 'PA'

    tipo_documento = [
        (cedula, 'Cédula de ciudadanía'),
        (cedula_extranjeria, 'Cédula de extranjería'),
        (pasaporte, 'Pasaporte'),
    ]

    documento = models.CharField(
        max_length=2, choices=tipo_documento, default=cedula)
    numero_cedula = models.IntegerField()
    name = models.CharField(max_length=100, verbose_name='Nombres')
    apellido = models.CharField(max_length=100, verbose_name='Apellidos')
    escuela = models.ForeignKey(
        Sede, default="LA MILAGROSA", on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.apellido}"

    class Meta:
        """para ordenar los docentes por nombre"""
        ordering = ['name']


class Permiso(models.Model):
    """
    Este modo crea los diferentes permisos solicitados por los docentes de la institución educativa
    """
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_inicio_permiso = models.DateField()
    fecha_fin_permiso = models.DateField()
    descripcion = models.TextField(null=True, blank=True)
    imagen_solicitud = models.ImageField(
        upload_to='solicitudes/', null=True, blank=True)

    def __str__(self):
        return f"Permiso de {self.docente} - {self.fecha_solicitud}"

    def delete(self, *args, **kwargs):
        if self.imagen_solicitud:
            self.imagen_solicitud.delete(save=False)
        return super().delete(*args, **kwargs)

"""
importando lo necesario
"""
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Docente, Permiso, Sede
from .forms import DocenteForm, PermisoForm, SedeForm
from django.http import HttpResponseRedirect


# Create your views here.

class Index(LoginRequiredMixin, TemplateView):
    """
    pagina inicial que renderiza el dashboard.

    """

    template_name = 'src/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fecha actual
        today = now().date()

        # Cantidad total de permisos
        total_permisos = Permiso.objects.all().count()

        # Permisos solicitados hoy
        permisos_dia = Permiso.objects.filter(fecha_inicio_permiso=today)
        total_permisos_dia = permisos_dia.count()

        # Permisos de la semana actual (del lunes hasta el domingo)
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        permisos_semana = Permiso.objects.filter(
            fecha_inicio_permiso__range=(start_of_week, end_of_week))
        total_permisos_semana = permisos_semana.count()

        # Permisos del mes actual
        permisos_mes = Permiso.objects.filter(
            fecha_inicio_permiso__month=today.month, fecha_inicio_permiso__year=today.year)
        total_permisos_mes = permisos_mes.count()

        # Agrega los datos al contexto
        context['title'] = 'Inicio'
        context['total_permisos'] = total_permisos
        context['total_permisos_dia'] = total_permisos_dia
        context['total_permisos_semana'] = total_permisos_semana
        context['total_permisos_mes'] = total_permisos_mes
        context['permisos_dia'] = permisos_dia
        context['permisos_semana'] = permisos_semana
        context['permisos_mes'] = permisos_mes

        return context


class ListarDocente(ListView):
    """
    lista de docentes
    """
    model = Docente
    paginate_by = 20
    template_name = 'src/listar_docente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado docentes'
        return context


class CrearDocente(CreateView):
    """
    vista para crear docentes
    """
    model = Docente
    form_class = DocenteForm
    template_name = 'src/crear_docente.html'
    success_url = reverse_lazy('listar_docente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear docente'
        return context


class EditarDocente(UpdateView):
    """
    vista para editar docentes
    """
    model = Docente
    form_class = DocenteForm
    template_name = 'src/editar_docente.html'
    success_url = reverse_lazy('listar_docente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar docente'
        return context

class EliminarDocente(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'login/docente_confirm_delete.html'
    success_url = reverse_lazy('listar_docente')

    def post(self, request, *args, **kwargs):
        """
        Sobrescribimos post para evitar que se llame al borrado físico.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        # Lógica de Soft Delete
        self.object.estado = False
        self.object.save()

        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar docente'
        return context

    # views permisos


class ListarPermisos(ListView):
    """
    lista de permisos
    """
    model = Permiso
    paginate_by = 20
    template_name = 'src/listar_permiso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de permisos'
        return context

def ver_permiso(request, pk):
    """
    vista para ver detalle del permiso
    """
    permiso = Permiso.objects.get(pk=pk)
    context = {
        'title': 'Detalle del permiso',
        'permiso': permiso
    }
    return render(request, 'src/ver_permiso.html', context)

class CrearPermiso(CreateView):
    """
    vista para crear permiso
    """
    model = Permiso
    form_class = PermisoForm
    template_name = 'src/crear_permiso.html'
    success_url = reverse_lazy('listar_permiso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear permiso'
        return context


class EditarPermiso(UpdateView):
    """
    vista para editar permiso
    """
    model = Permiso
    form_class = PermisoForm
    template_name = 'src/editar_permiso.html'
    success_url = reverse_lazy('listar_permiso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar permiso'
        return context


class EliminarPermiso(DeleteView):
    """
    Elimnar registro de un permiso
    """
    model = Permiso
    success_url = reverse_lazy('listar_permiso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar permiso'
        return context

# views Sedes


class ListarSedes(ListView):
    """
    lista de sedes
    """
    model = Sede
    paginate_by = 20
    template_name = 'src/listar_sedes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de sedes'
        return context


class CrearSede(CreateView):
    """
    vista para crear sede
    """
    model = Sede
    form_class = SedeForm
    template_name = 'src/crear_sede.html'
    success_url = reverse_lazy('listar_sedes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear sede'
        return context


class EditarSede(UpdateView):
    """
    vista para editar sede
    """
    model = Sede
    form_class = SedeForm
    template_name = 'src/editar_sede.html'
    success_url = reverse_lazy('listar_sedes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar sede'
        return context


class EliminarSede(DeleteView):
    """
    Elimnar registro de una sede
    """
    model = Sede
    success_url = reverse_lazy('listar_sedes')

    def post(self, request, *args, **kwargs):
        """
        Sobrescribimos post para evitar que se llame al borrado físico.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        # Lógica de Soft Delete
        self.object.estado = False
        self.object.save()

        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar sede'
        return context


class Reportes(ListView):
    """
    reportes
    """
    model = Sede
    template_name = 'src/reportes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = 'Reportes'
        return context


def Contacto(request):
    """
    recibe un formulario envia un tiquet a soporte
    """
    context = {}
    context['title'] = 'Contacto'
    context['direccion'] = 'Carrera 13, Tierrarlta'
    context['email'] = 'soporte@mypage.com'
    context['telefono'] = '3115556677'
    context['horario'] = "8:00 A.M - 5:00 P.M"

    return render(request, 'src/contacto.html', context)

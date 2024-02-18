from django.shortcuts import render
from django.views import generic
from . import models
from . import forms 
from .forms import DeporteForm, InstalacionForm

class ListadoView(generic.ListView): 
    model = models.Deporte
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instalaciones'] = models.Instalacion.objects.all() #ya
        context['equipos'] = models.Equipo.objects.all()
        context['jugadores'] = models.Jugador.objects.all()
        context['partidos'] = models.Partido.objects.all()
        return context
    
# TODO: DEPORTES
class ListadoDeportesView(generic.ListView): 
    model = models.Deporte
    template_name = "listado_deportes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context

class CrearDeporteView(generic.CreateView):  # Asegúrate de usar CreateView para crear una nueva instancia del modelo Deporte
    model = models.Deporte
    form_class = DeporteForm  # Especifica el formulario que utilizarás
    template_name = "crear_deporte.html"  # Define el nombre del template
    success_url = "/listado_deportes"  # Define la URL a la que se redirigirá después de crear el deporte

class EliminarDeporteView(generic.DeleteView):
    model = models.Deporte
    template_name = "eliminar_deporte.html"
    success_url = "/listado_deportes"  # Define la URL a la que se redirigirá después de crear el deporte

class EditarDeporteView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = "editar_deporte.html"
    success_url = "/listado_deportes"  # Define la URL a la que se redirigirá después de crear el deporte
    
    
    
# TODO: INSTALACIONES
class ListadoInstalacionesView(generic.ListView): 
    model = models.Instalacion
    template_name = "listado_instalaciones.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context    
    
class CrearInstalacionView(generic.CreateView):  # Asegúrate de usar CreateView para crear una nueva instancia del modelo Deporte
    model = models.Instalacion
    form_class = InstalacionForm  # Especifica el formulario que utilizarás
    template_name = "crear_instalacion.html"  # Define el nombre del template
    success_url = "/listado_instalaciones"  # Define la URL a la que se redirigirá después de crear el deporte

class EliminarInstalacionView(generic.DeleteView):
    model = models.Instalacion
    template_name = "eliminar_instalacion.html"
    success_url = "/listado_instalaciones"  # Define la URL a la que se redirigirá después de crear el deporte

class EditarInstalacionView(generic.UpdateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = "editar_instalacion.html"
    success_url = "/listado_instalaciones"  # Define la URL a la que se redirigirá después de crear el deporte
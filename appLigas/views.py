from django.shortcuts import render
from django.views import generic
from . import models
from . import forms 
from .forms import DeporteForm

class ListadoView(generic.ListView): 
    model = models.Deporte
    template_name = "listado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instalaciones'] = models.Instalacion.objects.all()
        context['equipos'] = models.Equipo.objects.all()
        context['jugadores'] = models.Jugador.objects.all()
        context['partidos'] = models.Partido.objects.all()
        return context

class CrearDeporteView(generic.CreateView):  # Asegúrate de usar CreateView para crear una nueva instancia del modelo Deporte
    model = models.Deporte
    form_class = DeporteForm  # Especifica el formulario que utilizarás
    template_name = "crear_deporte.html"  # Define el nombre del template
    success_url = "/ligas"  # Define la URL a la que se redirigirá después de crear el deporte

class EliminarDeporteView(generic.DeleteView):
    model = models.Deporte
    template_name = "eliminar_deporte.html"
    success_url = "/ligas"  # Define la URL a la que se redirigirá después de crear el deporte

class EditarDeporteView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = "editar_deporte.html"
    success_url = "/ligas"  # Define la URL a la que se redirigirá después de crear el deporte
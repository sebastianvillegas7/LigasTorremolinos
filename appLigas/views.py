from django.shortcuts import render
from django.views import generic
from . import models

class ListadoDeportesView(generic.ListView): 
    model = models.Deporte
    template_name = "listado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instalaciones'] = models.Instalacion.objects.all()
        return context

    
# class ListadoInstalacionView(generic.ListView): 
#     model = models.Instalacion
#     template_name = "listado_instalaciones.html"
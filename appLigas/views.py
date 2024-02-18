from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class ListadoView(generic.ListView): 
    model = models.Deporte
    template_name = "listado.html"
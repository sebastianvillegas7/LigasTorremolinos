from django.shortcuts import render
from django.views import generic
from . import models
from . import forms 
from .forms import DeporteForm, EquipoForm, InstalacionForm, JugadorForm, PartidoForm

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
    
    
    
    # TODO: EQUIPOS
class ListadoEquiposView(generic.ListView): 
    model = models.Equipo
    template_name = "listado_equipos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context    
    
class CrearEquipoView(generic.CreateView):  # Asegúrate de usar CreateView para crear una nueva instancia del modelo Deporte
    model = models.Equipo
    form_class = EquipoForm  # Especifica el formulario que utilizarás
    template_name = "crear_equipo.html"  # Define el nombre del template
    success_url = "/listado_equipos"  # Define la URL a la que se redirigirá después de crear el deporte

class EliminarEquipoView(generic.DeleteView):
    model = models.Equipo
    template_name = "eliminar_equipo.html"
    success_url = "/listado_equipos"  # Define la URL a la que se redirigirá después de crear el deporte

class EditarEquipoView(generic.UpdateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = "editar_equipo.html"
    success_url = "/listado_equipos"  # Define la URL a la que se redirigirá después de crear el deporte
    
def agregar_jugador_equipo(request, pk):
    equipo = models.Equipo.objects.get(id_equipo = pk)
    return render(request, 'info_equipo.html', {'equipo': equipo})
    
def info_equipo(request, pk):
    equipo = models.Equipo.objects.get(id_equipo=pk)
    
    def get_context_data(**kwargs):
        context = {}
        jugadores = models.Jugador.objects.filter(id_equipo=pk)        
        context["equipo"] = equipo
        context["jugadores"] = jugadores
        return context

    context = get_context_data()
    return render(request, 'info_equipo.html', context)    
    
    # TODO: JUGADORES
class ListadoJugadoresView(generic.ListView): 
    model = models.Jugador
    template_name = "listado_jugadores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context  
    
class CrearJugadorView(generic.CreateView):  
    model = models.Jugador
    form_class = JugadorForm  
    template_name = "crear_jugador.html"  
    success_url = "/listado_jugadores" 
    
    # TODO: Si ya recibe el id_equipo como parámetro,
    # TODO: es para agregar un jugador a un equipo en particular,
    # TODO: sino es parar crear un jugador para cualquier equipo.
    def get_initial(self):
        initial = super().get_initial()
        id_equipo = self.kwargs.get('pk')
        if id_equipo:
            initial['id_equipo'] = id_equipo
        return initial    
class EliminarJugadorView(generic.DeleteView):
    model = models.Jugador
    template_name = "eliminar_jugador.html"
    success_url = "/listado_jugadores"
    
class EditarJugadorView(generic.UpdateView):
    model = models.Jugador
    form_class = JugadorForm
    template_name = "editar_jugador.html"
    success_url = "/listado_jugadores"
    
def info_jugador(request, pk):
    jugador = models.Jugador.objects.get(id_jugador = pk)
    
    # def get_context_data(**kwargs):
    #     context = {}
    #     jugadores = models.Jugador.objects.filter(id_equipo=pk)        
        
    #     context["jugadores"] = jugadores
    #     return context

    # context = get_context_data()
    return render(request, 'info_jugador.html', jugador)  
    
    
    # TODO: PARTIDOS
class ListadoPartidosView(generic.ListView): 
    model = models.Partido
    template_name = "listado_partidos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context  
    
class CrearPartidoView(generic.CreateView):  
    model = models.Partido
    form_class = PartidoForm  
    template_name = "crear_partido.html"  
    success_url = "/listado_partidos"
    
class EliminarPartidoView(generic.DeleteView):
    model = models.Partido
    template_name = "eliminar_partido.html"
    success_url = "/listado_partidos"
    
class EditarPartidoView(generic.UpdateView):
    model = models.Partido
    form_class = PartidoForm
    template_name = "editar_partido.html"
    success_url = "/listado_partidos"
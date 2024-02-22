from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from . import models
from .forms import DeporteForm, EquipoForm, InstalacionForm, JugadorForm, PartidoForm

# TODO: HOME
class ListadoView(generic.ListView): 
    model = models.Deporte
    template_name = "home.html"
    # Se obtienen los partidos en el contexto para mostrar las tablas del home
    def get_context_data(self, **kwargs):
        ultimos_partidos_jugados = models.Partido.objects.filter(fecha_hora__lt=timezone.now()).order_by("-fecha_hora")[:5]
        proximos_partidos = models.Partido.objects.filter(fecha_hora__gte=timezone.now()).order_by("fecha_hora")[:5]

        context = super().get_context_data(**kwargs)
        context["ultimos_partidos_jugados"] = ultimos_partidos_jugados
        context["proximos_partidos"] = proximos_partidos
        return context
    
# TODO: DEPORTES
class ListadoDeportesView(generic.ListView): 
    model = models.Deporte
    template_name = "listado_deportes.html"    
    ordering = 'id_deporte'
    
    def get_queryset(self):
        return super().get_queryset().order_by(self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context

class CrearDeporteView(generic.CreateView):  
    model = models.Deporte
    form_class = DeporteForm  
    template_name = "crear_deporte.html"  
    success_url = "/listado_deportes"  

class EliminarDeporteView(generic.DeleteView):
    model = models.Deporte
    template_name = "eliminar_deporte.html"
    success_url = "/listado_deportes"  

class EditarDeporteView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = "editar_deporte.html"
    success_url = "/listado_deportes"  
    
    
    
# TODO: INSTALACIONES
class ListadoInstalacionesView(generic.ListView): 
    model = models.Instalacion
    template_name = "listado_instalaciones.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context    
    
class CrearInstalacionView(generic.CreateView):  
    model = models.Instalacion
    form_class = InstalacionForm  
    template_name = "crear_instalacion.html"  
    success_url = "/listado_instalaciones"  

class EliminarInstalacionView(generic.DeleteView):
    model = models.Instalacion
    template_name = "eliminar_instalacion.html"
    success_url = "/listado_instalaciones"  

class EditarInstalacionView(generic.UpdateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = "editar_instalacion.html"
    success_url = "/listado_instalaciones"  
    
    
    
# TODO: EQUIPOS
class ListadoEquiposView(generic.ListView): 
    model = models.Equipo
    template_name = "listado_equipos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        return context    
    
class CrearEquipoView(generic.CreateView):  
    model = models.Equipo
    form_class = EquipoForm  
    template_name = "crear_equipo.html"  
    success_url = "/listado_equipos"  

class EliminarEquipoView(generic.DeleteView):
    model = models.Equipo
    template_name = "eliminar_equipo.html"
    success_url = "/listado_equipos"  

class EditarEquipoView(generic.UpdateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = "editar_equipo.html"
    success_url = "/listado_equipos"  
    
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
    
    # Si ya recibe el id_equipo como parámetro,
    # es para agregar un jugador a ese equipo en particular,
    # sino es parar crear un jugador para cualquier equipo.
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
    return render(request, 'info_jugador.html', {'jugador': jugador})  
    
    
# TODO: PARTIDOS
class ListadoPartidosView(generic.ListView): 
    model = models.Partido
    template_name = "listado_partidos.html"
    ordering = '-fecha_hora' # se ordena por la fecha de forma descendente
    
    def get_queryset(self):
        return super().get_queryset().order_by(self.ordering)

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
    
def info_partido(request, pk):
    partido = models.Partido.objects.get(id_partido = pk)   
    return render(request, 'info_partido.html', {'partido': partido})  
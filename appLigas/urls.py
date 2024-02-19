from django.urls import path
from . import views

app_name="appLigas"
urlpatterns = [
    path('', views.ListadoView.as_view(), name="home"),   
    path('home/', views.ListadoView.as_view(), name="home"),        
    # DEPORTES
    path('listado_deportes/', views.ListadoDeportesView.as_view(), name="listado_deportes"),
    path('crear_deporte/', views.CrearDeporteView.as_view(), name="crear_deporte"),
    path('editar_deporte/<int:pk>', views.EditarDeporteView.as_view(), name="editar_deporte"),
    path('eliminar_deporte/<int:pk>', views.EliminarDeporteView.as_view(), name="eliminar_deporte"),
    # INSTALACIONES
    path('listado_instalaciones/', views.ListadoInstalacionesView.as_view(), name="listado_instalaciones"),
    path('crear_instalacion/', views.CrearInstalacionView.as_view(), name="crear_instalacion"),
    path('editar_instalacion/<int:pk>', views.EditarInstalacionView.as_view(), name="editar_instalacion"),
    path('eliminar_instalacion/<int:pk>', views.EliminarInstalacionView.as_view(), name="eliminar_instalacion"),
    # EQUIPOS
    path('listado_equipos/', views.ListadoEquiposView.as_view(), name="listado_equipos"),
    path('crear_equipo/', views.CrearEquipoView.as_view(), name="crear_equipo"),
    path('editar_equipo/<int:pk>', views.EditarEquipoView.as_view(), name="editar_equipo"),
    path('eliminar_equipo/<int:pk>', views.EliminarEquipoView.as_view(), name="eliminar_equipo"),
    path('ligas/info_equipo/<int:pk>', views.info_equipo, name="info_equipo"),
    # JUGADORES
    path('listado_jugadores/', views.ListadoJugadoresView.as_view(), name="listado_jugadores"),
    path('crear_jugador/', views.CrearJugadorView.as_view(), name="crear_jugador"),
    path('editar_jugador/<int:pk>', views.EditarJugadorView.as_view(), name="editar_jugador"),
    path('eliminar_jugador/<int:pk>', views.EliminarJugadorView.as_view(), name="eliminar_jugador"),
    # PARTIDOS
    path('listado_partidos/', views.ListadoPartidosView.as_view(), name="listado_partidos"),
    path('crear_partido/', views.CrearPartidoView.as_view(), name="crear_partido"),
    path('editar_partido/<int:pk>', views.EditarPartidoView.as_view(), name="editar_partido"),
    path('eliminar_partido/<int:pk>', views.EliminarPartidoView.as_view(), name="eliminar_partido"),    
]

from django.contrib import admin

from .models import Deporte, Instalacion

# Register your models here.
@admin.register(Deporte)
class DeportesAdmin(admin.ModelAdmin):
    model = Deporte
    list_display = ["id_deporte", "nombre"]
    search_fields = ["id_deporte", "nombre"]

@admin.register(Instalacion)
class InstalacionAdmin(admin.ModelAdmin):
    model = Instalacion
    list_display = ["id_instalacion", "nombre", "direccion", "iluminacion", "cubierta"]
    search_fields = ["id_instalacion", "nombre"]
    
# @admin.register(Equipo)
# class EquipoAdmin(admin.ModelAdmin):
#     model = Equipo
#     list_display = ["id_equipo", "nombre", "id_deporte", "equipacion_principal", "equipacion_suplente", "contacto", "telefono", "email"]
#     search_fields = ["id_equipo", "nombre"]

# @admin.register(Jugador)
# class JugadorAdmin(admin.ModelAdmin):
#     model = Jugador
#     list_display = ["id_jugador", "nombre", "apellido1", "apellido2", "id_equipo", "dorsal", "fecha_nacimiento", "altura", "peso", "telefono"]
#     search_fields = ["id_jugador", "nombre"]

# @admin.register(Partido)
# class PartidoAdmin(admin.ModelAdmin):
#     model = Partido
#     list_display = ["id_partido", "id_deporte", "fecha_hora", "id_instalacion", "id_local_equipo", "id_visitante_equipo", "puntos_local", "puntos_visitante", "observaciones"]
#     search_fields = ["id_partido", "nombre"]
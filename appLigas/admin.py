from django.contrib import admin

from .models import Deporte, Equipo, Instalacion, Jugador, Partido

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
    
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    model = Equipo
    list_display = ["id_equipo", "nombre", "id_deporte", "equipacion_principal", "equipacion_suplente", "contacto", "telefono", "email"]
    search_fields = ["id_equipo", "nombre"]

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    model = Jugador
    list_display = ["id_jugador", "nombre", "apellido1", "apellido2", "equipo_id", "dorsal", "fecha_nacimiento", "altura", "peso", "telefono"]
    search_fields = ["id_jugador", "nombre"]

    def equipo_id(self, obj):
        return obj.id_equipo.id_equipo

    equipo_id.short_description = 'ID Equipo'

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    model = Partido
    list_display = ["id_partido", "deporte_id", "fecha_hora", "instalacion_id", "equipo_local_id", "equipo_visitante_id", "puntos_local", "puntos_visitante", "observaciones"]
    search_fields = ["id_partido"]

    def deporte_id(self, obj):
        return obj.id_deporte.id_deporte
    
    def instalacion_id(self, obj):
        return obj.id_instalacion.id_instalacion
    
    def equipo_local_id(self, obj):
        return obj.id_equipo_local.id_equipo

    def equipo_visitante_id(self, obj):
        return obj.id_equipo_visitante.id_equipo

    equipo_local_id.short_description = 'ID Equipo Local'
    equipo_visitante_id.short_description = 'ID Equipo Visitante'

    
# @admin.register(Jugador)
# class JugadorAdmin(admin.ModelAdmin):
#     model = Jugador
#     list_display = ["id_jugador", "nombre", "apellido1", "apellido2", "id_equipo", "dorsal", "fecha_nacimiento", "altura", "peso", "telefono"]
#     search_fields = ["id_jugador", "nombre"]
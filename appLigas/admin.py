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
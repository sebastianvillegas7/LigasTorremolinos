from django.contrib import admin

from .models import Deporte

# Register your models here.
@admin.register(Deporte)
class DatosAdmin(admin.ModelAdmin):
    model = Deporte
    list_display = ["id_deporte", "nombre"]
    search_fields = ["id_deporte", "nombre"]


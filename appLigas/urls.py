from django.urls import path
from . import views

app_name="appLigas"
urlpatterns = [
    path('', views.ListadoView.as_view(), name="listado"),    
    path('crear_deporte/', views.CrearDeporteView.as_view(), name="crear_deporte"),
    path('editar_deporte/<int:pk>', views.EditarDeporteView.as_view(), name="editar_deporte"),
    path('eliminar_deporte/<int:pk>', views.EliminarDeporteView.as_view(), name="eliminar_deporte"),
]
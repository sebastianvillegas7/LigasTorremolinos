from django.urls import path
from . import views

app_name="appLigas"
urlpatterns = [
    path('', views.ListadoView.as_view(), name="listado"),
    path('listado/', views.ListadoView.as_view(), name="listado"),
    # path('detalles/<int:pk>',views.DetalleView.as_view(), name="nombre"),
    # path('update/<int:pk>',views.UpdateView.as_view(), name="update"),
    # path('delete/<int:pk>',views.DeleteView.as_view(), name="delete"),
]
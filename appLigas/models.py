from django.db import models

# Create your models here.
# Modelo Deporte
class Deporte(models.Model):
    id_deporte = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)        
        
    class Meta:        
        verbose_name_plural = "Deportes"
        db_table = "deportes"
        def __str__(self):
            return f"{self.id_deporte} {self.nombre}"
        
# Modelo Instalacion
class Instalacion(models.Model):
    id_instalacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 50)      
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)
    class Meta:        
        verbose_name_plural = "Instalaciones"
        db_table = "instalaciones"
        def __str__(self):
            return f"{self.id_instalacion} {self.nombre} {self.nombre} {self.direccion} {self.iluminacion} {self.cubierta}"
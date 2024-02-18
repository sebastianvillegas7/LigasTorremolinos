from django.db import models

# Create your models here.
class Deporte(models.Model):
    id_deporte = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)        
        
    class Meta:        
        verbose_name_plural = "Deportes"
        db_table = "deportes"
        def __str__(self):
            return f"{self.id_deporte} {self.nombre}"
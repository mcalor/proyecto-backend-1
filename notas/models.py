from django.db import models
from django.utils import timezone

class Nota(models.Model):
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    creada = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-creada']
        
    def __str__(self):
        return self.titulo
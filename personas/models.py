from django.db import models
from django.urls import reverse
from oficinas.models import Oficina

class Persona(models.Model):
    apellido = models.CharField(max_length=100, default='Desconocido')
    nombre = models.CharField(max_length=100, default='Desconocido')
    edad = models.IntegerField(default=0)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name='personas', verbose_name="Oficina")
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    def get_absolute_url(self):
        return reverse('personas:detalle', kwargs={'pk': self.pk})
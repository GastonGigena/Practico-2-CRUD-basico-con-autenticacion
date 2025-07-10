from django.db import models
from django.urls import reverse

class Oficina(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    nombre_corto = models.CharField(max_length=20, verbose_name="Nombre Corto")
    
    class Meta:
        verbose_name = "Oficina"
        verbose_name_plural = "Oficinas"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('oficinas:detalle', kwargs={'pk': self.pk})
from django.db import models
from .hotel import Categoria

class DisponibilidadCategoria(models.Model):
    fecha = models.DateField()
    capacidad_disponible = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='disponibilidades')

    def __str__(self):
        return f"{self.categoria.nombre} - {self.fecha} ({self.capacidad_disponible})"

    class Meta:
        verbose_name = "Disponibilidad Categoría"
        verbose_name_plural = "Disponibilidad Categorías"

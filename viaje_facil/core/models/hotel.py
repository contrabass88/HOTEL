from django.db import models
from .ubicacion import Direccion

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estrellas = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to='hoteles/', null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)
    precio = models.FloatField(default=0.00)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class HotelCategoria(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='categorias_hotel')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hotel Categoría"
        verbose_name_plural = "Hoteles Categorías"
        unique_together = ('hotel', 'categoria')

    def __str__(self):
        return f"{self.hotel} - {self.categoria}"
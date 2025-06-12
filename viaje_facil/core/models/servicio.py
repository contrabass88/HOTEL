from django.db import models
from .hotel import Hotel, Categoria

class ServicioHotel(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Servicio Hotel"
        verbose_name_plural = "Servicios Hoteles"


class HotelServicio(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioHotel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hotel Servicio"
        verbose_name_plural = "Hoteles Servicios"
        unique_together = ('hotel', 'servicio')

    def __str__(self):
        return f"{self.hotel} - {self.servicio}"


class ServicioCategoriaHabitacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Servicio Categoría Habitación"
        verbose_name_plural = "Servicios Categorías Habitaciones"


class CategoriaServicio(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioCategoriaHabitacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Categoría Servicio"
        verbose_name_plural = "Categorías Servicio"
        unique_together = ('categoria', 'servicio')

    def __str__(self):
        return f"{self.categoria} - {self.servicio}"

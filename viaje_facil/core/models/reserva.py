from django.db import models
from .viajero import Viajero
from .hotel import Categoria

class EstadoReserva(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Estado Reserva"
        verbose_name_plural = "Estados Reservas"


class ReservaHotel(models.Model):
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_reserva = models.DateField()
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id} - {self.viajero}"

    class Meta:
        verbose_name = "Reserva Hotel"
        verbose_name_plural = "Reservas Hoteles"


class ReservaHotelDetalle(models.Model):
    cantidad_habitaciones = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    reserva = models.ForeignKey(ReservaHotel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reserva} - {self.categoria} - {self.cantidad_habitaciones} hab."

    def save(self, *args, **kwargs):
        self.sub_total = self.precio_unitario * self.cantidad_habitaciones
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Reserva Hotel Detalle"
        verbose_name_plural = "Reservas Hoteles Detalles"

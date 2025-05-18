from django.contrib import admin
from .models import (
    Pais, Provincia, Localidad, Direccion,
    Viajero, Hotel, Categoria,
    HotelCategoria, ServicioHotel, HotelServicio,
    ServicioCategoriaHabitacion, CategoriaServicio,
    DisponibilidadCategoria,
    EstadoReserva, ReservaHotel, ReservaHotelDetalle
)

# =============================
# Ubicación
# =============================

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre',)

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia')
    search_fields = ('nombre',)

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'cod_postal', 'localidad')
    search_fields = ('calle', 'numero')


# =============================
# Viajero
# =============================

@admin.register(Viajero)
class ViajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')


# =============================
# Hoteles
# =============================

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'estrellas')
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)

@admin.register(HotelCategoria)
class HotelCategoriaAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'categoria')
    autocomplete_fields = ['hotel', 'categoria']


# =============================
# Servicios
# =============================

@admin.register(ServicioHotel)
class ServicioHotelAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

@admin.register(HotelServicio)
class HotelServicioAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'servicio')
    autocomplete_fields = ['hotel', 'servicio']

@admin.register(ServicioCategoriaHabitacion)
class ServicioCategoriaHabitacionAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

@admin.register(CategoriaServicio)
class CategoriaServicioAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'servicio')
    autocomplete_fields = ['categoria', 'servicio']


# =============================
# Disponibilidad
# =============================

@admin.register(DisponibilidadCategoria)
class DisponibilidadCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'fecha', 'capacidad_disponible')
    list_filter = ('fecha',)
    autocomplete_fields = ['categoria']


# =============================
# Reservas
# =============================

@admin.register(EstadoReserva)
class EstadoReservaAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)

@admin.register(ReservaHotel)
class ReservaHotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'viajero', 'fecha_reserva', 'fecha_ingreso', 'fecha_egreso', 'monto_total', 'estado')
    search_fields = ('viajero__nombre', 'viajero__apellido')
    autocomplete_fields = ['viajero', 'estado']

@admin.register(ReservaHotelDetalle)
class ReservaHotelDetalleAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'categoria', 'cantidad_habitaciones', 'precio_unitario', 'sub_total')
    autocomplete_fields = ['reserva', 'categoria']

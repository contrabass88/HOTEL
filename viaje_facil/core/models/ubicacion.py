from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='provincias')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"


class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='localidades')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cod_postal = models.CharField(max_length=10)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='direcciones')

    def __str__(self):
        return f"{self.calle} {self.numero}, CP {self.cod_postal}"

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"

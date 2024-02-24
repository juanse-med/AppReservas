from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    def duracion_estancia(self):
        return (self.fecha_salida - self.fecha_entrada).days

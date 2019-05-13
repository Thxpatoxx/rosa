from django.db import models
from django.utils import timezone


class Implementodep(models.Model):
    folio = models.PositiveIntegerField()
    ESTADO = (
        ('NO_DISPONIBLE','NO_DISPONIBLE'),
        ('DISPONIBLE','DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    IMPLEMENTO = (
        ('PALETAS','PALETAS'),
        ('PELOTA_PINPONG','PELOTA_PINPONG'),
        ('PELOTA_FOOTBALL','PELOTA_FOOTBALL'),
        ('PELOTA_BASCKETBALL','PELOTA_BASCKETBALL'),
        ('CANCHA','CANCHA'),
    )
    implemento = models.CharField(max_length=80,choices=IMPLEMENTO,default='PALETAS')
class Factura(models.Model):
    horas = models.PositiveIntegerField()
    pago = models.PositiveIntegerField()


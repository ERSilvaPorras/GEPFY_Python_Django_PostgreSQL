from django.db import models

# Create your models here.
class Service(models.Model):
    empresa = models.CharField(max_length=30)
    logo = models.ImageField()
    estado = models.CharField(max_length=20)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    monto_total = models.FloatField()
    fecha_pago = models.DateField()
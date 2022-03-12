import email
from django.db import models

# Register
class UserProfile(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.PositiveBigIntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    altura = models.PositiveIntegerField()
    CP = models.PositiveSmallIntegerField()
# Login

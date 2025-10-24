from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)


from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Profesor(Alumno):
    turno = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Profesores"
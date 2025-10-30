from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    inscriptos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    inscriptos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

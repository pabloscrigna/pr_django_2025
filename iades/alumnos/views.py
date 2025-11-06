from django.shortcuts import HttpResponse

# Create your views here.
from .models import Alumno


def alumnos_vista(request):
    return HttpResponse("En construccion")


def alumnos_agregar(request):

    nombre = "Micaela"
    edad = 20

    alumno = Alumno()
    alumno.nombre = nombre
    alumno.edad = edad

    alumno.save()

    return HttpResponse(f"Se creo el usuario {alumno.nombre} exitosamente")


def alumnos_listar(request):

    alumnos = Alumno.objects.all()

    for alumno in alumnos:
        print(alumno.nombre)

    return HttpResponse(f"Se listaron los alumnos exitosamente")
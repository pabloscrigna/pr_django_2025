from django.urls import path

from .views import alumnos_vista, alumnos_agregar, alumnos_listar

urlpatterns = [
    path("listar/", alumnos_listar),
    path("agregar/", alumnos_agregar),
    path("eliminar/", alumnos_vista),
    path("", alumnos_vista)
]

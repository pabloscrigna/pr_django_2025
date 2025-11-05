from django.urls import path

from .views import alumnos_vista, alumnos_agregar

urlpatterns = [
    path("listar/", alumnos_vista),
    path("agregar/", alumnos_agregar),
    path("eliminar/", alumnos_vista),
    path("", alumnos_vista)
]

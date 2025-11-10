from django.urls import path

from .views import cursos_agregar, cursos_listar, curso_lista

urlpatterns = [
    path("listar/", cursos_listar),
    path("listar/<int:id>/", curso_lista),
    path("agregar/", cursos_agregar),
    # path("eliminar/", cursos_vista),
    # path("", cursos_vista)
]
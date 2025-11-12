from django.urls import path

from .views import cursos_agregar, cursos_listar, curso_lista, cursos_vista

urlpatterns = [
    path("listar/", cursos_listar),
    path("listar/<int:id>/", curso_lista),
    path("agregar/", cursos_agregar),
    path("", cursos_vista, name="Cursos")
]
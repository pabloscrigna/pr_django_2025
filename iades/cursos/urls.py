from django.urls import path

from .views import listar_cursos, busca_curso, vista_inicio, crear_curso, crear_instructor

urlpatterns = [
    path("listar/", listar_cursos, name="ListarCursos"),
    path("listar/<int:id>/", busca_curso, name="BuscarCurso"),
    # path("agregar/", agregar_curso, name="AgregarCurso"),
    path("inicio/", vista_inicio, name="Inicio"),
    path("curso-formulario", crear_curso, name="CrearCurso"),
    path("crear-instructor", crear_instructor, name="CrearInstructor")
]

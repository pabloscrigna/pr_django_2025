from django.shortcuts import render

# Create your views here.
from cursos.models import Curso


def cursos_agregar(request):
    pass


def cursos_listar(request):

    cursos = Curso.objects.all()

    return render(request, "listar_cursos.html", {"cursos": cursos})


def curso_lista(request, id):

    curso = Curso.objects.get(id=id)

    return render(request, "lista_curso.html", {"curso": curso})


def cursos_vista(request):
    print("Cursos vista")
    return render(request, "index.html")
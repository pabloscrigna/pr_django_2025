from django.shortcuts import render

# Create your views here.
from cursos.models import Curso

from cursos.forms import InstructorForm

def cursos_agregar(request):
    pass


def listar_cursos(request):

    print("Ingreso en la vista listar cursos")

    cursos = Curso.objects.all()

    return render(request, "listar_cursos.html", {"cursos": cursos})


def busca_curso(request, id):

    curso = Curso.objects.get(id=id)

    return render(request, "busca_curso.html", {"cursos": curso})


def vista_inicio(request):
    print("Cursos vista")
    return render(request, "index.html")


# def agregar_curso(request):
# 
#     return render(request, "agregar_curso.html")


def crear_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["nombre"]
        inscriptos_curso = request.POST["inscriptos"]

        curso = Curso(nombre=nombre_curso, inscriptos=inscriptos_curso)
        curso.save()

        return render(request, "index.html")
    
    return render(request, "agregar_curso.html")


def crear_instructor(request):

    if request.method == "POST":

        return render(request, "index.html")
    
    form_instructor = InstructorForm()
    return render(request, "crear_instructor.html", {"form_instructor": form_instructor})


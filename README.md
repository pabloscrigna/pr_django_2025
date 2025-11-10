# Proyecto en django

# Crear entorno virtual

$python3.12 -m venv .venv

# Activar el entorno virtual

$source .venv/bin/activate

# Instalamos las dependencias

$ pip install requirements.txt

# Crear un proyecto en django

$django-admin startproject <project_name>
$django-admin startproject iades

# Levantamos el servidor de desarrollo

$ python manage.py runserver

# probar la pagina de prueba

$ http://localhost:8000

# Crear una applicacion

$ python manage.py startapp alumnos

# Configurar la DB en settings de django

# Creamos un modelo en la app alumnos

models.py

# Dar de alta la app en django

Configurar la app alumnos en INSTALLED_APPS

# Hicimos las migraciones para ese modelo

$ python manage.py makemigrations

# Corrimos las migraciones

$ python manage.py migrate

# Ver las migraciones

$ python manage.py showmigrations

# Crear el superuser

$ python manage.py createsuperuser

## Flujo de una peticion a una pagina

1. Levantar el servidor de desarrollo

python manage.py runserver

2. Acceder a la url

Navegador: http://localhost:8000/admin
Navegador: http://127.0.0.1:8000/alumnos/noche

localhost == 127.0.0.1

#. analisis de la URL

http://127.0.0.1:8000 --> Direccion del servidor

/alumnos/noche ---> ROOT_URLCONF

Encuentra la ruta a /alumnos en iades.urls path("alumnos/", include("alumnos.urls")),

Y sigue buscando en alumnos.urls ---> analiza el resto de la url y consume la vista correspondiente.

# ORM

$ python manage.py shell

# Para el modelo Curso

# Buscar todos los registros de un modelo

Curso.objects.all() ---> Queryset

# Buscar registros por valor de un campo

Curso.objects.filter(nombre="valor") ---> Queryset

# Buscar registros por valor de un campo - solo el primero

Curso.objects.filter(nombre="valor").first() ---> hace la consulta, tiene el valor

# Buscar por id

Curso.objects.get(id=3) --> hace la consulta tiene el valor

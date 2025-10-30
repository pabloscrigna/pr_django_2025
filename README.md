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
